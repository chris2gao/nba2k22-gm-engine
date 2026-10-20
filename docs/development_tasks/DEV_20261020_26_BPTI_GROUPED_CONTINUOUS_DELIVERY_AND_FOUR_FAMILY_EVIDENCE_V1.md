# DEV26 — BPTI B2–B6 分组连续开发与四体系补证执行计划 V1

日期：2026-10-20 | 编制：Web 开发规划 | 状态：**SCHEDULING_PROPOSAL / PLAYER_TO_AUTHORIZE**。本文件仅改变推荐调度，不自动合并PR、授权游戏内存读写、正式运营GM V4或启动Codex。玩家转发相应工作包提示词后，该工作包的具体范围和明确最小检查视为授权；授权后工作包内不需要每个B阶段再逐一征求批准。仍遵守`PLAYER_DEVELOPMENT_POLICY_V2`：工作包以外扩展设计/追加检查必须先询问玩家。

## 0. 当前GitHub事实与此前方案冲突的解决

- B0 PR #8 玩家批准后已合并到main（`e4b397e`）；B1 [PR #9](https://github.com/chris2gao/nba2k22-gm-engine/pull/9) 完成10/10 SystemCard、10/10研究可读、截至2021-10-19普通GM可读6/10；本规划时PR #9仍OPEN/Draft、未合并（head `65efdafb43636812eebeb8e88e6e1660763d7f97`），Web审核建议合并。不要把本文件误解为PR #9已经合并。
- [DEV23](DEV_20261020_23_BPTI_CORE_PLAYBOOK_SEMANTICS_CODEX_DISCOVERY_V1.md) 是待玩家触发的只读核心Playbook/角色语义调查，可能需要玩家打开当前存档页面；它是**人工交互边界**，不适合偷偷混进长时间无人参与的B2–B6代码批次。
- [DEV22](DEV_20261020_22_BPTI_RESEARCH_TO_CODEX_PHASED_HANDOFF_V1.md) 之前建议B0→B1→DEV23→B2→B3→B4→B5→B6每段单独审批。本DEV26在用户选择**分组连续交付模式**后取代其“每个小阶段都必须中途停止”的**调度要求**；DEV22的知识/授权/代码质量边界仍有效。默认代码执行需玩家主动发给Codex一次工作包指令。
- [DEV24](DEV_20261020_24_BPTI_ANTIGRAVITY_GAME_DATA_SOURCE_REQUIREMENTS_V1.md) Antigravity逐场/高级统计扩展由玩家决定**在B0–B6全部完成后进行**。这不取消正式开档另需可靠真实采集的独立条件；B4/B6不可伪造逐场赛果或真实30队已评估。

## 1. 推荐三工作包、两次工程验收门

| 包 | 内容 | 流程 | 人工门 |
|---|---|---|---|
| A / DEV23 | 现有原生目录+玩家页面只读Playbook语义/类型/角色调查 | **单独任务**；有页面时调查，无页面交静态证据及明确待玩家操作表 | **游戏UI可能需要用户动作**；玩家审核并确认研究是否足够支持B2 |
| B / CORE DATA | **B2 → B3 → R1-Four-Family Evidence Patch** | **一次授权、同一Codex工作包连续三个内部里程碑**；分别小提交，末尾一个Draft PR | **B3/补证后工程审核并由玩家合并**，再进入GM经营核心 |
| C / DECISION | **B4 → B5 → B6** | **一次授权、一个工作包连续三个内部里程碑**；先完成B4接入、再B5历史演化、最后B6精简集成验收，末尾一个Draft PR | 最终玩家审核与合并；**不直接启用V4/新档** |

理由：B2映射、B3球队seed和四家族来源补充都是**知识与事实解释层**，可以一批完成；B4接M3并形成真实GM选择属于**决策层契约变更**，应先在B3后交接检查一次。B5依赖B4的角色/决策历史，B6依赖B4+B5全部能力，这三段适合在同一包内连续完成。一次把B2–B6全部交付只有一个巨大Draft PR会放大上下文与调试成本；一次每个小阶段再停又浪费人工和Codex的加载成本。

