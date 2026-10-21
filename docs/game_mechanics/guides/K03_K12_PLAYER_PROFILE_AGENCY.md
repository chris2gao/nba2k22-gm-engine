# K03 / K12 — NBA2K22球员完整档案、属性、身体耐久、徽章与自主职业生命线

> **DEV29 V3 / R04-A 首批正式中文研究（2026-10-21）**。研究对象NBA2K20–23系列，最终目标NBA2K22 PC本世代离线MyLEAGUE。**这份文档是供未来球员、GM、教练、媒体自主观察和选择的游戏机制原料，不是玩家编辑教程、不启动Agent、也不是批准修改球员属性。** 来源[SOURCES](../SOURCES.md) SRC-0072..0080；项目原生[PLAYER字段配置](../../../config/memory_field_profile.json)、[player.json](../../../config/state_io_native/player.json)、[source_extensions](../../../src/source_extensions.py)、[DEV15潜力遮蔽](../../development_tasks/DEV_20261019_15_GM_SCOUTING_FOG_AND_OVR_ROTATION_CONTROL_V1.md)，以及R03的[K06](K06_TRAINING_HEALTH_GROWTH.md)。
>
> **按任务书本轮只完成R04-A**：个人身份、完整已知属性子集、部位耐久、徽章组/人格类别的首次梳理、自然成长的关键输入与严格信息边界。R04-B再调查全部行为倾向/PlayTypes与3D/Sim；R04-C深入人格徽章和合同意愿；R04-D全字段交叉权限、人物互动图谱。未完成的后续主题不能在此宣告完整。

## 0. 三轴证据：机制能够复用，字段仍需认证，当前实际读数又是第三件事

- `FRANCHISE_MECHANISM_REUSABLE`：用户确认2K22 PC本世代与PS5/Xbox Series终极联盟的经营机制大体高度可复用；合同、培养、球员卡、职业成长的参考优先取2K22同版，再参考2K20–23，**但不能倒推出同一raw/菜单项**。
- `PROJECT_NATIVE_LAYOUT_REGISTERED`：本仓库 `memory_field_profile.json` 已登记55项 `PLAYER.attributes`（含16项耐久）和17项 `PLAYER.contract`。这是有偏移的**真实项目注册子集**，不是球员全部可见数据全集、更不是R04-A进行了读内存或查看目前save。
- `CURRENT_BATCH_CAPTURE_VERIFIED`：只有当前`save_id/source_batch_id/source_profile`能确认名字、队伍、出生、属性读数与健康/合同状态均为真实游戏世界事实。本轮不读取存档，**第三方2K22球员展示站的球员数值不可当本项目当前联盟值**。

**额外关键**：官网/OS作者制作的ATD自定义名单展示**有哪些原生编辑领域**，不是“原版2K22默认的球员真实数值”或某项加成的官方算法。2021年12月ATD作者发文时PC名单还写为`work in progress`，其PS5/Xbox编辑数据不能代入项目PC存档。[SRC-0072/0073]

## 1. 球员“是谁”：身份、职业档案与全生命周期

### 1.1 个人资料和职业归属必须拆层

| 分组 | 玩家可见/有同版资料的候选字段 | 游戏系统中为什么有用 | 当前证据状态 |
|---|---|---|---|
| 核心身份 | 原生player identity/人物名字、姓/名、脸型与face ID、球员卡/头像/动画外观 | 交易、合同、历史选秀、职业故事必须知道**同一个人是谁** | 名字/face与来源映射在本项目数据工作流中出现；`face_id`单独不保证跨历史班唯一 |
| 生物与身体尺寸 | 生日、按game_date算年龄、身高、体重、臂展、位置与副位置、国籍、大学或来源 | 对位/阵容/运动属性、成长窗口和个人背景 | 2K22版本第三方原始字段页面详列[SRC-0074]；**本批PC字段覆盖不等于完全已采** |
| 选秀与经历 | Draft Year/Round/Pick/原选中球队、Years Pro、Roster Year、队史与球员位置变化 | 年资合同规则、历史选秀轮回和年龄相符性、跨队人生故事 | 同版2K22球员导出站[SRC-0074/0075] |
| 当前联盟状态 | 当前team、所属合同team、roster slot/健康可用状态、是否自由球员/伤停、球队球衣号码 | 合同/名单容量/出场资格、身份冲突 | 项目代码`player_details()`有`current_team_id`与`contract_team_id`两个指针；不一致需验证，**不是两者相同的硬假设** |
| 合同职业状态 | 当前年度工资、合同期限/剩余年限、选项/禁交易、Bird年数、续约相关字段 | 签约或交易时的真实约束及球员利益 | 项目原生Profile已登记17项合同子字段；合法合同机制在R05深入，本轮只识别原料 |
| 生涯事件 | 已完成比赛、赛季数据、联盟奖项、冠军、荣誉、签约/交易/伤停记录、退役 | Player在真实世界累积经历后改变自己的职业目标 | 可研究为信息来源，但**逐条事件是否被当前游戏保存/SQLite可查询必须按批次独立认证** |
| 外部身份记忆 | 球员自我故事、对球队/城市情感、教练信任、复仇或争冠志向、谈判承诺 | 实现真正的人格与长期记忆 | **外挂未来`EXTERNAL_SQLITE_CANONICAL`，不是游戏原生已记录事实** |

在2021年2K22同版Marques Johnson与Joel Embiid导出样例，`Bio`和`Development`还分开展示身高臂展、选秀顺位、年资、峰值年龄、成长曲线和合同等[SRC-0074/0075]。这足以为R04编制**人物来源字段目录**，但不能借外部网站冒称已读取本用户的球员pool。

### 1.2 不能把“名字/face ID”当跨世界线稳定主键

项目2021–22开档会轮回导入1984–2020历史选秀。如果一位球员被历史选秀注入、未来回归或多个数据源发生同名，应同时存储`career_id/save_id`、原生身份定位与来源、`snapshot_id/game_date`、选秀班身份和实际归属。**单靠名字、球衣号、face_id甚至当前队伍**不能可靠区分人物。候选复合身份只有经过游戏原生返回及本批去重、交易前后再认定为稳定；R04-A没有开发新的ID算法。

### 1.3 信息不是所有角色都等价可见

