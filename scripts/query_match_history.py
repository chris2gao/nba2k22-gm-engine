# -*- coding: utf-8 -*-
"""
NBA 2K22 赛季比赛历史与高阶技术统计查询工具 (Match History & Box Score Query CLI)

用法示例:
    # 1. 查询指定日期的所有比赛战报
    python scripts/query_match_history.py --date 2021-10-19

    # 2. 查询单场比赛详尽双边 BoxScore (包含球员对位防守与高阶统计)
    python scripts/query_match_history.py --game 2021-2022_G0001

    # 3. 查询球队赛季战绩与全场赛果日程 (Game Log)
    python scripts/query_match_history.py --team MIL

    # 4. 查询球员个人全季比赛日志与场均统计 (Game Log & Averages)
    python scripts/query_match_history.py --player "Giannis Antetokounmpo"

    # 5. 查询全联盟单场最高分/最高 GameScore 榜单
    python scripts/query_match_history.py --leaders pts --limit 10
    python scripts/query_match_history.py --leaders gamescore --limit 10

    # 6. 查询全联盟实时积分榜与攻防净效率
    python scripts/query_match_history.py --standings
"""

import os
import sys
import argparse
import sqlite3
from pathlib import Path
from typing import Dict, List, Any, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import save_context

DEFAULT_DB = str(ROOT / "database" / "league_state.sqlite")
FALLBACK_TEST_DB = str(ROOT / "_exports" / "test_match_history.sqlite")


def _has_match_tables(path: str) -> bool:
    if not os.path.exists(path):
        return False
    try:
        c = sqlite3.connect(path)
        r = c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='match_games'").fetchone()
        c.close()
        return r[0] > 0
    except Exception:
        return False


def resolve_db_path(db_path: Optional[str], save_id: Optional[str]) -> str:
    if db_path and os.path.exists(db_path):
        return db_path
    if save_id:
        ctx = save_context.resolve_context(save_id)
        if os.path.exists(ctx["db_path"]):
            return ctx["db_path"]
    if _has_match_tables(DEFAULT_DB):
        return DEFAULT_DB
    if _has_match_tables(FALLBACK_TEST_DB):
        return FALLBACK_TEST_DB
    return DEFAULT_DB


def query_date_matches(conn: sqlite3.Connection, game_date: str):
    c = conn.cursor()
    c.execute("""
        SELECT game_uid, home_team_abbr, away_team_abbr, home_score, away_score,
               winner_team_id, point_differential, overtime_count, attendance,
               home_q1, home_q2, home_q3, home_q4, home_ot,
               away_q1, away_q2, away_q3, away_q4, away_ot
        FROM match_games
        WHERE game_date = ?
        ORDER BY game_uid
    """, (game_date,))
    rows = c.fetchall()
    
    if not rows:
        print(f"[-] 在日期 {game_date} 未检索到已完成的比赛记录。")
        return

    print("=" * 82)
    print(f"  NBA 2K22 比赛日历战报: {game_date} (共 {len(rows)} 场比赛)")
    print("=" * 82)
    
    for r in rows:
        uid, h_abbr, a_abbr, h_pts, a_pts, win_id, diff, ot, att = r[:9]
        hq1, hq2, hq3, hq4, hot = r[9:14]
        aq1, aq2, aq3, aq4, aot = r[14:19]
        
        ot_str = f" ({ot}OT)" if ot > 0 else ""
        winner = h_abbr if h_pts >= a_pts else a_abbr
        
        # 查单场最高分球员
        c.execute("""
            SELECT player_name, team_abbr, points, reb, ast, game_score
            FROM match_game_players
            WHERE game_uid = ?
            ORDER BY points DESC LIMIT 1
        """, (uid,))
        star = c.fetchone()
        star_str = f" | 本场焦点: {star[0]} ({star[1]}) {star[2]}分 {star[3]}板 {star[4]}助 (GmSc {star[5]})" if star else ""
        
        print(f"\n【比赛标识: {uid}】 {a_abbr} {a_pts} @ {h_abbr} {h_pts}{ot_str}  [胜者: {winner}, 分差: {diff}分, 上座: {att:,}人]")
        print(f"   单节比分:")
        print(f"   {a_abbr:>5}: Q1:{aq1:2d} | Q2:{aq2:2d} | Q3:{aq3:2d} | Q4:{aq4:2d}" + (f" | OT:{aot:2d}" if ot > 0 else "") + f" -> 总计: {a_pts:3d}")
        print(f"   {h_abbr:>5}: Q1:{hq1:2d} | Q2:{hq2:2d} | Q3:{hq3:2d} | Q4:{hq4:2d}" + (f" | OT:{hot:2d}" if ot > 0 else "") + f" -> 总计: {h_pts:3d}")
        if star_str:
            print(f"  {star_str}")


