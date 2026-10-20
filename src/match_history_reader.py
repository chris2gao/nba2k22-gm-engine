# -*- coding: utf-8 -*-
"""
NBA 2K22 赛季全量比赛历史与赛程技术统计抓取引擎 (Match History & Box Score Engine)
【核心职责】：
1. 从正在运行的 NBA2K22.exe 进程中定位 SEASON 根结构体 (3.5MB)。
2. 解码 SEASON_SCHEDULE 赛程表 (1,232 场比赛)、LineScore (四节与加时单节比分) 与 BOXSCORE。
3. 从 BOXSCORE_STATBANK 解码全场双方出场球员的 24 字节原生 BOXSCORE_STATLINE (出场时间、各项出手命中、正负值、对位防守失分)。
4. 纯确定性计算全套球队高阶数据 (ORTG, DRTG, NetRating, Pace, TS%, eFG%, 四要素) 与球员高阶数据 (GameScore, TS%, eFG%, USG%, 两双/三双)。
5. 结构化持久化至 match_seasons -> match_game_days -> match_games -> match_game_teams / match_game_players 五层关联数据库中。
"""

import os
import sys
import struct
import sqlite3
import ctypes
from typing import Dict, List, Any, Optional, Tuple

sys.path.insert(0, os.path.dirname(__file__))
from coach_locator import CoachLocator, live_memory, u64, read_exact
import config

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(PROJECT_DIR, "database", "match_history_schema.sql")
DEFAULT_PLAYERS_DB = os.path.join(PROJECT_DIR, "database", "nba2k22_players.sqlite")

SEASON_SLOT_RVA = 0x632B4B8 # NBA2K22.exe + 0x0632B4B8 points to live SEASON
GAMES_CAPACITY_MAX = 1742
SEASON_SCHEDULE_OFFSET = 40
STATBANK_OFFSET = 112308
NUMBER_OF_GAMES_OFFSET = 104520

GAME_PERIOD_NAMES = {
    0: "PRESEASON",
    1: "REGULAR",
    2: "REGULAR",
    3: "PLAYIN",
    4: "PLAYOFFS",
    5: "ALLSTAR"
}


def load_player_name_catalog(players_db_path: str = DEFAULT_PLAYERS_DB) -> Dict[int, str]:
    """加载球员原生 ID 到姓名的映射字典"""
    catalog = {}
    if os.path.exists(players_db_path):
        conn = sqlite3.connect(players_db_path)
        try:
            c = conn.cursor()
            c.execute("SELECT full_name, raw_struct FROM player_pool")
            for name, raw in c.fetchall():
                if raw and len(raw) >= 0x2FA:
                    pid = int.from_bytes(raw[0x2F8:0x2FA], 'little')
                    if pid != 0 and pid != 0xFFFF:
                        catalog[pid] = name
        finally:
            conn.close()
    return catalog


def ensure_match_history_schema(conn: sqlite3.Connection):
    """确保多赛季比赛关联数据表结构存在"""
    if os.path.exists(SCHEMA_PATH):
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            schema_sql = f.read()
        conn.executescript(schema_sql)
    conn.commit()


def decode_schedule_date(date_int: int) -> Tuple[int, int, int, str]:
    """
    解码 2K SCHEDULEDATE 32位位域
    bits 0..4: Id (5 bits)
    bits 5..15: MinutesSinceMidnight (11 bits)
    bits 16..20: Day (5 bits, 1..31)
    bits 21..24: Month (4 bits, 1..12)
    bits 25..31: BaseYearOffset (7 bits, 0..127) -> 2000 + offset
    """
    day = (date_int >> 16) & 0x1F
    month = (date_int >> 21) & 0x0F
    year_offset = (date_int >> 25) & 0x7F
    year = 2000 + year_offset
    date_str = f"{year:04d}-{month:02d}-{day:02d}"
    return year, month, day, date_str


