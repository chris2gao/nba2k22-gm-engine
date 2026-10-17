# DEV-20261017-05 — NBA2K22 PC 教练攻防、模拟策略与战术手册：开发前调研及内存定位任务 V1

> 状态：RESEARCH_SPEC_PUBLISHED / MEMORY_DISCOVERY_PENDING / IMPLEMENTATION_NOT_STARTED  
> 2026-10-17 · Web GPT DEVELOPMENT → Codex DEVELOPMENT  
> 仓库：`chris2gao/nba2k22-gm-engine`；游戏：**NBA2K22 Windows PC，2021–22 赛季起**。严格区分PC/MyLeague与PS5/XSX次世代MyNBA；当前玩家多为快速模拟对战。  
> 本任务**仅授权 Codex 做调查、UI 对照、隔离测试存档中的最小内存验证并提交研究报告**。用户要求“发现可行后再开始开发”，所以**不要立即开发生产模块、运行正式GM、修改正式游戏存档，或把可能字段当作已验证能力**。后续正式工程实现单独交付/确认范围。  
> 规则：`config/gameplay_policy.json` (`PLAYER_RULES_20261017_V3`)；任何正常球员能力、潜力、徽章、倾向、性格修改仍禁止，教练战术不能绕开该限制；游戏写入需独立、具体玩家批准。

## 0. 研究目的和最终设计边界

用户表示 NBA2K22 的教练菜单可配置每队攻防和Playbook，实际比赛时 CPU AI 会动态调整，但普通快速模拟是否读设置、是否AI改写设置尚未知。Codex 已找到部分策略地址。本轮不是“设计一个新的比赛引擎”，而是**验证原生游戏已有控制量的准确位置、作用范围、枚举、持续性和普通快速模拟是否真正使用**，从而给网页GM开放有意义、可审批的球队级策略决策。

**开发价值预判**：球队级Sim POE、教练轮换/体系、战术手册可能值得开放；比赛中实时ACE的改写、多对手逐场微操暂不优先。不同模块可以对比说明“可读、可通过游戏UI变更、可在内存安全写入、可随存档保存、普通Sim有效、实际比赛有效、执行器已验收”，这些状态不可互相推出。

**特别注意四个不同对象**：
1. 联盟级 `Simulation Sliders`（全联盟、可能影响模拟算法）：只做实验环境参数记录，绝不能当30队独立GM策略。
2. `Sim Points of Emphasis`（球队级模拟重点）：优先验证，但不能默认已有Team结构偏移正好对应Sim POE。
3. `Coach Gameplan / Coaching Sliders / Defense Settings`：可能有 All Teams 默认方案、指定对手的单独 Gameplan、比赛内临时值、以及 AI 的 ACE/教练自动调整；必须分作用域。
4. `System Proficiency / Playbook / Freelance`：教练偏好、球队激活体系、战术列表和比赛临时调用池可能是不同数据对象；不能只找一个整数即宣布覆盖完整战术手册。

## 1. 可核对资料及证据强弱

