# -*- coding: utf-8 -*-
"""
NBA 2K22 赛季比赛历史与技术统计采集命令行工具 (Match History Capture CLI)
用法示例:
    python scripts/capture_match_history.py --season-id 2021-2022
    python scripts/capture_match_history.py --save-id default --season-id 2021-2022
"""

import os
import sys
import argparse
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from match_history_reader import MatchHistoryReader, save_match_data_to_db
import save_context


def parse_args():
    parser = argparse.ArgumentParser(description="NBA 2K22 全量比赛历史与 BoxScore 采集工具")
    parser.add_argument("--save-id", default=None, help="目标存档 ID (例如 mc_haliburton_2021, default)")
    parser.add_argument("--season-id", default="2021-2022", help="赛季标识符 (例如 2021-2022)")
    parser.add_argument("--db-path", default=None, help="自定义写入的 SQLite 数据库路径")
    parser.add_argument("--dry-run", action="store_true", help="只读提取并打印摘要，不写入数据库")
    return parser.parse_args()


def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    
    # 确定数据库物理路径
    if args.db_path:
        target_db = args.db_path
    elif args.save_id:
        context = save_context.resolve_context(args.save_id)
        target_db = context["db_path"]
    else:
        target_db = str(ROOT / "database" / "league_state.sqlite")
        
    print(f"[*] 启动赛季比赛数据采集引擎...")
    print(f"[*] 目标赛季: {args.season_id}")
    print(f"[*] 目标数据库: {target_db}")
    
    reader = MatchHistoryReader()
    try:
        data = reader.capture_season_match_data(season_id=args.season_id)
        
        season = data["season"]
        games = data["games"]
        days = data["days"]
        
        print("\n" + "="*50)
        print("★ 赛季比赛数据采集成功 ★")
        print("="*50)
        print(f"- 赛季名称: {season['season_name']}")
        print(f"- 赛程规划总场次: {season['total_schedule_games']}")
        print(f"- 当前已赛场次: {season['played_games']}")
        print(f"- 当前游戏推进日期: {season['current_game_date']}")
        print(f"- 赛程总日历天数: {len(days)} 天")
        print(f"- 成功提取完赛 BoxScore: {len(games)} 场")
        
        total_team_records = sum(len(g["team_stats"]) for g in games)
        total_player_records = sum(len(g["player_stats"]) for g in games)
        print(f"- 提取球队单场高阶记录: {total_team_records} 条")
        print(f"- 提取球员单场高阶记录: {total_player_records} 条")
        
        # 统计本月精彩个人单场表现
        top_scorers = []
        for g in games:
            for p in g["player_stats"]:
                if p["points"] >= 35:
                    top_scorers.append((p["points"], p["player_name"], p["team_abbr"], g["game_date"], p["game_score"]))
        top_scorers.sort(key=lambda x: x[0], reverse=True)
        
        if top_scorers:
            print(f"\n[!] 本月单场 35+ 高分巨星表现 (前 5 名):")
            for pts, name, team, dt, gmsc in top_scorers[:5]:
                print(f"    * {dt} | {name} ({team}) 砍下 {pts} 分 | GameScore: {gmsc}")

        if args.dry_run:
            print("\n[+] --dry-run 模式生效，数据未写入磁盘。")
            return 0
            
        print(f"\n[*] 正在原子写入关系型数据库...")
        counts = save_match_data_to_db(data, target_db)
        print(f"[+] 数据成功持久化落库！")
        print(f"    - 日历天数已同步: {counts['days_recorded']}")
        print(f"    - 比赛总表已同步: {counts['games_stored']}")
        print(f"    - 球队比赛数据表已同步: {counts['team_records_stored']}")
        print(f"    - 球员比赛数据表已同步: {counts['player_boxscores_stored']}")
        
    finally:
        reader.close()
        
    return 0


if __name__ == "__main__":
    sys.exit(main())
