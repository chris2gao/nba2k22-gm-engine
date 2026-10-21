# DEV29 游戏机制知识库：研究进度与断点恢复

**当前权威状态**：`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`（2026-10-20）。
**下一研究轮：`R02_COACH_PLAYS_DEFENSE_RESEARCH`，立即具备启动条件。** R01-A/B/C/D的公开资料研究全部结束；R01已形成带版本边界、GM数据需求、公式和质量检查的中文攻略，**不是说PC22 UI/内存/逐场采集已经实现**。R01遗留UI未知列入以后单独取证待办，**不再重复R01论坛检索**。研究计划：[DEV29 V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)。

## 当前批次地图

| 轮次 | 工作主题 | 最新状态 | 权威产物 |
|---|---|---|---|
| R01-A | Schedule、Game Log与逐场Box候选、篮球统计派生 | PUBLISHED | [K01/K02](guides/K01_K02_GAME_STATS.md) §§0–8；SRC-0004..15、VIS-0001..03 |
| R01-B | Stats视图切换、Shot Chart、旧季历史与数据异常 | PUBLISHED | 同一指南§§9–13；SRC-0016..25、VIS-0004..06 |
| R01-C | 官方同版次世代Box证据、PS4模拟器参数、PC旧版本质量异常 | PUBLISHED | 同一指南§§14–18；SRC-0026..28、VIS-0007 |
| **R01-D** | **最后一轮PC22原版公开视觉取证；证据矩阵和精简截图需求** | **`RESEARCH_CLOSED_WITH_PC22_UI_GAPS / TASK_CLOSED`** | **同一指南§§19–22；SRC-0029；本轮合格新VIS为0；来源排除审计已写入图证索引** |
| **R02** | **教练、攻防、Playbook、Freelance、ACE、战术12分类、Play Discipline** | **NEXT / NOT_STARTED** | 目标新建`guides/K04_COACH_AND_PLAYS.md` |
| R03 | 球员、训练、疲劳/伤病/成长 | NOT_STARTED | 后续 |
| R04 | 财务、合同、员工、球探、选秀、休赛期 | NOT_STARTED | 后续 |
| R05 | 3D比赛设置、世界线、历史与存档 | NOT_STARTED | 后续 |
| R06 | 跨机制矩阵、GM决策证据、来源查漏 | NOT_STARTED | 后续 |
| FINAL-CODEX | 索引/既有Registry、M0、DEV14、SQLite对照和DEV28技术缺口 | NOT_STARTED | **只在主要网页研究R01–R06结束后** |

## R01-D到底新增/没有新增什么

- **新增确有PC平台指向的文字来源`SRC-0029`**：2K22本世代Operation Sports玩家`res2`确认“PC with default rosters”并贴Setup/Simulation等参数；但他在首帖称自己主要玩`Season Mode`、MyLeague参数多从别的玩家转载再修改，**这不是PC原版MyLEAGUE统计菜单屏幕证据**。此处不提升任何Stats、Box或Game Log字段。
- 本轮面向PC MyLEAGUE、Steam Screenshots、各类公开视频/攻略检索后**未获得同时满足NBA2K22/PC/无UI Mod/MyLEAGUE/可读目标统计菜单的原图/视频帧**：新增`PC22_UI_CONFIRMED = 0/6`、新增合格VIS为0；并不说明六项游戏功能不存在。
- Steam外层`View Stats`属于平台成就入口；网上的`MyCareer Hot Zones`、真实NBA.com Box、2K22 PS5 MyNBA/2K23、`PC Remastered`的自定义菜单**均不能作为PC22原版认证**。
- 审核截图来源与许可，未上传任何第三方图片。资料足够完善“该查什么/怎么判数据质量/GM该如何利用原始Box”，但**不能捏造本机真实数据**。

## R01最终目标证据表

