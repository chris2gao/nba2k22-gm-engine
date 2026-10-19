"""M3 reads only sealed M0 projections; exports plain DTOs and actual access receipts."""
from copy import deepcopy
import json
import re

from . import AccessError, QUERY_VERSION
from .query import QuerySession
from gm_core.workbench_common import now, require, text_required

PROJECTIONS = {
    'teams': ['team_id','team','total_wins','total_losses','total_salary'],
    'team_stats': ['team_id','team','season_year','totals','source_status'],
    'players': ['identity','name','team_id','team','pool_slot','position','face_id','birth_date','salary','years_left','contract','attributes','season_totals'],
    'staff': ['identity','name','team_id','team','role','candidate_position','mapping_status','salary','years_left','attributes'],
    'coaching': ['team_id','team','coach','values','readiness'],
    'defense': ['team_id','opponent_team_id','values','mixed_fields','status'],
    'picks': ['asset_id','team_id','owner','original_team_id','draft_year','draft_round','trade_eligible'],
    'finance': ['team_id','team','total_salary','payroll','budget','cash','financial_eligibility'],
}


def consume(session, entity, fields, receipts):
    rows, cursor, pages = [], None, 0
    if not session.available[entity]:
        receipts.append(dict(access_id='access:'+entity, entity=entity, binding=deepcopy(session.binding),
            projection=fields, status='SOURCE_UNAVAILABLE', read_count=0, returned_identities=[], cursor_exhausted=True))
        return rows
    while True:
        p = session.query(entity, fields=fields, limit=50, cursor=cursor)
        rows.extend(p['rows'])
        pages += 1
        if not p['truncated']:
            break
        if not p['next_cursor'] or p['next_cursor'] == cursor:
            raise AccessError('RESULT_LIMIT_REACHED', 'M3 could not exhaust '+entity)
        cursor = p['next_cursor']
    receipts.append(dict(access_id='access:'+entity, entity=entity, binding=deepcopy(session.binding),
        projection=fields, filters={}, query_version=QUERY_VERSION, screened_count=None, read_count=len(rows),
        returned_identities=[r.get('identity', r.get('asset_id', str(r.get('team_id'))+':'+str(r.get('opponent_team_id','')))) for r in rows],
        cursor_exhausted=True, pages=pages, status='ROWS_READ_NOT_ASSESSED', requested_scope='ALL_PROJECTED_SOURCE_ROWS',
        execution_origin=dict(kind='LOCAL_CLI', tool_name='QuerySession', time=now())))
    return rows


def load_inputs(query_root, published_root, career, batch, allow_local=False):
    if not batch:
        raise ValueError('EXPLICIT_BATCH_REQUIRED')
    session = QuerySession(query_root, published_root, career, batch)
    try:
        if session.binding['publication_status'] == 'LOCAL_AUDITED_NOT_PUBLISHED' and not allow_local:
            raise AccessError('LOCAL_AUDITED_NOT_PUBLISHED', 'Explicit development opt-in required')
        receipts = []
        result = {e: consume(session, e, f, receipts) for e,f in PROJECTIONS.items()}
        result.update(source_binding=deepcopy(session.binding), context=deepcopy(session.record['source_manifest'].get('context',{})), source_access=receipts)
        return result
    finally:
        session.close()


