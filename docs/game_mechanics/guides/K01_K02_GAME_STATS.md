# K01/K02 — NBA2K20–23 终极联盟逐场比赛、Box Score、Game Logs、投篮和高级统计实用指南

> DEV29 V2 / R01-A，2026-10-20，研究主目标 **NBA2K22 PC 本世代离线 MyLEAGUE**。研究文献涉及 NBA2K20–23、PS4/PC本世代和PS5次世代；跨版本经验可指导查找和经营，不等于已获得 PC22 内存认证。
>
> **当前研究状态：`INCOMPLETE_WITH_OPEN_ITEMS`**（第一批可用攻略已交付）；**目标游戏原生状态：`UNKNOWN / PC22_NATIVE_PENDING`**，本轮没有进入游戏、读写进程或运行采集。页面位置若没有直接证据均写为“检索路径/待核”，绝不伪造已确认的精确PC操作按键。
>
> 本文中的 `SRC-####` 引用见 [SOURCES](../SOURCES.md)；`VIS-####` 见 [外部图源](../visuals/EXTERNAL_VISUALS.md)。真实截图、菜单身份、保留期最终均须按指定平台取证。

## 0. 证据分级和开箱先读

| 标签 | 准确定义 | R01判定 |
|---|---|---|
| `KNOWN_IN_SERIES` | 同系列已有实物/一手社区资料，可能不同游戏版本、平台、模式 | Schedule/Daily View、历史Box查询、球员投篮图 |
| `PC22_UI_CONFIRMED` | 本项目实际NBA2K22 PC本世代 MyLEAGUE 对应页面已截图及确认 | **本轮未达到** |
| `PC22_NATIVE_READ_VERIFIED` | 对同一目标存档、对象身份、读数验证 | **本轮未达到** |
| `PROJECT_CAPTURED` | 原生数据进入带来源和批次的正式数据库 | 逐场Game/Box/Shot **未由本轮审计证明** |
| `GM_QUERYABLE` | GM可稳定按GameID/球队/球员/日期读取并追溯 | 逐场事实 **未由本轮证明** |
| `UNKNOWN` | UI、字段、定义、历史留存等尚缺证据 | 明确留为未知 |

**最重要的区别**：真实 NBA.com 提供 Play-by-play、Tracking、Shot Dashboard、Advanced Box，**不代表2K22 PC自带这些全部数据**。2K22 PC英文官方手册列的是按钮与临场战术控制，没有逐场统计页面索引、合法字段清单或历史数据保存承诺；因此不能用该手册“证明没有该功能”[SRC-0004]。

## 1. K01.GAME_SCHEDULE / K01.GAME_LOGS — 从赛程找到“这一场发生了什么”

```yaml
mechanism_id: K01.GAME_SCHEDULE
priority: P0
version_scope: NBA2K22_PC_CURRENT_GEN_MYLEAGUE_TARGET
knowledge: KNOWN_IN_SERIES
pc22_ui: UNKNOWN
pc22_native: NOT_OBSERVED
project_capture: DEV28_GAP_OPEN
gm_consumers: [WEB_GM, WEB_ANALYTICS]
sources: [SRC-0005, SRC-0006, SRC-0007, SRC-0008]
```

### 1.1 WHAT：赛程、Game Log、Box Score 是三个层次

- **Schedule/Calendar / Daily View**：一场赛事是否存在，日期、主客场、对手、当前赛季阶段、比赛状态及最终比分。它是 **game identity** 的来源，而不是比赛表现的完整记录。
- **Game Logs**：同一球员/球队按场次展开的时间序列，回答“最近5/10场表现如何”“对哪支球队打得好”“交易/换帅前后怎么变”。**玩家常说的 Game Log 既可能是球员分页，也可能只是从日历逐场打开 Box 的替代操作**；本轮没有在 PC22 证明独立 Game Logs 标签存在。
- **单场 Box Score**：与某个 game 绑定，所有上场和未上场球员的实际计分统计、对应球队合计；不能用“本赛季场均 × 已打场数”反推出每场明细。防止把赛季统计当逐场历史。
- **Play-by-play/逐回合、事件级射点和阵容在场片段**：与上述三者再分开；即使能打开Box，也不代表有这些追踪数据。

### 1.2 HOW：可靠历史导航线索（不能照抄成PC22已证键位）

