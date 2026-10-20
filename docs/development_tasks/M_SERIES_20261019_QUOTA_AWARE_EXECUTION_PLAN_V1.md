# M系列紧急开发路线 — Codex额度受限分批执行 V1.1

> **2026-10-19 最新GM政策**：[个人防守优先+球队专属战术书](../../web_gm/manuals/GM_DEFENSE_AND_TEAM_PLAYBOOK_POLICY_V1.md)与[DEV16](DEV_20261019_16_M3_NATIVE_COVERAGE_AND_GM_TRAINING_PLAYBOOK_INTEGRATION_V1.md)已更新：日常GM不再写整体防守，个人针对球员；GM不主动切PlaybookID，必须用本队原生独占Book修改槽位，多队共享PHI等书时BLOCKED，换帅需重审Book归属/新教练体系。Antigravity先研究独占书实体、专属绑定可行性与安全战术替换；Codex之后用现有DEV14做少量策略禁写与独占验证，**不要为此重做引擎或重复测试50世界参数**。

> **2026-10-19 DEV16用户七项修订**：新增[DEV16](DEV_20261019_16_M3_NATIVE_COVERAGE_AND_GM_TRAINING_PLAYBOOK_INTEGRATION_V1.md)作为新执行范围：Antigravity可并行做Playbook目录/替换、51无名倾向语义及位置模板与疲劳只读；Codex只在既有DEV14上注册这些新增字段，DEV13使用，不重复开发19/18教练、48倾向、6+5训练、50World/4Gameplay。某一codec家族已有成功代表实验不再逐字段手工测试；战术书替换因曾失败属于例外独立修复。总体优先B0、B1，之后AG字段资料就绪再做B2；B3Intangibles不需要其他系统副作用研究。训练只改模板/强度/休息，不做属性微操。

**日期2026-10-19** · 此前用户反馈Codex **周额度约9%、5小时约49%**，这是界面现状快照，任务书不承诺所剩额度一定足够，也不按百分比换算成完成工时。**务必避免一条指令同时要求写完全部M3-T、完成30队研究、上线完整脚本并部署。**

## 0. 已有成果/权威链接

