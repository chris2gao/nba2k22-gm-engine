"""Live source audit for roster descriptors and extended observations.

These are memory/database checks, not JSON export or synchronization checks.
"""
import json
import struct
from source_extensions import (roster_directory, stats_record, staff_details, player_details,
                               team_statistics, player_statistics)
from data_context import decode_context


def audit_extensions(conn, mem, calibration, teams, snapshot_id):
    root = int(calibration['player_pool']['base_addr'], 16)
    directory = roster_directory(mem, root)
    team_map = {t['address']: tid for tid, t in teams.items()}
    notes = conn.execute('SELECT notes FROM monthly_snapshots WHERE snapshot_id=?', (snapshot_id,)).fetchone()[0]
    game_date = decode_context(notes).get('game_date')
    season_year = conn.execute('SELECT season_year FROM monthly_snapshots WHERE snapshot_id=?', (snapshot_id,)).fetchone()[0]
    checks = {}
    totals = []
    for tid, team in teams.items():
        idx = mem.require_uint16(team['address'] + 0xe80)
        values, raw = stats_record(mem, directory, 'team_stats', idx, season_year)
        row = conn.execute('SELECT * FROM team_source_stats WHERE snapshot_id=? AND team_id=?', (snapshot_id, tid)).fetchone()
        if row is None or row['raw_struct'] != raw or json.loads(row['totals_json']) != values:
            raise RuntimeError(f'Team source statistics changed: {tid}')
        summary = team_statistics(values)
        stored = conn.execute('SELECT * FROM team_monthly_stats WHERE snapshot_id=? AND team_id=?', (snapshot_id, tid)).fetchone()
        if any(stored[k] != v for k, v in summary.items()):
            raise RuntimeError(f'Team statistical calculations differ: {tid}')
        totals.append(values)
    checks['extended_team_statistics_match_live_memory'] = True
    checks['league_win_loss_and_points_balance'] = (sum(v['w'] for v in totals) == sum(v['l'] for v in totals)
        and sum(v['points'] for v in totals) == sum(v['pa'] for v in totals))
    staff = conn.execute('SELECT * FROM staff_source_details WHERE snapshot_id=? ORDER BY staff_slot', (snapshot_id,)).fetchall()
    checks['complete_staff_descriptor_captured'] = len(staff) == directory['staff']['count']
    for row in staff:
        detail, raw = staff_details(mem, directory['staff']['address'] + 0x30 + row['staff_slot'] * 0x160,
                                    row['staff_slot'], teams)
        if row['raw_struct'] != raw or json.loads(row['details_json']) != detail:
            raise RuntimeError(f'Staff source differs: {row["staff_slot"]}')
    checks['extended_staff_identity_and_team_links_match_live'] = True
    players = conn.execute('SELECT * FROM player_source_details WHERE snapshot_id=? ORDER BY team_id,roster_slot', (snapshot_id,)).fetchall()
    for row in players:
        addr = mem.require_uint64(teams[row['team_id']]['address'] + row['roster_slot'] * 8)
        raw = mem.read_bytes(addr, 0x4f0)
        if raw is None or raw != row['raw_struct']:
            raise RuntimeError(f'Player source changed: {row["player_name"]}')
        detail = player_details(raw, team_map, game_date)
        index = struct.unpack_from('<H', raw, 0xfc)[0]
        values, _ = stats_record(mem, directory, 'player_stats', index, season_year)
        detail.update(season_totals=values, stats_index=None if index == 65535 else index,
                      stats_source='OBSERVED_CURRENT_SEASON' if values is not None else 'NOT_OBSERVED_NO_STATS_INDEX')
        if json.loads(row['details_json']) != detail:
            raise RuntimeError(f'Player decoded fields differ: {row["player_name"]}')
        monthly = conn.execute('SELECT * FROM player_monthly_stats WHERE snapshot_id=? AND team_id=? AND player_name=? AND face_id=?',
                               (snapshot_id, row['team_id'], row['player_name'], row['face_id'])).fetchone()
        if monthly is None or any(monthly[k] != v for k, v in player_statistics(values).items()):
            raise RuntimeError(f'Player statistical calculations differ: {row["player_name"]}')
    checks['extended_player_birth_attributes_contracts_statistics_match_live'] = bool(players)
    assets = conn.execute('SELECT * FROM draft_asset_observations WHERE snapshot_id=? ORDER BY asset_slot', (snapshot_id,)).fetchall()
    checks['draft_asset_slots_match_descriptor'] = len(assets) == directory['draft_assets']['count']
    checks['draft_asset_uncertain_metadata_remains_null'] = all(row['draft_year'] is None and row['draft_round'] is None and row['protection'] is None for row in assets)
    return checks
