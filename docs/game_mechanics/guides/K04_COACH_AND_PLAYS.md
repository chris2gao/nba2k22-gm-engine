# K04 — NBA2K20–23 教练、Playbook、Freelance、ACE与攻防策略实用指南

> **DEV29 V3 / R02-A；2026-10-20。** 主研究对象NBA2K22 PC本世代离线MyLEAGUE。结合当前仓库已认证原生操作与NBA2K22官方/同代玩家观察，讲清具体机制、冲突、GM经营价值和未知。**文档不授权运行DEV28、Codex、采集、修改原生游戏或调整球员能力。** 当前R02-A为第一批正式攻略，不等于所有战术效果已验证。
>
> 来源：本仓库 [教练手册](../../../web_gm/manuals/GM_COACHING_OPERATIONS.md)、[个人防守与本队手册政策](../../../web_gm/manuals/GM_DEFENSE_AND_TEAM_PLAYBOOK_POLICY_V1.md)、[12类战术研究](../../development_research/NBA2K22_PLAYBOOK_12_CATEGORY_AND_NATIVE_TYPE_MAPPING_V1.md)、[共享战术池](../../GM_SHARED_PLAY_POOL_V1.md)；外部新来源SRC-0030..0039见[SOURCES](../SOURCES.md)。

## 0. 对象与证据等级

| 级别 | 研究结论与界限 |
|---|---|
| PC22_PROJECT_NATIVE_VERIFIED | 项目既有隔离测试已有19项Coach默认设置中多字段读写/回读证据、18项针对对手的防守字段原生信息、34种Freelance枚举PE文本配对、68战术书槽位和CRC定位。不是本轮新做测试，更不是所有设置的3D效果已实测 |
| PLAYER_REPORTED_UI | 玩家已确认PC22战术可浏览12种类别、每人四个有序PlayTypes、四个有序Freelance，以及战术2D预览；“前槽优先”只作定性描述 |
| OFFICIAL_2K22_GAMEPLAY | 官方披露2K22优化AI防守轮转、位置、射门/投篮IQ等；不是详细MyLEAGUE内存枚举 [SRC-0030] |
| CURRENT_GEN_ANALOGUE | Xbox One版2K22玩家具体说明Gameplan→Defensive Settings选项；不提升为PC菜单截图 [SRC-0034] |
| KNOWN_IN_SERIES | 较早MyLEAGUE的Coach Gameplan、ACE/暂停菜单、Freelance经验 [SRC-0036/0037]；不证明PC22菜单完全相同 |
| UNKNOWN | PC22逐像素全页签、ACE精确模式/覆盖持久性、CRC真实分类成员、Playbook槽位对应3D战术调用概率等尚无完整认证 |

**研究、可观察、可用项目接口、能合法改变、产生实战效果，是不同证据轴。** 不把原生字节可写当作游戏已经按预期运行，也不把用户/教练Agent建议当作玩家批准。

## 1. 什么是真正的完整进攻系统：七层互相作用

1. **球员和阵容**：持球点、策应者、射手、挡拆顺下者、短顺下传球者与其可用性，这是打法的物理基础。
2. **教练体系与POE**：PreferredSystem是偏好，ActiveSystem是当前采用；POE包括进攻重点、耐心/速度倾向、进攻篮板/退防取舍。
3. **RunPlayTendency**：有多强的调用成套预设战术倾向；原生0–100并不等于每100回合必执行同数次完整战术。
4. **球队本名Playbook容器**：68个各有来源CRC的槽，意味着球队有哪些**候选动作**，不是球员触球次数。
5. **每个球员4个有序PlayTypes**：球员可被安排的战术**类型**，不是直接指定4个play CRC；本项目玩家认为前两项主要、后两项较少，不能量化概率。
6. **四个有序Freelance槽**：整体自由进攻阵型/空间配置，并非4名球员或4条具体战术；优先级次序保留，不假设等频。
7. **ACE、Play Initiator、Touches、Shot Tendencies、Play Discipline与临场叫战术**：影响由谁发起、是按设计跑还是自行创造、怎样终结；只能用真实比赛观测研究关系，不能假造单变量算法。

依赖链：**阵容角色 → 教练POE/体系 → Playbook内有合适的类型与动作吗 → Run Plays/ACE/球员四槽 → 实际出手、助攻、篮板、失误 → GM按动态数据复盘**。逻辑上如果某球员没有匹配类型/书中无对应动作，单纯调高Run Plays不会凭空生成战术。同版玩家曾发现SF没有合适战术，因为书内根本没有匹配其PlayType的动作 [SRC-0031]。

