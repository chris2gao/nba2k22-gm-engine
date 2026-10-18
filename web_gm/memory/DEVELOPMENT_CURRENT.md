# Web GPT · 开发规划基线当前记忆

- role: WEB_GPT_DEVELOPMENT
- memory_version: 1
- last_reviewed: 2026-10-17
- state: COACHING_IMPLEMENTATION_TASK_PUBLISHED_AWAITING_CODEX
- linked_codex_state: `docs/34_BASELINE_CURRENT_STATE.md`（**Codex 状态索引，不在此复制更新**）

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
