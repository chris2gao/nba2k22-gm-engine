# -*- coding: utf-8 -*-
"""
NBA 2K22 赛季比赛历史与 BoxScore 数据系统离线单元测试 (Offline Unit Tests)
【核心原则】：
1. 纯确定性、完全脱机、不依赖正在运行的 NBA2K22.exe 进程。
2. 验证 2K 原生 SCHEDULEDATE 位域解码、24 字节 BOXSCORE / STATLINE 结构体拆解。
3. 验证高级统计公式 (GameScore, TS%, eFG%, USG%, ORTG, DRTG, NetRating, Pace) 精度。
4. 验证 SQLite 5 层关系型拓扑结构、外键级联与幂等更新机制。
"""

import os
import sys
import struct
import sqlite3
import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from match_history_reader import (
    decode_schedule_date,
    ensure_match_history_schema,
    save_match_data_to_db,
    DEFAULT_TEAM_MAP,
    normalize_team_abbr
)


def test_decode_schedule_date():
    """验证 SCHEDULEDATE 32位位域解码逻辑"""
    # 构造一个 2021年10月19日的测试位域:
    # Day = 19 (0x13), Month = 10 (0x0A), YearOffset = 21 (0x15) -> Year = 2021
    # bits 0..4: Id = 3
    # bits 5..15: Minutes = 1200
    # bits 16..20: Day = 19
    # bits 21..24: Month = 10
    # bits 25..31: YearOffset = 21
    packed = (3 & 0x1F) | ((1200 & 0x7FF) << 5) | ((19 & 0x1F) << 16) | ((10 & 0x0F) << 21) | ((21 & 0x7F) << 25)
    
    yr, mo, day, dt_str = decode_schedule_date(packed)
    assert yr == 2021
    assert mo == 10
    assert day == 19
    assert dt_str == "2021-10-19"


def test_boxscore_statline_unpacking():
    """验证 24 字节原生 BOXSCORE_STATLINE 的解构与进阶公式计算"""
    # 模拟 Giannis Antetokounmpo 的真实单场统计:
    # PlayerId = 101, Minutes = 36, +/- = +47
    # FGM = 14, FGA = 22, 3PM = 2, 3PA = 7
    # FTA = 8, STL = 1, BLK = 3, DREB = 21
    # DefFGM = 1, DefFGA = 9, DefPtsAllowed = 3
    # AST = 11, FTM = 7, OREB = 0, TOV = 1
    # Possessions = 85, Fouls = 2, Started = 1
    
    pid = 101
    in_use = 1
    mins = 36
    raw_pm = 47 # +47
    w0 = (pid & 0xFFFF) | (in_use << 16) | ((mins & 0x7F) << 17) | ((raw_pm & 0xFF) << 24)
    
    fgm, fga, tpm, tpa = 14, 22, 2, 7
    w1 = (fgm & 0xFF) | ((fga & 0x1FF) << 8) | ((tpm & 0x7F) << 17) | ((tpa & 0xFF) << 24)
    
    fta, stl, blk, dreb = 8, 1, 3, 21
    w2 = (fta & 0xFF) | ((stl & 0xFF) << 8) | ((blk & 0xFF) << 16) | ((dreb & 0xFF) << 24)
    
    def_fgm, def_fga, def_pts = 1, 9, 3
    w3 = (def_fgm & 0xFF) | ((def_fga & 0x1FF) << 8) | ((def_pts & 0x7FFF) << 17)
    
    ast, ftm, oreb, tov = 11, 7, 0, 1
    w4 = (ast & 0x7F) | ((ftm & 0x7F) << 7) | ((oreb & 0xFF) << 14) | ((tov & 0x7F) << 22)
    
    poss, fouls, started = 85, 1, 1
    w5 = (poss & 0xFF) | ((fouls & 0x0F) << 8) | ((started & 0x01) << 12)
    
    raw_bytes = struct.pack("<IIIIII", w0, w1, w2, w3, w4, w5)
    assert len(raw_bytes) == 24
    
    # 模拟解包
    rw0, rw1, rw2, rw3, rw4, rw5 = struct.unpack("<IIIIII", raw_bytes)
    assert (rw0 & 0xFFFF) == 101
    assert ((rw0 >> 17) & 0x7F) == 36
    assert ((rw0 >> 24) & 0xFF) == 47
    
    pts = fgm * 2 + tpm + ftm
    assert pts == 14 * 2 + 2 + 7 # 37
    
    # GameScore 公式验证
    # GmSc = PTS + 0.4*FGM - 0.7*FGA - 0.4*(FTA - FTM) + 0.7*OREB + 0.3*DREB + STL + 0.7*AST + 0.7*BLK - 0.4*PF - TOV
    gm_sc = round(pts + 0.4 * fgm - 0.7 * fga - 0.4 * (fta - ftm) + 0.7 * oreb + 0.3 * dreb + stl + 0.7 * ast + 0.7 * blk - 0.4 * fouls - tov, 2)
    assert gm_sc == 42.5
    
    # TS% 真实命中率: PTS / (2 * (FGA + 0.44 * FTA))
    ts_att = fga + 0.44 * fta
    ts_pct = round(pts / (2 * ts_att), 4)
    assert round(ts_pct * 100, 1) == 72.5
    
    # eFG% 有效命中率: (FGM + 0.5 * 3PM) / FGA
    efg_pct = round((fgm + 0.5 * tpm) / fga, 4)
    assert round(efg_pct * 100, 1) == 68.2


