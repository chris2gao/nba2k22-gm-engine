# 游戏机制资料库：研究进度与断点恢复

**当前状态**：`R01_B_RESEARCH_PUBLISHED_WITH_OPEN_ITEMS`，更新 2026-10-20。当前研究目标仍为 NBA2K22 PC 本世代 MyLEAGUE；**R01未达到完整PC22 UI与原生数据验证，不得标`COMPLETE`**。此前R01-A研究已保留在同一指南内。权威计划：[DEV29 V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)。

| 轮次 | 内容 | 已提交状态 | 成果 / 下一步 |
|---|---|---|---|
| R01-A | 赛程/Game Logs、逐场Box、Advanced/Shot Chart、公式/数据需求 | PUBLISHED_WITH_OPEN_ITEMS | [K01/K02指南 §§0–8](guides/K01_K02_GAME_STATS.md) |
| **R01-B** | 统计菜单操作证据、旧赛季留存、赛后Shot与错误口径、图证分层 | **RESEARCH_PUBLISHED_WITH_OPEN_ITEMS** | [K01/K02指南 §§9–13](guides/K01_K02_GAME_STATS.md)、[SRC-0016..25](SOURCES.md)、[VIS-0004..06](visuals/EXTERNAL_VISUALS.md) |
| **R01-C** | **PC22 原生统计菜单/完整字段/跨季历史证据** | NOT_STARTED / NEXT_IF_PLAYER_TRIGGERS | 优先寻找真实无模组PC22视频/截图；对现存UI做纯只读现场认证必须由玩家另行安排 |
| R02 | Coach/Playbook/战术与联动 | NOT_STARTED | 在完成/明确保留R01的未知后另轮启动 |
| R03 | 球员、训练、疲劳/伤病/成长 | NOT_STARTED | 后续 |
| R04 | 财务/合同、员工、球探、选秀、休赛期 | NOT_STARTED | 后续 |
| R05 | 实时3D、世界线、历史、存档自动化 | NOT_STARTED | 后续 |
| R06 | 全域查漏、跨机制关系、GM需求目录 | NOT_STARTED | 后续 |
| FINAL-CODEX | 文档源矩阵/Registry/M0/DEV14/DEV28工程交接 | NOT_STARTED | 网页R01–R06研究后才能启动 |

## R01-B已核实的可用知识与版本范围

1. **2K16 MyLEAGUE**：OS一手问答证实在player stats按Triangle/Y轮换普通、Per-36、Advanced [SRC-0018]；不能直接当作PC22键位。
2. **2K22 PS5 MyNBA**：玩家报告Player Stats→Triangle切至Per-36；按PAPG和plus/minus排序不准 [SRC-0017]。这是**确切2K22但非目标平台**的直接事实/错误报告。
3. **2K23 MyCareer**：统计分类页有Totals/Per-Game/Per-36/Advanced，入口为MyCareer→Stats→League Leaders [SRC-0019]；模式不相同。
4. **2K22赛后Shot Chart**：Operation Sports一手玩家明确将赛后的投篮图同PIP摘要对照，报告部分禁区外投篮错算为禁区得分 [SRC-0016]。只是文字报告，没有PC22像素/落点内存认证。
5. **历史视图保留并不统一**：2020 MyLEAGUE的旧季Bracket不可回看，但旧Standings能看 [SRC-0021]；2025 MyEras有关更久历史记录的用户说法有分歧 [SRC-0022]。均**不能推成PC22旧Box保留几赛季**。
6. **其它模式也有数据污染风险**：2K22/23在线MyNBA玩家报告完赛未记录 [SRC-0024]；仅属于异平台/线上BUG警示，不等于PC离线必现。
7. **热区与投篮图不可混淆**：Gamepur为2K22 MyCareer/MyTeam给了hot-zone导航 [SRC-0020]，不是MyLEAGUE Shot Chart验证；PC版Remastered自订UI [SRC-0025]不得用于原生截图认证。

## 当前还不能填写成PC22事实的P0/高优先级问题

| 待证 | 当前状态 | R01-C应获取的最少证据 |
|---|---|---|
| PC22 MyLEAGUE 球员/球队Stats准确页面与全部视图 | `PC22_UI_PENDING` | 无mod当前存档页面及底部按钮提示/字段全表 |
| PC22是否有独立Game Logs表/逐场条目 | `UNKNOWN` | player card、league stats全部页签与日历对应检索 |
| 已打比赛（玩家队和AI队）完整Box Score列 | `UNKNOWN` | 同一个game的主队/客队player/team Box及日期/比赛阶段 |
| 赛后Shot Chart、投篮热区、是否能按场/赛季 | `KNOWN_IN_SERIES / PC22_UNKNOWN` | 原生赛后UI + 历史Box页面、图例与筛选选择器 |
| 跨月/跨季/季后赛完整历史Box与旧Bracket | `UNKNOWN` | 不推进正式存档，只在已存在历史的只读页面比对 |
| PC22高级统计算法、排序可靠性 | `UNKNOWN` | 真实Advanced表头、原始列、同页排序对照 |
| 逐场游戏内存、存储位置及正式SQLite可查询 | `PC22_NATIVE_PENDING` / `DEV28_GAP_OPEN` | 研究完成后，由独立授权的后续技术任务处理 |

## 本轮GitHub成果与证据等级

- 研究更新目标：`guides/K01_K02_GAME_STATS.md`的 **§§9–13**、`SOURCES.md` 新增`SRC-0016..0025`、`visuals/EXTERNAL_VISUALS.md`新增`VIS-0004..0006`、本`PROGRESS.md`和总`README.md`。
- `DOCUMENTED`：统计页按键的**其它版本**、赛后投篮图社区用法、历史可见性与错误口径风险。
- `KNOWN_IN_SERIES`：`YES`。
- `PC22_UI_CONFIRMED`、`PC22_NATIVE_READ_VERIFIED`、`PROJECT_CAPTURED`、`GM_QUERYABLE`：**本轮均未获得新增认证**。
- 图像：只写外部定位和许可边界，**未将未授权第三方媒体文件上传仓库**。
- 执行：无Codex、无DEV28、无游戏启动/模拟/读写、无生产采集、无球员能力修改。

## 下轮研究窗口恢复指令

1. 先读本页，再读[K01/K02](guides/K01_K02_GAME_STATS.md)的**§§9–13**和[SOURCES](SOURCES.md)的`SRC-0016..0025`，不要重新搜已有引用当作新证据。
2. 在公开资料中优先查**无mod NBA2K22 PC本世代MyLEAGUE**的完整菜单/表头/切页操作录屏；必要时同代PS4作为`KNOWN_IN_SERIES`候选。
3. 依[VIS-TODO-PC22-01..06](visuals/EXTERNAL_VISUALS.md)有界补足：Game Log是否独立、当前场Player/Team Box所有列、Per36/Advanced、Shot Chart筛选、旧比赛回溯期和标准化字段；没有证据绝不将`UNKNOWN`转换为`VERIFIED`。
4. 实际无法靠公开资料获取原生PC22截图时：报告准确缺口、结束研究窗口；玩家自行决定是否提供只读页面截图。**不要直接启动正式存档或DEV28，不能等待Codex活动会话。**
5. 每轮更新同一指南/来源/图源和本进度，再回读GitHub校验；当前的R01-C是具体调查入口而非新开发任务。

**最终工程衔接**：DEV24与未来DEV28 D28-3要得到的`game/schedule/player_game_box/team_game_box`和当场shot zones / advanced按源证据分级，不能依赖只有赛季平均的既有来源伪造逐场表现；研究R01只建立知识与真实需求，不获得采集与游戏写入授权。
