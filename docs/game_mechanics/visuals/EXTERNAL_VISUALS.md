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
