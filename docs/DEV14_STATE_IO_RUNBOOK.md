# DEV14 确定性状态读写引擎 V1.1

状态：`ENGINEERING_IMPLEMENTED / SYNTHETIC_AND_STATIC_VERIFIED / REAL_CAPTURE_NOT_TRIGGERED`。本文件随独立 DEV14 PR 交付，未合并前不能称为 main 已部署。游戏写入、数据采集、GitHub 数据发布仍需玩家分别明确触发；本工程不启用 GM V4，也不合并 M3 Draft PR。

## 三类状态与物理位置

| 数据 | 权威与更新者 | 位置 |
| --- | --- | --- |
| Observed | 玩家触发的 full_verified_v1、原来源审计、SQLite backup/M0 密封副本 | 每档 `league_state.sqlite`、`player_pool.sqlite`；不可变 `query_snapshots/<career>/<batch>` |
| Desired | GM 只提交稀疏意图，Python 从同批来源展开和编码 | 每档 `gm_control.sqlite` 的 desired_change_sets/desired_changes |
| Applied | 具体玩家批准后的原生内存写入与回读；不代表游戏已经保存 | approval_records、execution_runs、execution_blocks、私有 state_io_journals |
| Reconciled | 后续独立全量观察与此前执行结果离线比较 | reconciliation_records，只报告，不自动重写 |

控制库 schema：`database/gm_control_schema.sql`，`user_version=1`，通过 `store.initialize()` 建库/迁移并验证 save_id、save_instance_id、generation_id。静态 registry 以指纹版本投影到 native_field_registry，capability_registry 是查询视图。观察增量表 `state_io_captures/state_io_objects/observed_setting_values` 由采集迁移安装在事实库，与原有 coaching 表并存；后者是原始来源，通用值表是同批派生投影，不是第三个事实权威。

对象按类型共享物理表，不按 30 队复制表。USER/CPU 是明确的 side；不从“30 队外挂经营”推断比赛侧。所有运行时地址只出现在本地执行 journal，不作为下次定位依据。控制库、原始日志和活跃数据库不进入 Git。

## 已接入字段与边界

`src/gm_state_io/registry.py` 读取原 `config/coach_tactics_profile.json`，并读取 `config/state_io_native/` 中归档的 Antigravity 原生目录；后者的原文件 SHA 和相对路径记录在 provenance.json。没有导入原适配器的全权限构造器，也没有执行其测试/修改脚本。

| 域 | 注册/采集/受控写入 |
| --- | --- |
| 教练 | 19 默认字段继续复用 coach_codec；另外 5 Sim 只读，不开放 GM 控制。Tempo raw 含义未知；BenchDepth 不设 9–10 人样本限制 |
| 防守 | 18 OVERALL + 18 PERSONAL，复用 defense_codec。整体展开至所有有效记录；个人目标只有在当前双方名单 native ID 可唯一对应时才产生来源对象。身份/defender/shared 8-byte 前像保留 |
| 球员 | 99 字节倾向区原值；本地目录已命名 48 项可提案，其余 51 项只读、语义 UNKNOWN。4 有序 PlayType + Initiator 受控写入，不写 Ability/Potential/Badge/合同/身体/伤病 |
| 战术本 | 当前在用本的 68 槽；一个对象包含所有共享使用球队，批准覆盖该完整 owner 集合。目标只允许本批已加载目录实际出现的 Play CRC（含观测到的空值），不猜 PlayType/战术行为或接受任意 CRC |
| Gameplay | Antigravity court 目录中的 4 项设置，USER/CPU 分开；按原逻辑同时写 Current/Custom 两个 float32 表，分别保留前值和回滚 |
| World | 两份本地 settings/world 目录中可用的 50 个原生设置，按 slot/group 注册和读写。原生类型正确不代表效果量化或整套玩法配置已经批准 |
| Training | 6 球队训练字段、5 球员训练字段；复用原生 packed 布局。球队按真实 franchise slot 映射，个人 native ID 歧义/缺失时不采、不写 |
| Mentor | 仅 DISCOVERED 扩展位置；关系增删、计数及徽章传授数据尚未适配到统一事务。导师的徽章/进度不通过本引擎直接编辑 |

训练、世界与 Gameplay 根对象不可用时，逐域记录 NOT_OBSERVED/PARTIALLY_OBSERVED，不用 50 填值。现有 required 教练来源和源审计继续 fail closed。原教练三个 CLI 和 coaching_batch.py 保持可用，共享既有按进程加锁机制；管理过的存档同时受 DEV14 生命周期互斥锁保护。

