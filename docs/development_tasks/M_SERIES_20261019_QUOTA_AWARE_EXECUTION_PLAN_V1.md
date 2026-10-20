# M系列紧急开发路线 — Codex额度受限分批执行 V1

**日期2026-10-19** · 当前用户反馈Codex **周额度约9%、5小时约49%**，这是界面现状快照，任务书不承诺所剩额度一定足够，也不按百分比换算成完成工时。**务必避免一条指令同时要求写完全部M3-T、完成30队研究、认证原生Intangibles并部署。**

## 0. 已有成果/权威链接

- [M3 PR#4](https://github.com/chris2gao/nba2k22-gm-engine/pull/4)：M3A/M3B工程已完，Draft/open未合并；head `fa62fb2`；现有30队事实/分析、D1–D6、HOLD/INTERNAL/MARKET、双边市场、P1–P5、终稿回滚不重写。
- [DEV14 PR#5](https://github.com/chris2gao/nba2k22-gm-engine/pull/5)：确定性Observed/Desired/Applied、每档控制库、单活动多档、99倾向只读/48已命名可提案、教练、战术本、训练、个人防守等，Open未合并；head `31f2682`；其119项合成/静态验收不能代表实际新批次生产验收。
- [DEV13](DEV_20261019_13_M3_TACTICAL_DECISION_INTEGRATION_V1.md)：GM的战术因果分析和动作整合，用新DEV14只读事实/执行器，不重建。
- [DEV14-H](DEV_20261019_14H_DEV14_POST_REVIEW_HARDENING_V1.md)：低成本必修：事实库/控制库/球员池三库同代次检查、真人批准来源隔离（或明确人工模式），PR顺序兼容。
- [DEV15](DEV_20261019_15_GM_SCOUTING_FOG_AND_OVR_ROTATION_CONTROL_V1.md)：P0隐藏玩家真实Potential，P1研究`Intangibles`综评补偿引导原版AI分钟。属于用户授予的**一项极窄例外**，不是普通直接改篮球能力值；真实写入另需逐批玩家批准。

## 1. Codex每次只接受一个阶段任务，完成即PR/commit报告、明确停止

### B0 / P0 — DEV14-H（优先执行，工作范围极小）

输入：PR#5分支代码。交付：`Workspaces.check_databases()`对球员池增加身份/代次验证、采集pool staging替换绑定，和一份不依赖模型自称批准的最小人工授权界限；原生进程/合同未知绝不执行实际RW。只跑相关tests（跨档错pool、未批准拒绝、共享位域不受影响）。PR#5独立保留，**不要自动合并**。周额度特别不足时先做H1，H2可提供`MANUAL_OPERATOR_TRUST_ONLY`安全约束与后续签发隔离接口，不能虚称已实现不可伪造授权。

**停止条件**：本次不开始DEV13、不把隐藏Pot修在错误的M3分支、不运行全量119测试。

### B1 / P0 — 合并顺序与GM潜力遮蔽

在玩家明确授权后，DEV14 PR#5先合并main；再让M3 PR#4更新到新main、处理实际文件合并冲突（至少`src/gm_data_access/query.py`与`scripts/gm_data_query.py`整合）并跑M3 P1–P5定向回归；合并PR#4仍需玩家单独授权。

把**DEV15-A**放到新M3数据消费和GM查询统一代码层：GM只读投影、M3数据包、市场查询以及任意SQL投影不能泄露原生Potential，原始私有数据库保持完整。测试必须跨球员/历史新秀池/SQL/M3报告，并显示GitHub原始发布数据是否仍对GM可直接访问（如果仍开放，`FOG_NOT_ENFORCED_RAW_SOURCE_ACCESSIBLE`不宣称完全隔离）。

**M3正式评估门禁：即使M3程序和数据已经可用，也不应在潜力值仍可直达GM时进行30队正式新秀/球员潜力研究。**

周额度不足时：只做兼容合并准备和DEV15-A的GM字段红线，不开始30队真实经营。

### B2 / P1 — DEV13 M3-T 最小闭环

已有M3A/M3B原流程不重建；DEV13的最小GM工作流：
1. 同career/batch/generation从DEV14只读来源取得教练系统/当前书68槽、球员4PlayTypes/99原始Tendency（48有名，51未知保持UNKNOWN）、个人防守、训练及负荷；查询分页和原生来源版本记录。
2. 更新M3 D1–D6分析：球队哲学、首发与第6人以及主力/替补、进攻创造者/无球/终结/护框，结构战术适配、球权冲突启发式、对手防守、内部战术/训练反事实，然后MARKET；**不把未解CRC类型、Touch75的启发式阈值、教练熟练度最高值宣称静态已验证**。
3. 提供HOLD/INTERNAL/MARKET的有证据比较，生成最小稀疏`DEV14 stage`意图，不把获批执行附带为本次开发成果；交易后旧球员/手册/个人防守/训练等行动重规划。
4. 事件分离：GM可以做RESEARCH_ONLY/PROPOSED/DRY_RUN，正式游戏写入仍经用户逐项批准；训练和Intangibles不得修改普通属性/徽章/潜力。
5. 定向回归真实现有M02旧档**新域NOT_OBSERVED**，不得凭缺来源断言战术缺口；合成30队D1–D6和市场规则最低必要案例；已发布数据不可改。

该阶段可拆为B2a（M3A只读桥接+UNKNOWN约束）、B2b（M3B诊断+提案合同）；每个小任务独立PR/测试，不要求Codex单次完成巨量大任务。

### B3 / P1 — DEV15-B 轮换引导（须Antigravity原生证据）

Antigravity先交付PC本局Intangibles/OverallAdjustment原生地址/字段名/25–99实际值域、只读可见OVR/先发第6人/实际分钟和原生属性保护证据。Codex再把一个**独立**`PLAYER_ROTATION_OVR_BIAS`动作加入DEV14能力表与M3方案合同；真实球队GM先采集/提出软分钟区间+HOLD替代，不运行强制锁分钟；正式修改由玩家批准。若没有原生认证，结束为READ_ONLY及完整诊断规则而不是硬写内存。

**实现目标不是精确分钟公式**：按位置OVR及第6人、BenchDepth/BenchUtilization、年龄/体系适配/训练疲劳观察，做可逆的小范围试验与月度复核；该评级影响合同/市场或模拟的副作用没有证据前保持风险警示，GM估值不能把被调高的显示OVR当真实能力。

## 2. 当前额度策略/交付格式

- 先执行**B0单独一轮**。如果Codex运行额度不足，即使只完成H1也可以先交commit；下次同分支继续，不重新开第二套架构。
- DEV15-A的字段遮蔽**优先于**M3 V4正式GM分析；DEV15-B的内存操作**晚于**DEV13核心只读/GM决策，可以由Antigravity先行定位/研发而不消耗Codex额度。
- 不重新搞DEV14 A/B/C/D、完整采集、仓库大迁移、99种倾向重新探址、全部30队策略首次运行、两套GitHub历史快照重发布、117+个重复验收；阶段成功只要求本阶段直接相关测试。
- 任何阶段都不默认合并GitHub PR、写入游戏存档、采集或更新正式数据库、启用GM V4。已经完成并提交的代码与尚未真实生产验收严格区分。
- Codex单次输出固定四项：完成变更/commit/PR、定向测试与剩余风险、是否需要Antigravity原生证据、**下一个可独立触发任务**。不报告不能保证的完成时间或额度换算。

## 3. 推荐发给Codex的首轮简短指令

> 按`docs/development_tasks/DEV_20261019_14H_DEV14_POST_REVIEW_HARDENING_V1.md`实施**B0**，只修PR#5三库同代次绑定及人工审批信任边界，做少量定向测试并提交commit。**不要在同一轮开发DEV13/DEV15，不合并PR，不运行正式游戏采集或RW。** 周额度不足时先完成H1，保留干净可续分支并报告完成状态。

**总原则：一次模型只执行一小块、所有事实与正式授权由确定性程序和玩家确认，篮球决策才由GM分析模型负责。**