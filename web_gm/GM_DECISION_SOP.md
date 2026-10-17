# 网页 GM v1.0 工作规程

本规程只在玩家明确说“开始 GM 回合”后使用。新数据、发布回执、模拟报告及 ANALYSIS_ONLY 准备包都不是启动授权。Python 负责数据整理和计算，网页 GPT 负责篮球经营判断，玩家批准具体方案，Codex 另行执行。

## 1. 读取当前规则和数据

读 `GM_INSTRUCTIONS.md`、文档 26/29 和 `config/gameplay_policy.json`。`config/gm_policy.json` 是待玩家确认的经营配置，其生命周期阈值和偏好不能直接成为已确认球队战略。

从 main 的当前局 latest.json 看 `data_updated_at`、`uploaded_at` 和游戏日期，再按 batch_path 读取来源覆盖、联盟规则、计算结果、球队及名单。维持当前时间戳同步方式，不新增 JSON 哈希、下载复核或逐字段同步验收。source_commit/rules_commit 保留作引用；未知时标 UNKNOWN，不编造。

可使用玩家明确触发生成的 gm_prepare 分析包，每队有独立 JSON 和 12 个模块；它是事实/计算准备，不是已经完成的篮球经营决策。模拟模式必须保持 SIMULATION 标识。

## 2. 执行必要计算

所有数值判断引用 `run.json` 的 calculations、已发布 calculations.json，或 Python/SQL 工具新算的结果。保留计算版本、输入、单位及来源批次。缺少 OVR、年龄、潜力、战绩或合同，返回 UNKNOWN，不使用 75、25 岁、500 万等默认值。

网页没有计算工具时，将如下请求交给玩家带回本地：

```json
{
  "career_id": "PLAYER_SELECTED_CAREER",
  "source_batch_id": "PLAYER_SELECTED_BATCH",
  "operation": "win_percentage",
  "inputs": {"wins": null, "losses": null}
}
```

可用操作：difference、observed_sum、distribution、win_percentage、efficiency、field_changes、roster_changes、salary_exchange、draft_year。上例缺少真实胜负时应得到 UNKNOWN，不能由模型补数。

## 3. 每队独立审查

逐队完成 strategy、roster、staff、offense、defense、trades、contracts、draft_free_agency、development、business、culture、worldline 共 12 个模块。每项分别写已知事实、关键分析、缺失数据、战略建议、优先级及能否提出可执行操作。

区分 OBSERVED、CALCULATED、CONFIGURED、REFERENCE、UNKNOWN；每个模块给 READY、PARTIAL 或 BLOCKED，无数据时可 NOT_EVALUABLE。某项缺失不能阻断其余 30 队审查。

每队说明短/中/长期目标、阵容问题、资产保护、老板/文化参考、生命周期依据，以及相对前次的变化。没有真实战绩时保留 UNDETERMINED，不按工资额或球队历史名气分类。CHAMPIONSHIP/CONTENDING/RISING/COMPETITIVE/RETOOLING/REBUILDING 是候选经营状态，不是预测冠军。

`docs/team_dossiers` 中的文化/经营哲学只能列为 REFERENCE，预定交易、历史冠军、球员评分和未来管理层不能成为当前事实。新方向默认 PROPOSED，不改正式球队档案。上一轮未经批准的建议不能写成“已确认决定”。换局、读旧档或另开世界线时，核对存档及时间分支；不得沿用未来战略。

## 4. 联盟市场讨论

先从各队独立需求形成兴趣或询价，再讨论双方利益。v1 不自动撮合固定交易，不生成选秀权所有权，不给缺失能力的球员估造价值。双方有动机、主观估值可接受，均不表示成交或 CBA 合法。

v1 的完整 CBA 与双向谈判属于后续 v2，正常交易合法性为 UNKNOWN；明显身份冲突/重复资产/受保护玩家等直接列为阻止项。已配置工资帽减总薪资只叫静态 proxy。