Player可知道自己的年龄、已有经历、合同与由自己提出的目标；GM可知名单/合同/公开比赛事实，但不该自动知道球员独有的内心打算；Coach能依据阵容、技能、训练与实际场上表现形成自己的判断；Media能知道公开荣誉、交易、出勤以及公开表态，但**不能从内部健康隐私或角色长记忆直接“报道事实”**。

## 2. 本仓库确有名字的39项非耐久属性：完整列出，不凭外站凑成“全游戏属性”

下面采用`memory_field_profile.json`中55项`attributes`扣除16项耐久得到**39项**。每项底层为1字节，转换函数`rating`，但**公开显示/实际历史上限、合法写入权不能从1字节推定**。名字是项目字段英文，中文为研究释义。这里强调何种**篮球行动能力**可能相关，**不是官方发动机计算公式或可直接编辑能力的权限**。

| 机制组 | 项目已注册英文原字段（中文） | 对角色决策可提供的区别 |
|---|---|---|
| 篮下与背身 7 | `driving_layup`突破上篮、`standing_dunk`原地扣篮、`driving_dunk`行进扣篮、`post_fadeaway`背打后仰、`post_hook`勾手、`post_moves`背身动作、`draw_foul`制造犯规 | 同样是内线得分，终结路径/身体对抗/被犯规能力不同，Coach可要求不同角色 |
| 外线与判断 5 | `shot_close`近距离、`mid_range_shot`中投、`3pt_shot`三分、`free_throw`罚球、`shot_iq`投篮决策 | 技术命中能力与选球IQ不同；不得从三分评分直接生成三分出手次数 |
| 控传与接球 6 | `ball_control`控球、`speed_with_ball`持球速度、`passing_accuracy`传球准确、`passing_iq`传球判断、`passing_vision`传球视野、`hands`接球/控球可靠性 | 人物是否能胜任组织者、挡拆持球者、短顺下处理者 |
| 防守与篮板 12 | `offensive_rebound`前场板、`defensive_rebound`后场板、`interior_defense`内线防守、`perimeter_defense`外线防守、`block`盖帽、`steal`抢断、`shot_contest`干扰投篮、`lateral_quickness`横移敏捷、`pass_perception`传球预判、`defensive_consistency`防守稳定、`help_defensive_iq`协防IQ、`pick_and_roll_defensive_iq`挡拆防守IQ | 一名防守者为何适配某种战术，Coach可选择换防、护框或补篮板；不等同球员实际防守态度 |
| 运动与韧性 7 | `speed`跑速、`acceleration`加速、`vertical`弹跳、`strength`力量、`stamina`比赛耐力、`hustle`拼抢积极性、`offensive_consistency`进攻稳定 | 出场体能、跑动与球星稳定输出不同；**Stamina不是R03的实时Fatigue值** |
| 特殊/成长 2 | `intangibles`无形因素、`potential`潜力 | Intangibles在本项目有非常有限的轮换干预例外；Potential必须遮蔽，不泄露真实未来 |

**数量复核**：7+5+6+12+7+2 = **39项**。具体offset、bytes、编码、是否被本项目发布给GM见[字段与权限矩阵](../catalogs/PLAYER_FIELD_AND_RIGHTS_MATRIX.json)，不能从这里数出“NBA2K22全部Skill Ratings恰好39种”：ATD作者2021年明确说他们编辑的还含很多别的可见属性与倾向[SRC-0073]。

### 2.1 最易引起世界扭曲的三个字段

- **Intangibles**：项目DEV15将其0x440（十进制1088）设为**仅此一字节**的特别受控轮换偏差操作（raw合法范围25–99）；这是玩家对GM业务的一项具体豁免，不等于可以操作所有其他属性，且**不能从外部资料推断其他签约/模拟/能力影响**。即使某角色要求修改，也须用户正式批准、原生身份验证、读回与回滚。
- **Potential**：项目DEV15明确`PLAYER[0x441]`原生潜力在游戏内部保持原值，但**正式发布给GM的玩家和历史新秀两库、raw/JSON中统一掩码为1**，并标`MASKED_BY_GM_WORLD_RULE`。这个1**不是实测球员潜力，更不意味着低潜**。任何玩家/教练/媒体Agent不得把潜力1用于识人、排序或叙事；同样不能绕过公开权限去读私有注入源。GM脱敏原始结构绝不能作为未来新秀直接注入源。
- **Shot IQ/Offensive Consistency与倾向**：技能评分、执行策略`RunPlays`、`Touches`、`Play Discipline`是不同字段家族。即使玩家拿到真实球员命中率，也不能反推单个原生技能的引擎真实权重。自动调用战术由K04研究，R04-B专查全部倾向。

### 2.2 OVR不是自由意志，更不是完整技能向量

OVR是游戏汇总评估，可能和位置、技能加权、Intangibles等互动。即使OVR不动，球员某项技能或体能也可能真实变化；反过来OVR上涨不保证某项指定技能上涨。R04个体职业判断需要**同批技能向量 + 比赛事实 + 对自己目标的不同解释**，不是由GM统一按OVR高低替30队和全部球员作相同选择。

## 3. 身体Durability：项目确名的16项完整子集与“25项”公共声称的区别

本机`memory_field_profile.json`已登记以下**16项部位耐久**，全属`attributes`且`rating`编码（不表示当前有完整伤病事件）。

| 身体组 | 原字段与篮球含义 |
|---|---|
| 头颈背 | `head_durability`头部、`neck_durability`颈部、`back_durability`背部 |
| 左右肩 | `left_shoulder_durability`、`right_shoulder_durability` |
| 左右肘 | `left_elbow_durability`、`right_elbow_durability` |
| 左右髋 | `left_hip_durability`、`right_hip_durability` |
| 左右膝 | `left_knee_durability`、`right_knee_durability` |
| 左右踝 | `left_ankle_durability`、`right_ankle_durability` |
| 左右脚 | `left_foot_durability`、`right_foot_durability` |
| 其他 | `misc_durability` |

**数量是3+6组左右各2+1=16。** 2K22当年ATD原作者曾称其团队覆盖约25项`durability attributes`[SRC-0073]，但没有在该帖逐条提供全部原生英文名。因此R04-A**不能凭25声称我们已确认25个名称/原生位置**。第三方同年球员页面也逐项展示上述16种[SRC-0074..0076]，为名字提供了**同版外部交叉支持**；仍不能排除该站未显示的额外字段或与其它健康机制的不同计数口径。其余与16不符的项目全部`UNKNOWN_PENDING_FULL_GAME_MENU`。