## 2. K04.COACH_GAMEPLAN — 已有19项默认设置怎么用于建队

项目手册登记19项COACH_DEFAULT，下表的数字是已知原生**枚举ID**，不是玩家应全队统一设置的目标。

| 原生字段 | 有来源的合法值/语义 | 经营用途和潜在代价 |
|---|---|---|
| POEOffense | 0无偏好；1 Get to Basket；2 Get Shooters Open；3 Feed Post；4 Pick and Roll Offense；5 Neutral；6 Run Through Scorer | 突破/外线/低位/挡拆/核心选择，须先看阵容与战术书 |
| POEOffense2 | 0无偏好；7 Patient；8 Neutral Tempo；9 Shoot at Will | 半场耐心组织与快速出手取舍；不是“第二得分手” |
| POEOffense3 | 0无偏好；10 Crash Offensive Boards；11 Neutral；12 Limit Transition | 拼二次进攻还是防对手快攻；不是“第三得分手” |
| POEDefense | 0无偏好；13 Protect Paint；14 Neutral；15 Limit Perimeter Shots | 限篮下或防外线，需看对手投篮结构 |
| POEDefense2 | 0无偏好；16 Conservative；17 Neutral；18 Physical | 侵略性/犯规/被突破风险；不能推导必然增加抢断 |
| POEDefense3 | 0无偏好；19 Crash Defensive Boards；20 Neutral；21 Run in Transition | 防守结束篮板与提速转换的取舍 |
| PreferredSystem / ActiveSystem | 0 Balanced；1 Grit and Grind；2 Pace and Space；3 Perimeter；4 Post；5 Triangle；6 Seven Seconds；7 Defense | 教练偏好与实际体系两套字段，不直接改球员体系熟练度 |
| PlaybookID | 原生真实book enum_id | **日常GM只读**，不能随意切其它队书；换帅后的恢复须另获授权 |
| BenchDepth | 原生整数；轮换人数上限 | 不按百分比、不把10人当最大上限；不再精确锁分钟 |
| RunPlayTendency | 0–100 | 设置调用战术倾向；不能等同绝对战术执行率 |
| ZoneUsage | 0–100 | 选择联防倾向，不能用单场数据保证联防收益 |
| BenchUtilization | 0–100 | 替补使用程度，和BenchDepth分开 |
| Tempo | 已有本机原始字段；确切UI含义、端点未知 | 不等于POEOffense2，也不等于SimPace；不要想象0–100就是已证端点 |
| HelpDefense | 0–100 | 帮助内线/弱侧补位与漏三分、协防轮转相权衡 |
| FreelanceType / Type2 / Type3 / Type4 | 已登记34种原生枚举raw 0..33 | 四槽保留原生顺序；本轮未核对每种动画、4槽实际使用率 |

**当前业务安全规则**：SimPace/SimPress/SimHelpDef/SimOffReb/SimDefReb是GM只读；默认不切PlaybookID；轮换分钟游戏AI会覆盖精细分钟控制，GM只使用人数上限与替补倾向等可靠杠杆。已部署原生写入范围/保存条件须以最新同批真实来源与DEV14已批准合同为准；本节不产生修改请求。

**实例**：球队拥有真正能创造挡拆优势的后卫、能顺下的内线与两名可靠射手时，POEOffense=4是一个合理**候选**；但还应先检查本队书是否有适配的FIST、球员类型、对手换防策略，不能只因这队有一个高评分PG就自动复制。若球队缺投射，换Pace and Space并不产生额外三分能力。

## 3. K04.PLAYBOOK — 本队专属Book容器与联盟共享战术池

本项目当前规则：球队持有本队同名**原生书容器**；一条具体战术CRC可以被多个球队各自引用。GM修改的是自己球队有限槽，不允许通过编辑B队原生book来实现A队战术变化。**休赛期每个赛季最多换帅一次**，换帅后如新教练携带原书，需另行批准把PlaybookID恢复本队书，再读新前值并分别批准改槽；仅研究不执行。

| 书区 | 原生容量 | 用法与界限 |
|---|---:|---|
| Regular | 30 | 常规set plays候选 |
| Bench | 20 | 替补相关战术槽，未证AI怎样触发 |
| Endgame | 10 | 末段候选，具体CPU调用时机待验 |
| Favorite | 8 | 快捷/偏好槽，不等于额外8条全新完整动作 |
| **总计** | **68** | 空位在各自分区计算，不能跨区借位 |

