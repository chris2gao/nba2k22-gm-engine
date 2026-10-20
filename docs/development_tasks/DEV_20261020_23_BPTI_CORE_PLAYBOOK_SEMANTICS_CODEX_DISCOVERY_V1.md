# DEV23 — BPTI关键战术手册语义与球员角色专项调查（Codex，限范围）V1

日期：2026-10-20 | 负责人：开发规划Web GPT | 阶段：RESEARCH_TASK_PREPARED / PLAYER_TO_TRIGGER_CODEX | 依赖：DEV19/21/22、R1–R4、M3-T/DEV14；**不自动启动游戏操作/编码/测试/写入**。

## 1. 为什么值得做，什么不值得做

现有M3-T和DEV14已能读取当前球队同名Playbook的68槽、按同批目录写入已存在CRC、读取/提案4个有序PlayTypes及Initiator，已能通过个人18项防守字段和具名48项球员Tendencies提案。**原生字段已知 ≠ 战术CRC是什么、由谁发起/谁受益、哪名球员执行、在ACE中如何调用已经被证实。**

对BPTI而言，最关键缺口是连接`SystemCard“如何创造第一优势/第二优势”`与`本队某条可实际选择的战术`的语义桥梁。如果不研究，B2仍能做coach/role等粗粒度映射，但对勇士Motion/公牛Midrange/掘金Elbow等场景无法有把握地推荐某项Playbook改动；不得把"可写CRC"当"已能执行复杂进攻链"。

**价值高的是核心战术语义/角色映射，不是把全部CRC解码完、拆出黑盒ACE进攻选择公式、或证明真实NBA战术必然在日历模拟里发生。** 本研究不作为B0/B1的前置阻断；在B1确定首批SystemCards场上动作需求后开启，支持B2关键映射和B4经营配置。若游戏当前页面/现有静态目录能更早提供证据，可先做无代码静态梳理，但不因本文件自动触发Codex。

## 2. 开发者必须先读

- 最新main `AGENTS.md`、`docs/DEVELOPMENT_BOUNDARIES_AND_VALIDATION_POLICY.md` V2；
- `docs/development_tasks/DEV_20261020_22_BPTI_RESEARCH_TO_CODEX_PHASED_HANDOFF_V1.md`；
- `docs/development_research/BPTI_R1_BASKETBALL_SYSTEMS_DEEP_RESEARCH_V1.md` 十体系和五级球员自主；
- `docs/development_research/BPTI_R3_NBA2K22_NATIVE_MAPPING_AND_CONFLICTS_V1.md`；
- `docs/DEV14_STATE_IO_RUNBOOK.md`、`web_gm/manuals/GM_M3_TACTICAL_WORKBENCH.md`、`web_gm/manuals/GM_DEFENSE_AND_TEAM_PLAYBOOK_POLICY_V1.md`；
- `docs/research/NBA2K22_TACTICAL_ECOSYSTEM_AND_PLAYER_BEHAVIOR_RESEARCH_V1.md`、`docs/research/NBA2K22_TACTICAL_RELATIONSHIP_EVIDENCE_V1.md`。后者部分Tendency阈值和球权规则只是社区/研究假设，**不能当作本机引擎已验证定律**。

## 3. 研究目标与优先级（不要全量解68×30）

按首批**可影响三种代表篮球文化**的动作类型调查，而非按CRC数盲目覆盖：

**P0：可执行性底座**
- 本队68槽，至少能静态取得每个有效槽的`slot_index / native_crc_or_enum / raw_label_if_available / play_type_enum_if_available / source_batch_id / team_and_book_identity`；**无可认证PlayType或名称则UNKNOWN**。
- 球员4个有序PlayTypes/Initiator与本队可用战术类型之间的静态匹配；能发现真正`STATIC_PLAY_TYPE_UNSERVED`和`TYPE_MATCHED_ONLY`，但PlayType相符不保证战术第一受益人。
- 通过当前游戏**战术编辑/分配页面**确认名字、类目、通常安排给的球员/位置；若可以合法只读定位相关内存结构，记录复现方法，不把这一步自动升级为真实ACE运行效果。