身体耐久≠当前伤病、预计恢复≠实际复赛、Stamina≠Progressive Fatigue。举例：历史名单网站对Michael Porter Jr.的背部给出的耐久数值与其他部位不同[SRC-0076]，只能说明**字段可独立取值**；绝不能拿历史网站数值作为本项目某一赛季他已经背伤的依据。**普通GM、Coach、Player Agent都不能为了提高伤病风险或塑造职业剧情直接改Durability**。

## 4. Vitals的成长时间表：Peak Start/End与Boom/Bust不能一概当“已认证PC算法”

2019–21 MyLEAGUE玩家通过`Edit Player → Vitals`观察`Peak Start`、`Peak End`；一些玩家解释成长在Peak Start前趋向提高，过Peak End后逐步退化，且会受`Potential`及全局进步/衰退滑块影响，但对年龄区间内如何变化也有疑问[SRC-0077]。**这是一种机制参照，不是我们拥有精确逐年成长公式**。

2022年**2K22 PS5 MyNBA**选秀班作者回帖显示`Boom%`、`Bust%`、潜力上下限可在球员Vitals设置，并和Peak Start/End共同影响成长结果[SRC-0078]；但其他本世代玩家曾说Boom/Bust也许是次世代新增，**PC22实际是否拥有同一菜单字段与编码需单独认证**。

同版球员导出网站可列出`Peak starts/ends`、`Minimum/Maximum potential`、`Boom/Average/Bust chance`与`Growth/Decline curve`[SRC-0074/0075]，这说明相关数据结构可以纳入R04的**研究对象清单**，并不自动证明本项目PC本世代`memory_field_profile`已注册这些字段。未来别将2K22网站某人的实际未来成长当成现在存档的必然命运。

**R04原料而非“最优成长规则”**：
- Player可以追求力量/速度/投篮等不同目标，接受输掉短期上场时间的代价；
- Coach可以重视体系/短期胜率，拒绝给新秀稳定上场；
- GM可以保留有潜力但当前低效的球员，或选择低风险即战力；
- Media可以对公开成长趋势作不同评价，但不能使用被遮蔽的真实Potential或未来Boom随机种子。

真正`LEARNING_SIGNAL`须由有来源的跨期attribute diff、真实比赛、伤病、训练来源形成；不改原生技能来兑现剧本。

## 5. 徽章与人格徽章：记录技能作用和职业态度的候选，而不是“统一人格标签”

### 5.1 四大游戏徽章家族

2K22同年玩家指南将Gameplay Badges分为：
- **Finishing** 终结/篮下；
- **Shooting** 投篮；
- **Playmaking** 传控组织；
- **Defense/Rebounding** 防守与篮板。

技能徽章有常见`Bronze/Silver/Gold/Hall of Fame`四档；无徽章记为None。本项目`training.json`亦登记`0 None;1 Bronze;2 Silver;3 Gold;4 HOF`。同年NBA2KW指南[SRC-0079]提供4大组/多个徽章解释、在**MyPLAYER**中按属性与身高解锁的条件：**MyPLAYER的徽章点获取方法不能直接搬成MyLEAGUE历史球员自然成长或导师升级的确切公式**。R03已有导师关系结构与玩家报告的自然徽章转移；R04-A只建立字段家族与将来比对方法。

一些代表性项目包括`Acrobat`、`Fearless Finisher`（终结）、`Catch & Shoot`、`Clutch Shooter`（投篮）、`Dimer`、`Floor General`（组织）、`Clamps`、`Rim Protector`（防守）；名称只说明使用领域，其适用条件、数值加成、是否当前版本真实存在须逐枚举认证。不同2K版本会有徽章改名、新增和取消，**不得把2K26的徽章树误标为2K22**。

### 5.2 人格与职业徽章必须单独保留

2K22同年ATD深度编辑社区会给球员分配`Alpha Dog`、`Friendly`、`Media Ringmaster`、`Finance Savvy`、`Extremely Confident`等Personality标签/徽章[SRC-0073/0080]，并区分技能徽章；社区球员资料有`Personality`单列。老版2K Wiki还有`Low Ego`、`High Work Ethic`、`Legendary Work Ethic`、`Keep It Real`、`Pat My Back`、`Unpredictable`等系列术语[SRC-0081]。**不同来源的标签不必然属于PC22同一枚举列表，更不证明每项参与合同报价、伤病或社交**。

球员可以因为人格徽章形成**个性假设**，但不应把它们简化成“一个徽章对应一条必然行为”。例如有`Finance Savvy`不意味着每次都拒绝降薪；`Alpha Dog`不意味着禁止其他主力控球；`Friendly`也不等于任何交易都同意。实际原生行为影响需要另看游戏说明/样本；**模型的外部长期价值取向独立存储**。R04-C专门调查人格徽章各项可见、合法值域和效果及与Loyalty/Financial Security/Play For Win的作用。

### 5.3 R04-A的徽章读取/权限契约

需要同时记录`badge_id, native_label, tier, group, source_snapshot, visibility, persistence, effect_evidence`。如果未来游戏自然成长、导师/退化导致新徽章，靠两期真实数据差分记录；若当前还没有可靠的徽章原生解码则`UNKNOWN`。项目**不允许普通经营直接写原始Badge等级给球员加强能力**，不能将`badge_slot`当外挂人格变量仓库。

### 5.4 R04-A增加全名录：80项Gameplay Badge与20个人格候选

已建立[PLAYER_BADGES_R04_A_REFERENCE.json](../catalogs/PLAYER_BADGES_R04_A_REFERENCE.json)作为**非原生ID的可检索名单**。根据2K22社区独立整理的徽章页[SRC-0082]，列出**Finishing 20、Defense/Rebounding 20、Playmaking 20、Shooting 20，共80个名称**；另外按当年ATD名单作者的真实2K22人物标签与旧NBA2K人格术语整理**20个人格徽章候选**。名单不是把20项人格全部冒充已认证PC22菜单，也不是对其原生编号的猜测。

