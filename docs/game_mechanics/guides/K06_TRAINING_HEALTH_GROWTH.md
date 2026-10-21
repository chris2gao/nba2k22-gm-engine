# K06 — NBA2K22终极联盟训练、疲劳、伤病与自然成长：面向GM/教练/球员/媒体的机制与选择手册

> **DEV29 V3 / R03-A（2026-10-21）**。目标版本：NBA2K22 **PC本世代原版、离线MyLEAGUE**。2K22 PS4/Xbox One、2K22 PS5/Xbox Series MyNBA、2K20–21/23旧新系列单独标平台，不偷换为PC22菜单。玩家能够设置训练，不意味着本项目已采到疲劳、不意味着比赛引擎会按预期加能力；读到内存布局也不等于当前存档已发布可信值。
>
> 研究任务是**提供自由行动原料**，不制定训练处方、不开发Agent、不改球员属性、不运行游戏。事实与能力核查以[DEV14交接](../../development_reviews/DEV14_TO_M3_HANDOFF.md)、[原生训练目录](../../../config/state_io_native/training.json)、[Registry](../../../src/gm_state_io/registry.py)、[GM训练能力审计](../../research/NBA2K22_MYLEAGUE_GM_CAPABILITY_GAP_AND_MONTHLY_TRAINING_V1.md)和[DEV16](../../development_tasks/DEV_20261019_16_M3_NATIVE_COVERAGE_AND_GM_TRAINING_PLAYBOOK_INTEGRATION_V1.md)为准。外部来源SRC-0049..0059见[证据库](../SOURCES.md)。

## 0. 本领域最容易犯的五个混淆

1. **训练模板（player_type）不是球员比赛PlayTypes**。前者是培养方向的9类通用原生编码，后者是K04的4个有序比赛战术角色槽（0..15）；同叫“类型”，不同原生对象。
2. **训练强度≠总身体负荷**。比赛分钟、背靠背、休息日、训练安排可能共同影响负担。2K14/15开发人员曾给出计算解释[ SRC-0052 ]，不能无认证地说PC22仍用完全相同“两周公式”。
3. **记录了progressive_fatigue_history布局≠已经知道实时疲劳百分比**。当前注册/通用采集主要覆盖11个训练设置，历史区的编码、单位、窗口和游戏UI映射仍未验证。
4. **训练方向≠直接提升球员某个能力数值**。成长由2K引擎自然发生，且发展/衰退、潜力和模拟设置会影响观测；普通经营禁止直接改Ability/Potential/Badge。
5. **2K22次世代Prep Hub与PS5 MySTAFF不属于本项目PC MyLEAGUE已认证功能**。即便同属“2K22”，训练页的内容、教练自动规划和球员“自己决定降强度”等不能直接搬来作为PC22原生控制。

## 1. 本项目真正拥有什么：11个训练设置字段及其等级

**项目工程事实**：⟦src/gm_state_io/registry.py⟧已登记6个TEAM_TRAINING和5个PLAYER_TRAINING，⟦config/state_io_native/training.json⟧含原生位域布局和值域。DEV14已建立通用捕获/稀疏变更/回读机制，状态以具体执行版本和当前真实发布批次为准。**未在本轮执行采集/写入/实机持久性测试**；不能把Registry的⟦writable=true⟧说成所有球队本档当前已读到并获批准。

