# 游戏机制资料库：研究进度与断点恢复

状态：`R01_A_PUBLISHED_INCOMPLETE_WITH_OPEN_ITEMS`；更新时间 **2026-10-20**。主研究版本 NBA2K22 PC本世代 MyLEAGUE。权威计划：[DEV29 V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)。下一轮从此恢复，**不要把文献完成混为真实游戏数据来源认证**。

| 轮次 | 游戏主题 | 状态 | 核心文档 | 下一步 |
|---|---|---|---|---|
| **R01-A** | 赛程/Game Logs/每场Box/Per Game/Per36/Advanced/Shot Charts | **PUBLISHED; INCOMPLETE_WITH_OPEN_ITEMS** | [K01/K02 第一批中文实用指南](guides/K01_K02_GAME_STATS.md) | 下一轮优先R01-B补确切PC22菜单表头/留存和截图 |
| R01-B | PC22统计菜单与保存范围证据补缺、R01校对 | NOT_STARTED | 继续上面同一指南 | 收集真实PC22截图/真实同代引文，留未知而非编造；完成才考虑R01 COMPLETE |
| R02 | 教练/Playbook/战术类别/纪律与攻防 | NOT_STARTED | `guides/K04_COACH_AND_PLAYS.md` | R01-B结束后由玩家触发 |
| R03 | 球员、训练、疲劳、伤病、成长 | NOT_STARTED | `guides/K03_K06_PLAYER_TRAINING.md` | 后续 |
| R04 | 合同、财务、员工、球探/选秀、休赛期 | NOT_STARTED | `guides/K07_K09_FRANCHISE_OPERATIONS.md` | 后续 |
| R05 | 实时3D设置、历史纪元、联赛规则、游戏自动化 | NOT_STARTED | `guides/K05_K10_K11_WORLD_SETTINGS.md` | 后续 |
| R06 | 全域查漏、跨机制关系、决策证据及索引合并 | NOT_STARTED | `catalogs/`候选机读清单 | 后续 |
| FINAL-CODEX | 源/图/能力矩阵工程收尾 | NOT_STARTED | 待生成工程回执 | **网页研究主体R01–R06完成后才允许** |

## 本轮 R01-A 已交付的实际机制研究

- 逐场Schedule / Daily View / Game Logs / 单场Player Box / Team Box的概念、前往查找的系列导航线索及**不能自动推断PC22正确按键**的版本边界。
- GM使用单场Box与近5/10/20场数据诊断投篮、失误、篮板、罚球、防守问题的解释性流程，不凭1场比赛直接认定交易必需。
- 明确Per Game、Per36、eFG%、TS%、TOV%、Team ORB%、估算回合/OffRtg/DefRtg，区分实际Box可派生、需要对手/分钟背景以及**需要比赛片段/坐标追踪才有可能**的指标。
- Shot Chart与Hot Zone、区域聚合与出手坐标的层级划分，并区分MyCareer/本世代/次世代与目标MyLEAGUE。
- 2022年2K22本世代社区`Normalize Sim Minutes`导致赛程得分与场内比分不同的案例；2K22线上赛季统计污染报告作为质量风险，必须记录`sim_mode`、`quarter_length`、`normalized`和异常。
- 更新[来源表](SOURCES.md)新增`SRC-0004..0015`、[外部截图索引](visuals/EXTERNAL_VISUALS.md)新增`VIS-0001..0003`，无第三方图片二进制发布。
- 根据DEV24/DEV28 D28-3给出逐场game、player_game_box、team_game_box、shot_zones的P0/P1/P2来源候选与项目证据状态；**本轮不采原生游戏数据、不启动DEV28**。

### R01-A 研究验收判定

| 项目 | 状态 |
|---|---|
| 机制攻略和使用说明 | `DOCUMENTED`（首批，且附版本限制） |
| 公式方法来源 | `VERIFIED_EXTERNAL_METHODOLOGY`（非游戏原生） |
| 跨版本导航/个人图像行为 | `KNOWN_IN_SERIES` |
| NBA2K22 PC目标UI页面/准确字段 | `PC22_UI_PENDING` |
| 逐场原生读取、历史留存期 | `PC22_NATIVE_PENDING` |
| 已发布GAME/BOX SQLite实时数据 | `NOT_VERIFIED_IN_THIS_ROUND`，对应DEV28缺口 |
| R01轮次整体 | **`INCOMPLETE_WITH_OPEN_ITEMS`**，不可标 COMPLETE |
| 游戏进程/存档/GM数据 | **未读取、未写入、未发布** |

## 下轮恢复指针：R01-B（具体而非重新做规划）

1. 读取最新 [PROGRESS](PROGRESS.md) 与 [第一批机制攻略](guides/K01_K02_GAME_STATS.md) 以及SRC-0004..0015与VIS-0001..0003，避免重复写相同一手案例。
2. 搜索**具备显示菜单表头/点击步骤的**2K22 PC或PS4本世代MyLEAGUE统计图文/视频，按页/时间定位；对目前已登记的Reddit图源尝试核对图片像素（不得将未看的图片宣称核实）。
3. 如果只有同代但非PC版本证据，保留`KNOWN_IN_SERIES`；玩家后续若允许，可用 **独立只读截图** 核对`VIS-TODO-PC22-01..06`，不为本任务直接推进正式比赛/模拟赛季。
4. 特别查：Game Logs是否存在独立页、完赛和跨月/跨季Box保存时长、球员/球队每场确切列名、统计时间窗过滤选项、Advanced/Per36本机是否存在、投篮图能否逐场查看。
5. 更新同一指南、SOURCES、visuals索引与本文件；如证据仍缺，明确`R01_B_INCOMPLETE_WITH_OPEN_ITEMS`后TASK_CLOSED，**不要安排Codex或DEV28**。R02须另轮由玩家触发。

**项目特定开发关联**：DEV24已指出只保留赛季/累计与片段数据难以满足GM真实决策，DEV28 D28-3是日后受单独授权的源注册/全量同批采集/SQL只读投影工作；DEV29只负责先建立游戏实际功能和决策需求知识。禁止重新编造数据源或把官方NBA.com实时数据库当成游戏存档。
