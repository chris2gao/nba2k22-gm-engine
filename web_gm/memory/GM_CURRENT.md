# Web GPT · GM 基线当前记忆

- role: WEB_GPT_GM
- memory_version: 2
- last_reviewed: 2026-10-17
- state: FIRST_FORMAL_GM_ROUND_PROPOSED_PENDING_PLAYER_APPROVAL
- career_hint: `mc_haliburton_2021`（下轮需重验）
- source_batch_id: `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`
- data_updated_at: `2026-10-17T11:50:28.464724+00:00`
- game_date: UNKNOWN
- month_closed: false
- last_decision_id: GM-20261017-M01-R01
- player_approved_actions: NONE_RECORDED
- executed_game_changes: NONE_RECORDED

## 当前有效的经营判断（待玩家批准）

- [30队×12模块完整决策草案](../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_PROPOSED.md)
- [本轮会话总结](gm/sessions/20261017_M01_LEAGUE_GM_ROUND01.md)
- [同批数据分析](../../docs/gm_analysis/2021-2022_SIMPLE_PICKS_V1_ANALYSIS_ONLY.md)
- GM-A01..GM-A07 仅待审批战略、数据核验、战术可行性与世界线约束；MKT-01 CHI/DET与MKT-02 CHA/IND均为询价，CBA和执行能力未验收。
- PHI/BKN/LAL/SAC为本轮争冠观察四强。保护国王玩家球员 Tyrese Haliburton（pool_slot=1235），不可与 Ty Hali（pool_slot=184）混淆。
- UTA米切尔仅2场、Oni仅1场，不能强制推断伤病/轮换。球队现金异常、完整人员/轮换/伤病、OVR为本轮信息缺口。

## 下次正式 GM 工作流

1. 读取 `published/index.json` 和当前 `latest.json`，确认本轮批次是否已过期；若新批次已发布不能照搬旧事实。
2. 读取玩家对GM-A01..GM-A07及两项市场询价的明确批准或反对；未记录批准默认为 PROPOSED。
3. 如需新资产/交易计算，向数据分析基线发送 calculation_request，数字由确定性Python/SQL核验；技术缺口由开发基线交给Codex。
4. 游戏执行只由玩家明确授权后交给Codex执行基线，不能自动修改属性、名单、合同、POE和选秀权。
5. 完成本轮后仍保存非事实决策报告、sessions，再更新本索引；不覆盖 `published/`、不编辑正式球队档案。

## 固定限制

现代比赛实际结果优先；普通球员能力编辑禁止；历史重力具体方案需专项批准；MC成长关闭。1984–2020历史选秀循环的已完成次数需玩家明确确认；本批next_draft_year=2022，仅未来三届2022–2024简单选秀权可在方案中提出。