### 较直接关联 NBA2K22
- [NBA2K22 Attention to Detail Roster 说明](https://www.operationsports.com/nba-2k22-attention-to-detail-roster-from-celticlg-and-crew/)：社区团队专门为30队修订Coaching Profiles/Coaching Sliders和POE以优化模拟统计。证明有人按此路径调校，不证明具体单字段因果或代码偏移。
- [2K22 MyLeague simulation sliders，PS4帖子](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917042-2k22-myleague-settings-sliders)：展示全联盟Simulation/Team Style Factors等与游戏内比赛Sliders分开；这些是**联盟级**设置，项目中不应被当作单队GM旋钮。
- [2K22 教练菜单防守策略讨论](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/nba-2k-basketball-sliders/917100-nba-2k22-the-eccentric-edition-realistic-ng-slider-set/page11?postcount=140)：针对实战游戏，由社区描述根据对手调整Help Defense、手动gameplan，不能直接推断快速模拟效果。
- [2K22 轮换保存问题](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/920193-mynba-rotations-not-saving)：玩家报告游戏自动轮换、Lineup Performance Factor/Player Minutes开关和保存行为可能影响可持久化性；需用PC实机核对。

### 跨版本概念表（作为Codex的UI核对清单，不得作为2K22 PC的最终枚举）
- [MyLeague旧版Sim POE完整选项讨论](https://www.reddit.com/r/NBA2k/comments/i2g4bi/)：六类Focus、Tempo、Off Rebounding、Def Focus、Aggression、Def Rebounding的英文枚举候选。
- [旧版Sim POE影响快速模拟统计的经验研究](https://forums.operationsports.com/forums/forum/basketball/nba-2k-basketball/922628-getting-realistic-myleague-2.html)：有对统计分布的观察，不等于2K22 PC版本已验证。
- [篮球2K Coaching 模块说明](https://nba2k.fandom.com/wiki/Coaching)：游戏系常见 Coach Gameplan、System Proficiency、Edit Playbook菜单和8类战术体系；不应全部视作2K22当前UI固定项。
- [旧版MyLeague Sim POE/教练滑块提纲](https://gamefaqs.gamespot.com/boards/2000208-sports-and-racing-nba/76861758)：Help Defense/Run Plays/Zone Usage及选手主要得分选择，跨版本候选。
- [2K官方2021-09-08 NBA2K22 Next Gen MyNBA公告](https://newsroom.2k.com/news/nbar-2k22-adds-new-features-to-mynba-for-playstation-5-and-xbox-series-xs-consoles)：Conditional Coaching在模拟中触发条件指令，但官方注明PS5/XSX，**不能在PC本项目上认定已存在**。

## 2. Codex 第一阶段：游戏UI枚举台账（不要先猜内存）

在复制的NBA2K22 PC 终极联盟存档打开教练设置，逐项截图并手动归档：菜单路径（中文/英文）、是否每队可独立控制、是否默认和对手专属分层、所有UI合法取值及默认值、读取/修改后UI是否即时刷新、存档再开是否保留。

候选清单如下。每项都要标示 `PRESENT_PC22|ABSENT_PC22|NOT_CHECKED`，没有的不要硬猜或从别的版本补入。未知初始为NOT_CHECKED。

### A. Sim POE（最高优先级，6组）
1. `sim_offensive_focus`：Neutral / Play Through Star / No Preference / Get to Basket / Get Shooters Open / Feed Post / Pick & Roll 等旧版候选；逐项核实。
2. `sim_offensive_tempo`：Average / Shoot at Will / Patient / No Preference 候选。
3. `sim_offensive_rebound`：Some Crash / Limit Transition / Crash Glass / No Preference 候选。
4. `sim_defensive_focus`：Neutral / Limit Perimeter / Protect Paint / No Preference 候选。
5. `sim_defensive_aggression`：Neutral / Play Physical / Conservative / No Preference 候选。
6. `sim_defensive_rebound`：Some Crash / Run in Transition / Crash Glass / No Preference 候选。
- 若UI存在 `first_scoring_option`、`second_scoring_option`、`third_scoring_option`，另归档；如游戏版本已移除，记为ABSENT，不用人物倾向修改来替代。

### B. Coaching Sliders / Coach Gameplan
- `help_defense`（协防强度）、`run_plays_frequency`（战术执行频率）、`zone_usage`（区域联防频率）。
- `bench_depth`（轮换人数）、`bench_utilization`（替补使用比重）、`lineup_performance_factor`（若有）。
- 每名球员的上场分钟、首发、替补排序与On-the-Fly Lineups，球员必须使用已验证身份，不凭姓名/指针持久关联。
- `player_minutes_auto`、替换模式（轮换/体能）、`ACE`启用状态、进攻/防守自动叫战术：要区分**球队配置 / 玩家本地控制选项 / 比赛临时状态**，不可默认这些都属于每队可控制属性。
- 多队或仅单队可编辑问题，Codex需实机辨别。

### C. 教练体系
- `system_preferred` / `system_active`：Balanced、Grit & Grind、Pace & Space、Perimeter Centric、Post Centric、Triangle、Seven Seconds、Defense这8类是已有`STAFF` profile编码的初步候选。
- `system_proficiency` 是否是只读派生评价、可手动设置或主教练-球员融合计算，**不得直接修改派生分数以提高胜率**。如只有系统选择可写，只使用合法选择，不注入熟练度。

### D. Playbook / Freelance / Plays
- Playbook选择对应的playbook ID / 名称；每队战术本引用、战术数目、各项战术条目ID和顺序；Edit Playbook更换操作。
- Freelance offense（若可选）：方案、Series选项、调用优先级、ACE/手动叫战术关系。
- 注意“战术本改名/ID”“教练战术调用概率”“球员Play Types/Touches”可能属于不同层；**本项目禁止通过改球员的个人倾向或Play Types来配合战术**，最多用其已采集事实做GM分析。

### E. Defensive Settings / Defensive Matchups（优先定义目录，不默认可用于快模拟）
- 队级：On-Ball Pressure、Off-Ball Pressure、Force Direction、On-Ball Screen、Hedge、Center对应两项、Stay Attached、Off-Ball Screen、Post、Perimeter Double / Post Double、Switch Rules、Pre Rotate、Screen Help Rules、Drive Help Rules；如实际UI存在DHO相关选项也纳入。
- 球员对位级：防守目标、指定防守者、按对手个人的压迫及挡拆方案；记录是否 per-opponent 存储、对手球员转会后是否自动失效。
- 比赛临时值：暂停界面/On-The-Fly修改是否仅影响单场，并与赛前Gameplan内存作对照。
- 不把此类设置当作模拟可用，除非P0实证。

### F. 全联盟 Simulation Settings（仅作为实验控制项，不为GM独立修改）
- Simulation Difficulty、Simulated Quarter Length、Team Pace/Team Fastbreak、Possessions、Shots、Assists、Shot Types 等。
- 核对当前存档值，实验固定一致。联盟级参数不因单队GM喜好自动变化，也不能以修改模拟引擎全局滑块实现单队“战术增强”。

## 3. 现有仓库线索和必检异常

- `src/strategy_manager.py` 已提供 `StrategyManager.get_team_strategy/set_team_strategy`，候选Team结构偏移：
  `0xEB2 OFF_PACE`、`0xEB3 FASTBREAK_FOCUS`、`0xEB4 OFF_REBOUND`、`0xEB5 DEF_REBOUND`、`0xEB7 ON_BALL_PRESSURE`、`0xEB8 OFF_BALL_PRESSURE`、`0xEB9 PICK_AND_ROLL_DEF`、`0xEBC HELP_DEFENSE_LEVEL`。这些并未证明是**Sim POE**，可能只是球队比赛策略。
- 旧 `docs/13_TACTICAL_STRATEGIES_AND_BUSINESS_OPERATIONS.md` 含由注释推断的取值和“某体系熟练度95”建议，以及与 `strategy_manager.py` 参数名不完全一致的示例。它是**历史规划/线索，不是实机枚举认证、百分百生效或能力改动授权**。
- `config/gm_policy.json`中的 `poe_on_ball` 明确为`UNVERIFIED_ENUM_CONFLICT_OBSERVED_7_VS_LEGACY_0_TO_4`；旧取值0..4/0..6或历史读到7互相矛盾。无需急于统一，先UI单变量测试确认范围、含义及bit-packed的可能性。
- `config/memory_field_profile.json` 的 `STAFF` 有`preferred_system`、`active_system`三bit字段（需由教练对象定位和岗位关联支持），但不是`TEAM`长期战术引用已认证的证据。
- `src/gm_core/tactics.py` 目前是分析+占位验参，不是可用游戏执行器；`src/gm_core/coverage.py`部分team POE已作为observed观测；无已验收的Playbook、SimPOE完整字段采集器/运行中按对手指令执行器。
- `src/strategy_manager.py` setter只检查uint8 0..255，不验证游戏合法枚举/目标队伍重复身份/共享位掩码/事前授权；不能因写后readback一致就认为游戏战术有效。应核实写入权限、参数名，禁止旧文档未经验证的`pnr_def`示例误导开发。
- 先对 `src/address_calibrator.py`、`src/source_extensions.py`及现有源profile进行复用，不发布指针/未经认证的值作为永久球员或球队ID。

## 4. Codex 第二阶段：UI ↔ 内存定位协议（复制测试存档）

每个字段单独做最小观察：
1. 在复制存档记录进程PID、版本、save ID、当前球员名单、球队内部`team_id`/教练身份、Gameplan范围(All Teams/指定对手/当前比赛)、当前UI原值与字节/结构快照。
2. 在游戏菜单**只改动一个选项**，例如从A→B；在静态会话对比内存变化，排除镜像、UI缓存、别的同时变化参数以及菜单切换噪声。观察是Team结构、Coach结构、League settings、opponent-specific表、playbook数组还是比赛临时对象。
3. 依次测试不同取值B→C→A，反证：恢复原UI值后，候选字节应可逆回到原始值。针对按位编码必须验证读写仅变目标bit，保留同字节其他flag；数组必须校验长度、元素类别和引用完整性，不以固定偏移的整个内存块覆盖。
4. 更换第二支球队同样修改同一UI项，验证两个独立owner的映射；返回第一队确认值没有被全局覆盖；更换指定对手重复以识别对手级索引。注意“选择球队”不一定等于实际控制者，验证对象和场景作用域。
5. 经本轮玩家研发调研许可，若需要验证直接内存写入，只允许在**隔离复制测试存档**对一项已知合法UI枚举做最小可逆写入，遵守当前程序写入权限；观察UI反向更新、返回菜单/进入比赛、存档关闭重开。未具备可信指针/bit语义时保持只读，不试验多字节猜写。
6. 验证保存持久性：当前游戏菜单值→退出菜单→保存→退出游戏→重启读取；更换月/赛季、主教练、比赛对手后的持久性边界分别记录；如果只存在临时比赛对象，不向GM开放为长期球队配置。
7. 检测AI覆盖：快速模拟前后，进入实机比赛前/中/后，ACE开启与关闭（如果是本平台UI可控制），验证原队策略字段是否被改写、是否只覆盖内存运行态、退出比赛能否恢复。
8. 记录`enum_map`：UI中文名/英文名、encoded raw value、类型/bit宽、合法范围、拥有对象ID、来源证据、作用域、存档持久性、当前是否授权/只读。不能用`uint8 0..255`作为合法游戏枚举。
9. 每个重要结果需至少另一支球队和重启进程复验；不要把工作内存指针写进跨存档身份标识。

强制失败状态：`NO_UI_FIELD`、`AMBIGUOUS_ADDRESS`、`UNVERIFIED_ENUM`、`WRITES_NOT_PERSISTENT`、`AI_OVERWRITES`、`WRONG_SCOPE_LEAGUE_GLOBAL`、`NO_SAFE_WRITE_PATH`；允许部分字段通过，不要求全部通过才产出调研结论。

## 5. Codex 第三阶段：模拟效果的最小实证（仅已映射UI设置、复制测试存档）

**分四种运行模式**：普通快速模拟/Sim Through Date（核心）；SimCast；CPU-v-CPU实机；玩家实际对战。每条效果记录 `effect_scope`，不能以CPU比赛影响推断普通快速模拟影响。测试不改任何球员属性、倾向或能力。

- A 基线：不修改配置；
- B Sim POE 单项变更（进攻重点优先，随后节奏）；
- C 原有`0xEBx`球队比赛POE单项变更（确认与B非同一底层字段时）；
- D 教练体系、Run Plays或Playbook单项变更（每次只改一项；分开验证）。
- 保持名单、教练、比赛日程、模拟时长、联盟sliders、对手与主客场一致；随机数重跑/赛季事件会产生自然波动，重开相同存档**不保证**相同随机种子。采用分组/重复、随机顺序或匹配对照。
- 建议先筛查 20场/组，若有信号再扩大每组至少约100场或更多的重复实验，以净胜分/三分出手/节奏/进攻回合分配为敏感性指标；胜率样本需求更大。并非每组100场都能显著证明胜率变化。
- 已知采集来源有赛季累计胜负、每队每季累计技术数据，并非逐场日志。实验报告必须明确数据是否由UI截图/隔离记录/新开发临时读取得来，不许由累积数伪造逐场、月度细节。
- 至少一支以外线为主球队与一支以内线为主球队，不能只评估用户控制球队。
- 保存每组`mean/variance/confidence_interval`和基线差，注明干预字段、实际持久性及覆盖。无效果可能是样本量小或被游戏覆盖，而非“绝对无效”。

对每个字段给出结论：
`SIM_VERIFIED`、`GAMEPLAY_VERIFIED_ONLY`、`PERSISTENT_NO_EFFECT_DETECTED`、`UNSTABLE_AI_OVERRIDE`、`NOT_SUPPORTED_PC22`、`UNRESOLVED`。
区分技术验证`UI_AND_MEMORY_MAPPED`、`SAFE_WRITE_VERIFIED_TEST_SAVE`和效果验证`SIM_VERIFIED`，缺一不可直接当生产可执行能力。

## 6. 计划给GM开放的抽象契约（**只定义设计，不立即开发**）

GM可提出三类方案：
- `SEASON_TEAM_TACTIC`：30队长期默认方案。每队一组经验证的`sim_poe`、`system`、`coach_sliders`、`playbook_ref`、轮换。一般季初/交易后/每个玩家触发的GM节点复核，控制改变次数，不保证“一改就赢”。
- `MATCHUP_TACTIC`：针对指定对手的赛前布置，仅当确认存在`per_opponent`持久数据对象且在相应比赛模式生效时才开放，目标对手、相应球员身份都必须校验。普通快速模拟若不生效则不用于模拟批量优化。
- `IN_GAME_TEMPORARY`：比赛内ACE/临时指令，暂缓开发，不覆盖原生AI；必须显式区分正在跑的比赛引擎临时数据与长期球队设置。

未来`tactics_plan.json`提案应携带：
`career_id`、`season`、`game_date`、`source_batch_id`、`policy_id`、`decision_id`、`version`、`status=PROPOSED`、`team_id`、`coach_id`、`scope=TEAM_DEFAULT|VS_OPPONENT|IN_GAME`、`opponent_team_id?`、`changes:[{field,old_raw,proposed_value,enum_version,source_evidence,effect_scope,readiness}]`、`expected_effect`、`unknowns`、`rollback_plan`。
批准后的执行器还需玩家具体批准、目标球队/教练/存档身份复验、原值检查、白名单映射、逐字段写入/回读、失败回滚、存档重启校验与执行回执；任何MODEL传入的`approved=true`不得当作授权。禁止分析侧`src/gm_core`import游戏写入/内存模块。

## 7. 阶段门槛：找到地址不等于可以开始正式开发

依次完成并明确验收：
- G0 `UI_CATALOG_COMPLETE`：PC22菜单真实可见项目/合法枚举/对象作用域台账；不存在标NA。
- G1 `MEMORY_MAPPING_VERIFIED`：至少拟定核心字段UI↔RAM双向可逆、不同队互相隔离、保存/重开复验，原始证据可以追溯。
- G2 `SIM_EFFECT_CLASSIFIED`：每项对应快模拟、SimCast、实机影响的实验结论；“不确定”仍能进入只读信息采集但不能声称SIM优化。
- G3 `SAFE_WRITE_FEASIBLE`：测试存档最小受控写入、旧值校验与原值恢复、重启稳定，没有不受控副作用。
- **满足G0/G1并证明至少若干核心模拟字段有真实作用且安全可写后，向玩家报告具体范围，请玩家确认下一阶段开发**。本次不自动实现生产模块。若只能控制实际比赛，也可以另报“仅针对玩家对战”的小范围可行设计。
- 未发现Sim POE 或并未生效时停止“模拟优化模块”的假设，不为了交任务强行修改联盟级模拟滑块或个人球员能力。

## 8. Codex 必须提交的调研结果

正式文档：`docs/development_reviews/DEV_20261017_05_COACHING_MEMORY_DISCOVERY_REPORT.md`，字段登记建议 `docs/development_reviews/DEV_20261017_05_COACHING_FIELD_MATRIX.json`。

建议每一字段记录对象：
```json
{
  "ui_path": "Coaching > Coach Gameplan > ...",
  "ui_label": "verified label or null",
  "feature_group": "SIM_POE",
  "scope": "TEAM_DEFAULT",
  "game_platform": "PC_NBA2K22",
  "source_kind": "MENU_OBSERVED",
  "owner": {"team_id": 0, "coach_id": null, "opponent_team_id": null},
  "address_status": "UNVERIFIED",
  "location": {"base_structure": null, "relative_offset_hex": null, "width_bits": null, "bit_offset": null},
  "enum_status": "UNVERIFIED",
  "choices": [],
  "ui_memory_roundtrip": false,
  "writes_tested_on_copy": false,
  "persistent_after_restart": null,
  "ai_override_observed": null,
  "simulation_effect": "UNRESOLVED",
  "confidence": "UNVERIFIED",
  "evidence": []
}
```
此例中的0仅为schema示意，不指向任何球队；未知身份字段用null而不是猜测数字。

报告要包含：实际游戏版本和复制测试存档ID、截图索引、内存位置相对于经核验结构的偏移和共享bit说明、枚举/默认值、AI覆盖时间点、Sim实验分组、哪些可以进入下一步工程开发、哪些暂缓、剩余风险、所有事实的证据级别。可把截图留本地有权限位置而不在公开Git仓库上传含私人信息的原始转储。

更新`docs/34_BASELINE_CURRENT_STATE.md` 时**仅反映真实研究发现**；未开发执行器不得标“已实现”。Code/Git变更只交付本次研究成果与最小安全实验所需文件，不顺带修改`published/`、正式GM方案或玩法policy。对玩家报告后停止，等下一步明确研发任务。

## 9. 给Codex的实际执行顺序（避免探测范围失控）

(1) git状态和当前HEAD → (2) 验证PC版游戏菜单 → (3) 完整填写字段清单 → (4) 优先Sim POE 6项，确认是否独立于现有`0xEBx` → (5) 教练Coaching Sliders/系统 → (6) 轮换/得分核心 → (7) 轻量Playbook身份与数组 → (8) 防守默认及对手专属 → (9) A/B快速模拟、AI覆盖、存档持久性 → (10) 交研究报告、字段矩阵和下一阶段建议，**不得自动开始产品工程实现**。

定位难度高的Playbook数组、逐球员防守匹配、比赛临时指令可以在“未找到”状态早停，不影响已经证实的Sim POE核心交付。优先拿到小范围但高可信的真实证据，而不是宽而未验证的偏移猜测。