def query_single_game(conn: sqlite3.Connection, game_uid: str):
    c = conn.cursor()
    c.execute("""
        SELECT game_uid, season_id, game_id, game_date, played_date, game_type,
               home_team_id, away_team_id, home_team_abbr, away_team_abbr,
               home_score, away_score, winner_team_id, point_differential,
               overtime_count, attendance, was_simulated,
               home_q1, home_q2, home_q3, home_q4, home_ot,
               away_q1, away_q2, away_q3, away_q4, away_ot
        FROM match_games
        WHERE game_uid = ?
    """, (game_uid,))
    g = c.fetchone()
    if not g:
        print(f"[-] 未找到比赛 UID: {game_uid}")
        return

    uid, season, gid, g_date, p_date, g_type, h_id, a_id, h_abbr, a_abbr, h_pts, a_pts, win_id, diff, ot, att, was_sim = g[:17]
    hq1, hq2, hq3, hq4, hot = g[17:22]
    aq1, aq2, aq3, aq4, aot = g[22:27]

    print("=" * 95)
    print(f"  NBA 2K22 比赛完整详尽 BoxScore: {uid}")
    print(f"  赛季: {season} | 日期: {g_date} | 类型: {g_type} | 观众: {att:,} 人 | 模拟模式: {'是' if was_sim else '3D实打'}")
    print("=" * 95)
    print(f"\n【终局比分 Final Score】")
    print(f"   {a_abbr:>5}: Q1:{aq1:2d}  Q2:{aq2:2d}  Q3:{aq3:2d}  Q4:{aq4:2d}" + (f"  OT:{aot:2d}" if ot > 0 else "") + f"  =>  {a_pts:3d}")
    print(f"   {h_abbr:>5}: Q1:{hq1:2d}  Q2:{hq2:2d}  Q3:{hq3:2d}  Q4:{hq4:2d}" + (f"  OT:{hot:2d}" if ot > 0 else "") + f"  =>  {h_pts:3d}")

    # 球队数据对比
    c.execute("""
        SELECT team_abbr, is_home, points, fgm, fga, fg_pct, tpm, tpa, tp_pct, ftm, fta, ft_pct,
               oreb, dreb, reb, ast, stl, blk, tov, pf, pts_paint, pts_fastbreak, pts_2nd_chance,
               pts_off_to, biggest_lead, possessions, ortg, drtg, net_rating, pace, ts_pct, efg_pct
        FROM match_game_teams
        WHERE game_uid = ?
        ORDER BY is_home ASC
    """, (game_uid,))
    t_rows = c.fetchall()
    
    if len(t_rows) == 2:
        away_t, home_t = t_rows[0], t_rows[1]
        print(f"\n【全队高阶技术统计对比 (Team Stats Comparison)】")
        print(f"  {'指标 (Statistic)':<26} | {a_abbr:>12} | {h_abbr:>12}")
        print(f"  {'-'*26}-+-{'-'*12}-+-{'-'*12}")
        print(f"  {'总得分 (Points)':<26} | {away_t[2]:>12} | {home_t[2]:>12}")
        print(f"  {'投篮 (FGM-A / FG%)':<26} | {away_t[3]}-{away_t[4]} ({away_t[5]*100:.1f}%) | {home_t[3]}-{home_t[4]} ({home_t[5]*100:.1f}%)")
        print(f"  {'三分 (3PM-A / 3P%)':<26} | {away_t[6]}-{away_t[7]} ({away_t[8]*100:.1f}%) | {home_t[6]}-{home_t[7]} ({home_t[8]*100:.1f}%)")
        print(f"  {'罚球 (FTM-A / FT%)':<26} | {away_t[9]}-{away_t[10]} ({away_t[11]*100:.1f}%) | {home_t[9]}-{home_t[10]} ({home_t[11]*100:.1f}%)")
        print(f"  {'真实命中率 (TS%)':<26} | {away_t[30]*100:>11.1f}% | {home_t[30]*100:>11.1f}%")
        print(f"  {'有效命中率 (eFG%)':<26} | {away_t[31]*100:>11.1f}% | {home_t[31]*100:>11.1f}%")
        print(f"  {'篮板 (OREB / DREB / REB)':<26} | {away_t[12]}/{away_t[13]}/{away_t[14]:>6} | {home_t[12]}/{home_t[13]}/{home_t[14]:>6}")
        print(f"  {'助攻 / 抢断 / 盖帽':<26} | {away_t[15]}/{away_t[16]}/{away_t[17]:>6} | {home_t[15]}/{home_t[16]}/{home_t[17]:>6}")
        print(f"  {'失误 (TOV) / 犯规 (PF)':<26} | {away_t[18]}/{away_t[19]:>8} | {home_t[18]}/{home_t[19]:>8}")
        print(f"  {'内线得分 (Points in Paint)':<26} | {away_t[20]:>12} | {home_t[20]:>12}")
        print(f"  {'快攻得分 (Fastbreak Pts)':<26} | {away_t[21]:>12} | {home_t[21]:>12}")
        print(f"  {'二次进攻得分 (2nd Chance Pts)':<26} | {away_t[22]:>12} | {home_t[22]:>12}")
        print(f"  {'失误转化得分 (Pts off TO)':<26} | {away_t[23]:>12} | {home_t[23]:>12}")
        print(f"  {'最大领先优势 (Biggest Lead)':<26} | {away_t[24]:>12} | {home_t[24]:>12}")
        print(f"  {'回合数 (Possessions)':<26} | {away_t[25]:>12.1f} | {home_t[25]:>12.1f}")
        print(f"  {'进攻百回合效率 (ORTG)':<26} | {away_t[26]:>12.1f} | {home_t[26]:>12.1f}")
        print(f"  {'防守百回合效率 (DRTG)':<26} | {away_t[27]:>12.1f} | {home_t[27]:>12.1f}")
        print(f"  {'净效率 (Net Rating)':<26} | {away_t[28]:>+12.1f} | {home_t[28]:>+12.1f}")
        print(f"  {'比赛节奏 (Pace)':<26} | {away_t[29]:>12.1f} | {home_t[29]:>12.1f}")

    # 双方球员技术统计
    for is_h, tabbr in [(0, a_abbr), (1, h_abbr)]:
        print(f"\n【{tabbr} 球员详尽个人统计 (Player BoxScore)】")
        print(f"  {'球员 (Player)':<20} | {'MIN':>3} | {'PTS':>3} | {'FGM-A':>7} | {'3PM-A':>6} | {'FTM-A':>6} | {'REB (O/D)':>9} | {'AST':>3} | {'STL':>3} | {'BLK':>3} | {'TO':>2} | {'+/-':>4} | {'对位防守 (失分/防守投篮)':>20} | {'GmSc':>5} | {'TS%':>5} | {'USG%':>5}")
        print(f"  {'-'*20}-+-{'-'*3}-+-{'-'*3}-+-{'-'*7}-+-{'-'*6}-+-{'-'*6}-+-{'-'*9}-+-{'-'*3}-+-{'-'*3}-+-{'-'*3}-+-{'-'*2}-+-{'-'*4}-+-{'-'*20}-+-{'-'*5}-+-{'-'*5}-+-{'-'*5}")
        
        c.execute("""
            SELECT player_name, is_starter, minutes, points, fgm, fga, tpm, tpa, ftm, fta,
                   oreb, dreb, reb, ast, stl, blk, tov, plus_minus,
                   defensive_pts_allowed, defensive_fgm, defensive_fga,
                   game_score, ts_pct, usg_pct
            FROM match_game_players
            WHERE game_uid = ? AND is_home = ?
            ORDER BY is_starter DESC, minutes DESC, points DESC
        """, (game_uid, is_h))
        
        for p in c.fetchall():
            p_name, starter, mins, pts, fgm, fga, tpm, tpa, ftm, fta, oreb, dreb, reb, ast, stl, blk, tov, pm, def_pts, def_fgm, def_fga, gmsc, ts, usg = p
            star_prefix = "*" if starter else " "
            pm_str = f"{pm:+d}" if pm != 0 else "0"
            def_str = f"{def_pts}分 ({def_fgm}-{def_fga})" if def_fga > 0 else "-"
            ts_str = f"{ts*100:.1f}%" if ts else "-"
            usg_str = f"{usg:.1f}%" if usg else "-"
            
            print(f"  {star_prefix}{p_name:<19} | {mins:>3} | {pts:>3} | {fgm:>2}-{fga:<4} | {tpm:>2}-{tpa:<3} | {ftm:>2}-{fta:<3} | {reb:>3} ({oreb}/{dreb}) | {ast:>3} | {stl:>3} | {blk:>3} | {tov:>2} | {pm_str:>4} | {def_str:>20} | {gmsc:>5.1f} | {ts_str:>5} | {usg_str:>5}")


