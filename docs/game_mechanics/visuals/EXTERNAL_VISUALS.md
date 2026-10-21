# DEV29 外部截图/图文证据索引

> 版权策略：本文件只保存网页定位信息和待证可见性，**不复制第三方图片到GitHub**。无法直接审看画面像素时只能标记“待人工/后续截图核对”，不能将帖主描述等同图片中确证字段。2026-10-20首次研究。

| VIS ID | 关联来源 | 游戏版本/模式 | 位置 / 原始网页 | 可追溯的证据与待核项 | 审查级别 | 分发许可 |
|---|---|---|---|---|---|---|
| VIS-0001 | SRC-0014 | NBA2K22 PS5/次世代 MyCareer（玩家自报） | [Reddit贴文内两张原始截图](https://www.reddit.com/r/NBA2k/comments/uxwomf)，原文靠近帖子开头“Image: img”两处 | **已核实原帖称包含两图**，帖主与评论谈Shot Chart/Hot Zones差异；**未独立读取原图像素、栏目名和数值**；不能证明PC MyLEAGUE页签 | EXTERNAL_VISUAL_CANDIDATE_NOT_PIXEL_VERIFIED | 第三方版权未明，只留链接 |
| VIS-0002 | SRC-0004 | 官方NBA2K22 PC英文手册 | [官方PDF第2页（0基索引第1页）目录](https://cdn.2kgames.com/manuals/nba2k22/PC/2KSWIN_NBA2K22_PC_Online_Manual_ENG.pdf) | **已逐页查看目录截图**，包含基本/进阶操作、战术及防守，不提供MyLEAGUE统计图谱；作为官方文档覆盖边界证据，不是游戏数据页 | OFFICIAL_PDF_PAGE_VISUALLY_CHECKED | 官方版权；仅链接，不复制 |
| VIS-0003 | SRC-0006 | 2K22论坛中的2K20历史Box操作经验 | [Operation Sports贴文第11页对应回帖](https://forums.operationsports.com/forums/forum/dynasty-headquarters/basketball-dynasties/923062-thunder-up-rebuild-in-okc-nba-2k22/page11) | **文字证据索引，不是已发现截图**：回帖给出Box按Y/Triangle切换系列历史场次的方法，需PC22 screenshot/实机认证 | TEXTUAL_VISUAL_CAPTURE_REQUEST | 原帖版权，链接定位 |

## 目标PC22截图证据待办（R01-B，不依赖实时写入游戏）

| 待补截图位 | 需要截的画面与关联指南 | 最关键的证据 |
|---|---|---|
| `VIS-TODO-PC22-01` | MyLEAGUE联赛赛程：同一天一场已完成与未完成比赛 | 日期/主客/比分/菜单操作与可选Daily View |
| `VIS-TODO-PC22-02` | 已结束比赛的Box Score：球员页与球队页各一张 | 所有列、DNP/Starter、加时与节次、真实比赛身份 |
| `VIS-TODO-PC22-03` | 球员统计的页签栏、Game Log（若存在） | 是否有逐场栏目、可选赛季/阶段、对手/日期 |
| `VIS-TODO-PC22-04` | 球队/球员Season Stats：Per Game、Per36、Advanced（若存在） | 真实名称、字段与过滤器完整列表 |
| `VIS-TODO-PC22-05` | PC22 MyLEAGUE的Shot Chart/Hot Zones（若有） | 单场/赛季范围、分区/坐标的实际有无 |
| `VIS-TODO-PC22-06` | League Settings中Quarter Length、Simulated Quarter Length、Normalize | 实际选项名称、当前值、开关、对应游戏模式 |

**使用方式**：图源仅说明到何处核查。除`VIS-0002`外，本轮没有逐像素确认可引用的截图字段，公开攻略不得写成“已有PC22原生截图”。图证补全后可以按此编号推进；玩家私有实机截图遵守`visuals/README.md`的授权路径。


## DEV29 R01-B 图文与菜单证据增量（2026-10-20）

> 新索引的外部页面图片仍然**只做网页定位**，除非可读到图中像素和真实菜单，不得声称已认证任意PC22原生UI。数字ID与R01-A保留，不覆盖旧条目。

| VIS ID | SRC ID / 原始链接 | 对应版本/状态 | 图/文字所在位置与证明了什么 | 目前未证明什么 | 图像版权 |
|---|---|---|---|---|---|
| VIS-0004 | SRC-0020 / [Gamepur 2K22 Hot Zones攻略](https://www.gamepur.com/GUIDES/NBA-2K22-HOW-TO-FIND-A-PLAYERS-HOT-ZONES) | NBA2K22 MyCareer/MyTeam，文章标“Screenshot by Gamepur” | 页面中Hot Zone图/说明；原文给MyCareer暂停→Stats→Roster→R3→RT/R2切换Hot Zones | 截图像素未独立核对，**不是MyLEAGUE菜单图证** | 网站第三方，链接-only |
| VIS-0005 | SRC-0025 / [2K22 PC Remastered UI展示](https://www.2kspecialist.net/2021/09/nba-2k22-remastered-blog-new-details.html) | **MODDED_PC22_NOT_VANILLA** | “Main Menu Overhaul”及自定义PC版MyNBA样式截图所在版块，用来排除误用修改版界面 | 不可作为PC22原生统计页/Hot Zone/Box确证 | 第三方模组作者，链接-only |
| VIS-0006 | SRC-0024 / [NBA2k线上未保存比赛BUG报告](https://www.reddit.com/r/NBA2k/comments/xk44uu) | 2K22/23线上模式跨平台，不属于目标PC离线 | 发帖文字称附50多场未存比赛的截图；定位到正文第2个“Bug”段落；本轮**未核对图片像素** | 并无PC22离线Game Log历史留存证据 | 玩家图片，只留原帖链接 |

### 重要的“只有文字，没有截图”的索引

- [SRC-0016 OS 2K22 Useful Findings 第7页 #93/#96](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917203-nba-2k22-useful-findings/page7?t=992582)：玩家**用文字**指出游戏结束后Shot Chart可与Stats Summary/PIP比对；这是一手报告，但**不是截图认证**。
- [SRC-0017 Reddit 2K22 Feedback](https://www.reddit.com/r/NBA2k/comments/plmeto)：PS5玩家**用文字**指出Triangle切到Per36和该页排序异常；无本轮独立核对的PC22表格截图。
- [SRC-0021 OS 2020 MyLEAGUE历史Bracket](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/889354-myleague-viewing-past-playoff-bracket)：Coach2K仅文本回答，没有确认旧单场Box留存范围。

### 下阶段最有价值的截图集合（保留R01-A的六位TODO）

优先序：`VIS-TODO-PC22-03` (Stats页面完整表头、Triangle/Y真实按键) → `VIS-TODO-PC22-02` (当前赛季主客Box、球员列和球队列) → `VIS-TODO-PC22-01` (同日不同比赛日历与进入Box方式) → `VIS-TODO-PC22-05` (赛后Shot Chart及历史查询) → `VIS-TODO-PC22-04` (球队/球员Advanced、Per36所有列) → `VIS-TODO-PC22-06` (实战模拟分钟与标准化参数)。额外需要**跨赛季的只读存档画面**验证旧Bracket/Box是否能调出，不能为了取证擅自推进正式世界线。


## DEV29 R01-C — 官方图文中的Box描述与PC截图缺口（2026-10-20）

| VIS ID | 关联 | 图文位置、实际可见信息 | 为什么不能当PC22 Box证据 | 权利/状态 |
|---|---|---|---|---|
| VIS-0007 | SRC-0026 | [2K22 MyNBA开发团队说明](https://hoopsgamers.com/nba-2k22-mynba-full-details-mystaff-training-pre-built-teams-more) 的`COMPACT SPREADSHEETS`小节；旁边配图为`MySTAFF Roster`，[该配图原地址](https://assets.2k.com/1a6ngf98576c/7jr3c008x0rKag3ykS3nGs/adaf38d3e3c8870bb2337758d53eb751/Roster.jpg)。对应**官方文字**提到了Box Score，但图片名称为Roster.jpg，不是已证的Box Score截图。 | 官方原文明确本节属于2K22 **次世代MyNBA**，不能证明PC本世代MyLEAGUE布局，也没有提供完整球员/球队Box表头。图片原地址本轮未逐像素解析，不升级为已检视像素的Box证据。 | 2K官方图片受版权保护；仓库只索引，不转载。状态：`OFFICIAL_NEXTGEN_ADJACENT_VISUAL_NOT_PC22_BOX` |

### R01-C图源质量审计

公开检索出现若干题为“NBA2K22 PC MyNBA”的图片，已登记`VIS-0005`说明存在**将次世代界面移植到PC的Remastered模组**，无法在缺少原版/模组元数据时拿来确证PC原生菜单。其它命中包括NBA.com 2021–22真实比赛的Box、NBA 2K22 MyCareer热区图、2K21/2K23教学视频、非NBA2K统计模拟器；**不得计入PC22 MyLEAGUE原生菜单截图覆盖率**。

**保留未完成原生取证任务**：`VIS-TODO-PC22-01..06`全部待PC22原版画面。R01-C为其补充以下**单张/少量截图即可回答的判定标准**：

- `STATS_HEADER`：截图包含游戏版本/页面位置、筛选器、列名以及底部按钮映射；每种Totals/PerGame/Per36/Advanced类型各至少一张，不能单凭2K22 PS5写PC按键。
- `GAME_BOX_TWO_TEAMS`：在同一场已完赛比赛显示主客身份及两个队伍的球员行、团队总计；每页可以多截，记录是否能横向切列。
- `GAME_LOG_OR_CALENDAR`：若找不到独立Game Logs标签，也要拍可检索到的所有相关Stats页签并记录实际路径，才能区分`FEATURE_NOT_FOUND_IN_UI`与`GAME_LOG_ABSENT`。
- `POSTGAME_SHOT`：同场赛后Shot Chart与赛程旧Box页面分别截图，核查是否能在离开比赛后重新打开；热区图不能替代Shot Chart。
- `OLD_SEASON_BOX`：只在已经自然经历跨季的**只读页面**检查旧季；不推进、修改正式存档，也不能以旧赛季Standings推断旧Box有无。

原网页/视频的**准确时间戳若无法读取视频帧，保持`UNKNOWN`**，不得虚构“第几分第几秒看到表头”。图证索引暂不上传任何图片二进制。


## DEV29 R01-D — 最终截图来源审计与最小取证请求（2026-10-20）

**本轮合格新增`VIS-####`为0。** 既有`VIS-0001..0007`全部保留原先版本、来源和许可级别；没有任何一条升级为目标`PC22_UI_CONFIRMED`。**严格禁止为了凑图源数把游戏封面、Steam外层成就统计、NBA.com或2K22 PC Remastered当作原版MyLEAGUE统计图。**

### 排除项（不是新增VIS）

- [Steam NBA 2K22社区Screenshots](https://steamcommunity.com/app/1644960/screenshots/)：PC游戏平台身份成立，但当前检索未找到可同时识别原版MyLEAGUE及真实Box/Stats表头的可审查图片；外层“View Stats”是成就页，不等于游戏内`Player Stats`。
- [GamesKeys 2K22 MyLeague Player Lock文章](https://gameskeys.net/how-to-use-player-lock-position-lock-in-nba-2k22/)：带MyLEAGUE操作截图但主题是`Player Lock/Position Lock`，不显示本次需要的Box/Advanced/Game Logs表头；按键提示采用PS手柄术语，平台不能强行标PC。
- [2K22 PC Remastered](https://www.2kspecialist.net/2021/09/nba-2k22-remastered-blog-new-details.html)已有`VIS-0005`：非原版，禁止提升UI认证。
- 其它视频/图片检索：无法读取实际相关帧或得不到准确时间戳时只能记录为`VIDEO_FRAME_NOT_REVIEWED`，**不能声称看见任何具体字段**。

### 从六类TODO缩成三组最少截图（用户将来可按需提供）

| 优先级 | 保留原TODO | 最少提供 | 从画面要记录的原始事实 | 一组图可关闭的疑问 |
|---|---|---|---|---|
| **A，先做** | `VIS-TODO-PC22-03`+`04` | **约2张**：①Stats入口/菜单栏/按钮提示；②进入Player Stats或League Leaders后页签、切换提示、真实表头 | `NBA2K22 PC original offline MyLEAGUE`、选中球员或球队、栏目名/英文原文、筛选、按钮映射 | ①Stats、②独立Game Logs是否可由页签看出、④Per36/Advanced候选 |
| **B，接着做** | `VIS-TODO-PC22-01`+`02` | **约2张**：①已完赛日期的Calendar/选中比赛操作菜单；②同一场Box含主客/列名；另一队或Team Totals不在同屏时补一张 | game date/season/phase、主客、Box球员/球队栏目、能否横向切字段 | ②Calendar→Box实际路线、③Player/Team Box和本季比赛可回看 |
| **C，按需要** | `VIS-TODO-PC22-05`+`06`及跨季 | **按已有页面补1–2张**：赛后Shot Chart或已经自然完成的旧赛季Box入口；若模拟口径仍不明再拍Setup | 图中区域/图例/时段、是否从旧比赛重开、跨季可见窗口、实际`Normalize`名称 | ⑤Shot Chart与Hot Zones关系、⑥历史留存；节长标准化作为质量上下文 |

当组A/B无法显示某项，也只记录`NOT_VISIBLE_IN_OBSERVED_PAGE`，而不是`FEATURE_ABSENT`。组C的“跨季”只能在**已自然跨季**存档进行只读查询，不为取证擅自模拟或推进正式世界线。所有图片若未来获准归档，需补作者/平台、存档阶段、版本、无模组声明、操作页面路径、字段、权利及`VIS`编号；**本轮没有上传任何第三方媒体文件或生成图像**。

**结案标记**：`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`。未来R01截图空缺交给独立玩家只读页面取证/以后授权的Antigravity，DEV29网页研究现在直接转R02。详见[PROGRESS](../PROGRESS.md)与[攻略§20–22](../guides/K01_K02_GAME_STATS.md)。

## DEV29 R02-A — 教练与战术视觉证据审查（2026-10-20）

视觉素材不等于每个画面的游戏版本与模式已经认证。**本轮没有新的NBA2K22 PC原版MyLEAGUE Coach/Playbook/ACE全部菜单的逐像素认证图**；资料的一手文字可以支持机制经验，但截图等级必须独立审核。

| VIS ID | 来源、原始页面 | 可定位到什么 | 图证等级与适用限制 | 许可 |
|---|---|---|---|---|
| **VIS-0008** | SRC-0033 / [Operation Sports 2021-10-18：Help Defense Saga Part 2](https://www.operationsports.com/the-ongoing-help-defense-saga-in-nba-2k22-part-2/) | 文章页面主图为“NBA 2K22 help defense”，正文中有作者引用的弱侧协防/赛中画面示例说明和视频内容区；真实支持的是**同年文章中的防守AI/补丁评论** | **EXTERNAL_VISUAL_CONTEXT_NOT_MENU_PIXEL_VERIFIED**：本轮未独立检查视频逐帧、不提供时间戳，主图也不是已认证的PC22 Coach Gameplan字段截图；不能证明本局菜单某项已实现 | 图片/视频属原作者或第三方，仓库仅留网页链接 |

### R02-B定向视觉候选清单（暂不把待办算成VIS证据）

| 待办 | 最少画面及为何重要 | 能认证与不能认证 |
|---|---|---|
| VIS-TODO-R02-01 | 原版NBA2K22 PC MyLEAGUE Coach Gameplan首页、POE栏目、底部按键提示 | 静态POE页签/菜单；**不**证明3D自动效果 |
| VIS-TODO-R02-02 | 同一球队Book编辑界面：Regular/Bench/Endgame/Favorite切页及1条完整Play Name/2D战术预览 | 证明UI类别、槽位与当前CRC关联候选；**不**凭名字写入类型id |
| VIS-TODO-R02-03 | Player Edit/PlayTypes四槽有序分配与12类具体play目录过滤面板 | 证明“球员角色枚举≠play类别”两个界面独立；需同时记录过滤后候选及实际动画 |
| VIS-TODO-R02-04 | Freelance四槽与Offensive Settings/ACE/Automatic Playcalling是否在比赛暂停/Timeout菜单出现 | 区分本队静态Coach字段和比赛内动态调整；不从PS5视频直接推PC |
| VIS-TODO-R02-05 | 选定对手具体球员的个人防守页及整体防守页（只读） | 查看18类列及特殊OnBall5/Hedge5/TagOnRoll含义；**日常GM仍不写OVERALL** |

已检索但不当可认证画面：SRC-0034 Xbox One+Series X原帖写了防守选项且作者纠正错误，可给**同代文字**，不自动产出PC22截图；SRC-0039 NG玩家写PlayVision/Auto菜单，不代表其有目标PC UI；SRC-0038按键控制表，不是球队Coach配置图。未来如有玩家自供真实截图且获得允许，可按[视觉材料规范](README.md)在approved/独立保存。**R02-A研究无游戏读写、无第三方图片复制、无虚构视频时间戳。**

## DEV29 R02-B — 菜单真实画面审计与最后一轮PC22截图优先级（2026-10-21）

**新增合格原版NBA2K22 PC MyLEAGUE可读菜单图证：0；VIS-0001..0008原证据等级不变。** 仅有文章正文引用了“视频”“Image”或玩家文字说明菜单，并不能登记为`PC22_UI_CONFIRMED`。没有获取或上传任何版权不明的图片文件。

| 文本/画面线索（本轮新增） | 原始页面 / 来源 | 实际核实到的证据 | 不得声称 |
|---|---|---|---|
| 2K22的ACE即使Off，Defensive Settings仍自动切回的报告 | [OS 2022-01 贴文](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/920049-defensive-settings-not-staying-on-custom) / SRC-0040 | 原作者与回复在搜索索引可读；**直接打开因redirect loop失败** | 已看见PC22原版ACE UI/证明一切ACE设置无效 |
| 2K22 Series选中后回Freelance | [OS 2021-09-16原帖](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917118-are-series-not-working) / SRC-0042 | XBX作者的**文字一手报告**，没有本轮逐帧视频和时间戳 | PC22必然同错，或已经读取Series native ID |
| Xbox Series X/S **MyTEAM**的Run Freelance菜单步骤 | [Reddit 2K22教程](https://www.reddit.com/r/MyTeam/comments/q36nsh) / SRC-0043 | 作者自报平台与按键、场上两步激活流程；**未提供可复核PC MyLeague页签图** | 相同的PC22按键/自动CPU调用 |
| 2K16的On Ball Screen (Center)与Hedge (Center)讨论 | [OS 2016 第2页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/806956-on-ball-screen-center-hedge-center/page2) / SRC-0044 | 可读取旧版多位玩家对持球防守者/掩护人/己方大个身份的争论 | PC22 Center字段精确触发、UI顺序或实战执行已实机认证 |
| 旧版TagOnRoll从Gameplan消失、SimCast仍能访问的报告 | [OS 2018 第2页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/865843-defensive-settings-discussion/page2) / SRC-0045 | 玩家文字明确表示**没有验证SimCast改动效果** | PC22一定隐藏或SimCast能执行 |
| PC版CPU-vs-CPU MyLeague实际玩家生态 | [OS NBA2K PC Forum](https://forums.operationsports.com/forums/forum/basketball/nba-2k-pc-forum/918715-cdcool-nba-2k22-cpu-vs-cpu-myleague-sliders) / SRC-0046 | 原帖实际自报PC、控制所有队、逐场看3D不快Sim | 已经找到本机PC22 Coach菜单像素/默认数值 |

### R02-C仅一次目标视觉补证，优先2组少量截图

- **组A（控制入口，优先2–3张）**：现有原版PC22离线MyLEAGUE Coach Gameplan中的POE/Coach Settings/Freelance四槽、ACE/自动叫战术菜单（若出现）。要求画面包含完整栏目、可选值、上下文与底部按键说明；需分清赛前静态 vs 暂停临场，两者若不同分别标注。
- **组B（战术内容/对手方案，优先2–3张）**：Book编辑内Regular/Bench/Endgame/Favorite、12类别筛选、某条具体动作的2D动态棋盘；以及选定对手某持球者后的PERSONAL Defense页中`OnBallScreen(Center)/Hedge(Center)/TagOnRoll/PreRotate`（已有页面能看见哪些就截哪些）。
- **历史保持未知**：任何截图能证实**UI菜单是什么**，但不能证明3D比赛真实跑此play或ACE永久保存。同一对手不同时间读数对比/视频必须有明确场次、时间戳与平台；未经同意不推进/模拟正式比赛。

若第三方公开视频无法读取足够清晰的原始菜单画面、没有可信的精确时间戳，统一`VIDEO_FRAME_NOT_VERIFIED`。R02-C若仍无新一手原版图，**保留UNKNOWN并关闭R02公开研究，转R03**；不为一个UI无限重复搜索2K16或在研究期启动DEV28/Antigravity。本文件只有文字索引、没有第三方截图复制。

## DEV29 R02-C — 最后一轮直接图证核查及R02研究结案（2026-10-21）

**原版NBA2K22 PC本世代离线MyLEAGUE Coach/ACE/Playbook/Freelance/Personal Defense可复核完整UI新增：0。** 保留`VIS-0001..0008`既有定位和证据等级，不把本轮检索到的截图容器、文章主图或模拟版MyNBA误记为`PC22_UI_CONFIRMED`。本轮没有获得能完整核实的目标视频帧或准确时间戳；因此**不新增编号式VIS实证**。SRC-0048是MyLEAGUE玩家对Freelance按球队自动保存的**纯文字**一手报告，亦不产生图证。

### 定向公开素材审计

| 链接/检索线索 | 实际来源属性 | 结论 |
|---|---|---|
| [NBA2K22 Steam社区](https://steamcommunity.com/app/1644960/screenshots/)及[SteamDB游戏截图](https://steamdb.info/app/1644960/screenshots/) | PC游戏ID是正确的，但目前没有可辨别目标MyLEAGUE赛前Coach页面全部字段的独立原版画面 | **PC game container only**，非原版Coach截图实证 |
| [官方2K22 MyNBA新功能报告（OS转载）](https://www.operationsports.com/nba-2k22-mynba-details-revealed-mystaff-staff-carousel-prep-hub-attributes-badges-more/) | **PS5 / Xbox Series的MyNBA**；明确含Conditional Coaching和更新后的Coach Gameplan表格 | 可供V3未来条件决策概念参考，**不得认证PC本世代也有该原生命令界面** |
| [2K22原版PC Remastered UI新闻](https://www.2kspecialist.net/2021/09/nba-2k22-remastered-blog-new-details.html) | 标明移植MyNBA外观的改装PC UI，先前VIS-0005已登记 | 排除，禁止当作vanilla MyLEAGUE |
| [NBA2K22同发行季MyLEAGUE Freelance保存讨论](https://www.reddit.com/r/NBA2k/comments/qg2amb) / SRC-0048 | 2021-10/12文字，平台未知，玩家表示比赛中改Freelance会为队伍保存 | **TEXT_ONLY_NO_VIS**，不认证PC22保存范围 |
| [被错误日期误导的“2K22精确分钟”攻略](https://www.magicgameworld.com/how-to-adjust-player-minutes-in-season-mode-in-nba-2k22-myleague/) | 显示2021-04-30早于2K22正式发售，且无可读原版菜单，仅泛化控制叙述 | **REJECT_DATE_PROVENANCE_AND_GAME_AI_CONFLICT**，不单独分配VIS |

### 保留的最小未来只读截图需求（不会阻断R03）

**A：教练设置两页。** 同队原版PC22 MyLEAGUE赛前Coach Gameplan（包含6 POE中的实际项目/下方按键），以及比赛暂停/ACE/进攻设置（如可进入）各1张；记录是否同一支球队和游戏阶段，避免把比赛策略当静态字段。

**B：战术/防守两页。** 本队Book内一条play的完整名称、类型筛选及2D战术板（如果不是同页可追加1张），以及一个指定进攻球员的PERSONAL Defense页面（优先Center与TagOnRoll/PreRotate选项）。可以先只提供有画面的部分，未出现的字段仍UNKNOWN。

身份条件：`NBA2K22 / PC_CURRENT_GEN / VANILLA_UNMODDED / OFFLINE_MYLEAGUE / menu_path / game_date / team / before-or-after-timeout`，且真实表头能清楚阅读；不要求玩家模拟正式比赛或读取内存。**未看见某个字段≠引擎没有该功能。**

**R02官方结案：`R02_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`。** 已有原生字段和当前采集能力保留原等级；待以后独立授权的Antigravity/DEV28定向只读取证或玩家偶尔自主截图时，增量升级K04，不重开R02整个网络研究。**下一研究批次R03训练/健康与自然成长。**

## DEV29 R03-A — 训练和负荷的官方可读图证（2026-10-21）

本轮新增**2个已实际查看像素的官方2K22次世代图源**；**NBA2K22 PC本世代离线MyLEAGUE训练菜单合格画面仍为0**。第三方/官方版权图片**只留稳定原图URL/官方出处，不上传到GitHub**。图源版本不可因同为2K22而合并。

| VIS ID | SRC ID/官方页与原图 | 平台、模式、具体可见栏目 | 原生PC22取证资格 | 权利及状态 |
|---|---|---|---|---|
| **VIS-0009** | SRC-0049/0050；[2K Newsroom原页](https://newsroom.2k.com/news/nbar-2k22-adds-new-features-to-mynba-for-playstation-5-and-xbox-series-xs-consoles)；[Individual Training Focus PNG](https://cdn.prgloo.com/media/2858117e546348dbb3c016b7282e72c3.png?height=663&width=442) | **NBA2K22 PS5/Xbox Series MyNBA**：已看见`SKILL TRAINING FOCUS`、位置列表PG/SG/SF/PF/C、`PLAYER TYPE`、`TRAINING COMPATIBILITY`列及所选球员OVR；PG可见一组all-around/two-way/Offensive/Defensive/Athletic/Rebounding/Playmaking/Outside Scoring/Inside Scoring原型名称 | **不符合PC22_UI_CONFIRMED**；不能凭截图给本机(player.position,player_type)和UI顺序建立1:1 raw映射 | `OFFICIAL_NEXTGEN_SCREEN_PIXEL_REVIEWED`，2K版权，仅文字/外链 |
| **VIS-0010** | SRC-0049/0050；[官方Newsroom原页](https://newsroom.2k.com/news/nbar-2k22-adds-new-features-to-mynba-for-playstation-5-and-xbox-series-xs-consoles)；[Training Schedule PNG](https://cdn.prgloo.com/media/eedbfc01c17a465eb26f5093c697ee8b.png?height=663&width=442) | **2K22次世代MyNBA**：已看见`TRAINING SCHEDULE`日期日历、底部`TEAM SYSTEM`、`TRAINING GOALS`、`TEAM OVERVIEW`三块信息摘要；多日练习/比赛与球队系统显示在同屏 | **不符合PC22_UI_CONFIRMED**；不能证明PC当前局逐日计划、实际疲劳单位、官方建议训练配方；小图中的所有练习格文字未完整验明 | `OFFICIAL_NEXTGEN_SCREEN_PIXEL_REVIEWED`，2K版权，仅文字/外链 |

同页有[Prep Hub原图入口](https://cdn.prgloo.com/media/3d1a4901fc3c49cd8f4a0f65808d1a61.png?height=663&width=442)，**本轮无法可靠取回原图像素**，只作为文字定位，不分配新的已认证VIS。

### PC22 R03未来最小分批只读证据（无需现在提供）

1. **团队训练页（约1–2张）**：原版PC22无模组离线MyLEAGUE，完整主页/客场强度、是否Auto、背靠背前后休息与恢复选项的屏幕、可选值、游戏日与页脚控制提示。
2. **个人训练页（约1–2张）**：当前人物、Position、可见训练原型/模板列表、强度、Override和伤病恢复，优先一名PG及一名中锋用于发现UI模板按位置变化。不要为了取证擅改正式存档。
3. **健康和导师页（以后可选）**：在已经自然发生的状态下截玩家fatigue/fatigue history、伤病状态与预计康复、训练师/导师链接，以及徽章发展的显示数据；必须区分“历史条”和“当前值”。

截图可认证**菜单候选/来源身份**，但不能保证训练收益或伤病概率。现有技术目录的`progressive_fatigue_history`尚无本轮实时解码认证，不能以任何截图名词替代。

**R03-A真实图证：VIS-0009..0010为2K22官方次世代**；目标PC22新增UI图证0。后续R03-B继续伤病/恢复/真实负荷来源，不需再次把Prep Hub营销稿当作PC22证据。

## DEV29 R03-B/C — 健康/导师原版视觉取证与审核结案（2026-10-21）

R03-B和R03-C新增合格`NBA2K22 PC VANILLA OFFLINE_MYLEAGUE` **健康状态、伤病列表、康复剩余天数、导师进度或Trainer精确效果的菜单截图：0**。既有`VIS-0009/0010`是已实际查看像素的**2K22官方次世代MyNBA训练页**，持续作为高价值终极联盟机制参考，不降级其机制价值，也**不冒充PC本世代屏幕或字段读值**。

| 可追溯图证线索 | 本轮实际可用证据 | 图证级别与边界 |
|---|---|---|
| [OS 2021 MyLeague Injury Sliders](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/918980-myleague-injury-sliders) / SRC-0060 | 玩家关于手打/Sim伤病差异的**文字实战报告**，也有人自述亲见Luka受伤动画 | `TEXT_ONLY`；未看到可认证PC22的受伤视频具体帧 |
| [OS 2022 MyLeague Why no injuries](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/921266-myleague-why-are-there-no-injuries) / SRC-0061 | 多位玩家对滑块/Durability调节作出互相冲突的文字描述 | `TEXT_ONLY`；改Durability不是研究授权动作 |
| [OS 2022/23 MyNBA Injury Duration](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/926689-mynba-injury-duration) / SRC-0063 | 历史伤停时间与实际返场提前的玩家回忆/个案 | `TEXT_ONLY`；无原版PC22恢复日列表像素 |
| [Reddit 2022 Mentor assignment crash](https://www.reddit.com/r/NBA2k/comments/s88jzz) / SRC-0068 | 玩家对某些导师组合会引起崩溃的文字描述 | `TEXT_ONLY`；未获得重现录像与PC版本证据 |
| [2K官方新世代MySTAFF医疗分工](https://www.operationsports.com/nba-2k22-mynba-details-revealed-mystaff-staff-carousel-prep-hub-attributes-badges-more/) / SRC-0064 | 各Sports Medicine职位功能的官方文字/图片上下文 | `OFFICIAL_NEXTGEN_MECHANISM`；不证明PC22本世代能聘七个新医疗岗位 |

### 以后最少4组可分批取证（不是现在让用户执行）

1. **真实伤病页**：当前Game Date、球队、具体球员身份、伤病类型/部位/严重度、预计返场天数与真实最后复赛日期。至少同一球员两个自然出现的时间点；未出现伤员时不人为制造。
2. **实时与历史疲劳**：同一球员的比赛前/后体力、Training History或Progressive Fatigue字段，明确时点、单位、原版或次世代来源；不由过去历史尾数假装当前体力。
3. **导师页**：一个真实Mentor/Mentee pair、可选Badge、Compatibility和自然推进后的进度，优先仅只读；发生已知崩溃风险则停止，不操作正式游戏。
4. **PC本世代Trainer与个人训练原型**：训练师原生UI属性、球员Training中的Position+Player Type原型与Intensity、是否显示Recovery等，和现有Registry逐项映射。

研究完结时的图证状态：`R03_RESEARCH_COMPLETE_WITH_NATIVE_DATA_GAPS`、`PC22_HEALTH_UI_FULL_VERIFIED=0`。**不能据此说原版游戏没有健康菜单，只是当前公开材料无法完成源级认证**。R04完整身体部位Durability的研究会独立展开，在用户审核R03后方可启动。

## DEV29 R04-A — 原版2K22球员资料与Badge视觉证据登记（2026-10-21）

本轮检索NBA2K22本世代MyLEAGUE原始**Edit Player / Vitals / Attributes / Durability / Badge / Personality / Development**菜单，以及同年PS5 MyNBA的可借鉴画面。研究取得**版本指向明确的详细球员字段页面**，但没有逐帧/像素确认`vanilla_PC22_Offline_MyLEAGUE`中同样分组和完整标签的可读截图，**不新增`PC22_UI_CONFIRMED`或已认证正式VIS编号**。本页保留稳定网页索引和未来最小证据请求，供R04后续研究使用。

| 原网页/视觉线索 | 真实性与这次具体获得什么 | 视觉审查结论 |
|---|---|---|
| [2kAuction：NBA2K22 Joel Embiid](https://2kauction.com/mynba/2k22/players/joel-embiid?roster=offseason_nba) 和 [Marques Johnson](https://2kauction.com/mynba/2k22/players/marques-johnson) | 页面以原站文字版分栏输出`Attributes/Badge/Bio/Development/Contract/Injuries`，每个字段具体存在并配一个导出玩家数据样例 | **THIRD_PARTY_GAME_SNAPSHOT_HTML_NOT_GAME_MENU_PIXEL_VERIFIED**：可作字段清单和示例来源，不是原版游戏菜单截图、不是本项目当前save |
| [OS：NBA 2K22 All Player Ratings第2页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/916765-nba-2k22-all-player-ratings/page2) | 页面玩家贴`Jordan Clarkson 2K22 Player Edit`内容，有嵌入的YouTube链接`https://www.youtube.com/watch?v=RWGYk4y_i2M` | **VIDEO_LINK_LOCATED_NOT_FRAME_REVIEWED**：可后续核对版别/菜单，不能填写看见的完整UI字段或视频时间戳 |
| [OS：2021 2K22 ATD编辑报道](https://www.operationsports.com/nba-2k22-attention-to-detail-roster-from-celticlg-and-crew/) | 编辑内容涉及Durability、Attributes、Badge、Peak及Personality；2021-12 PC名单尚处WIP | **CUSTOM_ROSTER_RESEARCH_TEXT**，非vanilla PC本局的真实数值 |
| [2K Film Room：2K22 Badge Cheat Sheet](https://2kfilmroom.com/cheat-sheets/2k22) | 可读取80项当代Badge标签文字，20/20/20/20四类分布 | **TEXTUAL_BADGE_REFERENCE**，不是MyLEAGUE PC Edit Badges原生截图，MyPLAYER解锁条件不能用于本局成长公式 |
| [2K22 PS5历史新秀Boom/Bust讨论](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/916715-jb-s-2k22-ps5-fictional-draft-classes/page6) | 一手作者说明Vitals中最低/最高潜力、Boom/Bust概率和峰值年龄 | **NEXTGEN_PLAYER_REPORTED_TEXT**，不冒充PC原版Vitals图或算法实测 |

### 下一轮最少的定向真实菜单证据（不要求立即用户操作）

1. **人物Vitals 1–2张**：在NBA2K22 PC无模组离线MyLEAGUE下，当前球员姓名/主副位置/生日/身高臂展/选秀和Peak Start/End、Boom/Bust如果有。记录`game_date`和保存版本，避免把同名历史人物当同一ID。
2. **Attributes与Durability 1–2张**：左侧分类和真正可见全部字段，尤其**耐久是否恰为16还是还有其它类别**；截图能证UI列名、不能从一次数值推演伤病概率。
3. **Skill与Personality Badges 1–2张**：徽章组、实际标签、数量和层级，区分赛季自然变化、手工编辑页、MyPLAYER构建页；同版网页清单中的名字不等于本机native badge ID。
4. **人物Development/Contract 1–2张**：`Peak`/可见潜力类设置要严格保密，**不要拍摄或上传会向普通GM/媒体泄露真实Potential的页面**。可仅由授权隔离人员做字段名/选项范围检验并遮蔽真实值。

**版权**：本轮无第三方图像复制或上传。文字研究用`SRC-0072..0082`追溯，新增机读目录`PLAYER_FIELD_AND_RIGHTS_MATRIX.json`和`PLAYER_BADGES_R04_A_REFERENCE.json`对应R04-A，PC可读菜单和完整人物Agent权限以后分R04-B/C/D逐项补齐。