OVERALL 与同一 owner/opponent 的 PERSONAL 混合动作拒绝为 `BLOCKED_UNVERIFIED_OVERALL_PERSONAL_ORDER`；应拆成有独立来源和批准的顺序批次。切换 PlaybookID 与修改内部槽也要求分开批准、重新采集来源后再做第二步。不会猜覆盖优先级后静默吞掉个人配置。

## 存档管理：最多四档，只有一个 ACTIVE

下面命令仅管理本地工作区，不加载游戏、不采集、不发布或写游戏。示例 ID 需换成玩家明确指定的值。

```powershell
python -B scripts/gm_state_io.py save create --save-id career_new
python -B scripts/gm_state_io.py save list
python -B scripts/gm_state_io.py save activate --save-id career_new
python -B scripts/gm_state_io.py save status
python -B scripts/gm_state_io.py save deactivate
```

新档复用 `save_context.initialize_save()`、原 clean template 和静态引用目录，建立空球员池与空控制库，标 `NEW_UNCAPTURED`。已有数据不被 create 覆盖。历史未登记存档须玩家明确认领后才能参加 DEV14：

```powershell
python -B scripts/gm_state_io.py save adopt --save-id existing_career --confirm-existing-save existing_career
python -B scripts/gm_state_io.py save activate --save-id existing_career
```

adopt 不声称旧 M02 属于新登记的实例认证；首次重新触发 full_verified_v1 后才可 stage。每档 workspace.json 是三库路径的单一代次提交点，database/active_save.json 是唯一活动绑定。历史只读查询 `gm_data_query --career A --batch ...` 不切 ACTIVE。新 CLI 没有隐式 legacy-shared。

retire 需 `--confirm-manifest <当前workspace.manifest_digest>`，保留全部历史并腾出四档名额。未恢复执行、APPLYING/PREPARED、遗留的原生过程写锁会阻止切档、停用、退役和重置；不通过换日志目录绕过。

### 同名 reset 的例外流程

优先新 save_id。同名 reset 仅处理玩家明确重开的新世界：

```powershell
python -B scripts/gm_state_io.py save reset --save-id career_new --dry-run
# 将三库、旧代次、归档位置和 manifest digest 交玩家审阅并获得明确批准后：
python -B scripts/gm_state_io.py save reset --save-id career_new --generation <旧generation_id> --confirm-manifest <旧manifest_digest>
```

使用 Connection.backup() 密封三库和执行 journals，校验完整性/归档指纹；再准备全新 generations/<new>/ 三库，最后原子提交 workspace manifest。每次归档使用独立 attempt 目录，失败重试不会复用旧业务状态的备份。旧代次原文件仍保留。新库不继承人物、目标或批准。仅有 stage/apply 的控制状态不能修改历史观察。

本版选择任务书允许的保守兼容方式：该 save_id 已有 published 历史时返回 `BLOCKED_UNSUPPORTED_GENERATION:CREATE_NEW_SAVE_ID`；不修改/删除旧 latest、历史批次或 query_snapshots。同步异常恢复旧 manifest；进程在提交中断导致 active/workspace 代次不一致时拒绝新工作，操作者核对 reset_activation.json 后可以显式恢复旧完整代次：

```powershell
python -B scripts/gm_state_io.py save recover --save-id career_new --confirm-manifest <旧manifest_digest>
```

这不是内存部分写入恢复/解锁入口。部分未恢复写入必须按 journal 人工核对和具体批准处理。

## 全量来源与 GM 读取

唯一正式采集脚本仍是 run_data_update.ps1。管理过的档须 ACTIVE，并由玩家确认实际加载的游戏档。当前没有可靠的游戏内唯一 save ID 读取器，因此不允许无人监督仅凭 `--career` 写入或采集；人工降级确认严格包含 `save_id:save_instance_id:generation_id`，回执披露无法独立识别游戏档的限制。

```powershell
# 玩家已加载对应游戏存档并授权本次完整更新；是否 -Publish 必须另有本次授权
./scripts/run_data_update.ps1 -SaveId career_new -GameDate 2021-12-12 -Season 2022 -Month 2 -Name CHECKPOINT -LoadedSaveConfirmation '<save_id>:<save_instance_id>:<generation_id>'
```

