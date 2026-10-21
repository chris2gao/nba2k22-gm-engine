# 游戏机制资料库 — 进度与断点恢复（DEV29 V2）

**最新状态**：`R01_C_RESEARCH_PUBLISHED_WITH_OPEN_ITEMS`；更新2026-10-20。**研究任务R01-C已结束并正式发布；整个R01仍为`INCOMPLETE_WITH_OPEN_ITEMS`**。目标版本NBA2K22 PC原版 MyLEAGUE；来源的年份、平台、模式要与原生认证分开。正式开发项目`DEV28`尚未开始。本轮无游戏进程、存档、模拟或数据修改。

权威总计划：[DEV29 V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)；[中文正式机制攻略K01/K02](guides/K01_K02_GAME_STATS.md)、[来源](SOURCES.md)、[图证与版权](visuals/EXTERNAL_VISUALS.md)。

| 轮次 | 主题 | 状态 | 发布成果与下一步 |
|---|---|---|---|
| R01-A | 赛程、Game Logs、每场Box与普通/高级统计、投篮图 | PUBLISHED_WITH_OPEN_ITEMS | K01/K02 §§0–8；SRC-0004..15、VIS-0001..03 |
| R01-B | 统计视图切换、赛后Shot与旧季记录风险 | PUBLISHED_WITH_OPEN_ITEMS | K01/K02 §§9–13；SRC-0016..25、VIS-0004..06 |
| **R01-C** | **PC22原生统计UI公开证据搜索、同年版本/模式交叉核查、数据层级** | **RESEARCH_PUBLISHED_WITH_OPEN_ITEMS / TASK_CLOSED** | **K01/K02 §§14–18；SRC-0026..28；VIS-0007** |
| **R01-D** | 一次有界的目标PC22原版UI/历史数据视觉认证，或维持UNKNOWN后封存R01 | NOT_STARTED / NEXT_IF_PLAYER_TRIGGERS | 优先已有原版PC22 MyLEAGUE画面；没有则保留证据请求，不无限搜索 |
| R02 | Coach、Playbook、战术类别与联动 | NOT_STARTED | 独立研究轮 |
| R03 | 球员、训练、疲劳、伤病与发展 | NOT_STARTED | 独立研究轮 |
| R04 | 财务、合同、员工、球探/选秀/休赛期 | NOT_STARTED | 独立研究轮 |
| R05 | 实时3D、世界线、历史和自动化 | NOT_STARTED | 独立研究轮 |
| R06 | 全域查漏、经营决策证据矩阵 | NOT_STARTED | 独立研究轮 |
| FINAL-CODEX | 核对Registry/M0/DEV14及缺口、工程整理 | NOT_STARTED | **R01–R06研究主体完成之后** |

## R01-C实际增加的三项新来源（截至2026-10-20）

1. **SRC-0026 / 2K22开发团队介绍的次世代MyNBA**：明确提到`roster`、`coach gameplan`、`box score`表格的紧凑布局（更多同屏行）；**限定PS5/Xbox Series，不证明PC22相同**。VIS-0007是相邻Roster配图，不冒充Box截图。
2. **SRC-0027 / 2022年OS同期玩家建议**：明确区分`Current Gen MyLeague`与`NextGen MyNBA`；另有玩家希望强化季后赛统计和旧纪录在球员卡上的显示。**愿望不等于已证功能不存在**。
3. **SRC-0028 / 2K17 PC MyLEAGUE老版BUG**：特殊投篮犯规规则下，场内球员34分、完赛Box/赛季仅27分；仅说明同系列早期有阶段值重算风险，**不能声称PC22有同BUG**。

**现存SRC-0015再核对**：2K22 PS4本世代一手玩家列出`Quarter Length`、`Simulated Quarter Length`及`Simulation`下各统计生成设置组；数值是该玩家自设，不是PC22默认或实际百回合数。攻略K01/K02 §15已明确把设置快照和真正比赛统计分离。

## 当前目标PC22原生的证据状态（不能越级）

| 目标 | 最严格有效状态 |
|---|---|
| Stats与League Leaders的准确原版PC22菜单名、按键、页签与全部表头 | `PC22_UI_PENDING` |
| 个人独立Game Logs是否存在 / 玩家对手日期逐场条目 | `UNKNOWN` |
| 当场两队完整Box、首发/DNP/个人分钟与团队汇总全字段 | `UNKNOWN` |
| Per36、Advanced具体字段/准确公式、排序可靠性（PC本世代） | `PC22_UI_PENDING` |
| Shot Chart单场/赛季范围和历史Box重开、原始坐标 | `KNOWN_IN_SERIES`、`PC22_NATIVE_PENDING` |
| 跨月、季后赛、跨赛季逐场Box与Bracket的保存窗口 | `UNKNOWN` |
| 已纳入正式SQLite并且GM可查询的逐场数据 | `NOT_VERIFIED_IN_DEV29`；未来DEV28 D28-3的P0来源缺口 |
| R01攻略的系列知识 | `DOCUMENTED_WITH_VERSION_CAVEATS`；**≠PC22原生认证** |

## R01-D下一次研究窗口如何直接开始

1. 读取本页与[K01/K02 §§14–18](guides/K01_K02_GAME_STATS.md)、[SRC-0026..28](SOURCES.md)、[VIS-0007](visuals/EXTERNAL_VISUALS.md)，勿重复将PS5官方Box界面认定为PC22。
2. 最优先**目标游戏可审查的原版PC22 UI**（不是Remastered、MyCareer或NBA.com）：`VIS-TODO-PC22-03`球员/球队Stats全页签；`VIS-TODO-PC22-02`同场双方Box全部列；`VIS-TODO-PC22-01`赛程Game Log入口；`VIS-TODO-PC22-05`Post-game Shot Chart及是否可从旧比赛重开；`VIS-TODO-PC22-04`Per36/Advanced；`VIS-TODO-PC22-06`节长和标准化。
3. 最困难的是跨季：只有真实已有历史存档才能判断`old_season_game_box`是否保留；不要为了研究擅自推进/模拟任何正式世界线。若可获得经过许可的玩家只读截屏，明确截图适用版本、日期、设置与存档身份；没有则依然`UNKNOWN`。
4. 如果没有新可靠PC22截图，在**一次有界检索后**报告`PC22_TARGET_EVIDENCE_UNAVAILABLE`并封存具体未知项，避免为找不到菜单阻挡R02–R06；用户可按需求以后再让技术人员专项检查。下一轮不自动启动DEV28或Codex。
5. 新轮继续更新GitHub四件套（指南、SOURCES、visuals、PROGRESS）及README，回读确认SHA。任何`PC22_UI_CONFIRMED`必须由真实原版画面及对应证据ID支持。

## 本轮研究/工程边界

实际交付本轮5个GitHub文档：攻略增补、来源索引、外部图源、PROGRESS、README。**未访问/修改游戏存档和球员数值、未运行游戏内存扫描、未启动DEV28、未启动Codex、未执行生产全量采集。** 只有玩家可单独批准未来游戏操作。历史线、普通球员能力修改禁止规则不变。

> `DEV29_R01_C_PUBLISHED_WITH_OPEN_ITEMS_TASK_CLOSED`。继续研发时先用GitHub最新`PROGRESS.md`恢复，而非根据聊天记忆重开R01-A。