| 真实原生字段 | 已登记值域/表示 | 可供角色考虑的行为及边界 |
|---|---|---|
| ⟦training.team.home_intensity⟧ | ⟦0..5⟧原生强度：Rest/Very Low/Low/Medium/High/Very High | 主场训练力度候选；比赛主场前后如何应用未量化 |
| ⟦training.team.away_intensity⟧ | ⟦0..5⟧同上 | 客场训练力度；为何区分home/away尚未证明的引擎效果保持UNKNOWN |
| ⟦training.team.automate_intensity⟧ | 布尔0/1 | 是否让引擎自动管理强度；不能证明它会理解角色私人目标或总能防伤 |
| ⟦training.team.rest_before_b2b⟧ | 布尔0/1 | 背靠背之前休息候选；触发时点/例外待PC22 UI |
| ⟦training.team.rest_after_b2b⟧ | 布尔0/1 | 背靠背之后休息候选；不等同每天休息 |
| ⟦training.team.injury_recovery⟧ | 布尔0/1 | 球队恢复相关原生设置；不能用字段名推算加速康复天数 |
| ⟦training.player.position⟧ | 0 PG /1 SG/2 SF/3 PF/4 C/5 None | 属于训练位置模板身份，不是本球员实际上场位，也不是可任意更换位置的证明 |
| ⟦training.player.player_type⟧ | 0..8，9项训练原型，见§2 | 训练方向，不是比赛中的P&R/3PT PlayTypes |
| ⟦training.player.intensity⟧ | 0..5 | 个人力度；可与团队自动/override产生关系，覆盖优先级未知 |
| ⟦training.player.injury_recovery⟧ | 布尔0/1 | 个人康复侧设置，原生实际效果/伤员资格待证 |
| ⟦training.player.is_intensity_overriden⟧ | 布尔0/1 | 个人强度覆盖标记；不能直接从1推出所有比赛会按指定强度训练 |

⟦team_training.percentage_per_focus/profile_per_focus/points_per_subfocus/intensity_history⟧及球员⟦points/overall_history/attribute_value_history/progressive_fatigue_history/intensity_history⟧在原生目录中**有布局候选**；但这批字节的⟦source_status/current_value/单位/自然时间窗口⟧没有被本次认证为角色可读数据。导师⟦mentorship_manager⟧布局含导师/被指导者ID、持续时间、兼容性、徽章槽与进度；Registry仅登记⟦mentor.relationship⟧为⟦DISCOVERED⟧不可常规执行，不能借目录里出现⟦badges_array⟧就说我们已获得“导师自然传徽章”的当前进度。

**本项目过去的历史报告曾称训练尚未有执行接口**，那是旧时点；现行DEV14交接/Registry已经含11字段。反过来，**真实当前月/当前人物的实时疲劳/伤病并未因有11字段而自动被采集**。数据消费者要以实际⟦source_coverage⟧和batch确认。

## 2. 九个原生通用培养原型（TRAINING player_type）

| Raw | 英文原文 / 中文 | “期望方向”的篮球语言（目录说明，非具体属性增益证明） |
|---:|---|---|
| 0 | All-Around / 全能 | 不刻意只追一个得分技能，寻整体成长 |
| 1 | Two-Way / 攻防兼备 | 攻防两端的均衡职能 |
| 2 | Offensive / 进攻 | 得分、终结与进攻工具 |
| 3 | Defensive / 防守 | 单防、防守阅读、护筐等方向 |
| 4 | Athletic / 运动 | 速度、弹跳、力量等身体工具方向 |
| 5 | Rebounding / 篮板 | 篮板争抢与相关定位 |
| 6 | Playmaking / 组织 | 运控、传球、组织选择 |
| 7 | Outside / 外线 | 外线出手、中投等投射方向 |
| 8 | Inside / 内线 | 低位、近框终结、篮下对抗 |

**最重要的未证缺口**：玩家实际PC训练UI据此前项目记录存在“分位置的多套模板”，而目前Registry仅有**9种通用原型**和独立⟦position⟧。无法断定⟦PG/SG/SF/PF/C⟧每个UI模板如何与⟦(position,player_type)⟧配对，也不能声称所有位置都显示9项或10项。以后只读菜单/原生列表证实前，应将⟦EXACT_POSITION_TEMPLATE_MAPPING=UNKNOWN⟧标给角色。