**P1：对首批BPTI案例最重要的动作**
- Warriors/MOTION：无球射手(Offscreen 3、Floppy/Pindown)、掩护后切入、Hand-Off/连接者与二次接应。
- Bulls/ISO-MIDRANGE：wing isolation、midrange pull-up/post face-up，弱侧/第二持球选择。
- Heat/防守身份：个人防守已经能按对手设置，进攻调查仅需对应Butler持球/篮下创造及Bam手递手/高位策应等若有真实可映射战术。
- 拓展1–2组：Spread PnR（持球者/顺下/外弹/反制）、Post/High-Low、Point-Center/Elbow。防守Scram/Peel或ACE现场阅读若无原生专用控制，不强制寻找假按钮。
- 关键应急类型：ISO late-clock、reset/re-screen；除非游戏真实有可识别菜单或行为证据，否则仅保留篮球意图。

## 4. Codex调查步骤（**只有玩家独立触发本任务后才实施**）

阶段A：**只读静态目录审计**。盘点本仓库`config/state_io_native`、球队本队book/CRC原生目录、M3-T安全投影和已存capture中能确定哪些PlayType/槽/枚举/名字；输出已知映射和UNKNOWN，不重做DEV14、不能拿猜测的CRC+球员一对一关系当事实。

阶段B：**游戏当前页面辅助调查**。如果玩家提供当前存档并将游戏停在编辑Playbook/Assign Plays/球员PlayType或运行时战术菜单页面，Codex使用本项目已有授权只读进程工具或已认证采集方式研究可见条目与内存/对象身份，必要时由玩家切换UI以A/B比较。未准备游戏页面/进程时先完成阶段A并生成`REQUIRES_PLAYER_UI_STEP`，不得凭离线样例冒充本机验证，也不要运行全量正式采集、模拟赛季、修改存档、游戏内存或任何教练/战术设置。页面切换可由玩家亲自完成；Codex的进程访问严格只读。绝对地址/原始进程dump不进GitHub。

阶段C：**建立语义映射**。仅对证据足够的核心动作记录：`game_version_and_platform`、`play_identifier_and_book`、`native_type`、`visible_name`、`entry_actor_role`、`intended_primary_option_role`、`known_secondary_role`、`observed_vs_inferred`、`evidence_ref`、`coverage_status`、`uncertainty`、`fallback`。同一CRC若随阵容/角色/Assign菜单产生不同受益人，必须多态表示并保留冲突，不可强制唯一受益球员。
- **三个不同证明层**：`UI_OR_STATIC_LABEL_VERIFIED`（菜单字样、类型、槽） / `RUNTIME_ASSIGNEE_OBSERVED`（当前分配指定人） / `IN_GAME_EXECUTION_OBSERVED`（真实比赛AI有实际行动证据，另需批准比赛观察）。不能从第一层自动推出后两层。

阶段D：**最小交付和停止**。产出Markdown和可机读映射建议（如现有知识文件补充），列出`PLAYTYPE_COVERED`、`TYPE_MATCH_ONLY`、`BENEFICIARY_UNKNOWN`、`UNSUPPORTED`和明确的后续一两个阻断。可以提出下一批扩充清单，但需玩家另行批准，不自动穷尽所有68槽、全部Playbook或模拟AI行为。

## 5. 原生边界与验收

- 日常GM不得修改`OVERALL_DEFENSE`、任意其它队书、未经确认的`coach.PlaybookID`，不得修改Ability/Potential/Badge/身体；游戏写入/切档/新采集/自动测试/新开发模块均不属于此只读调查。
- 静态最低验收：能够对已观测核心Playbook槽说明标识、证据层级及可能的PlayType匹配；至少三种代表哲学（Motion、Creator-Midrange、Adaptive防守所需进攻支援）都列出已知可行方向和具体不足；未知部分返回HOLD而非预设定数值。
- 是否影响BPTI里程碑：**不阻断B0/B1与B3历史seed**。B2/B4可以对已有获认证原生行为实现部分支持；若首批三队重点篮球优势的实现依赖尚未识别的战术受益人，相关Playbook动作保持BLOCKED/RESEARCH，必须专项解决后才可宣称该球队的核心打法完全可落地；不因其它上千种游戏战术未破解而阻断全项目。
- 如果专项结束仍无法确定某细节，说明证据/工程限制和低保真替代方案即可；不重复试验、擅自增加测试或扩张成全量逆向项目。

## 6. 与Antigravity数据源扩展的关系

Antigravity负责赛程、逐场赛果、球员Box Score等**历史比赛事实的采集**；本Codex任务只负责**战术控制语义**。`Playbook Native Mapping`属于慢更新的本地目录与同批有效身份；不要要求Antigravity为了获得每条战术CRC语义而延迟逐场数据源上线。两项可以按玩家触发并行进行，Codex将结果交BPTI B2/B4，Antigravity源头结果交M0数据消费/GM分析链。
