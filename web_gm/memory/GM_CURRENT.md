# Web GPT · GM 基线当前记忆

- role: `WEB_GPT_GM`
- memory_version: 7
- gm_chat_scope: `ONE_CHAT_PER_GAME_SEASON_V1`（本赛季持续使用一个 GM 决策聊天；月度 Wxx 为节点归档，不要求另开聊天）
- updated_real_world: `2026-10-17`
- current_game_season: `2021-2022`
- current_career: `mc_haliburton_2021`
- current_window: `GM-S2021-2022-W02` / `R01`（最新已归档的同批次专题续议；同一赛季聊天继续待命）
- last_game_month_hint: `2021-11`（原项目进度参考，**本批精确game_date UNKNOWN**）
- last_game_date_exact: UNKNOWN
- month_closed: false
- last_snapshot_batch: `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`
- last_snapshot_data_updated_at: `2026-10-17T11:50:28.464724+00:00`
- last_gm_decision_id: `GM-20261017-W02-R01 v1`（新方案PROPOSED，非玩家批准）
- approved_actions: W01 `GM-A01..GM-A07`（仅战略/研究/非约束询价）；W02暂无批准动作
- current_game_change_decision: `W02_A01_GRANT_TRADE_PROPOSED_NOT_PLAYER_APPROVED`; `W02_A02_TURNER_TRADE_NO_DEAL`；全部游戏写入仍禁止自动执行
- game_write_approved: false
- gm_game_write_executed: false

## 必读入口：按赛季、游戏窗口和回合形成的决策链

1. [2021–2022 赛季GM时间线总索引](../seasons/2021-2022/INDEX.md)
2. [W02/R01最新归档：同批市场议价/战术续议（没有新比赛）](../seasons/2021-2022/windows/W02_GM_20261017/ROUND_R01_RECAP.md)；[W01历史归档](../seasons/2021-2022/windows/W01_GM_20261017/ROUND_R01_RECAP.md)
3. [W02 30队同批对比基线](../seasons/2021-2022/windows/W02_GM_20261017/TEAM_BASELINE.json)（完全复用W01观测）；[W01基线](../seasons/2021-2022/windows/W01_GM_20261017/TEAM_BASELINE.json)
4. [W02新待批准交易及战术方案](../decisions/mc_haliburton_2021/20261017_W02_SAME_SNAPSHOT_GM_PROPOSED.md)；[W01原30队经营初案](../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_PROPOSED.md)
5. [7项玩家批准回执](../decisions/mc_haliburton_2021/20261017_M01_LEAGUE_GM_ROUND01_APPROVAL.md)
6. [GM决策机制v2](../GM_DECISION_MECHANISM_V2.md)及[GM SOP v2](../GM_DECISION_SOP.md)

## W02 最新节点发生了什么（2026-10-17，游戏日期 UNKNOWN）

- **批次没有变化**：`published/latest.json`仍是W01的完整相同批次，W02为玩家再次启动的赛季内专题经营节点，不是下一自然月，不能计算新月战绩或视作游戏已经推进。
- **交易议价**：外挂CHI/DET两队GM对 `GM-W02-A01`（Coby White + Derrick Jones Jr. + CHI持有2022 POR首轮换Jerami Grant）模拟达成具体经营共识；状态 `PROPOSED_NOT_PLAYER_APPROVED`，执行器未验收且游戏未写。CHA/IND特纳旧报价判定 `NO_DEAL`，不冻结其资产。
- **战术方向**：GSW防守优先、UTA米切尔两场原因未知继续等证据、DAL改善防守；保护SAC Tyrese Haliburton，所有战术均未改游戏。
- **授权边界**：仅W01七项战略/研究/非约束询价已获有限批准，W02任何新交易尚无批准。W02节点已归档，同赛季GM聊天待命。

## W01 历史节点发生了什么