DEFAULT_TEAM_MAP = {
    0: ("76ers", "PHI"), 1: ("Bucks", "MIL"), 2: ("Wizards", "WAS"), 3: ("Bulls", "CHI"),
    4: ("Cavaliers", "CLE"), 5: ("Celtics", "BOS"), 6: ("Clippers", "LAC"), 7: ("All-Stars East", "EST"),
    8: ("Grizzlies", "MEM"), 9: ("Hawks", "ATL"), 10: ("Heat", "MIA"), 11: ("Pelicans", "NOP"),
    12: ("Jazz", "UTA"), 13: ("Kings", "SAC"), 14: ("Knicks", "NYK"), 15: ("Lakers", "LAL"),
    16: ("Magic", "ORL"), 17: ("Mavericks", "DAL"), 18: ("Nets", "BKN"), 19: ("Nuggets", "DEN"),
    20: ("Pacers", "IND"), 21: ("Pistons", "DET"), 22: ("Raptors", "TOR"), 23: ("Rockets", "HOU"),
    24: ("Thunder", "OKC"), 25: ("Spurs", "SAS"), 26: ("Suns", "PHX"), 27: ("Timberwolves", "MIN"),
    28: ("Trail Blazers", "POR"), 29: ("Warriors", "GSW"), 30: ("All-Stars West", "WST"), 31: ("Hornets", "CHA")
}

def normalize_team_abbr(abbr: str) -> str:
    if abbr == "GS": return "GSW"
    if abbr == "NY": return "NYK"
    if abbr == "NO": return "NOP"
    if abbr == "SA": return "SAS"
    return abbr


