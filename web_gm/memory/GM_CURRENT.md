# Web GPT · GM 基线当前记忆

DEV07 V2 开发状态补充：见[教练操作手册](../manuals/GM_COACHING_OPERATIONS.md)。新范围为 19 项球队默认设置、指定对手整体防守、30 队批准绑定批次及同会话来源；五项 Sim 禁止 GM 操作。PR #1已于2026-10-18合并main（2509b3b）并同步本地，首次生产采集/发布未运行；六默认 POE 沿用既有验证，整体防守新增 PHI→IND 14 条 UI 等价批量写入/显示/恢复证据，五数值设置、双体系与命名手册现也通过分项门槛，14项有实机写回证据，四Freelance依原生完整目录/有序codec提供受控接口，加上玩家明确开放的原生Tempo共19项；Tempo界面含义仍未知，参考同局教练实际值，不声称其为已验证的进攻节奏，BenchDepth不再设置9–10测试白名单，GM按阵容决定人数。未运行新的 GM 轮次、正式存档执行或数据发布，不改变以下已归档赛季决定。

- role: `WEB_GPT_GM`
- memory_version: 15
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
- approved_actions: W01 `GM-A01..GM-A07`（限战略/研究）；W02 `GM-W02-A01`、`GM-W02-R02-A01` 玩家批准且于2026-10-17报告已在游戏中成功落地
- current_game_change_decision: `W02_A01_GRANT_PLAYER_CONFIRMED_EXECUTED`; `W02_R02_A01_NWABA_PLAYER_CONFIRMED_EXECUTED`; `W02_A02_TURNER_NO_DEAL`；最新采集尚未同步，不能把历史批次当交易后状态
- game_write_approved: true (only W02 two specifically approved trades; not blanket writing permission)
- gm_game_write_executed: `PLAYER_REPORTED_COMPLETED_2026-10-17`（两笔；待下次新发布批次核对球员和选秀权，未在网页端执行）

## 2026-10-18 玩家确认：游戏AI会覆盖精细分钟分配；GM不再寻求精确个人分钟控制

- **用户实机观察**：游戏AI会频繁重置并重新分配各球员上场分钟，外部细化修改易被复写；未来也不强求解决。此为用户认可的**长期设计边界**，不是未完成研发任务。
- **GM应做**：使用已认证的`BenchDepth`（轮换人数上限）、`BenchUtilization`（替补使用倾向）与教练攻防体系间接影响球员实际获得的时间；根据后续赛季真实`minutes_per_game`、健康状态（如果来源可用）、比赛绩效和成长观察，提出球队整体轮换取舍、阵容搭配与打法建议。
- **GM不应做**：不向Codex交付任何`player_id/minutes_before/minutes_after`精确分钟调整、分钟锁定、周期补写或与AI重置对抗的任务；**不再将`PLAYER_MINUTES_EXECUTION_UNAVAILABLE`列为待实现功能**，不在后续GM工作中因无法精调分钟而卡住。即使当前教练设置间接影响分钟，也不能保证某球员具体上场数值。
- 与“训练全交游戏AI、GM不参与”和“教练会影响游戏自然成长”的玩家规则同时生效；普通能力/倾向等不允许外挂直接编辑。本节点未触发新的采集、比赛、经营决策或游戏写入。
- 对应最新版[教练手册](../manuals/GM_COACHING_OPERATIONS.md)、[GM SOP](../GM_DECISION_SOP.md)、[GM基线](../baselines/GM_BASELINE.md)和[GM说明](../GM_INSTRUCTIONS.md)已一并修订。后续窗口以这一段覆盖历史有关“精确分钟待接口确认”的旧记忆。

## 2026-10-18 最新玩家明确规则：训练退出GM范围，教练影响自然成长，内部调配优先于只寻求交易

**最新指令优先于过去有关训练研究的任何历史文字**。

