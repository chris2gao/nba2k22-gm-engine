# GM 教练战术操作手册

状态：DEV07 V2 开发中，尚未部署 main。整体防守及混合批次已完成隔离局技术验证；默认六POE沿用既有验证，五数值设置、双体系与命名手册合计14项已有实机写回证据，四Freelance按完整原生枚举与有序接口提供，加上玩家明确开放的原生Tempo，共19项可提案和受控执行。Tempo界面含义未知，不称为已验证的进攻节奏或百分比。板凳深度由GM根据实际阵容选择，没有9–10测试样本上限。不能越过字段字典的生产门槛。本手册随实际验收更新，不代表玩家批准了任何具体战术。

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

## 逐队决定与提案

30 队分别根据已观察的阵容能力、核心角色、深度和教练打法选择 HOLD 或 PROPOSED。每个动作说明具体篮球理由，不全联盟复制一套配置，不承诺固定胜率提升。效果状态为 `SIM_EFFECT_PENDING_PLAYER_MONTH`；技术可用无需模拟比赛证明。

可交给本地离线提案生成器的请求示例：

```json
{
  "requests": [
    {"team_id":0,"scope":"COACH_DEFAULT","targets":{"POEOffense2":7},"action_id":"PHI_DEFAULT_TEMPO","expected_effect":"减少仓促出手；尚无本局效果验证"},
    {"team_id":0,"scope":"VS_OPPONENT_DEFENSE","opponent_team_id":20,"defensive_setting_scope":"OVERALL","targets":{"PressureOnball":1},"action_id":"PHI_VS_IND_PRESSURE","expected_effect":"针对该对手调整整体持球压迫；尚无本局效果验证"}
  ],
  "hold_team_ids":[8]
}
```

示例只说明格式，不是当前球队的正式建议或玩家批准。生成器从所选来源补入真实的 coach identity、全部旧共享块、整体组身份和前值。执行对象是生成后的 `COACHING_BATCH_CHANGE`，不是缺少前值的请求文件。

批次必须含 career_id、source_batch_id、game_season、game_date、policy_id、snapshot_id、batch_id、decision_id、version、status=PROPOSED、actions、hold_team_ids。各动作绑定同一上下文和版本；默认动作携带 verified_coach_identity/old_blocks/changes，整体动作另带 opponent_team_id/verified_overall_identity/old_defense_blocks。旧值、字段、目标值、预期效果必须具体。唯一键为 team_id+scope+opponent；HOLD 不可同时包含该队调整。

GM 外层提案使用 operation=COACHING_BATCH_CHANGE，并提供 coaching_batch、coaching_snapshot、teams、evidence、calculation_refs、data_gaps、requested_approval。验证器核对已发布默认数据和按需读取的对手对象，不接受模型自带的观察事实、approved=true 或执行声明。

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