def query_team_history(conn: sqlite3.Connection, team_abbr: str, limit: int = 20):
    c = conn.cursor()
    c.execute("""
        SELECT game_uid, game_date, opponent_abbr, is_home, is_win, points, points_allowed,
               fgm, fga, fg_pct, tpm, tpa, tp_pct, reb, ast, stl, blk, tov,
               ortg, drtg, net_rating, pace
        FROM match_game_teams
        WHERE team_abbr = ?
        ORDER BY game_date ASC
    """, (team_abbr.upper(),))
    rows = c.fetchall()
    
    if not rows:
        print(f"[-] 未检索到球队 {team_abbr} 的比赛记录。")
        return

    wins = sum(1 for r in rows if r[4])
    losses = len(rows) - wins
    tot_pts = sum(r[5] for r in rows)
    tot_opp = sum(r[6] for r in rows)
    avg_pts = tot_pts / len(rows)
    avg_opp = tot_opp / len(rows)

    print("=" * 86)
    print(f"  NBA 2K22 球队比赛日志与战绩: {team_abbr.upper()} (总战绩: {wins}胜 {losses}负 | 胜率: {wins/len(rows)*100:.1f}%)")
    print(f"  场均得分: {avg_pts:.1f} | 场均失分: {avg_opp:.1f} | 场均净胜: {avg_pts - avg_opp:+.1f}")
    print("=" * 86)
    print(f"  {'比赛日期':<10} | {'对阵对手':<9} | {'主客':<4} | {'赛果':<4} | {'比分 (Score)':<12} | {'投篮 (FG%)':<11} | {'三分 (3P%)':<10} | {'REB':>4} | {'AST':>3} | {'ORTG':>5} | {'DRTG':>5} | {'NET':>6}")
    print(f"  {'-'*10}-+-{'-'*9}-+-{'-'*4}-+-{'-'*4}-+-{'-'*12}-+-{'-'*11}-+-{'-'*10}-+-{'-'*4}-+-{'-'*3}-+-{'-'*5}-+-{'-'*5}-+-{'-'*6}")
    
    for r in rows[-limit:]:
        uid, g_date, opp, is_home, is_win, pts, opp_pts, fgm, fga, fg_pct, tpm, tpa, tp_pct, reb, ast, stl, blk, tov, ortg, drtg, net, pace = r
        loc_str = "主场" if is_home else "客场"
        res_str = "胜 W" if is_win else "负 L"
        score_str = f"{pts:>3} - {opp_pts:<3}"
        fg_str = f"{fgm:>2}/{fga:<2} ({fg_pct*100:.0f}%)"
        tp_str = f"{tpm:>2}/{tpa:<2} ({tp_pct*100:.0f}%)"
        
        print(f"  {g_date:<10} | vs {opp:<6} | {loc_str:<4} | {res_str:<4} | {score_str:<12} | {fg_str:<11} | {tp_str:<10} | {reb:>4} | {ast:>3} | {ortg:>5.1f} | {drtg:>5.1f} | {net:>+6.1f}")