一个希望改打射手的年轻中锋可能**请求**Outside训练，教练可能认为他优先发展护筐，GM可能希望培养有交易价值的投射能力。三种偏好允许冲突；**选Outside不保证一年后增加固定三分数值，更不代表可直接写三分Ability**。训练计划所代表的是拟投入方向，而不是兑现成功的承诺。

## 3. 团队训练、个人训练、比赛负荷：如何理解相互作用

### 3.1 机制关系与不确定性

从玩家选择自由看，至少有如下潜在相互作用：

- **球队训练强度/主客场与背靠背休息**：团队级负荷基线；为何home/away分别存两段是当前原生布局事实，具体每周时序并无PC22逐日UI已证。
- **个人训练原型/强度/覆盖标记**：个体培养方向与负担的候选；受比赛出场、年龄、训练后恢复以及伤病可用性影响。影响比例未认证。
- **自然比赛投入**：比赛由2K运行并产生真实赛程、分钟及健康事件；不是模型事先“选择训练会赢球”就保证出现。
- **训练和体能的关系**：身体疲劳可能影响之后比赛可用性与受伤风险；精确⟦dose→fatigue→injury⟧函数、随机参数、跨快速模拟与观战的差别均UNKNOWN。
- **教练和训练师**：PC本世代玩家已确认球队有训练师等可聘员工，员工能力对伤病预防/恢复/发展作用须独立认证；不把PS5新增“Sport Science/Medical MySTAFF”职位搬到PC22。

NBA2K14/15时期Visual Concepts AI工程师Leftos公开解释[ SRC-0052 ]：旧版训练⟦Overall Workload⟧不仅由Intensity确定，还考虑比赛日、练习日、休息日、上场分钟与Work Ethic；该帖描述投诉/承诺的滚动2周窗口，以及比赛日按“High”计负担。这是**开发人员的历史原始解释**，具有机制研究价值，但**并未证明同样窗口/换算在PC22存留**，也不自动赋予MyLEAGUE球员游戏内“训练协议拒绝”按钮。

### 3.2 年份/平台差异的关键事实

2K22 **PS5/Xbox Series MyNBA**官方新闻[ SRC-0049 ]确认⟦Prep Hub⟧、新版MySTAFF、团队和个体训练。2021年开发者Courtside文章在官方内容转载[ SRC-0050 ]描述：
- Prep Hub聚合下场对手、团队体系熟练度、训练与疲劳；
- Team Training可见未来3周安排、练习种类/强度/疲劳/受伤风险与当前伤员及Load Management情况；
- 教练会按自身风格自动生成团队计划；球员的负荷管理可让其在不利条件下自主选择低压力训练；高负荷会降低Game Fitness，作者称与比赛时精力/属性有关；
- Individual Training允许围绕目标原型发展，并显示疲劳、受伤风险和负荷管理。

这份文献极其适合V3将来“教练、球员拥有独立判断权”的世界设计，**但明确是次世代MyNBA！** 在本项目PC22默认只记录⟦NEXT_GEN_ANALOGUE_AGENT_BEHAVIOR⟧，不得写成PC原生已有⟦Prep Hub⟧或球员会自动拒绝练习。

2021-09 OS**2K22次世代MyNBA**玩家[ SRC-0051 ]报告三周训练日程在推进日期后出现错乱；作者提供两段视频URL，并表示每天只推进一天/每天纠正时暂能绕开。我们只核实**作者的文字说明和视频链接存在**，**没有审查视频具体帧/时间戳**；对PC本世代不构成BUG定论。2023-04另一玩家回顾2K22次世代的训练表错乱，称2K23已改善[ SRC-0057 ]，说明该历史问题有明确版本边界。

### 3.3 PC本世代/同代实际参考，而非偷用PS5菜单

本项目玩家此前直接确认：PC22 MyLEAGUE训练含**团队、个人、导师**概念，界面类似2K20；这项⟦PLAYER_CONFIRMED_OPERATIONAL_CONTEXT⟧比次世代MySTAFF更贴近目标，但不是每个枚举的完整图证。

