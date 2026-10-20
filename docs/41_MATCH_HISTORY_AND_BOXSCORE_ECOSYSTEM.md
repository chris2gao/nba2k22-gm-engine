# NBA 2K22 赛季全量常规赛/季后赛历史比赛数据系统 (Match History & Box Score Ecosystem)

> **文档代号**: 41_MATCH_HISTORY_AND_BOXSCORE_ECOSYSTEM  
> **制定版本**: v1.0 (2026-10-20)  
> **所属模块**: 数据采集引擎 (Data Acquisition & Analytics Layer)  
> **核心原则**: 100% 游戏实机物理内存观测、纯确定性衍生推导、AI 零幻觉、支持跨越 100 个赛季纵向长周期大数据库架构。

---

## 1. 架构定位与业务拓扑

在原有的 NBA 2K22 Antigravity 外部 GM 引擎中，系统主要按“月度快照 (Monthly Snapshots)”进行月度结算。为了实现更深度的 GM 战术分析、球员交易价值评估、MVP/DPOY/最佳阵容评选、负荷管理及全联盟历史纵向比对，本模块建立了**按自然日历与单场比赛粒度的 5 层关系型数据库建模**：

```mermaid
flowchart TD
    S["1. 赛季总账表 (match_seasons)<br/>- 100个赛季唯一标识<br/>- 赛程总规划与阶段"]
    D["2. 比赛日历表 (match_game_days)<br/>- 年-月-日日历索引<br/>- 当日排期与完赛聚合"]
    G["3. 单场比赛总体表 (match_games)<br/>- 比赛 UID / 双方比分<br/>- 四节及加时比分 LineScore<br/>- 上座人数 / 胜者 / 焦点标记"]
    T["4. 球队比赛数据表 (match_game_teams)<br/>- 双方全场传统技术统计<br/>- 2K 原生禁区/快攻/二次进攻/失误转化得分<br/>- ORTG / DRTG / NetRating / Pace 高阶数据"]
    P["5. 球员比赛数据表 (match_game_players)<br/>- 双方每位登场球员详尽 BoxScore<br/>- 2K 原生对位防守失分与命中限制<br/>- Hollinger GameScore / TS% / eFG% / USG% / 两双三双"]

    S -->|1:N (game_date)| D
    D -->|1:N (game_uid)| G
    G -->|1:2 (game_uid)| T
    G -->|1:20~26 (game_uid)| P
```

---

## 2. 2K 原生内存结构体逆向映射标准

通过逆向分析 `NBA2K22.exe` 运行时内存与反射元数据，核心比赛数据均挂载于全局 `SEASON` 结构体：

### 2.1 全局指针与根对象
- **静态全局插槽 RVA**: `NBA2K22.exe + 0x0632B4B8` (`0x14632B4B8`)
- **根结构体名称**: `SEASON` (总大小: 3,526,944 字节 ≈ 3.36 MB)
- **关键偏移**:
  - `+0x00`: 当前游戏日期 `Date` (4 字节 packed bitfield `SCHEDULEDATE`)
  - `+0x04`: 赛季阶段 `Period` (4 字节: 0=Preseason, 1=Regular, 3=Playin, 4=Playoffs)
  - `+0x28`: 当前正在进行的比赛索引 (`CurrentGameIndex`, uint32)
  - `+0x28 (40)`: `Schedule` (大小 111,688 字节，容量 1,232 场)
  - `+0x1B6AC (112,308)`: `BoxScoreStatBank` (大小 1,087,012 字节，容量 45,292 球员统计行)
  - `+0x19848 (104,520)`: 赛程场次总数 (`NumberOfGames`, uint32，标准常规赛为 1,230)

### 2.2 日期位域 (`SCHEDULEDATE`, 4 字节)
- **Bits 0..4 (5 bits)**: 日期内部 ID
- **Bits 5..15 (11 bits)**: 距离午夜的分钟数 (`MinutesSinceMidnight`)
- **Bits 16..20 (5 bits)**: 日 (1..31)
- **Bits 21..24 (4 bits)**: 月 (1..12)
- **Bits 25..31 (7 bits)**: 基础年份偏移量 (`BaseYearOffset`) $\rightarrow$ 年份 = $2000 + \text{offset}$ (例如 $2000 + 21 = 2021$)