1. **训练**：外挂尚未引入训练机制。游戏训练交由NBA2K22 AI完整负责；GM不管理、不研究、不提出训练策略、不要求补齐训练源、不让Codex开发训练接口，除非玩家未来明确重新启用。
2. **教练与成长**：玩家和其他人类玩家在大量终极联盟赛季实战中观察到，教练机制会直接影响比赛结果，也会影响球员在游戏引擎控制下的**自然属性/倾向成长走势**。此为项目GM采用的经验性运营前提，而非能推导任何教练raw值具体成长幅度的公式。GM应围绕体系适配和合理出场角色创造更好的赢球与发展环境。**不通过外挂直接编辑普通球员属性、潜力、倾向、徽章**；这些自然变化归游戏AI。
3. **GM四项并行经营杠杆**：阵容搭配与首发/替补角色、上场时间及轮换负荷、教练默认19项/指定对手整体防守18项、必须时的交易签约。不再默认“球队问题=找交易”，先看现有人能否通过更好的使用方式改善，同时比较交易资产成本。对30队逐队给具体调配/教练建议或有理由HOLD。
4. **上场时间实施边界（更新）**：游戏AI持续调整并覆写逐人分钟，用户明确放弃追求精确个人分钟；`BenchDepth`和`BenchUtilization`只间接影响实际轮换。球员赛季场均分钟用于观察分析，不设可执行的个人分钟指令，不列开发待办。
5. **风险与证据**：阵容与教练强度兼顾健康、体力、胜率和自然成长。没有本局伤病/疲劳数据不得假称某参数提升了X%的伤病概率。次世代MyNBA公开资料只是参考，不能代替PC/MC实测。教练自然成长的多赛季经验不等于获得训练管理权限。
6. **操作**：优先读[GM教练手册](../manuals/GM_COACHING_OPERATIONS.md)、[GM SOP](../GM_DECISION_SOP.md)、[GM初始化基线](../baselines/GM_BASELINE.md)和[GM职责](../GM_INSTRUCTIONS.md)的最新文本。具体教练值仍须在玩家下次正式采集后取得同批`coaching_tactics=VERIFIED_OBSERVED_SAME_BATCH`来源，通过程序生成动作和digest，玩家审批后由Codex执行。不能擅自新开GM回合、游戏采集或修改游戏。

此条是规则/认知升级，没有新的比赛、执行批次或训练操作。

## 2026-10-18 GM新经营机制正式加载（以main上的GM手册/执行规程为权威，非新GM决策）

本节基于玩家请求对main分支的正式机制再次核实。核对资料：
- [GM教练手册](../manuals/GM_COACHING_OPERATIONS.md)
- [教练执行手册](../../docs/40_COACHING_EXECUTION_RUNBOOK.md)
- [交易执行器](../../docs/37_APPROVED_TRADE_EXECUTOR.md)
- [签约执行](../../docs/38_APPROVED_SIGNING_EXECUTION.md)
- [能力状态表](../../docs/34_BASELINE_CURRENT_STATE.md)
- [休赛期P0研究](../../docs/development_reviews/DEV_20261017_04_OFFSEASON_FA_P0_RESEARCH.md)
- [休赛期P1源码](../../docs/development_reviews/DEV_20261017_04_OFFSEASON_FA_P1_IMPLEMENTATION.md)

**教练19项球队默认设置：** `COACH_DEFAULT`。六项POE：`POEOffense/POEOffense2/POEOffense3/POEDefense/POEDefense2/POEDefense3`；`PreferredSystem`、`ActiveSystem`（0–7原生体系）；`PlaybookID`（仅用最新同进程已命名字典）；`BenchDepth`、`RunPlayTendency`、`ZoneUsage`、`BenchUtilization`、`Tempo`、`HelpDefense`；`FreelanceType/2/3/4`（34个原生合法枚举、有序四槽）。四项已确认百分比字段0–100；BenchDepth是轮换人数不是百分比，9–10仅测试样本无固定上限；Tempo允许原生raw读写，但UI/引擎效果UNKNOWN，不能假称进攻节奏、百分比；不自行猜原生枚举值。