2022-02 OS同年**PS4 MyLEAGUE**玩家[ SRC-0053 ]自述：给所有年轻人分配个人训练方向，许多人High/Very High，整个赛季以模拟方式推进，发展并没有达到他预期。其存档同时用了社区ATD roster和改变过的成长/衰退滑块，因此**不能单变量断言“Very High没有效果”**；但足以反驳“把强度拉满自然必成长”的错误规则。PS4属于本世代类比，不能认证PC确切值域。

旧版2K15论坛玩家[ SRC-0054/0055 ]清楚描述球队训练、按原型训练、个人Intensity、球员疲劳条和按技能单独训练的取舍。有玩家发现专练投篮会增加专长却使其它能力下滑，影响OVR；另有人用不同训练模板发展边缘球员。这是**旧版具体经验**，不等于PC22旧版的每项训练入口仍存在。2021年2K22次世代玩家甚至抱怨“以前逐项训练属性，2K22仅能选择presets”[ SRC-0056 ]，再次提醒项目不能未经核对地开放“逐属性训练百分比”。

## 4. 自然成长与统计反馈：真实需要怎样判断？

**把输入和结果分开**：

| 类型 | 事实字段或候选来源 | 有什么用 | 现阶段的真实限制 |
|---|---|---|---|
| 训练输入 | 当前⟦training.team.* / training.player.*⟧源真实已观察值与其生效日 | 教练/球员能知道自己已选择的训练计划 | 注册字段不代表本期Snapshot已有值；若missing要继续UNKNOWN |
| 比赛暴露 | 每场game_id、实际出场分钟、背靠背日期/主客、比赛类型 | 区分练太多和打太多的暴露量 | R01记录PC22逐场日志/赛程原生查询有缺口 |
| 生理状态 | 当前疲劳、Game Fitness、伤病部位/类型、预计恢复、健康上下限 | 球员是否希望保护身体与赛季竞技能力 | 历史Fatigue原生字节布局≠已解读有效**实时**疲劳；伤病目前可用发布来源不足 |
| 变化 | 赛前/赛后/下月真实属性、徽章、伤病、上场、复发事件 | 判断成长与损失，允许模型修正预期 | 必须来源相同的真实游戏存档，不能用潜力泄露、不可随意写能力作为实验 |
| 世界环境 | progression/regression sliders、injury sliders、simulation vs 3D | 解释同方案不同世界线为什么不同 | 与训练师、潜力、年龄、不同进度均混杂；不能直接归因 |
| 人格/谈判 | 球员私有训练目标、伤病风险承受、教练要求、GM资源边界、媒体公开争议 | 为未来多Agent提供意见冲突/自由决策空间 | 外部SQLite概念，**不是已读取的原生NPC思想或拒绝API** |

**数据比较质量要求**：必须至少存`save_id / source_batch_id / game_date / player_native_id / team_id / injury_status_source / training_source_status / actual_minutes_window / ability_snapshot_ids`；如果比赛不同赛程/不同难度/不同伤病随机性，不得从一次成长差值计算训练增益系数。OVR受位置/角色权重影响，**不能仅凭OVR升降断言所有底层属性都同步改变**；R04再研究全部属性和徽章明细。

本轮不是执行实验，因此**不存在真实某队本季训练成功率、康复提速天数和永久损伤概率**。

## 5. V3角色可见、可选、可拒绝、承担代价：给自主涌现而非最优控制

