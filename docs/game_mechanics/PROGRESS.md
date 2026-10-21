# DEV29 游戏机制知识库：研究进度与断点恢复

**当前权威状态**：`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`（2026-10-20）。
**当前轮：`R02_B_RESEARCH_PUBLISHED_WITH_NATIVE_UI_GAPS`；下一轮：`R02_C_BOUNDED_ORIGINAL_UI_OR_CLOSE`。** R01-A/B/C/D的公开资料研究全部结束；R01已形成带版本边界、GM数据需求、公式和质量检查的中文攻略，**不是说PC22 UI/内存/逐场采集已经实现**。R01遗留UI未知列入以后单独取证待办，**不再重复R01论坛检索**。研究计划：**[DEV29 V3 多智能体世界研究路线](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V3.md)**（原[V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)网页GPT多轮交付方法继续有效）。

## 当前批次地图

| 轮次 | 工作主题 | 最新状态 | 权威产物 |
|---|---|---|---|
| R01-A | Schedule、Game Log与逐场Box候选、篮球统计派生 | PUBLISHED | [K01/K02](guides/K01_K02_GAME_STATS.md) §§0–8；SRC-0004..15、VIS-0001..03 |
| R01-B | Stats视图切换、Shot Chart、旧季历史与数据异常 | PUBLISHED | 同一指南§§9–13；SRC-0016..25、VIS-0004..06 |
| R01-C | 官方同版次世代Box证据、PS4模拟器参数、PC旧版本质量异常 | PUBLISHED | 同一指南§§14–18；SRC-0026..28、VIS-0007 |
| **R01-D** | **最后一轮PC22原版公开视觉取证；证据矩阵和精简截图需求** | **`RESEARCH_CLOSED_WITH_PC22_UI_GAPS / TASK_CLOSED`** | **同一指南§§19–22；SRC-0029；本轮合格新VIS为0；来源排除审计已写入图证索引** |
| **R02-A** | **教练、攻防、Book/PlayTypes/Freelance/ACE基本语义、原生已有接口与权限** | **PUBLISHED_WITH_OPEN_ITEMS** | [K04第一批中文攻略](guides/K04_COACH_AND_PLAYS.md)；SRC-0030..39、VIS-0008 | 
| **R02-B** | **ACE自动覆盖与Series/Freelance、Center双挡拆字段与TagOnRoll旧版可见性、CPU-vs-CPU差异、多角色权利** | **PUBLISHED_WITH_OPEN_ITEMS / TASK_CLOSED** | [K04 §§11–17](guides/K04_COACH_AND_PLAYS.md)，SRC-0040..47；新合格PC菜单图证0 |
| **R02-C** | **一次有界原版PC22教练/ACE/Book/个人防守菜单取证，或封存UNKNOWN后转R03** | **NEXT / NOT_STARTED** | 参考VIS索引末节，优先2组4–6张关键截图（若有） |
| R03 | K06 团队与个人训练机制、疲劳、伤病、恢复与自然成长 | NOT_STARTED | 后续；研究共性训练和健康机制，不替代R04全人物字段 |
| **R04 新增重点** | **K03/K12 完整球员个人资料、全部属性/徽章/倾向、耐久及Play for Win/Financial Security/Loyalty；未来Player Agent自主决策接口** | **NOT_STARTED** | [R04独立研究任务书](../development_tasks/DEV29_R04_PLAYER_FULL_PROFILE_AND_AGENCY_RESEARCH_SPEC_V1.md)，后续分R04-A/B/C/D |
| R05（原R04） | 合同、财务、员工、球探、选秀、休赛期、巨星谈判 | NOT_STARTED | 后续；承接R04的球员职业诉求 |
| R06（原R05） | 3D比赛设置、世界线、历史、媒体与存档 | NOT_STARTED | 后续 |
| R07（原R06） | 多角色知识矩阵、GM/球员/教练/媒体决策证据及可执行能力查漏 | NOT_STARTED | 后续 |
| FINAL-CODEX | 源/图索引、已有Registry/M0/DEV14/SQLite与DEV28能力差距收尾 | NOT_STARTED | **只在主要网页研究R01–R07结束后** |

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

## 2026-10-20 新增多智能体游戏目标（不改变当前NEXT_R02）