- 全名录存`badge_label/category/2K22_source/visibility/known_native_id/status`，所有`native_2k22_pc_player_id=null`，没有PC原生内存归属就不会生成Badge执行命令；
- 同版2K22玩家、名单作者对球员Gameplay徽章和人格徽章具体组合给出了独立样例[SRC-0080]，但某些Community属性与总徽章数、版本混用的风险持续保留；
- 在R04-C逐个调查人格、契约/自我定位及NPC行为效果；在R04-D补完整原生Badge位置、具体角色权限与自然更新来源；不从`low ego`或`high work ethic`直接定义球员人生剧本。

## 6. 按字段性质给未来角色“能做什么”，而不是“应该怎么做”

| 资料/变化 | 球员的自主提议 | Coach可能的独立意见 | GM可能的独立意见 | Media可报道边界 |
|---|---|---|---|---|
| Vitals/合同/选秀与岁数 | 定义个人身份、表达长期职业阶段和目的地 | 对角色、状态、经验与战术定位持不同看法 | 依合法名单/合同评估球队方向 | 可以报道有来源的公开身高、选秀和合同；不得伪造内幕 |
| 各项篮球属性 | 请求训练某方向、接受角色转换、拒绝打法变更 | 按进攻/防守要求重新分工，也可以不听球员的 | 提供资源、交易、选秀和续约选择 | 只能对确实公开的能力评级/真实比赛表现发表评论 |
| 耐久/伤病 | 愿意保护身体、愿冒伤病风险，争取医疗选择 | 冲争冠窗口或给球员恢复机会 | 聘训练师、改变阵容、保护薪资资产 | 不把私有健康敏感数据/传闻冒充游戏公布的事实 |
| Peak/成长区间 | 优先长期发展、争取训练/出场，也可能放弃高强度 | 教练可以保守不用新秀 | 球队可以提长期合同或交易，即使误判未来 | 允许公开预测，但不阅读GM已遮蔽Potential |
| 技能/人格徽章 | 提出学习导师、改变风格、坚持角色身份 | 根据现有徽章安排战术，也可否决 | 讨论合同/人员适配 | 能讲述真实勋章与比赛事件，不自行给徽章 |
| 外部职业目标与关系 | 追求冠军/出场/金钱/城市生活/忠诚甚至拒绝条件 | 维护体系、在谈判中退让或坚持 | 协商合同/人员/建队，可能拒绝巨星额外条件 | 报道有来源的公开立场及明确标记的传闻 |

**模型保留选错的自由**：球员可为了名声或家庭地点选择损失总冠军概率；GM可误判天赋；教练可以坚持非最优打法；媒体可能批评错误但须区分`FACT`与`INFERENCE`。需要明确谈判与隐私：`ROLE_GOAL/ROLE_BELIEF/ROLE_PROMISE`不是2K原生真实数值，不能擅改Potential/Badges/人物身份或赛季事件来做涌现。

## 7. 重要技术与安全检查点

1. **只读可见 ≠ 可改**：用户在游戏Edit Player里能动原始Ratings/Vitals，不等于本项目给GM经营授权。用户历史线重力的个别能力变动是独立特例，每次需明确批准。本轮仅网页资料与GitHub文字/机读索引。
2. **已采源 ≠ 完整**：PLAYER profile的55个attr、17个contract是项目当前字段清单；游戏还有年龄/脸型/球员主宰/动作/全部倾向/人格/导师等其它模块，不按55或72就宣称该人物所有字段已捕捉。
3. **Potential去泄漏**：GM公开值1是人为遮蔽，禁止作为“Potential=1”事实让球员/媒体判断，尤其在1984–2020历史选秀里不能泄露真实未来。
4. **真实伤病vs耐久**：16项耐久不是16个正在发生的伤病；当前伤病起止依R03-G02真实来源，若无数据只`UNKNOWN`。
5. **成长不强制**：既有峰值/潜力/训练/年龄/属性都是决定自然成长的候选相互作用。没有引擎回归就不写增益率或“到30岁必退化X点”。
6. **外部状态独立**：不以名字、FaceID、Intangibles、真实Contract Preferences或闲置字节承载人格记忆。角色人物的自主目标和谈判记录未来须自己的持久表，不覆盖可能继续参加游戏模拟的Native。
7. **R04单轮边界**：人格徽章全条目/真实效应、所有倾向、个人合约偏好及各种球员与GM互动不在R04-A一次说完；分别由R04-B/C/D进行源级研究与知识目录扩充，不用审核机制阻塞下一研究轮。

## 8. 本批交付与下一窗口R04-B研究入口

**R04-A新研究**：球员职业身份/真实身份键来源、已注册**39项非耐久属性和16项部位耐久**、额外17项合同子字段的存在、PS5 MyNBA Boom/Bust与Peak年龄、四大Gameplay Badge组和人格徽章家族、自然成长反馈与游戏原生真值/角色自主记忆的隔离。以[SRC-0072..0081](../SOURCES.md)支持，**没有实机访问/玩家数据库读取**。

**R04-B下一步**：
1. 从GitHub读取本K03/K12、[R04任务书](../../development_tasks/DEV29_R04_PLAYER_FULL_PROFILE_AND_AGENCY_RESEARCH_SPEC_V1.md)、[player.json](../../../config/state_io_native/player.json)、已知K04教练与Book、[R03健康攻略](K06_TRAINING_HEALTH_GROWTH.md)和[字段目录](../catalogs/PLAYER_FIELD_AND_RIGHTS_MATRIX.json)。
2. 研究全**99个原生倾向byte**里已命名的48个与51个`UNKNOWN`，对照同版实机菜单/公开ATD/OS战术作者列表扩展到所有可见倾向类别，提供**英/中文释义、合法值、作用场景和冲突**。**项目现有命名48个不是游戏全量倾向，真实可见全表可更多**。不得未证raw与名字就启用写入。
3. 深入四个有序PlayTypes、Play Initiator、Touches、Shot IQ/Play Discipline、实际Gameplan/Coach和Freelance/Book，以及3D比赛和快Sim差别。角色有提议/拒绝权，实际本机倾向更改必须在许可范围与玩家审批下。
4. R04-C再专项研究全部Personality徽章、`Play for Win/Financial Security/Loyalty`、情绪、媒体与人物价值，R04-D完成完整字段权利图谱；**本轮没有创建任何Agent**。

