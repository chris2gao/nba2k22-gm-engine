"""Immutable fact packets with caller-supplied, separately validated analysis."""
from copy import deepcopy
import re
from uuid import uuid4
from .analysis_metrics import metrics, interval, temporal_links, VERSION
from .workbench_common import now, reject_authority, require, text_required

ANNOTATIONS = ('diagnosis','talent_gap_evidence','utilization_hypothesis','internal_levers',
               'market_clues','strategy_change_signals','alternatives_explanations')


def prepare(inputs, season, node_type, previous=None, finance=None, strategies=(), run_id=None,
            history_context=None, code_commit=None):
    if not re.fullmatch(r'\d{4}-\d{4}', season or '') or int(season[-4:])!=int(season[:4])+1 or node_type not in ('BOOTSTRAP','SEASON_INITIALIZATION','CHECKPOINT'):
        raise ValueError('EXPLICIT_SEASON_AND_NODE_TYPE_REQUIRED')
    b = deepcopy(inputs['source_binding'])
    context = dict(season=season, node_type=node_type, history_branch_context=history_context,
                   source_context=deepcopy(inputs.get('context',{})))
    comparable = bool(previous and history_context and previous['source_binding']['career_id']==b['career_id']
        and previous.get('history_branch_context')==history_context and previous.get('season')==season
        and previous['source_binding'].get('game_date','') < b.get('game_date',''))
    if finance and finance['source_binding']['career_id'] != b['career_id']:
        raise ValueError('FINANCE_CAREER_MISMATCH')
    for s in strategies:
        if s['career_id'] != b['career_id']:
            raise ValueError('STRATEGY_CAREER_MISMATCH')
    teams = []
    for t in inputs['teams']:
        tid = t['team_id']
        stats = next((s for s in inputs['team_stats'] if s['team_id']==tid), None)
        totals = deepcopy(stats['totals']) if stats else {}
        stat_ref = 'team_stats:'+str(tid)
        # Captured TEAM_STATS uses the ending year (2022 for 2021-2022).
        season_matches = bool(stats and stats['season_year']==int(season[-4:]))
        players = deepcopy([p for p in inputs['players'] if p['team_id']==tid])
        for p in players:
            p['evidence_ref'] = 'player:'+p['identity']
            p['identity_scope'] = 'BATCH_LOCAL_NOT_PERMANENT'
            p['decoded_attributes'] = {k:v.get('value') for k,v in (p.get('attributes') or {}).items() if isinstance(v,dict)}
            p['unknowns'] = ['IN_GAME_OVR_AGE_AND_CONTRACT_CLASSIFICATION_NOT_CERTIFIED']
        old = next((s for s in previous['team_stats'] if s['team_id']==tid), None) if previous else None
        local_comparable = comparable and season_matches and bool(old and stats and old['season_year']==stats['season_year'])
        team = dict(team_id=tid, team=t['team'], observed_team=t,
            observed_performance=dict(cumulative=metrics(totals if season_matches else {}, stat_ref), raw_totals=totals,
                interval=interval(totals, old['totals'] if old else {}, local_comparable),
                comparability='EXPLICIT_SAME_CONTEXT_ORDERED' if local_comparable else 'NOT_ESTABLISHED'),
            player_supply=dict(source_identity_set=sorted(p['identity'] for p in players), players=players,
                coverage='COMPLETE_SOURCE_ROSTER_NOT_ASSESSED',
                temporal_links=temporal_links(players, previous['players']) if previous else []),
            staff_context=dict(rows=[s for s in inputs['staff'] if s['team_id']==tid],
                appointable_ui_roles=6, native_team_role_slots=8, appointment_effect='UNKNOWN'),
            coaching_context=dict(defaults=[c for c in inputs['coaching'] if c['team_id']==tid], overall=[c for c in inputs['defense'] if c['team_id']==tid]),
            financial_and_assets=dict(finance=[f for f in inputs['finance'] if f['team_id']==tid], picks=[p for p in inputs['picks'] if p['team_id']==tid],
                finance_run_id=finance['run_id'] if finance else None, signing_capacity=None),
            strategy_refs=[dict(state_id=s['state_id'], revision=s['revision'], status=s['status'],
                alignment='SAME_BATCH' if s['source_binding']['batch_id']==b['batch_id'] else 'REFERENCE_ONLY') for s in strategies if s['team_id']==tid],
            annotations=None, source_refs=['team:'+str(tid),stat_ref],
            issues=[] if stats else [dict(code='TEAM_STATS_MISSING', effect='UNKNOWN_METRIC')])
        if not team['staff_context']['rows']:
            team['issues'].append(dict(code='STAFF_SOURCE_GAP', effect='REVIEW_ONLY'))
        if stats and not season_matches:
            team['issues'].append(dict(code='SEASON_ANCHOR_MISMATCH',effect='UNKNOWN_METRIC'))
        for m in team['observed_performance']['interval']['metrics'].values():
            m['input_refs']=[ref.replace('interval:', 'interval:'+str(tid)+':',1) for ref in m['input_refs']]
        teams.append(team)
    ids = [t['team_id'] for t in teams]
    identities = [p['identity'] for t in teams for p in t['player_supply']['players']]
    if len(ids)!=len(set(ids)) or len(identities)!=len(set(identities)) or set(identities)!={p['identity'] for p in inputs['players']}:
        raise ValueError('SOURCE_COVERAGE_IDENTITY_CONFLICT')
    return dict(analysis_run_id=run_id or uuid4().hex, revision=1, created_at=now(), sealed_at=None,
        source_binding=b, previous_source_binding=deepcopy(previous['source_binding']) if previous else None,
        supersedes_run_id=None,
        context=context, code_commit=code_commit, calculation_version=VERSION, knowledge_version='M2_KNOWLEDGE_V1',
        status='DRAFT_FACTS', authority='ANALYSIS_ONLY', execution_authorized=False,
        expected_team_ids=sorted(ids), read_team_ids=sorted(ids), prepared_team_ids=sorted(ids), annotated_team_ids=[],
        source_access=deepcopy(inputs['source_access']), method_registry=dict(version=VERSION,
            formula_source='gm_core.analysis_metrics', possessions='UNKNOWN', identity='BATCH_LOCAL'),
        finance_run_id=finance['run_id'] if finance else None,
        finance_alignment='NOT_LINKED' if not finance else ('SAME_BATCH' if finance['source_binding']['batch_id']==b['batch_id'] else 'DIFFERENT_BATCH_REVIEW_REQUIRED'),
        issue_index=[dict(team_id=t['team_id'], **i) for t in teams for i in t['issues']], teams=teams)