玩家已确认选秀权采用简单交易：仅年份、轮次、原球队和当前持有球队，不使用保护或交换权。读取本批 `draft_assets.json` 的已验证记录，使用 `next_draft_year` 通过 Python 的 `draft_pick_window` 计算接下来三届年度选秀窗口；超过窗口的选秀权不能加入方案。资产使用导出的 `asset_id` 和 `offering_team_id`；本地校验器从本批记录核对权属和年份，不接受模型自填的 `observed_owner` 作为证据。游戏年份和历史新秀届次不可混用。

不按薪资自动增加 POE，不提出未登记或越界的策略值。对球压迫旧注释 0–4 与实测 7 冲突，目前不提供该字段的具体改值方案。

## 5. 汇总具体待批准方案

每项使用 decision_id、version、career_id、source_batch_id、teams、operation、evidence、calculation_refs、expected_effect、data_gaps、requested_approval；默认 status=PROPOSED。

evidence 引用本批文件和字段，例如 `{file: teams/IND.json, field: state.total_salary, availability: OBSERVED, source_batch_id: ...}`。calculation_refs 引用准备包中的明确计算 ID，例如 `IND.observed_roster_salary_sum`；UNKNOWN 计算不能充当确定结果。

明确区分：

| 阶段 | 意义 |
| --- | --- |
| 战略建议 | 经营方向候选，无执行权限 |
| 交易兴趣/询价 | 意图讨论，不是报价已被接受 |
| 正式提案 | 具体资产与条件，仍待数据/规则审查 |
| 数值/结构检查通过 | 只说明对应检查完成，不等于合法或获批 |
| 玩家具体批准 | 只有玩家明确批准该方案版本才成立 |
| EXECUTED_VERIFIED | 由另行触发的执行窗口提供实际执行及回读证据 |

外部模型自写 approved=true 或 EXECUTED_VERIFIED 不构成人类批准/执行证据；v1 核心不接受升级这些状态。

## 6. 世界线与人物限制

本局事实 GAME_REALITY、历史参考 HISTORICAL_REFERENCE、待批准 PROPOSED_WORLDLINE 分开记录。到游戏年份 2026 的参考锚点为 1988；后续须结合玩家确认的进度，不用系统日期自动推进。

历史参考可影响文化和战略讨论，不强制冠军、交易或成长。普通属性/潜力/徽章/倾向/动作/性格改值禁止；MC 成长继续禁用。历史重力只能形成有参考来源、原值/拟议值、计算、期限和恢复办法的专项待批准方案，不附带修改权限。

## 7. 交付玩家并停止

交付 30 队独立结论、联盟讨论、具体待批准方案、缺失数据和计算请求。保留来源与规则版本。未批准方案保存到外部 gm_state，不回写 LIVE_MEMORY 数据。

结束本轮。玩家决定是否批准、是否找 Codex 执行，以及何时再次采集或决策。不得启动其他模型、后台执行、采集或发布。


## 8. 与网页版三基线及持久记忆的衔接

本 SOP 由 `web_gm/baselines/GM_BASELINE.md` 引用；每个新 GM 窗口启动先读 `web_gm/memory/GM_CURRENT.md` 和当前相同数据批次的 `docs/gm_analysis/` 报告，而不要求 Codex 再次整理 GM 分析。量化加工是 `web_gm/baselines/ANALYTICS_BASELINE.md` 的责任，技术开发规格是 `web_gm/baselines/DEVELOPMENT_BASELINE.md` 的责任。参见 `docs/35_WEB_GPT_BASELINES_AND_MEMORY_PROTOCOL.md`。

玩家触发的本轮 GM 结束后，按许可把经营结论/待批准提案单独保存在 `web_gm/decisions/<career_id>/` 等非事实路径，写入 `web_gm/memory/gm/sessions/<run_id>.md`，再更新 `GM_CURRENT.md`。未经批准的经营判断保持 PROPOSED，不修改 `docs/team_dossiers/` 正式档案、不自动通知 Codex 执行、不擅自采集或进入下一轮。
