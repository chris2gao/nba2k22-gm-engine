# DEV17 — Codex先完成M系列主线：球队同名战术书、换帅归位、GM最小闭环

**日期2026-10-19 · 角色：Codex主线工程，Antigravity仅在卡住特定原生对象时小范围协助，后续补扩展。**
**状态：玩家批准开发任务规划，但未批准合并PR、正式NBA2K22存档RW、生产采集或GM V4上线。**

## 0. 核心最终经营规则

- **球队始终使用本队同名的、真正独立的原生Playbook**。教练决定体系和执教风格，球队保留自己的战术书，通过该书68槽的具体战术适应教练与当前球员。GM日常**不以更换`coach.PlaybookID`来调整打法**。
- 教练更换示例：A球队–A主教练–A球队书 → A球队聘B主教练时可能短暂变为A–B主教练–B球队书 → **必须受控将B主教练在A球队的`PlaybookID`恢复绑定到A球队同名书** → 再根据B教练体系、A球员能力/PlayTypes/倾向与实际比赛，重新配置**A球队书**。B球队及其B书不能被本次操作改变。
- 每球队每**游戏赛季**最多更换**一次**正式主教练，且只在**休赛期**。此处只记录M3 GM决策门禁、对应审计事件/履约接口，**不在本期开发休赛期员工合同签约、竞价、自由市场、阶段推进**。用户会在每一休赛期节点更新数据，外挂签约将在游戏CPU自由市场操作前作出决策；此业务作为后续开发规划，不在DEV17展开。
- **日常GM防守仅写`PERSONAL_DEFENSE`，`OVERALL_DEFENSE`只读**，从而避免原生整体防守覆盖个人防守。
- DEV15 V2继续生效：正式采集入库/发布前自动把所有球员的Potential字段与PLAYER raw字节0x441脱敏为1（不能用于历史新秀原生注入）；`Intangibles` byte0x440作为30队GM轮换引导字段，常规获批25–99，不研究额外业务副作用；ACE负责实际分钟。
- 以上是**最新优先级权威规则**，替换此前“GM先改整体再改个人”“先切书再改槽作为日常调整”和“必须等Antigravity全部扩展完才能开发M3”的旧任务表述。

## 1. 现存源码与能立即复用的事实