def team(run, key):
    rows = [t for t in run['teams'] if str(t['team_id'])==str(key) or t['team']==str(key).upper()]
    if len(rows)!=1:
        raise ValueError('TEAM_NOT_FOUND')
    return rows[0]


def evidence(run, ref):
    # Only values recoverable from this immutable packet are accepted as fact refs.
    if ref in run.get('reference_evidence',{}):
        return deepcopy(run['reference_evidence'][ref])
    if ref in run.get('supplemental_evidence',{}):
        return deepcopy(run['supplemental_evidence'][ref])
    for t in run['teams']:
        if ref=='team:'+str(t['team_id']):
            value=t['observed_team']
            break
        prefix='team_stats:'+str(t['team_id'])
        if ref==prefix or ref.startswith(prefix+':'):
            value=t['observed_performance']['raw_totals']
            if ref!=prefix:
                value=value.get(ref[len(prefix)+1:])
            break
        prefix='metric:'+str(t['team_id'])+':'
        if ref.startswith(prefix) and ref[len(prefix):] in t['observed_performance']['cumulative']:
            value=t['observed_performance']['cumulative'][ref[len(prefix):]]
            break
        prefix='interval:'+str(t['team_id'])+':'
        if ref.startswith(prefix):
            value=t['observed_performance']['interval']['counters'].get(ref[len(prefix):])
            break
        if ref=='coaching:'+str(t['team_id']):
            value=t['coaching_context']['defaults']
            break
        if ref=='finance:'+str(t['team_id']):
            value=t['financial_and_assets']['finance']
            break
        matches=[s for s in t['staff_context']['rows'] if isinstance(s.get('identity'),str) and ref=='staff:'+s['identity']]
        if matches:
            value=matches[0]
            break
        matches=[s for s in t['coaching_context']['overall'] if ref=='defense:'+str(t['team_id'])+':'+str(s['opponent_team_id'])]
        if matches:
            value=matches[0]
            break
        matches=[p for p in t['financial_and_assets']['picks'] if isinstance(p.get('asset_id'),str) and ref=='pick:'+p['asset_id']]
        if matches:
            value=matches[0]
            break
        matches=[p for p in t['player_supply']['players'] if ref==p['evidence_ref']]
        if matches:
            p=matches[0]
            value={k:p[k] for k in ('identity','name','team_id','position','salary','years_left','decoded_attributes','season_totals')}
            break
    else:
        raise ValueError('UNKNOWN_PACKET_EVIDENCE_REF:'+str(ref))
    return dict(ref_id=ref, kind='METRIC' if ref.startswith('metric:') else 'FACT',
        binding=run['source_binding'], run_id=run['analysis_run_id'], value=value, availability='UNKNOWN' if value in (None,{},[]) else 'AVAILABLE', method_version=VERSION)