**权威进度**：`R04_A_RESEARCH_PUBLISHED_WITH_FIELD_GAPS`，下一轮为`R04_B_TENDENCIES_PLAYSTYLE_RESEARCH`，尚未启动。DEV29的发布资料不代表当前player_pool里所有字段真实存在或允许写入。


---

# DEV29 R04-B — 球员行为倾向、PlayTypes、发起权与实际3D/Sim选择机制（2026-10-21）

> **阶段状态：`R04_B_RESEARCH_PUBLISHED_WITH_BEHAVIOR_GAPS`。** 继续遵守V3：游戏原料用于未来角色自主选择，而不是GM强制每人选择一条“最优倾向”。**新[99字节原生目录＋99条独立同版导出倾向目录](../catalogs/R04B_TENDENCY_PLAYSTYLE_RESEARCH_V1.json)**，源码和来源见[SOURCES](../SOURCES.md) SRC-0083..0090，核心既有来源SRC-0031/0032、SRC-0072、K04。不采集游戏、不调能力、不生成任何执行动作。

## 9. 倾向（Tendency）究竟是什么：能力与频率选择不能混为一谈

如果球员的`3pt_shot`属性很高但`Spot Up 3PT`和`Off Screen 3PT`倾向很低，游戏可以让他**具备命中能力而较少主动选择该动作**；相反极高出手倾向、低命中属性也不保证真实每场投进球。倾向描述某种处境中AI**更愿意考虑的行动**，还受球队战术与回合情境影响；它不是实际犯规/出手/运球次数，更不是“玩家人格强制值”。

完整决策框架按现有K04分为：

`阵容角色/真实属性/徽章` → `教练POE、RunPlayTendency、ACE、Freelance` → `本队Playbook的适用战术候选` → `球员四个有序PlayTypes/Initiator` → `攻防情境中的某个Tendency候选` → `游戏3D执行或FastSim` → `比赛/事件的真实反馈`。

**顺序只是因果检查框架，不是经反编译认证的程序调用栈。** 即使技术上能写一个合法的Tendency字节，也不保证2K CPU本场从该点做动作；尤其CPU自动换阵、ACE动态战术和模拟器可能各用不同权重。球员提出训练/打法改变与GM支持的实际原生写入必须分离。

## 10. 当前真正掌握的48项倾向、51项UNKNOWN与独立导出的99种外部标签

### 10.1 本项目原生结构的事实和合法性

- `src/gm_state_io/registry.py`针对`PLAYER[0x458..0x4BA]`建立连续**99个1-byte槽**，技术字典范围`raw_range=[0,100]`。
- `config/state_io_native/player.json`的`TENDENCY_OFFSETS`精确命名**48个offset**，其余**51个`RAW_0x...`仅能保留未知身份**，`UNKNOWN_RAW_BYTE`不因本章发现相似英文就转成可写。
- Registry对48项设置`writable=true`，这是**原生动作候选的技术标志**，不等于普通GM本轮获得统一编辑球员个人偏好的许可。任何将来动作还需要字段当前批次与人员身份、球员独立同意/不同意、原项目允许的类型、**真实玩家批准**、游戏写后回读；51项不写。
- **48/51的计数是已登记的*字节*，而不是游戏可见倾向菜单数**：UI可能有更广的对象、不同编码、跨页或隐藏字段；不因99这个数字碰巧相同就把两份目录逐行对齐。

### 10.2 48项已命名原生字段完整概览（每项精确字节见JSON）

| 游戏情境 | 全部当前已命名字段（原生英文与篮球语义） |
|---|---|
| 总出手与篮下终结（14项） | `SHOT_TENDENCY`总出手候选；`DRIVING_LAYUP_TENDENCY`突破上篮；`STANDING_DUNK_TENDENCY`原地扣篮；`DRIVING_DUNK_TENDENCY`突破扣篮；`FLASHY_DUNK_TENDENCY`花式扣篮；`ALLEY_OOP_TENDENCY`空接终结；`PUTBACK_TENDENCY`补篮；`CRASH_TENDENCY`冲抢进攻篮板；`SPIN_LAYUP_TENDENCY`转身上篮；`HOP_STEP_LAYUP_TENDENCY`跳步；`EURO_STEP_LAYUP_TENDENCY`欧洲步；`FLOATER_TENDENCY`抛投；`STEP_THROUGH_SHOT_TENDENCY`跨步晃后出手；`SHOT_UNDER_BASKET_TENDENCY`篮框下出手 |
| 距离和投篮动作（15项） | `SHOT_CLOSE_TENDENCY`近距离；`SHOT_MID_RANGE_TENDENCY`中投；`SPOT_UP_SHOT_MID_RANGE`中投定点接球；`OFF_SCREEN_SHOT_MID_RANGE`绕掩护中投；`SHOT_THREE_TENDENCY`三分；`SPOT_UP_SHOT_THREE`定点三分；`OFF_SCREEN_SHOT_THREE`绕掩护三分；`CONTESTED_JUMPER_THREE`受干扰三分；`CONTESTED_JUMPER_MID_RANGE`受干扰中投；`STEPBACK_JUMPER_THREE`后撤三分；`STEPBACK_JUMPER_MID_RANGE`后撤中投；`SPIN_JUMPER_TENDENCY`转身跳投；`TRANSITION_PULL_UP_THREE`转换追身三分；`DRIVE_PULL_UP_THREE`突破急停三分；`DRIVE_PULL_UP_MID_RANGE`突破急停中投 |
| 持球、球权与战术角色（10项） | `DRIVE_TENDENCY`突破；`SPOT_UP_DRIVE_TENDENCY`定点后攻框；`OFF_SCREEN_DRIVE_TENDENCY`绕掩护后突破；`ATTACK_STRONG_ON_DRIVE`强硬攻框；`DISH_TO_OPEN_MAN_TENDENCY`分空位；`TOUCHES_TENDENCY`球权接触倾向；`POST_UP_TENDENCY`低/高位背打意愿；`ROLL_VS_POP_TENDENCY`挡拆顺下/外弹取舍；`TRANSITION_SPOT_UP`快攻中拉开接球；`PLAY_DISCIPLINE_TENDENCY`战术纪律/是否依从动作的候选 |
| 传球与防守（9项） | `FLASHY_PASS_TENDENCY`花式传球；`ALLEY_OOP_PASS_TENDENCY`空接传球；`PASS_INTERCEPTION_TENDENCY`预判传球路线；`TAKE_CHARGE_TENDENCY`造进攻犯规；`ON_BALL_STEAL_TENDENCY`持球掏抢；`CONTEST_SHOT_TENDENCY`干扰出手；`BLOCK_SHOT_TENDENCY`封盖尝试；`FOUL_TENDENCY`犯规；`HARD_FOUL_TENDENCY`强硬犯规 |