共享池是**历史已加载归档**：84本书、1,392条去重CRC，原始名称通过CRC与静态标签关联，其中一部分仅有名字、用途仍属NAME_INFERRED；**1,392条目前均未认证完整CRC→原生战术类别成员**。来源曾是旧归档，不代表现在每个队都装着同一book。GM可从池检索用途/球员角色适配，但**只能把有真实来源的CRC作为将来合法提案候选**，不能因FIST字样就臆测类别id。

**名称怎么读**：用户已经确认共享池真实的 '95 FIST 15 SIDE、CRC 0x79215B33，是挡拆家族，95年代标识、FIST挡拆、15涉及1号位发起与5号位掩护、SIDE侧翼路线。其他FIST 14 POP可依据字面先猜4号位外弹，但第一接球者、第二机会、实际最后投手要通过2D战术板或3D观测确认。**名字蕴含篮球语义，但不是不可反驳的原生type证据**。

NBA2K22同年MyNBA玩家说达拉斯名单缺适合Luka出任SF的行动时，增补Cutter、Mid及3PT类型play后观感改善 [SRC-0035]；这是**次世代社区个案**，不是官方万能配方。

## 4. K04.PLAY_CATEGORY — 玩家确认的12种动作分类

这些中文类别来自**PC22用户已在游戏UI中浏览的描述**，对应英文是通用NBA2K篮球术语，并不保证PC英文菜单逐字。它们不同于球员4个PlayTypes的raw id。

| # | 中文 / 英文参考 | 球员职责、为何需要 | 不适合/被克制 |
|---|---|---|---|
| 1 | 单打 Isolation | 清空一侧由高单打能力球员攻击错位 | 效率低、拖慢球权转移 |
| 2 | 挡拆 Pick & Roll | 持球+掩护人，寻顺下/突破/转移 | 防守换防和收缩会破坏初次机会 |
| 3 | 中投外弹 Pick & Fade Mid | 掩护者外弹至中投点接球 | 掩护者无中投或对手顺利换防 |
| 4 | 三分外弹 Pick & Fade 3PT | 会投三分的掩护者外弹至三分线 | 内线无射程反而降低空间 |
| 5 | 挡拆选项 P&R Option | 按防守决定顺下/外弹等分支 | 游戏具体分支规则与触发未知 |
| 6 | 低位背身 Post Up Low | 能背打或分球的内线低位接球 | 对手包夹、弱侧投射不佳 |
| 7 | 高位背身 Post Up High | 肘区传控/面框/中投核心 | 接应区域与节奏配合不到位 |
| 8 | 后卫背身 Guard Post Up | 大后卫打小后卫错位 | 缺身材优势、失去团队空间 |
| 9 | 中投 Mid Range | 绕掩护无球跑动，制造中距离 | 球员中投效率不足 |
| 10 | 三分 3PT | 让移动/定点射手获得三分接球机会 | 盲投、对手追防/换防 |
| 11 | 手递手 Handoff | 肘区或高位传球者递球+掩护 | 接手者、传球者职责不匹配 |
| 12 | 切入 Cutter | 无球从防线背后切篮下 | 对手拥堵禁区、缺接球发起人 |

**不要将12类play目录和球员play_type_names 0..15视为同一枚举**。一条CRC可能归多个战术类别，类型过滤的有效集合才是将来实机认证目标；没有该事实，只有NAME_INFERRED候选，不能悄悄填本机类型ID。

## 5. 球员PlayTypes、Play Discipline、Touches：缺席的第三球星为什么不参与？

本项目原生球员角色类型枚举：0 None；1 Isolation；2 Isolation Point；3 Isolation Wing；4 P&R Ball Handler；5 P&R Point；6 P&R Wing；7 P&R Roll Man；8 Post Up Low；9 Post Up High；10 Guard Post；11 Cutter；12 Handoff Receiver；13 Handoff Passer；14 Mid Range；15 3PT。

玩家说明每人四个类型槽，**前槽更优先**，后两槽较少调用但并非不可能；**一个PlayType不是一个具体战术CRC**。即使给球员设了P&R Ball Handler，也不意味着book中必有相容的FIST，更不意味着下一回合必为他叫战术。

2021年9月OS 2K22一手讨论特别有用：jimbo3772将Touches主要视为自由进攻/未跑预设时球权分配，认为真正叫谁的战术还取决于教练focus、球员能力、PlayTypes和Playbook；他报告曾找不到适合某SF的书内动作 [SRC-0031]。有人声称统一Touches或提高Play Discipline使球队分享球更好，也有人在10月反馈改Touches仍使教练仅为两名后卫叫战术、另有玩家反驳 [SRC-0031/0032]。**社区没有可信的固定数值—成功率公式**。

