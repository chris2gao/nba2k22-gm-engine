# 2021–2022 赛季 GM 长期时间线索引

- season_id: `2021-2022`
- career_id: `mc_haliburton_2021`
- season_gm_baseline: `2021-2022`（一个游戏赛季一个派生 GM 决策聊天，赛季内各节点沿用同一聊天）
- current_window: `GM-S2021-2022-W02`（本赛季同一聊天最新已归档决策节点，未发生新游戏月份确认）
- last_confirmed_exact_game_date: `UNKNOWN`
- current_progress_hint: `2021-11`（来自既有历史玩家进度，不是本批实测日期）
- index_created_real_date: `2026-10-17`
- policy: `PLAYER_RULES_20261017_V3` + `WEB_GM_DECISION_MECHANISM_V2`
- execution_state: `NO_GAME_WRITES_APPROVED_OR_EXECUTED_IN_W01_OR_W02`; W02新交易提案仍未获批准

## 本赛季 GM 决策节点时间线（整季沿用同一 GM 聊天）

| 顺序 | 游戏时间范围 | 窗口 / 回合 | 基准数据 | 经营记录与最终状态 |
| --- | --- | --- | --- | --- |
| 01 | 2021年11月附近，**精确日 UNKNOWN**；没有确认月终 | `GM-S2021-2022-W01 / R01` | `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2` | [本轮完整决策链](windows/W01_GM_20261017/ROUND_R01_RECAP.md) · 已批战略/研究/非约束询价，所有游戏修改暂缓 |
| 02 | **与W01相同的未知日期检查点；没有新的发布批次，不是新月月结** | `GM-S2021-2022-W02 / R01`（同赛季聊天已触发的专题续议） | `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`（与W01完全相同） | [本次决策归档](windows/W02_GM_20261017/ROUND_R01_RECAP.md) · [30队同批基线](windows/W02_GM_20261017/TEAM_BASELINE.json) · CHI/DET格兰特具体交易仅PROPOSED；CHA/IND暂不成交；无写入 |

## 本赛季关键时点的权威事实与文件

1. [W01 30队冻结对比表](windows/W01_GM_20261017/TEAM_BASELINE.json)：球队赛季累计战绩、进攻/防守输出、薪资、士气相关观测、若干团队战术字段，不能当成11月独立统计。
2. [W01 R01 决策链](windows/W01_GM_20261017/ROUND_R01_RECAP.md)：包括游戏时间/现实生成时间区分、战略结论、审批、暂停执行和下轮承接条件。
3. [初次全联盟30队经营提案](../../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_PROPOSED.md)：历史原始 `PROPOSED` 版本，不覆盖旧文案。
4. [玩家审批回执](../../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_APPROVAL.md)：7项仅限战略、研究和非约束询价。对于是否已执行以独立执行回执为准。
5. [GM v2 机制](../../GM_DECISION_MECHANISM_V2.md)：外部双边谈判、胜率优先、士气次级、每次最多3回合。
6. [最新 GM_CURRENT](../../memory/GM_CURRENT.md)：只作快速入口，窗口历史以此处文件为准。

## W02 后最新待处理事项（W01历史记录不变）

- **最新节点 W02/R01 是同批专题续议，而非新的游戏日期/月度数据**；此时仍不得计算相对W01的新增战绩。
- [W02正式待批准提案](../../decisions/mc_haliburton_2021/20261017_W02_SAME_SNAPSHOT_GM_PROPOSED.md)：`GM-W02-A01` CHI将Coby White + Derrick Jones Jr. + 持有的2022年POR首轮换DET Jerami Grant，外挂两队GM在此价格达成模拟经营层共识，**玩家尚未批准且交易执行器未验收，绝对未成交**。
- `GM-W02-A02`：CHA/IND旧MKT-02按当前样本决定 `NO_DEAL`，不锁资产、不授权交易。
- GSW防守、UTA米切尔缺席原因、DAL防守继续观察；SAC玩家哈利伯顿继续保护。W02无游戏写入、无新赛季事实。
- 玩家如批准W02-A01，仍必须先由执行端重新核验最新存档与执行器；后续有新赛季批次时，GM需要重新估价，不能直接按本批交易。
  
