# Web GPT · GM 基线当前记忆

- role: WEB_GPT_GM
- memory_version: 4
- last_reviewed: 2026-10-17
- state: GM_V2_EXTERNAL_GM_WIN_FIRST_MAX3_ROUNDS
- career_hint: `mc_haliburton_2021`（下一任务重新验证）
- source_batch_id: `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`
- data_updated_at: `2026-10-17T11:50:28.464724+00:00`
- game_date: UNKNOWN
- month_closed: false
- last_decision_id: GM-20261017-M01-R01
- decision_version: 1
- player_approved_actions: `GM-A01,GM-A02,GM-A03,GM-A04,GM-A05,GM-A06,GM-A07`
- player_approval_scope: STRATEGY_RESEARCH_NONBINDING_INQUIRY_ONLY
- player_approval_evidence: EXPLICIT_USER_MESSAGE_2026-10-17
- game_writes_approved: false
- executed_game_changes: NONE_RECORDED

## 玩家最新GM机制（2026-10-17）

- [完整外挂GM决策机制v2](../GM_DECISION_MECHANISM_V2.md)
- [修订GM决策SOP v2](../GM_DECISION_SOP.md)
- [交开发规划基线的能力需求](../decisions/mc_haliburton_2021/20261017_GM_V2_DEVELOPMENT_HANDOFF.md)
- [本轮机制纠偏会话](gm/sessions/20261017_GM_V2_MECHANISM_CORRECTION.md)
- 交易由外挂系统的双方独立GM达成一致，再提交玩家批准，由Codex落实；不需要游戏内CPU交易逻辑同意。
- 赢球和长期争冠优先；士气/化学反应是次级观察因素，不阻止有事实依据的轮换。
- 每月或季后赛每轮由玩家触发GM节点，默认一次决策，最多三轮；内部多次报价不计入对话回合。
- 上轮 MKT-01/MKT-02仍只是经批准的询价，没有双方定案或已批准的交易执行。没有新游戏写入授权。

## 权威交接文件

- [原始30队×12模块v1提案](../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_PROPOSED.md)：保留首次提出时的 PROPOSED 历史状态，不视为当前审批索引。
- [玩家逐项审批记录（当前有效）](../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_APPROVAL.md)
- [机器可读审批 JSON](../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_APPROVAL.json)
- [本次审批会话](gm/sessions/20261017_M01_LEAGUE_GM_ROUND01_APPROVAL.md)
- [初次GM会话](gm/sessions/20261017_M01_LEAGUE_GM_ROUND01.md)
- [同批量化分析](../../docs/gm_analysis/2021-2022_SIMPLE_PICKS_V1_ANALYSIS_ONLY.md)

## 已批准，但需正确理解状态

1. `GM-A01`：30队战略方向获批作为经营基线，不等于任何球队字段已写入。
2. `GM-A02`：保护国王 Tyrese Haliburton、保留表现良好的争冠核心；SAC 的 Tyrese Haliburton (slot=1235) 与 Ty Hali (slot=184) 不得混淆。
3. `GM-A03`：数据异常核验需求获批、尚未执行。UTA 米切尔仅2场、Oni仅1场；CLE/NOP/ORL/UTA cash存在约42.9亿异常值。
4. `GM-A04`：GSW/UTA/DAL/CHI/IND 战术与轮换研究获批、尚未执行；没有数值 setter 授权。
5. `GM-A05`：MKT-01（CHI/DET，Grant）和 MKT-02（CHA/IND，Turner）只批准非约束询价/研究；交易未被批准，CBA和执行能力仍 UNKNOWN/NOT_VALIDATED。
6. `GM-A06`：制服组/伤病/轮换/门票/CBA信息补全需求获批，未启动采集和开发。
7. `GM-A07`：保持普通球员能力编辑禁止、历史重力和历史新秀注入不执行；MC故事保持关闭。

## 下一阶段优先级（需要玩家另行触发对应角色/任务）

- **P0 ANALYTICS / DATA**：核验 UTA 小样本原因可否观测、SAC 同名身份及 cash 异常；数据缺失保持 UNKNOWN，不改变 `published/` 事实。
- **P1 GM**：研究 GSW/UTA/DAL/CHI/IND 的战术适配与合理轮换，提供新的可验证候选数值或数据需求，不自动写游戏。
- **P1 GM + ANALYTICS**：研究两组非约束市场询价，更新双方动机和可能反报价，核实真实筹码、工资差及 CBA 缺口。
- **P2 DEVELOPMENT**：制定 staff、伤病、轮换、票务时间窗与正式交易合法性/执行器的开发和验收规范；不要假定已有生产接口。
- **新的 PLAYER APPROVAL GATE**：任何真正要执行的操作需新决策版本、真实对象/原值/目标/回读条件与明确批准后交 Codex。当前无游戏写入授权。

## 固定约束

当前最新生产批次及 game_date 每轮重新读取 `published/index.json` / `latest.json`；不沿用旧批次作为永恒事实。现实比赛表现优先。历史选秀1984–2020逐届循环，但当前实际进度需要玩家确认。简单选秀权仅当前后三届（本批2022–2024），按最新记载所有权核验。普通能力修改禁止，MC成长故事关闭。合同完整 CBA、精准伤病与轮换、OVR仍未观测；严格区分 OBSERVED/PROPOSED/PLAYER_APPROVED/EXECUTED。