class MatchHistoryReader:
    def __init__(self, mem=None, loc=None, players_db_path=DEFAULT_PLAYERS_DB):
        self.owns_mem = mem is None
        self.mem = mem or live_memory(read_only=True)
        self.base = self.mem.base_address
        self.player_names = load_player_name_catalog(players_db_path)
        
        # 缓存球队 ID 到 队名、简称的字典
        self.team_catalog = {}
        if isinstance(loc, dict):
            # 直接传入 teams 字典
            for tid, t in loc.items():
                name = t.get("name", DEFAULT_TEAM_MAP.get(tid, (f"Team {tid}", f"T{tid}"))[0])
                abbr = normalize_team_abbr(t.get("abbreviation", DEFAULT_TEAM_MAP.get(tid, ("", f"T{tid}"))[1]))
                self.team_catalog[tid] = {"name": name, "abbr": abbr}
        elif hasattr(loc, "teams"):
            for tid, t in loc.teams.items():
                name = t.get("name", DEFAULT_TEAM_MAP.get(tid, (f"Team {tid}", f"T{tid}"))[0])
                abbr = normalize_team_abbr(t.get("abbreviation", DEFAULT_TEAM_MAP.get(tid, ("", f"T{tid}"))[1]))
                self.team_catalog[tid] = {"name": name, "abbr": abbr}
        else:
            try:
                locator = CoachLocator(self.mem).calibrate()
                for tid, t in locator.teams.items():
                    name = t.get("name", DEFAULT_TEAM_MAP.get(tid, (f"Team {tid}", f"T{tid}"))[0])
                    abbr = normalize_team_abbr(t.get("abbreviation", DEFAULT_TEAM_MAP.get(tid, ("", f"T{tid}"))[1]))
                    self.team_catalog[tid] = {"name": name, "abbr": abbr}
            except Exception:
                pass
                
        # 补全默认球队映射
        for tid, (tname, tabbr) in DEFAULT_TEAM_MAP.items():
            if tid not in self.team_catalog:
                self.team_catalog[tid] = {"name": tname, "abbr": tabbr}

    def close(self):
        if self.owns_mem and self.mem:
            self.mem.close()

    def get_season_pointer(self) -> int:
        """获取当前正在运行的 SEASON 内存指针"""
        season_ptr = u64(self.mem, self.base + SEASON_SLOT_RVA)
        if not season_ptr or season_ptr < 0x10000:
            raise RuntimeError("SEASON_POINTER_NULL_OR_UNINITIALIZED")
        return season_ptr

    def capture_season_match_data(self, season_id: str = "2021-2022") -> Dict[str, Any]:
        """
        全量提取当前赛季的所有赛程、比赛结果、球队数据、球员 BoxScore 与进阶高阶数据
        """
        season_addr = self.get_season_pointer()
        sched_addr = season_addr + SEASON_SCHEDULE_OFFSET
        statbank_addr = season_addr + STATBANK_OFFSET
        
        # 1. 解码 SEASON 头部信息
        hdr = read_exact(self.mem, season_addr, 40)
        cur_date_int, period = struct.unpack_from("<II", hdr, 0)
        cur_year, cur_month, cur_day, cur_date_str = decode_schedule_date(cur_date_int)
        cur_game_idx, next_game_idx = struct.unpack_from("<II", hdr, 28)
        
        # 2. 读取 SCHEDULE 元信息
        num_games = struct.unpack("<I", read_exact(self.mem, sched_addr + NUMBER_OF_GAMES_OFFSET, 4))[0]
        if not (100 <= num_games <= GAMES_CAPACITY_MAX):
            raise RuntimeError(f"INVALID_SCHEDULE_GAMES_COUNT_{num_games}")
        allstar_idx = struct.unpack("<I", read_exact(self.mem, sched_addr + 111676, 4))[0]
        
        # 3. 批量读取所有 60 字节 SEASON_GAME 结构
        all_games_raw = read_exact(self.mem, sched_addr, 60 * num_games)
        
        games_list = []
        days_dict = {}
        total_played = 0
        
        for g_idx in range(num_games):
            g_raw = all_games_raw[g_idx * 60 : (g_idx + 1) * 60]
            
            date_val, pdate_val, g_id = struct.unpack_from("<III", g_raw, 0)
            home_id, away_id = struct.unpack_from("<HH", g_raw, 12)
            flags = struct.unpack_from("<I", g_raw, 56)[0]
            
            # 状态与模拟标记
            status = (flags >> 11) & 0x03 # 0: Scheduled, 1: In-Progress, 2: Final
            was_sim = (flags >> 18) & 0x01
            time_period_code = (flags >> 6) & 0x07
            is_nat_tv = (flags >> 20) & 0x01
            ot_count = flags & 0x3F
            
            # 日期解码
            g_yr, g_mo, g_day, g_date_str = decode_schedule_date(date_val)
            p_date_str = decode_schedule_date(pdate_val)[3] if pdate_val != 0 else g_date_str
            
            # 统计日历聚合
            day_entry = days_dict.setdefault(g_date_str, {
                "season_id": season_id, "game_date": g_date_str,
                "month": g_mo, "day": g_day, "scheduled_games": 0, "played_games": 0
            })
            day_entry["scheduled_games"] += 1
            
            # 只有已打完的比赛 (status == 2 或 was_sim == 1) 才采集详尽技术统计
            is_final = (status == 2 or was_sim == 1)
            if not is_final:
                continue
            
            day_entry["played_games"] += 1
            total_played += 1
            
            # 4. 解码 LineScore (单节比分)
            q1_h, q2_h, q3_h, q4_h = g_raw[44], g_raw[45], g_raw[46], g_raw[47]
            q1_a, q2_a, q3_a, q4_a = g_raw[48], g_raw[49], g_raw[50], g_raw[51]
            line_ot = struct.unpack_from("<I", g_raw, 52)[0]
            ot_h = line_ot & 0xFF
            ot_a = (line_ot >> 8) & 0xFF
            attendance = (line_ot >> 16) & 0x7FFF
            
            score_h = q1_h + q2_h + q3_h + q4_h + ot_h
            score_a = q1_a + q2_a + q3_a + q4_a + ot_a
            winner_id = home_id if score_h >= score_a else away_id
            diff = abs(score_h - score_a)
            
            game_uid = f"{season_id}_G{g_id:04d}"
            
            # 5. 解码 24 字节 BOXSCORE 结构体
            bs = g_raw[20:44]
            stat_idx = struct.unpack_from("<H", bs, 0)[0]
            num_h, num_a = bs[2], bs[3]
            
            # 主队专属比赛深层数据
            h_lead = bs[4]
            h_fb = bs[5]
            h_pip = bs[6]
            h_2nd = bs[7]
            h_poss_sec = (struct.unpack_from("<I", bs, 8)[0]) & 0x0FFF
            h_oreb_tm = (bs[9] >> 4) & 0x3F # team rebound
            h_dreb_tm = (struct.unpack_from("<H", bs, 10)[0] >> 2) & 0x3F
            h_pts_off_to = bs[11]
            
            # 客队专属比赛深层数据
            a_lead = bs[12]
            a_fb = bs[13]
            a_pip = bs[14]
            a_2nd = bs[15]
            a_poss_sec = (struct.unpack_from("<I", bs, 16)[0]) & 0x0FFF
            a_pts_off_to = bs[19]
            
            # 回合数
            w20 = struct.unpack_from("<I", bs, 20)[0]
            h_poss = max(1.0, float(w20 & 0xFF))
            a_poss = max(1.0, float((w20 >> 14) & 0xFF))
            
            # 6. 从 BOXSCORE_STATBANK 读取双方球员全量技术统计
            total_players = num_h + num_a
            statlines_raw = read_exact(self.mem, statbank_addr + stat_idx * 24, total_players * 24)
            
            players_data = []
            
            # 累加校验用的全队总计
            h_stats = {"fgm":0, "fga":0, "tpm":0, "tpa":0, "ftm":0, "fta":0, "oreb":0, "dreb":0, "ast":0, "stl":0, "blk":0, "tov":0, "pf":0}
            a_stats = {"fgm":0, "fga":0, "tpm":0, "tpa":0, "ftm":0, "fta":0, "oreb":0, "dreb":0, "ast":0, "stl":0, "blk":0, "tov":0, "pf":0}
            
            for p_idx in range(total_players):
                is_home_player = (p_idx < num_h)
                p_tid = home_id if is_home_player else away_id
                p_opp_tid = away_id if is_home_player else home_id
                p_team_abbr = self.team_catalog.get(p_tid, {}).get("abbr", f"T{p_tid}")
                p_opp_abbr = self.team_catalog.get(p_opp_tid, {}).get("abbr", f"T{p_opp_tid}")
                
                pline = statlines_raw[p_idx * 24 : (p_idx + 1) * 24]
                w0, w1, w2, w3, w4, w5 = struct.unpack("<IIIIII", pline)
                
                pid = w0 & 0xFFFF
                in_use = (w0 >> 16) & 0x01
                mins = (w0 >> 17) & 0x7F
                # +/- 有符号 8 位整数
                raw_pm = (w0 >> 24) & 0xFF
                pm = raw_pm - 256 if raw_pm > 127 else raw_pm
                
                fgm = w1 & 0xFF
                fga = (w1 >> 8) & 0x1FF
                tpm = (w1 >> 17) & 0x7F
                tpa = (w1 >> 24) & 0xFF
                
                fta = w2 & 0xFF
                stl = (w2 >> 8) & 0xFF
                blk = (w2 >> 16) & 0xFF
                dreb = (w2 >> 24) & 0xFF
                
                def_fgm = w3 & 0xFF
                def_fga = (w3 >> 8) & 0x1FF
                def_pts = (w3 >> 17) & 0x7FFF
                
                ast = w4 & 0x7F
                ftm = (w4 >> 7) & 0x7F
                oreb = (w4 >> 14) & 0xFF
                tov = (w4 >> 22) & 0x7F
                
                poss = w5 & 0xFF
                fouls = (w5 >> 8) & 0x0F
                started = (w5 >> 12) & 0x01
                
                pts = fgm * 2 + tpm + ftm
                reb = oreb + dreb
                
                # 进阶个人数据计算
                fg_pct = round(fgm / fga, 4) if fga > 0 else None
                tp_pct = round(tpm / tpa, 4) if tpa > 0 else None
                ft_pct = round(ftm / fta, 4) if fta > 0 else None
                def_fg_pct = round(def_fgm / def_fga, 4) if def_fga > 0 else None
                
                ts_attempts = fga + 0.44 * fta
                ts_pct = round(pts / (2 * ts_attempts), 4) if ts_attempts > 0 else None
                efg_pct = round((fgm + 0.5 * tpm) / fga, 4) if fga > 0 else None
                
                # Hollinger Game Score
                # GmSc = PTS + 0.4*FGM - 0.7*FGA - 0.4*(FTA - FTM) + 0.7*OREB + 0.3*DREB + STL + 0.7*AST + 0.7*BLK - 0.4*PF - TOV
                gm_sc = round(pts + 0.4 * fgm - 0.7 * fga - 0.4 * (fta - ftm) + 0.7 * oreb + 0.3 * dreb + stl + 0.7 * ast + 0.7 * blk - 0.4 * fouls - tov, 2)
                
                # 两双 / 三双判定
                categories_double = sum(val >= 10 for val in (pts, reb, ast, stl, blk))
                is_dd2 = categories_double >= 2
                is_td3 = categories_double >= 3
                ast_tov_ratio = round(ast / tov, 2) if tov > 0 else float(ast)
                
                # 累加全队
                cur_team_totals = h_stats if is_home_player else a_stats
                cur_team_totals["fgm"] += fgm; cur_team_totals["fga"] += fga
                cur_team_totals["tpm"] += tpm; cur_team_totals["tpa"] += tpa
                cur_team_totals["ftm"] += ftm; cur_team_totals["fta"] += fta
                cur_team_totals["oreb"] += oreb; cur_team_totals["dreb"] += dreb
                cur_team_totals["ast"] += ast; cur_team_totals["stl"] += stl
                cur_team_totals["blk"] += blk; cur_team_totals["tov"] += tov
                cur_team_totals["pf"] += fouls
                
                p_name = self.player_names.get(pid, f"Player_{pid}")
                
                players_data.append({
                    "game_uid": game_uid, "season_id": season_id, "game_date": g_date_str,
                    "player_id": pid, "player_name": p_name,
                    "team_id": p_tid, "team_abbr": p_team_abbr,
                    "opponent_team_id": p_opp_tid, "opponent_abbr": p_opp_abbr,
                    "is_home": is_home_player, "is_starter": bool(started),
                    "minutes": mins, "points": pts,
                    "fgm": fgm, "fga": fga, "fg_pct": fg_pct,
                    "tpm": tpm, "tpa": tpa, "tp_pct": tp_pct,
                    "ftm": ftm, "fta": fta, "ft_pct": ft_pct,
                    "oreb": oreb, "dreb": dreb, "reb": reb,
                    "ast": ast, "stl": stl, "blk": blk, "tov": tov, "pf": fouls,
                    "plus_minus": pm,
                    "defensive_fgm": def_fgm, "defensive_fga": def_fga, "defensive_fg_pct": def_fg_pct,
                    "defensive_pts_allowed": def_pts, "possessions": poss,
                    "ts_pct": ts_pct, "efg_pct": efg_pct, "usg_pct": None, # 填充完团队后再补全
                    "game_score": gm_sc, "pie": None, "ast_to_tov": ast_tov_ratio,
                    "double_double": is_dd2, "triple_double": is_td3
                })
            
            # 7. 构建双方球队的高阶数据行
            home_abbr = self.team_catalog.get(home_id, {}).get("abbr", f"T{home_id}")
            away_abbr = self.team_catalog.get(away_id, {}).get("abbr", f"T{away_id}")
            
            def build_team_row(tid, tabbr, opp_tid, opp_abbr, is_home, pts, opp_pts, stats, opp_stats, poss, lead, fb, pip, sec, poss_s, pts_to):
                fgm, fga = stats["fgm"], stats["fga"]
                tpm, tpa = stats["tpm"], stats["tpa"]
                ftm, fta = stats["ftm"], stats["fta"]
                oreb, dreb = stats["oreb"], stats["dreb"]
                reb = oreb + dreb
                opp_oreb, opp_dreb = opp_stats["oreb"], opp_stats["dreb"]
                
                fg_pct = round(fgm / fga, 4) if fga > 0 else 0.0
                tp_pct = round(tpm / tpa, 4) if tpa > 0 else 0.0
                ft_pct = round(ftm / fta, 4) if fta > 0 else 0.0
                efg_pct = round((fgm + 0.5 * tpm) / fga, 4) if fga > 0 else 0.0
                ts_att = fga + 0.44 * fta
                ts_pct = round(pts / (2 * ts_att), 4) if ts_att > 0 else 0.0
                
                # 攻防效率
                ortg = round((pts / poss) * 100, 2)
                drtg = round((opp_pts / poss) * 100, 2)
                net = round(ortg - drtg, 2)
                pace = round(poss * 48.0 / (48.0 + ot_count * 5.0), 2)
                
                # 篮板率
                oreb_pct = round(oreb / (oreb + opp_dreb), 4) if (oreb + opp_dreb) > 0 else 0.0
                dreb_pct = round(dreb / (dreb + opp_oreb), 4) if (dreb + opp_oreb) > 0 else 0.0
                reb_pct = round(reb / (reb + opp_oreb + opp_dreb), 4) if (reb + opp_oreb + opp_dreb) > 0 else 0.0
                ast_ratio = round(stats["ast"] / fgm, 4) if fgm > 0 else 0.0
                tov_denom = fga + 0.44 * fta + stats["tov"]
                tov_pct = round((stats["tov"] / tov_denom) * 100, 2) if tov_denom > 0 else 0.0
                
                return {
                    "game_uid": game_uid, "season_id": season_id, "game_date": g_date_str,
                    "team_id": tid, "team_abbr": tabbr, "opponent_team_id": opp_tid, "opponent_abbr": opp_abbr,
                    "is_home": is_home, "is_win": (pts > opp_pts),
                    "points": pts, "points_allowed": opp_pts,
                    "fgm": fgm, "fga": fga, "fg_pct": fg_pct,
                    "tpm": tpm, "tpa": tpa, "tp_pct": tp_pct,
                    "ftm": ftm, "fta": fta, "ft_pct": ft_pct,
                    "oreb": oreb, "dreb": dreb, "reb": reb,
                    "ast": stats["ast"], "stl": stats["stl"], "blk": stats["blk"],
                    "tov": stats["tov"], "pf": stats["pf"],
                    "pts_paint": pip, "pts_fastbreak": fb, "pts_2nd_chance": sec, "pts_off_to": pts_to,
                    "biggest_lead": lead, "possession_seconds": poss_s, "possessions": poss,
                    "ortg": ortg, "drtg": drtg, "net_rating": net, "pace": pace,
                    "efg_pct": efg_pct, "ts_pct": ts_pct,
                    "oreb_pct": oreb_pct, "dreb_pct": dreb_pct, "reb_pct": reb_pct,
                    "ast_ratio": ast_ratio, "tov_pct": tov_pct
                }
            
            team_rows = [
                build_team_row(home_id, home_abbr, away_id, away_abbr, True, score_h, score_a, h_stats, a_stats, h_poss, h_lead, h_fb, h_pip, h_2nd, h_poss_sec, h_pts_off_to),
                build_team_row(away_id, away_abbr, home_id, home_abbr, False, score_a, score_h, a_stats, h_stats, a_poss, a_lead, a_fb, a_pip, a_2nd, a_poss_sec, a_pts_off_to)
            ]
            
            # 8. 补全球员 USG%
            # USG% = 100 * ((FGA + 0.44 * FTA + TOV) * (Team MP / 5)) / (MP * (Team FGA + 0.44 * Team FTA + Team TOV))
            total_game_mins = 240 + ot_count * 25
            for p in players_data:
                p_mins = p["minutes"]
                t_stats = h_stats if p["is_home"] else a_stats
                team_usg_denom = t_stats["fga"] + 0.44 * t_stats["fta"] + t_stats["tov"]
                if p_mins > 0 and team_usg_denom > 0:
                    player_att = p["fga"] + 0.44 * p["fta"] + p["tov"]
                    usg = 100.0 * (player_att * (total_game_mins / 5.0)) / (p_mins * team_usg_denom)
                    p["usg_pct"] = round(usg, 2)
            
            game_obj = {
                "game_uid": game_uid,
                "season_id": season_id,
                "game_id": g_id,
                "game_date": g_date_str,
                "played_date": p_date_str,
                "game_type": GAME_PERIOD_NAMES.get(time_period_code, "REGULAR"),
                "home_team_id": home_id,
                "away_team_id": away_id,
                "home_team_abbr": home_abbr,
                "away_team_abbr": away_abbr,
                "home_score": score_h,
                "away_score": score_a,
                "winner_team_id": winner_id,
                "point_differential": diff,
                "overtime_count": ot_count,
                "attendance": attendance,
                "was_simulated": bool(was_sim),
                "status": status,
                "is_nationally_televised": bool(is_nat_tv),
                "home_q1": q1_h, "home_q2": q2_h, "home_q3": q3_h, "home_q4": q4_h, "home_ot": ot_h,
                "away_q1": q1_a, "away_q2": q2_a, "away_q3": q3_a, "away_q4": q4_a, "away_ot": ot_a,
                "team_stats": team_rows,
                "player_stats": players_data
            }
            games_list.append(game_obj)
        
        season_meta = {
            "season_id": season_id,
            "season_year": int(season_id.split("-")[-1]) if "-" in season_id else cur_year,
            "season_name": f"{season_id} NBA Season",
            "total_schedule_games": num_games,
            "played_games": total_played,
            "current_game_date": cur_date_str,
            "stage": GAME_PERIOD_NAMES.get(period, "REGULAR_SEASON"),
            "allstar_game_index": allstar_idx,
            "is_active": True
        }
        
        return {
            "season": season_meta,
            "days": list(days_dict.values()),
            "games": games_list
        }