玩家正式提出：项目的最终价值是**自主GM、教练、球员、媒体等角色在真实NBA2K22游戏状态中进行选择、谈判、试错并产生涌现**，而非唯一GM优化器。为此DEV29新增完整球员研究R04，保留R03训练一般机制，原R04/R05/R06顺延为R05/R06/R07。**R02仍为下一轮，R01已结束，无需重新做统计文献搜索**。研究所有信息不仅问“GM能看到和修改什么”，还应问“Player/Coach/Media能够看到、提出、拒绝什么，原生字段是否可安全映射外挂人格、哪些应优先独立SQLite保存”。完整规划见[DEV29 V3](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V3.md)。这只是规划更新，R04尚未开始、未修改游戏或角色数据库。

## R02-A（2026-10-20）：本轮实际研究交付与断点

**状态：R02_A_PUBLISHED_WITH_OPEN_ITEMS / TASK_CLOSED；R02领域整体未COMPLETE。** R01已经关闭并保留PC22 UI证据缺口，不重新研究。

**可直接用于GM的中文机制卡**：[K04_COACH_AND_PLAYS](guides/K04_COACH_AND_PLAYS.md) §§0–10，明确分清：
- 19项Coach defaults（六POE、8个教练体系、BenchDepth/RunPlay/Zone/BenchUtilization/Tempo/HelpDefense/四Freelance和BookID）的原生含义、GM可用/只读限制；
- 球队同名**战术书容器**68槽Regular30/Bench20/Endgame10/Favorite8与**共享1,392 CRC池**，书归属不是战术条目独占；CRC真实战术类别映射仍UNKNOWN；
- 玩家报告12类目录类别和球员4个有序PlayTypes的**不同枚举**，四Freelance也独立于这些对象；
- 官方2K22防守改进 [SRC-0030] 与2K22同年玩家触球/纪律/自动Playcalling及防守BUG的冲突报道 [SRC-0031..34]；不把建议Touches=50/Discipline=100当游戏规律；
- ACE动态层 vs 静态Coach/Playbook设置 vs 3D实际调用的分层；2018–20旧版意见仅KNOWN_IN_SERIES；
- **日常GM只能提案逐人PERSONAL_DEFENSE，整体OVERALL_DEFENSE只读**，不修改能力/潜力/徽章。换帅后Book重绑与slot更新必须按本队政策和玩家逐笔批准。
- 以场次/阵容/类型与真实对手Box为起点，提出HOLD或有依据的POE、战术书、个体防守候选；不得因缺少真实逐场数据直接编胜率效果。

**源与图**：[SOURCES](SOURCES.md)新增**SRC-0030..0039**（10项），含2K官方、同年OS论坛与编辑评测、Xbox One本世代文字菜单、PS5 MyNBA球队增补Playbook报告、较早ACE分歧、同年控制指南；[VIS清单](visuals/EXTERNAL_VISUALS.md)新增**VIS-0008**（2021年2K22帮助防守图文上下文，**不是PC原生UI认证**）及**VIS-TODO-R02-01..05**，没有第三方图片上传。

**本轮严格保留UNKNOWN**：PC22本机Coach/ACE/Offensive/Defensive所有菜单和动态覆盖；特殊OnBall5/Hedge5/TagOnRoll、2D预览到原生CRC/类别对应；四Freelance实际自动切换/真实频率；整套执行器能力以当前DEV14部署/同批来源而非K04假定。

### 下轮R02-B启动方法

1. 先从GitHub读**本PROGRESS**和[K04 §§0–10](guides/K04_COACH_AND_PLAYS.md)、[SRC-0030..39](SOURCES.md)、[VIS-TODO-R02](visuals/EXTERNAL_VISUALS.md)，不要重新整理已有19/18项原生schema。
2. 优先公开**NBA2K22 PC本世代无模组MyLEAGUE**的Coach Gameplan、ACE/Offensive Settings、Personal Defense、Freelance和2D战术板界面；如只有Xbox One/PS4同代素材，等级为CURRENT_GEN_ANALOGUE。
3. 针对ACE和Freelance、Play Discipline/Run Plays与个人防守的冲突寻找同年实测及不同意见；游戏效果未知不承诺胜率公式，旧版本不升级为PC22事实。
4. 补K04具体截图与菜单、来源和图索引，形成下一批可直接读的攻略并提交GitHub回读。若所需原生数据取不到，保留DEV28/Antigravity未来待认证项而不启动它们。
5. **权威研究路线已更新为DEV29 V3的R01–R07**：R03训练，R04人物完整资料/Player Agency，R05经营，R06世界，R07总矩阵；不要从V2旧表误标后续轮次。FINAL-CODEX须所有R01–R07后。