实务顺序：**先看Book类型与球员四槽相容性，再看教练RunPlayTendency、POE、Freelance及阵容实战表现**。不因讨论贴推荐Touches=50、Discipline=100就直接修改普通球员倾向或能力。球员Tendencies是否在项目允许修改的动作内须另过审批，研究不构成授权。

## 6. Freelance、ACE与自动叫战术：三个不同控制层

**Freelance**主要指自由进攻的站位/空间与球员间配合，并非严格固定路线play。项目已通过本机原生enum/同版PE字串匹配34类：包括FOUR_OUT、WARRIORS、JAZZ、PHILLY_ELBOW、TRIANGLE、PRINCESTON_CHIN、PACE、FLOW、SEVEN_SECONDS等，但**名字不等于本轮看过逐个实际跑位**。教练四槽同样有序，不能由位置1/2/3/4推算25%/25%/25%/25%。

**ACE = Adaptive Coaching Engine**。旧版开发人员材料称其依据对手、阵容和比赛时间动态调整战术计划 [SRC-0037]；2018–2020玩家对ACE是否会临时覆盖Gameplan、是否重复叫同一条play有**冲突说法** [SRC-0036]；2021年2K22 OS帖子也有玩家提到将ACE设成Defense Only后进攻更灵活，却没有对目标PC CPU vs CPU可靠控制实验 [SRC-0031]。因此：
- 默认教练字段反映**静态设置**；
- ACE/Offensive Playcalling/Defensive Playcalling是比赛运行时的**动态自动策略层**；
- 游戏引擎实际3D战术选择、球员是否执行到底是**结果层**。
静态字段写回成功不可当作3D打法已证明，玩家既有业务希望保留默认ACE，**本攻略不自动建议关闭ACE**。

更早MyLEAGUE玩家抱怨自己临场Freelance难以在下场保存，这只能启发我们区分“菜单可选 / 当前回合有效 / 下一场有效 / 保存后仍有效”，不能直接说PC22一定有一样的BUG。2K22 PS5玩家通过PlayVision=All Plays、Offense Playcalling=Auto显示更多战术移动，属于**次世代个人游戏设置体验** [SRC-0039]，不是当前终极联盟CPU模拟自动战术认证。

## 7. 防守：普通GM必须区分OVERALL、PERSONAL与ACE

**用户当前规则优先**：对方球队29支的默认整体防守可以只读采集，但日常GM**不再提出修改OVERALL_DEFENSE**；相反，为对方明确的具体进攻者用DEV14支持的PERSONAL_DEFENSE稀疏策略，有变化才提案。整体修改可能覆盖个人设置（玩家实机经验），所以不能在本项目继续沿用旧整体防守操作示例。个人目标须具备稳定native_player_id、defender_id与指定owner/opponent，未知就HOLD。

| 原生字段（共18项） | 球队经理可理解的用途与代价 |
|---|---|
| PressureOnball / PressureOffball | 持球/无球施压。对方射手需紧、对方切入快需考虑被反跑风险。注意压力不等于绕过掩护 |
| ForceDirection | 引导持球人方向，必须按本批raw字典选择 |
| ScreenDefenseOnBall / ScreenDefenseHedge | 后卫绕有球掩护/协防大个上提或沉退；过分上提易丢顺下 |
| OffballScreenDefense | 防无球绕掩护与空切，不等于有球Hedge |
| PostDefense | 低位前顶或从不同角度顶防，收益与犯规/篮板相关 |
| DoubleTeamPerimeter / DoubleTeamPost | 外线/背身包夹，考虑对手传球及弱侧射手 |
| ScreenDefenseOnBall5 / ScreenDefenseHedge5 | **两个独立字段**；当前PC中文标签、适用对象和与普通版的覆盖条件UNKNOWN，禁止凭“5”猜为“中锋开关” |
| SwitchRule | 换防允许范围；受阵容尺寸/错位/护筐制约 |
| OnballHelp / ScreenHelp | 持球帮助和掩护帮助，独立于Coach HelpDefense与Hedge |
| ExtendPressure | 扩张压迫意图，不能推定就是全场紧逼 |
| TagOnRoll | 顺下协防相关原生名与枚举已登记，**具体本机触发逻辑UNKNOWN** |
| StayAttached | 在掩护/弱侧场景保持盯防，效果受换防/协防协同影响 |
| PreRotate | 原生packed bool，只接受0或1，不是假想的AUTO/YES/NO三值 |