**路径A：日历/球队赛程 → 选择过去某场 → 进入比赛相关操作 → 查当场Box**。Operation Sports 关于早期MyLEAGUE的玩家经验称，Calendar上的比赛可进入“Daily View”以切换当日其它比赛；2015年原帖中另一位玩家明确表示 MyGM/ MyLEAGUE 权限可能不同 [SRC-0005]。作为2022年NBA2K22重建记录帖中的玩家回帖，另有人针对“查看旧季后赛Box”解释了 **2K20的特定操作**：上一次比赛Box后按 Xbox Y / PS Triangle 依Game1、Game2顺序切换；发言者**特别注明只在2K20验证** [SRC-0006]。这项信息只用于 PC22 定向检查，不是2K22现成操作说明。

**路径B：球员卡/Stats → 按游戏内提供的统计维度切换 → 检查有无逐场Game Log及比赛日期/对手**。这是给未来实机核验的导航尝试，**不是已认证菜单路径**。检查入口选择球员个人页、球队统计页、League Stats及赛程详情，准确记录页签名、按键、筛选器和结果集合。

**路径C：次世代MyNBA → Daily View**。2K21次世代高级制作人Dave Zdyrko的正式开发者介绍确认 Daily View 可查看当日NBA/G League安排，进入比赛或普通模拟、SimCast、SimCast Live [SRC-0007]。此信息是次世代MyNBA，不应把G League、所有操作和UI复制到PC22 MyLEAGUE。

### 1.3 WHERE：PC22实机需要按顺序查的页面及可见选项

| 候选页面 | 实机读数检查（列名与可选项未确认前不写死） | 玩家使用方法/意义 | 证据 |
|---|---|---|---|
| 联赛日历/球队赛程 | 当前/往日、球队、轮次、比赛是否完成、主客、比分、对手、入口按键 | 从“赢/输”钻到单场对手问题 | 系列一手玩家/次世代官方；PC22待核 |
| 当日 Daily View | 可否转到其它队赛事；普通Sim、SimCast与现场观看分支 | 同日30队跟踪、侦察潜在对手 | SRC-0005/0007，模式不同 |
| 完赛 Box Score | 球员列表、主客球队、得分、分钟、合计、节次表、DNP、赛后退出后能否回看 | 追查某场核心球员效率和轮换 | SRC-0006（2K20）、PC22待核 |
| 个人/球队赛季统计 | 是否存在 Game Logs、切换球队/时期/赛季及比赛类型；统计页签和排序 | 不同于 Season Totals 的逐场动态 | 待PC22截图 |

**不能跳过赛程键**：`game_id` 首选真实原生稳定ID，如缺则记录 `save_instance + season + league + phase + date + home_team + away_team + occurrence` 复合候选身份并检测冲突；“日期+球队”不足以区分极端重赛、季后赛、同日异常或跨存档。不允许当前球队归属覆盖旧比赛事实。

### 1.4 常见陷阱：模拟标准化与比分对不上

2022-06-09 的**2K22本世代 MyLEAGUE**玩家报告：在SimCast模拟后跳入比赛，场内结束显示102:110，日历却显示142:150；回复建议检查“normalize simulated minutes/stats”（回帖具体英文选项名不确定），原发言者随后表示关闭分钟标准化后恢复 [SRC-0008]。这是可复核的单例玩家证据，**不是对所有版本和玩法都必然成立的引擎公式**。

实务：在读Box之前先抄 `played_quarter_length`, `simulated_quarter_length`, `normalization_enabled`（分别如实填 `UNKNOWN`）、`sim_mode`（Play/Quick Sim/SimCast/SimCast Live/Jump-in）以及 “Box/日历/赛后” 三处比分；遇矛盾打 `SCORE_CONFLICT` 而不是直接取最新的覆盖旧值。教练对比、交易评价也必须按相同模拟设置分组。

## 2. K02.GAME_BOX_PLAYER / K02.GAME_BOX_TEAM — 单场球员与球队Box

```yaml
mechanism_id: K02.GAME_BOX_PLAYER
priority: P0
research_status: DOCUMENTED_WITH_OPEN_ITEMS
version_scope: NBA2K20_22_SERIES; PC22_UNVERIFIED
sources: [SRC-0006, SRC-0008, SRC-0009]
pc22_native_status: NOT_OBSERVED
dev28_followup: D28-3
```

