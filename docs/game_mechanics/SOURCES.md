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