**对手防守18字段：** `VS_OPPONENT_DEFENSE` + owner team + opponent team + `defensive_setting_scope=OVERALL`，改变该owner面对该对手的**所有有效matchup记录**，不是单球员对位写入。字段：`PressureOnball`、`PressureOffball`、`ForceDirection`、`ScreenDefenseOnBall`、`ScreenDefenseHedge`、`OffballScreenDefense`、`PostDefense`、`DoubleTeamPerimeter`、`DoubleTeamPost`、`ScreenDefenseOnBall5`、`ScreenDefenseHedge5`、`SwitchRule`、`OnballHelp`、`ScreenHelp`、`ExtendPressure`、`TagOnRoll`、`StayAttached`、`PreRotate`；每字段必须按最新source里的合法原生字典，部分原生名作用尚未知。禁止GM写五项SimPace/SimPress/SimHelpDef/SimOffReb/SimDefReb；旧TEAM poe_*不可当作教练值；无单独球员对位/轮换分钟写入能力。

**首次生产来源门槛：** 玩家下一次主动触发正式采集上传；读取最新 `published/index.json → saves/<career>/latest.json`，本批 `source_coverage.json` 必须 `coaching_tactics=VERIFIED_OBSERVED_SAME_BATCH`，存在 `coaching/teams.json`（30队）与 `coaching/field_dictionary.json`；对手按需读`coaching/opponents/<owner>.json`，不要默认全读870组合。2026-10-18本次检查的latest仍指向旧批次 `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`，**尚无可信正式教练新来源**。教练代码已main合并，隔离局技术验收与正式来源成功发布不可混淆。

**教练提案→执行：** GM逐队以球队真实阵容决定HOLD/PROPOSED、`COACH_DEFAULT`或`VS_OPPONENT_DEFENSE`、目标合法raw值、篮球理由；只能用程序从可信批次生成`gm_intent → requests → coaching_batch → gm_proposal`，模型不猜coach IDs、before_raw/共享块、整体组身份。玩家审核`career_id/batch_id/decision_id/version/全部action_ids/batch_digest`，批准后Codex才执行`scripts/coaching_batch.py`的离线校验、RO preflight、受控execute及回执；必须玩家确认先退出教练编辑页`--coach-editor-closed`。回执`COMMITTED_VERIFIED_IN_MEMORY`不等于玩家游戏保存或新批次上传。无批准不写，互不并行，异常按原执行手册处理。保持“不为验证胜率自动推进比赛”的规则。

**交易能力：** 受控`ownership_transfer_v2`脚本`scripts/execute_approved_trades.py`或`scripts/run_approved_trades.ps1`，常用姓名/from_team/to_team，可选face/DOB；简单三届选秀权身份；plan→player-approved execute→verify；15人常规名单上限、计数与引用一致、防重放。有限支持普通球队不重叠批次；不把此成功推广成复杂多笔同队依赖、签约或裁员能力。先前两笔交易玩家确认已落地，切忌重复执行。

**签约：** GM负责球员/目标球队/逐年整数美元合同/选项/择队/审批，Codex不重复议价。`approved_signing_v1_unvalidated`和`scripts/execute_approved_signing.py`仅源码准备，`SIGNING_LAYOUT_VALIDATED=False`/`SIGNING_EXECUTION_ENABLED=False`，真实写回未运行/未验收；等有正式签约且玩家明确批准才做实机布局核验、打开控制写入，不能现在当作可用完成态。

**休赛期竞价：** `src/gm_core/offseason.py`、`scripts/offseason_plan.py`、`scripts/offseason_validate.py` 已有30队集中竞价、同队最终匹配、UFA/RFA、工资/名额顺序占用的合成来源离线规划源码，但P0真实休赛期采集、到期判定/原生AI签约冻结、下一季资金资格、持久性及签约执行未验收。规划器v1_1只准`SYNTHETIC_OFFSEASON_V1`，真实输入会阻断，不得声称已“彻底堵死”原生球员流动。待玩家触发休赛期测试/采集，另行验证原生AI不覆盖外部决策与跨赛季保存。该系统是外部竞价与合同方案来源，不自动执行游戏写入。

**经营方向：** 每月30队独立经营，除交易/人员外新增球队体系与对手防守的战术选择，提高争胜能力，同时依据玩家历史重力专项规则平衡现实/历史线。普通球员属性/潜力/徽章、人物成长仍由游戏决定，任何历史重力例外需玩家逐项批准。此次仅加载文档与GM能力，无新比赛、无任何游戏写入、无新30队决策节点；仍沿用同赛季一个GM聊天、玩家先发布新源再触发GM的流程。