**校正与数量提示**：分组只是篮球分类而非Memory连续分区；**精确48项 =14项篮下终结 + 15项中远距离投篮 + 10项持球/球权 + 9项传球/防守。** 实际原生偏移按JSON中唯一offset定位，不依赖段落顺序。。全部字段从`player.json`直接生成机器目录，未用文字推测新的偏移。**篮球解释只是一种合理使用语义，不是固定概率函数。**

### 10.3 2K22原始导出页面提供的另外99个“有名字的可见数据”——不与原生Byte强配

[SRC-0083]是第三方2kAuction明确标记`NBA2K22 v91 / Sep 10, 2021`的历史球员快照，展示包括`### Shot`、`### Drive / Pass`、`### Defense`、`### Other tendencies`。经过逐项抄录、独立编目，当前共：

| 同版导出分组 | 已有可见英文标签数 | 典型本仓库缺名但导出有名的**候选概念** |
|---|---:|---|
| Shot（投篮+背身） | 35 | Use Glass打板、Post Shimmy/Face Up/Back Down/Aggressive Backdown、Post Hook Left/Right、Post Fade Left/Right、Up and Under、Post Stepback、Drop Step等 |
| Drive / Pass（突破、三威胁、持球、传球、单打） | 43 | Drive Right、TT Pump Fake/Jab Step/Idle/Shoot、Setup Sizeup/Hesitation/No Setup、Driving Crossover/Spin/Stepback/Half Spin/Double Cross/Behind Back/Hesi/In-and-Out/No Move、ISO vs Elite/Good/Average/Poor |
| Defense（防守） | 7 | Pass Interception、Take Charge、On-Ball Steal、Contest Shot、Block Shot、Foul、Hard Foul |
| Other tendencies（存档导出特殊区域数据） | 14 | 三分区域5档、近框3档、中投5档及篮下区域候选；例如`shot 3pt left center t` |
| **总计** | **99** | **99是该第三方导出页面的条目数，不是对`PLAYER[0x458..0x4BA]`99字节一一对应的证明** |

这是一项**比只看48个已命名字段更丰富的研究发现**：第三方同版球员资料明确给出了长串具有篮球含义的**三威胁与持球连续动作、背身左右方向、按对手防守等级的单打倾向、不同投篮区域**等可用原料。未来球员可以有偏爱右路、依赖后撤步、愿意分球、不想承担强硬犯规等风格选择，但**不能在本轮先把这些候选名称强行填入51个UNKNOWN的raw bytes**。即使同版网站输出某个具体球员的数字，仍只是第三方历史快照，与本用户游戏和未来2000年代历史选秀世界线无关。

[机读目录](../catalogs/R04B_TENDENCY_PLAYSTYLE_RESEARCH_V1.json)将**99个原生slot**与**99个外部导出label**分别保存、来源和对象状态独立，原生已命名项有实际Offset，外部标签的`native_offset=null`，不会制造错误的一对一。

## 11. AI出手最关键的三种混淆：Touches、Shot与Play Discipline

### 11.1 同是2K22一手测试，也存在相互矛盾的解释

| 同时代观点 | 来源 | 对GM、Coach、Player真正意味着什么 |
|---|---|---|
| `Touches`主要影响没有执行固定战术的**Freelance接触球权**，教练Run Plays高时战术目标更多由教练POE、PlayTypes、Book确定 | 2021-09 jimbo3772；K04已登记SRC-0031，[SRC-0085]带完整上下文 | **合理可检验假说**，不是唯一正确函数 |
| 对全队平均降低Touches，可让Tatum/Brown之外角色得到更多进攻机会，电脑出手分配更丰富 | 2021-09 tcnumba10，同帖[SRC-0085] | **个人体验**；不能让所有球员都改50并宣称已获球员同意 |
| `Freelance Shot`/总体`Shot`主要用于模拟数据，3D投篮更多由Spot-Up/Off-Screen/Stepback/Drive Pull-Up等具体动作决定 | 2021-11 Sheitan、Evtnj直接讨论[SRC-0084] | 可能存在**快Sim专用或主要效果**，但没有官方引擎证明其对3D完全为0 |
| 2K22比赛里降低最高`Shot Tendency`后，CPU阵地出手分配改善；但别的用户改后仍只给某两个后卫叫战术 | 2021-10分歧个案[SRC-0032/0085] | **总体出手倾向可能间接作用**，不同试验方法和球队配置不能合成万能法则 |
| 老NBA2K系列中，总`Shot`主要影响Sim，临场会考虑位置分布、Playbook和角色优先级 | 2012/2018 OS不同玩家[SRC-0089/0090] | 仅**KNOWN_IN_SERIES**，不能拿老版玩家的数学式替PC22确定算法 |

**研究必须保留的独立数据维度**：`shot_in_sim`、`shot_in_cpu_vs_cpu_3D`、`shot_in_user_vs_cpu_3D`以及`team_runplays`、`touches`、`shot_tendency`、`play_discipline`、`play_type_order`、`book_compatibility`。不把任何一项直接命名“真实球权使用率”或“每100回合的绝对出手概率”。

### 11.2 为什么一种球员会在快Sim得分高、3D却几乎不持球？

四种可验证机制层——不是保证都已发生：
1. 快Sim可能用总体Shot/位置投篮倾向来分配总体FGA，3D更依赖球场位置、具体动作与球的流动；社区对这一点有不同意见。
2. 高频Run Plays、POE核心偏好、球队的有效Playbook CRC可能将动作分配给另外的球员；某前锋如果4个PlayTypes没有在本队Book里匹配的类别，可以有极高射术却没有专门为他叫的进攻战术。
3. 某人`Play Discipline`、单打倾向可能导致或抑制自行提前终结，但作用方向和游戏AI的具体状态转移尚不知；也可能因为防守换防、赛程或个人技能等别的因素无法执行。
4. 当且仅当有真实GameID、各球员出场、FGA/3PA、所跑回合、Playbook与当前coach设置，才能对“为什么没参与”形成有事实约束的解释；若这些数据没有捕获，就只是角色自己的**信念假说**。

