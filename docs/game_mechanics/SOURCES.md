# 游戏攻略、官方资料与社区证据登记

研究窗口应在此登记每轮**真正打开并核对过**的资料。来源应注明主题、适用版本/模式/平台、发布日期（如可得）、原始链接、支持的结论与限制。来源本身不是游戏内存认证。

| Source ID | 来源 | 适用游戏/版本 | 研究用途 | 证据级别 | 状态 |
|---|---|---|---|---|---|
| SRC-0001 | [DEV29 V1现有来源入口](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V1.md) | NBA2K20–23 | 前期已收集的官方、NBA2KW、OS文献索引 | PROJECT_EXISTING_REFERENCE | 下一轮需按主题核对正文 |
| SRC-0002 | [NBA 2KW — 2K23 MyNBA Settings Explained](https://nba2kw.com/nba-2k23-mynba-eras-settings-explained) | NBA2K23 / MyNBA Eras | 演示完整游戏参数表如何呈现描述、范围、可选项；不能直接当PC22参数 | COMMUNITY_GUIDE / VERSION_SPECIFIC | 导航参考 |
| SRC-0003 | [OS — Adding and removing plays from playbook](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/841395-adding-and-removing-plays-from-the-playbook) | NBA2K18及讨论适用模式 | 玩家报告Playbook容器与UI退出后修改恢复的联系；需要PC22验证 | COMMUNITY_REPORTED / OLDER_VERSION | 导航参考 |

> SRC-0002/3为当前已检查的研究案例，**不是已经完成的主题机制文档**。下一窗口发现原帖已更新/失效须更新状态。勿把初步例子无限重复复制到每张卡片；每个事实直接指向对应的source_id及必要的页内位置。

格式建议：`SRC-#### | title | URL | 20/21/22/23 | PC/PS4/PS5/Xbox | mode | authored_at | reviewed_at | supported_claims | caveats`。每轮只加有实质帮助的来源，不追求引用数量。


## DEV29 R01-A：2026-10-20 首批按主题核对的来源

以下都已读取/核对对应可访问页面内容或带原帖正文的搜索结果。不是PC22内存证据；对PC22具体菜单无直接支持的均保留“不证明”的边界。

| ID | 标题/原始网址 | 版本/平台/模式；发表时间 | 本轮真正使用的事实 | 级别 / 限制 |
|---|---|---|---|---|
| SRC-0004 | [2K官方NBA 2K22 PC英文手册](https://cdn.2kgames.com/manuals/nba2k22/PC/2KSWIN_NBA2K22_PC_Online_Manual_ENG.pdf) | 2K22 PC，官方手册2021；PDF页1–11 | 按键/临场攻防设置；目录**没有**详细MyLEAGUE统计图谱，不能据此判定其不存在 | OFFICIAL_PC22，非统计菜单来源 |
| SRC-0005 | [Operation Sports / Daily schedule in my league?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/781588-daily-schedule-in-my-league) 与 [where is league schedule](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/688998-where-is-the-league-schedule-in-myleague) | 2014–2015早期MyLEAGUE/MyGM，玩家社区 | 从Calendar操作进入Daily View看其它比赛；有玩家明示MyGM与MyLEAGUE权限未核实相同 | COMMUNITY_OLDER_VERSION，不证明PC22准确键位 |
| SRC-0006 | [Operation Sports / Thunder Up! Rebuild in OKC (NBA 2K22), page 11](https://forums.operationsports.com/forums/forum/dynasty-headquarters/basketball-dynasties/923062-thunder-up-rebuild-in-okc-nba-2k22/page11) | 2022讨论；回帖描述 **NBA2K20**，Xbox/PS按键 | 从最近Box按Y/Triangle遍历Game1/2等旧季后赛Box；回帖人主动提示只确认2K20 | COMMUNITY_FIRST_HAND_2K20_ON_2K22_FORUM，PC22未证；页面完整打开曾受缓存影响，使用可见正文 |
| SRC-0007 | [NBA2K21 Next-Gen MyNBA Courtside Report, Dave Zdyrko开发者说明](https://devtrackers.gg/nba2k/p/8ff62bb9-nba-2k21-next-gen-mynba-courtside-report) | 2020，2K21 PS5/Xbox Series MyNBA | 官方制作人说明Daily View包括NBA/G League，支持普通sim、SimCast、SimCast Live；也明确旧MyLEAGUE与新MyNBA不同 | OFFICIAL_AUTHOR_MIRROR_NG，不能认证PC22菜单 |
| SRC-0008 | [Reddit / my league question current gen](https://www.reddit.com/r/NBA2k/comments/v8697b) | 2022-06-09，2K22本世代 MyLEAGUE | 玩家在SimCast跳入比赛后日历102:110→142:150不一致，关闭“normalize sim minutes”后表示修复 | COMMUNITY_FIRST_HAND_ANOMALY，选项精确字符串和普遍性待核 |
| SRC-0009 | [Reddit / myNBA League Leader Stats Bug](https://www.reddit.com/r/NBA2k/comments/us3tgd) | 2022-05-18，2K22线上MyNBA，平台未确证 | 赛季得分异常、Box与累计同时受影响；自述SimCast Live和36分钟标准化 | COMMUNITY_BUG_REPORT，不能外推PC离线 |
| SRC-0010 | [Basketball-Reference Glossary](https://www.basketball-reference.com/about/glossary.html) | 篮球分析标准资料，非游戏页面 | Per Game/Per36、eFG%、TS%、USG%、TOV%、Pace、估算回合等计算定义 | STAT_METHODOLOGY，非2K原生字段证明 |
| SRC-0011 | [Basketball-Reference Four Factors](https://www.basketball-reference.com/about/factors.html) | 篮球战术/四因素方法学，非游戏页面 | eFG、TOV、ORB、罚球因素及攻防两侧解释 | STAT_METHODOLOGY，权重不等于2K胜率公式 |
| SRC-0012 | [NBA.com Players Advanced Box Scores](https://www.nba.com/stats/players/boxscores-advanced) 与 [Players Advanced](https://www.nba.com/stats/players/advanced) | 现实NBA官方统计页，非NBA2K模拟 | 区分真正Advanced Box的可见字段、季/阶段/对手筛选与实际跟踪统计 | OFFICIAL_REAL_NBA_REFERENCE，**不能当作游戏内置栏目** |
| SRC-0013 | [Reddit / Are my hot zones the same in NBA and Park?](https://www.reddit.com/r/NBA2k/comments/q1eays) | 2021-10-04，2K22本世代 **MyCareer/Rec/Park** | 玩家描述从Roster/Stats看Shot Chart与Hot Zone Chart及模式切换；评论对热区继承有分歧 | COMMUNITY_CURRENT_GEN_DIFFERENT_MODE，不能证PC MyLEAGUE |
| SRC-0014 | [Reddit / Can someone explain how Hot Zone works?](https://www.reddit.com/r/NBA2k/comments/uxwomf) | 2022-05-26，2K22 **次世代MyCareer** | 原帖含两张图，玩家称热区与投篮图显示不同；评论解释存在矛盾 | COMMUNITY_NEXT_GEN_SCREENSHOT_POST，图像本体未复制且像素证据待审 |
| SRC-0015 | [Operation Sports / NBA2K22 MyLeague settings/sliders](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917042-2k22-myleague-settings-sliders) | 2021-09~10，2K22 **PS4 MyLEAGUE**，DarthRambo等人 | Simulated Quarter Length、Team Pace、Possessions per Game、Shot Types/Percentages/Stat Distribution影响模拟统计口径；帖内值为玩家自选 | COMMUNITY_FIRST_HAND_CURRENT_GEN，PC相同性仍待核 |

### R01的采信规则

- 对玩家原帖如回复时间和模式不确定，本文注明，非官方承诺不能升级为游戏系统真相。
- **截图已知存在 ≠ 本轮已逐像素核对**。参见 `VIS-0001`，未许可图片不复制。
- `Basketball-Reference` 和 `NBA.com` 是解释篮球计算和数据粒度的参照，不是2K菜单或内存结构的证据。
- 各行的研究核查日期均为2026-10-20；一旦有PC22本机画面，优先新增独立实机证据而非覆写原跨代引文。


## DEV29 R01-B：2026-10-20 新增版本交叉证据（全部保留适用边界）

| ID | 可复核的原始来源与日期 | 游戏/平台/模式 | 核实的操作或风险 | 证据与限制 |
|---|---|---|---|---|
| SRC-0016 | [Operation Sports: NBA 2K22 Useful Findings，第7页，帖#93与#96](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917203-nba-2k22-useful-findings/page7?t=992582)，2021-09-24 | NBA2K22，OS玩家讨论；具体平台/离线模式未认证 | tcnumba10报告赛后Shot Chart可与Stats Summary比较，某些禁区外中投被算入PIP | COMMUNITY_FIRST_HAND_TEXT; **页面未提供本站可像素核对的PC22截图**，不证明内存/历史保留 |
| SRC-0017 | [Reddit: r/NBA2k 2K22 Feedback Vol.1，2021-09-10回帖](https://www.reddit.com/r/NBA2k/comments/plmeto) | NBA2K22 **PS5 MyNBA** | player stats按Triangle切换per-36；PAPG与plus/minus排序被玩家报告有问题 | COMMUNITY_DIRECT_BUG_REPORT，不能用于PC22按钮认证 |
| SRC-0018 | [Operation Sports: NBA2K16 MyGM/MyLEAGUE Thread，第33页，#485–486](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/780313-nba-2k16-mygm-myleague-thread/page33?postcount=238)，2015-10-21 | NBA2K16 MyLEAGUE；PS/Xbox按键 | 统计页按Triangle/Y切换普通、per36、advanced；问题讨论PER与Points per Possession | COMMUNITY_OLDER_MY_LEAGUE_FIRST_HAND，**不证明PC22完整字段** |
| SRC-0019 | [Reddit: How can I look at My Career stats on next gen?](https://www.reddit.com/r/NBA2k/comments/103i5j5)，2023-01-04 | NBA2K23 **MyCareer次世代** | MyCareer→Stats→League Leaders，按Y切total/per-game/per36/advanced | COMMUNITY_OTHER_MODE，不能当MyLEAGUE直接菜单 |
| SRC-0020 | [Gamepur: NBA 2K22 — How to find a player's hot zones](https://www.gamepur.com/GUIDES/NBA-2K22-HOW-TO-FIND-A-PLAYERS-HOT-ZONES)，2021–2022文章 | NBA2K22 **MyCareer/MyTeam** | MyCareer暂停→Stats→Roster→R3→RT/R2到Hot Zones；红蓝灰区域意义和MyTeam不同入口 | GAME_GUIDE_SCREENSHOT_PAGE; 图像元信息存在，但本轮未核对原图像素；**不证明PC22 MyLEAGUE Shot Chart** |
| SRC-0021 | [Operation Sports: MyLeague Viewing past Playoff Bracket?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/889354-myleague-viewing-past-playoff-bracket)，2020-02-23，Coach2K #2 | 2020年MyLEAGUE（当时2K20系列） | 旧赛季Bracket不可回看，前赛季Standings能查 | COMMUNITY_OLDER_MY_LEAGUE，**并未回答单场Box是否删除** |
| SRC-0022 | [Operation Sports: Playing MyEras — any chance to access old stats?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/954313-playing-myeras-any-chance-to-access-old-stats)，2025-03至04，帖#1–3 | 后期MyEras次世代（具体版本/平台没有可靠锁定） | 用户报告旧季详细统计访问困难，另有用户认为年分统计可看，**意见不完全一致** | CONFLICTING_LATER_VERSION_TESTIMONY，不可推成PC22一年留存 |
| SRC-0023 | [Reddit: Is there a way to view season and game records in 2k23 my career current gen?](https://www.reddit.com/r/NBA2k/comments/102td0m)，2023-02回帖 | NBA2K23 **本世代MyCareer** | Play Next Game赛程向过去滚动能打开前面比赛Box；另有玩家表示已找到 | COMMUNITY_OTHER_MODE，**跨季历史未证明** |
| SRC-0024 | [Reddit: Major Bugs of MyNBA Online](https://www.reddit.com/r/NBA2k/comments/xk44uu)，2022-09-21 | NBA2K22/23 **线上MyLEAGUE/MyNBA**多平台 | 发帖人报告部分已打比赛未保存，提及50余场未记录及截图；仅作在线模式质量风险 | COMMUNITY_UNVERIFIED_BUG_REPORT，**不等于PC22离线会丢存档** |
| SRC-0025 | [2KSpecialist: NBA 2K22 Remastered — UI overhaul](https://www.2kspecialist.net/2021/09/nba-2k22-remastered-blog-new-details.html)，2021 | NBA2K22 **PC第三方Remastered模组** | 作者公开展示修改界面并将“MyNBA”样式引入PC；说明网络截图需辨模组 | MODDED_UI_PROVENANCE_WARNING；不用于原生菜单认证 |

**R01-B 文献边界审计（2026-10-20）**：独立打开OS#485-486及2020旧Bracket讨论正文；其余以可访问的原帖/全文检索段核对。图文仅按“页面存在或发帖人声称附图”登记，**不把未逐像素看到的第三方截图当作`PC22_UI_CONFIRMED`**。第三方资料链接不等于再发布图像许可。NBA2K22 PS5≠NBA2K22 PC本世代，NBA2K23 MyCareer≠MyLEAGUE，2025 MyEras≠2021版游戏。最终仍需目标平台独立取证。


## DEV29 R01-C — 2026-10-20 版本/模式明确的新一手资料

| ID | 来源及直接定位 | 版本、时间、作者 | 支持的具体事实 | 严格限制 |
|---|---|---|---|---|
| SRC-0026 | [2K22 MyNBA官方开发团队说明：MyNBA Full Details](https://hoopsgamers.com/nba-2k22-mynba-full-details-mystaff-training-pre-built-teams-more)，§`COMPACT SPREADSHEETS`（[2K原始页面](https://nba.2k.com/courtside-report/nba-2k22-mynba)） | 2021-09-08，Visual Concepts开发团队，经NBA2KW/HoopsGamers转载；**PS5/Xbox Series MyNBA** | 官方文字列`roster, coach gameplan, box score`三类压缩表格，每屏显示行数超过此前两倍；图文页面旁有MySTAFF Roster截图 | OFFICIAL_AUTHOR_REPRINT_VERIFIED_TEXT，**不是PC/PS4 MyLEAGUE界面证明**；未取得可核验的Box本体截图；原站可能403 |
| SRC-0027 | [Operation Sports：What are some new things you want to see in 2K23 MYleague?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/920627-what-are-some-new-things-you-want-to-see-in-2k23-myleague)，2022-02-02/10，#6与#9 | NBA2K22时期玩家讨论（当前世代MyLeague与次世代MyNBA混合） | #6直接区别`Current Gen MyLeague`和`NextGen MyNBA`；#9希望将季后赛统计及单场最高放入球员卡并增强历史跟踪 | COMMUNITY_CONCURRENT_WISHLIST；**期待改进≠已验证PC22功能不存在、也≠存档无Box历史** |
| SRC-0028 | [Steam：NBA2K17 PC MyLEAGUE特殊联盟规则下场内与Box得分不一致](https://steamcommunity.com/app/385760/discussions/0/1290691308577544770/)，2017-05-26，Ray原帖 | NBA2K17 **PC MyLEAGUE** | 玩家指出“罚球自动给分”规则下，场内统计34分，赛后Box/赛季重新结算只计27分；说明一些游戏规则可能造成统计阶段不一致 | COMMUNITY_FIRST_HAND_OLDER_PC；**不是NBA2K22仍有此BUG的证据**，仅用来定义质量风险和分层来源 |

### 本轮保留而不重复计数的来源
- [SRC-0015] 2K22 PS4本世代MyLEAGUE **DarthRambo #1–#2**：再次直接核对原文中`Quarter Length`, `Simulated Quarter Length`, `Team Style Factors`, `Possession Results`, `Shot Types`, `Shot Percentages`, `Stat Distribution`栏目；11分钟和各数值是**作者个人设置**而非PC默认/游戏中的现实回合数。
- [SRC-0025] PC自定义`Remastered`新闻：继续作为排除非原版PC截图的重要警示，不能将其“MyNBA”菜单作为本项目证据。

**研究结果的阴性边界**：针对“NBA2K22 PC MyLEAGUE Game Logs/Advanced/Per36菜单截图、每场完整Box表头、赛后Shot Chart、跨年单场Box寿命”做了多组中文/英文和PC/本世代限定检索。返回大量**真实NBA联盟统计网站**、2K次世代官方图文、2K其它玩法、游戏模组或非NBA2K软件；**没有找到足以逐像素确证上述PC22原生页面的独立公开材料**。阴性搜索不等于不存在功能，不给`PC22_UI_CONFIRMED`、`PC22_NATIVE_READ_VERIFIED`或`PROJECT_CAPTURED`升级。2026-10-20只读取公开材料，没有复用/上传外部截图文件。


## DEV29 R01-D — 最后一轮有界视觉取证（2026-10-20）

**本批次只登记1项经核查、真正提升PC版本边界的新增一手文本；没有获得满足PC22原版MyLEAGUE统计表头标准的可审查截图。** 来源数不是本轮目标。

| ID | 页面 / 准确定位 | 版本、平台、模式 | 可采信的具体事实 | 证据级别与不可外推范围 |
|---|---|---|---|---|
| **SRC-0029** | [Operation Sports — RES2 2K22 All Star Current Gen Sliders，第3页，2022-01-07 #40/#41](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917713-res2-2k22-all-star-current-gen-sliders/page3) | NBA2K22 **PC本世代玩家**的MyLEAGUE设置文字模板；作者首页注明主要玩`Season Mode`，MyLeague配置参考IrishSalsa | 问者询问能否用PC默认阵容；res2答“Yep - PC with default rosters”，转贴自己的MyLeague Setup/Simulation设置：Quarter Length=12、Simulated Quarter Length=11，以及Team Pace/ Possessions Per Game/Shot Types/Shot Percentages/Stat Distribution等项目 | `PC22_COMMUNITY_REPORTED_TEXT`；**不是MyLEAGUE菜单截图或Stats/Box字段认证**。作者在首帖自述实际主要玩`Season Mode`、MyLeague清单借鉴他人后修改；数值是玩家自选，不是游戏默认/用户当前设置，也不构成编辑授权 |

### R01-D公开检索范围与未采用材料（审查痕迹，不计SRC/VIS）

| 检索类别与网址 | 查核结果 | 为什么不升级PC22 UI |
|---|---|---|
| [Steam NBA2K22 Screenshots](https://steamcommunity.com/app/1644960/screenshots/) 和 [NBA2K22社区](https://steamcommunity.com/app/1644960) | 正确游戏PC平台图库，但没有获取到可可靠标记`原版+MyLEAGUE+统计字段可读`的目标屏幕。Steam的“View Stats”是游戏成就页外层UI而非MyLEAGUE中的Player Stats | 画面身份/原始菜单内容不成立 |
| [GamesKeys — 2K22 MyLeague Player/Position Lock攻略](https://gameskeys.net/how-to-use-player-lock-position-lock-in-nba-2k22/) | 包含带截图的MyLEAGUE操作攻略，目标却是`Options→Position Settings→Player Lock`等操作 | **不显示Game Logs、Box Score、Advanced或Shot Chart的已证列名**；无法凭PS按钮断定PC平台 |
| [NBA2K22 PC版已知问题Steam指南](https://steamcommunity.com/sharedfiles/filedetails/?id=2796430022) | PC专属指南，但正文聚焦其它问题 | 不含目标统计菜单截图/字段 |
| [2K22 PC Remastered来源，既有SRC-0025](https://www.2kspecialist.net/2021/09/nba-2k22-remastered-blog-new-details.html) | 非原版UI，前轮已登记 | 排除，不重复新增 |
| 带`NBA 2K22 PC/ MyLeague`标题的网络视频/图像或真实NBA Game Log表格 | 未能同时获得可辨原版PC MyLEAGUE菜单、字段和可靠视频时间戳；部分结果实际是NBA.com、MyCareer、2K23、其它游戏 | **检索标题≠已观看的游戏画面** |

**关闭结论**：R01-D未取得符合五重身份条件（NBA2K22 + PC + 原版无模组 + 离线MyLEAGUE + 可读统计字段）的新图证；记作`NO_NEW_PC22_UI_CONFIRMED`，不等于“无Box Score/无Game Logs”。已完成公开研究`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`。未来新截图只增量更新当前指南§20、[VIS TODO](visuals/EXTERNAL_VISUALS.md)和[PROGRESS](PROGRESS.md)，下轮直接研究R02教练与攻防。

## DEV29 R02-A — 教练与攻防机制：2026-10-20新核对资料

以下新增的是**真正有教练/战术作用事实的来源**，并非只按游戏标题扩展检索量。URL在本轮分别打开或审看可访问的对应作者原帖/官方正文；社区数字只是个人经验，主机同代不自动成为PC22实机认证。

| ID | 原始页面与定位 | 版本/平台/模式及时间 | 本轮支持的具体事实 | 证据等级与限制 |
|---|---|---|---|---|
| **SRC-0030** | [2K官方新闻：NBA 2K22 Unveils New Gameplay Innovations](https://newsroom.2k.com/news/nbar-2k22-unveils-new-gameplay-innovations)，Defense/Shot IQ段 | 2K22官方，2021-08-31；跨平台新闻，对PC MyLEAGUE菜单无专门字段表 | 2K22官方宣布重新设计干扰投篮、封盖、防守轮转，并重视高质量出手机会 | OFFICIAL_2K22_GAMEPLAY；不认证Coach某个字段的量化效果 |
| **SRC-0031** | [OS：NBA 2K22 Useful Findings首页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917203-nba-2k22-useful-findings)，2021-09-18 **#1、#4、#5** | 2K22同年玩家，作者比赛设备/模式并非全部可精确认证 | tcnumba10与jimbo3772对Touches、Shot Tendency、Play Discipline、教练Run Plays和Book/PlayTypes关联提出不同经验；#5发现球员类型与本队书的类型未匹配使该SF得不到合适战术 | COMMUNITY_2021_FIRST_HAND_DISCUSSION；不是官方AI公式；触球50等个人调数值不适用于项目自动建议 |
| **SRC-0032** | [OS：NBA 2K22 Useful Findings 第10页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917203-nba-2k22-useful-findings/page10)，2021-10-07 **#136–139** | 2K22玩家，未独立确定其PC/PS5/PS4 | Tynole14声称自动叫战术反复只给魔术两名后卫，改Touches没解决；另一用户观察相反/提供不同替代经验 | COMMUNITY_CONFLICTING_PLAYCALLING_REPORT；不是PC22稳定缺陷，更不构成改球员倾向授权 |
| **SRC-0033** | [Operation Sports：The Ongoing Help Defense Saga in NBA 2K22 Part 2](https://www.operationsports.com/the-ongoing-help-defense-saga-in-nba-2k22-part-2/)，Chase Becotte，2021-10-18，Help Defense Issues / On Ball vs Off Ball / Gameplan段 | 2K22同年作者亲玩/技术评论，具体PC目标/补丁版本未确证 | 弱侧协防、无球紧贴与轮转问题；暂停Gameplan有说明但某些设置效果受游戏bug/补丁影响 | ORIGINAL_EDITORIAL_GAMEPLAY_CRITIQUE；主观分析+案例，不当作所有游戏版本某按钮无效的定理 |
| **SRC-0034** | [OS：NBA on TNT 2k22 Realistic Game Play，第1页与#12–14](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/918002-nba-on-tnt-2k22-realistic-game-play-for-me)，2021-10-11至20 | 作者明确 **Xbox One + Xbox Series X**；Player/Gameplan相关，主机本世代类比适用，**非PC实测** | 玩家文字说明Gameplan→Defensive Settings、Pressure、Screen、Hedge、Stay Attached、Post、Double Team；#12指出Pressure合法词是Gap/Moderate/Tight/Smother而非Go Over，#14原作者承认修正 | CURRENT_GEN_XBOX_ONE_TEXT_ANALOGUE；文中具体值是个人设定，非官方最优推荐；页面内标题Image未用作菜单画面认证 |
| **SRC-0035** | [Reddit：Best playbooks?](https://www.reddit.com/r/NBA2k/comments/r6yxow/best_playbooks/)，2021-12-02 | NBA2K22 **MyNBA次世代**帖子标记MyNBA；非PC MyLEAGUE | 一名用户因达拉斯锋线使用缺适合其角色的战术，在Book加入Cutter、Mid、3PT后反馈球队进攻更顺 | COMMUNITY_NEXT_GEN_EXPERIENCE；不能当作通用必胜配方 |
| **SRC-0036** | [OS：Questions regarding coach settings](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/862337-questions-regarding-%E2%80%98coach-settings%E2%80%99)（2018-09-10 #1–3）及[ACE Effectiveness](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/903464-ace-effectiveness)（2020-11-22 #1–8） | NBA2K19/21时代（不同作者与平台），非2K22 PC直接证明 | 玩家对于ACE/Auto Playcalling/临场默认Freelance是否自动覆盖、是否重复调用存在分歧；某人认为开ACE会在暂停后重排，另一人称ACE有助动态变化 | COMMUNITY_OLDER_VERSION_CONFLICTS；不可把旧菜单具体开关直接搬到本机 |
| **SRC-0037** | [OS：Is ACE engine Team or Coach Specific?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/814745-is-ace-engine-team-or-coach-specific)，2016-09-22 | 2K17前后；论坛保存开发者介绍/引文，非2K22官方游戏菜单 | 说明ACE设计意图包括不同阵容、对手与关键时间变化、临场动态攻击策略；“归教练还是队伍所有”原帖本身属于玩家争论 | OLDER_SERIES_DEVELOPER_TEXT_REPRODUCED；不证明2K22 PC当前运行频率/覆盖规则 |
| **SRC-0038** | [NBA2KW/HoopsGamers：2K22 Controls Guide](https://hoopsgamers.com/nba-2k22-controls-shooting-dribbling-dunking-defense-rebound-offense-guide-xbox-1-x-ps5-ps4)，2021-09-10 | 2K22 **PS4/PS5/Xbox One/Series**操作表，非PC键盘映射 | 正常比赛有On the Fly Coaching(D-pad)、Call Play(L1/LB)、防守换人、协防/包夹等手动操作 | SAME_GAME_CONSOLE_CONTROL_GUIDE；不证明GM网页能向CPU强制实时调用 |
| **SRC-0039** | [OS：NBA2K22 The Eccentric Edition Realistic NG Slider Set](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917100-nba-2k22-the-eccentric-edition-realistic-ng-slider-set)，EccentricMeat首帖2021-09-15，后续版本于12月更新 | 2K22 **次世代**个人Slider/Coach Settings，非PC MyLEAGUE | 玩家公开将PlayVision=All Plays、PlayVision Display=Full、Offense Playcalling=Auto用于观察更活跃的进攻跑位 | COMMUNITY_NEXT_GEN_USER_SETTINGS；不能把个人值域推荐当PC22默认/实战CPU自动比赛认证 |

### 本轮的内容与图源审核纪律

- 已分别打开2K官方新闻、OS原帖、OS编辑文章、HoopsGamers控制说明和Reddit的MyNBA用户回帖；Coach2K关于Isolation/P&R/Fade/Post/Cutter的旧版术语索引已被本项目12类文档引用，**当前直接URL抓取返回404**，本轮不新增编号，也不把搜索引擎摘要说成完整网页正文。
- [SRC-0034] 的作者初稿存在“Pressure=Go Over”错误，后续回帖当面改正：这是为什么按字段登记enum，比复制网红一键设置更重要。
- 原版PC22 Coach/ACE/Freelance的完整操作截图仍未取得；当前项目既有原生字典与用户游戏经验单列“项目事实”，不靠主机截图倒证。外部图像未获再分发许可，不复制到GitHub。

## DEV29 R02-B — ACE/Series/Freelance冲突、Center防守语义、PC CPU-vs-CPU及角色视角（2026-10-21）

本轮优先一手有情境的玩家操作报告；**不以同年代=同平台、或文章里有Image就等于已逐像素核对菜单**。只登记具体推进已知问题的来源，不重复R02-A范围。

| ID | 原始网页 / 作者定位 | 版本、模式、证据事实 | 不可外推的界限 |
|---|---|---|---|
| **SRC-0040** | [Operation Sports：Defensive Settings Not Staying On Custom](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/920049-defensive-settings-not-staying-on-custom)，2022-01-02/03 #1–4（smuhead/vetmin/jeebs9） | **2K22时期**：用户报告Team Focus/Defensive Settings比赛中Custom反复变Automatic，即使ACE=Off仍无法保留；其他用户首先建议ACE Off或Offense Only | `COMMUNITY_USER_REPORT_SEARCH_INDEXED_FULL_PAGE_REDIRECT_FAILED`，原网页直接打开因重定向循环失败，引用只按带原帖内容的搜索索引；没有平台/模式认证，不能说所有PC22 ACE失效 |
| **SRC-0041** | [Operation Sports：Adaptive Coaching Engine](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/921133-adaptive-coaching-engine)，2022-02-24—03-05 #1–3（DJ81） | 同版玩家提出ACE Off可能让手控设置保留，却需人工比赛中改Tempo/篮板；并主张“ACE only affects the user” | `COMMUNITY_FIRST_HAND`：对真人user情境的主张，不是NBA2K22 PC CPU-vs-CPU源代码事实，与SRC-0040分歧并列 |
| **SRC-0042** | [Operation Sports：Are series not working?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917118-are-series-not-working)，2021-09-16 #1（Smirkin Dirk） | 2K22发售早期，玩家称无论Gameplan选Series还是比赛暂停再选，场上似乎都回退Freelance | `COMMUNITY_2K22_XBX_SELF_REPORTED`，作者签名指XBX，实际模式/PC未证；只报告现象，不代表所有Series失效 |
| **SRC-0043** | [Reddit r/MyTeam：Freelance sets EASY FIX in MyTeam](https://www.reddit.com/r/MyTeam/comments/q36nsh)，2021-10-07，原作者wiiiiigs | **NBA2K22 Xbox Series X/S MyTEAM**：先暂停Offensive Settings选set，再场上方向键Gameplan→Run Freelance，然后Freelance→具体set；由此区分“选中配置”和“主动触发” | `COMMUNITY_CURRENT_2K22_NEXTGEN_MYTEAM`，不等于PC本世代MyLEAGUE的菜单或自动CPU调用 |
| **SRC-0044** | [OS：On ball screen (center), Hedge (center) 第2页 #18–23](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/806956-on-ball-screen-center-hedge-center/page2)，2016-08（harryl/Nevertheles109等） | **2K16旧系列**：普通On-Ball Screen控制盯持球人的防守者，Hedge是掩护者防守人；Center后缀可能表示有中锋参与的掩护，讨论关于“被设置的对手持球者”和“己方协防中锋”身份的区别 | `KNOWN_IN_SERIES_PLAYER_EXPLANATION`，不是NBA2K22 PC Center字段实际触发、enum、对位特殊情况和覆盖关系认证 |
| **SRC-0045** | [OS：Defensive Settings discussion 第2页，2018-11 #22–27](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/865843-defensive-settings-discussion/page2) | **NBA2K19时期经验**：球员报告Tag On Roll在Gameplan消失但SimCast Defensive Settings仍见，明说未测是否有效；另外讨论Hedge(Center)/Pre-Rotate与具体掩护/帮助 | `OLDER_SERIES_CONFLICTING_MENU_VISIBILITY`，不能说NBA2K22 PC同样隐藏或一定生效 |
| **SRC-0046** | [OS NBA 2K PC Forum：cdcool NBA 2K22 CPU vs CPU MyLeague Sliders](https://forums.operationsports.com/forums/forum/basketball/nba-2k-pc-forum/918715-cdcool-nba-2k22-cpu-vs-cpu-myleague-sliders)，2021-11-03 #1（2022-01更新） | 明确为**NBA2K22 PC MyLEAGUE，全联盟控制、每场看3D CPU-vs-CPU且不快模拟**；玩家公开自定义12分钟、Game Speed及打法滑块 | `PC22_COMMUNITY_DIRECT_MODE_TEXT`，可以确认有该研究条件，**不能认证Coach UI/ACE效果**；作者滑块数值非项目默认/非推荐 |
| **SRC-0047** | [OS：Next-Gen Freelance / Series / Offensive and Defensive Gameplanning Questions](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/907707-next-gen-freelance-series-offensive-and-defensive-gameplanning-questions)，2021-03-17 #1–2（skeenz/El_Tercero） | **NBA2K21次世代MyNBA**：玩家将Freelance、Series、暂停策略和Gameplan分成不同控制入口，抱怨赛前选Freelance不持久及改用Timeout的经验 | `OLDER_NEXTGEN_PLATFORM_UI_REPORT`，不证明本项目PC22本世代有同一菜单/BUG，不算目标版视频像素认证 |

**外部视觉审核结果**：寻找PC22 MyLEAGUE无模组Coach/ACE/Defense/Book、2D战术板与视频精确帧，未找到足以同时辨认平台、原版、模式与完整菜单/字段的材料；**本轮新增`PC22_UI_CONFIRMED=0`，不等于功能不存在**。有标题的YouTube视频、OS文章“Image”、Xbox MyTEAM文字教程均不冒充PC22像素认证。未复制/公开再分发第三方截图。

**R02-B主要新研究值**：把ACE是否重置、Series是否被调用、Center个人防守的“谁掩护/谁防”角色视角、SimCast旧版字段可见性和本世代PC CPU-vs-CPU玩法分别登记，构建可证伪的对象/时点/角色观测合同，而非“建议统一设置某个数值”。

## DEV29 R02-C — 原版PC22菜单的有界补证与V3研究结案（2026-10-21）

本轮只登记**1项确有新增信息的同版MyLEAGUE玩家经历**。没有为了凑来源数量登记Steam封面、重构UI Mod、2K20/21旧截图或没有目标菜单画面的攻略。

| ID | 原始链接与准确位置 | 游戏/平台/模式 | 已核对的具体新增事实 | 不能认证的内容 |
|---|---|---|---|---|
| **SRC-0048** | [Reddit r/NBA2k — Saving coaching strategy](https://www.reddit.com/r/NBA2k/comments/qg2amb)，主帖2021-10-26；2021-12-19原提问者追问后回覆 | 发帖时间属于NBA2K22发行季，原帖写MyLEAGUE；**平台不明**，没有可逐像素审查的页面 | 提问者起初不知道如何持续保存默认Freelance，每场似乎要重新设置；后续明确表示，在比赛中修改后会按**该球队**自动保存。这与另一玩家报告Series/Freelance被覆盖并不直接矛盾——两者可能涉及不同入口、游戏阶段或其他条件 | `COMMUNITY_2K22_ERA_MYLEAGUE_REPORTED_PERSISTENCE`；不能升级`PC22_UI_CONFIRMED`、`PC22_NATIVE_READ_VERIFIED`或跨赛季确定保存；不能当作ACE/CPU vs CPU原生覆盖公式 |

### R02-C检索排除和版本警告

- 定向核查NBA2K22 PC原版MyLEAGUE `Coach Gameplan / ACE / Offensive Settings / Defensive Settings / Edit Playbook / Freelance / 2D Play Diagram`，包含Steam社区截图、公开视频标题、图片检索、PS4/Xbox One同代图文。返回的2K22 MyNBA Conditional Coaching官方说明[既有SRC-0026](https://www.operationsports.com/nba-2k22-mynba-details-revealed-mystaff-staff-carousel-prep-hub-attributes-badges-more/)明确限PS5/Xbox Series，不能冒充PC22“赛中规则代理”。
- [Magic Game World：2K22 MyLEAGUE固定轮换分钟文章](https://www.magicgameworld.com/how-to-adjust-player-minutes-in-season-mode-in-nba-2k22-myleague/)显示发表2021-04-30，**在NBA2K22 2021-09-10发售前**；未提供真实PC22游戏菜单/实验，声称固定分钟能持续整季与项目用户已观察AI重新分配分钟不符。**不采信，不分配SRC-####**。
- [NBA2K22 PC SteamDB截图页](https://steamdb.info/app/1644960/screenshots/)与[Steam Community截图页](https://steamcommunity.com/app/1644960/screenshots/)可确认目标游戏容器，但主要是平台商店图像/非可识别MyLEAGUE菜单；不可把外层`View Stats`当游戏内Coach/Stats界面。
- [2K22官方MyNBA Conditional Coaching](https://www.operationsports.com/nba-2k22-mynba-details-revealed-mystaff-staff-carousel-prep-hub-attributes-badges-more/)报告让玩家在模拟时设置条件指令，这是**2K22次世代官方机制**而不是PC MyLEAGUE证据；R03可参考其中训练内容但仍不得迁移为本机字段。
- 其它版本MyLEAGUE和主机MyTEAM的菜单文章已在SRC-0030..0047登记。**本轮没有新增符合NBA2K22 + PC + 无模组 + 离线MyLEAGUE + 目标菜单字段可读五条件的画面，`NEW_PC22_UI_CONFIRMED=0`**。不意味着功能缺失；不虚构截图、字段枚举或视频时间戳。

**结案**：`R02_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`。已编写教练、GM、球员和媒体的`OBSERVABLE/ACTIONABLE/MECHANISM/OWNER`研究原料与权限矩阵于[K04 §19–21](guides/K04_COACH_AND_PLAYS.md)；PC22 UI和赛中引擎覆盖待日后定向只读证据。**下一轮R03训练、健康、自然成长；不重启R02网络搜证，不启动DEV28/Codex/游戏改动。**