## 2026-10-17 玩家新指令：两个交易均已批准、攻防开发恢复

- `GM-W02-A01`: 公牛得到 Jerami Grant；活塞得到 Coby White、Derrick Jones Jr. 和 CHI 持有的 2022 POR 首轮（`draft_pick:2022:1:28`）。玩家明确批准；`APPROVED_BLOCKED_EXECUTOR`，尚无游戏写入或存盘/数据库回执。
- `GM-W02-R02-A01`: 独行侠得到 David Nwaba；火箭得到 Sterling Brown、DAL 原始 2022 次轮（`draft_pick:2022:2:17`）和 DAL 原始 2024 次轮（`draft_pick:2024:2:17`）。玩家在同一聊天明确批准；`APPROVED_BLOCKED_EXECUTOR`，尚未执行。
- 后续使用 `docs/36_EXECUTION_BASELINE_PROMPT.md`、`docs/28_EXECUTION_WINDOW_RUNBOOK.md` 与 `docs/34_BASELINE_CURRENT_STATE.md` 第8节，由玩家交 Codex 处理，执行端先只读核验；正式交易业务写回及选秀权转让执行器在本次审查的能力表中仍未完整验收。不要把批准误当成交。
- **攻防系统开发已恢复**：以玩家最新口头指令为准，允许 Codex/开发规划基线继续开发球队自身攻防、针对特定对手的攻防设置。GM 仅在玩家提供并经验证的接口能力后使用，不自行设具体枚举、不默认AI不会覆盖。
- **MC 哈利伯顿申请交易**：玩家确认该剧情即将导致转队，尚未发生；Sacramento 下一轮准备应对核心离队，不能把未来剧情当作已执行变更。
- 本次只针对当前赛季同批次W02的后续审批和技术交接，不新增已发生的比赛场次。后续每次真实游戏月份应依据最新同口径数据，30队都做明确经营裁决（HOLD亦需理由），而不仅列出观察问题。

## 2026-10-17 新进展：玩家确认两笔交易已在游戏落地（最新状态，优先于历史节点描述）

- **执行反馈（玩家权威陈述）**：`GM-W02-A01` 公牛/活塞 Jerami Grant 交易与 `GM-W02-R02-A01` 独行侠/火箭 David Nwaba 交易，均已成功完成游戏修改。此处登记 `PLAYER_REPORTED_EXECUTED`，不再标记“待执行”，不要求重复执行或再次批准。旧W02提案内 `PROPOSED` 属原审议时历史状态。
- **尚待下次数据发布复核**：`published/saves/mc_haliburton_2021/latest.json` 在本次检查仍指向交易前批次 `2021-2022_M01_SIMPLE_PICKS_V1_88101a36a3e3_fbde28d7_TS2`，不能拿旧球员归属质疑玩家已完成的执行。等玩家**主动触发** Codex 数据源更新、GitHub 新批次上传后再核对双方新阵容、合同归属和三枚选秀权。游戏执行已完成与数据同步待更新分别记载。
- **新功能进度（玩家报告）**：Codex已完善自动化交易、自由球员签约、模拟休赛期签约球员的脚本机制。前述 `docs/34_BASELINE_CURRENT_STATE.md` 第8节为旧版能力索引，不可继续简单断言“交易执行器仍没有”；但具体CLI、批准入口、适用范围、成功回读、签约资金/土豪线规则仍需下次获取最新文档/验收说明，不能自行臆造调用方式。
- **玩家固定同步节奏**：下一次 GM 月度或阶段经营前，玩家先主动触发数据源更新与发布；Web GM每次开始决策先读 `published/index.json`、职业存档 `latest.json` 和新批次，重新对齐W01/W02历史数据，不自动采集、不自动推定交易后的战绩。随后30队逐队独立经营并提出新提案。
- **攻防功能**：沿用玩家最新指令继续开发，尚需玩家届时提供具体已验收接口；正常比赛AI按游戏本体运行。不额外修改球员能力。MC哈利伯顿剧情转队仍须通过未来游戏结果验证。

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
