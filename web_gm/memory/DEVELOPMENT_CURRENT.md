# Web GPT · 开发规划基线当前记忆

- role: WEB_GPT_DEVELOPMENT
- memory_version: 2
- last_reviewed: 2026-10-17
- state: COACHING_V2_IMPLEMENTATION_AND_ISOLATED_ACCEPTANCE_IN_PROGRESS
- linked_codex_state: `docs/34_BASELINE_CURRENT_STATE.md`（**Codex 状态索引，不在此复制更新**）

DEV07 Codex 已在 PR#1 分支继续实施 V2，不再处于代码未开始状态。当前证据、字段门槛和剩余工作只读 [Codex 状态34](../../docs/34_BASELINE_CURRENT_STATE.md)与[集成报告](../../docs/development_reviews/DEV_20261017_07_COACHING_INTEGRATION_REPORT.md)。已建立 [GM 操作手册](../manuals/GM_COACHING_OPERATIONS.md)及 [Codex 执行手册](../../docs/40_COACHING_EXECUTION_RUNBOOK.md)。main 部署、完整19项及实际生产来源发布未完成，不得宣布整项交付完成；本条只是工程交接索引更新。

## 已知工程事实

- GM v1.0 M1–M6 的 Python 核心、命令行分析准备、提案协议已由 Codex 实现；v2 双方谈判、v3 正式王朝经营仍未全部实现。
- 最新来源已包括 30 队赛季胜负/累计统计、球员 55 项能力、部分球员赛季表现、员工关联、简单选秀权；玩家将薪资采集需求限定为当前大名单工资。
- 上一次 Web GPT 的 30 队独立量化分析已写到 `docs/gm_analysis/`；这是网页分析角色，不应每轮交给 Codex 重新做。
- 现有 Codex 数据采集/开发基线为 `docs/32`、`docs/33`，它们与本 `web_gm/baselines/DEVELOPMENT_BASELINE.md` **分属不同执行角色**。

## 待做（由玩家按需触发）

- 维护 Web GPT 需求文档与 Codex 工程开发任务书：例如 GM v2 交易谈判、多模型交接、对话基线协议的后续自动化可行性、单来源生产更新。
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

- 状态：`COACHING_CLOSED_LOOP_SPEC_PUBLISHED_AWAITING_CODEX`，**代码尚未开发、PR #1仍是六POE单队技术能力，未合并**。用户不再要求“快速模拟胜率效果验证”；教练机制完成以工程闭环为准。
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
