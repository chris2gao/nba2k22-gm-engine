# Web GPT · 数据整理分析基线当前记忆

- role: WEB_GPT_ANALYTICS
- baseline_id: `WEB_GPT_ANALYTICS_V2`
- method_version: `ANALYTICS_DECISION_READY_V2`
- memory_version: 2
- last_reviewed: 2026-10-18
- state: `BASELINE_V2_METHOD_READY_NO_NEW_ANALYSIS`
- current_observed_published_batch: `2021-2022_M02_DEC12_FULL_20261018_bee1cb016256_e94b241a_TS2`（核验时最新；**下一任务必须重新读latest**）
- current_observed_game_date: `2021-12-12`（玩家确认）
- previous_comparison_candidate: `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`
- last_completed_analysis_batch_id: `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`（以前完成的旧版初评）
- latest_methodology_session: [20261018_decision_ready_v2_baseline](analytics/sessions/20261018_decision_ready_v2_baseline.md)

## 正式方法和交付

- [新版方法规范：ANALYTICS_DECISION_READY_V2](../../docs/gm_analysis/ANALYTICS_DECISION_READY_V2_METHOD.md)
- [分析基线V2](../baselines/ANALYTICS_BASELINE.md)
- 历史已发布的 [30队量化报告](../../docs/gm_analysis/2021-2022_SIMPLE_PICKS_V1_ANALYSIS_ONLY.md) / [原JSON](../../docs/gm_analysis/2021-2022_SIMPLE_PICKS_V1_ANALYSIS_ONLY.json)。它们不是M02新分析。
- 此次完成的是**基线和方法文档升级，不是M02分析执行**；本次`execution_mode=NOT_EXECUTED`，未计算或发布新的M01→M02结果。

GM要求V2放弃**默认长篇排行榜**，改为四项决策支持：
1. 30队简短诊断：阶段候选、区间战绩、核心与替补、攻防问题、教练与阵容是否匹配、内部改善与人才缺口/交易需求证据。
2. 相邻同存档同赛季批次的球员55项/潜力和名单、合同、简单选秀权差分；身份必须可信，旧`roster_changes`的姓名+FaceID只作候选，不是稳定身份。
3. 同批19项教练默认设置与按需18项对手OVERALL防守适配、异常和优先复核摘要，不复制870组原始数据。M02教练源`VERIFIED_OBSERVED_SAME_BATCH`；M01无教练来源。
4. 进攻特征、eFG%、3PA率、估算TOV率、场均得失分等确定性指标；`poss`的原生攻守语义未认证前，不能称结果为标准ORtg/DRtg/NetRtg。

每轮玩家授权发布时，在`docs/gm_analysis/<career_id>/`新建一组五个文件：`_ANALYSIS_ONLY.md`（简明报告）、`_TEAM_DECISION_TABLE.md`、`_CHANGE_TRACKING.md`、`_METHOD_AND_SOURCES.md`、`_ANALYSIS_ONLY.json`（完整证据）。每个报告必须绑定两批（如适用）、game_date、规则、计算版本/方法、身份匹配等级和未知项。

## 下一次任务入口和明确缺口

1. 新窗口先读本CURRENT、方法规范、当前`latest.json`和选定的历史批次，重新判断当前真实latest；不要默认M02永远最新。
2. 验证可比性后用安全Python/SQL执行已有真实来源的30队、教练与区间计算；身份不足部分标`HIGH_CONFIDENCE_TEMPORAL_CANDIDATE` / `UNKNOWN`，不把候选成长当确定事实。
3. 需要可靠永久跨批球员键 → `DATA_SOURCE_REQUEST: PERSISTENT_PLAYER_IDENTITY`；`poss`语义 → `DATA_SOURCE_REQUEST: POSSESSIONS_SEMANTICS`。不要求单来源重新采集（当前采集全量-only）；缺口不妨碍其他分析。
4. 仅按玩家当前任务授权发布新五文件，回读，写对应session，最后更新本CURRENT；交接链接给GM，不自动开启GM。

## 权限边界

分析不改`published/`、`latest.json`、原数据库、Release ZIP、正式球队档案、普通球员能力、游戏内存或执行脚本。五Sim只读禁写、Tempo语义UNKNOWN、`is_in_use_raw=0`不等于防守关闭；逐人分钟与训练不在目标。源码可用则按实际Python运行方式报告，不冒充`gm_prepare.py`原样执行。单笔交易/签约、具体教练raw、历史重力都由GM玩家审批与Codex另行执行。