**PR策略**：每个工作包一个独立GitHub分支/一个Draft PR，内部每个B里程碑使用清晰提交和验收小节，不要求中途合并或逐阶段PR。**不允许Codex自动把任何Draft PR合入main**；B包在PR9、DEV23相关权威研究交接经玩家接受后从最新main起步；C包在玩家批准B包PR合并后从最新main起步。DEV23若仅研究文档即可交接，需确保其正式文档已可由C/B真实读取，不能依据未同步的本地草稿编造完成。

## 2. 包A：DEV23持续独立，不建立额外前置条件

读取DEV23已定义的静态目录/68槽/PlayTypes/角色/本队同名书，必要时只读游戏UI/进程并向玩家索取菜单步骤；目标是**核心**Warriors Motion、Bulls Iso/Mid、Heat Hub与有限Spread PnR/Post/Elbow映射的高价值语义，分清`UI_OR_STATIC_LABEL_VERIFIED`、`RUNTIME_ASSIGNEE_OBSERVED`、`IN_GAME_EXECUTION_OBSERVED`。本任务不授权第三层比赛运行，不遍历全部CRC，不做B2正式代码。若不可调查部分保持UNKNOWN，B2应输出部分支持/HOLD而不是为了证明完整性卡住全部后续开发。

## 3. 包B：B2、B3和四家族补证连续执行

### B2 NativeBinding：R3+DEV23→B0 DTO

复用M3/DEV14：八Coach系统、19默认字段的可写边界（常规18）、Freelance1–4、本队已加载68槽/同批真实CRC、4 PlayTypes+Initiator、具名48 Tendencies、18 PERSONAL_DEFENSE、训练及软轮换；系统家族与原生Enum绝不强制一对一。仅生成只读`NativeBinding`及简短匹配报告、`SUPPORTED_FIELD_DIRECTION/TYPE_MATCHED_ONLY/UNKNOWN_NATIVE_BEHAVIOR/UNSUPPORTED_ACTION`；行为效果未知保持HYPOTHESIS。实时内存/游戏/DEV14执行器禁止引入gm_core。51未知倾向、Tempo解释、受益球员若未获DEV23证据必须HOLD。

### B3 TeamIdentity：R2 30/30历史seed与本局对象分离

按2021-10-19真实历史可知界限，区分组织文化、教练本人哲学、当期战术和人员优势。产出30/30 TeamIdentity可检索历史`HISTORICAL_SEED_ONLY`，保留未证据支持的UNKNOWN、LAL-S2/POR-S2缺URL/ATL-S2部分支持的现有B0条件；不凭当期名单或城市名字捏造文化。留已有M3同批Team/Coach/Roster绑定钩子，但在未收到新档合法源前`NOT_BOUND_TO_ANY_SAVE`、真实30队仍UNASSESSED。

### B1-EVIDENCE-4：在B4之前给四个RESEARCH_ONLY家族做**最小、真实、在2021前已知的知识补充**

正式GM目前10家族中6张可读；四张`ISOLATION_MIDRANGE_CREATION`、`POST_HIGH_LOW`、`TRANSITION_EARLY_OFFENSE`、`DEFENSE_FIRST_RIM_PROTECTION`暂`NOT_READY`。四者是正常篮球常见打法，B4若只能在六家族中选择会形成结构性偏置。

Codex限范围完成：
1. 将下面**已初步查实**的2021前NBA官方历史报道作为**候选来源**，对照原文与2021日期确定适用的机制句子、来源标题/发表时间、具体事件时间、证据界限和反证；无需重新启动长篇Deep Research或修改R1原始报告。
2. 每体系只补一条**保守的篮球原理细粒度Claim**（如需第二来源才能支持具体重要主张，可保留较窄范围、不扩大调查），遵守B0的`SUPPORTED_INTERPRETATION`与`source_id/parent_claim_id/fact_valid_from/fact_valid_to/knowledge_available_from`，有确切原始URL、时间和事实才入库；不要把NBA官方单队案例当作全联盟战术有效性定律。
3. 按既有B0/B1校验将卡片关联改为截止日前可阅读的机制Claim；保留牌面七段篮球意图，但不能让未证实/未来句子顺着单一许可引用泄漏到普通GM。
4. **目标是10/10普通GM具备至少一个2021前定性机制入口，非必须逐命题VERIFIED或游戏行为验证。** 若真实来源不能支持完整卡片叙述，只将可支撑的子命题做安全可读参考，其它仍NOT_READY/UNKNOWN；**不可人为改变日期、绕过索引或直接解除HOLD以凑10/10**。研发如未完成，明确`GM_ELIGIBLE_COVERAGE`的真实值与B4可用子集，继续在安全子集内实施，不阻断整项BPTI计划。

