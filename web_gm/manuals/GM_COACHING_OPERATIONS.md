# GM 教练战术操作手册

状态：DEV07 V2已通过玩家审查；PR #1于2026-10-18合并main（2509b3b）并同步本地执行仓库。首次真实生产采集/发布尚未运行，等待玩家触发。整体防守及混合批次已完成隔离局技术验证；默认六POE沿用既有验证，五数值设置、双体系与命名手册合计14项已有实机写回证据，四Freelance按完整原生枚举与有序接口提供，加上玩家明确开放的原生Tempo，共19项可提案和受控执行。Tempo界面含义未知，不称为已验证的进攻节奏或百分比。板凳深度由GM根据实际阵容选择，没有9–10测试样本上限。不能越过字段字典的生产门槛。本手册随实际验收更新，不代表玩家批准了任何具体战术。

## GM 核心经营原则：教练不是装饰性设置，而是球队竞争力的生产系统（2026-10-18增补）

**定位**：球员交易解决“有哪些食材”，教练的球队体系、进攻/防守方案、球员角色与使用强度决定“怎样烹饪”。GM在追求当季胜场与长远争冠时，把教练体系作为与阵容建设、交易、签约同等级的核心杠杆；除非确有不可修复的人才短板，不得在没有审查战术适配、负荷与替补资源前直接认定“只有交易能解决”。这一定位由玩家基于模拟终极联盟的游戏经验特别强调，是本项目的**经营优先级**，不是可保证固定胜场收益的游戏引擎公式。

### 全方位影响：当期表现、健康负荷、长期成长

| 影响链 | GM必须考虑的实质 | 证据边界 |
| --- | --- | --- |
| **即时攻防表现** | POE、体系匹配、Playbook、Freelance、战术频率、协防、联防及指定对手整体方案可改变球队使用既有天赋的方式；反映在出手分配、比赛风格、进攻/防守质量和胜负上 | 本项目已认证字段可读写；真实比赛中的具体边际胜率/触发机理必须靠本局反馈，不发明百分比加成 |
| **轮换与疲劳暴露** | BenchDepth、BenchUtilization、攻防打法与比赛负担之间可能存在相互作用；过度集中主力时间、连续高要求战术、训练工作量过高均需考虑恢复成本 | 两项板凳字段可控，**精确上场分钟、球队训练工作量和疲劳值不是这套19+18字段的已验收写入接口**；不能声称改了BenchDepth就直接指定某人的分钟 |
| **伤病与可用性** | 阵容可用性是胜率的前提，策略选择应审查体力余量、伤停、赛程密度和替补质量；高负荷可能提高风险，不能为单场胜利无条件牺牲整个赛季出勤 | 玩家反馈这是重要游戏影响；本项目当前伤病/疲劳来源仍缺，**没有证据可将某一个POE/防守raw值直接映射为受伤概率增幅** |
| **球队训练/角色适配与成长** | 长期观察教练体系与年轻人角色、专项训练方向、上场机会、体能恢复如何协同；避免短期战术挤压培养空间 | 2K22次世代MyNBA官方明确训练影响未来分项属性及高疲劳损失当前比赛有效能力；**PC 2K22／MC本存档的具体训练菜单与生效规则未在本项目认证**。当前教练19+18接口不包含训练计划写入 |
| **场上倾向与底层属性的区别** | 战术、Playbook和球权分配可能改变出手分布、队员跑位及观察到的行为倾向；GM以比赛统计检测 | **战术改变场上行为 ≠ 修改球员存储的tendency/attributes/badges**。没有可信逐月属性/倾向来源，不宣称教练参数自动长期增长某个底层数值；自然成长仍由游戏引擎控制 |
| **文化和世界线** | 高适配体系可在不改任何球员能力的前提下让不同历史阵容发挥优势。现实强队可优先获得适合其球员的战术，历史巨星时代随球员进场建立体系 | 不许仅因现实/历史叙事调高普通球员属性，不用“战术提升”作历史重力写入的代名词，不保送现实冠军 |

### 版本与来源事实层级——不可误用2K22次世代功能