| 目标 | 目标PC22状态 | 已知跨版本事实 | 未来取证队列 |
|---|---|---|---|
| 1. Stats、Player Stats、Team Stats、League Leaders完整页签和筛选 | `UNKNOWN` | `KNOWN_IN_SERIES`：老版MyLEAGUE、PS5 MyNBA其它版统计页 | `DEV28_NATIVE_DISCOVERY_REQUIRED` |
| 2. Player Game Logs独立入口或Calendar→每场Box | `UNKNOWN`；没找到独立标签不表示无逐场数据 | `KNOWN_IN_SERIES`：老版Calendar/Daily View、2K20旧比赛Box | `DEV28_NATIVE_DISCOVERY_REQUIRED` |
| 3. 主客双方Player/Team Box原生表头、合计及DNP/Starter | `UNKNOWN` | `KNOWN_IN_SERIES`：2K22次世代官方Box表格文字 | `DEV28_NATIVE_DISCOVERY_REQUIRED` |
| 4. Per Game、Per36、Advanced本机字段/操作提示 | `UNKNOWN` | `KNOWN_IN_SERIES`：2K16 MyLEAGUE、2K22 PS5、2K23 MyCareer | `DEV28_NATIVE_DISCOVERY_REQUIRED` |
| 5. Shot Chart赛后及历史比赛回看、可选窗口 | `UNKNOWN` | `KNOWN_IN_SERIES`：2K22玩家赛后文本报告，MyCareer热区不可代替 | `DEV28_NATIVE_DISCOVERY_REQUIRED` |
| 6. 跨月/跨季旧Box、赛程、季后赛记录保留期 | `UNKNOWN` | 其它版本保留粒度不同；没有可外推的PC22固定期限 | `DEV28_NATIVE_DISCOVERY_REQUIRED` |

**证据等级无变化**：没有新`PC22_UI_CONFIRMED`、`PC22_NATIVE_READ_VERIFIED`、`PROJECT_CAPTURED`、`GM_QUERYABLE`。只有研究机制`DOCUMENTED_WITH_VERSION_LIMITS`。PS4玩家提供的模拟器设置为当前世代间接证据，**不是Stats菜单的`CURRENT_GEN_ANALOGUE`截图**。

## 最小外部补证（非R01继续网上研究）

若玩家日后自然有机会查看正在使用的原版PC22 MyLEAGUE，分两组、总计**优先约4张**：①Stats首页/按钮与Player Stats切页各1张（解决1/2/4）；②已完成比赛Calendar入口及同场Box表头各1张（解决2/3）。其它列未显示时仅增加一张横向/另一队切页图。Shot Chart、旧赛季Box可在**已有真实历史页面**按需要补1–2张，不能为取证擅自模拟/推进正式存档。详见[VIS待办与许可](visuals/EXTERNAL_VISUALS.md)，以及[K01/K02第20–21节](guides/K01_K02_GAME_STATS.md)。

**后续责任**：DEV28/Antigravity只获得明确的`PC22_ORIGINAL_STATS_UI`和`NATIVE_READABILITY`积压清单，之后是否授权由玩家另行决定；这份研究结案**不启动DEV28**、不开始Codex、游戏进程、数据采集、存档修改或普通球员属性变动。取得新截图时仅局部升级目标列与VIS/SRC，不重新开启R01全面网络检索。

## R02直接启动入口（下次窗口照此执行）

1. 读取本`PROGRESS.md`与[DEV29 V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)、知识库README、Mechanism Card模板；**不要再重复K01/K02研究**。
2. 阅读项目已有`web_gm/manuals/GM_COACHING_OPERATIONS.md`、`docs/40_COACHING_EXECUTION_RUNBOOK.md`、`docs/development_research/NBA2K22_PLAYBOOK_12_CATEGORY_AND_NATIVE_TYPE_MAPPING_V1.md`及DEV28规划的相关教练/战术段；避免把现有已做的19 Coach defaults/18 opponent defense/PlayTypes重新定义成虚构待建系统，精确已实现/已在目标游戏验证另分层。
3. 主动搜索**2K20–23、NBA2K22 PS4/PC MyLEAGUE/PS5 MyNBA**的玩家操作截图、社区战术帖、教练游戏计划、POE、ACE、Playbook、Freelance、12种战术分类/球员4个PlayTypes、战术纪律与防守调整，标清版本/合法枚举/联动/GM决策证据/已知BUG；不要把截图和真实内存混用。
4. 直接写实际**中文经营与战术攻略**到`docs/game_mechanics/guides/K04_COACH_AND_PLAYS.md`（可拆R02-A/B），同步SOURCES、VIS、PROGRESS及README，提交GitHub回读。**不要先产出仅规划的任务清单。**

> 终态：`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS / DEV29_R01_D_TASK_CLOSED / NEXT_R02`。
