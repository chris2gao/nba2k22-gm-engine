# -*- coding: utf-8 -*-
"""
NBA 2K22 球队战术策略、战术手册与商业运营管理器 (Strategy & Business Manager)
支持：
1. 球队攻防策略与战术重点 (Points of Emphasis, POEs) 读写调优：
   - 比赛节奏 (Pace)、快攻推进 (Fastbreak)、前板冲抢 (Off Rebound)
   - 对球施压 (On-Ball Pressure)、无球盯防 (Off-Ball)、挡拆防守 (P&R Defense: Switch/Drop/Ice/Trap)
2. 战术手册与教练体系联动 (Coach System & Playbook Alignment)
3. 主场球票分级定价与特许商品运营 (Lower Bowl, Upper Bowl, Concessions, Fan Interest)
"""
import os
import sys
import math
from typing import Dict, Optional

sys.path.append(os.path.dirname(__file__))
from memory import GameMemory
from scanner import LeagueScanner
import config

# ==========================================
# 攻防策略 (POEs) 偏移字典 (基于 Team 结构体)
# ==========================================
STRATEGY_OFFSETS = {
    "OFF_PACE": 0xEB2,              # 进攻节奏 (0: 慢速阵地, 3: 平衡, 5: 高速跑轰)
    "FASTBREAK_FOCUS": 0xEB3,       # 快攻推进重点 (0: 稳扎稳打, 3: 寻找快攻, 5: 坚决快攻)
    "OFF_REBOUND": 0xEB4,           # 前场篮板冲抢 (0: 快速回防, 3: 平衡, 5: 疯狂冲抢)
    "DEF_REBOUND": 0xEB5,           # 防守篮板策略 (0: 抓板即推快攻, 3: 保底保护)
    "ON_BALL_PRESSURE": 0xEB7,      # 对球施压 (0: 留空间放投, 1: 适度, 3: 贴身紧逼, 4: 窒息撕咬)
    "OFF_BALL_PRESSURE": 0xEB8,     # 无球盯防 (0: 缩进油漆区, 1: 适度, 2: 紧贴阻绝传球 Deny)
    "PICK_AND_ROLL_DEF": 0xEB9,     # 挡拆防守针对 (0: 自动, 1: 沉退 Drop, 2: 冰封 Ice, 3: 软延误 Soft, 4: 硬延误 Hard, 5: 夹击 Trap, 6: 无限换防 Switch)
    "HELP_DEFENSE_LEVEL": 0xEBC,    # 弱侧协防轮转等级 (0: 单防不协防, 3: 标准轮转, 5: 极速补位协防)
}

# ==========================================
# 场馆商业与物价偏移字典 (基于 Team 结构体)
# ==========================================
BUSINESS_OFFSETS = {
    "TICKET_LOWER_BOWL": 0xF8C,     # 下层看台票价 (float)
    "TICKET_UPPER_BOWL": 0xF90,     # 上层看台平民票价 (float)
    "TICKET_CLUB_LEVEL": 0xF94,     # 贵宾俱乐部票价 (float)
    "TICKET_COURTSIDE": 0xF98,      # 场边VIP/平均指导票价 (float)
    "PARKING_FEE": 0xF9C,           # 停车费 (float)
    "CONCESSION_BEER": 0xFA0,       # 啤酒饮料售价 (float)
    "CONCESSION_HOTDOG": 0xFA4,     # 热狗食品售价 (float)
    "CONCESSION_SODA": 0xFA8,       # 碳酸汽水售价 (float)
    "MERCH_HAT": 0xFB0,             # 球队主题球帽售价 (float)
    "MERCH_TSHIRT": 0xFB8,          # 球队官方T恤售价 (float)
    "MERCH_JERSEY": 0xFC0,          # 官方复刻比赛球衣售价 (float)
    "FAN_INTEREST": 0xF7C,          # 球迷热度 (float, 0.0 ~ 1.0)
    "GATE_REVENUE": 0xFD8,          # 门票总收入 (uint32)
    "MERCH_REVENUE": 0xFDC,         # 周边商品总收入 (uint32)
}