- **官方/开发者描述**：2K于2021年发布的NBA 2K22 MyNBA说明指出，主教练安排训练、球队体系适配、训练强度/疲劳/受伤风险、球员专项发展方向会影响竞技状态或成长；并介绍体育医疗人员的健康作用。这篇材料**明确针对PS5、Xbox Series X|S版本的MyNBA**，不能自动套用为本项目PC版NBA2K22、MC模式或当前外挂字段已认证功能。
- **旧版MyLEAGUE/PC相关社区观察**：教练方案与体系、轮换和战术手册常被玩家用于影响模拟比赛风格；也有教练AI改写计划、发展进程不透明等反馈。社区记录只能支持“值得管理/复核”的判断，不构成具体参数的原生效果证明。
- **本项目最强事实**：同一存档同一时间采集的真实教练原生字段、玩家在PC本局的界面/游戏反馈、实际执行回执，以及后续合法同口径比赛/球员数据。后续GM判断按此优先；未知来源写UNKNOWN，不用外部PS5教程替代本局采集。
- 资料索引（公开、非本局已验证事实）：2K官方 [NBA 2K22 MyNBA介绍](https://newsroom.2k.com/news/nbar-2k22-adds-new-features-to-mynba-for-playstation-5-and-xbox-series-xs-consoles)；开发者详细说明的[转录/图文](https://nba2kw.com/nba-2k22-mynba-full-details-mystaff-training-pre-built-teams-more)；[MyLEAGUE教练与模拟体验讨论](https://www.reddit.com/r/NBA2k/comments/hh6fld/)；[2K22教练AI覆盖玩家设置的反馈](https://www.reddit.com/r/NBA2k/comments/w0v87c/)；[MyLEAGUE训练与成长机制不确定性讨论](https://www.reddit.com/r/NBA2k/comments/im4o6j/)。

### 30队每个经营节点的强制教练评估步骤

1. **先核对新鲜来源**：30队实际阵容、赛季累计与期间可算战绩、真实主教练、已认证19项默认值及指定对手整体设置。首次生产采集未完成或缺`coaching_tactics=VERIFIED_OBSERVED_SAME_BATCH`则标`COACHING_SOURCE_UNAVAILABLE`，只做篮球方向研判，不提交猜值写入；不沿用旧 TEAM POE。
2. **先评估阵容与体系匹配**：核心发动机（持球、挡拆、低位、射手）、防守者横移/协防/护框、篮板、板凳质量；区分真实人员缺口与原有能力未被正确使用。选`PreferredSystem/ActiveSystem/PlaybookID/Freelance`等须查原生字典；**先考虑低成本可逆的战术优化，再比较交易收益与其成本**，并非全队强制改设置。
3. **把强度与健康当作隐含成本**：审查`BenchDepth`（人数上限）与`BenchUtilization`（使用频率）是否让主力承担不必要负荷；选进攻/防守侵略性时说明短期收益与犯规、体力、潜在伤停风险。没有真实伤病/疲劳数据时只给保守风险说明，不编造“受伤概率+X%”或假定某人健康。
4. **按对手匹配防守而不迷信统一答案**：对于真正的重要对手按需读取owner整体文件，利用对手持球、外线与内线威胁、掩护类型、己方换防资源选择18项中的已认证目标。不得为全部29个对手随便复制一组raw值；设置会影响**整体有效matchup组**，不提供个人指定防守/每人分钟写入。
5. **把长短期合并裁决**：争冠队兼顾季后赛战术可迁移性、负荷和伤病缺阵成本；年轻重建队可为持久体系、角色和训练环境作适度短期牺牲；历史纪元球队围绕已出现的历史新秀合理建队，不修改底层能力。发展建议**不等于**已获得训练计划控制权；真实训练调整如需新接口交开发规划基线，而非用教练raw模拟。
6. **每队必须形成明确结果**：`COACHING_PROPOSED`（列球队/对手、合法字段与raw值、原状态、篮球理由、风险）或`COACHING_HOLD`（说明已有配置适配、证据不充分或调整机会成本）。30队均须检查；只详细展开确需变更者。不因“缺伤病来源”停止其他可以做的有据可查经营判断。
7. **闭环复盘**：玩家批准→受控执行→玩家自行继续比赛→玩家触发下一次采集后比较胜负、攻防、核心使用和已观测健康/成长趋势。仅能计算可比期间的差分；现有赛季平均数、个别比赛及生涯进度不允许伪装成某月变化；不可将相关性当成教练因果或宣称已提升固定胜场。

### 具体取舍示范：战术调整不等于乱拉滑块

- **勇士类外线核心**：可先审视外线体系、Freelance、协防与限制对手外线方案；如板凳防守薄弱，要兼顾更强协防可能漏底角、缩短轮换可能过劳的风险，之后才计算增补侧翼的交易必要性。
- **独行侠类高占有率发动机**：匹配挡拆与空间策略，利用己方侧翼防守资源调整对手整体ScreenDefense、PressureOnball等；不要为了压迫而在内线轮转/体能资源不足时盲目提高强度。
- **弱旅年轻核心**：避免把短期数据低迷全归因于球员能力，区分球员尚未成熟、体系不适配和板凳不够；保留有意义的角色成长空间，但不直接编辑其属性或倾向。

**模型职责边界不变**：以上为GM战略决策准则，非新原生字段或写入权限。只准通过既有已认证19项默认与18项整体防守字段提出具体批次；五项Sim、逐人轮换分钟、训练计划、医疗/疲劳数值、个人属性/倾向/徽章绝不借教练批次写入。具体执行仍需用户逐批批准完整action集合与digest，并由Codex核验回读；不要为了证明收益自行推进比赛。

## 第一次正式启用

首次启用按以下顺序核对；这是后续使用流程，不是本次文档修订已执行的动作：

1. PR #1 已由玩家决定合并，执行机器已更新到包含该合并的版本；确认当前代码、profile与本手册一致。本次PR已经玩家批准合并main；执行机器的实际版本仍需与合并提交对应。
2. 玩家触发正常数据采集及发布：沿用 `scripts/run_data_update.ps1` 的真实参数和 `-Publish`；不新增“只采教练”开关，不由开发窗口自动运行。
3. `published/saves/<career>/latest.json` 的新批次已完成上传（`upload_status=UPLOADED`，`data_updated_at/uploaded_at`有效），并指向所选存档与玩家确认的游戏日期。不能沿用尚不含教练来源的旧批次。
4. 新批次 `source_coverage.json` 中 `coaching_tactics` 为 `VERIFIED_OBSERVED_SAME_BATCH`；新来源审计通过，不能仅凭文件存在认定可用。
5. GM可读本批 `coaching/teams.json`、`coaching/field_dictionary.json`，需要某队对手方案时再读该队 `opponent_file`。本批恰有30队，身份、日期与更新时间一致。
6. GM形成提案、离线生成并校验批次；玩家明确批准具体摘要后，执行模型才按[执行手册](../../docs/40_COACHING_EXECUTION_RUNBOOK.md)写游戏。

第一次真实生产采集/发布尚未运行。此处核对的是启用条件，不能把本手册、此前隔离局验证或下面的示例说成生产验证成功。

## 读取本局事实

按 `published/index.json → saves/<career>/latest.json → batch_path` 选择玩家要求的生涯和批次。先核对 `data_updated_at`、`uploaded_at`、`game_date`、career/batch，再读 `coaching/teams.json` 和 `coaching/field_dictionary.json`。不存在这些文件或 coverage 未标 `VERIFIED_OBSERVED_SAME_BATCH` 时，教练来源不可用；不能拿旧 TEAM `poe_*`、另一局截图或现实 NBA 声誉补值。

`teams.json` 含 30 队各自当前 HEAD_COACH 身份、阵容签名、19 项原始值、原始共享块和逐字段 readiness。更换主教练、名单、游戏进程或存档后需要重新取得可信来源。不能在旧采集包里补入较晚读取的教练数值，伪装成同一时点。数据单来源更新尚未实现；请求只更新教练时不能擅自扩大成全量。

GM先读取实际阵容和当前教练设置，自行选择人数、倾向与已知原生枚举。不要把少量测试过的值当作白名单：BenchDepth的9→10只是验收样本，11、12等人数不会因此被拒绝。四个已确认百分比字段的0–100是实际UI范围；原生整数位宽/枚举校验与对象保护仍保留。完整UI端点未知时如实标未知，不编造游戏上限。

所有教练设置的取值判断统一参考本局其他教练的实际值和已核对的原生枚举，不安排逐值试验、菜单端点或保存重启测试。GM据分布、阵容和战术意图选择实用目标；样本最小值/最大值不是执行限制。

仅在确实分析某一对手时读取该队 `opponent_file`，例如 `coaching/opponents/PHI.json`。不要在 GM 启动时一次读取 870 条方案。旧批次不追填新观察。

## 球队默认战术：19 项

作用域 `COACH_DEFAULT`，对象是该队当前 HEAD_COACH。这里的默认表示该队面对所有对手的基础设置。

| 字段 | 篮球含义与允许值 |
| --- | --- |
| POEOffense | 进攻重点：0 NO_PREFERENCE、1 GET_TO_BASKET、2 GET_SHOOTERS_OPEN、3 FEED_THE_POST、4 PICK_AND_ROLL_OFFENSE、5 NEUTRAL_OFFENSE_FOCUS、6 RUN_OFFENSE_THROUGH_SCORER |
| POEOffense2 | 进攻节奏策略：0 NO_PREFERENCE、7 PATIENT_OFFENSE、8 NEUTRAL_OFFENSE_TEMPO、9 SHOOT_AT_WILL |
| POEOffense3 | 进攻篮板：0 NO_PREFERENCE、10 CRASH_OFFENSIVE_BOARDS、11 NEUTRAL_OFFENSE_REBOUND、12 LIMIT_TRANSITION |
| POEDefense | 防守重点：0 NO_PREFERENCE、13 PROTECT_PAINT、14 NEUTRAL_DEFENSE_FOCUS、15 LIMIT_PERIMETER_SHOTS |
| POEDefense2 | 防守侵略性：0 NO_PREFERENCE、16 PLAY_CONSERVATIVE、17 NEUTRAL_DEFENSE_TEMPO、18 PLAY_PHYSICAL |
| POEDefense3 | 防守篮板与转换：0 NO_PREFERENCE、19 CRASH_DEFENSIVE_BOARDS、20 NEUTRAL_DEFENSE_REBOUND、21 RUN_IN_TRANSITION |
| PreferredSystem | 教练偏好体系，0–7原生枚举；原生元数据与独立位域写入/回读/恢复已验收，未单独看到其UI，玩家停止同类重复核对 |
| ActiveSystem | 当前体系，0–7原生枚举；4主打内线→3主打外线已由玩家确认，不修改体系熟练度或评分 |
| PlaybookID | 只能选本次进程已加载且有名的 `playbooks` 条目 enum_id；目录数量动态，不接受任意 0–255 |
| BenchDepth | 板凳深度，即轮换球员人数上限；GM结合可用阵容与目标轮换自行选择。9→10仅为测试样本，没有10人的人为上限；保持原生整数格式校验，不解释为百分比 |
| RunPlayTendency | 执行战术频率，0–100、步长1；70→71已验收 |
| ZoneUsage | 区域联防频率，0–100、步长1；1→2已验收 |
| BenchUtilization | 替补球员使用率，0–100、步长1；40→41已验收，与轮换人数分开 |
| Tempo | 玩家已明确开放原生raw读写；UI及实际效果未确认，不混同POE进攻节奏、SimPace、阵容表现因素或百分比。此前同局8位主帅观测40–95（Rivers80、Kerr95、Nurse40等），可按这些值选择实用目标；0–100仅为据分布推断的参考刻度，不是UI端点证明或执行白名单。8位存储格式只拒绝溢出和非整数，不建议按存储极值制定战术 |
| HelpDefense | 协防，0–100、步长1；50→51已验收 |
| FreelanceType | Freelance 优先级第 1 槽 |
| FreelanceType2 | Freelance 优先级第 2 槽 |
| FreelanceType3 | Freelance 优先级第 3 槽 |
| FreelanceType4 | Freelance 优先级第 4 槽 |

体系原生枚举：0 BALANCED、1 GRIT_AND_GRIND、2 PACE_AND_SPACE、3 PERIMETER、4 POST、5 TRIANGLE、6 SEVEN_SECONDS、7 DEFENSE。

四套 Freelance 用 `freelance_sets:[slot1,slot2,slot3,slot4]` 保留顺序，或只修改一个具名槽。数组与具名槽不能在同一动作中重复指定。原生 34 个名称/raw 映射已由当前进程 enum CRC 与同版本可执行文件标签配对，见本批 `field_dictionary.json` 和仓库 `config/coach_tactics_profile.json`；按原生字段编号保存第1至4槽的顺序，提供全部34种合法枚举；不以测试样本缩减选项。未直接查看本局比赛内四槽页面，不宣称该项UI验证或四套使用概率相同。

五项 `SimPace/SimPress/SimHelpDef/SimOffReb/SimDefReb` 仅允许只读兼容，标 `GM_CONTROL_DISABLED`；任何 GM 目标均拒绝这些字段。逐球员对位、轮换、普通球员能力和全联盟模拟滑块不属于此接口。

## 指定对手的整体防守

作用域必须是 `VS_OPPONENT_DEFENSE`，同时指定 `team_id`、`opponent_team_id`、`defensive_setting_scope=OVERALL`。例如 PHI(0) 面对 IND(20) 的方案不会用于其他 28 个对手。

本局 PC 页面本身就是整体防守，没有额外 All 下拉项。实际存储由该对手的全部有效 matchup 记录组成。一次整体调整会把所选字段应用到整个有效组，保留各记录的球员 ID、已分配防守者、空槽和其他未选字段。**不提供指定某名球员或任意内存槽的目标参数。**

本批字典列出 18 个原生字段及各自合法值：PressureOnball、PressureOffball、ForceDirection、ScreenDefenseOnBall、ScreenDefenseHedge、OffballScreenDefense、PostDefense、DoubleTeamPerimeter、DoubleTeamPost、ScreenDefenseOnBall5、ScreenDefenseHedge5、SwitchRule、OnballHelp、ScreenHelp、ExtendPressure、TagOnRoll、StayAttached、PreRotate。前 17 项分别使用自己的原生 enum，不共享一个通用枚举表；PreRotate 是原生 packed bool，只接受整数 0/1。无法确认的 PC 中文标签保留原生名称，不自行解释 OnBall5、Hedge5 或 TagOnRoll 的页面位置。

已直接配对的 PC UI：PressureOnball 0=自动，1=间隔。一次 UI 操作、程序同范围写入、玩家页面确认及条件恢复均成功。其他原生合法值使用字段字典中的英文标签，不把猜测译名作为观测。

每个整体对象保存全部有效记录的身份和完整 8-byte 前值。`values[field]` 若为 null、且列入 `mixed_fields`，表示当前各记录取值不同，不表示观察不到整个对象。整体目标会有意统一该字段，同时保留所有旧块供条件恢复；不能伪造一个共同旧值。`IsInUse` 是原始提交标记：已观察 UI 退出时 0→1，执行器在数值写完后复现该提交动作；不要将 0 直接解释成禁用或清除原始事实。

## 如何从设置形成篮球方案

下面描述GM选择这些设置的篮球意图与取舍，不声称已验证游戏内部算法或固定胜率收益。先看本局阵容、当前教练和其他教练的实际取值，再选本批字段字典中的合法目标；含义不明时保持 `UNKNOWN`，可以HOLD，不为确定取值另做菜单端点或逐值试验。

| 默认字段 | 决策意图与主要取舍 |
| --- | --- |
| POEOffense | 按核心与空间选择突破、射手空位、低位或挡拆；把主攻方式与实际持球人、掩护人和投射配置对应，不全联盟复制同一重点 |
| POEOffense2 | `PATIENT_OFFENSE`偏向耐心组织，`SHOOT_AT_WILL`表达更快寻找出手机会；根据球权组织与失误风险取舍，它才是已确认的进攻节奏策略 |
| POEOffense3 | `CRASH_OFFENSIVE_BOARDS`争取二次进攻，`LIMIT_TRANSITION`侧重退防；看篮板优势与对手转换威胁 |
| POEDefense | 保护禁区与限制外线之间取舍，看对手突破、内线与投射来源 |
| POEDefense2 | `PLAY_CONSERVATIVE`与`PLAY_PHYSICAL`表达保守或更具对抗性的防守意图；结合犯规、对位与防守资源，不承诺犯规或抢断变化幅度 |
| POEDefense3 | 冲抢防守篮板与更早转换进攻之间取舍；先考虑能否稳定结束防守回合 |
| PreferredSystem | 教练偏好体系，用于表达长期风格；与当前体系分开，不修改任何人或球队的熟练度评分 |
| ActiveSystem | 当前采用的体系，应匹配已观察阵容：如内线支点、外线投射或转换资源；不能把换体系直接解释为球员能力提升 |
| PlaybookID | 从当前已加载、有名称的手册中选择适合核心角色的战术集合；不凭现实球队名称推定本局手册内容，必要时按实际目录理解 |
| BenchDepth | 轮换总人数上限；轮换深度、疲劳与核心上场时间的安排。按可用阵容选人数，不是百分比，也没有10人的人为上限 |
| RunPlayTendency | 预设战术调用倾向；较重视组织化set plays或更多自主处理之间取舍，参考当前持球组织能力 |
| ZoneUsage | 区域联防使用倾向；按对手空间、传球与本队协防配置决定，不承诺对任何进攻必然有效 |
| BenchUtilization | 替补使用倾向；在深度、疲劳与主力负担之间分配，与“最多用几人”的BenchDepth分开 |
| Tempo | `UNKNOWN`：原生raw读写已获玩家明确开放，但当前界面含义和实际作用未确认；只能参考本局教练分布选raw，不能当POE进攻节奏、SimPace或已验证百分比 |
| HelpDefense | 协防倾向；帮助防突破与保留原对位/外线空间之间取舍，结合具体对手整体方案考虑 |
| FreelanceType | 第1槽，规划为主要自由进攻方案；不表示经验证的固定使用概率 |
| FreelanceType2 | 第2槽，可作为对主要方案的补充或针对性替代；保持原生顺序 |
| FreelanceType3 | 第3槽，可用于另一空间结构或节奏选择；不保证AI必然按预期切换 |
| FreelanceType4 | 第4槽，备用方案；同样是有序配置，不是四个无关的随机选项 |

体系名称表达的意图可以作规划参考：`POST`内线支点、`PERIMETER`外线、`PACE_AND_SPACE`节奏与空间、`SEVEN_SECONDS`更早组织进攻、`DEFENSE`防守、`BALANCED`均衡；`TRIANGLE`与`GRIT_AND_GRIND`保留原生名称。具体游戏实现和加成不由名称推定，未知机制仍标UNKNOWN。

四套Freelance先确定本队主要进攻形态，再安排有用的替代，而不是为了填满四槽选四个名字。`FOUR_OUT`、`THREE_OUT`可作为空间结构的名称线索；`FLOW`、`TWENTY_ONE_DELAY`及各队命名方案的本版本具体落位/触发细节为UNKNOWN，不能仅凭名称编造战术过程。完整34项原生目录在文末；数组 `[slot1,slot2,slot3,slot4]` 保留配置顺序，不要求四套均匀使用。

| 指定对手字段（18项） | 篮球策略说明／未知边界 |
| --- | --- |
| PressureOnball | 持球压迫；`GAP`留间隔、`TIGHT/SMOTHER`表达更紧的压迫。按对手投射与突破威胁取舍；已配对UI为0自动、1间隔 |
| PressureOffball | 无球施压；`GAP/LEAVE`表达更多放空，`TIGHT/DENY_BALL`表达更紧或限制接球，取舍是补防空间与失去原对位的风险 |
| ForceDirection | `MIDDLE/BASELINE`表达引导中路或底线的意图；与本队协防位置配合，不推断引擎一定成功封堵 |
| ScreenDefenseOnBall | 持球掩护应对；`GO_OVER/GO_UNDER/SWITCH/ICE`分别表达绕上、绕下、换防或ICE策略。依据投射、突破与换防资源选合法枚举 |
| ScreenDefenseHedge | 掩护延误；`NO_HEDGE/SOFT_HEDGE/HARD_HEDGE/DOUBLE/CATCH_HEDGE`表达不同支援方案，取舍是持球压力、顺下和弱侧空位；精确触发细节UNKNOWN |
| OffballScreenDefense | 无球掩护的绕上、绕下或换防；看对手接球投射威胁与本队追防/换防能力 |
| PostDefense | `FRONT/BEHIND/THREE_QUARTERS_TOP/THREE_QUARTERS_BOTTOM`表达低位前顶、身后或不同侧的防守位置；看接球路线与身后协防 |
| DoubleTeamPerimeter | 外线包夹；`MANUAL/ON_CATCH/ON_DRIVE`按手动、接球或突破阶段表达包夹意图，接受放出其他空间的代价 |
| DoubleTeamPost | 低位包夹；`MANUAL/DIG/ON_CATCH/ON_DRIBBLE`表达手动、短暂协扰或不同触发阶段；`DIG`的本版本具体实现UNKNOWN |
| ScreenDefenseOnBall5 | `UNKNOWN`：保留原生独立字段与自己的枚举，不从后缀5推断适用球员、与普通项的覆盖关系或中文菜单位置 |
| ScreenDefenseHedge5 | `UNKNOWN`：保留原生独立字段；不能未经依据当作普通Hedge的别名或指定中锋设置 |
| SwitchRule | `SWITCH_AUTO/ALL/BIGS/GUARDS`表达换防对象规则的意图；本版本如何划分BIGS/GUARDS及具体无球触发UNKNOWN |
| OnballHelp | `HELP/NO_HELP`表达持球侧支援或保留原对位的取舍；准确中文菜单位置与引擎触发UNKNOWN |
| ScreenHelp | `HELP/NO_HELP`表达掩护场景支援或减少帮助的意图；与Hedge独立，不当作同一字段 |
| ExtendPressure | 扩大施压的原生YES/NO选项；具体扩大到何处、何时触发UNKNOWN，不编造全场压迫效果 |
| TagOnRoll | `UNKNOWN`：保留原生名及AUTO/YES/NO，不凭英文推断本版本具体tag规则或中文对应 |
| StayAttached | 保持紧贴的原生YES/NO意图；具体适用对象、与Hedge/Tag关系UNKNOWN，不自行宣称可消除掩护威胁 |
| PreRotate | 预轮转意图；原生packed bool仅0/1。具体触发和覆盖关系UNKNOWN，不把它解释为另一个AUTO/YES/NO枚举 |

这些动作只影响所选owner队面对指定对手的整体组；不开放逐球员防守或轮换写入。原生英文与raw映射始终以本批字段字典为准，`AUTO`不解释为“关闭”。

## 逐队决定与提案

30 队分别根据已观察的阵容能力、核心角色、深度和教练打法选择 HOLD 或 PROPOSED。每个动作说明具体篮球理由，不全联盟复制一套配置，不承诺固定胜率提升。`SIM_EFFECT_PENDING_PLAYER_MONTH`只是现有合同兼容字段，由生成器填写；它不要求等待一个游戏月份、做胜率验收或推进日期，也不是新的发布/执行门槛。

### 从30队来源到requests，再到完整外层提案

GM先读取本批30队、实际阵容和可用字段，逐队决定HOLD或调整。只为要改的队填写请求；指定对手方案还要选对手并按需加载owner文件。GM负责球队、对手、字段、合法目标raw和篮球理由；确定性程序负责补入career/batch/date、当前教练身份、原始共享块、整体组身份、before_raw及codec版本。**模型不得手写或猜这些原生事实。**

下面是完整可运行的离线例子，沿用先前PHI/IND的说明场景，**不是本局正式建议、玩家批准或新的实机验收要求**。例子表示已审阅30队：PHI两项调整，其余29队明确HOLD。若实际来源没有PHI/IND，按真实球队改意图后再生成，不能伪造队名或来源。`hold_other_teams`是本段说明脚本的篮球意图约定，不是现有CLI的新开关；只有GM明确决定其余队HOLD时才设true。

把以下篮球意图保存为 `_exports/coaching_example/gm_intent.json`：

```json
{
  "batch_id": "COACH_BATCH_001",
  "decision_id": "COACH_DECISION_001",
  "version": 1,
  "requests": [
    {"team":"PHI","scope":"COACH_DEFAULT","targets":{"POEOffense2":7},"action_id":"PHI_DEFAULT_TEMPO","expected_effect":"示例：更耐心组织进攻，不承诺胜率变化"},
    {"team":"PHI","opponent":"IND","scope":"VS_OPPONENT_DEFENSE","defensive_setting_scope":"OVERALL","targets":{"PressureOnball":1},"action_id":"PHI_VS_IND_PRESSURE","expected_effect":"示例：面对IND采用留间隔的整体持球压迫方案"}
  ],
  "hold_other_teams": true,
  "expected_effect": "示例：按所选阵容与对手规划战术，效果以实际游戏反馈为准",
  "data_gaps": []
}
```

以下脚本保存为 `_exports/coaching_example/build_proposal.py`，在**已部署的仓库根目录**运行 `python -B _exports/coaching_example/build_proposal.py <实际career_id>`。它只读已发布JSON、调用现有离线CLI并输出本地文件，不发起GM回合、不连接游戏、不批准执行。它展示的 `proposal` 字典列全外层合同，最终JSON嵌入真实完整batch/snapshot，**没有省略号、伪造旧块或待模型补齐的身份占位符**。

```python
import copy
import json
from pathlib import Path
import subprocess
import sys

root = Path.cwd()
sys.path.insert(0, str(root / "src"))
from gm_core.data_reader import DataReader, attach_coaching_opponents, load_json, safe_child
from gm_core.decisions import validate_proposal

work = root / "_exports/coaching_example"
intent = load_json(work / "gm_intent.json")
data = DataReader(root).read(sys.argv[1])
if not data.coaching:
    raise ValueError("本批没有已审计的教练来源；等待玩家触发首次采集发布")
snapshot = copy.deepcopy(data.coaching)
by_name = {row["abbreviation"]: row for row in snapshot["teams"]}
requests = []
owner_files = {}
for item in intent["requests"]:
    row = by_name[item["team"]]
    request = {key: item[key] for key in ("scope", "targets", "action_id", "expected_effect")}
    request["team_id"] = row["team_id"]
    if item["scope"] == "VS_OPPONENT_DEFENSE":
        request["opponent_team_id"] = by_name[item["opponent"]]["team_id"]
        request["defensive_setting_scope"] = item["defensive_setting_scope"]
        owner_files[row["team_id"]] = row["opponent_file"]
    requests.append(request)
if intent.get("hold_other_teams") is not True:
    raise ValueError("此30队示例须由GM明确其余队HOLD；不能自动代替决策")
changed = {item["team_id"] for item in requests}
holds = sorted(row["team_id"] for row in snapshot["teams"] if row["team_id"] not in changed)

def write(name, value):
    (work / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

write("requests.json", {"requests": requests, "hold_team_ids": holds})
command = [sys.executable, "-B", str(root / "scripts/coaching_batch.py"),
    "--snapshot", str(data.batch_directory / "coaching/teams.json"),
    "--requests", str(work / "requests.json"),
    "--batch-id", intent["batch_id"], "--decision-id", intent["decision_id"],
    "--version", str(intent["version"]),
    "--proposal-output", str(work / "batch.json"), "--output", str(work / "dry_run.json")]
for relative in owner_files.values():
    path = safe_child(data.batch_directory, relative)
    command.extend(["--opponent-source", str(path)])
    attach_coaching_opponents(snapshot, load_json(path))
subprocess.run(command, cwd=root, check=True, capture_output=True, text=True)
batch = load_json(work / "batch.json")
dry_run = load_json(work / "dry_run.json")
if not dry_run["valid"] or not dry_run["executable"]:
    raise ValueError(dry_run)
participants = {a["team_id"] for a in batch["actions"]} | set(batch["hold_team_ids"])
evidence = [{"source_batch_id": data.source.batch_id, "file": "coaching/teams.json",
             "field": "teams", "availability": "OBSERVED"}]
evidence.extend({"source_batch_id": data.source.batch_id, "file": relative,
                 "field": "records", "availability": "OBSERVED"}
                for relative in owner_files.values())
approval_request = {key: batch[key] for key in ("career_id", "batch_id", "decision_id", "version")}
approval_request.update(action_ids=[a["action_id"] for a in batch["actions"]],
                        batch_digest=dry_run["batch_digest"])
proposal = {
    "decision_id": batch["decision_id"], "version": batch["version"],
    "career_id": batch["career_id"], "source_batch_id": batch["source_batch_id"],
    "status": "PROPOSED", "operation": "COACHING_BATCH_CHANGE",
    "teams": [r["abbreviation"] for r in snapshot["teams"] if r["team_id"] in participants],
    "evidence": evidence, "calculation_refs": [],
    "expected_effect": intent["expected_effect"], "data_gaps": intent["data_gaps"],
    "requested_approval": [approval_request],
    "coaching_batch": batch, "coaching_snapshot": snapshot,
    "execution_authorized": False
}
verdict = validate_proposal(proposal, data)
if not verdict["valid"]:
    raise ValueError(verdict)
write("gm_proposal.json", proposal)
write("gm_verdict.json", verdict)
print(json.dumps({"proposal": str(work / "gm_proposal.json"), "validation": verdict,
                  "requested_approval": approval_request}, ensure_ascii=False, indent=2))
```

这个脚本使用现有 `src/gm_core/decisions.py` 校验完整外层提案。`calculation_refs:[]`表示本例没有另行引用计算产物；实际引用数值计算时必须填入真实计算ID，并在验证CLI传同批 `--run`，不能编造引用。篮球理由若引用阵容、合同或统计，应把相应已发布JSON字段加入 `evidence`；本例仅演示教练设置合同，不替玩家生成正式篮球决策。

可以再用现有外层CLI校验文件（完全离线）：

```powershell
python -B scripts/gm_validate_proposal.py --save-id '<实际career_id>' --proposal _exports/coaching_example/gm_proposal.json
```

得到 `valid=true` 仍是结构和来源校验，`execution_authorized=false/player_approval=NOT_GRANTED` 保持不变。`requests.json`不是可执行batch；`gm_proposal.json`也不能作为 `--batch` 输入。执行器读取其中由程序生成的 `coaching_batch`，即 `batch.json`。四套Freelance可在requests中用 `freelance_sets:[slot1,slot2,slot3,slot4]`；生成后会正规化为具名槽的changes。

若网页GM不能运行本地CLI，它只提交篮球意图和真实来源引用，由获委派的本地模型运行上述离线生成和外层校验后再呈交摘要审批；不得由模型补写native身份或前值。完整外层JSON应使用实际生成的文件交接，无需在聊天中手抄30队原始块。

## 批准与生命周期

玩家逐批明确批准 batch_id/decision_id/version/action_ids/digest 后，才交执行角色按 `docs/40_COACHING_EXECUTION_RUNBOOK.md` 操作。任何目标、范围或版本变化都需重新批准。执行回执 `COMMITTED_VERIFIED_IN_MEMORY` 只证明内存提交；游戏保存及后续数据更新各由玩家单独触发。

执行角色顺序调用脚本，不组织并发写入。若收到共享执行锁或未恢复告警，保留当前提案与缺口，不通过更换批次、career标签、工作树或日志目录绕过执行端人工审阅。

GM 赛季聊天按玩家触发的月度、交易截止、季后赛和休赛期节点继续；不自动触发下月、采集、比赛模拟、写入或发布。数据陈旧、换帅、来源缺失或字段门槛关闭时输出具体缺口和 HOLD，等待可信来源或开发验收。

## 原生 Freelance 完整目录（同版本可执行文件 CRC 对应）

下列名称来自已加载原生枚举与同 PE 游戏字符串的唯一 CRC 对应，不编造中文译名。四槽按原生字段顺序提供完整目录；玩家已取消重复菜单验收，当前可执行状态以本批字段字典为准，不宣称已直接验证比赛内中文页面或保存持久性。

| Raw | 原生名称 |
| --- | --- |
| 0 | `DEFAULT` |
| 1 | `TWO_MAN` |
| 2 | `THREE_MAN` |
| 3 | `THREE_OUT` |
| 4 | `WNBA_THREE_OUT` |
| 5 | `FOUR_OUT` |
| 6 | `BUCKS_2018` |
| 7 | `CLIPPERS_2018` |
| 8 | `DENVER_2018` |
| 9 | `HAWKS_2018` |
| 10 | `JAZZ` |
| 11 | `MAVERICKS_2018` |
| 12 | `PELICANS_2018` |
| 13 | `PHILLY_ELBOW` |
| 14 | `PISTON_SNAP` |
| 15 | `SPURS_2018` |
| 16 | `WARRIORS` |
| 17 | `FLIP_PUSH` |
| 18 | `FLOW` |
| 19 | `FORTY_THREE` |
| 20 | `FOURTEEN` |
| 21 | `PACE` |
| 22 | `POINT_FREELANCE` |
| 23 | `PRINCESTON_CHIN` |
| 24 | `SEVEN_SECONDS` |
| 25 | `SLICE` |
| 26 | `SWING` |
| 27 | `TRIANGLE` |
| 28 | `TWENTY_ONE_DELAY` |
| 29 | `BULLS_88` |
| 30 | `CELTICS_86` |
| 31 | `EIGHTY` |
| 32 | `FREELANCE_ONE` |
| 33 | `FREELANCE_TWO` |
