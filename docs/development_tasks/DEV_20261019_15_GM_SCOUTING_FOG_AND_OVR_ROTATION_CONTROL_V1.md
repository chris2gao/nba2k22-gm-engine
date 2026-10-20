# DEV15 — GM潜力信息遮蔽 + Intangibles综评补偿引导轮换（拆成A/B两阶段）

**2026-10-19 · GM信息规则：Web Development · 开发：Codex（M0/M3/DEV14只读接口与业务合同）+ Antigravity（原生Intangibles字段实机定位/持久化及效果取证）· 游戏更改批准：用户。**

**优先级/依赖**：DEV15-A潜力遮蔽=**P0，GM V4任何真实球员评估之前必须完成**；DEV15-B轮换=**P1，DEV13增量模型可先研究/只读，内存写入须Antigravity先证明**。本任务不直接授权更改正式存档。

## 一、用户业务需求与研究证据等级

用户明确指出原版AI通常按位置OVR排首发、教练BenchDepth/BenchUtilization/年轻老将与System Familiarity等因素影响替补数量与轮换、6th man常有较多分钟；一种25–99的“综评补偿”修改OVR而不动投篮/传球/速度等篮球技术属性，预计能**间接引导**CPU AI分钟；具体1–10分钟变化**是用户游戏经验，不是已证实的公式**，需要赛后/下月正式采集数据反馈。

