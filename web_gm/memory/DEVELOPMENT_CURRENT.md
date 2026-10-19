# Web GPT · 开发规划基线当前记忆

## 2026-10-18 玩家最新开发职责：历史线人物定制单独立项，与GM球队经营分离

玩家明确将**符合历史年代逻辑的当前联盟人物特殊能力/属性定制**放到**开发规划模型**，与网页GM五轮以上30队赢球经营/正常交易/教练修改隔离。正式交接：[DEV_HISTORY_GRAVITY_SEPARATION_20261018_V1](../../docs/development_tasks/DEV_20261018_HISTORY_GRAVITY_GM_BOUNDARY_V1.md)。GM最新六维经营：[GM_DATA_TO_DECISION_V1](../manuals/GM_DATA_TO_DECISION_STANDARD_V1.md)。

- 开发基线任务仅是机制/方法/人物同一性/时代参考/数值边界/原值→拟议值/短长期影响及回滚与安全执行器的**独立规划**；按已批准规则2026游戏年开始模拟1984乔丹选秀四年后的历史年代，历史选秀1984–2020循环依玩家确认，不自动推进或强制历史赛果。
- 当前**没有批准任何历史人物能力改动**；文档26记载历史重力受控属性执行器尚未实现，旧`growth_engine`/通用`modifier`停用。不得因职责移交就启动开发执行/修改游戏或数据库。具体专项由玩家另行明确触发，再设计、审计、逐项批准、交Codex受控执行。
- GM只负责本局真实的30队球员评估、制服组/战术、市场交易签约，以符合历史发展逻辑为参考而非硬改属性；正常交易授权永不包含历史重力改属性。
- **员工变化同样存在开发/GM职责界面**：M02来源已验证30队×8岗位员工关联可读，员工产生的PC版游戏属性/比赛影响和完整雇佣/岗位变更写回未认证。GM在六维评价中可提出业务上换帅/换员工的研究候选；只有玩家未来触发开发专项，开发基线再核验真正有效字段、双向变更与恢复路径。次世代MySTAFF的17人四部门与加成不可误导PC来源。
- 训练与个人分钟锁定在本项目明确交由游戏AI，不建立外挂开发任务。



- role: WEB_GPT_DEVELOPMENT
- memory_version: 4
- last_reviewed: 2026-10-18
- state: COACHING_CODE_MAIN_DEPLOYED_FULL_CAPTURE_FIRST_PRODUCTION_PENDING
- linked_codex_state: `docs/34_BASELINE_CURRENT_STATE.md`（**Codex 状态索引，不在此复制更新**）

DEV07 Codex 已在 PR#1 分支继续实施 V2，不再处于代码未开始状态。当前证据、字段门槛和剩余工作只读 [Codex 状态34](../../docs/34_BASELINE_CURRENT_STATE.md)与[集成报告](../../docs/development_reviews/DEV_20261017_07_COACHING_INTEGRATION_REPORT.md)。已建立 [GM 操作手册](../manuals/GM_COACHING_OPERATIONS.md)及 [Codex 执行手册](../../docs/40_COACHING_EXECUTION_RUNBOOK.md)。当前19项默认字段接口已实现，Tempo按玩家明确选择开放原生raw并标明界面含义未知；PR #1已于2026-10-18通过玩家审查并合并main（2509b3b），本地已同步；真实生产采集和数据发布未运行，不能把代码部署当成数据发布成功。

玩家最新修正：正式脚本顺序执行；不要把少量验收样本当作允许值白名单。BenchDepth取消9–10人为上限，由GM读取阵容后选择人数；四Freelance按完整原生枚举/布局及有序codec提供受控接口，不因未重复菜单检查而禁用，也不冒充实际UI已验证。当前19项默认字段可提案/受控执行；玩家明确开放原生Tempo并保留界面含义未知，结合其他教练观测值选择目标，不增加测试样本限制。原生类型/枚举、来源身份、具体批准和条件恢复保护保留。

## 已知工程事实

- GM v1.0 M1–M6 的 Python 核心、命令行分析准备、提案协议已由 Codex 实现；v2 双方谈判、v3 正式王朝经营仍未全部实现。
- 最新来源已包括 30 队赛季胜负/累计统计、球员 55 项能力、部分球员赛季表现、员工关联、简单选秀权；玩家将薪资采集需求限定为当前大名单工资。
- 上一次 Web GPT 的 30 队独立量化分析已写到 `docs/gm_analysis/`；这是网页分析角色，不应每轮交给 Codex 重新做。
- 现有 Codex 数据采集/开发基线为 `docs/32`、`docs/33`，它们与本 `web_gm/baselines/DEVELOPMENT_BASELINE.md` **分属不同执行角色**。

## 待做（由玩家按需触发）

- 维护 Web GPT 需求文档与 Codex 工程开发任务书：例如 GM v2 交易谈判、多模型交接、对话基线协议的后续自动化可行性；**单来源生产更新已被玩家取消，不再开发**。
- 新开发需求发生时先核对仓库当前代码、相关测试与 commit；不要根据之前工作总结宣称新功能已有生产能力。
- 完成一次开发任务后保存 `development/sessions/<run_id>.md`，更新此索引并报告实际变更/交接文件/提交。