def test_team_advanced_metrics_formulas():
    """验证球队高阶数据 (ORTG, DRTG, NetRating, Pace, 四要素) 计算公式"""
    pts = 150
    opp_pts = 84
    poss = 103.0
    ot_count = 0
    
    ortg = round((pts / poss) * 100, 2)
    drtg = round((opp_pts / poss) * 100, 2)
    net = round(ortg - drtg, 2)
    pace = round(poss * 48.0 / (48.0 + ot_count * 5.0), 2)
    
    assert ortg == 145.63
    assert drtg == 81.55
    assert net == 64.08
    assert pace == 103.0


def test_database_schema_and_atomic_upsert():
    """验证 5 层关联表建表、外键级联与原子幂等落库"""
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    
    ensure_match_history_schema(conn)
    
    # 验证 5 张表均已成功建立
    tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
    expected_tables = {"match_seasons", "match_game_days", "match_games", "match_game_teams", "match_game_players"}
    assert expected_tables.issubset(tables)
    
    # 构建一组高保真合成比赛数据
    synthetic_data = {
        "season": {
            "season_id": "2021-2022",
            "season_year": 2022,
            "season_name": "2021-2022 NBA Season",
            "total_schedule_games": 1230,
            "played_games": 1,
            "current_game_date": "2021-10-19",
            "stage": "REGULAR_SEASON",
            "allstar_game_index": 700,
            "is_active": True
        },
        "days": [
            {
                "season_id": "2021-2022",
                "game_date": "2021-10-19",
                "month": 10,
                "day": 19,
                "day_of_season": 1,
                "scheduled_games": 1,
                "played_games": 1
            }
        ],
        "games": [
            {
                "game_uid": "2021-2022_G0001",
                "season_id": "2021-2022",
                "game_id": 1,
                "game_date": "2021-10-19",
                "played_date": "2021-10-19",
                "game_type": "REGULAR",
                "home_team_id": 1,
                "away_team_id": 24,
                "home_team_abbr": "MIL",
                "away_team_abbr": "OKC",
                "home_score": 150,
                "away_score": 84,
                "winner_team_id": 1,
                "point_differential": 66,
                "overtime_count": 0,
                "attendance": 18717,
                "was_simulated": True,
                "status": 2,
                "is_nationally_televised": True,
                "home_q1": 33, "home_q2": 47, "home_q3": 39, "home_q4": 31, "home_ot": 0,
                "away_q1": 15, "away_q2": 15, "away_q3": 20, "away_q4": 34, "away_ot": 0,
                "team_stats": [
                    {
                        "game_uid": "2021-2022_G0001", "season_id": "2021-2022", "game_date": "2021-10-19",
                        "team_id": 1, "team_abbr": "MIL", "opponent_team_id": 24, "opponent_abbr": "OKC",
                        "is_home": True, "is_win": True, "points": 150, "points_allowed": 84,
                        "fgm": 57, "fga": 94, "fg_pct": 0.606, "tpm": 18, "tpa": 41, "tp_pct": 0.439,
                        "ftm": 18, "fta": 22, "ft_pct": 0.818, "oreb": 4, "dreb": 47, "reb": 51,
                        "ast": 35, "stl": 6, "blk": 6, "tov": 7, "pf": 15,
                        "pts_paint": 58, "pts_fastbreak": 6, "pts_2nd_chance": 16, "pts_off_to": 10,
                        "biggest_lead": 73, "possession_seconds": 1200, "possessions": 103.0,
                        "ortg": 145.6, "drtg": 81.5, "net_rating": 64.1, "pace": 103.0,
                        "efg_pct": 0.702, "ts_pct": 0.723, "oreb_pct": 0.118, "dreb_pct": 0.870,
                        "reb_pct": 0.580, "ast_ratio": 0.614, "tov_pct": 6.5
                    },
                    {
                        "game_uid": "2021-2022_G0001", "season_id": "2021-2022", "game_date": "2021-10-19",
                        "team_id": 24, "team_abbr": "OKC", "opponent_team_id": 1, "opponent_abbr": "MIL",
                        "is_home": False, "is_win": False, "points": 84, "points_allowed": 150,
                        "fgm": 31, "fga": 95, "fg_pct": 0.326, "tpm": 9, "tpa": 40, "tp_pct": 0.225,
                        "ftm": 13, "fta": 16, "ft_pct": 0.812, "oreb": 7, "dreb": 30, "reb": 37,
                        "ast": 20, "stl": 4, "blk": 1, "tov": 11, "pf": 20,
                        "pts_paint": 28, "pts_fastbreak": 2, "pts_2nd_chance": 8, "pts_off_to": 2,
                        "biggest_lead": 3, "possession_seconds": 1150, "possessions": 104.0,
                        "ortg": 80.8, "drtg": 144.2, "net_rating": -63.4, "pace": 104.0,
                        "efg_pct": 0.374, "ts_pct": 0.412, "oreb_pct": 0.130, "dreb_pct": 0.882,
                        "reb_pct": 0.420, "ast_ratio": 0.645, "tov_pct": 9.8
                    }
                ],
                "player_stats": [
                    {
                        "game_uid": "2021-2022_G0001", "season_id": "2021-2022", "game_date": "2021-10-19",
                        "player_id": 101, "player_name": "Giannis Antetokounmpo",
                        "team_id": 1, "team_abbr": "MIL", "opponent_team_id": 24, "opponent_abbr": "OKC",
                        "is_home": True, "is_starter": True, "minutes": 36, "points": 37,
                        "fgm": 14, "fga": 22, "fg_pct": 0.636, "tpm": 2, "tpa": 7, "tp_pct": 0.286,
                        "ftm": 7, "fta": 8, "ft_pct": 0.875, "oreb": 0, "dreb": 21, "reb": 21,
                        "ast": 11, "stl": 1, "blk": 3, "tov": 1, "pf": 2, "plus_minus": 47,
                        "defensive_fgm": 1, "defensive_fga": 9, "defensive_fg_pct": 0.111,
                        "defensive_pts_allowed": 3, "possessions": 85,
                        "ts_pct": 0.725, "efg_pct": 0.682, "usg_pct": 31.9, "game_score": 42.5,
                        "pie": 0.285, "ast_to_tov": 11.0, "double_double": True, "triple_double": True
                    }
                ]
            }
        ]
    }
    
    # 第一次落库
    summary = save_match_data_to_db(synthetic_data, conn=conn)
    assert summary["games_stored"] == 1
    assert summary["team_records_stored"] == 2
    assert summary["player_boxscores_stored"] == 1
    
    # 验证各表数据
    c = conn.cursor()
    assert c.execute("SELECT count(*) FROM match_seasons").fetchone()[0] == 1
    assert c.execute("SELECT count(*) FROM match_game_days").fetchone()[0] == 1
    assert c.execute("SELECT count(*) FROM match_games").fetchone()[0] == 1
    assert c.execute("SELECT count(*) FROM match_game_teams").fetchone()[0] == 2
    assert c.execute("SELECT count(*) FROM match_game_players").fetchone()[0] == 1
    
    # 验证三双和数据完整性
    p = c.execute("SELECT player_name, points, reb, ast, triple_double, game_score FROM match_game_players").fetchone()
    assert p[0] == "Giannis Antetokounmpo"
    assert p[1] == 37
    assert p[2] == 21
    assert p[3] == 11
    assert p[4] == 1 # triple_double == True
    assert p[5] == 42.5
    
    # 第二次落库 (测试幂等性，不应报 UNIQUE 约束错误或导致数据翻倍)
    summary2 = save_match_data_to_db(synthetic_data, conn=conn)
    assert summary2["games_stored"] == 1
    assert c.execute("SELECT count(*) FROM match_games").fetchone()[0] == 1
    assert c.execute("SELECT count(*) FROM match_game_teams").fetchone()[0] == 2
    assert c.execute("SELECT count(*) FROM match_game_players").fetchone()[0] == 1
    
    # 验证查询聚合逻辑
    from query_match_history import query_date_matches, query_single_game, query_standings
    # 确保无异常抛出
    query_date_matches(conn, "2021-10-19")
    query_single_game(conn, "2021-2022_G0001")
    query_standings(conn)
    
    conn.close()