def query_player_history(conn: sqlite3.Connection, player_query: str, limit: int = 20):
    c = conn.cursor()
    # 模糊查找匹配的球员名
    c.execute("""
        SELECT DISTINCT player_id, player_name, team_abbr
        FROM match_game_players
        WHERE player_name LIKE ? OR player_id = ?
        LIMIT 5
    """, (f"%{player_query}%", player_query if player_query.isdigit() else -1))
    candidates = c.fetchall()
    
    if not candidates:
        print(f"[-] 未找到匹配 '{player_query}' 的球员。")
        return
        
    pid, p_name, p_team = candidates[0]
    
    c.execute("""
        SELECT game_date, opponent_abbr, is_home, is_starter, minutes, points,
               fgm, fga, fg_pct, tpm, tpa, tp_pct, ftm, fta, ft_pct,
               oreb, dreb, reb, ast, stl, blk, tov, plus_minus, game_score, ts_pct, usg_pct
        FROM match_game_players
        WHERE player_id = ?
        ORDER BY game_date ASC
    """, (pid,))
    rows = c.fetchall()
    
    if not rows:
        print(f"[-] 球员 {p_name} 暂无比赛出场记录。")
        return
        
    gp = len(rows)
    pts_avg = sum(r[5] for r in rows) / gp
    reb_avg = sum(r[17] for r in rows) / gp
    ast_avg = sum(r[18] for r in rows) / gp
    stl_avg = sum(r[19] for r in rows) / gp
    blk_avg = sum(r[20] for r in rows) / gp
    min_avg = sum(r[4] for r in rows) / gp
    gmsc_avg = sum(r[23] for r in rows) / gp
    
    tot_fga = sum(r[7] for r in rows)
    tot_fgm = sum(r[6] for r in rows)
    tot_tpa = sum(r[10] for r in rows)
    tot_tpm = sum(r[9] for r in rows)
    tot_fta = sum(r[13] for r in rows)
    tot_ftm = sum(r[12] for r in rows)
    
    fg_pct = tot_fgm / tot_fga if tot_fga > 0 else 0
    tp_pct = tot_tpm / tot_tpa if tot_tpa > 0 else 0
    ft_pct = tot_ftm / tot_fta if tot_fta > 0 else 0
    
    print("=" * 90)
    print(f"  NBA 2K22 球员全季实战日志: {p_name} ({p_team}) [ID: {pid}]")
    print(f"  出战场次: {gp} 场 | 场均出场: {min_avg:.1f} 分钟 | 综合 GameScore: {gmsc_avg:.1f}")
    print(f"  场均数据: {pts_avg:.1f}分 {reb_avg:.1f}板 {ast_avg:.1f}助 {stl_avg:.1f}断 {blk_avg:.1f}帽")
    print(f"  三项命中率: 投篮 {fg_pct*100:.1f}% ({tot_fgm}/{tot_fga}) | 三分 {tp_pct*100:.1f}% ({tot_tpm}/{tot_tpa}) | 罚球 {ft_pct*100:.1f}% ({tot_ftm}/{tot_fta})")
    print("=" * 90)
    print(f"  {'比赛日期':<10} | {'对手':<6} | {'主客':<4} | {'MIN':>3} | {'PTS':>3} | {'FGM-A':>7} | {'3PM-A':>6} | {'FTM-A':>6} | {'REB':>3} | {'AST':>3} | {'STL':>3} | {'BLK':>3} | {'TO':>2} | {'+/-':>4} | {'GmSc':>5}")
    print(f"  {'-'*10}-+-{'-'*6}-+-{'-'*4}-+-{'-'*3}-+-{'-'*3}-+-{'-'*7}-+-{'-'*6}-+-{'-'*6}-+-{'-'*3}-+-{'-'*3}-+-{'-'*3}-+-{'-'*3}-+-{'-'*2}-+-{'-'*4}-+-{'-'*5}")
    
    for r in rows[-limit:]:
        g_date, opp, is_home, starter, mins, pts, fgm, fga, _, tpm, tpa, _, ftm, fta, _, oreb, dreb, reb, ast, stl, blk, tov, pm, gmsc, _, _ = r
        loc_str = "主场" if is_home else "客场"
        pm_str = f"{pm:+d}" if pm != 0 else "0"
        
        print(f"  {g_date:<10} | vs {opp:<3} | {loc_str:<4} | {mins:>3} | {pts:>3} | {fgm:>2}-{fga:<4} | {tpm:>2}-{tpa:<3} | {ftm:>2}-{fta:<3} | {reb:>3} | {ast:>3} | {stl:>3} | {blk:>3} | {tov:>2} | {pm_str:>4} | {gmsc:>5.1f}")