## 边界

本窗口的默认任务是**研发设计、Codex 任务书与验收**，不是 Codex 本地脚本执行窗口；不默认修改生产源码/采集真实内存/发布游戏数据，不提交未经授权的正式 GM 战略和游戏执行变化。

## 最近已完成的开发规划/文档任务

- [2026-10-17 三份 Web GPT 专用基线及记忆协议建立](development/sessions/20261017_web_gpt_three_baselines_v1.md) — `COMPLETED`；Web GPT GM / DEVELOPMENT / ANALYTICS 三种基线现已放在 `web_gm/baselines/`，角色协议 `docs/35_WEB_GPT_BASELINES_AND_MEMORY_PROTOCOL.md`，Codex 的 docs/32–34 保持独立。
- 此次成果仅建立文档与项目职责，并未自动生成聊天窗口、启动 GM、运行采集或写入游戏。

## 当前开发交接：DEV-20261017-04 休赛期自由球员签约（规划完成、代码待做）

- 状态：`SPEC_PUBLISHED_AWAITING_CODEX_P0`。此项为研发任务书，不构成正式赛季签约许可。
- 入口：[Codex 任务书](../../docs/development_tasks/DEV_20261017_04_OFFSEASON_FREE_AGENCY_V1.md)，[本次规划归档](development/sessions/20261017_offseason_free_agency_plan_v1.md)。
- 任务书创建提交：`3ff1ff53e50084390092402462efa7e2600c8e3a`。
- 顺序：P0休赛期安全节点及原生AI自动签约调研 → P1 30队只读候选池/报价/母队竞价 → P2安全签约执行器测试 → P3全闭环跨赛季实机验收。
- 硬阻塞：没有经过验证的完整签约执行器/自由球员权属/原生AI控制。2021–22薪资规则不得代替以后年份；大名单工资帽差额非真实签约空间。正常球员能力编辑禁止；玩家每次具体签约需要独立批准。

## 2026-10-17 教练战术对模拟比赛影响：历史评估（赛前A/B建议已被V2规则覆盖）

- 状态：`SIM_TACTICS_ASSESSMENT_ONLY`，不代表Code已开发或允许写入正式存档。
- [评估报告](../../docs/development_reviews/DEV_20261017_COACH_TACTICS_SIMULATION_ASSESSMENT_V1.md)；[会话归档](development/sessions/20261017_coach_tactics_simulation_assessment_v1.md)，报告提交`b599e17`。
- 结论：优先验证NBA2K22 PC普通快速模拟的Sim Points of Emphasis/教练体系与传统球队POE、战术手册是否分路生效；有效才提供GM season tactic proposals、玩家批准及Codex受控执行。不开发未经验证的实时模拟教练AI。
- 技术风险：`StrategyManager.set_team_strategy`仅uint8/回读；`poe_on_ball`枚举冲突；还需真实UI字段↔内存映射、Sim效应对照、AI覆盖与存档持久性证据。次世代主机Conditional Coaching不能视为PC功能。

## 当前交接：DEV-20261017-05 教练战术定位、条件开发、玩家月度验证 V2

- 状态：`MEMORY_DISCOVERY_THEN_IMPLEMENT / GAMEPLAY_TEST_DEFERRED_TO_PLAYER_MONTH_END`。玩家最新要求**Codex先定位内存、确认安全后直接开发；不要求Codex先跑20/100场对照模拟**。开发期只需合法枚举、对象身份、隔离存档读写/恢复/重启等最小技术安全检查。
- [V2主任务书](../../docs/development_tasks/DEV_20261017_05_COACHING_MEMORY_DISCOVERY_V1.md)（原V1同路径覆盖更新）；[V2变更历史归档](development/sessions/20261017_coaching_month_end_validation_change_v2.md)。任务书最后更新提交`d5702d759a14285b76def883b7ff2306ff345b3a`。
- 交付：Codex在确认部分字段可安全实现后，直接编写GM读取/提案及**受控**执行器，提交真实代码/必要技术验证/字段矩阵。技术实现完成时**不得声明模拟比赛效果得到证明**，效果标`SIM_EFFECT_PENDING_PLAYER_MONTH`。
- 下一步游戏内测试归**玩家**：具体战术方案须独立审批并由执行端受控落地，玩家推进一个游戏月后分别触发比赛来源更新→Web GPT ANALYTICS分析→同赛季GM决策复核。游戏效果属于首月观察，不自动证明因果关系。
- 月度计算仅在同存档同赛季同统计口径且游戏日期单调前进时：`ΔW`/`ΔL`/`ΔG`以及累计总量差计算本月指标，不能对赛季累计场均做直接相减；已知只有赛季累计，不假称逐场明细存在。
- 持续保持游戏写入审批、不得改普通球员能力/潜力/倾向/徽章、不得偷改全联盟Simulation Sliders，也不得因开发完成自动开始采集、GM回合或正式存档执行。仍未知：比赛内CPU AI是否覆盖、普通快速模拟具体读取哪些战术字段，等实际反馈。