### 2.1 什么是“最小可分析”的原始Box

逐场球员候选：真实Player ID、当场Team ID、`game_id`, `starter`, `played/DNP`, `minutes`, `PTS`, `FGM/FGA`, `3PM/3PA`, `FTM/FTA`, `OREB/DREB/REB`, `AST`, `STL`, `BLK`, `TOV`, `PF`, `+/-`（如原生有），技术犯规/盖帽被盖/DNP原因仅在来源证实时加入。这里是**采集候选字典**，不是“已在PC22看到每一列”。

球队逐场候选：主/客队ID、每节得分、总PTS、FG/3P/FT出手命中、进攻/防守/总篮板、助攻、抢断、盖帽、失误、犯规、快攻分/禁区分/二次进攻分/替补得分（原生存在则采）、得失分和胜负；对手同级原始Box必须成对保存，不能拿最新赛季场均替代。

**球员出场分钟和赛季合计不可随便反算：**
- 球员`MIN`的分钟/秒单位、精度、标准化状态要保留；DNP可记录`0`上场分钟+明确DNP标志，但不能推断缺行=0分钟；
- 赛季小数分钟和BOX分钟四舍五入可能不精确相加；允许容差并留原始字符串；
- 每一侧的球员分数求和应与队伍总分在相同原生口径内核对；若不一致，记录标准化/加时/模拟及其它异常证据，不替游戏修正。

### 2.2 GM如何真正用单场Box：三组分析

**进攻识别**：先看队伍出手结构 (`3PA/FGA`)、罚球频率 (`FTA/FGA`) 与失误，再看核心球员使用了多少出手与罚球；如果外围投得少，不应只根据最终胜负立刻调整主教练进攻体系。观察同类对手连续若干场，检验是否是战术、球员定位、对手防守还是随机样本。

**防守识别**：以对手 eFG%、对手FTA/FGA、失误和进攻篮板比判断问题出在对手投得准、犯规控制、球权施压或篮板终结；**一个球员单场 +/- 不能单独证明防守好坏**，它包含共同出场球员、对手强度和轮换影响。

**阵容/合同识别**：近5/10/20场的真实分钟、出手和效率变化，先辨认角色变化或教练造成的使用方式差异，再谈交易。用户规定不通过改能力值“修好”低命中率；GM可提出真实人员调整或已有受控教练配置，不得擅改球员能力/潜力/徽章。

### 2.3 核查结果质量

同一比赛要尽量有：`score_calendar`, `score_box`, `score_end_screen`；`sum_player_pts`, `team_box_pts`, `game_final_pts`；主客两队字段完整性；`played/simmed/normalized`；常规赛/季后赛；来源时间和屏幕/源标识。出现全部球员得分大幅膨胀或奇怪重复统计不应进入无标记的趋势分析。

2022年一位2K22线上MyNBA玩家报告部分AI队员赛季得分异常高，且Box与异常赛季累计一致；其使用SimCast Live和36分钟标准化 [SRC-0009]。这是另一种**社区故障报告**，不证明相同故障在PC22离线必现。与单场日历不符案例共同提醒：从结果页面读取的数字也可能已有污染，不意味着采集脚本出错。

## 3. K02.PER_GAME_PER36_ADVANCED — 三种统计不要混淆

```yaml
mechanism_id: K02.ADVANCED_STATS
priority: P0
sources: [SRC-0010, SRC-0011, SRC-0012]
status: SERIES_MENU_UNKNOWN_PC22; STANDARD_FORMULAS_DOCUMENTED
pc22_native_status: NOT_OBSERVED
```

