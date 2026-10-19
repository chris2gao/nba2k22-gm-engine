"""Pure offline business handoffs. No executor imports or process access."""
from copy import deepcopy
from .coaching_batch import propose_batch, validate_batch, normalize_freelance
from coach_codec import load_profile
from .finance_scenarios import compare


def generate(decision, selected, analysis, finance=None, coach_snapshot=None):
    items, research, generated = [], [], []
    research.extend(dict(item_id=r['research_id'],kind='RESEARCH_ALTERNATIVE',team_id=r['team_id'],
        alternative_revision=r['alternative_revision'],alternative=r['alternative'],executor_readiness='RESEARCH_ONLY',
        approval_status='NOT_GRANTED',execution_authorized=False) for r in selected.get('research',[]))
    moves=[]
    issues=selected['issues']
    bad_offers={i.get('object_id') for i in issues if i['code']=='DEPENDENCY_UNSUPPORTED'}
    overlapping={i['team_id'] for i in issues if i['code']=='DEPENDENCY_UNSUPPORTED_SAME_TEAM_TRADES'}
    for offer in selected['offers']:
        blocked=offer['offer_id'] in bad_offers or bool(set(offer['team_ids'])&overlapping)
        item=dict(item_id=offer['offer_id'],kind='SPECIFIC_TRADE_INTENT',source_binding=deepcopy(decision['source_binding']),
            terms=deepcopy(offer),analysis_status='BILATERAL_REVIEWED',rule_check='CURRENT_SIMPLE_ASSETS_CHECKED',
            financial_evidence='COST_COMPARISON_ONLY_SIGNING_CAPACITY_UNKNOWN',
            executor_readiness='DEPENDENCY_UNSUPPORTED' if blocked else 'REQUIRES_LIVE_TRADE_PLAN',
            approval_status='NOT_GRANTED',execution_authorized=False,
            next_step='Player approval, then separate live identity/regular-capacity/five-man-reference plan')
        (research if blocked else items).append(item)
        moves.extend(dict(type=m['kind'],identity=m.get('source_identity'),asset_id=m.get('asset_id'),
            from_team_id=m['from_team_id'],to_team_id=m['to_team_id']) for m in offer['moves'])
    requests=[]
    pending={i.get('object_id') for i in issues if i['code']=='POST_TRADE_COACHING_REPLAN_REQUIRED'}
    for action in selected['actions']:
        if action['kind']!='COACHING' or action['action_id'] in pending:
            research.append(dict(item_id=action['action_id'],kind=action['kind'],action=deepcopy(action),
                executor_readiness='POST_TRADE_COACHING_REPLAN_REQUIRED' if action['action_id'] in pending else 'BLOCKED_EXECUTOR',
                approval_status='NOT_GRANTED',execution_authorized=False))
            continue
        requests.extend(deepcopy(action['requests']))
    if requests:
        if coach_snapshot is None:
            research.append(dict(kind='COACHING',executor_readiness='EXECUTION_PREPARATION_PENDING',requests=requests))
        else:
            b=decision['source_binding']
            if any(coach_snapshot.get(k)!=b.get(v) for k,v in [('career_id','career_id'),('source_batch_id','batch_id'),('game_date','game_date'),('data_updated_at','data_updated_at')]):
                raise ValueError('OFFLINE_COACHING_SOURCE_MISMATCH')
            # Merge identical field targets while keeping their original reasoning in portfolio.
            merged={}
            for r in requests:
                key=(r['team_id'],r.get('opponent_team_id'))
                r['targets']=normalize_freelance(r['targets'],load_profile())
                if key in merged:
                    for f,v in r['targets'].items():
                        if f in merged[key]['targets'] and merged[key]['targets'][f]!=v:
                            raise ValueError('COACH_FIELD_CONFLICT')
                    merged[key]['targets'].update(r['targets'])
                else:
                    merged[key]=r
            batch=propose_batch(coach_snapshot,list(merged.values()),decision['decision_run_id']+'_coach',decision['decision_run_id'],decision['revision'])
            dry=validate_batch(batch,coach_snapshot)
            generated.append(dict(kind='COACHING_OFFLINE_ARTIFACT',batch=batch,dry_run=dry,
                gm_verdict=dict(valid=dry['valid'],executable_after_separate_player_approval=dry['executable'],
                    blocked_action_ids=dry['blocked_action_ids'],mode='OFFLINE_NO_PROCESS_HANDLES'),
                action_ids=[a['action_id'] for a in batch['actions']],batch_digest=dry['batch_digest']))
            if dry['executable']:
                items.append(dict(item_id=batch['batch_id'],kind='COACHING_BATCH',action_ids=generated[-1]['action_ids'],
                    source_internal_action_ids=[a['action_id'] for a in selected['actions'] if a['kind']=='COACHING' and a['action_id'] not in pending and a.get('requests')],
                    batch_digest=dry['batch_digest'],source_binding=deepcopy(b),executor_readiness='OFFLINE_PREPARED_REQUIRES_PLAYER_APPROVAL',
                    analysis_status='REVIEWED',rule_check='PURE_CODEC_VALIDATED',financial_evidence='NO_CONTRACT_CHANGE',
                    approval_status='NOT_GRANTED',execution_authorized=False))
            else:
                research.append(dict(kind='COACHING',executor_readiness='BLOCKED_CODEC_OR_READINESS',artifact_ref=batch['batch_id']))
    finance_result=None
    if moves and finance and analysis['finance_alignment']=='SAME_BATCH':
        finance_result=compare(finance,dict(scenario_id=decision['decision_run_id']+'_portfolio_r'+str(decision['revision']),kind='TRADE_OR_SIGNING',moves=moves))
    return dict(specific_approval_items=items,research_items=research,generated_artifact_refs=generated,
        finance_evidence=finance_result or dict(status='NOT_LINKED_OR_STALE',signing_capacity=None),execution_authorized=False)