class StrategyManager:
    def __init__(self, mem: Optional[GameMemory] = None):
        self.mem = mem or GameMemory()
        self.scanner = LeagueScanner(self.mem)
        self.teams = self.scanner.find_active_teams()

    def get_team_strategy(self, team_id: int) -> Optional[Dict]:
        """读取指定球队当前攻防策略重点"""
        if team_id not in self.teams:
            return None
        base = self.teams[team_id]["address"]
        return {
            "team_name": self.teams[team_id]["name"],
            "off_pace": self.mem.require_uint8(base + STRATEGY_OFFSETS["OFF_PACE"]),
            "fastbreak_focus": self.mem.require_uint8(base + STRATEGY_OFFSETS["FASTBREAK_FOCUS"]),
            "off_rebound": self.mem.require_uint8(base + STRATEGY_OFFSETS["OFF_REBOUND"]),
            "def_rebound": self.mem.require_uint8(base + STRATEGY_OFFSETS["DEF_REBOUND"]),
            "on_ball_pressure": self.mem.require_uint8(base + STRATEGY_OFFSETS["ON_BALL_PRESSURE"]),
            "off_ball_pressure": self.mem.require_uint8(base + STRATEGY_OFFSETS["OFF_BALL_PRESSURE"]),
            "pnr_def": self.mem.require_uint8(base + STRATEGY_OFFSETS["PICK_AND_ROLL_DEF"]),
            "help_def": self.mem.require_uint8(base + STRATEGY_OFFSETS["HELP_DEFENSE_LEVEL"]),
        }

    def set_team_strategy(self, team_id: int, **kwargs) -> bool:
        """设置指定球队攻防策略"""
        if team_id not in self.teams:
            return False
        base = self.teams[team_id]["address"]
        writes = []
        for key, val in kwargs.items():
            k_upper = key.upper()
            if k_upper not in STRATEGY_OFFSETS:
                raise ValueError(f"未知的球队策略字段: {key}")
            value = int(val)
            if not 0 <= value <= 255:
                raise ValueError(f"策略字段 {key} 超出 uint8 范围: {value}")
            writes.append((key, base + STRATEGY_OFFSETS[k_upper], value))
        for key, address, value in writes:
            if not self.mem.write_uint8(address, value):
                raise OSError(f"写入球队 {team_id} 策略字段 {key} 失败")
        for key, address, value in writes:
            actual = self.mem.require_uint8(address)
            if actual != value:
                raise OSError(f"球队 {team_id} 策略字段 {key} 回读不符: 期望 {value}, 实际 {actual}")
        return True

    def get_team_business(self, team_id: int) -> Optional[Dict]:
        """读取指定球队商业与票价参数"""
        if team_id not in self.teams:
            return None
        base = self.teams[team_id]["address"]
        return {
            "team_name": self.teams[team_id]["name"],
            "ticket_lower": round(self.mem.require_float(base + BUSINESS_OFFSETS["TICKET_LOWER_BOWL"]), 2),
            "ticket_upper": round(self.mem.require_float(base + BUSINESS_OFFSETS["TICKET_UPPER_BOWL"]), 2),
            "ticket_courtside": round(self.mem.require_float(base + BUSINESS_OFFSETS["TICKET_COURTSIDE"]), 2),
            "beer_price": round(self.mem.require_float(base + BUSINESS_OFFSETS["CONCESSION_BEER"]), 2),
            "hotdog_price": round(self.mem.require_float(base + BUSINESS_OFFSETS["CONCESSION_HOTDOG"]), 2),
            "jersey_price": round(self.mem.require_float(base + BUSINESS_OFFSETS["MERCH_JERSEY"]), 2),
            "fan_interest": round(self.mem.require_float(base + BUSINESS_OFFSETS["FAN_INTEREST"]), 2),
            "gate_revenue": self.mem.require_uint32(base + BUSINESS_OFFSETS["GATE_REVENUE"]),
        }

    def set_ticket_pricing(self, team_id: int, courtside: float, lower: float, upper: float) -> bool:
        """分级设置球票价格"""
        if team_id not in self.teams:
            return False
        base = self.teams[team_id]["address"]
        values = {
            "ticket_courtside": (BUSINESS_OFFSETS["TICKET_COURTSIDE"], float(courtside)),
            "ticket_lower": (BUSINESS_OFFSETS["TICKET_LOWER_BOWL"], float(lower)),
            "ticket_upper": (BUSINESS_OFFSETS["TICKET_UPPER_BOWL"], float(upper)),
        }
        for name, (_, value) in values.items():
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} 必须是有限的非负价格")
        for name, (offset, value) in values.items():
            if not self.mem.write_float(base + offset, value):
                raise OSError(f"写入球队 {team_id} {name} 失败")
        for name, (offset, expected) in values.items():
            actual = self.mem.require_float(base + offset)
            if not math.isfinite(actual) or not math.isclose(actual, expected, rel_tol=1e-6, abs_tol=0.02):
                raise OSError(f"球队 {team_id} {name} 回读不符: 期望 {expected}, 实际 {actual}")
        return True

if __name__ == "__main__":
    mgr = StrategyManager()
    print("=== 全联盟代表性球队攻防策略与门票经济抽检 ===")
    for tid in [20, 29, 10, 8]:  # IND, GSW, MIA, MEM
        strat = mgr.get_team_strategy(tid)
        biz = mgr.get_team_business(tid)
        print(f"\n[{strat['team_name']}]")
        print(f"  - 攻防策略: 进攻节奏={strat['off_pace']}, 快攻={strat['fastbreak_focus']}, 对球施压={strat['on_ball_pressure']}, 挡拆防守={strat['pnr_def']}")
        print(f"  - 主场经济: 场边票=${biz['ticket_courtside']:.2f}, 下层票=${biz['ticket_lower']:.2f}, 上层票=${biz['ticket_upper']:.2f}, 球衣=${biz['jersey_price']:.2f}, 球迷热度={biz['fan_interest']}")