## 最新交接：DEV-20261017-06 NBA2K22 原生教练战术受控执行器实施

- 状态：`IMPLEMENTATION_TASK_PUBLISHED_AWAITING_CODEX`，用户转交Codex原生代码+进程只读调研并允许直接开发；截至此处无正式写入和赛果效果实测。用户原话“可以开发”不等于对任何30队具体战术方案的正式游戏写入批准。
- [Codex正式开发任务书](../../docs/development_tasks/DEV_20261017_06_COACHING_IMPLEMENTATION_V1.md)（创建提交 `dd561e9e5455b118ff01e304689cd6460b519d6b`）；[玩家转发只读调研](../../docs/development_reviews/DEV_20261017_05_COACHING_READONLY_HANDOFF.md)；[开发规划归档](development/sessions/20261017_coaching_native_implementation_handoff_v1.md)。
- **高危缺口：旧TEAM+0xEB2不能再用于策略写入！** `src/strategy_manager.py`的旧setter和`src/bootstrap_new_game.py`初始30队批量调用必须先停用/迁移，不能把旧0..6枚举自动转换为新POE值；票价功能独立保留。
- 新默认教练六POE为`COACHDATA+0x13C`的32bit共享位域，six×5bit，bits30..31保留；精确enum列在实施任务书。Sim系列另在教练`+0xF4`附近共享位域，尚缺完整bit掩码。查实时code再允许写。
- 对手方案：`FRANCHISE_GAMEPLAN_MANAGER`每队35槽、29条有效他队方案，本局报告总870条，Gameplan=0x370/条。原生`IsInUse=0`全未启用，启用语义未知则只读/提案，不得声称写入会生效；Playbook当前加载84本只用于该次读数，不可固定上限。
- Codex应先重新实测结构、修旧入口，再做可行模块的GM只读+提案和执行器、必要技术安全检查与Github交付；未完成战术作用验证时标`SIM_EFFECT_PENDING_PLAYER_MONTH`，不要求Codex事先模拟20/100场。
- **玩家实效验收**：具体GM战术方案→玩家批准→Codex执行回执→玩家游戏正常推进一个月→玩家另行触发数据采集→Web GPT ANALYTICS用同存档同赛季累计值计算月度`ΔW/ΔL`及可观测统计差→GM评估。不得自动串联。
- 证据边界：上面的新原生地址/位域依据玩家转交的Codex文本，当前Web GPT未取得实机源码/日志，因此属于`USER_RELAYED_CODEX_FINDINGS_NOT_INDEPENDENTLY_RETESTED`，不是已验收业务执行器。

## 最新交接：DEV-20261017-07 GM教练系统30队批次/来源/双手册

