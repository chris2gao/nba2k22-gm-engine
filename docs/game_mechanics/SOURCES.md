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

## DEV29 R03-A — 训练、健康与自然成长：官方/玩家一手来源（2026-10-21）

**研究目标=为未来角色列出可观察事实、合法选择及反馈，而非提供万能高强度训练方案。** 与已有仓库PC22原生字段区别：这些外部文献解释历史机制，但**不证明本期训练字段已经有动态观测值**。下列SRC-0049..0059除注明的个别网页只可检索到正文外，均已从真实页面或可核对的原文检索定位，非单纯题名。

| ID | 原文、链接和原始日期 | 版本 / 平台 / 模式 | 真正证实或报告的内容 | 证据边界 |
|---|---|---|---|---|
| **SRC-0049** | [2K Newsroom官方新闻：2K22 Adds New Features to MyNBA](https://newsroom.2k.com/news/nbar-2k22-adds-new-features-to-mynba-for-playstation-5-and-xbox-series-xs-consoles)，2021-09-08 | **NBA2K22 PS5/Xbox Series MyNBA，仅次世代** | 新增MySTAFF、Prep Hub、团队及个人训练改进、教练条件指挥。官方附Prep Hub/Individual Training Focus/Training Schedule等具名原图入口 | OFFICIAL_NEXT_GEN_ONLY，**绝不能说PC22 MyLEAGUE原生有Prep Hub**；游戏图片版权官方 |
| **SRC-0050** | [NBA2KW：NBA 2K22 MyNBA Full Details（官方Courtside Report正文转载）](https://nba2kw.com/nba-2k22-mynba-full-details-mystaff-training-pre-built-teams-more)，2021-09 | **2K22 PS5/Xbox Series MyNBA**；同份开发者文字另在[Reddit开发博客转录](https://www.reddit.com/r/NBA2k/comments/pkc7ii) | Prep Hub显球队/对手/熟练度；团队训练未来3周的训练种类、Intensity/Fatigue/Injury Risk、Game Fitness、伤员与Load Management；玩家可自主采取较低负荷练习；个人Focus影响希望发展的方向 | OFFICIAL_DEV_TEXT_REPRODUCED_NEXTGEN；原版PC旧世代所有上述菜单和玩家“自动降训练”仍UNKNOWN |
| **SRC-0051** | [OS玩家：2k22 - MyNBA - Training schedule](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/916991-2k22-mynba-training-schedule)，2021-09-13—19，coachmac75 #1/#6/#7 | 2K22 **MyNBA次世代**，作者页面签名2K22 MyNBA Pistons | 真实玩家问负荷/背靠背、练习日和Game Day冲突；推进日程后练习顺序错乱，称逐天修正是一种 workaround；帖附2段YouTube视频 | SAME_YEAR_NEXT_GEN_FIRST_HAND_TEXT；**视频未本轮逐帧检验，不虚构时间戳**，不能说PC22也有该BUG |
| **SRC-0052** | [OS开发人员Leftos：Regarding Training Intensity in MyGM and Promises](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/697404-regarding-training-intensity-in-mygm-and-promises)，2014-10-21，#1 Visual Concepts AI engineer Leftos | **NBA2K15年代MyGM**，开发人员本人解释 | `Overall Workload`由训练强度+比赛/休息天/实际出场+Work Ethic共同作用，原帖称承诺与投诉按滚动两周而不是单一强度判断，游戏日视同高强度训练日 | DEVELOPER_OLDER_VERSION_FIRST_HAND；对现代多Agent有价值的机制思路，但**两周公式/强度换算不是PC22已证规则** |
| **SRC-0053** | [OS：Schnaidt1 2K22 Sliders第31页的PS4球员帖子](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917177-schnaidt1-s-nba-2k22-next-gen-mynba-gameplay-sliders-settings/page31)，tetoleetd约2022-02-01 | **NBA2K22 PS4本世代 MyLEAGUE，ATD roster修改过进步/退化滑块**；标题含Next Gen但作者明确写PS4，需以回帖为准 | 玩家表示逐人设训练方向，多数强度High/Very High，模拟首季之后未见预期年轻人成长 | CURRENT_GEN_PS4_SELF_REPORTED_CASE_SEARCH_EXCERPT；精确回帖页面带postcount参数直接打开时403，已从可用搜索摘要阅读；不可反推训练无效，样本含多混杂设置 |
| **SRC-0054** | [OS：Advice for player development for MYGM/MyLeague](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/706081-advice-for-player-development-for-mygm-myleague)，2014-11-07，玩家回帖 | **NBA2K15时期MyGM/MyLEAGUE** | 玩家指出专练单一投篮技能时其他能力可能后退、OVR与单技能进步背离，强度高可能导致赛季疲劳加快，示范按原型培养 | OLDER_COMMUNITY_CASE；此个案不是2K22可改逐属性训练比例证据 |
| **SRC-0055** | [OS：Help with setting training in myleague](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/772729-help-with-setting-training-in-myleague)，2015-08-04起 | **NBA2K16左右旧MyLEAGUE**，非目标版 | 玩家在“injury rehab / player type / intensity”之间切换；另提问老将、中生代、新秀如何选强度、过度训练是否带伤病反效果 | OLDER_PLAYER_EXPERIENCE；并非证明PC22 InjuryRecovery准确伤愈速度 |
| **SRC-0056** | [OS：How's your MyNBA Going — 2K22 Edition](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/916895-how-s-your-mynba-going-2k22-edition)，2021-09-12 #11–15，asap_lenoo、lakerhater等 | 同年**NBA2K22 MyNBA次世代**训练设置玩家讨论 | 有玩家指出与2K21旧版分配单属性训练比例不同，2K22 MyNBA仅可选训练presets，不能逐属性微调 | COMMUNITY_NEXT_GEN_MENU_REPORT；不能据此删PC22本世代任何已证训练选项 |
| **SRC-0057** | [OS：Is 2K23 MyNBA any better than 2K22?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/936550-is-2k23-mynba-non-eras-version-any-better-than-2k22)，2023-04-02 #3 dwayne12345 | **2K23次世代玩家对2K22 MyNBA日程缺陷回顾** | 该用户说2K22训练日程推进几天后排列错乱，在2K23已修复部分；与SRC-0051同期玩家叙述呼应 | LATER_COMMUNITY_RETROSPECTIVE；版本补丁不明，不能断言PC22有同BUG |
| **SRC-0058** | [OS：What do the assistant coach and trainer affect again?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/787529-what-do-the-assistant-coach-and-trainer-affect-again)，2015-11-26 #1–4 | 旧MyLEAGUE员工培训讨论（非2K22） | 玩家对训练师究竟影响预防/康复/耐久或休赛期训练营数量存在不一致理解，回帖一人称A-训练师换C-后训练营名额由7变4 | OLDER_COMMUNITY_CONFLICTING；不能给PC22 Trainer属性固定增长加成和训练营资格公式 |
| **SRC-0059** | [Reddit r/NBA2k：Understanding MyLeague Player Progression](https://www.reddit.com/r/NBA2k/comments/vvy2gu)，2022-07-10 | NBA2K22发行年度附近的MyLEAGUE社区问答，**具体玩家游戏版本和平台未自证** | 玩家提问年轻球员如何自然涨分及徽章，其他人讨论Potential/Boom-Bust/AVG及教练Mentor类徽章影响；意见非独立实验 | COMMUNITY_VERSION_UNCONFIRMED / LOWER_CONFIDENCE；只能用于标记R04需核对哪些字段，**不成为直接修改Potential或徽章的依据** |

### 本轮来源与工程验证补充

**重要项目内证据链**：`config/state_io_native/training.json`登记6个团队训练布局、5个个人flags、9种通用player_type、可见强度0–5以及fatigue/history/mentor结构候选；`src/gm_state_io/registry.py`精确注册`training.team.{home_intensity,away_intensity,automate_intensity,rest_before_b2b,rest_after_b2b,injury_recovery}`和`training.player.{position,player_type,intensity,injury_recovery,is_intensity_overriden}`。`docs/development_reviews/DEV14_TO_M3_HANDOFF.md`交付说明该11项已进通用Native state I/O，但同批当前疲劳/伤病/导师进度不等于已经可靠采到；无玩家新批准本轮**没有采集、运行或修改**。更旧`docs/research/NBA2K22_MYLEAGUE_GM_CAPABILITY_GAP_AND_MONTHLY_TRAINING_V1.md`“尚无训练接口”的描述属于当时报告，不应取代更新后Registry事实。

**阴性来源审计**：搜索中大量“Madden 22 progressive fatigue”的结果属于NFL游戏，不是NBA2K22；MC/The W使用徽章点数的玩法也**不等于MyLEAGUE自然徽章发展**。2K22次世代官方图片只登记为`NEXT_GEN_VISUAL_ONLY`，未经许可不上传第三方媒体原图。R03-A交付中文K06§0–6和未认证范围，下一轮**R03-B伤病/实时疲劳/恢复/导师与角色选择**。

## DEV29 R03-B/C — 健康事件、疲劳、导师与训练师专项证据（2026-10-21）

**来源编号 SRC-0060..0071**；下列研究优先基于2K22同年玩家及官方开发文本，次世代机制允许复用作“角色选择和风险”资料，具体PC22可读/可写字段仍单独定级。每条明确内容，不把讨论者的slider偏好当科学公式。

| 来源编号 | 可复核原始链接、年份与作者 | 真实支持的论点 | 适用范围和不能推出的结论 |
|---|---|---|---|
| SRC-0060 | [Operation Sports: MyLeague Injury Sliders](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/918980-myleague-injury-sliders), 2021-11-14 起，swanklax/Cesco/titanswin53 | 同版玩家称手打100+场无伤而Sim有伤；另玩家表示MyNBA首场Luka有真实受伤动画，反驳“3D永不伤”；讨论伤病sliders调高与不同游戏模式的反应 | NBA2K22 MYLEAGUE/MYNBA_COMMUNITY_CONFLICTING；部分PS5次世代，非PC22实机伤病概率公式 |
| SRC-0061 | [OS: MyLeague Why are there no injuries](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/921266-myleague-why-are-there-no-injuries), 2022-03-06 至04-12，Hockeytown954/vetmin/MattyIce 等 | 49场无受伤、模拟伤病多；有人见鼻骨伤，有人尝试降低Durability得到伤病，反例即使滑块开满仍未受伤 | NBA2K22同年未经控制的**冲突个案**。不能建议改球员Durability或强行生成随机伤病来补“真实性” |
| SRC-0062 | [RealSport101: NBA 2K22 Sliders](https://realsport101.com/article/nba-2k22-sliders-realistic-settings-gameplay-options-optimized-experience-offense-defense-movement-attributes), 2021/后更新 | 2K22攻略在MyLEAGUE/MyNBA环境里列出Fatigue Rate、Player Recovery Rate、CPU Injury Frequency、模式设置等候选世界层参数 | THIRD_PARTY_SERIES_SLIDER_GUIDE。编辑推荐数值是主观；平台、菜单分组和GM可调整权限须独立PC22验证，不按说明直接写World |
| SRC-0063 | [OS: MyNBA Injury Duration](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/926689-mynba-injury-duration), 2022-09-16，ripken823/dwayne12345/coachmac75 等 | 2K23 MyNBA玩家说实际康复快于最初伤期；dwayne12345明确声称2K22也有同类问题；讨论伤期/世界Duration与场次长度的混杂 | 2K23直接经验+2K22**回忆**，不可认PC22恢复天数计算或断言bug必现 |
| SRC-0064 | [2K官方MyNBA开发博客转载（OS）](https://www.operationsports.com/nba-2k22-mynba-details-revealed-mystaff-staff-carousel-prep-hub-attributes-badges-more/), 2021-09-08, Sports Medicine章 | 官方明确2K22**次世代**Team Doctor、Strength Trainer、Stamina Trainer、Sports Psych、Sports Scientist、Physio、Sleep Doctor的各自医学/体能职责 | OFFICIAL_NEXTGEN_MY_NBA，**机制与角色分工可复用**；不是PC22能聘七岗或Trainer加成公式 |
| SRC-0065 | [OS: Can MyLeague Players Earn New Badges?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/908209-can-myleague-players-earn-new-badges), 2021-04-01..05，canes21 #3/#5/#7 | 玩家称离线MyLeague训练页有Mentor，Mentor页可见目标徽章进度，并可比较前后卡片与赛季自然变化 | NBA2K21时代OFFLINE_MYLEAGUE 一手社区，不能假装PC22当前mentor进度已采 |
| SRC-0066 | [OS: Mentor System](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/904106-mentor-system), 2020-12-05..2022-01 | 2K21 current gen有人报告老将导师确实向年轻人传过徽章，另有人质疑此类机制过去版本失效 | SAME_SERIES_CURRENT_GEN_PLAYER_EXPERIENCE，不证明NBA2K22每个师徒都有效 |
| SRC-0067 | [Reddit r/NBA2k: MyLeague Player Mentorship](https://www.reddit.com/r/NBA2k/comments/rm6rr9), 2021-12-22 | 同2K22发售期玩家询问把恩比德Post Lockdown传给斯图尔特是否会扣掉导师徽章，回帖认为不会 | COMMUNITY_2K22_ERA_ANSWER；平台与真实通过结果未证，不是“必定不会消耗导师等级”的官方定律 |
| SRC-0068 | [Reddit: MyLeague Player Mentorship Broken](https://www.reddit.com/r/NBA2k/comments/s88jzz), 2022-01-20..04-08 | NBA2K22 MyLeague玩家报告为特定学员指定某导师时反复崩溃；其他人表示复现，有人说在更改前单独保存 | COMMUNITY_2K22_FIRST_HAND_FAILURE；非当前PC22定向Crash确认，亦不意味着整个系统失效 |
| SRC-0069 | [学术研究：Game Load, Fatigue, and Injury Risk in NBA](https://pmc.ncbi.nlm.nih.gov/articles/PMC6107769/), 2018 | 真实NBA观察研究发现球员个体之间负荷/疲劳与伤病风险关系存在差异，给出科学的“不同球员风险可能不同”背景 | REAL_NBA_RESEARCH_ONLY：不是游戏内部伤病概率，也不产生替游戏设置健康阈值的合法权力 |
| SRC-0070 | [Reddit: 2k22 MyLeague Online](https://www.reddit.com/r/NBA2k/comments/pmg3z0), 2021-09-11..2022-02-24 | 在线MyLeague用户先认为没有Mentoring，后来有人指出可在Overview里滚动并看到“Change Mentor” | NBA2K22 ONLINE_LEAGUE_MENU_DISCUSSION，不能从线上入口推断离线PC具体按钮 |
| SRC-0071 | [OS: Has Anyone Figured Out How Training/Progression Work?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/899504-has-anyone-figured-out-how-training-progression-work), 2020-09-03 | 玩家称模拟多个赛季、很高训练强度、A级Trainer与冠军球队，却见部分球员OVR下降；交易到其它队后个别球员又恢复 | NBA2K20/21附近一手社区报告；混杂年限、年龄、世界滑块、潜力、位置与状态，不说明PC22强度→属性数学式 |

**研究中明确否决的不可靠迁移**：
- 有人把“Trainer A”同次世代Sports Scientist、Physio、Sleep Doctor几项效果相加，缺PC本世代原生依据，不采用。
- 只看历史`progressive_fatigue_history`已存在指针就宣称可以获取球员当前体力和伤病，缺实机解码、时序与来源批次，不采用。
- 依据同年手动比赛与Sim伤病争论就修改球员Durability、手动添加伤情以制造事故，**不在DEV29研究授权内**。
- 依别的2K游戏/MyCAREER/移动版徽章成长说明将导师`badge_slot.progression`写成MyLEAGUE的已确认执行接口，不采用。

**R03-C结论**：中文K06增补§§9–15，研究范围覆盖；PC当前身体状态/医学事件实时数据仍有缺口。独立审核见`reviews/R03_COMPLETENESS_AUDIT_V1.md`，R04需等玩家完成审核。

## DEV29 R04-A — 人物身份、完整已注册属性、耐久、徽章与自然成长（2026-10-21）

下列**SRC-0072..0082**用于描述NBA2K22个人卡/Vitals、属性分组、Durability、Peak与Badge。**第三方球员站的2021年导出数值不代表本项目当前2021–22存档真实值**；2K22多平台社区编辑数据也不能替换原版，徽章解锁攻略可能特指MyPLAYER。

| ID | 精确来源 / 作者 / 日期 | 本轮用于什么真实研究事实 | 平台、版本及局限 |
|---|---|---|---|
| **SRC-0072** | [Operation Sports编辑报道：NBA 2K22 Attention to Detail Roster From CelticLG and Crew](https://www.operationsports.com/nba-2k22-attention-to-detail-roster-from-celticlg-and-crew/)，Chase Becotte，**2021-12-16** | 2K22球员编辑维度包括Tendencies、Attributes、Badges、Durability、Personality、Play Types、Peak Start/End、Potential、Play For Win/Financial Security/Loyalty、合同、号码、身高与容貌等 | EDITORIAL_REPORT_OF_CUSTOM_ROSTER；当时报道明确PC版本still work in progress，**不能把ATD编辑值当原版PC默认** |
| **SRC-0073** | [OS官方ATD 2K22原始讨论，第11页#151等](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/916767-nba-2k22-attention-to-detail-roster-ps4-ps5-xb1-xbsx-pc-switch/page11)，CelticLG及后续回复，2021-11-27至29 | 作者同年代说明其项目覆盖属性/倾向/Gameplay及Personality Badges/各部位Durability，社区回复声称约60属性、120倾向、80Gameplay和20Personality、25Durability。源码/菜单单项清单并未在帖子完整逐名提供 | PRIMARY_2K22_ROSTER_CREATOR_CLAIM；**这些数量是制作者自述，不是当前项目本机Field Registry的总数证明**，不得以25去猜其余身体字段 |
| **SRC-0074** | [2kAuction同版球员资料：Marques Johnson](https://2kauction.com/mynba/2k22/players/marques-johnson)，其页面称2K22安装快照/2021年数据 | 对一个真实样例逐栏提供Attributes/Badges/Tendencies/Animations/Bio/Development/Contract/Injuries标签，Bio含生日、身高、臂展、体重、位置/号码、选秀/年资，Development含Peak、最低/最高Potential、Boom/Average/Bust与曲线，显示16个具名Durability | THIRD_PARTY_GAME_SNAPSHOT_INDEX；**不是用户当前PC save的官方直接内存/菜单逐像素认证**，图片或站方抽取字段尚需独立核对 |
| **SRC-0075** | [2kAuction NBA2K22人物：Joel Embiid（Offseason NBA）](https://2kauction.com/mynba/2k22/players/joel-embiid?roster=offseason_nba)，2021-09基线 | 再次证实导出站分离Bio、Draft、Development、Motivations(Loyalty/Playing for a winner/Financial security)、4 PlayTypes及合同、2个伤病slot等候选结构，人物出生与归属可独立存在 | THIRD_PARTY_2K22_EXPORT；`Motivations`当前项目原生raw偏移未认证，R04-C后续调查原生效果；伤病duration不可与当前剩余天数混淆 |
| **SRC-0076** | [2kAuction NBA2K22人物：Michael Porter Jr.（Offseason）](https://2kauction.com/mynba/2k22/players/michael-porter-jr?roster=offseason_nba)，2021版数据 | 相同球员不同身体部位耐久值可以不同，Back/Misc/Hip与其它部位独立字段，构成“部位耐久≠实时伤停”示例 | THIRD_PARTY_2K22_EXPORT；任何展示的单人数字都不是当前用户存档数据 |
| **SRC-0077** | [OS：What causes Player Progression in MyLeague?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/908145-what-causes-player-progression-in-myleague)，2021-03-30至04-01，jk31/El_Tercero/marshdaddy等 | 玩家描述Edit Player→Vitals里Peak Start/End的观察位置，讨论Peak之前成长/之后退化及Potential/Progression Slider对成长的作用，**互有不同解释**；其中用户怀疑Boom/Bust属于Next Gen | NBA2K21时期MyLEAGUE系列级玩家一手经验，不能推成PC22精确年龄衰退函数或Boom/Bust有本世代原生raw |
| **SRC-0078** | [OS：JB's 2K22 (PS5) Fictional Draft Classes，第6页#78–80](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/916715-jb-s-2k22-ps5-fictional-draft-classes/page6)，2022-01-29/31 | 2K22 **PS5 MyNBA**玩家明确举例Vitals中Boom/Bust机会、最低/最高潜力，以及Peak Start/End的角色；个人预测未经独立多档概率试验 | SAME_GAME_NEXT_GEN_FRANCHISE_MECHANISM；PC22本世代是否同菜单/编码，尚需认证 |
| **SRC-0079** | [NBA2KW：NBA 2K22 All-in-One Complete Badges Guide](https://nba2kw.com/nba-2k22-all-in-one-complete-badges-guide-breakdown-analysis)，2021-08-31 | 2K22游戏徽章分Finishing、Shooting、Playmaking、Defense/Rebounding四大类，常见Bronze/Silver/Gold/HOF等级，游戏技术技能辅助玩法 | COMMUNITY_SAME_GAME_MYPLAYER_GUIDE；**徽章点数获取/身高解锁条件不等于MyLEAGUE历史球员自然增长与导师规则** |
| **SRC-0080** | [OS：NBA 2K22 All Player Ratings 第2页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/916765-nba-2k22-all-player-ratings/page2)，2021-09-11作者Real2KInsider及2022年内容 | 玩家同版公开列Jordan Clarkson等球员Offense/Defense/Athleticism/Mental评分与Finishing/Shooting/Playmaking/Defense徽章；后续样例将Alpha Dog、Finance Savvy、Media Ringmaster、Expressive、Extremely Confident等列为Personality | ORIGINAL_2021_2K22_PLAYER_EDIT_DISCUSSION；其中任何建议的新评分是**个人自制R2K编辑值**，不属于默认真实数据；原生徽章功能未一一测试 |
| **SRC-0081** | [NBA2K Wiki：Personality（跨版本术语）](https://nba2k.fandom.com/wiki/Personality)，当前检索可见旧系列人格徽章解释 | Alpha Dog、Low Ego、Friendly、Legendary/High Work Ethic、Unpredictable、Pat My Back、Keep It Real、Hardened、Championship DNA等可作为跨代名录候选 | WIKI_KNOWN_IN_SERIES; **网页直接展开可能受防爬限制，且历史列表不是NBA2K22 PC逐个徽章原生列表**；不把旧MyCareer阈值搬进MyLEAGUE |
| **SRC-0082** | [2K Film Room：NBA 2K22 Badge Cheat Sheet](https://2kfilmroom.com/cheat-sheets/2k22)，2KFR社区独立表 | 页面可读取完整 **80项Gameplay Badges名称**，Finishing20、Defense&Rebounding20、Playmaking20、Shooting20，可作为检索标签池；已登记于[PLAYER_BADGES_R04_A_REFERENCE.json](catalogs/PLAYER_BADGES_R04_A_REFERENCE.json) | FANSITE_2K22_MYPLAYER_BADGE_REQUIREMENTS；**列出的属性阈值及身高门槛属构建玩法，未证明本机MyLEAGUE当前各球员Badge真实native ID、自然升级公式或执行接口** |

### 本轮仓库内可证据定位（非网页SRC项）

- `config/memory_field_profile.json` 的 `fields.PLAYER` 共**72项已经命名字段：55项attributes（39个非耐久评分 +16个具体Durability），17个合同字段**，只是本项目原生已注册子集。不要误写成2K22游戏完整属性总数；具体源偏移放进矩阵，但游戏里对人的自然变化仍由原生决定。
- `src/source_extensions.py` 的 `player_details()` 返回 `birth_date`、按game_date推算`age`、`current_team_id`、`contract_team_id`、`attributes/contract`，且明确`overall_rating=None`/`overall_source=NOT_OBSERVED`；不是已经采到全部Vitals或人物Career荣誉。
- `config/state_io_native/player.json`目前含4 PlayTypes的0..15编码与48个命名Tendency offsets；Registry定义0x458..0x4BA共99字节，**51未知raw**不得给模型解释成确定倾向。此处详细内容留R04-B。
- **严格保护**：DEV15批准的公开数据库Potential=1是`MASKED_BY_GM_WORLD_RULE`，不是观察到的真实潜力；不得公开真实Potential/泄给GM或媒体；特殊`Intangibles 0x440`仅被批准用于特定经人工审批的轮换偏置，不能衍生“任意评分修改”。
- 同版2K22球员导出站显示16个具名Durability，ATD编辑作者自述25个**计数口径未证**；不构造9个不存在的名字/偏移，不把`injury_status`和`durability`合并。

**R04-A范围**：K03/K12§§0–8和两份研究矩阵均属于原料交付，R04-B接全部行为倾向及教练/Book联动，R04-C接合同偏好与人格徽章，R04-D完成角色权利与互动图谱。没有创建任何Agent、启动DEV28/Codex、打开游戏或改存档。

## DEV29 R04-B — 倾向、出手分配、3D/Sim与PlayTypes同版证据（2026-10-21）

本轮新增**SRC-0083..0090**，均只支持其能够证明的行为/界面/来源版本。**重点：2K22同版用户报告Touch与Shot不同作用且彼此冲突；不能选择合自己偏好的那个结论当2K引擎公式。** [R04-B研究目录](catalogs/R04B_TENDENCY_PLAYSTYLE_RESEARCH_V1.json)保存99个原生slot和独立的99个同版归档导出标签；两组**没有经认证的行序/offset映射**。

| ID | 来源和定位 | 内容如何帮助研究 | 等级与边界 |
|---|---|---|---|
| **SRC-0083** | [2kAuction NBA2K22 Anthony Davis · Offseason NBA 2021/09 v91历史存档](https://2kauction.com/mynba/2k22/players/anthony-davis?roster=offseason_nba)；参照[Haliburton 同版页](https://2kauction.com/mynba/2k22/players/tyrese-haliburton?roster=offseason_nba) | 归档人物详细独立标签：`Shot`（含投篮/背身35项）、`Drive / Pass`（含三威胁、左右、连续运球、ISO vs防守等级43项）、`Defense`7项、`Other tendencies`（区域出手）14项，共**99个具名label**。可观察Shot/Tou​​ches/Post, TT/Setups、ISO四级、Play Discipline、防守7类等界面语义；均以第三方导出为研究原料 | **SAME_GAME_THIRD_PARTY_ARCHIVED_ROSTER_HTML**。网页快照值≠本项目当前球员；网页可读条目≠NBA2K22 PC原版滚动截图；**不能据“99”把label逐行对应Registry原生99字节** |
| **SRC-0084** | [Operation Sports：NBA 2K22 Tendencies — A Better Realism for Roster Creators](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/917138-nba-2k22-tendencies-a-better-realism-for-roster-creators)，Sheitan 2021-09-17 #1，Evtnj与Sheitan 2021-11-25 #9–11 | 作者尝试把3D行为倾向按经验频率/分位数分类，认为极端0或99会使人物行动单一；同月用户明确说`Edit Player→Freelance`有`Touches`和`Shot`及下方ISO防守等级。Sheitan后答`Freelance Shot`主要对应**Sim统计**而非3D，不是场上各类具体投篮动作的同义词 | **2K22_2021_COMMUNITY_DIRECT_ROSTER_DISCUSSION**；个人测试、部分作者PSN/Xbox不详，**不是PC原生effect=0的已证公式**；“避免99”是作者名单设计哲学，角色可不服从 |
| **SRC-0085** | [OS：NBA 2K22 Useful Findings](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917203-nba-2k22-useful-findings)，2021-09 #1–7，以及[第10页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/917203-nba-2k22-useful-findings/page10)，2021-10 #136–150 | tcnumba10认为全队降低Touches或主星Shot后3D出手更分散；jimbo3772认为Touches主要用于Freelance、Book/PlayTypes/POE/RunPlays决定叫谁的set；Tynole14报告把Shot调至0仍只给两后卫叫战术。**这是实质互相冲突的同版场上观察** | **COMMUNITY_2K22_FIRST_HAND_CONFLICTING**，同一游戏不同控制模式/角色/战术书/AI设置样本未控制；不得形成“Shot≤80最佳”“Touches都调50”强制规则 |
| **SRC-0086** | [2kAuction 2K22 Trae Young v91历史人物档案](https://2kauction.com/mynba/2k22/players/trae-young?roster=offseason_nba) | 将`Play Initiator=Yes`与4个**有序PlayTypes**分别列出，并有Touches/Shot等偏好；证明**字段概念独立存在于2K22归档人物展示** | THIRD_PARTY_2021_PLAYER_EXPORT；不可据外站Yes/No认定本项目当前人物，也不能反推出cpu固定控球时长 |
| **SRC-0087** | [2kAuction NBA2K22 Jayson Tatum Current NBA](https://2kauction.com/mynba/players/jayson-tatum?game=2k22&roster=current_nba)，2021-09历史导出 | `Play Initiator=No`却仍有4个PlayTypes，其中`Pick & roll wing`、`Isolation`、`Three-point screens`、`Handoff`。与Trae对比证明Initiator概念独立于4槽存在；官网字面“Three-point screens”与本机`3 PT`enum**不认定编码相同** | THIRD_PARTY_2K22_EXPORT，非当前GM名单/原生enum逐项已验 |
| **SRC-0088** | [OS：2K22 MyLeague Settings / Sliders](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917042-2k22-myleague-settings-sliders)，DarthRambo 2021-09-20/21 | 同版MyLEAGUE玩家表示在测试Sim赛季时批量编辑了Foul/3PT/Midrange/Drive Pull-Up等球员倾向，并提供**Sim进球/得分/犯规**的另一组联盟世界滑块；表明原生球员倾向与世界全局权重是**两个对象** | COMMUNITY_CURRENT_GEN_PS_PLAYER_EXPERIENCE；作者按个人风格调整，并非官方“正确数值”；不得改当前世界全局Slider或人物能力 |
| **SRC-0089** | [OS：Shot Tendency](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-last-gen/471405-shot-tendency)，2012-02-18/19，beast10/youALREADYknow/RyanFitzmagic | 老版用户对总体Shot究竟影响Sim还是3D、Touches/战术类别/球星目标哪个是主要驱动有不同解释。支持“不用单一公式直接计算每场FGA” | **OLDER_SERIES_COMMUNITY_CONFLICTS**；2012不同引擎版本，不能当2K22原生准确机制 |
| **SRC-0090** | [OS：Tendency Edits That Are Game Changers for Realism? 第84页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/841295-tendency-edits-that-are-game-changers-for-realism/page84)，vannwolfhawk、daveberg、JoFri 2021-09-17至20 | Vannwolfhawk以2K22编辑者身份讨论左右突破、左右后撤步、Flashy Passing对CPU 3D动画选择的影响；同帖用户又对Shot/Shot Location影响Sim或3D提出疑问，另一些答案明确只基于2K19 | **MIXED_CONTEXT_PRIMARY_EDITOR_DISCUSSION**；2021版经验有用，内嵌2K19案例不得当2K22验证或角色统一参数模板 |

### 本轮与本地原生来源的交叉核对

`config/state_io_native/player.json`精确**48个已命名offset**，`src/gm_state_io/registry.py`将`0x458..0x4BA`共**99个1-byte PLAYER_TENDENCY槽**注册为技术`raw_range=[0,100]`，其中**51个`UNKNOWN_RAW_BYTE`只读**；四个PlayType槽是`0x168/0x169`的4×4bit/0..15，Initiator为`0x16A`一个1bit候选。**所有这些原生当前值是否已采、是否具有真实PC菜单精确名字和3D效果是独立事实**。玩家角色是否愿意改、Coach/GM是否反对、真实玩家是否批准也是独立权限，不由`writable=true`自动赋予。

**图证阴性确认**：本轮已检索2K22 PC原版Tendencies、PlayTypes、Initiator截图和Google图片，未获得具有可读滚动菜单、能明确识别原版PC和Offline MyLEAGUE的认证页面。2kAuction为**可读网页数据导出，不是Edit Player原版菜单帧**；见VIS增量。本次新增合格`PC22_UI_CONFIRMED=0`，不说明这些功能不存在。

**R04-B交付**：K03/K12新§§9–16和原生/外部两个99项目录；R04-C继续人格徽章与Loyalty/Financial Security/Play For Win、士气、合同/关系的自主选择；不启动Agent、DEV28/Codex或游戏采集/修改。

## DEV29 R04-C — 人格徽章、三类职业动机、士气、合同意愿与角色协商（2026-10-21）

新增**SRC-0091..0105**。同版玩家案例、2K20开发人员原始说明与老版受控/半受控试验的效力分开评价；外部自制Event Generator不当游戏内置能力。**角色目标和原生职业偏好是两套数据，研究不等于允许修改原始球员资料。**

| 来源 | 页面、版本与具体位置 | 可靠的机制原料 | 不可做的推断 |
|---|---|---|---|
| **SRC-0091** | [OS转载NBA2K20 MyGM/MyLEAGUE开发博客](https://www.operationsports.com/nba-2k20-franchise-mode-developer-blog-mygm-2-0-myleague-more/)，2019-07-29 `Additional MyLEAGUE-Level Features`；亦见[2KW全文转录](https://nba2kw.com/nba-2k20-mygm-myleague-mode-details-features-leaderboards-action-points-more) | **开发人员明确**：Morale/Team Chemistry各自向每日平衡点变化、工作态度差异影响Chemistry；针对顶薪竞争引入Media Ringmaster大市场、Warm Weather Fan暖气候、Finance Savvy税务的选择“辅助平局因素”，不是主导签约的绝对规则 | **官方2K20系列说明**：不能据此说2K22 PC保留完全相同数值系数/页面原生地址，或用它替代外部Player Agent的自由选择 |
| **SRC-0092** | [Operation Sports 2021-09-10 原创ATD 2K22帖子](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/916767-nba-2k22-attention-to-detail-roster-ps4-ps5-xb1-xbsx-pc-switch)，CelticLG #1及第二帖 | ATD作者明确将`Play For Win / Financial Security / Loyalty`作为独立人格/合同请求编辑字段；也分开处理Personality Badges；贴文同时称外部MyNBA Event Generator 200+ scenarios | 自制名单主张并不构成默认2K22原版数值、CPU合同公式，Event Generator是社区外挂配套作品，**不是游戏内建NPC事件系统** |
| **SRC-0093** | [2kAuction：NBA2K22 Joel Embiid Offseason 2021](https://2kauction.com/mynba/2k22/players/joel-embiid?roster=offseason_nba)、[Tyrese Haliburton Offseason 2021](https://2kauction.com/mynba/2k22/players/tyrese-haliburton?roster=offseason_nba) | 真实可读同版球员数据`Motivations`分组：`Loyalty / Playing for a winner / Financial security`独立0–100评分。例如Embiid 80/15/70，Haliburton 100/50/30；均有其人物资料和合同快照 | **第三方2K22游戏归档HTML**，不是本用户当前存档，也没有真实PC22编辑菜单逐像素与native offset映射；三个数字不是比例和必须的签约决定 |
| **SRC-0094** | [Reddit r/Nba2k22：Unhappy players in MyLeague](https://www.reddit.com/r/Nba2k22/comments/s1fuk4)，2022-01-11/12，作者答使用**PS4** | 作者报告降低Morale/调整Loyalty/Play for Winner后，给予Brissett首发和队内第三进攻点仍遭遇球员想离队的局面 | **2K22_CURRENT_GEN_PS4_ANECDOTE**；一人一档未控制因果，不证明本机PC22相同bug或“调整3项完全无效” |
| **SRC-0095** | [Reddit：2K22 MyNBA Free Agency is Awful](https://www.reddit.com/r/NBA2k/comments/v2mwpq)，2022-06-01 | 同版次世代MyNBA玩家报告不同队报价/球员要价和谈判可接受程度不对称，少数80+球员长期没人签、每个FA阶段要再次寻找球员并接洽 | **2K22_NEXTGEN_PLAYER_FIRST_HAND_BUT_COMPLAINING**；用户描述不是合同AI官方公式，不足以据此设置球员贪婪/忠诚性格 |
| **SRC-0096** | [OS：Free Agent Logic in MyGM，第2页及2015-03-15 #27–30](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/754168-free-agent-logic-in-mygm/page2) | 旧版玩家分别测试三项忠诚/争冠/金钱权重组合、续约/测试FA/胜利后果，另有用户提出不同“会留”的观察 | **2K15_MyGM_COMMUNITY_SMALL_EXPERIMENT**；各种“Loyalty=99必留”“只有夺冠才接受”是个人试验报告，不能当2K22 PC规则 |
| **SRC-0097** | [OS：MyLeague Free Agency Movement](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/901133-myleague-free-agency-movement)，2020-10-02/05，El_Tercero/WeFireThoseCannons | 玩家不同试跑出现Giannis签不同球队，回复认为Money/Role/3 Motives与Media/Weather/Tax可能影响去留，但最终结果带随机感 | **2K21时期本世代系列经验**；逻辑复杂性和未知必须保留，不证明精确合同概率 |
| **SRC-0098** | [NBA2KW人格词条：Media Ringmaster](https://nba2kw.com/nba-2k-media-ringmaster-badge)、[Warm Weather Fan](https://nba2kw.com/nba-2k-warm-weather-fan-badge)、[Finance Savvy](https://nba2kw.com/nba-2k-finance-savvy-badge)、[Alpha Dog](https://nba2kw.com/nba-2k-alpha-dog-badge)、[Friendly](https://nba2kw.com/nba-2k-friendly-badge)、[Unpredictable](https://nba2kw.com/nba-2k-unpredictable-badge)、[Legendary Work Ethic](https://nba2kw.com/nba-2k-legendary-work-ethic-badge) | 为这些独立人格徽章提供可读英文/通用语义，例如Friendly外向、Unpredictable行为难预期、传奇训练态度极高；前3项有SRC-0091开发说明作机制支撑 | 多词条混合MyPLAYER/旧版本释义；Alpha Dog旧版场上临时+属性的说明**绝不是PC22已认证效应**；21人名录中的其它项目还需认证native id与版本归属 |
| **SRC-0099** | [OS：Personality Badges in MyLeague/MyGM](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/827405-personality-badges-in-myleague-mygm)，2017-03-11 | 真实玩家问All Time Great、Legendary Work Ethic究竟会不会影响成长/受伤/合同，显示**社区本身不清楚单项机制** | **OLDER_COMMUNITY_QUESTION_ONLY**；问题不是已证“可以Very High练且不会受伤”的答案 |
| **SRC-0100** | [OS：MyLeague impressions? 2K20，第7–8页](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/881906-myleague-impressions-2k20/page7)，2019-09玩家 | 玩家解释`Player Morale`与`Team Chemistry`不同；上场时间、赢球、角色和联盟动态与球员拒绝续约有关；有人报告名单箭头显示士气和伤病等综合状态变化 | 同版**2K20**论坛玩家观测，非PC22单场原生字段映射；不能用一条评分箭头倒推出Ability被永久改写 |
| **SRC-0101** | [Reddit r/2KMyLeague：The same glitches are bothering me year after year](https://www.reddit.com/r/2KMyLeague/comments/sqfmqh)，2022-02-12 | 2K22玩家称受限球员签多年合同后被一年QO替代，无法确认某些市场条款持久正确，影响对“已经签约”的理解 | SAME_GAME_PLAYER_REPORTED_FREE_AGENCY_BUG；不认定所有平台/每次都会发生，R05再研究RFA/签约流程 |
| **SRC-0102** | [OS：PLAYER LOYALTY - FINANCIAL IMPORTANCE - PLAY FOR WINNER](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/871898-player-loyalty-financial-importance-play-for-winner)，2019-03-14问题 | 作者询问三种偏好是否会**随赛季/转会/赢球/工资变化而自动更新**，论坛未给出可验证结论 | **UNANSWERED_OLDER_SERIES_QUESTION**；R04-C标三项native跨季动态机制UNKNOWN，不应擅自动调整 |
| **SRC-0103** | [ATD社区2021-09主帖第二段说明外部MyNBA Event Generator](https://forums.operationsports.com/forums/nba-2k-basketball-rosters/992144-nba-2k22-attention-detail-roster-ps4-ps5-xb1-xbsx-pc-switch.html) | 作者自建约200–250个随机/人物事件场景，允许使用社区编辑的人格徽章筛选活动 | **EXTERNAL_COMMUNITY_EVENT_TOOL**，不是原生NBA2K22/PC/PS5自动剧情引擎；不能由此推断“NBA2K22自带200个事件” |
| **SRC-0104** | [NBA2K22 MyNBA官方开发细节转述：MySTAFF Sports Psych](https://www.operationsports.com/nba-2k22-mynba-details-revealed-mystaff-staff-carousel-prep-hub-attributes-badges-more/)，2021-09-08 | 2K22**次世代**官方称Sports Psych影响Morale/Team Chemistry；若弱可能出现负反馈循环 | **OFFICIAL_NEXTGEN_ROLE_MECHANISM_REFERENCE**，不证明PC本世代能雇用完全同名岗位或已读此属性 |
| **SRC-0105** | [NBA2K Wiki：MyGM Front Office / Review Player Roles](https://nba2k.fandom.com/wiki/Front_Office) | 老MyGM资料列Star/Starter/Sixth Man/Role Player/Bench Warmer/Prospect等角色，并认为角色影响士气与续约、合同谈判涵盖薪资、年限、球员/球队Option和No-trade | **OLDER_MyGM_MODE_DOCUMENTATION**，不是2K22 PC原版MyLEAGUE菜单或新增Agent谈判接口的证明 |

**新研究原料与工程边界**：
- 完整独立目录[`R04C_PLAYER_MOTIVATIONS_PERSONALITY_V1.json`](catalogs/R04C_PLAYER_MOTIVATIONS_PERSONALITY_V1.json)：三项0–100动机、21个来源分级的人格候选（原R04-A 20项加Warm Weather Fan）、四类情绪/角色/谈判状态、六类可提出/拒绝的角色选择。全部`native_offset=null`和当前真实人物数值`null`，不虚构PC22可写。
- NBA2K22 Archived Motivation的**三个数值不要求合计100**；`Finance Savvy`是环境税务偏好，和`Financial Security`收入保障偏好**两个不同实体**。
- 玩家与GM各自的外部思想、决议、合同承诺必须独立于原生游戏的字段读值；普通游戏操作不允许改Ability、Potential、Badge、Durability；交易/合同仍需原生合法条件、当事角色权利与真人玩家批准。
- 现有`config/memory_field_profile.json`确有17项已注册合同字段，但是没有本轮可核对的三项Motivation原生具名偏移；**字段存在于网页归档不代表现行存档已捕获值，也不代表能直接写**。

**R04-C状态**：`R04_C_RESEARCH_PUBLISHED_WITH_NATIVE_MOTIVATION_GAPS`，下一轮`R04_D_PLAYER_AGENT_DUAL_SEMANTICS_AND_INTERACTION_ATLAS`；独立审核由其它模型负责，本研究窗口不主动审核、不开发Agent，不启动DEV28/Codex或修改游戏。