def query_leaders(conn: sqlite3.Connection, stat: str = "pts", limit: int = 10):
    stat_col_map = {
        "pts": ("points", "得分 (Points)"),
        "reb": ("reb", "篮板 (Rebounds)"),
        "ast": ("ast", "助攻 (Assists)"),
        "stl": ("stl", "抢断 (Steals)"),
        "blk": ("blk", "盖帽 (Blocks)"),
        "gamescore": ("game_score", "综合比赛评分 (GameScore)"),
        "pm": ("plus_minus", "正负值 (+/-)")
    }
    col, label = stat_col_map.get(stat.lower(), ("points", "得分 (Points)"))
    
    c = conn.cursor()
    c.execute(f"""
        SELECT player_name, team_abbr, opponent_abbr, game_date, points, reb, ast, stl, blk, {col}, game_uid
        FROM match_game_players
        ORDER BY {col} DESC
        LIMIT ?
    """, (limit,))
    rows = c.fetchall()
    
    print("=" * 86)
    print(f"  NBA 2K22 单场历史纪录排行榜: 【{label}】 TOP {limit}")
    print("=" * 86)
    print(f"  {'排名':<4} | {'数值':>6} | {'球员名称 (Player)':<22} | {'球队':<4} | {'对手':<4} | {'比赛日期':<10} | {'基础数据 (PTS/REB/AST)'}")
    print(f"  {'-'*4}-+-{'-'*6}-+-{'-'*22}-+-{'-'*4}-+-{'-'*4}-+-{'-'*10}-+-{'-'*24}")
    
    for idx, r in enumerate(rows, 1):
        name, tabbr, opp, g_date, pts, reb, ast, stl, blk, val, uid = r
        val_str = f"{val:.1f}" if isinstance(val, float) else f"{val}"
        print(f"  #{idx:<3} | {val_str:>6} | {name:<22} | {tabbr:<4} | {opp:<4} | {g_date:<10} | {pts}分 {reb}板 {ast}助 ({stl}断 {blk}帽)")