### 2.3 单场赛程结构体 (`SEASON_GAME`, 60 字节)
- `+0x00` (uint32): 计划比赛日期 (`SCHEDULEDATE`)
- `+0x04` (uint32): 实际完赛日期 (`SCHEDULEDATE`)
- `+0x08` (uint32): 比赛编号 (`GameId`, 1..1232)
- `+0x0C` (uint16): 主队 ID (`HomeTeamId`, 0..35)
- `+0x0E` (uint16): 客队 ID (`AwayTeamId`, 0..35)
- `+0x14` (24 字节): `BOXSCORE` 比赛整体高阶统计容器
- `+0x2C` (8 字节): 单节比分明细 `LineScore` (主队 Q1~Q4 各 1 字节；客队 Q1~Q4 各 1 字节)
- `+0x34` (uint32): 主队加时总得分 (Byte 0)、客队加时总得分 (Byte 1)、观众人数 `Attendance` (Bits 16..30)
- `+0x38` (uint32): 状态标记 Flags:
  - `Bits 0..5`: 加时赛节数 (0=常规四节, 1=1OT, 2=2OT...)
  - `Bits 6..8`: 时间段编码 (0=Preseason, 1=Regular, 4=Playoffs)
  - `Bits 11..12`: 比赛终局状态 `Status` (0=未开打, 1=进行中, 2=已终局 Final)
  - `Bit 18`: 模拟标记 `WasSimulated` (1=日历模拟, 0=3D 实时操控)
  - `Bit 20`: 全美直播标记 `IsNationallyTelevised`

### 2.4 原生比赛概况结构体 (`BOXSCORE`, 24 字节)
- `+0x00` (uint16): `StatLinesIndex` (指向 `BOXSCORE_STATBANK` 的起始槽位索引)
- `+0x02` (uint8): 主队出场球员统计数 `NumberOfHomeStats`
- `+0x03` (uint8): 客队出场球员统计数 `NumberOfAwayStats`
- `+0x04` (4 字节): 主队最大领先分 `Lead`、快攻得分 `FastBreak`、内线得分 `PointsInPaint`、二次进攻得分 `2ndChance`
- `+0x08` (4 字节): 主队控球时长秒数 `PossessionSeconds`、主队团队篮板、失误转化得分 `PointsOffTO`
- `+0x0C` (4 字节): 客队最大领先分、快攻得分、内线得分、二次进攻得分
- `+0x10` (4 字节): 客队控球时长秒数、客队团队篮板、失误转化得分
- `+0x14` (uint32): 回合数 `Possessions` (主队 Bits 0..7, 客队 Bits 14..21)

### 2.5 球员单场统计结构体 (`BOXSCORE_STATLINE`, 24 字节)
- **Word 0 (uint32)**:
  - `Bits 0..15`: 2K 原生球员 ID (`PlayerId`，对应 `player_pool.sqlite` 中的 `0x2F8` uint16 原生 ID)
  - `Bit 16`: 在用标记 `InUse`
  - `Bits 17..23`: 出场实机分钟数 `Minutes`
  - `Bits 24..31`: 正负值 `PlusMinus` (带符号 8 位整数，-128 ~ +127)
- **Word 1 (uint32)**:
  - `Bits 0..7`: 投篮命中 `FGM`
  - `Bits 8..16`: 投篮出手 `FGA` (9 bits, 0..511)
  - `Bits 17..23`: 三分命中 `3PM`
  - `Bits 24..31`: 三分出手 `3PA`
- **Word 2 (uint32)**:
  - `Bits 0..7`: 罚球出手 `FTA`
  - `Bits 8..15`: 抢断 `STL`
  - `Bits 16..23`: 盖帽 `BLK`
  - `Bits 24..31`: 防守篮板 `DREB`
- **Word 3 (uint32) - 2K 专属对位防守监测**:
  - `Bits 0..7`: 对位防守时被对手打进球数 `DefensiveFieldGoalsMade`
  - `Bits 8..16`: 对位防守时被对手出手数 `DefensiveFieldGoalsAttempted`
  - `Bits 17..31`: 对位防守时总失分数 `TotalPointsAllowed`
- **Word 4 (uint32)**:
  - `Bits 0..6`: 助攻 `AST`
  - `Bits 7..13`: 罚球命中 `FTM`
  - `Bits 14..21`: 进攻篮板 `OREB`
  - `Bits 22..28`: 失误 `TOV`
- **Word 5 (uint32)**:
  - `Bits 0..7`: 个人参与进攻回合数 `Possessions`
  - `Bits 8..11`: 个人犯规数 `Fouls`
  - `Bit 12`: 是否首发先发 `GamesStarted` (1=首发, 0=替补)

---

## 3. 高阶数据计算与衍生数学模型

外部 GM 引擎采用纯确定性公式对提取的数据进行二次建模：

### 3.1 真实命中率 (True Shooting Percentage, TS%)
$$\text{TS\%} = \frac{\text{PTS}}{2 \times (\text{FGA} + 0.44 \times \text{FTA})}$$

### 3.2 有效命中率 (Effective Field Goal Percentage, eFG%)
$$\text{eFG\%} = \frac{\text{FGM} + 0.5 \times \text{3PM}}{\text{FGA}}$$