脚本自动交给 gm_state_io capture 持有生命周期 lease，仍调用原 full_verified_v1→审计→backup→M0→JSON，并只在显式 -Publish 时调用原发布器。可用 gm_state_io capture 传已批准的原脚本参数列表；它不是局部采集接口。独立调用托管档的底层 monthly_cycle 会拒绝绕过该 lease。旧未登记档入口兼容；不能借旧档绕过一个已选定的 ACTIVE 工作区。

新域位于同一份事实 SQLite/Release/M0 副本；published manifest/source_coverage 提供轻量能力/代次说明，不生成大型字段 JSON 或独立 latest。

```powershell
python -B scripts/gm_state_io.py registry --domain tendency --limit 20
python -B scripts/gm_data_query.py tendency team --career career_new --team CHA --batch <batch> --limit 20
python -B scripts/gm_data_query.py gameplay search --career career_new --side CPU --field-key gameplay.inside_shot_success
python -B scripts/gm_data_query.py training team --career career_new --team CHA --player-identity <本批identity> --limit 20
```

分域查询包括 world/gameplay/tactics/tendency/training/personal_defense，继承 M0 默认20、最多50、约20KB及固定 batch 游标；不返回原始内存地址。旧批缺新表时保持 UNVERIFIED_FIELD/未观测，不回填新字段。

## 稀疏意图、审批与执行

意图 JSON 仅允许 change_set_id（可选）、decision_id、version、origin_model（可选）、reason、changes。每个 change 严格为 action_id、object_key（来自同批查询）、field_key、target_value、reason。例如：

```json
{"decision_id":"D_EXAMPLE","version":1,"reason":"示例，非批准","changes":[{"action_id":"A1","object_key":"本批查询返回的对象键","field_key":"coach.POEOffense","target_value":4,"reason":"阵容支持挡拆"}]}
```

```powershell
python -B scripts/gm_state_io.py stage --career career_new --source-batch <真实batch> --proposal _exports/intent.json
python -B scripts/gm_state_io.py validate --career career_new --change-set <change_set_id>
python -B scripts/gm_state_io.py preflight --career career_new --change-set <change_set_id>
```

stage 从现有 M0 密封副本取同批事实，稳定排序、编码和摘要；仅写本档控制库，预览最多20项，不打开游戏句柄。preflight 全批 RO，不能设置 APPROVED。批准 JSON 只含 save_id、save_instance_id、generation_id、source_batch_id、decision_id、version、完整 action_ids、digest；文件本身不授权。

玩家批准确切摘要，确认退出相关 Coach/Player/Playbook/Training 编辑页和当前所加载游戏档后，执行角色才可运行：

```powershell
python -B scripts/gm_state_io.py apply --career career_new --change-set <id> --approval _exports/approval.json --approve-game-writes --player-approval-reference '<本次玩家明确批准依据>' --loaded-save-confirmation '<save_id>:<save_instance_id>:<generation_id>' --editors-closed
python -B scripts/gm_state_io.py receipt --career career_new --change-set <id>
# 若玩家批准原动作的条件恢复：使用同一批准绑定，将 apply 换为 rollback
python -B scripts/gm_state_io.py reconcile --career career_new --batch <后续独立全量batch>
```

先整批 RO，再打开 RW 重新核对；相同物理块合并 mask、所有前像安全落盘后才写。逐块写前比较/立即回读；失败逆序条件恢复，仅恢复仍等于本次 after 的块。成功 MEMORY_VERIFIED 不代表游戏保存；部分恢复失败保留共享进程锁和 PARTIAL_UNRECOVERED。重复批次重新 RO 比较目标，变化时拒绝，不盲写。相同 decision/version 不能用不同目标覆盖。

reconcile 只比较最近仍有效的已批准 MEMORY_VERIFIED 结果和后续新观察，报告 MATCHED/DRIFT_DETECTED/NOT_OBSERVED/IDENTITY_CHANGED/GAME_MANAGED_EXPECTED，不采集、不自动纠正。浮点设置比较原生 float32 编码后的值。

## 后续 DEV13 消费合同

DEV13 读取本批 object_key、field_key、source_status、registry_version、save_instance_id、generation_id；用最少稀疏 changes 表达意图。不得生成地址、before hex 或把 SQL status 改成批准。源批、实例、代次、decision/version/action_ids/digest 必须进入批准元组。换队、换档、换进程或原字段变化重新取源/preflight，绝不自动继承旧批准。未注册世界曲线、剩余 Gameplay 目录、未命名倾向、导师关系等按清单继续接入，不自动启动 GM V4。
