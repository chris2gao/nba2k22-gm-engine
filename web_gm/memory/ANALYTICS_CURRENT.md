# Web GPT · 数据整理分析基线当前记忆

- role: WEB_GPT_ANALYTICS
- memory_version: 1
- last_reviewed: 2026-10-17
- state: INITIALIZED_FROM_VERIFIED_PREVIOUS_OUTPUT
- last_source_batch_id: `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`（**历史引用，新任务必须查最新 latest.json**）
- last_known_game_date: UNKNOWN

## 已有可复用工作成果

- [30 队量化分析报告](../../docs/gm_analysis/2021-2022_SIMPLE_PICKS_V1_ANALYSIS_ONLY.md)
- [结构化结果](../../docs/gm_analysis/2021-2022_SIMPLE_PICKS_V1_ANALYSIS_ONLY.json)
- 分析报告已经记录 30 队胜负、场均得分差、工资总额、三届内选秀权及阈值候选生命周期。上一轮为 `ANALYSIS_ONLY`，无正式 GM 回合和游戏执行。
- 已验证的工作方式：GitHub 连接获取**精简事实输入**，本地 Python/等价仓库计算规则求值，通过 GitHub 连接写回文件。此前**没有**完整 `git clone` 或原样运行 `gm_prepare.py`；不能混称。
- 源数据已有 30 队赛季战绩、55 项能力/潜力、部分球员赛季统计、员工归属、工资和未来简单选秀权。OVR、游戏界面年龄及完整伤病/轮换依然缺失。

## 待做（不是自动任务）

1. 新任务先读 `published/saves/<career_id>/latest.json` 和当前规则，再决定是否沿用旧分析。旧报告不能覆盖新批次。
2. 在可用条件下，尝试把仓库实际源码/发布 JSON 放到 Python 运行环境并执行现有 GM 模块；如果连接权限/命令行网络不允许，记录使用文件方式及是否原样运行。
3. 由玩家触发分析后，按 `ANALYTICS_BASELINE.md` 产出新的 Markdown/JSON，保存 sessions 总结并更新本索引。
4. 需要 GM 做主观经营取舍时，交接给 GM 基线（不自动启动）。

## 责任与禁区

分析结果归 `docs/gm_analysis/`；只修改分析与本岗位记忆。不得编辑 `published/` 游戏事实、Release ZIP、正式球队档案、交易执行文件。当前无自动发布/后台任务。