跨版本参考：
- [Operation Sports 2017 Intangibles评级讨论](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-rosters/839369-roster-draft-class-creators-heads-up-intangible-rating-effect)：玩家举例25–99评级可影响OVR，且认为属于阵容/球员价值权重；`Intangibles`本身是编辑器原生属性，不等于所有2K22版本已认证无比赛/合同副作用。
- [Operation Sports 2024 Intangibles讨论](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/943402-can-someone-explain-the-intangibles-slider?p=25254631)：编辑玩家多年观察它主要影响OVR和轮换，但**没有官方统一引擎公式**。
- [Reddit旧MyLEAGUE CPU Rotations讨论](https://www.reddit.com/r/NBA2k/comments/ge4crz/how_do_you_guys_handle_cpu_rotations_in_myleague/)：玩家提到低OVR新秀被AI弃用、改Intangibles影响可用轮换。
以上仅支持方向可研究，**不能据此保证当代PC NBA2K22真实场上无副作用**。

用户允许这一**单项极窄的例外**：若经Antigravity在本局真正验证`Intangibles / OVR Compensation`是非技能、非潜力的评级补偿，可供GM提出经过玩家批准的轮换调整。项目原有“普通经营不得直接改原始球员能力/潜力/徽章/合同/伤病”禁令**仍生效**。特殊字段虽位于原生编辑器Attribute区，也**不能泛化批准邻近任何原生Attribute地址写入**；需要一个与原来ABILITY写保护白名单分离的、按原生精确offset/width/identity的单字段允许list + Approval + rollback。

## 二、DEV15-A（P0）— GM球探视图去潜力（Scouting Fog of War）

### 业务原则与关键数据源风险

**不要破坏历史人才基础数据，不删除原始潜力，不为保证模型看不到Potential而改变游戏中的原生属性。** 原始Potential/peak类数据留在本机权限隔离的观测/球员池与完整性检验来源，GM决策模型不能从这些数据中读取未来真实成长上限。GM只使用当前实测能力、比赛、年龄、位置、工资、可用性和历史增长趋势对球员**估计**未来发展，附可信区间/未知信息，不把真实原生Potential当确定论。

当前PR #5 `src/gm_data_access/query.py` 的`q_players.attributes`直接`json_extract(details_json,'$.attributes')`；`q_pool.attributes`也直接给完整原生attributes JSON。PR #4 `src/gm_data_access/analysis_inputs.py`的`PROJECTIONS['players']`含`attributes`，`src/gm_core/analysis_packet.py`逐项扩展`decoded_attributes`；M3市场筛选还允许`attributes.<field>.value`规则。**仅从命令行显示文本删Potential，而不从所有查询/SQL/市场接口切断，实际上仍可泄露。**

**P0实际修改：**
1. 统一`GM_SCOUTING_VISIBLE`字段白名单与版本号，由当前游戏原生字典注册。不把未知字段自动放进GM视图；已证真实潜力、潜力下限/上限、可能泄露确定未来成长上限的原生字段（如潜力、潜在巅峰发展/原生potential相关别名、raw_struct、可反推原值的raw hex/字节）列HIDDEN。区分“年龄、现状、当前身体运动能力”等当前可见事实，除非它们真实编码了未来潜力，不无差别屏蔽。
2. **在M0查询投影边界实施而非事后改M3文本**：`q_players`、`q_pool`（包括attributes JSON）、筛选/排序/任意SQL允许访问的临时视图、字段查询、`staff`里不相关潜力不要误删。严格禁止GM通过`json_extract(attributes,'$.Potential...')`、SQL拼装/`json_remove`反向重构或别名获取隐藏内容。使用可维护allowlist构造GM-safe JSON，非“仅删Potential一个键”的脆弱denylist。
3. M3A/市场/GM报告消费者不得再拿原始`source_details_json`、`raw_struct`或未经筛选的`decoded_attributes`。扫描PR#4 `analysis_inputs.py`、`analysis_packet.py`、`decision_handoff.py`、市场筛选器、球员池与新秀查询、导出JSON、训练投影；曾经sealed的M02事实不能被偷偷原地更改，只在新GM输出采用标明`scouting_visibility_profile`的可见投影。
4. **GitHub发布/物理权限边界**：若完整`published` SQLite或可读的GitHub原始JSON中继续包含隐藏Potential，而网页GM有权限直接提取原文件，则只控制M0查询并不能实现“GM无法知道真实值”。应将**原始完整观测限于受控本地/受限层**，把GM可访问的导出产物变为经过allowlist净化的只读查询副本或GM-safe SQLite；同步保留源哈希、来源日期、snapshot同批签名并避免GM能回读未脱敏的文件。若仓库/connector仍向GM暴露原始完整文件，须明确标注`FOG_NOT_ENFORCED_RAW_SOURCE_ACCESSIBLE`，GM V4不能宣称严格实现信息遮蔽。不能让同一模型自己签“没看Pot”替代权限隔离。
5. 现实历史球员“乔丹、科比”等真实身份/历史声誉仍可能被语言模型知道，这是另一层**历史信息泄露**：GM决策规范禁止依据尚未发生的现实后验荣誉/实际球员生涯来认定当前赛季新秀未来必成巨星；将现实历史球员信息限于截止当前游戏年份可用的篮球背景，未来名人身份不能当本世界确定收益。选秀球探今后只提供游戏内可观测数据/预测，不开放全部未来峰值。
6. GM可另算`prospect_projection` / `estimated_development_band`，但有来源（比赛分钟、效率、年龄、技术结构、逐批成长），输出概率区间、UNKNOWN；不能写入原生Potential、不能重新训练一个直接还原原Potential真值的泄露模型。

**验收（最小）**：
- 注入合成球员`Potential=97`、`potential_lower=90`等到私有快照。测试GM从`players`、`pool`、M3A`decoded_attributes`、市场的属性过滤/排序、SQL查询、任意允许导出/检索路径均无法得到隐藏字段名和值，也不能读取raw/敏感bytes；当前可见投篮/传球/速度/年龄/合同仍正常。
- 多档同名批次独立执行同一可见策略，源校验原始私有DB保持不变（不把抹去Potential写回源事实）。旧M02不能因schema迁移被悄悄改写。
- 如果GM还能从GitHub直接读取原始潜力，该门禁必须显式FAIL，不能只认查询测试PASS。
- 给出`GM_SCOUTING_VIEW_V1`和版本化字段字典，适合DEV13直接消费。

## 三、DEV15-B（P1）— 原版CPU轮换引导，不开发硬锁分钟

### 原生认证：Antigravity先完成（短期最小交付）

1. 精确定位PC NBA2K22本局`Intangibles/OverallAdjustment`字段（原生名字、UI中是否25–99、offset/width、当前与编辑后显示OVR）。证明它**不是普通能力变化的掩护**：修改前后投篮、传球、速度、潜力、徽章及战术倾向的逐值哈希与实际UI画面保持不变。支持写前/写后恢复与持久化审计；未经验证先只能READ_ONLY。
2. 同时只读获取球员现有展示OVR、真实能力向量、实际先发/第6人/替补顺序、原生旋转目标分钟/实际上场分钟，以及教练`BenchDepth`/`BenchUtilization`、青年/老将、体系适配等原生字段（若某项未证含义标UNKNOWN）。
3. 验证OVR补偿是否改变原生模拟统计/交易估价/合同/选秀顺位/阵容角色，而不是默认绝对无副作用。**不以完整现实球员生涯或多赛季手工测试为验收前提**。发生未预期真实篮球技能改变→禁用修改能力并报告。

### GM决策层：DEV13需知道“软目标”与闭环

- 由GM给每人期望`target_role`（Starter/PrimarySixth/Rotation/Development/Out）与`minutes_target_band`（范围而非硬锁），不要让GM生成强制34分钟的口头伪命令。正常12分钟×5人=240团队常规上场分钟，但替补偏差、加时、伤病与动态调整都应解释。
- 优先用非原始属性手段：调整教练BenchDepth/BenchUtilization、已认证先发、阵容角色、疲劳/训练和战术安排。若AI仍因OVR排序导致符合策略的人才长期DNP，才考虑单独的OVR compensation例外。
- 轮换方案必须关注各位置原始OVR排序、当前先发5、第6人、剩余轮换分配、教练体系/年龄/角色与可用性。**用户经验中“年龄/体系使分钟变化1–10分钟”不是稳定数值公式**。以真实3D比赛和CalendarSim分钟分别观察并评估两者是否反应不同。
- `intangible_override`只作为单独字段极窄动作：真实native原值、审批目标值、事前显示OVR、预计轮换方向（非精确分钟）、角色理由、可能的交易/合同侧效应及一个月反馈假设；只经DEV14 stage/preflight/人工Approval/apply/readback/reconcile，禁止使用直接裸运行地址或一次修改30队全部非目标球员。
- **保留两套评级口径**：`displayed_ovr`可能被策略性调节，**不得**直接用于GM真实能力强弱比较、交易估值或历史重力；角色价值要结合原始55项能力、比赛、年龄、合同、训练。单独保存`intangible_raw_before` / `current`、`rotation_intervention_active`。观察到球员自然成长变化时不能误归因为Override。
- 反馈周期：每一正式检查点以`observed_mp`、先发次数、板凳出场、6th-man出场、伤病/犯规、球队实际策略变化对照`minutes_target_band`，标`CONFOUNDED/INCONCLUSIVE/CONSISTENT_WITH_HYPOTHESIS`等，支持撤销恢复。不得编“Intangibles+10=多上场5分钟”的公式。
- 原版ACE与自动换人始终ON。若游戏持续覆盖直接分钟字段，不开发锁定反写脚本，不与原生AI抢同一内存。

### 数据/接口规范与验收

建议在DEV14 NativeFieldRegistry注册明确`player.rotation_intangibles`（**示例字段键，不表示已找到offset**），`gm_control`目标动作键`PLAYER_ROTATION_OVR_BIAS`；读写状态随Antigravity认证报告从DISCOVERED→READ_VERIFIED→TEST_MEMORY_WRITE_VERIFIED→GM_ENABLED，经玩家批准才进入正式。关联`player_id/team_id/save_instance_id/generation_id/source_batch`。
- 校验输入25–99的真实原值域和单字段mask只触碰允许的字节，不破坏其它Ability/Potential/Badge/身份。
- 有真实前后值+显示OVR+直接/模拟分钟观测才报告`EFFECT_DIRECTION_SUPPORTED`；没有真实数据报告`EFFECT_UNKNOWN`。
- 若读不到原生地址、真实轮换分钟或用户不批准测试，交付规则/数据模型与READ_ONLY，不伪造可写功能。
- **本任务是独立GM例外权限**，不修改DEV12普通Tendency权限，不把职业生涯历史重力通道扩权。

## 四、开发与额度安排

**开发顺序**：
1. **P0**：Codex只做DEV15-A的M0/M3 GM可见投影与最少防泄露测试；若PR#4仍为Draft，补丁放在与后续DEV13相容的分支，避免main/旧M3双份修同段代码。
2. **P1**：Antigravity可并行输出Intangibles原生定位/原生副作用/先发及第6人真实读取字段证据，不等Codex额度。
3. **P1**：在DEV13战术/训练正式决策打通以后由Codex通过DEV14 adapter增加轮换偏置行动，并以真实全量采集+用户批准作验证；不能在P0一次性强推30队轮换。
4. 不需要重跑全量119项、重新训练潜力预测大模型、自动模拟10个赛季、重新开发教练分钟锁定。

## 五、交付物

- GM脱敏字段配置、查询过滤/SQL和M3消费的代码与针对性测试；游戏和私有原始DB保持完整。
- `docs/GM_SCOUTING_VISIBILITY_POLICY.md`：可见字段白名单、源码/输出审核、潜力泄露与历史后见之明边界。
- `docs/GM_ROTATION_INTANGIBLES_RUNBOOK.md`：一支球队实例、原生字段/副作用证据、DEV14审批示例、反馈指标及不锁分钟声明；若尚无原生地址，标`AWAITING_ANTIGRAVITY_NATIVE_VERIFICATION`。
- `DEV15_ACCEPTANCE.md`及单独PR/后续阶段报告，不自动合并、不直接写入正式游戏。

**成功条件**：GM不知道未发生的潜力终值，但能依据有限资料估值和训练；拥有可验证的、可撤销的CPU分钟分配引导办法，而不是重新锁定分钟或偷改真实篮球能力。