**执行边界**：纯文献与GitHub知识文档。没有运行Codex、DEV28、游戏进程/采集/模拟或存档/玩家能力修改。R02仍有未完成项，**不能标全部完成**。

## R02-B（2026-10-21）：研究成果、反证与研究下一轮指针

**R02-B已实际完成并发布**；R02总体仍`INCOMPLETE_WITH_PC22_UI_GAPS`，不能声称原版PC22教练与战术动态覆盖已完全认证。R01继续保持`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`，没有再次搜统计旧菜单。

- [K04 §§11–17](guides/K04_COACH_AND_PLAYS.md)新增：**2022年ACE关掉仍重置Defensive Custom**与**ACE Off可保留人工手动调度**的对立玩家报告；将静态原生Coach值、赛前Gameplan、暂停后动态覆写、3D执行分成四层。`SRC-0040/0041`
- 2K22早期Xbox玩家说设置Series后仍回Freelance；同年**Xbox Series MyTEAM**需场上Run Freelance两步激活，是跨模式的诊断线索，不意味着PC离线MyLEAGUE有相同按钮或自动CPU执行。`SRC-0042/0043`
- 2K16的On-Ball Screen/Hedge(Center)讨论把**持球者B、掩护者S、双方防守者DB/DS**分别标识；2K19提到Tag On Roll在赛前菜单不可见但SimCast页仍见。旧版场景帮助理解字段，但**PC22精确触发、UI和值域/可执行性均UNKNOWN**。`SRC-0044/0045`
- 2K22 PC Forum作者明确公开“控制所有队、逐场看3D CPU-vs-CPU MyLEAGUE，不用Fast Sim”的研究方式；不能用人控MyTEAM调ACE的经验等同这种比赛。`SRC-0046`
- 2K21次世代玩家将Freelance/Series/Timeout与Gameplan定义为多个入口，不能套用于本世代。V3新增教练/GM/球员/媒体的观察、提议、否决、长期学习信号与外部SQLite语义区分。`SRC-0047`
- [SOURCES](SOURCES.md)新增**SRC-0040..0047**；[VIS](visuals/EXTERNAL_VISUALS.md)新增**R02-B视觉负面核验和R02-C的2组最小原版截图需求**，**未新增合格VIS编号或PC22_UI_CONFIRMED画面**。所有外部图片留网页原始链接，未上传媒体文件。

**本轮最重要的未知**：PC22完整Coach/Offense/Defense/ACE界面、ACE真正覆盖保存规则、Freelance四槽调用概率/2D形态、Series在CPU对CPU被选择的方式、十二类Play CRC→真实category id以及个人防守OnBall5/Hedge5/TagOnRoll/StayAttached/PreRotate原版UI与执行条件。项目已记录的19教练原生、18对手防守、34 Freelance raw和68 Book槽**保持已有等级**，不得因为文学调研重写原生字典或批准执行。

### 下轮入口：R02-C_BOUNDED_ORIGINAL_UI_OR_CLOSE

1. 从GitHub读取本PROGRESS与[K04 §§11–17](guides/K04_COACH_AND_PLAYS.md)、[SRC-0040..0047](SOURCES.md)、[VIS-TODO-R02](visuals/EXTERNAL_VISUALS.md)，**优先目标PC22原版画面，而非继续堆积旧论坛讲法**。
2. 若有清楚原版PC22 Coach、ACE/Freelance、Book与个人防守视图，登记原链接/确切版本/菜单位置/页签/可辨字段/版权，按证据升级。优先原版PC22 **赛前Coach页**和**指定对手个人防守/Book的动态2D预览**两个画面组合。只有PS4/Xbox One一代画面则标`CURRENT_GEN_ANALOGUE`。
3. **一次有限公开检索**仍拿不到可靠原版PC22界面，保留UNKNOWN；把目标画面需求交未来玩家可选截图/已获授权Antigravity的原生专项，**关闭R02公开文献阶段直接进入R03团队/个人训练、疲劳、伤病和自然成长**。不因此启动DEV28或Codex。
4. V3的后续顺序是R03训练健康、R04全量球员及Agency、R05财务合同经营、R06历史规则与媒体、R07全角色矩阵、最后FINAL-CODEX；V2旧排期不再权威。每轮更新GitHub并回读。

> 权限与边界：R02-B只做网页研究及GitHub文档更新。用户批准前不启动游戏内存扫描、正式存档、比赛模拟、球员属性编辑、DEV28、Codex或外部Agent实现。研究可提出不同教练目标和反对声音，**不将篮球策略强制为全队最优模板**。