| 游戏原料 | GM能选择/担负什么 | Coach能选择/担负什么 | Player可提出/拒绝什么 | Media何时能报道 | 原生效果与外部状态分界 |
|---|---|---|---|---|---|
| 团队强度、背靠背休息 | 讨论球队赛季目标、风险与球队资源，不必亲自安排每个动作 | 可能主张训练文化、高强度或恢复优先；与GM争论 | 对个人承担过载或休息不足表示不满，要求改变 | 报道真正公开的训练和伤病信息，不能偷窥私有诉求 | 真实6个team字段是原生设置；教练坚持什么、球员是否不满要在外部世界建模 |
| 个人模板、Intensity与override | 提供培养资源和薪资/球队职责的交换条件 | 依据打法希望球员往指定角色发展，也可愿意放手 | 争取投射/组织/低位模板，选择争取上场或保护职业生涯、甚至拒绝球队方案 | 只有球员或队伍公开训练分歧才可写新闻 | 真实5个player字段可成受控操作；人格拒绝不是游戏字段 |
| 身体风险、伤病与恢复 | 重排阵容或签人、容忍比赛短期损失，也可提出交易 | 可能减少使用、改变战术负担，或坚持要赢关键战 | 可拒绝过度训练/要求休息，面对长期事业选择 | 可报道真实已知伤停，不把“怀疑带伤”冒充医疗诊断 | 伤病真实记录必须从游戏取；自述痛感/未来担忧属于外部角色内心 |
| 成长/退化与导师 | 是否长期培养、买入即战力、能否负担老将导师成本 | 可能愿意给年轻人机会，也可能保守弃用 | 追求某种打法、跟某位老将学习，也可拒绝导师安排 | 报道真实成长趋势、天赋评价要按可公开资料 | 徽章增长只能记录游戏自然事实；不能直接编辑徽章以制造“导师成效” |
| 不确定性与失败 | 一支球队可以为了当季总冠军忽视年轻球员成长 | 教练可以坚持低效练法、在赛季中反思或拒绝变化 | 球员可冒伤病风险赌地位，也可提前休息选择长期职业寿命 | 对失败作主观评价但必须承认资料缺口 | 不设全联盟一套强度最优表、不用固定阈值压制不同价值取向 |

未来的`CHOICE`、`COUNTER`、`REJECT`、`HOLD`仅是**外部角色行为的研究描述**，**不是立即能调用的游戏原生命令**。让球员具备个人训练自主权是系统愿景；是否允许某类计划真正改写原生训练字段，需满足**原生映射已认证、同批身份、人物/角色模拟同意和真人玩家批准**。一旦Coach、Player、GM利益冲突，不能在研究阶段替任何角色强制裁决。

### 5.1 一场自由的谈判可以怎样发生（不是必选剧情）

一名健康但出场少的新秀想多练三分；教练认为球队更需要防守；GM认为自己可能很快交易他。三人分别看到**同一人物当前真实训练类型/强度、比赛出场和公开伤病**，但对未来与风险有不同信念。球员要求Outside、教练反报价Two-Way、GM可提不同职责。任一方可拒绝；未来比赛或成长若被真正观测，各自仍可重新评价。**不能为了完成故事自动把球员三分能力调高**。

另一名带伤老将可以要求休息，即使教练想冲击季后赛。失去的比赛胜率机会和长期健康目标同时存在；在没有真实疲劳/伤病来源时，不能根据年龄制造一条“已发生伤病”新闻。

## 6. 本轮已证/未证/下一轮R03-B