| 分类 | 计算粒度 | 实际解释 | 可否从真实逐场Box可靠得到 |
|---|---|---|---|
| Season Totals / 累计 | 每项统计赛季求和 | 出勤和负荷量 | 是，需逐场完整性 |
| Per Game / 场均 | 累计÷符合口径的GP | 比赛产出，受分钟影响 | 是，需知道GP与DNP规则 |
| Per 36 Minutes | 统计累计÷总实际分钟×36 | 消除部分出场时间差，不等于球员真实打36分钟会等比生产 | 是，MIN>0；不是平均单场`per36`的简单平均 |
| eFG% | `(FGM+0.5×3PM)/FGA` | 三分额外价值，衡量有效投篮效率 | 是，FGA>0 |
| TS% | `PTS/[2×(FGA+0.44×FTA)]` | 结合三分、罚球的真实命中效率**估计** | 是，分母>0，0.44为约定 |
| 3PAr | `3PA/FGA` | 球员/球队的三分投篮选择 | 是 |
| FTr (常见版本) | `FTA/FGA` | 罚球制造频率；“罚球因素”也有FTM/FGA口径 | 是，须显式记录具体定义 |
| TOV% (常见Box模型) | `100×TOV/(FGA+0.44×FTA+TOV)` | 每次结束进攻行动的失误比 | 是，分母>0 |
| Team ORB% | `ORB/(ORB+Opp DRB)` | 争抢可用进攻篮板的份额 | 是，需要对手篮板 |
| Estimated Possessions | `FGA+0.44×FTA−ORB+TOV` | **粗估**回合数；不等于真正逐回合记录 | 可估，不能宣称 exact |
| Estimated Team OffRtg/DefRtg | `100×本队得分/估计回合`、`100×失分/估计对手回合` | 按百回合调整攻防，分母不精确 | 可估；使用固定版本，显示 estimated |
| USG% | 需要个人与全队FGA、FTA、TOV以及个人/球队实际分钟的标准公式 | 球员在场时球队由其投篮/罚球/失误终结的使用比，不是持球时间或触球次数 | 可近似，必须同场分钟与球队相同口径 |
| PER / BPM / VORP / RAPM | 依各自具体模型，需要联盟基准、场上片段或更多资料 | **不是**用基础Box随意拼成的“自定义PER” | 本项目当前不应宣称可计算原版 |
| Real on-court On/Off、lineup NetRtg | 需要球员在场时间段、双方得分/回合、阵容替换 | 识别双人搭配、替补协同和防守影响 | **纯总Box无法精确生成** |

数学定义与估算边界按Basketball-Reference Glossary及Four Factors [SRC-0010/0011]；实际NBA.com官方Advanced页面证明现实联盟有更多筛选和指标（如NetRtg、Pace、PIE、USG%），**不能冒充2K22 PC原生Advanced列表** [SRC-0012]。任何“2K自身Advanced”页签内容、PER算法、是否提供Per36/每百回合等均须从PC22屏幕独立验证。

**正确聚合方式示例**：球员近10场真实`TS%` = `SUM(PTS)/[2×(SUM(FGA)+0.44×SUM(FTA))]`，不是对10个单场TS%做等权平均。按对手/赛程/先发替补拆分也先筛选真实Box，再聚合。

篮球四要素（Four Factors）指导球队质量诊断：eFG%、TOV%、ORB%、罚球率，各自分攻防两个方向，比较己方与对手值[ SRC-0011 ]。权重是篮球经验模型，不得强行写成2K模拟胜率概率公式。

## 4. K02.SHOT_CHART / SHOT_ZONES — 投篮落点、热区和命中率不是一回事

```yaml
mechanism_id: K02.SHOT_CHART
priority: P1
sources: [SRC-0013, SRC-0014]
visuals: [VIS-0001]
known_in_series: YES
pc22_myleague_menu: UNKNOWN
raw_attempt_coordinates: NOT_OBSERVED
```

- **Shot Chart** 可能显示一个时期某场/一段样本的投篮出手分布和结果；若能按区域统计出手数/命中数，就可计算区域命中率及出手频率。
- **Hot Zones / 热区图** 是游戏状态/显示机制，不等于已采集到每次出手的原始坐标，也不意味着同一数值必适用所有模式。NBA2K22 Reddit玩家讨论确实把这两种图分开，有人介绍在Roster/Stats能切换Shot Chart及Hot Zones [SRC-0013]。其讨论围绕 MyCareer、Park、Rec；**这不是NBA2K22 PC离线MyLEAGUE的具体菜单确认**。
- 2K22 **次世代**玩家贴出两种图的截图并询问为何显示不同，回复对热区跨模式适用性有不同说法 [SRC-0014/VIS-0001]。因此跨模式互相继承、热区阈值、刷新范围不能靠单条评论认证，尤其不能将次世代UI直接照搬PC22。
- **Shot Zones Aggregates** (如禁区/近投/中距离/角落三分/弧顶三分) 与 **Shot Coordinates** (每次真实落点x,y、命中/失手) 要拆分：只有分区汇总不能生成像素级热力图；没有投篮尝试细目，不能宣称有事件序列/投篮质量/防守者距离。
- 经营上看的是“出手地图×人员能力与角色×教练战术×防守对策”；仅有命中率且样本量极小，不能据此认定某个球员完全不适合某一区域或要求直接修改他的属性。