### 3.3 球权使用率 (Usage Percentage, USG%)
$$\text{USG\%} = 100 \times \frac{(\text{FGA} + 0.44 \times \text{FTA} + \text{TOV}) \times (\text{Team\_MP} / 5)}{\text{MP} \times (\text{Team\_FGA} + 0.44 \times \text{Team\_FTA} + \text{Team\_TOV})}$$

### 3.4 霍林格单场综合表现分 (John Hollinger Game Score)
$$\begin{aligned}
\text{GameScore} = &\ \text{PTS} + 0.4 \times \text{FGM} - 0.7 \times \text{FGA} - 0.4 \times (\text{FTA} - \text{FTM}) \\
&+ 0.7 \times \text{OREB} + 0.3 \times \text{DREB} + \text{STL} + 0.7 \times \text{AST} + 0.7 \times \text{BLK} \\
&- 0.4 \times \text{PF} - \text{TOV}
\end{aligned}$$

### 3.5 球队进攻与防守百回合效率 (ORTG / DRTG / NetRating)
$$\text{ORTG} = \frac{\text{Team\_PTS}}{\text{Possessions}} \times 100$$
$$\text{DRTG} = \frac{\text{Opponent\_PTS}}{\text{Possessions}} \times 100$$
$$\text{NetRating} = \text{ORTG} - \text{DRTG}$$

### 3.6 比赛标准节奏 (Pace)
$$\text{Pace} = \text{Possessions} \times \frac{48}{48 + 5 \times \text{OvertimeCount}}$$

---

## 4. 数据库表结构规范 (SQLite DDL)

数据持久化于 `league_state.sqlite` 中，五张核心关系表如下：

1. **`match_seasons`**: 赛季元信息主表，存储 `season_id`、计划赛程场次、已赛场次、当前日期、阶段。
2. **`match_game_days`**: 日历索引表，存储自然日、所属月份、当日计划赛程场次与已赛场次。
3. **`match_games`**: 比赛主表，存储 `game_uid`（主键，格式 `{season_id}_G{game_id:04d}`）、主客队 ID 与缩写、终局总分、胜者、分差、四节单节与加时单节比分、观众上座数、模拟标识。
4. **`match_game_teams`**: 球队单场表现表（每场 2 行），存储双边全套攻防基础与高阶数据（投篮、三分、罚球、篮板冲抢率、禁区得分、快攻得分、失误转化得分、最大领先分、ORTG、DRTG、NetRating、Pace）。
5. **`match_game_players`**: 球员单场表现表（每场 20~26 行），存储每位球员的先发状态、实机分钟数、得篮助断帽犯失正负值、对位防守被进球数/被出手数/对位失分、GameScore、TS%、eFG%、USG%、两双/三双标记。

---

## 5. 命令行工具与接口使用指南

### 5.1 全自动数据采集
当运行月度采集流水线时，比赛历史会自动原子入库：
```powershell
python src/auto_pipeline_ingest.py --season-year 2022 --month-idx 1 --month-name NOV
```
亦可使用独立采集脚本随时全量采集当前赛季的所有比赛：
```powershell
python scripts/capture_match_history.py --season-id 2021-2022
```

### 5.2 比赛数据查询与分析工具 (`scripts/query_match_history.py`)

#### 查询 1: 按比赛日期查当日所有对决与关键球员
```powershell
python scripts/query_match_history.py --date 2021-10-19
```

#### 查询 2: 查看单场比赛详尽双边对比与球员完整 BoxScore
```powershell
python scripts/query_match_history.py --game 2021-2022_G0234
```

#### 查询 3: 查询球队赛季完整赛程与战报日志 (Game Log)
```powershell
python scripts/query_match_history.py --team MIL
```

#### 查询 4: 查询球员个人全季表现与场均进阶三项命中率
```powershell
python scripts/query_match_history.py --player "Giannis Antetokounmpo"
```

#### 查询 5: 全联盟单场数据排行榜 (高分榜 / GameScore 榜)
```powershell
python scripts/query_match_history.py --leaders gamescore --limit 10
python scripts/query_match_history.py --leaders pts --limit 10
```

#### 查询 6: 全联盟各队实时战绩、攻防效率与净效率排行榜
```powershell
python scripts/query_match_history.py --standings
```

---

## 6. 系统安全性与自动化守护

- **只读内存安全**: 数据采集模块采用纯确定性只读 Windows API (`OpenProcess(PROCESS_VM_READ)`、`ReadProcessMemory`)，绝不对游戏内存执行任何写入或注入，确保游戏进程零崩溃风险。
- **原子事务保障**: 数据库写入遵循 SQLite 严格事务机制，全季所有比赛、球队、球员技术统计在同一事务内完成，中途发生任何异常自动回滚，杜绝半写入脏数据。
- **幂等兼容性**: 表主键设计为 `game_uid`、`(game_uid, team_id)`、`(game_uid, player_id)`，结合 `INSERT OR REPLACE` 策略，支持重复执行无缝更新。