def validate_refs(run, refs):
    if not isinstance(refs, list) or not refs:
        raise ValueError('EVIDENCE_REFS_REQUIRED')
    for ref in refs:
        evidence(run, ref)


def annotate(run, payload):
    reject_authority(payload)
    if run['sealed_at']:
        raise ValueError('SEALED_ANALYSIS_IMMUTABLE')
    require(payload, ('teams',))
    seen=set()
    for item in payload['teams']:
        require(item, ('team_id','annotations','evidence_refs'))
        if set(item)-{'team_id','annotations','evidence_refs'} or item['team_id'] in seen:
            raise ValueError('ANNOTATION_ONLY_UNIQUE_TEAMS')
        seen.add(item['team_id'])
        t=team(run,item['team_id'])
        require(item['annotations'], ANNOTATIONS)
        for key in ANNOTATIONS:
            v=item['annotations'][key]
            if not isinstance(v,(str,list,dict)) or not v:
                raise ValueError('ANNOTATION_CONCLUSION_OR_REASONED_GAP_REQUIRED:'+key)
        validate_refs(run,item['evidence_refs'])
        t['annotations']=deepcopy(item)
    run['annotated_team_ids']=sorted(t['team_id'] for t in run['teams'] if t['annotations'])
    run['status']='DRAFT_ANNOTATED'
    return run


def seal(run):
    if run['sealed_at']:
        raise ValueError('SEALED_ANALYSIS_IMMUTABLE')
    complete = len(run['expected_team_ids'])==30 and set(run['annotated_team_ids'])==set(run['expected_team_ids'])
    for t in run['teams']:
        ps=t['player_supply']
        if sorted(p['identity'] for p in ps['players']) != ps['source_identity_set']:
            raise ValueError('ROSTER_COVERAGE_MISMATCH')
    run['status']='SEALED_COMPLETE' if complete else 'SEALED_PARTIAL'
    run['sealed_at']=now()
    return run


def summary(run):
    return {**{k:run[k] for k in ('analysis_run_id','revision','status','source_binding','context','sealed_at','finance_alignment')},
        'authority':'ANALYSIS_ONLY','execution_authorized':False,
        'teams':[dict(team_id=t['team_id'], team=t['team'], roster_count=len(t['player_supply']['source_identity_set']),
            annotation_status='ANNOTATED' if t['annotations'] else 'NOT_ASSESSED', issues=t['issues']) for t in run['teams']],
        'access_summary':[dict(entity=a['entity'], read_count=a['read_count'], status=a['status']) for a in run['source_access']]}