### PC22当前需要抓的证据

打开真实 PC22 MyLEAGUE 球员卡、球队统计页、完赛 Box/赛程、实时比赛暂停统计，核对能否在 **单场/全季** 切换Shot Chart、区域表、热区；每个页面记真实显示的区域名、单位、图例、样本时间窗、选项提示和可否回顾旧比赛。如果没有，`UNKNOWN`，不要通过 2K22 MyCareer 或NBA.com图替换。

## 5. 统计与游戏设置的联动：避免GM做出伪因果

| 原因或背景 | 影响哪些数据解释 | 能做什么、不该做什么 |
|---|---|---|
| 实战每节时长 vs Simulated Quarter Length | 出手/得分/上场时间、场均及Per36 | 必须记录，不混合不同规范化批次 [SRC-0008] |
| 标准化 Sim Minutes/Stats | Box与日历/赛季统计可能出现不同口径 | 先定位源与屏幕，不静默缩放到“统一值” [SRC-0008/0009] |
| 使用不同比赛方式（Play/SimCast/Quick Sim） | 比赛统计生成路径可能不一样 | 先标模式，比较前确保分层 |
| 教练 Pace/Run Plays/体系、Rotation | 球队回合数、球权分配、出手区域可能发生变化 | 统计提示需要调查；无引擎因果证据不得说修改X必提高Y |
| 对手风格与防守、体能伤病 | 攻防效率和出场分工 | 结合阶段、主客、强弱队样本解读 |
| 赛季阶段（Regular/Playoffs）、加时 | 分母、出场时间、比赛胜负 | 分阶段与加时标记，不能默认48分钟 |
| 赛季迁移、球员转会 | 历史球员归属及球员持续追踪 | 旧Box永久记录当场team_id，不追溯改写为最新所属队 |

2K22 PS4本世代Operation Sports高参与度模拟调参帖列出了 `Quarter Length`, `Simulated Quarter Length`, Team Pace、Possessions per Game、Shot Types、Shot Percentages、Stat Distribution 等，并明确是在研究“模拟统计是否像真实NBA”；用户给的数值是其自用滑块，不是原生默认或GM必须采用的“最优值” [SRC-0015]。本项目严格禁止自动改球员能力来校准统计，研究不是调参授权。

## 6. 推荐给GM的五步逐场诊断法（可以直接执行的分析逻辑）

**第一步：选正确比较对象**。选最近10场，按对手水平、主客、比赛阶段和模拟配置过滤，标记已知异常；保持同档口径。10场只代表趋势初探，不自动得到统计显著性。

**第二步：先算团队四要素与百回合估算**。先识别得分起伏主要来自回合数（Pace）、投篮质量/效率（eFG/TS proxy）、罚球制造、篮板还是失误，再找球员。

**第三步：看核心与替补**。每场记录分钟、FGA/3PA/FTA、效率、TOV及谁得分；观察高使用率低效率是否有连续性。对角色改变，用换帅/调整前后比赛分段与对手进行相似性对照。

**第四步：只有证据足够才提行动**。问题若是整体出手结构或协防，可提出已有认可范围内的教练/轮换/战术提案；若是某个位置持续缺人，再讨论交易和虚拟市场资金；不能根据一场起伏就调整所有战术，更不能用修改球员能力制造目标效果。

**第五步：下一批验证**。提案仅在玩家批准后交受控执行；后续正常全量采集比较相同指标，并记录对手、伤病、比赛方式变化。表现改善可视为关联，不能直接归因单一教练参数。

## 7. DEV24既有来源缺口与DEV28-3交付要求（本轮不实施）

项目`config/source_catalog.json`与DEV28总规划表明已经有赛季累计/部分静态来源，但没有可以据此声称**可靠全联赛逐场历史**的认证证据。DEV24是未来D28-3动态数据缺口的基础；本轮不重复设计执行器，也**不将尚未审计过的源码当已证实缺失全部字段**。以下为研究确定的**采集需求优先级**：