**初步核实的四条2021-10-19前来源（均为NBA官方，核实仅供候选，不算项目Claim认证）：**

| 家族 | 官方文章 | 发表时间 | 可支持的最小机制 |
|---|---|---|---|
| 单打/中距离 | `https://www.nba.com/news/film-study-kawhi-crowd` | 2019-06-04 | Leonard面对提前包夹/高压时，创作者要及早读协防，个人创造与二次传球互补 |
| 低位/高低位 | `https://www.nba.com/news/sixers-crown-jewel-shines-game-4` | 2019季后赛 | Embiid低位遭绕前，用罚球线高位接应建立高低位入口；包夹后及时找外线/切入 |
| 转换/早期 | `https://www.nba.com/news/film-study-lakers-transition-lebron-james-anthony-davis` | 2020-05-13 | 2019–20 Lakers篮板/提前传球制造早期优势，防守落位前的决策时间决定机会 |
| 护框优先 | `https://www.nba.com/news/film-study-sixers-joel-embiid-rim-protections` | 2020-07-08 | 护框分威慑出手与干扰出手，Drop会影响挡拆持球者的射程和选择 |

**单一文章有可能支持一个狭窄原理而非一张完整七段卡的所有句子；发布前逐条核对，杜绝全卡借一条来源“认证”。** 不把以后赛季DeRozan/Gobert的数据回填2021认知。

### 包B最小检查（若用户转发任务词则仅授权以下4项）

- B-B1：核心Binding中，已确认原生字段与尚未知CRC/受益人严格分级；个人18项防守、本队书、OVERALL只读、51未知不写；不能生成任何真实Desired/批准。
- B-B2：30张历史TeamIdentity唯一、来源可回查、2021截止/UNKNOWN和未绑定存档身份正确。
- B-B3：四类补充Claim候选逐条对照2021前年份与官方文章；GM可见/阻断覆盖结果如实记录，不能漏出未来赛果；不得为了达10/10绕过校验。
- B-B4：B2+B3共同查询是有界只读、返回状态和证据，研究包不会改变M3/DEV14执行权限或初始化正式30队运营状态。

不跑旧B0/B1/M3/DEV14全量测试；授权检查未通过只修直接失败项并定向复验。任何额外扩展或验证征询玩家。

## 4. 包C：B4、B5、B6连续执行

### B4：实际连接M3决策

在现有D1–D6、M1交易/资金、M3教练/类型/个人防守、DEV14审批环节**引用而不是重做**B1/B2/B3知识；输出`why_this_basketball`、`primary_secondary_system`、`first_advantage`、`opponent_counter`、`second_answer`、`roles_agency`、`native_support_and_unknowns`和三个经营备选HOLD/INTERNAL/MARKET。球队哲学必须影响解释与内部调整/人才缺口比较，不仅生成一个装饰性的历史段落；普通GM只能消费可用历史Claim和**同批经过脱敏的实际球员教练资料**，其余Research-only家庭不得漏进运营上下文。没有逐场Box Score时不虚构趋势/胜率效果；当前轮换分钟AI可覆盖，不强控精确分钟。

### B5：真实本局跨赛季演化状态

记录先前体系与文化、已观察变化和决定、六级转型建议`ROLE_TWEAK / SECONDARY_BRANCH / CO_PRIMARY_SYSTEM / TACTICAL_REBASE / COACH_ALIGNMENT_CHANGE / ORGANIZATIONAL_REIDENTIFICATION`；建队身份慢变量与教练/战术快变量分离；历史新秀名号不得决定未来职业能力，实际技能只由本局合法动态来源触发。存现有gm_workbench衍生历史/版本或等价已有点位，**不新增第二个GM经营数据库或教练签约市场**；所有建议仍须玩家审核，不自动换帅/交易或写内存。

### B6：最小集成验收与工程报告

验收**设计和离线安全推理**，不假称真实新档30队已经营、3D/Calendar效果验证、赛季统计校准完成或GM V4已启用。建议以现有合成安全DTO为输入，不跑实际比赛/采集。

### 包C最小检查（若用户转发任务词则仅授权以下5项）