**有价值的2K22同代菜单纠错**：2021年10月Xbox One与Series X玩家报告GAMEPLAN→Defensive Settings可调整On-Ball/Off-Ball Pressure、On-Ball Screen、Hedge、Post、Stay Attached等；作者一度错误地把Go Over写在Pressure字段，其他人指出压力选项是Gap/Moderate/Tight/Smother，作者回帖纠正 [SRC-0034]。这意味着**不能把不同字段的枚举混用**，也不能直接把Xbox截图推成PC原版逐字UI。

**防守效果真实风险**：官方宣布2K22重做投篮干扰、封盖与轮转 [SRC-0030]；同年Operation Sports编辑撰文指出防守弱侧补位在某补丁后可能异常，一些Gameplan选项可能不像文字描述那样生效 [SRC-0033]。官方更新意图与玩家BUG观察可以同时成立。不要把某年补丁问题无限推广到当前项目exe，也不要把一次保存成功当作实战一定发生防守动作。

## 8. 让GM能做决定的三类场景与反证

| 动态现象 | 优先确认的事实 | 可讨论的机制调整 | 什么情况下要HOLD |
|---|---|---|---|
| 核心单打频繁、其他人几乎没出手 | 比赛场次、出场分钟、Book类型/球员PlayTypes、实际核心可用性 | 增补有证据的3PT/Cutter/Handoff play、比较POE与RunPlays | 数据只有单场胜负，缺Book/人员真实来源 |
| 3PA不足而球队有优秀射手 | 真实3PA/FGA、射手上场与接球/无球角色 | Get Shooters Open、三分战术、空间Freelance候选 | 球员无射程，不能用菜单替球员增加能力 |
| 对手挡拆持球者反复杀到篮下 | 对手主攻者和掩护者、球队犯规、防守篮板/侧翼空间 | 指定对手球员Personal Screen/Hedge/Help，明确弱侧代价 | 个人matchup身份/合法enum不存在时不生成整体替代动作 |
| 对手低位得分高而外线弱 | 低位触球/罚球/外线投篮、内线犯规负荷 | 个人低位防守、定向包夹、POE护筐分析 | 不能仅凭对手PTS就假设全由Post产生 |

每次方案至少注明：save/career、最新数据批次、球队/对手/当前教练/本队Book、真正字段和枚举、当前值、期望值、依据、代价、结果观察指标与审批状态。**分析未验证读数时保留UNKNOWN；GM不造比赛数据、不随意修改球员属性。**

## 9. 多智能体权限（DEV29 V3）

教练Agent可以坚持自己的体系、拒绝GM的打法提议或主动请求特定类型球员；GM可以协商/提出经批准的团队配置；球员Agent会对触球/角色变化产生态度；媒体Agent可以质疑球队战术效果。但以上人格和态度如果并非游戏原生可读取，只能在外挂另存**角色意图/模拟事件**，不能直接伪装成NBA2K22的真实倾向、化学反应或比赛数据。教练/球员双方同意，也**不代替真实玩家授权游戏写入**。

## 10. R02-A已交付、未证事项与R02-B断点

**本轮交付**：Project-native能力与政策基线；Coach19和PERSONAL18的篮球含义、约束；12战术类别完整使用说明；book68槽与共享池1,392项历史来源边界；原生四PlayTypes和四Freelance区别；ACE/Play Discipline/Touches/Run Plays行为层分析；真实2K22玩家矛盾报告及2K官方防守信息；GM从动态数据提出可检验方案的模板。

**R02-B优先要补的具体事实**：
1. NBA2K22 **PC本世代原版**Coach Gameplan与暂停菜单、ACE/Offensive Settings/Defensive Settings的具体页签、按钮与完整合法值域，其他平台严格标同代或系列；
2. ACE与Freelance如何覆盖临场叫战术，四个Freelance原生槽如何映射实际站位；旧版菜单BUG不能擅自外推；
3. 12类具体play CRC→类别ID、2D动态board和球员PlayTypes的匹配依据；目前仍是显式UNKNOWN；
4. Personal18中OnBall5/Hedge5/TagOnRoll/StayAttached/PreRotate的原版UI与相互覆盖；战术效果需与AI是否自动覆盖分开；
5. 真实进攻/防守对手策略和阵容变化关联的可观测指标，不能编造调用率。

**恢复方式**：先读本K04、[PROGRESS](../PROGRESS.md)和SRC-0030..39，从R02-B继续研究，不重新开始R01或重新定义现有DEV14/Playbook共享池。R02尚未整体COMPLETE；本轮没有修改游戏、项目执行程序或球员能力。