def query_standings(conn: sqlite3.Connection):
    c = conn.cursor()
    c.execute("""
        SELECT team_abbr,
               count(*) as gp,
               sum(is_win) as wins,
               sum(CASE WHEN is_win = 0 THEN 1 ELSE 0 END) as losses,
               round(avg(points), 1) as ppg,
               round(avg(points_allowed), 1) as opp_ppg,
               round(avg(points - points_allowed), 1) as diff,
               round(avg(ortg), 1) as avg_ortg,
               round(avg(drtg), 1) as avg_drtg,
               round(avg(net_rating), 1) as avg_net,
               round(avg(pace), 1) as avg_pace
        FROM match_game_teams
        GROUP BY team_abbr
        ORDER BY wins DESC, diff DESC
    """)
    rows = c.fetchall()
    
    print("=" * 90)
    print(f"  NBA 2K22 联盟实时排行榜 (基于已完赛场次真实技术统计生成)")
    print("=" * 90)
    print(f"  {'排名':<4} | {'球队':<5} | {'场次':>3} | {'胜-负':>6} | {'胜率':>6} | {'场均得分':>8} | {'场均失分':>8} | {'净胜分':>7} | {'ORTG':>5} | {'DRTG':>5} | {'NET':>6} | {'PACE':>5}")
    print(f"  {'-'*4}-+-{'-'*5}-+-{'-'*3}-+-{'-'*6}-+-{'-'*6}-+-{'-'*8}-+-{'-'*8}-+-{'-'*7}-+-{'-'*5}-+-{'-'*5}-+-{'-'*6}-+-{'-'*5}")
    
    for idx, r in enumerate(rows, 1):
        tabbr, gp, w, l, ppg, opp, diff, ortg, drtg, net, pace = r
        pct = (w / gp * 100) if gp > 0 else 0.0
        rec_str = f"{w}-{l}"
        print(f"  #{idx:<3} | {tabbr:<5} | {gp:>3} | {rec_str:>6} | {pct:>5.1f}% | {ppg:>8.1f} | {opp:>8.1f} | {diff:>+7.1f} | {ortg:>5.1f} | {drtg:>5.1f} | {net:>+6.1f} | {pace:>5.1f}")


