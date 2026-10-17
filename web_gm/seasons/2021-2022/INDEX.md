# 2021–2022 赛季 GM 长期时间线索引

- season_id: `2021-2022`
- career_id: `mc_haliburton_2021`
- season_gm_baseline: `2021-2022`（玩家计划每个新赛季开启新的GM决策基线）
- current_window: `GM-S2021-2022-W01`
- last_confirmed_exact_game_date: `UNKNOWN`
- current_progress_hint: `2021-11`（来自既有历史玩家进度，不是本批实测日期）
- index_created_real_date: `2026-10-17`
- policy: `PLAYER_RULES_20261017_V3` + `WEB_GM_DECISION_MECHANISM_V2`
- execution_state: `NO_GAME_WRITES_APPROVED_OR_EXECUTED_IN_W01`

## 本赛季 GM 决策窗口

| 顺序 | 游戏时间范围 | 窗口 / 回合 | 基准数据 | 经营记录与最终状态 |
| --- | --- | --- | --- | --- |
| 01 | 2021年11月附近，**精确日 UNKNOWN**；没有确认月终 | `GM-S2021-2022-W01 / R01` | `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2` | [本轮完整决策链](windows/W01_GM_20261017/ROUND_R01_RECAP.md) · 已批战略/研究/非约束询价，所有游戏修改暂缓 |
| 02 | **尚未到达/未收到新发布数据** | `W02 / R01`（候选，待玩家下一节点确认） | UNKNOWN | 尚无决策；不得提前写“12月”或预填结果 |

## 本赛季关键时点的权威事实与文件

1. [W01 30队冻结对比表](windows/W01_GM_20261017/TEAM_BASELINE.json)：球队赛季累计战绩、进攻/防守输出、薪资、士气相关观测、若干团队战术字段，不能当成11月独立统计。
2. [W01 R01 决策链](windows/W01_GM_20261017/ROUND_R01_RECAP.md)：包括游戏时间/现实生成时间区分、战略结论、审批、暂停执行和下轮承接条件。
3. [初次全联盟30队经营提案](../../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_PROPOSED.md)：历史原始 `PROPOSED` 版本，不覆盖旧文案。
4. [玩家审批回执](../../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_APPROVAL.md)：7项仅限战略、研究和非约束询价。对于是否已执行以独立执行回执为准。
5. [GM v2 机制](../../GM_DECISION_MECHANISM_V2.md)：外部双边谈判、胜率优先、士气次级、每次最多3回合。
6. [最新 GM_CURRENT](../../memory/GM_CURRENT.md)：只作快速入口，窗口历史以此处文件为准。

## 当前窗口里必须保留的判断

- 76人16–3、篮网14–5、湖人15–5、国王14–5；保护现有强势核心，不照搬现实历史赛季交易。
- 国王实役 Tyrese Haliburton vs Ty Hali 同名身份冲突；以正确球员身份进行所有审批和下一次分析。
- 勇士9–9、爵士5–13、活塞2–16：下次判断是否出现扭转，要对比新的同赛季数据。
- `MKT-01` 公牛/活塞格兰特、`MKT-02` 黄蜂/步行者特纳：只处于市场询价历史，**都没有正式双方GM一致的交易协议和执行批准**。
- 已批准 `GM-A01..GM-A07` 的范围是战略、研究和询价；本次玩家明确将所有游戏修改推迟到未来GM节点。
- Codex/开发规划基线独立调研和开发球队教练/攻防能力，GM不参与技术勘探；开发完成后给GM提供已验收可操作的项目即可。

## 赛季级命名与记忆规范（后续所有赛季遵守）

**一个游戏赛季一份 GM 基线、一条独立时间线。** 新赛季可从本季模板新建 `web_gm/seasons/<YYYY-YYYY>/INDEX.md` 与对应 GM 基线窗口，保留指向上一赛季结果，但不能把上一季战绩当新季事实。

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

下一次决策的第一步是回读**本季最后一个窗口快照 + 新的最新快照**并确定两者是同一赛季、同一存档、相同统计口径。对 `total_wins/total_losses` 可进行确定性差分，计算两窗口之间战绩；场均技术数据的差异只是累计均值趋势，**不是直接得到某月技术统计**。若存档回档、赛季更替、日期未知或来源字段变动，必须标明且重新对齐基准。

## GM 与开发基线的分工

- **GM**只保留赛季决策链，获得已认证的实际功能后再做胜率优先的篮球决策；停止独立研究可写攻防字段或AI覆盖行为。
- **Codex**首先调研实际可修改范围和执行能力；玩家会把结果交给开发规划基线，完成开发和验收。
- **数据分析基线**在玩家触发后输出同批次可复用分析和跨快照变化，保证增量计算可信。
- **玩家**安排赛季节点并批准实际游戏修改，GM不使用未授权工具代替Codex执行。

该索引仅通过玩家明确触发的GM任务更新，不因新数据发布自动运行。