def save_match_data_to_db(data: Dict[str, Any], db_path: Optional[str] = None, conn: Optional[sqlite3.Connection] = None) -> Dict[str, Any]:
    """将提取出的全部结构化比赛历史原子落库至 SQLite"""
    close_conn = False
    if conn is None:
        if not db_path:
            raise ValueError("Either db_path or conn must be provided")
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        conn = sqlite3.connect(db_path)
        close_conn = True
        
    try:
        ensure_match_history_schema(conn)
        cursor = conn.cursor()
        
        # 1. 写入 match_seasons
        s = data["season"]
        cursor.execute("""
            INSERT INTO match_seasons (
                season_id, season_year, season_name, total_schedule_games, played_games,
                current_game_date, stage, allstar_game_index, is_active, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
            ON CONFLICT(season_id) DO UPDATE SET
                played_games = excluded.played_games,
                current_game_date = excluded.current_game_date,
                stage = excluded.stage,
                allstar_game_index = excluded.allstar_game_index,
                is_active = excluded.is_active,
                updated_at = datetime('now')
        """, (
            s["season_id"], s["season_year"], s["season_name"], s["total_schedule_games"],
            s["played_games"], s["current_game_date"], s["stage"], s["allstar_game_index"],
            1 if s["is_active"] else 0
        ))
        
        # 2. 写入 match_game_days
        days_tuples = [
            (d["season_id"], d["game_date"], d["month"], d["day"], d.get("day_of_season", 0),
             d["scheduled_games"], d["played_games"])
            for d in data["days"]
        ]
        cursor.executemany("""
            INSERT INTO match_game_days (
                season_id, game_date, month, day, day_of_season, scheduled_games, played_games
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(season_id, game_date) DO UPDATE SET
                scheduled_games = excluded.scheduled_games,
                played_games = excluded.played_games
        """, days_tuples)
        
        # 3. 批量写入 match_games, match_game_teams, match_game_players
        games_inserted = 0
        teams_inserted = 0
        players_inserted = 0
        
        for g in data["games"]:
            cursor.execute("""
                INSERT OR REPLACE INTO match_games (
                    game_uid, season_id, game_id, game_date, played_date, game_type,
                    home_team_id, away_team_id, home_team_abbr, away_team_abbr,
                    home_score, away_score, winner_team_id, point_differential,
                    overtime_count, attendance, was_simulated, status, is_nationally_televised,
                    home_q1, home_q2, home_q3, home_q4, home_ot,
                    away_q1, away_q2, away_q3, away_q4, away_ot
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                g["game_uid"], g["season_id"], g["game_id"], g["game_date"], g["played_date"], g["game_type"],
                g["home_team_id"], g["away_team_id"], g["home_team_abbr"], g["away_team_abbr"],
                g["home_score"], g["away_score"], g["winner_team_id"], g["point_differential"],
                g["overtime_count"], g["attendance"], 1 if g["was_simulated"] else 0, g["status"], 1 if g["is_nationally_televised"] else 0,
                g["home_q1"], g["home_q2"], g["home_q3"], g["home_q4"], g["home_ot"],
                g["away_q1"], g["away_q2"], g["away_q3"], g["away_q4"], g["away_ot"]
            ))
            games_inserted += 1
            
            # 球队数据
            for t in g["team_stats"]:
                cursor.execute("""
                    INSERT OR REPLACE INTO match_game_teams (
                        game_uid, season_id, game_date, team_id, team_abbr, opponent_team_id, opponent_abbr,
                        is_home, is_win, points, points_allowed, fgm, fga, fg_pct, tpm, tpa, tp_pct,
                        ftm, fta, ft_pct, oreb, dreb, reb, ast, stl, blk, tov, pf,
                        pts_paint, pts_fastbreak, pts_2nd_chance, pts_off_to, biggest_lead,
                        possession_seconds, possessions, ortg, drtg, net_rating, pace,
                        efg_pct, ts_pct, oreb_pct, dreb_pct, reb_pct, ast_ratio, tov_pct
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    t["game_uid"], t["season_id"], t["game_date"], t["team_id"], t["team_abbr"],
                    t["opponent_team_id"], t["opponent_abbr"], 1 if t["is_home"] else 0, 1 if t["is_win"] else 0,
                    t["points"], t["points_allowed"], t["fgm"], t["fga"], t["fg_pct"],
                    t["tpm"], t["tpa"], t["tp_pct"], t["ftm"], t["fta"], t["ft_pct"],
                    t["oreb"], t["dreb"], t["reb"], t["ast"], t["stl"], t["blk"], t["tov"], t["pf"],
                    t["pts_paint"], t["pts_fastbreak"], t["pts_2nd_chance"], t["pts_off_to"],
                    t["biggest_lead"], t["possession_seconds"], t["possessions"],
                    t["ortg"], t["drtg"], t["net_rating"], t["pace"],
                    t["efg_pct"], t["ts_pct"], t["oreb_pct"], t["dreb_pct"], t["reb_pct"],
                    t["ast_ratio"], t["tov_pct"]
                ))
                teams_inserted += 1
                
            # 球员数据
            player_tuples = [
                (
                    p["game_uid"], p["season_id"], p["game_date"], p["player_id"], p["player_name"],
                    p["team_id"], p["team_abbr"], p["opponent_team_id"], p["opponent_abbr"],
                    1 if p["is_home"] else 0, 1 if p["is_starter"] else 0, p["minutes"],
                    p["points"], p["fgm"], p["fga"], p["fg_pct"], p["tpm"], p["tpa"], p["tp_pct"],
                    p["ftm"], p["fta"], p["ft_pct"], p["oreb"], p["dreb"], p["reb"],
                    p["ast"], p["stl"], p["blk"], p["tov"], p["pf"], p["plus_minus"],
                    p["defensive_fgm"], p["defensive_fga"], p["defensive_fg_pct"],
                    p["defensive_pts_allowed"], p["possessions"],
                    p["ts_pct"], p["efg_pct"], p["usg_pct"], p["game_score"], p["pie"],
                    p["ast_to_tov"], 1 if p["double_double"] else 0, 1 if p["triple_double"] else 0
                )
                for p in g["player_stats"]
            ]
            cursor.executemany("""
                INSERT OR REPLACE INTO match_game_players (
                    game_uid, season_id, game_date, player_id, player_name, team_id, team_abbr,
                    opponent_team_id, opponent_abbr, is_home, is_starter, minutes, points,
                    fgm, fga, fg_pct, tpm, tpa, tp_pct, ftm, fta, ft_pct,
                    oreb, dreb, reb, ast, stl, blk, tov, pf, plus_minus,
                    defensive_fgm, defensive_fga, defensive_fg_pct, defensive_pts_allowed, possessions,
                    ts_pct, efg_pct, usg_pct, game_score, pie, ast_to_tov, double_double, triple_double
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, player_tuples)
            players_inserted += len(player_tuples)
            
        if close_conn:
            conn.commit()
            
        return {
            "season_id": s["season_id"],
            "total_schedule_games": s["total_schedule_games"],
            "played_games": s["played_games"],
            "days_recorded": len(data["days"]),
            "games_stored": games_inserted,
            "team_records_stored": teams_inserted,
            "player_boxscores_stored": players_inserted
        }
    finally:
        if close_conn:
            conn.close()