- C-C1：GSW Motion、CHI Creator/Midrange、MIA Defense-first三个实例给出**篮球原因与不同角色结构**，允许来源/Native不支持时HOLD，不能把三个队变同一种效率优化。
- C-C2：B4真实走M3的HOLD/INTERNAL/MARKET比较及角色/教练/市场机会成本，不创建重复审批器/市场。
- C-C3：历史巨星**异队**及教练变化的合成案例仅基于当期可见技能/组织惯性触发六级演化中的合理步骤，不能因姓名自动获得职业巅峰能力，也不随月度成绩瞬间重写球队文化。
- C-C4：数据源不可用/GM_SANITIZED身份不符、UNKNOWN Native或B1不可用卡正确HOLD；对真实比赛效果和缺失逐场数据不杜撰。
- C-C5：对接DEV14仍仅输出**未获批准意图**，不会自动修改Ability/Potential/Badge/OVERALL、51未知倾向、其它队书，或绕开CAS/玩家审批。GM_V4_NOT_ENABLED，30队实际经营仍UNASSESSED。

只运行本包这些直接相关检查，失败定向修正；不重跑旧完整集合，也不自行添加未知风险防御套件。

## 5. Codex连续执行规则和失败边界

- 玩家一次授权**某个工作包**，包内按列出顺序自动推进，不为B2/B3、B4/B5/B6每小阶段再次询问；如发生需求外新设计、扩大验证、真实游戏操作、PR合并、生产数据发布或教练市场操作，按政策V2停在该点请求许可，继续其它已授权工作。
- 每个内部阶段结束做**带版本号的本地提交+简明阶段记录**。遇到会话超时/上下文不足时，可在下一次用户触发后从最新阶段提交恢复，不重新从零开始；不能承诺后台持续工作。
- 内部阶段可以在同一个PR内多次push，**只有包完成且限范围检查完成，才宣告该包完成**。如发现未知原生机制，记录`UNKNOWN`和低保真替代，不能因为某CRC缺失而无限逆向；涉及核心行为缺口阻断的某项方案，明确`HOLD`，其他可开展阶段继续。
- 模型建议：包A DEV23：**Astra High**；包B B2→B3→四补证：**Astra High**（如可在内部步骤切模型B3/文献补充可用Sol High）；包C B4→B5→B6：**Astra High**优先业务+权限交叉，若上下文/额度不支持可用最强Sol High。实际型号以用户Codex选择器可用为准，思考级High，不因高模型自行增加测试。
- 禁止直接写游戏数据、修改球员原始能力/潜力、自动修Issue #6、自动启用V4/新档、做DEV24采集或3D/日历校准、自动合并任何PR。

## 6. 两条可直接发给Codex的授权任务入口

**包B（DEV23成果审核并同步 + PR9已合并后）**：

> 从最新main开始BPTI分组连续交付**工作包B：B2→B3→四类SystemCard 2021前年份补证**。权威任务`docs/development_tasks/DEV_20261020_26_BPTI_GROUPED_CONTINUOUS_DELIVERY_AND_FOUR_FAMILY_EVIDENCE_V1.md`第3、5节；另阅读DEV22、R4、B0/B1合同、DEV23最终核查。已授权范围只有此工作包及B-B1～B-B4四项最小验证，按三个内部里程碑连续开发，每阶段提交，不必等玩家逐一批准。不做B4–B6或Antigravity，最后交一个独立Draft PR和验收报告，停止等用户审查合并，`BPTI_B2_B3_AND_EVIDENCE_COMPLETE_AWAITING_PLAYER`。

**包C（包B经玩家审查合并main后）**：

> 从最新main开始BPTI分组连续交付**工作包C：B4→B5→B6**。权威任务`docs/development_tasks/DEV_20261020_26_BPTI_GROUPED_CONTINUOUS_DELIVERY_AND_FOUR_FAMILY_EVIDENCE_V1.md`第4、5节；另阅读B0/B1/B2/B3/DEV23验收及DEV22、R4和M3/DEV14。已授权范围只有此工作包及C-C1～C-C5五项最小验证，按三个内部里程碑连续开发，每阶段独立提交，不必等玩家逐一批准。不写游戏、不启用V4、不假称30队真实批次已评估；如四类篮球知识未达GM可用必须如实HOLD。最终一个Draft PR与整体验收，停止等用户审查合并，`BPTI_B4_B5_B6_ENGINEERING_COMPLETE_AWAITING_PLAYER`。