## 12. PlayTypes四槽 + Initiator一位：不是五个独立战术或教练全权控制

本项目Registry使用：
- `playtype.slot1..4`：从`PLAYER[0x168]`至`0x169`的4个**半字节（4bit）**，有顺序；每项0..15。**四槽有序的事实可认证，1号总比2号多被调用多少次仍UNKNOWN**。
- `playtype.initiator`：`PLAYER[0x16A]`中`start_bit=2,width=1`，布尔原生候选，表示是否具备Play Initiator身份；*候选描述不等于此布尔值使球员固定变成持球后卫*。
- 16个项目enum逐一是：`None(0)`、`Isolation(1)`、`Isolation Point(2)`、`Isolation Wing(3)`、`P&R Ball Handler(4)`、`P&R Point(5)`、`P&R Wing(6)`、`P&R Roll Man(7)`、`Post Up Low(8)`、`Post Up High(9)`、`Guard Post Up(10)`、`Cutter(11)`、`Handoff Receiver(12)`、`Handoff Passer(13)`、`Mid Range(14)`、`3 PT(15)`。

要避免三个错误映射：
- `player.4 PlayTypes`不等于`球队Book里68条CRC`，也不等于`12类Play目录`。一条有P&R类型的CRC可以有多个发起/终结角色，先查实际类型匹配才谈战术频率。
- `playtype.initiator=true`不等于`Touches=100`，更不等于教练`RunPlayTendency=100`；**角色可以是发起人，却在球队book没有对应球员目标动作**。
- 2021年2K22导出资料同时列出了`Play initiator = Yes/No`与4个类型，例如Trae Young标Yes、Tatum标No，各自仍有4个战术类型[SRC-0086/0087]。**只作为同版外部历史快照的字段独立性佐证**，不代表本项目当前球员值，也不能从字面将外站的“Three-point screens”与本项目`3 PT(15)`宣布为同一原生enum。

### 12.1 Roll vs Pop与P&R Roll Man不同：球员可以想要另一种角色

`P&R Roll Man`是**球员战术类别**，`ROLL_VS_POP_TENDENCY`是原生Player Tendency中**掩护后顺下/外弹选择的倾向**，`FIST...`则是球队Book具体CRC；三个对象并不互相替代。一个可以外弹但PlayTypes/Book没有适配动作的内线，教练不会因为修改一个`ROLL_VS_POP`就自然创造出所有适合他的三分战术。未来中锋球员可以**要求**扮演射手型内线，教练可反对，GM可补外线教练体系或不同人员；技能成长仍由游戏自身决定、不能因为人物立志转型直接增加三分能力。

## 13. 三威胁、持球运球、单打等级与区域投篮：新增行动原料的具体篮球意义

同版2kAuction快照列出以下在项目48个命名字段**尚未完整涵盖**的行为候选[SRC-0083]：

- **三威胁`TT Pump Fake / Jab Step / Shoot / Idle`**：拿球后假投、试探步、就地投、暂不发动。它们可以塑造谨慎侧翼、喜欢试探的得分手与快速决策球员，但这些名字**不等于已知原生raw位置**。
- **持球启动`Setup Sizeup / Hesitation / No Setup`**与**突破动作`Driving Crossover/Spin/Step Back/Half Spin/Double Cross/Behind Back/Hesi/In-and-Out/No Driving Move`**：拿球后用何种节奏摆脱守方。球员可能偏爱持球创造，教练可能觉得拖慢进攻；外部模型可以形成不同价值判断，而不修改运控属性。
- **单打对手质量`vs Elite / Good / Average / Poor`**：对不同防守等级选择单打的候选，这是非常适合构成**“球员遇到怎样的防守人愿不愿独立处理”**的原料；具体游戏采用什么防守评价阈值/哪一项属性、是否直接参与3D仍UNKNOWN。
- **背身动作/方向`Post Hook Left/Right / Fade Left/Right / Face Up / Aggressive Backdown / Drop Step`**：细分左/右路、转身脚步和面对不同体型防守者的自主动手段。
- **投篮落点**：`Other tendencies`的三分5区、中投5区、近框3区和篮下条目，是研究球员更偏爱左底角或弧顶接球的潜在输入，但不能等同于R01真实Shot Chart，**导出倾向只是预设、真实出手热区必须看场上数据**。
- **外观动作包/Animations**仍是另一家族：球员的实际签名运球包、投篮动作、扣篮包在导出页单独存在；不能用有`Driving Step Back`倾向就推断一定拥有指定的Curry动画或跳投速度。球员人格可以珍视个人标志性动作，但是否允许修改外观动作需项目另行审核。

**关于动作倾向的0/99**：同年Sheitan认为极端值让电脑选择过于机械，提出按分位数分配人物行为[SRC-0084]。这属于**社区名单设计者的一种建模哲学**，不是游戏官方0/99是否有概率绝对性的数学证明。未来自由角色系统可以选择极端专精、也允许不合理偏好；DEV29不能把“建议避免99”变成强制球员人格趋同。

## 14. 同样的Tendency在三种执行方式下如何判定结果

| 游戏执行方式 | 实际可研究的数据 | 什么证据不能复用 | 对多角色的意义 |
|---|---|---|---|
| `FAST_SIM` 快速模拟 | 真实赛季FGA/3PA/回合、分钟、出场和世界滑块（若已采） | 不把UI里具体后撤步出手偏好等同已被模拟器逐帧使用 | 球员对自己的数据表现可能不满，Coach/GM对战略影响的解释可能互相争执 |
| `CPU_VS_CPU_RENDERED` CPU观战 | 同一场具体持球者、动作时点、传球路径、实际所跑战术的录像/追踪，真实Box | 不把某人外站历史“Shot=90”当本局主动球权 | 教练可能观察到球员偏离战术、球员反驳是防守改变了选择 |
| `USER_VS_CPU_RENDERED` 玩家打AI | AI一方真实CPU行为、人物移动、手动/自动Playcalling区分 | 不能用玩家直接手控的投篮当角色原生AI自主决定 | 球员独立偏好只能研究AI控制的一侧，用户操控需另标 |
| `COACH_MENU_ONLY` 静态/临场菜单 | 当前coach/Playtype/倾向可选读数、数据批次 | **不当作真正执行过的战术或球权** | 角色有了可选择的对象，但没有真实结果前需提出更多信息请求 |