def screen(session, query, player_fields, staff_fields, limit=5, cursor=None):
    """Compile registered field names only; all caller values stay SQL parameters."""
    require(query, ('query_id','source_domain','role_question','filters','excluded_team_ids','order_by'))
    text_required(query['query_id'], 'query_id')
    text_required(query['role_question'], 'role_question')
    limit=min(limit,query.get('limit',limit))
    if type(limit) is not int or not 1<=limit<=5:
        raise ValueError('MARKET_LIMIT_1_TO_5')
    domain = query['source_domain']
    entity = {'roster':'players','pool':'pool','staff':'staff'}.get(domain)
    if not entity or not session.available[entity]:
        raise ValueError('MARKET_SOURCE_UNAVAILABLE')
    allowed = set(staff_fields if domain == 'staff' else player_fields)
    required_fields = set()
    params = []

    def field(name):
        match = re.fullmatch(r'attributes\.([A-Za-z0-9_]+)\.value', name)
        if match and match[1] in allowed:
            required_fields.add(name)
            return "json_extract(attributes, '$.\""+match[1]+"\".value')"
        if name in session.columns[entity] and name not in {'attributes', 'contract', 'season_totals'}:
            required_fields.add(name)
            return '"'+name+'"'
        raise ValueError('UNREGISTERED_MARKET_FIELD:'+name)

    conditions, ordering = [], []
    if not isinstance(query['filters'], list) or not isinstance(query['order_by'], list):
        raise ValueError('MARKET_FILTERS_AND_ORDER_LIST_REQUIRED')
    for f in query['filters']:
        expr = field(f['native_field'])
        op = f['operator']
        if op == 'is_null':
            conditions.append(expr+' IS NULL')
        elif op in ('eq','gte','lte') and type(f.get('value')) in (str,int,float):
            conditions.append(expr+{'eq':' = ?','gte':' >= ?','lte':' <= ?'}[op])
            params.append(f['value'])
        else:
            raise ValueError('INVALID_MARKET_OPERATOR_OR_VALUE')
    for o in query['order_by']:
        direction = o['direction'].upper()
        if direction not in ('ASC','DESC'):
            raise ValueError('INVALID_MARKET_ORDER')
        expr = field(o['native_field'])
        ordering.extend([expr+' IS NULL ASC', expr+' '+direction])
    ordering.append('identity ASC')
    excluded = query['excluded_team_ids']
    if not isinstance(excluded, list) or len(excluded)>30 or any(type(t) is not int for t in excluded):
        raise ValueError('INVALID_EXCLUDED_TEAM_IDS')
    population = ''
    if excluded:
        if entity == 'pool':
            # Pool has no certified team_id. Ownership is available only through same-batch roster join.
            population = ' NOT EXISTS(SELECT identity FROM q_players r WHERE r.pool_slot=q_pool.slot_id AND r.team_id IN ('+','.join('?' for _ in excluded)+'))'
        else:
            population = '(team_id IS NULL OR team_id NOT IN ('+','.join('?' for _ in excluded)+'))'
    base_params = list(excluded)
    base_where = ' WHERE '+population if population else ''
    where = base_where+(' AND ' if population else ' WHERE ')+(' AND '.join(conditions) or '1=1')
    projection = 'identity,name'+(',team_id,team' if entity in ('players','staff') else ',roster_status')
    # Return the specific decoded values used in screening, not whole raw structs.
    projection += ''.join(','+field_expr+' AS "screen_'+str(i)+'"' for i,field_expr in enumerate([field(k) for k in sorted(required_fields)]))
    stats_sql = 'SELECT COUNT(*) AS population FROM q_'+entity+base_where
    population_count = session.query('sql', sql=stats_sql, params=base_params)['rows'][0]['population']
    matched = session.query('sql', sql='SELECT COUNT(*) AS matched FROM q_'+entity+where, params=base_params+params)['rows'][0]['matched']
    # Explicit is_null is a requested class, not a silently failed numeric comparison.
    null_fields = [field(f['native_field']) for f in query['filters'] if f['operator'] != 'is_null']
    unknown = session.query('sql', sql='SELECT COUNT(*) AS unknown_count FROM q_'+entity+base_where+(' AND ' if population else ' WHERE ')+(' OR '.join(e+' IS NULL' for e in null_fields) or '0=1'), params=base_params)['rows'][0]['unknown_count']
    result = session.query('sql', sql='SELECT '+projection+' FROM q_'+entity+where+' ORDER BY '+','.join(ordering), params=base_params+params, limit=limit, cursor=cursor)
    return dict(query=deepcopy(query), source_binding=deepcopy(session.binding), filter_population_count=population_count,
        matched_count=matched, unknown_required_field_count=unknown, screen_fields=sorted(required_fields),
        rows=result['rows'], returned_identities=[r['identity'] for r in result['rows']], next_cursor=result['next_cursor'],
        cursor_exhausted=not result['truncated'], status='SCREENED_SUBSET_READ_NOT_ASSESSED',
        execution_origin=dict(kind='LOCAL_CLI', tool_name='QuerySession', time=now()), query_version=QUERY_VERSION)