def parse_args():
    parser = argparse.ArgumentParser(description="NBA 2K22 比赛历史与 BoxScore 查询工具")
    parser.add_argument("--db-path", default=None, help="SQLite 数据库文件路径")
    parser.add_argument("--save-id", default=None, help="存档 ID")
    parser.add_argument("--date", default=None, help="查询指定日期的所有比赛 (格式: YYYY-MM-DD)")
    parser.add_argument("--game", default=None, help="查询单场比赛 UID (例如: 2021-2022_G0001)")
    parser.add_argument("--team", default=None, help="查询球队比赛日志 (例如: MIL, GSW, LAL)")
    parser.add_argument("--player", default=None, help="查询球员全季比赛日志 (例如: 'Giannis Antetokounmpo')")
    parser.add_argument("--leaders", default=None, choices=["pts", "reb", "ast", "stl", "blk", "gamescore", "pm"], help="查询技术统计排行榜")
    parser.add_argument("--standings", action="store_true", help="查询全联盟实时排名与高阶战力榜")
    parser.add_argument("--limit", type=int, default=15, help="显示数量上限 (默认 15)")
    return parser.parse_args()


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        
    args = parse_args()
    target_db = resolve_db_path(args.db_path, args.save_id)
    
    if not os.path.exists(target_db):
        print(f"[!] 数据库文件不存在: {target_db}，请先运行数据采集脚本。")
        return 1

    conn = sqlite3.connect(target_db)
    try:
        if args.date:
            query_date_matches(conn, args.date)
        elif args.game:
            query_single_game(conn, args.game)
        elif args.team:
            query_team_history(conn, args.team, limit=args.limit)
        elif args.player:
            query_player_history(conn, args.player, limit=args.limit)
        elif args.leaders:
            query_leaders(conn, args.leaders, limit=args.limit)
        elif args.standings:
            query_standings(conn)
        else:
            # 默认展示全联盟最新进展与积分榜
            c = conn.cursor()
            c.execute("SELECT season_name, played_games, total_schedule_games, current_game_date FROM match_seasons ORDER BY created_at DESC LIMIT 1")
            s = c.fetchone()
            if s:
                print(f"[*] 当前赛季: {s[0]} | 已赛: {s[1]}/{s[2]} 场 | 游戏推进日期: {s[3]}\n")
            query_standings(conn)
    finally:
        conn.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