- 状态：`COACHING_CLOSED_LOOP_SPEC_PUBLISHED_AWAITING_CODEX`，**以下为已过期的历史规划状态；当前代码与合并状态以本页顶部及状态34为准**。用户不再要求“快速模拟胜率效果验证”；教练机制完成以工程闭环为准。
- [Codex最终完善任务书](../../docs/development_tasks/DEV_20261017_07_COACHING_GM_CLOSED_LOOP_V1.md)（首次提交`1aa5c2bacff2aaab80f4c7bb6c2b4c8c00f40d34`）；[本次范围归档](development/sessions/20261017_coaching_closed_loop_final_scope_v1.md)；既有[PR #1](https://github.com/chris2gao/nba2k22-gm-engine/pull/1)，已上传代码HEAD `5daeed8dc0001b5052dce1cfc97d6c22ee9317c3`。
- 基础版必须：**六项默认POE正式读写 + 1–30队整批预验证/逻辑事务/失败条件恢复 + 用户触发常规采集自动包含COACHDATA战术来源入SQLite与GitHub发布JSON + 两份正式角色手册**（`web_gm/manuals/GM_COACHING_OPERATIONS.md`、`docs/40_COACHING_EXECUTION_RUNBOOK.md`）并更新GM/执行基线入口。所有内容必须有真实代码/接口/回归集成测试。
- 主教练余18项：5Sim、2体系、1战术本（编码可用，未生产验收）；6教练滑块、4Freelance（只读）。玩家请求详细查看，**尚未批准统一转为可写**；单一对手Gameplan/18项具体防守/轮换保持只读。每字段独立认证后再提升production_enabled。
- `src/gm_core/coverage.py`旧`team_state.poe_*`应明确脱钩，改以新增`coaching_tactics`来源让GM读新原生字段；仍从现有`published/index.json→latest.json→batch_path`，无后台触发，不造第二个同步入口。仅原数据采集有`-Publish`才真正推送GitHub。
- 跨30队内存不存在硬件物理原子写；要求事前全部核验、批次批准、一致性验证、fsync预像日志、尽力条件rollback与`PARTIAL_UNRECOVERED`明确异常，绝不谎称所有失败能无损回滚。
- 开发完成后需要GM/执行模型每次分别按玩家批准的具体提案/批次工作；绝不代替用户批准真实游戏的30队修改。不再因未跑一个游戏月或不知模拟作用而阻止教练系统工程验收。

## 当前最高优先级：DEV-20261017-07 V2 19项球队级教练战术＋单对手整体防守

- 状态：`COACHING_V2_SPEC_PUBLISHED_AWAITING_CODEX`；[最新V2正式任务书](../../docs/development_tasks/DEV_20261017_07_COACHING_GM_CLOSED_LOOP_V2.md)（`3651e1d440d1fdba43a346cb8228b867889e29af`）；[完整上下文](development/sessions/20261017_coaching_scope_v2_19_plus_opponent_defense.md)。**前一条DEV07 V1“只有六POE是必需/其它18可选、指定对手防守以后再做”已作废**。PR#1现有六POE代码不代表V2已完成。
- 最新明确业务：五个`Sim*`仅玩家模拟比赛使用，GM不操作；球队默认需**19项**：六POE＋`PreferredSystem/ActiveSystem`＋`PlaybookID`＋六教练滑块`BenchDepth/RunPlayTendency/ZoneUsage/BenchUtilization/Tempo/HelpDefense`＋按1→4优先序配置的四个`FreelanceType`。主教练HEAD_COACH的设置映射到所属球队默认打法，不是全联盟共同slider。
- 用户当前PC UI报告六滑块可取1–100，但旧社区资料有0–100且BenchDepth具体单位存疑；Codex最小读/单项UI对照确定合法显示值→raw关系。可只读参考Kerr/Spoelstra/Popovich/Thibodeau等当前存档主教练值，不得捏造数值。
- 另一必需模块：**指定对手页面的整体防守理念**（原生GAMEPLAN8byte、18项候选），与单个对手的独立覆盖相关，不能推成全局。当前逐项防守读取器带`matchup_id/defender_id`，须最小差分确认“整体/All”对应owner/条目和`IsInUse`/继承/取消；若无法确认只能BLOCKED，不能误写个人对位或声称完整实现。
- V2闭环仍必须：30队全批预验证/受控写入/条件恢复＋玩家正常采集自动含战术源SQLite/JSON/GitHub发布＋GM/执行两本实用手册和基线接入。**不用快模拟比赛效果或大量无意义保存重启测试**，只做最小必要安全验证。游戏正式写入每批另需玩家批准。

## 2026-10-18 最新决策：所有游戏新数据更新只走全量，教练源不另开开发分支

- **这是最新范围裁定，优先于本文件中的历史规划段落**。用户已与Codex讨论并采纳全量刷新：脚本化完成、数据量不大，每次都更新所有已验证来源。正式数据更新唯一入口仍是`scripts/run_data_update.ps1`的`full_verified_v1`；不开发`COACHING_ONLY`、单来源/单队快照、跨不同来源日期组合发布、增量同步或独立教练latest。
- [DEV08全量教练源首次生产启用规划](../../docs/development_tasks/DEV_20261018_08_COACHING_FULL_REFRESH_FIRST_PRODUCTION_V1.md)已写入main（首次提交`d0da3ea34ec8d2e4b07aab638d66e4647caf2db7`）。该计划**不是研发新特性**：SQLite`coaching_source_captures/coaching_team_observations`、同RO会话采集与审计、19默认字段、29个对手整体防守、JSON`coaching/`、GM按batch读取均已随DEV07进入main，首次真实生产采集/上传目前尚无证据。
- 当前唯一待做的教练来源数据任务：由玩家下次**明确触发完整全量采集及按需-Publish**；Codex报告最新source coverage必须为`coaching_tactics=VERIFIED_OBSERVED_SAME_BATCH`、30队/19字段/29对手记录、SQLite、manifest/latest与GM源同批一致。任何失败只修该次真实阻断，不预开发单源采集，也不做比赛或反复保存重启验收。
- GM决定→玩家批准→执行模型内存写入和回读→玩家自行游戏/保存；下一次只有**玩家触发全量更新**后，GM才能从新已发布批次读到修改后的教练值。执行回执不能直接覆盖SQLite原始观察，也不自动采集/发布。
- 已同步最新`AGENTS.md`、Codex开发/数据基线32、33、状态34、数据runbook27、source registry24及GM教练手册的full-only规则。历史旧任务中的“单来源优先待办”作废。

## 2026-10-18 DEV09：NBA2K22 PC 当前终极联盟CPU滑块页 + MC主宰/佳得乐研究

- 已编写[DEV09三专项只读研发任务](../../docs/development_tasks/DEV_20261018_09_MC_MOVEMENT_TAKEOVER_GATORADE_RESEARCH_V1.md)；用户将其转交Codex：当前游戏位于终极联盟测试存档**CPU持球速度与持球加速度页面**，要优先就地只读记录画面原值及当前内存差分，找真正Movement字段，并核查MC/终极联盟底层共用但实际settings实例可能不同、HOF/CPU vs USER差异。
- 玩家已排除PC帧率和整体运行环境问题；中锋低持球属性导致的局部整套运球/篮球落地动作过慢，目标是两项Min的全局调整可行性，不准写普通球员能力，不动Game Speed/HOF。旧`slider_manager.py`静态地址及“拟真一键写入”不可信/会动其它设置，禁止本次直接使用。
- 另研究当前代MC**主宰类型**（须与充能/比赛激活分离）和Gatorade消耗品/每周锻炼额外体力槽/Gym Rat永久状态；先只读定位，服务端权益不可假造。**本次未批准任何游戏内存写入**；必要的GUI单值差分由玩家操作或在另行获准后于测试存档最小操作并恢复。
- [本次开发归档](development/sessions/20261018_mc_movement_takeover_gatorade_research_handoff.md)。研究不自动触发正式全量采集、GM回合或任何正式局写入。

## 2026-10-18 DEV10 — GM V4 phased development plan

- Master plan: `docs/development_tasks/DEV_20261018_10_GM_V4_FOUNDATION_DECISION_OBSERVABILITY_MASTER_PLAN_V1.md` (M0-M4). FIRST Codex delivery is M0 only: published data consumability, small queryable staff/player exports, consumer evidence and cash field semantics; no game writes.
- Observed issue: M02 staff.json manifest says 2,728,888 bytes / 1,458 employees, but current Web GitHub fetch returns empty content despite file SHA; Web GM cannot infer access from source audit. Large player catalogue and individual roster accessibility require live consumer tests separately.
- Financial anomaly: CLE/NOP/UTA/ORL cash near 2^32; signed 32-bit interpretations are unverified hypotheses, never silently replace raw values. `budget`, `cash`, `payroll`, `total_salary` not interchangeable.
- M1 financial & current-gen rules; M2 basketball/franchise knowledge and 30 team memory; M3 ANALYTICS decision packet plus five internal GM stages in one user-triggered decision task; M4 lifecycle feedback, issue inbox, and representative pilots. Feedback produced by normal player-triggered stages, never by unattended background work.
- Existing GM V3 five-interaction protocol stays effective until the new V4 contract passes real Web model verification and the player approves switching. Only the plan has been created; no implementation or game update is claimed.

## 2026-10-18 DEV10 V2 — Web GM / ANALYTICS / DEVELOPMENT SQLite-first

- Latest authoritative task: [DEV10 V2 SQLite-first master plan](../../docs/development_tasks/DEV_20261018_10_GM_V4_SQLITE_FIRST_MASTER_PLAN_V2.md). User offered authorized local terminal access for all three Web GPT roles. This access must be verified in each real Web chat; it has NOT been proven by the planning phase.
- **V2 overrides V1 M0 JSON paging/sharding**. Continue the existing full_verified_v1 capture and paired SQLite databases. Build immutable same-batch read-only local snapshots and a parameterized, limit-bound `gm_data_query.py` CLI for staff, active roster, global player pool, coaching, finance and picks. Only return small bounded rows/aggregates, not whole 2.7MB staff.json or 3383-model table. JSON remains for small cross-model GitHub handoffs and current publication compatibility.
- Strict roles: Web GPT facts SQLite read-only; Codex writes certified source only on authorized full capture; derived analytics/strategic feedback in separately writable `gm_workbench.sqlite` via controlled writers (M3/M4); no Web SQL access may directly edit source DB or game memory. Bind both DBs to career/batch/snapshot/data timestamp and GitHub publication status.
- M0 still includes unverified unsigned-like cash anomalies and original financial field semantic audit. First Codex delivery covers M0 only; requires actual read-only CLI validation by WEB_ANALYTICS, WEB_GM and WEB_DEVELOPMENT before `M0_CONSUMER_ACCEPTED`. Tool availability is not proof of machine connectivity. M1-M4 retained, with SQLite query/sidecar interfaces instead of enormous derived JSON files. Feedback remains player-triggered.
- Original [DEV10 V1 plan](../../docs/development_tasks/DEV_20261018_10_GM_V4_FOUNDATION_DECISION_OBSERVABILITY_MASTER_PLAN_V1.md) carries a supersession banner. No runtime database changes, game writes, or authorized terminal use occurred in this update.

## 2026-10-19 MyLEAGUE玩法全景研究：PC本世代终极联盟主战场

- 用户计划放弃以MC为主要模拟存档，改以NBA2K22 PC本世代终极联盟新开档运行30队GM V4；新局应独立save_id。M1/M2由Codex进行中，原五阶段仍玩家分别触发。
- 完整可持续扩充的[MyLEAGUE玩家操作/原生系统手册](../../docs/research/NBA2K22_PC_MYLEAGUE_PLAYER_OPERATIONS_AND_SYSTEMS_GUIDE_V1.md)已创建：16章，首页/日历、行政、教练、训练发展、球探/选秀、扩军搬迁、联盟新闻、排行榜/统计、全球设置、球队AI自动化、规则变化、休赛期与GM接管映射，并纳入用户提供的Gemini候选设置全集及外部资料来源。
- 用户已实机确认PC本世代很多全局设置与次世代一致；但PS5/Xbox Series 2K22新增MySTAFF/Prep Hub/Conditional Coaching具体专用机制不能未经PC菜单观察直接当PC事实。Gemini原文某些默认值/枚举/旧ADDR_TRADE/SETTINGS/SLIDERS地址尚未逐条认证；需Antigravity后续提供实机页面、实际值域与内存差分，补入手册，再独立规划MYLEAGUE_NATIVE_CONTROL层。
- **研究手册不授权任何游戏修改或自动接管**；已有教练19默认+18对手、交易等继续复用。GM可未来接管原生训练安排但仍禁止经营性直接改球员能力，世界级成长/伤病/工资帽设置由玩家批准。逐项确认GM已能执行后再关闭相应原生CPU自动化，以免休赛期无法签人/选秀。下一次玩家主动触发阶段更新时保留来源与反馈。

## 2026-10-19 MyLEAGUE实际GM能力审计/六人制服组/月度训练

- 新研究：[外部GM运营能力覆盖与月度安全训练方案](../../docs/research/NBA2K22_MYLEAGUE_GM_CAPABILITY_GAP_AND_MONTHLY_TRAINING_V1.md)；已同步修订[终极联盟玩法手册](../../docs/research/NBA2K22_PC_MYLEAGUE_PLAYER_OPERATIONS_AND_SYSTEMS_GUIDE_V1.md)，从人类可查看菜单转向外挂GM的`OBSERVED → ANALYSIS/DECISION → APPROVED EXECUTION → OUTCOME`覆盖审计，独立于现有M1/M2未验收设计PR #3。
- 玩家本世代实际UI可任命六人：CFO/财务、GM、主教练、助教、首席球探、训练师；当前`memory_field_profile.json`底层仍有8个staff岗位enum与8个反向指针槽，其中Governor/AssistantGM不能当作玩家UI已验证的可聘岗位，注意区别。主教练上任关联的Playbook/体系、助教/训练师加成实际公式待研究；已有数据读取但未有受控员工聘任执行闭环。
- 玩家确认训练类与2K20类似：球员导师影响徽章成长机会，团队/个体训练方向及强度，比赛+训练共用疲劳负担；老将/高分钟首发易过载，高潜年轻替补可在身体状况允许时更积极。但`source_catalog.json: injuries_availability_rotations`当前为`NOT_OBSERVED`，训练配置/伤病/疲劳/导师关系未认证读取；目前不应让GM基于假疲劳数据制定积极的每月高强度自动训练。首选`保守月度球队基准+少量目标球员例外`，无疲劳数据时原生自动或低强度HOLD；不能保证伤病为零。
- 下一步候选能力：累计疲劳/伤病与训练设置真实数据、六职位员工任免与人员市场、聘教练自动联动、CPU原生交易签约选秀自动化、导师、球探/休赛期阶段及历史事件账本；GM可新增信息不对称新秀/交易评估、长期预测等超出原生UI能力。**这些只是研究缺口，不直接给Codex新开发任务、不修改游戏，也不要求正在进行的M1/M2改范围。**

## 2026-10-19 NBA WORLD球员/媒体/赛场沉浸研究（不抢GM开发）

- 玩家最终次序：**先GM V4，随后球员系统，再做媒体系统**；媒体是高优先级的沉浸目标，不能只用“是否改变游戏数值”衡量其价值。独立研究文档：[NBA WORLD 人格、Obsidian媒体及NBA2K22赛场沉浸可行性](../../docs/research/NBA_WORLD_PLAYER_MEDIA_AND_BROADCAST_IMMERSION_FEASIBILITY_V1.md)。
- 研究证据：2K20 官方MyLeague士气化学反应+性格徽章；2K22社区阵容编辑Play For Win、Financial Security、Loyalty，为PC22字段线索，**本局尚未实机认证这些游戏内存地址**。用户设想“长期拒绝交易导致能力下降”与目前不准普通经营性直接修改球员属性的规则冲突，**不得按设想直接开发**；优先用外挂续约/交易请求/球员接受报价及已证实原生士气机制表达，任何超出既定规则的能力惩罚需玩家另行审议批准。
- NBA2K22 PC社区已存在Looyh NBA2K Hook（资源导出/加载日志/动态Mod/扩展插件线索）、Debug Unlock/Free Camera脚本和转播计分板Mod，证明部分改编空间；但**不证明**2K20破纪录叫暂停庆祝、记者/采访/社交观众图层仍存在于22，更不证明有可写事件触发器。分R0 Obsidian纯报道、R1外置赛场覆盖、R2原生转播UI资源Mod、R3原生事件/解说/动画注入四级，只读研究后再决定是否开发，禁止未经批准游戏修改。
- Obsidian原生Markdown+YAML+内链，可由未来Codex在玩家提供Vault路径权限后离线写文稿（不需要绑定未知插件）。媒体文章永远明确区分游戏事实、模拟报道/人物公开语句与传闻；每月/季后赛可先做，逐场真实赛后报道/即时场边采访须增加可信逐场或即时数据来源，现有数据仍缺game logs。

## 2026-10-19 GM V4之后：NBA2K22 PC竞技对抗与Sim Engine调校研究

- 用户确认发展次序：**先完成GM V4获得真实队伍建设与攻防决策能力，再独立调校NBA2K22 PC MyLEAGUE竞技引擎**，使竞技能力、对抗过程及博弈真实，而不是人/AI随便获胜；为后续球员、媒体沉浸生态奠基。
- 新研究基线：[竞技模拟与比赛引擎调校路线V1](../../docs/research/NBA2K22_COMPETITIVE_SIMULATION_CALIBRATION_ROADMAP_V1.md)。已初步检索Operation Sports本世代MyLeague sim研究、RES2 Current Gen、部分PC跨版反馈、Competitive slider比照及2021–22NBA统计基准。**不能直接套用社区整套数值；来源版本、玩法USERvsCPU/CPUvsCPU live/日历quick sim必须分开**，先动作/AI出手选择/犯规/战术响应，再投篮命中与联盟统计。
- 游戏世界级`WORLD_GAMEPLAY_PROFILE`只由玩家批准、稳定运行；GM按月仅调教练/战术/阵容等合法策略，绝不靠每月改变全局参数保证单队获胜。现有旧`docs/10_GAME_SETTINGS_AND_SLIDERS.md`自称权威但多个数值与效果未证实，旧`src/slider_manager.py`地址未经实机重新核验，不做一键写入。球员原始能力/潜力/徽章保持禁止普通经营性修改。
- 未来Antigravity取字段与内存真实地址/游戏消费验证，Codex按获批差分执行，分析模型比较赛场过程、联盟真实统计分布和GM战术效果；维持适量验证、不为找最优值长期停摆。**本轮只做研究文档，不开启调校开发或更改游戏。**

## 2026-10-19 玩家修正竞技调校范围：只针对NBA2K22实时3D赛场

- **新的权威文档**：[NBA2K22实时3D赛场引擎竞技调校V2](../../docs/research/NBA2K22_LIVE_COURT_ENGINE_CALIBRATION_V2.md)；前一版[竞技模拟调校V1](../../docs/research/NBA2K22_COMPETITIVE_SIMULATION_CALIBRATION_ROADMAP_V1.md)已经标记范围被覆盖。**用户明确不调日历快速模拟/Sim Engine，不以统计/赛季结果拟合作为项目目标。**
- 赛场唯一核心杠杆：**比赛Gameplay全局参数**（速度/加速度/防守/动作/疲劳/投篮与接触判定）、**球员Tendencies**（全局Tendency滑块 vs 个体球员真实倾向明确分开，后者现行普通属性/倾向禁写政策未自动改变，需要特别批准）、**球队教练战术**（19默认/18指定对手，手册/体系）及**AI攻防针对性临场调整/ACE覆盖**。CPU与玩家应凭篮球能力、战术对抗和操作公平竞争，不是通过CPU无解释加成确保结果。
- 重点用Operation Sports NBA2K22本世代RES2滑块反复调试经验、Eccentric关于先倾向后命中、Competitive体验作为候选，不直接照搬；**以玩家亲自打实时比赛/CPU对CPU观赛观察为主**，每次一个场上现象→模型查经验/定位相关机制→小范围配置差分→玩家再打后给出体验→保留/恢复，版本化LIVE_COURT_PROFILE。旧地址未经实机认证，不自动写游戏。
- **阶段顺序不变：M3 GM V4先完成，随后专项Live Court调校**；媒体球员系统之后，不把Sim Engine、训练/球员能力修改偷渡进新任务。当前文档只是研究规范。

## 2026-10-19 玩家已打通原生全局设置，Antigravity下一批原生GM控制点调研

- 玩家报告**之前交Antigravity查找的全局设置均已可以修改设置**；今后不再浪费查找时间重复扫描那些全局开关/滑块。M1/M2已合并main，M3 GM V4仍优先，Antigravity并行查操作入口。
- 新任务清单：[MyLEAGUE原生GM控制缺口发现V1](../../docs/development_tasks/DEV_20261019_MYLEAGUE_NATIVE_GM_CONTROL_DISCOVERY_V1.md)。P0：球队/个人训练与疲劳伤病读数、六职位员工任免、完整Playbook/得分选择/球员战术优先级、激活/首发角色、导师、ACE赛场覆盖；P1：真正合同签约裁员、休赛期阶段机、历史选秀大会选中与新秀归属、球探任务；P2：原生士气人格、逐场比赛/纪录新闻、老板商业、自然成长记录。
- 每项Antigravity交付须分别记录：真实UI、字段/类型/地址与对象身份、读能力、**实际执行操作及提交机制**、菜单退出/存档重开持久性、AI覆盖、效果证据和已验证范围。仅地址能读/设置页能显示不等于完成经营闭环；新增功能仍由玩家批准交Codex执行，不抢M3。
- 保留项目政策：不可普通经营性直接修改球员属性、潜力、徽章及倾向；原生训练/导师/招聘是合法的经营输入，球员个人Play Type若对应原始角色倾向需另获审批。旧世界级设置既然玩家已报告成功，不因开发记忆旧证据重开该任务。

## 2026-10-19 玩家纠正Native Control责任分工、M3设计审查

- 用户明确：[Native Control V2权威分工](../../docs/development_tasks/DEV_20261019_MYLEAGUE_NATIVE_GM_CONTROL_DISCOVERY_V2.md) **取代原V1中Antigravity工作分配**；Codex负责员工合同及任免、完整教练战术手册/球员角色/阵容（与已有交易签约教练执行器衔接）；外挂GM自建虚拟市场、球探/选秀/休赛期业务，Codex处理批准后的游戏合同/名单/新秀实际落地；**不要求Antigravity重新实现原生签约、选秀、球探、休赛期UI动作**。Antigravity已经继续找训练/导师/疲劳伤病/士气/赛场信息等原生读写接口，继续即可。
- 用户指出全真潜力/55项新秀数据会导致外部GM“全知选秀”，将来建议双视图：事实数据库保留真值，GM只看来源/资历/不确定性明确的虚拟球探档案，**尚不是M3工程阻塞**，也不能为了迷雾而修改游戏内球员能力。
- Codex PR #4（head `c3ce332`）Astra已完成M3A分析包与M3B独立30队GM五阶段/双边同版报价/portfolio冲突/策略状态的设计及15个合成场景，**没有M3运行实现、未在Web验证、正式30队仍UNASSESSED、V3仍生效**。研发侧审查认为可由Sol High按照设计包进入工程实现，重点 q_team_stats 真实来源、30队全员访问证据、双边同版接受、组合执行依赖、离线教练真实批次和持久状态；不为Cash/Web连接/单独引擎测试扩大交付。签约外部虚拟市场的商业逻辑与当前受控签约执行仍须区别，未来逐项接入。

## 2026-10-19 实时3D赛场AI与ACE研究优先顺序

- 最新研究交接：[DEV11球员决策/ACE临场教练调研V1](../../docs/development_tasks/DEV_20261019_11_LIVE_COURT_AI_AND_ACE_DISCOVERY_V1.md)。用户要先让球员AI做出合理投篮、传球、挡拆、跑位选择，**先查AI行为/战术调用与全局Tendency→临场ACE/攻防自动调整→最后调命中/运动/身体对抗**，只限真实3D比赛，不调日历Sim。
- 已有19默认+18对手教练受控写入，Antigravity不重建静态教练执行器而优先找**ACE实际控制范围**（玩家端/CPU端，自动进攻/防守，临场RUNTIME Coach/Gameplan实例、静态数据与live覆盖，是否每场重置、ACE四模式当前PC枚举）；并记录比赛前、节间、暂停后少量时点的动态状态，允许UNKNOWN，不把社区猜测视为已认证指针。Codex继续完整Playbook/阵容/角色实现。
- 2022 Operation Sports RES2本世代玩家为维持Play Physical选择关ACE，另一论坛用户指出ACE只作用于USER端，证据互有冲突；**开关不等于提高CPU教练智商**。长期若可受控运行时写入比赛计划，可以研究玩家批准的暂停/节间规则控制器，**目前仅研究不执行**，不承诺逆向/重编ACE内部算法。
- 当前项目仍不准经营性改个体球员真实倾向/能力/潜力/徽章；全局Gameplay Tendency可作为世界配置研究输入，今后若专项修改个体Tendency需玩家独立批准。用户主观实战体验与定向场上观察为调校主要反馈，M3优先级不变。

## 2026-10-19 用户最终限定实时赛场竞技：ACE原版开启，三方仅调Gameplay

- **最新权威研究：[NBA2K22实时赛场Gameplay全局参数V3](../../docs/research/NBA2K22_LIVE_COURT_GAMEPLAY_PARAMETERS_V3.md)**，覆盖前版Live Court V2中ACE动态控制部分及[DEV11 ACE实时控制探索V1](../../docs/development_tasks/DEV_20261019_11_LIVE_COURT_AI_AND_ACE_DISCOVERY_V1.md)。用户明确**不做C2实时内存改战术、C3外挂临场教练、不逆向修改ACE的决策算法**，无法常驻模型看比赛；已观察原版AI与教练会叫暂停、变更防守，接受其运行；**实时3D比赛ACE全程ON**。
- GM/Codex负责比赛开始前阵容、原生教练策略、Playbook、球员打法/个人倾向（个体倾向需明确批准设定与能力属性禁改边界）。之后游戏原版AI/ACE全程作场上临场调整。Antigravity不重复原生ACE实时对象逆向，之前已发现的全局GamePlay可读写接口作为来源即可。
- 用户+Web Development+Antigravity下一个竞技目标是**打磨Gameplay全局环境**：A运动8项上下限+Game Speed；B防守与接触/防守干扰；C投篮判定/覆盖和时机；D传球/控球安全；E Attributes全球作用倍率/疲劳；F犯规；G全球Tendencies（默认HOLD，与GM个人Tendency严格分开）；H真人操作/辅助与投篮模式。优先解决真实场上运动与攻防执行，不匹配赛季快速Sim统计、不先改个体能力/潜力/徽章。
- 继续采用玩家实时3D打球发现问题→按NBA2K22本世代社区资料定位参数小组→玩家批准差分→保留/回滚的反馈机制，适量试验；无后台监控，没有AI实时比赛干预。GM M3工程继续最高优先级，当前只是后续研究方案。