- **实测基线**：PHI 16–3、BKN 14–5、LAL 15–5、SAC 14–5、GSW 9–9、UTA 5–13、DET 2–16；全部30队战绩/球队指标保存在窗口JSON；当前数据是赛季截至快照累计，不是本月独立数据。
- **经营决定**：已对30队进行12模块战略审查；玩家批准GM-A01..GM-A07的方向/研究；保护玩家国王 Tyrese Haliburton (slot=1235)，不同于 Ty Hali (slot=184)。普通能力修改持续禁止。
- **未执行市场讨论**：MKT-01 CHI/DET 格兰特；MKT-02 CHA/IND 特纳；**双方GM尚无正式一致协议**、玩家没有批准交易、游戏名单/选秀权未因此变化。
- **机制修正**：外挂双方GM协商决定交易，而非游戏CPU；赢球优先，士气/化学反应次级；每个游戏节点最多3个GM回合，通常一次定案。
- **最新停写指令**：Codex因额度暂不可执行，玩家决定本窗口**任何经营修改都不落地**，不自行转交Antigravity，等待下一月GM决策节点。旧提案没有执行权，也不能自动递延为新月应执行的动作。
- **分工最新限制**：教练攻防系统可写范围、AI是否覆盖等由Codex先调研；**玩家将结果直接交开发规划基线处理**，GM无需参与开发调研/规划，只接收未来已验收的可用操作能力。此前[GM拟写的攻防开发需求](../seasons/2021-2022/DEV_REQUEST_COACHING_OPPONENT_GAMEPLANS.md)已标记历史草稿，不视作活动交接。

## 下一次玩家在本赛季聊天启动 GM 节点时，必须这样恢复

1. **同一游戏赛季沿用同一 GM 决策聊天**；从本季[时间线INDEX](../seasons/2021-2022/INDEX.md)找到最新决策节点 W02、先前W01和对应30队冻结对比表；检查最新`published/index.json`和`latest.json`，锁定本节点 `save_id/season/batch/data_updated_at/game_date`。W01、W02只是档案中的节点编号，不强制每月新开聊天；本次W02与W01完全同批次，下一次需要新的比赛数据须单独触发采集。
2. 分析基线读取新数据后，GM对照30队前后累计战绩：同存档同赛季同口径才用`ΔW/ΔL`计算新期间战绩；不从两个赛季平均值直接相减声称月度场均贡献。排查读档回退、赛季切换、球员去留变化及已执行回执。
3. 回看本轮保护核心战略是否经得住新的胜率、净胜分、球员样本、阵容变化；W02已有CHI/DET新拟成交方案，但仍为 `PROPOSED`，玩家若不批准就不能交执行；如新的实时数据已改变需先重新估价。CHA/IND本轮 `NO_DEAL`，未来若重谈必须用新证据。
4. 用本赛季下一节点时的**实际可用执行能力**决定战术/轮换提案，不研究技术本身，不推断数据缺口。士气/化学反应是赢球次级风险。
5. 用户每个游戏月或季后赛轮次独立触发**同一赛季聊天中的 GM 节点**；每个新节点仍建立 `web_gm/seasons/2021-2022/windows/Wxx_.../ROUND_Ryy_RECAP.md` + 新的30队基线（Wxx 是节点档案目录），更新本季 INDEX 和本 CURRENT，保留审批链。节点交付后在本聊天待命，不强制结束聊天。**只有玩家确认赛季完结并归档后，新赛季才开新的 GM 决策聊天与赛季目录。**

## 永久禁区和来源边界

一般球员能力、潜力、徽章、倾向、动作、性格不能靠外挂经营修改；历史重力须专项批准，MC成长仍关闭。1984–2020历史选秀循环的完成进度需要玩家确认。数据来源`NULL`不等于0，伤病/实际计划轮换/个体士气/交易请求未知则保持UNKNOWN；完整交易业务执行器尚需开发/验收。历史决策不是游戏实际发生的事实。