- [M3 PR#4](https://github.com/chris2gao/nba2k22-gm-engine/pull/4)：M3A/M3B工程已完，Draft/open未合并；head `fa62fb2`；现有30队事实/分析、D1–D6、HOLD/INTERNAL/MARKET、双边市场、P1–P5、终稿回滚不重写。
- [DEV14 PR#5](https://github.com/chris2gao/nba2k22-gm-engine/pull/5)：确定性Observed/Desired/Applied、每档控制库、单活动多档、99倾向只读/48已命名可提案、教练、战术本、训练、个人防守等，Open未合并；head `31f2682`；其119项合成/静态验收不能代表实际新批次生产验收。
- [DEV13](DEV_20261019_13_M3_TACTICAL_DECISION_INTEGRATION_V1.md)：GM的战术因果分析和动作整合，用新DEV14只读事实/执行器，不重建。
- [DEV14-H](DEV_20261019_14H_DEV14_POST_REVIEW_HARDENING_V1.md)：低成本必修：事实库/控制库/球员池三库同代次检查、真人批准来源隔离（或明确人工模式），PR顺序兼容。
- [DEV15 V2](DEV_20261019_15_GM_SCOUTING_FOG_AND_OVR_ROTATION_CONTROL_V1.md)：**业务已定**，P0在每次正式采集结束与发布前统一潜力=1（含Player raw byte0x441），P1将现有Player `intangibles`(0x440)作为30队轮换常用受控字段25–99；无其它业务副作用研究门禁，正式游戏修改仍需玩家批准。

## 1. Codex每次只接受一个阶段任务，完成即PR/commit报告、明确停止

### B0 / P0 — DEV14-H（优先执行，工作范围极小）

输入：PR#5分支代码。交付：`Workspaces.check_databases()`对球员池增加身份/代次验证、采集pool staging替换绑定，和一份不依赖模型自称批准的最小人工授权界限；原生进程/合同未知绝不执行实际RW。只跑相关tests（跨档错pool、未批准拒绝、共享位域不受影响）。PR#5独立保留，**不要自动合并**。周额度特别不足时先做H1，H2可提供`MANUAL_OPERATOR_TRUST_ONLY`安全约束与后续签发隔离接口，不能虚称已实现不可伪造授权。

**停止条件**：本次不开始DEV13、不把隐藏Pot修在错误的M3分支、不运行全量119测试。

### B1 / P0 — Potential=1数据库自动后处理 + PR兼容安排

**先完成DEV15 V2的自动净化**：在`auto_pipeline_ingest.py`原生采集与初步来源校验之后、两库commit/replace、snapshot digest/哈希、备份和GitHub发布之前，自动运行`sanitize_player_potential`，令全部`player_pool.potential/raw_potential`、所有球员`attributes.potential.raw/value`、球员`raw_struct[0x441]`统一为1；跨球员池/球队名单、JSON/静态副本和旧/新来源镜像，能读到实际潜力的存储位置都纳入检查。脱敏字段标MASKED而非游戏观测。除了字节0x441，绝不修改其他原始字段；失败停止发布。单脚本可用于dry-run和幂等再跑，正式`full_verified_v1`不需要GM/执行模型另外触发。

现有老M02历史批次如含真实Potential应隔离GM访问或另经审批生成安全的GM可见副本，不悄悄篡改不可变历史。**不需要再开发“只在显示层隐藏潜力”的多重替代方案**；在库阶段改1是当前权威决议。升级GM规则明确Potential=1不是所有球员低潜力，仅表示未来潜力未知。

PR顺序：B0完成后PR#5经用户许可合并main；PR#4更新到新main做必要兼容回归并等待用户批准合并（这不是B1可自动执行的merge指令）。要防止Codex误在旧M3分支复制采集器造成两套脱敏脚本。

**若周额度只够一个子工作**：先交付自动潜力处理、合成测试及新来源哈希验证，下一次接着做PR整合/GM轮换。

### B2 / P1 — DEV13 M3-T 最小闭环

已有M3A/M3B原流程不重建；DEV13的最小GM工作流：
1. 同career/batch/generation从DEV14只读来源取得教练系统/当前书68槽、球员4PlayTypes/99原始Tendency（48有名，51未知保持UNKNOWN）、个人防守、训练及负荷；查询分页和原生来源版本记录。
2. 更新M3 D1–D6分析：球队哲学、首发与第6人以及主力/替补、进攻创造者/无球/终结/护框，结构战术适配、球权冲突启发式、对手防守、内部战术/训练反事实，然后MARKET；**不把未解CRC类型、Touch75的启发式阈值、教练熟练度最高值宣称静态已验证**。
3. 提供HOLD/INTERNAL/MARKET的有证据比较，生成最小稀疏`DEV14 stage`意图，不把获批执行附带为本次开发成果；交易后旧球员/手册/个人防守/训练等行动重规划。
4. 事件分离：GM可以做RESEARCH_ONLY/PROPOSED/DRY_RUN，正式游戏写入仍经用户逐项批准；训练和Intangibles不得修改普通属性/徽章/潜力。
5. 定向回归真实现有M02旧档**新域NOT_OBSERVED**，不得凭缺来源断言战术缺口；合成30队D1–D6和市场规则最低必要案例；已发布数据不可改。

该阶段可拆为B2a（M3A只读桥接+UNKNOWN约束）、B2b（M3B诊断+提案合同）；每个小任务独立PR/测试，不要求Codex单次完成巨量大任务。

### B3 / P1 — Intangibles轮换正式动作+GM分钟反馈（用户已定，无需副作用研究）

**不再设置Antigravity额外副作用研究/测试门禁**：项目现存`config/memory_field_profile.json`已定义球员`intangibles` offset=0x440，`potential` offset=0x441；属于精确单字段可写例外。Codex在DEV14 Registry/Codec/Adapter新增`PLAYER_ROTATION_OVR_BIAS`，合法25–99，30队GM可按软分钟目标自由提出此类动作；所有正式内存修改依旧逐批用户批准和前后读回，原本真实Ability/Potential/Badge保护不放宽。

DEV13记录首发/第六人/BenchDepth/年轻老将/体系熟练度/实际场均分钟与GM目标分钟，后续正常采集持续改进。这是**操纵AI轮换输入**而不是通过脚本硬锁分钟；别重新研究Intangibles对交易/合同/模拟的副作用。只需确定性准确写入和不触碰相邻字段0x441的最小工程回归。

**如额度不足**：Antigravity可以把原生字段/写入适配细节交付，Codex稍后在已存在DEV14接口上补单个动作，不阻塞GM的P1/P2只读战术分析。

## 2. 当前额度策略/交付格式

- 先执行**B0单独一轮**。如果Codex运行额度不足，即使只完成H1也可以先交commit；下次同分支继续，不重新开第二套架构。
- **Potential入库后统一=1的自动脱敏**优先于任何GM V4正式球员分析；Intangibles单字段能力可独立接DEV14，M3后续按真实轮换效果调整，无需额外研究各模块副作用。
- 不重新搞DEV14 A/B/C/D、完整采集、仓库大迁移、99种倾向重新探址、全部30队策略首次运行、两套GitHub历史快照重发布、117+个重复验收；阶段成功只要求本阶段直接相关测试。
- 任何阶段都不默认合并GitHub PR、写入游戏存档、采集或更新正式数据库、启用GM V4。已经完成并提交的代码与尚未真实生产验收严格区分。
- Codex单次输出固定四项：完成变更/commit/PR、定向测试与剩余风险、是否需要Antigravity原生证据、**下一个可独立触发任务**。不报告不能保证的完成时间或额度换算。

## 3. 推荐发给Codex的首轮简短指令

> 按`docs/development_tasks/DEV_20261019_14H_DEV14_POST_REVIEW_HARDENING_V1.md`实施**B0**，只修PR#5三库同代次绑定及人工审批信任边界，做少量定向测试并提交commit。**不要在同一轮开发DEV13/DEV15，不合并PR，不运行正式游戏采集或RW。** 周额度不足时先完成H1，保留干净可续分支并报告完成状态。

**总原则：一次模型只执行一小块、所有事实与正式授权由确定性程序和玩家确认，篮球决策才由GM分析模型负责。**