任何“改变Touches会使A每场少投5次”的定量结论，必须同保存、版本、阵容、教练、Book、比赛模式、赛程/上场、球员已批准意向一致做多次对比；本轮没有此类验证，所以数值效应保持`UNQUANTIFIED`。**角色可以做错决定而后悔，但世界日志不能伪造已经发生的比赛事件。**

## 15. 交给角色的真实选择菜单，而不是全联盟统一倾向处方

| 情境 | 可真实观察的状态（须来源/权限） | Player自由选择 | Coach、GM可独立回答 | Media能够发布的事实及争议 |
|---|---|---|---|---|
| 高使用率核心与低参与替补 | 真实FGA、分钟、PlayTypes、Book和Coach现值、批次 | 维持单打、要求更多/更少持球、改无球动作、拒绝团队期望 | Coach可支持单核、要求分享球；GM可增援或拒绝；同意之外不得随意改普通倾向 | 公开真实出手与胜负；不能把未知内心“自私”当原生客观属性 |
| 中锋希望转型外弹 | 3PT属性/真实3PA，P&R Roll Man类别、Roll vs Pop、训练计划 | 要求Outside训练/改战术角色或保持内线打法 | Coach提出战术书和空间要求；GM有成本约束 | 评论外弹选择与球队效率，不能宣布3PT能力自动上涨 |
| 喜欢高风险抢断的球员 | `ON_BALL_STEAL`、`FOUL`、真实犯规/断球（有批次才可用） | 维持积极压迫、同意减少掏抢、或拒绝教练要求 | 教练权衡犯规/防守体系；GM可换防守人员 | 不能根据一个倾向值报道“球员已故意伤害对手” |
| 战术纪律低的天赋球员 | Play Discipline、Touches、真实战术执行片段（缺失则UNKNOWN） | 想保持创造空间、接受教练条件、在不满时要求交易 | 教练能争论自由与体系的边界；GM可支援或换教练 | 只能就公开赛后采访/比赛事实发表评论 |
| 侧翼不想改变投篮动作 | 签名动画包与实际shot attempt（如果已采） | 拒绝替换动作、要求个人训练而非换习惯 | 教练可调整围绕其动作的战术，也可否决球权诉求 | 个体风格与表现可公开评价，私有承诺只能在本人允许后披露 |

**ROLES与权限**：未来`Player.PROPOSE/COUNTER/REJECT`和`Coach.PROPOSE/REJECT`只是可供人格系统推理的行为词汇，**不是NBA2K22内置球员同意API**。球员倾向本身可能还影响模拟比赛，所以**不允许把这些仍有原生效果的raw bytes重新用来保存秘密人格、忠诚或承诺**。普通球员能力/Potential/徽章仍不可编辑；倾向/PlayTypes若未来允许经两角色协商更新，仍须**真实玩家批准**及现有合法原生执行边界。

## 16. R04-B本轮结论与R04-C直接研究断点

**本轮已发表**：
- 真实99个原生倾向byte：48已经命名，51未知保留只读；
- 另外99项**来自NBA2K22 2021快照的具名倾向标签**，完整分组/排序和字段来源独立入库，**不按“99=99”擅自赋raw offset**；
- 个人四有序PlayTypes（原生0..15）与1 bit Initiator、12战术类别、球队本队Playbook、Coach/ACE/Run Plays相互关系；
- 同年玩家对Touches、Shot、Play Discipline、3D vs Fast Sim的冲突实测及不承诺公式的解释；
- 三威胁/持球、单打对位、背身左右方向、Shot区域分布等未完整映射的候选行为；
- 四类人物能观察、提议、拒绝、长期学习什么，保持隐私和玩家原生写入权限。

**R04-B仍未完成的对象**：目标PC22无模组完整Edit Player→Tendencies的**具体像素顺序及作用类型**、99外站字段到99原生byte的一对一对照、所有动作具体CPU触发概率、命中/模拟器的区分、人员当期真实动态读值、换教练/换Book后自动调用的可重复案例。这些全部`UNKNOWN`、必要时未来DEV28定向只读；**不因没视频就停止后续R04-C**。

**R04-C下一任务**：独立深入Player Agency：`Loyalty/Play For Win/Financial Security`、全部真正存在的人格徽章、士气/合同/球队角色/明星议价、医疗和训练自主权；区分2K原生意愿（如果存在且有效）与外部人物永久记忆、职业目标、反报价、拒绝与媒体叙事。R04-D再综合完整权限图谱及R05市场接口。**后续研究不由本轮自动启动，不由DEV29执行独立审核**。

### R04-B原始来源编号与恢复码（供下一轮直接检索）

本轮研究事实的**逐项来源键**如下，详情及平台/模式限制均在[SOURCES](../SOURCES.md)：
- **SRC-0083**：NBA2K22 2021历史人物导出的99个具名倾向标签（独立于Native 99 bytes）。
- **SRC-0084**：Sheitan/Evtnj讨论三威胁、Shot/Freelance与模拟/3D差别。
- **SRC-0085**：2021年不同2K22玩家对Touches/Shot/教练叫战术产生矛盾结论。
- **SRC-0086**：同版Trae Young的Initiator=Yes及四PlayTypes归档字段。
- **SRC-0087**：同版Tatum的Initiator=No但仍有四PlayTypes归档字段。
- **SRC-0088**：同版MyLEAGUE玩家的个人倾向编辑与全球模拟滑块各自独立。
- **SRC-0089**：2012年旧系列总体Shot作用机制争论，仅KNOWN_IN_SERIES。
- **SRC-0090**：2021年的动作倾向编辑建议与部分2K19经验必须分开。

**正式断点**：`R04_B_RESEARCH_PUBLISHED_WITH_BEHAVIOR_GAPS`；**下一轮`R04_C_PLAYER_MOTIVATIONS_PERSONALITY_RESEARCH`，尚未启动**。下一轮调查人格徽章、Loyalty/Financial Security/Play for Win、情绪、球队/球员谈判与媒体知情范围；**DEV29只研究和发布原料，不担任独立审核、不开发Agent或启动原生写入**。