## 当前窗口里必须保留的判断

- 76人16–3、篮网14–5、湖人15–5、国王14–5；保护现有强势核心，不照搬现实历史赛季交易。
- 国王实役 Tyrese Haliburton vs Ty Hali 同名身份冲突；以正确球员身份进行所有审批和下一次分析。
- 勇士9–9、爵士5–13、活塞2–16：下次判断是否出现扭转，要对比新的同赛季数据。
- `MKT-01` 公牛/活塞格兰特、`MKT-02` 黄蜂/步行者特纳：只处于市场询价历史，**都没有正式双方GM一致的交易协议和执行批准**。
- 已批准 `GM-A01..GM-A07` 的范围是战略、研究和询价；本次玩家明确将所有游戏修改推迟到未来GM节点。
- Codex/开发规划基线独立调研和开发球队教练/攻防能力，GM不参与技术勘探；开发完成后给GM提供已验收可操作的项目即可。

## 赛季级命名与记忆规范（后续所有赛季遵守）

**一个游戏赛季一个派生 GM 决策聊天、一份赛季时间线。** 每个 Wxx 是该赛季的一个玩家触发决策节点，Rxx 是该节点内部的第几轮审议（最多三轮），**不是必须新开聊天**。节点完成后继续沿用本赛季 GM 聊天并等待玩家触发下次月度/季后赛/事件节点；玩家确认赛季结束并归档时，再为新赛季开新聊天和 `web_gm/seasons/<YYYY-YYYY>/INDEX.md`，保留前季总结而不把前季战绩当新季事实。因上下文容量续开聊天时，明确同赛季续接并回读本 INDEX。

建议文件结构：

```text
web_gm/seasons/
  2021-2022/
    INDEX.md
    windows/
      W01_GM_20261017/
        ROUND_R01_RECAP.md
        TEAM_BASELINE.json
      W02_GM_<real_date>/
        ROUND_R01_RECAP.md
        TEAM_BASELINE.json
        ROUND_R02_RECAP.md (如确实进入第二轮)
        ROUND_R03_RECAP.md (最多第三轮)
  2022-2023/
    INDEX.md
    windows/W01_GM_<real_date>/...
```

每次新文档顶部**必须同时标出**：
- 存档 `career_id`、`game_season`、`game_month`/精确 `game_date`（不知则 UNKNOWN）。
- `window_id`、`round_id`、`decision_id/version`、真实文档日期。
- `source_batch_id/data_updated_at`、是否月末封账、引用的已批准经营结论和执行回执。
- 本轮发生的事：**当时真实数据 → GM判断/两队议价 → 玩家批复 → 是否执行 → 真实赛场反馈 → 下轮待检**。
- 未执行和未观察的信息单独标记，不把旧提案变成已发生交易。

下一次同一赛季聊天的新节点，第一步是回读**本季上一个节点快照 + 新的最新快照**并确定两者是同一赛季、同一存档、相同统计口径。对 `total_wins/total_losses` 可进行确定性差分，计算两窗口之间战绩；场均技术数据的差异只是累计均值趋势，**不是直接得到某月技术统计**。若存档回档、赛季更替、日期未知或来源字段变动，必须标明且重新对齐基准。

## GM 与开发基线的分工

- **GM**只保留赛季决策链，获得已认证的实际功能后再做胜率优先的篮球决策；停止独立研究可写攻防字段或AI覆盖行为。
- **Codex**首先调研实际可修改范围和执行能力；玩家会把结果交给开发规划基线，完成开发和验收。
- **数据分析基线**在玩家触发后输出同批次可复用分析和跨快照变化，保证增量计算可信。
- **玩家**安排赛季节点并批准实际游戏修改，GM不使用未授权工具代替Codex执行。

该索引仅通过玩家明确触发的GM任务更新，不因新数据发布自动运行。