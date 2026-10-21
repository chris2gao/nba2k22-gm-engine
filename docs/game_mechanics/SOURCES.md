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
| SRC-0026 | [2K22 MyNBA官方开发团队说明：MyNBA Full Details](https://hoopsgamers.com/nba-2k22-mynba-full-details-mystaff-training-pre-built-teams-more)，§\`COMPACT SPREADSHEETS\`（[2K原始页面](https://nba.2k.com/courtside-report/nba-2k22-mynba)） | 2021-09-08，Visual Concepts开发团队，经NBA2KW/HoopsGamers转载；**PS5/Xbox Series MyNBA** | 官方文字列\`roster, coach gameplan, box score\`三类压缩表格，每屏显示行数超过此前两倍；图文页面旁有MySTAFF Roster截图 | OFFICIAL_AUTHOR_REPRINT_VERIFIED_TEXT，**不是PC/PS4 MyLEAGUE界面证明**；未取得可核验的Box本体截图；原站可能403 |
| SRC-0027 | [Operation Sports：What are some new things you want to see in 2K23 MYleague?](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/920627-what-are-some-new-things-you-want-to-see-in-2k23-myleague)，2022-02-02/10，#6与#9 | NBA2K22时期玩家讨论（当前世代MyLeague与次世代MyNBA混合） | #6直接区别\`Current Gen MyLeague\`和\`NextGen MyNBA\`；#9希望将季后赛统计及单场最高放入球员卡并增强历史跟踪 | COMMUNITY_CONCURRENT_WISHLIST；**期待改进≠已验证PC22功能不存在、也≠存档无Box历史** |
| SRC-0028 | [Steam：NBA2K17 PC MyLEAGUE特殊联盟规则下场内与Box得分不一致](https://steamcommunity.com/app/385760/discussions/0/1290691308577544770/)，2017-05-26，Ray原帖 | NBA2K17 **PC MyLEAGUE** | 玩家指出“罚球自动给分”规则下，场内统计34分，赛后Box/赛季重新结算只计27分；说明一些游戏规则可能造成统计阶段不一致 | COMMUNITY_FIRST_HAND_OLDER_PC；**不是NBA2K22仍有此BUG的证据**，仅用来定义质量风险和分层来源 |

### 本轮保留而不重复计数的来源
- [SRC-0015] 2K22 PS4本世代MyLEAGUE **DarthRambo #1–#2**：再次直接核对原文中\`Quarter Length\`, \`Simulated Quarter Length\`, \`Team Style Factors\`, \`Possession Results\`, \`Shot Types\`, \`Shot Percentages\`, \`Stat Distribution\`栏目；11分钟和各数值是**作者个人设置**而非PC默认/游戏中的现实回合数。
- [SRC-0025] PC自定义\`Remastered\`新闻：继续作为排除非原版PC截图的重要警示，不能将其“MyNBA”菜单作为本项目证据。

**研究结果的阴性边界**：针对“NBA2K22 PC MyLEAGUE Game Logs/Advanced/Per36菜单截图、每场完整Box表头、赛后Shot Chart、跨年单场Box寿命”做了多组中文/英文和PC/本世代限定检索。返回大量**真实NBA联盟统计网站**、2K次世代官方图文、2K其它玩法、游戏模组或非NBA2K软件；**没有找到足以逐像素确证上述PC22原生页面的独立公开材料**。阴性搜索不等于不存在功能，不给\`PC22_UI_CONFIRMED\`、\`PC22_NATIVE_READ_VERIFIED\`或\`PROJECT_CAPTURED\`升级。2026-10-20只读取公开材料，没有复用/上传外部截图文件。