- PR#5 `src/coach_locator.py:read_playbooks` 已返回当前已加载原生Playbook的`name,index,unique_id,enum_id`及CRC槽；`src/gm_state_io/adapters.py`按Coach真实PlaybookID解出`owner_team_ids`，并在`resolve(PLAYBOOK_SLOT)`核查owner未变；`src/gm_state_io/registry.py`已允许合法已加载的`coach.PlaybookID`变更、已观察的68槽CRC和其他教练/个人训练/球队训练/个人防守/4PlayTypes/48具名Tendency。
- 以上表示：**Codex可能仅需增加已知Codec上的业务动作合同与权限**，不必重新扫描所有Playbook内存地址或开发第二套读写引擎。
- **仍未知的是本存档30个球队同名书是否全部真实存在且互不共享**；\`name\`字符串本身不能证明物理独立。若A同名书不存在/enum身份不唯一/有其他owner，必须返回`TEAM_BOOK_UNIQUE_BINDING_UNAVAILABLE`，不能伪造对象或暗改其他球队；只阻断**改手册**，其他GM行动照常。
- Antigravity已报告曾解决“复杂战术书替换失败”，而PR#5只证明当前已加载CRC及批次编码的工程合同。旧报告不应据此宣称游戏内所有槽都完成正式验证；但**无需以全本目录语义研究阻挡Codex在已证CRC上实现安全主线**。

## 2. 主线Codex实施顺序（有限额度，每次只做一个小批次）

### B0（已立项）：DEV14-H精确加固

继续[DEV14-H](DEV_20261019_14H_DEV14_POST_REVIEW_HARDENING_V1.md)：三库pool/league/control的同档同generation验证及非模型自行审批信任边界。不要重做DEV14 A/B/C/D，不因本轮重测119项。

### B1：DEV15 V2确定性自动Potential=1

每次`full_verified_v1`采集完、正式commit/manifest/备份/发布前，自动清洗pool/roster/JSON/PLAYER raw_struct byte0x441；遮蔽后的GM球员池不能供历史选秀反注入，缺原始私有注入源时Fail Closed。既定工作按[DEV15 V2](DEV_20261019_15_GM_SCOUTING_FOG_AND_OVR_ROTATION_CONTROL_V1.md)，不再探索其它潜力遮蔽方案。

### B2：DEV13+DEV16已知字段M3-T最小闭环（主线优先）

1. 保留PR#4 M3A/M3B现有P1–P5六维研究及PR#5 DEV14读取/执行，不重写。将职业存档+batch+generation数据读入GM研判，形成HOLD/INTERNAL/MARKET证据比较+可交DEV14的稀疏目标；51未知Tendency不让GM猜、Play CRC无类别解码时`SEMANTICS_UNKNOWN`、疲劳没有当前真实指标则`NOT_OBSERVED`。
2. 建`TEAM_BOOK_CATALOG`只读投影：逐队真实`team_id/name/abbreviation,head_coach_id,coach.PlaybookID,Book.name/index/enum_id/unique_id,owner_team_ids,book_identity,exclusive_status`。从已有30队目录与同一源NativeSession读，不另造缓存事实库。定义经过原生球队目录校验的严格“当前球队同名书”匹配，不使用字符串模糊匹配；重复/缺名明示BLOCKED。
3. 正常GM禁止`coach.PlaybookID`直接切书与`OVERALL_DEFENSE`整体修改；启用多名对手球员的`PERSONAL_DEFENSE`并保持原值/回读审计。仅有明确批准的`TEAM_BOOK_INITIAL_BIND`、`TEAM_BOOK_REBIND_AFTER_VERIFIED_COACH_CHANGE`才可计划修改Coach PlaybookID；凭空提供`reason=rebinding`不能绕过作用域与玩家批准。
4. **A→B主教练的恢复绑定工作流**：先有已确认的合法换帅事件/事实；源发现A现任B主教练对应B书 → 确认A球队同名原生Book可独占绑定 → 生成第一份GM技术绑定提案，把A教练`coach.PlaybookID`设为A书已加载`enum_id`，经玩家批准、CAS、回读 → 刷新A球队和Book所有者+68槽快照 → 生成第二份A队本书的`PLAYBOOK_SLOT`战术更新提案，经玩家独立批准再执行。**两个阶段不能合并成一次引用旧槽位前像的物理事务**。恢复只影响A队Coach字段和A的独占书，不得修改B书/B队任何内容。
5. 绑定前/后书操作都需`owner_team_ids==[team_id]`与底层真实book identity匹配；若多个球队共用书，`SHARED_PLAYBOOK_MUTATION_BLOCKED`，不因所有owner同意就修改。因换帅或新绑定导致此前的个人/coach/书身份变动，旧批次须重新预检，不允许沿用批准。
6. 在GM计划增加正式主教练`season_change_count<=1`与`OFFSEASON_ONLY`业务约束（按`save_instance_id+generation+league_season+team_id`计数）。仅记录**实际确认完成的换帅**；初始化专属手册不是换帅；正式签约与员工合同执行保持后续专项，当前可先交纯离线模型接口和合成验收。
7. 已有训练只开放球队强度、休息与已证九种通用个人训练原型/强度，严格不开放逐项属性微调；增加`Intangibles`轮换可审批单字段动作，并记录GM期望角色/分钟范围与下次真实游戏反馈。**所有真实玩家批准规则继续有效**。
8. M3只要数据字段齐备即可形成有证据的战略候选，缺完整战术CRC语义/51倾向/位置模板时不得假装理解全部，但可以用已有信息做HOLD/内部调整/人才市场比较。

### B3：Antigravity扩展——一般放在Codex主线完成后

**这不是B2的通用前置条件。** Codex先完成确定性查询、GM诊断、战术/训练已知字段计划、球队独占书的状态与恢复绑定业务。Antigravity随后扩展：
- 战术手册CRC→UI真实战术/PlayType/使用位置/现实篮球动作及Coach体系匹配；
- 51未知Tendency的语义和值域；
- 各位置实际可用训练模板/原有9通用原型关系、疲劳只读解码。
**唯一可提前委托的小任务**：若本局未能唯一定位A球队原生同名书、或现有Book slot CRC写入尚不能安全操作，Antigravity只研究\`TEAM_BOOK_UNIQUE_BINDING_UNAVAILABLE\`的具体原生问题并提供最小定位/写入适配，而不是先研发整个篮球战术知识库。Codex不因此停止其它B2工作。

## 3. 最小验收与交付（避免消耗Codex额度）

1. 合成A/A主教练/A书→A/B主教练/B书，且B原生书属于其他球队：只对A教练做一次获批技术性BookID重绑定，A书owner独占后本队槽位可单独编辑，B书及B队全程未被修改。
2. A书不存在/共享/源身份改变时`TEAM_BOOK_UNIQUE_BINDING_UNAVAILABLE`或`SHARED_PLAYBOOK_MUTATION_BLOCKED`，不得落入随意选取其它本或改共享书；不可执行书槽不影响其余M3分析。
3. 每队每赛季休赛期最多1次主教练变更，常规赛或第二次变更拒绝；**不以此冒充完整休赛期签约系统已经实现**。
4. 个人对位防守可同批多球员；正常GM对整体防守/自由切书变更拒绝。Playbook绑定与改slot分先后两份计划并重新取前值。
5. 知识扩展未到位时`UNKNOWN`正确保留，不允许编造疲劳/战术类型；P0 Potential=1、人类审批与现有DEV14底层不被破坏。
6. 针对性合成+已有M02只读样本即可开发验收，不运行正式存档或生产上传、不自动合并PR#4/#5。

**交付**：Codex独立可续分支/PR、GM已知字段可查询和决策接口、Book目录/绑定/独占校验、换帅季节规则、定向验收与未解原生项清单。周额度不足时每阶段commit停止，下一次继续相同分支，不重构。