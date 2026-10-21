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