| 目标 | 已有真实基础 | 当前缺口 | 下一轮最值钱的资料 |
|---|---|---|---|
| 11训练设置 | 真实Repo Registry的6team+5player，Native packed布局 | PC22具体中文UI、各强度/覆盖优先级、正式本批对象读数 | 本世代训练页截图、模板/强度的完整选项，按实际身份关联 |
| 通用9个Player训练原型 | training.json已命名0..8 | 各位置UI更细模板的精确映射与能力方向；分配后的UI持久性 | 位置分类与实际原生编码配对，不以“9=全部UI模板”推断 |
| 团队Training强度 | home/away/autointensity/b2b休息/injury_recovery在Registry | 总负荷时间窗口、强度对比赛/体力的量化效果 | PC同代真实菜单及已观测状态 |
| 个人健康/疲劳 | progressive_fatigue_history布局候选 | 当前疲劳值解码与单位、伤病及可用性未发布 | 只读原生验证/玩家已有UI，区分HISTORY_ONLY与CURRENT_VALUE |
| 导师与徽章 | native mentorship_manager布局候选，Mentor在Registry为DISCOVERED | 关系有效期、兼容性与徽章自然变化、是否可执行关系设置 | 真实2K22 PC导师菜单/徽章变化；不改原始Badge |
| 2K22次世代高级训练 | 官方明确有Prep Hub、3周计划、Load Management/球员降强度 | PC本世代是否存在及操作/智能安排**UNKNOWN** | 不外推；仅供未来教练/球员自主决策原料启发 |
| 生涯自然成长 | 游戏引擎负责，OS多时代玩家有不确定且冲突经验 | 真实变化窗口、比赛/训练/员工/潜力独立因果未证 | R03-B继续研究伤病模型、康复与不同模式、成长差分，R04负责全属性/徽章/耐久字段 |

**R03-A现正式发表；整个R03仍需R03-B**（身体状态/伤病/导师以及PC菜单证据），未来必要时R03-C最后有界UI/结案。下批按PROGRESS恢复，不重复本轮已研究的2K22官方次世代Prep Hub全文。R04仍是完整球员本人属性/全部耐久和Play for Win/Financial Security/Loyalty等合同人格专项；本章不取代它。

**执行边界**：只读GitHub和公开资料、出版研究。没有打开游戏、训练写入、伤病编辑、潜力泄漏、创建Agent或启动DEV28/Codex。凡未知仍明确UNKNOWN。

## 7. R03-A新增官方可读图证：2K22次世代不是PC22

**VIS-0009：官方Individual Training Focus截图**，见[官方新闻原图](https://cdn.prgloo.com/media/2858117e546348dbb3c016b7282e72c3.png?height=663&width=442)。本轮已经实际看过图中像素：上方`SKILL TRAINING FOCUS`，中间`POINT GUARD/SHOOTING GUARD/SMALL FORWARD/POWER FORWARD/CENTER`位置选择、`PLAYER TYPE`和`TRAINING COMPATIBILITY`两列，右侧有球员OVR。可见PG类型组列出了ALL-AROUND、TWO-WAY、OFFENSIVE、DEFENSIVE、ATHLETIC、REBOUNDING、PLAYMAKING、OUTSIDE SCORING、INSIDE SCORING等。**这是一张2K22官方明确属PS5/Xbox Series MyNBA的截图，不是PC22原版字段画面**。图中组合对我们定义`(position, visible_player_type, compatibility)`关系有实际参考价值，但不证明其UI顺序直接对应本机raw 0..8或训练成功率。

**VIS-0010：官方Training Schedule截图**，见[官方新闻原图](https://cdn.prgloo.com/media/eedbfc01c17a465eb26f5093c697ee8b.png?height=663&width=442)，本轮也实际查看像素：顶部`TRAINING SCHEDULE`与跨日期的多格日历，底部有`TEAM SYSTEM`、`TRAINING GOALS`、`TEAM OVERVIEW`三个信息区域，显示练习日与队伍状态的同屏联系。**这不意味着PC本世代有同样逐日练习排班UI**；具体截图像素较小，未逐项认证每个单格训练名/数值/动画，绝不复制为PC菜单完整值域。新闻页还有`MyNBA Prep Hub`图片链接，但本轮该媒体原图链接无法稳定加载，不把它升级为已检视像素的VIS。

两张官方原图具有实质视觉证据、也拥有严格平台边界。本研究仓库只保存链接和逐项核查文字，**没有上传或复制官方受版权保护的截图**。后续若得到PC22真正对应的训练页面，再按实际列与原生`training.json`对照，不强求版本看起来完全一样。