| 等级 | 实体 / 最小字段与关系 | 质量与身份要求 | 当前状态 |
|---|---|---|---|
| P0 | `game`: game_id/日期/season/phase/home/away/最终比分/状态 | 同存档稳定ID、来源与游戏时间，可能双重比分及冲突标记 | `DEV28_GAP_OPEN` |
| P0 | `player_game_box`: player_id/game_id/team_id/分钟及基础Box、DNP/Starter若存在 | game×player唯一区分、真实当场team、与球队Box核对 | `DEV28_GAP_OPEN` |
| P0 | `team_game_box`: game_id/team_id/基础Box及对手侧 | 两球队成对、统计一致性、来源字段可见性 | `DEV28_GAP_OPEN` |
| P0 | `coverage_quality`: 赛季/赛事总数、已见场次、玩家与AI比赛覆盖、缺行/异常 | 非完整覆盖不得自称“全赛季所有比赛”；异常保留原值 | `DEV28_GAP_OPEN` |
| P1 | `shot_zone_game/season`: 区域+FGA/FGM/适用窗口 | 必须真实原生有区域聚合，不由整场FG假分配 | `UNKNOWN` |
| P1 | `advanced_game/season`: 游戏直接显示字段或公式版本的派生指标 | `observed/derived/estimated`分开，不混用不同指标定义 | `UNKNOWN` |
| P2 | 每次投篮坐标/防守者距离、真正逐回合、lineup-stint与真实On/Off | 只有真实来源才采，不由Box合成 | `UNKNOWN` |

最小身份/来源结构：`save_id,save_instance_id,generation_id,career_id,batch_id,season,phase,game_id,game_date,source_page_or_object,raw_or_derived,formula_version,capture_at,quality_flags`。需分别标 `KNOWN_IN_SERIES`、`PC22_UI_CONFIRMED`、`PC22_NATIVE_READ_VERIFIED`、`PROJECT_CAPTURED`、`GM_QUERYABLE`，不以“有截图/有地址”直接升级到最终等级。

建议严格以真实原生Box为事实，用显式版本计算 `eFG%/TS%/Per36/FourFactors/estimated possessions`；不能把现实NBA Stat官方逐场数据倒灌进游戏虚构赛季。这是游戏世界线独立性要求。

## 8. 本轮验证表、未解决项与下一轮操作入口

| 核对问题 | R01结果 | 下次专用取证动作 |
|---|---|---|
| NBA2K20–23系列可查赛程/旧场Box？ | 有玩家一手线索，但2K22具体操作未证 | 进入PC22现有存档，选1场已经完赛的玩家队比赛与1场AI对AI比赛 |
| PC22是否存在直接Game Logs表页？ | `UNKNOWN` | 球员卡/Stats页签逐一核对；保存完整英文标签 |
| 单场Box具体列及球队合计、首发、DNP？ | `UNKNOWN` | 同一game比对Score/TeamBox/PlayerBox，记录逐字段可见性 |
| League Stats是否提供Per36/Advanced分页？ | `UNKNOWN` | 记录玩家/球队所有统计页签、选择维度及默认值 |
| Shot Chart在PC22 MyLEAGUE是否可按单场查看？ | `UNKNOWN` | 不把MyCareer热区图直接当MyLEAGUE页面 |
| 多少赛季/多长时间还能重新打开旧Box？ | `UNKNOWN` | 在同一存档分别测试当月、跨月、季后赛、下一赛季与重开后；只记录观察，不人为推进正式世界线 |
| Sim standardization对日志/赛程影响？ | 本世代社区有实际异常 [SRC-0008] | 仅独立测试存档比对原始比分与统计，并记模拟参数 |
| 项目现行SQLite能否按player/game取历史事实？ | `NOT_AUDITED_IN_THIS_ROUND` | DEV29最终交Codex进行DEV24/Registry/M0比对，当前不调用DEV28 |

**恢复指针**：本批次 `R01-A` 完成 K01/K02 机制综述、标准派生公式、质量门槛与源/图索引；**R01-B** 优先补“PC22原生统计页/表头原始截图或可审查同代演示”和确切Game Log入口、Shot Chart可选窗口、历史存储期（可能需要玩家截图），然后决定 R01 是否真正 `COMPLETE`；R02研究教练Playbook不应抢在R01残缺核验之前自动启动。

**范围与安全**：只做公开资料研究并保存文字证据。无内存、没有真实游戏写入、没有新采集，没启动DEV28或Codex。玩家批准是任何游戏执行必要条件。
