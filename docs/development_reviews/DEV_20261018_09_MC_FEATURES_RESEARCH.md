# DEV-20261018-09：运动滑块、MC 主宰与佳得乐只读研究

日期：2026-10-18。状态：`RESEARCH_DELIVERED / READ_ONLY_TOOL_IMPLEMENTED / NO_GAME_WRITE_APPROVAL`。
任务书：[DEV09](../development_tasks/DEV_20261018_09_MC_MOVEMENT_TAKEOVER_GATORADE_RESEARCH_V1.md)。
结构化证据：[字段矩阵与现场差分](DEV_20261018_09_MC_FEATURES_EVIDENCE.json)；研究 profile：`config/mc_features_research_profile.json`。

## 1. 结论和实际范围

| 项目 | 已证实 | 未证实／不能据此声称 |
| --- | --- | --- |
| 持球运动滑块 | 定位到活动 `TUNEDATA_SAVED`、原生参数索引、USER/CPU 两列及 float32 缩放；玩家菜单差分确认两侧最低速度与 USER 最低加速度 | 尚未证明这些 Min 被 MC 运球／篮球弹跳动画实际消费，也未证明玩家、队友、对手如何选列；没有修复效果或胜率结论 |
| 终极联盟→MC | 同一 PID／创建时间下，玩家加载 MC 后活动设置对象地址相同、当前整表相同、预设仍为名人堂 | 只证明本次会话的共同活动对象；不是不同存档持久设置相同、不会重置或保存重开仍保持的证明 |
| MC 主宰类型 | `MyCAREER0004`、Tyrese Haliburton 的职业索引→名单人物→Blacktop 关联成立；原生 type=2 `SHOT_CREATOR` 与玩家报告“运投高手”一致 | 没有切换主宰、写入／保存／比赛效果验证；充能、激活、团队主宰分别未认证 |
| Gatorade | 绑定人物的三类原生数量字段均为0，Gym Turbo 剩余场次为0；玩家看到佳得乐“未获得”、灰图标及“未训练” | 数量非零是否足以激活效果、每周加成到期、额外体力槽及离线覆盖行为均未验证 |
| Gym Rat | 找到 `CareerGymEliminatorBadge` 原生候选位，当前为0 | 与实际 Gym Rat UI／永久效果的精确对应未认证；它属于徽章存储，本任务禁止徽章写入，不能借佳得乐接口修改 |

只读探针：`scripts/research_mc_features.py`；实现：`src/mc_feature_research.py`。没有加入任何正式可写执行器，未修改普通球员能力、潜力、倾向或徽章，没有购买／消费／解锁道具。未运行数据流水线、正式 GM、比赛模拟、游戏保存或发布游戏事实。

## 2. 现场和证据链

- 初始场景由玩家确认：NBA2K22 PC 本世代、终极联盟测试存档、CPU 运动滑块页面、名人堂。没有自动菜单识别；本次没有截图或 UI 自动操作。
- 当前进程 PID 552，创建时间 `2026-10-18T11:43:01.803000+00:00`。读取到 PE timestamp `1652287197`，image size `115056640`，x64；这些是本次指纹，后续必须重新核验。
- 普通命令进程首次 OpenProcess 返回错误5；使用仅运行本次只读脚本的管理员研究子进程后成功。游戏句柄一直为 `PROCESS_VM_READ | PROCESS_QUERY_INFORMATION`，无 RW 句柄或进程注入。
- 先保留 CPU 页完成基线和差分。玩家按请求手动改变单项；程序只读采样。取得并恢复所需证据后，玩家明确进入 `MyCAREER0004`。没有自动换存档、退出菜单或重启。
- 原生类型描述符、字段 CRC、格式、位宽、引用类型和枚举均在当前进程核对。代码切片与原始现场记录在本地 `_exports/dev09/`，不提交模块二进制、运行时地址或完整结构探针。

## 3. 运动设置原生定位

`TUNEDATA_SAVED` 大小 `0x7E4`：`GameStyle +0`，`CurrentTable +4`，`CustomTable +0x3F4`。每表126组，每组8字节，由两个 float32 构成。双侧通过玩家差分核对：列0=USER，列1=CPU。

研究定位器扫描当前 `.text` 的唯一 getter 签名，再解析 RIP-relative 位移取得索引映射和活动对象指针槽。现场 getter RVA 为 `0xAC1F60`，索引映射 RVA `0x39805F0`，活动指针槽 RVA `0x632B4A0`；后续扫描仍须唯一匹配、构建指纹及原生元数据通过，不将这些证据 RVA 当成跨版本授权。

getter 原生逻辑：native enum ID→索引表→`object + 4 + index*8 + side*4` 读取 float32。`SpeedWithBallMinRating` 原生 ID112映射索引111，不能把 enum ID直接当数组索引。与旧固定地址不同，这里有当前代码读路径、描述符、真实对象及菜单差分的联合证据。

| 字段 | native ID／表索引 | USER 相对对象偏移 | CPU 相对对象偏移 | 本次两侧原值 |
| --- | --- | --- | --- | --- |
| SpeedWithBallMaxRating | 111／110 | `0x374` | `0x378` | raw约0.70，对应70 |
| SpeedWithBallMinRating | 112／111 | `0x37C` | `0x380` | raw约0.40，对应40 |
| AccelerationWithBallMaxRating | 115／114 | `0x394` | `0x398` | raw约0.70，对应70 |
| AccelerationWithBallMinRating | 116／115 | `0x39C` | `0x3A0` | raw约0.40，对应40 |

CPU 四项 UI 原值由玩家明确报告为40／70／40／70；USER 两项 Min 有单项 UI／内存差分，USER 两项 Max 是原生读取，未单独宣称 UI 实测。相邻无球运动的4项也由原生索引读取，研究未修改它们。所有显示缩放和比较由 Python 计算。

### 最小差分与恢复

1. CPU 持球速度（最低）40→41：当前表仅 `+0x380` 由 `cdcccc3e` 变 `85ebd13e`；USER 列不变。玩家恢复40。
2. USER 第一次实际改的是“持球速度（最低）”，玩家后来明确抄名确认：`+0x37C` 同样40→41。未把这份样本错记为加速度证据。
3. 玩家将 USER 最低速度恢复40，再把页面称“控球加速”的最低项40→41：对应 `+0x39C`，证明另一参数及8字节步长。
4. 玩家恢复40并选回名人堂。最终 `GameStyle=4`，整个 `CurrentTable` 与初始逐字节相同。

原生枚举4=`TUNEDATA_GAMESTYLE_HALLOFFAME`、10=`TUNEDATA_GAMESTYLE_CUSTOM`。第一次菜单改值自动把4改成10，并将当前表复制到原先为空的自定义缓存；代码路径 `0xB2E190` 也可见复制及置10。最终自定义缓存仍有252个变化的4字节值；它不影响“当前表和名人堂预设已恢复”的结论，但完整 `0x7E4` 结构不等于初始，不能声称所有字节恢复。没有程序清零缓存或保存更改。

### MC 共用范围与动画效果

玩家进入 MC 后，在相同进程中重新扫描签名／校验元数据：活动指针仍指向同一对象，当前整表仍相同，名人堂仍为4。因此本次可记 `SAME_SETTINGS_INSTANCE_CONFIRMED_THIS_SESSION`。

尚未追到这些四项具体值最终进入运球动画时间或篮球弹跳更新的调用链，也没有在比赛中取得正常实战反馈。通用设置 getter 可读不等于动画消费已确认，状态仍为 `GAMEPLAY_CONSUMER_UNVERIFIED`；MC 本人、队友、对手的 USER／CPU 选列仍未知。本次不通过改 Game Speed、降难度或改人物能力作兜底，不安排大量比赛或重启试验。

### 旧 slider_manager 审计

`src/slider_manager.py` 的 `ADDR_SLIDERS=0x063319F8` 不能作为这四项的实际定位依据；本次以原生读链解析到的是指针槽及其指向的活动对象。旧 `GAME_DIFFICULTY` 偏移和投篮等常量未被本任务认证，不能据其命名补造 Movement 字段。

没有调用 `inspect_current_state` 或 `lock_realistic_sliders`；后者还会修改伤病、交易、时间等无关字段。旧设置／交易地址的其它用途不因本研究被一概判错，但本次不得使用旧一键入口来处理持球动作。

## 4. MC 主宰：已找到独立类型位域

玩家提供存档名及主宰界面。程序从当前原生 CAREERMODE 指针读取 `PlayerIndex`，经实时名单目录解析人物，严格匹配 `Tyrese Haliburton`，再跟随 `PLAYERDATA.BlacktopData +0xE0` 的完整指针。当前目录索引1234、native UniqueId7598只作本次关联证据，不当跨存档永恒身份。最初玩家拼写 `threse` 时工具拒绝匹配，玩家更正 `tyrese` 后才继续。

`BLACKTOPDATA` 大小 `0xD4`。`CareerModeTakeoverArchetype` 在 `+0x80` 的32位共享块，start bit21、width4，mask `0x01E00000`；当前完整前值 `00004000`（little endian）、raw2。它与扣篮／动画字段共享块，未来必须读改写并保护全部邻位，不能整块替换为type数字。

| raw | 原生主宰类型 |
| --- | --- |
| 0 | SPOT_UP_SHOOTER |
| 1 | SLASHER |
| 2 | SHOT_CREATOR（本人物，玩家 UI：运投高手） |
| 3 | PLAYMAKER |
| 4 | POST_SCORER |
| 5 | LOCKDOWN_DEFENDER |
| 6 | RIM_PROTECTOR |
| 7 | GLASS_CLEANER |
| 8 | DEFAULT（原生值存在，不建议把它当一个已验证可选专长） |

枚举9项由当前进程表及同版本名称 CRC核对。次主宰字段存在于 `+0xA0` bit28..31，当前raw0；解锁位在 `+0xA4` bit20，当前0。仅发现存储不能证明 PC Current Gen此人物可用次主宰；不改或解锁。

| 对象 | 本次结论 |
| --- | --- |
| TAKEOVER_TYPE | 身份绑定、原生位域／枚举及当前 UI已对应；可设计独立受控类型接口，无需改能力／徽章 |
| TAKEOVER_METER | 未定位当前充能值；`AI_PLAYER.takeoverPointsBeforeChallenge`是特定缓存名，不能冒充当前条 |
| TAKEOVER_ACTIVE | 未定位当前比赛激活状态；不得用type非零判断激活 |
| TEAM_TAKEOVER | 全局 `TeamTakeoverDisable`、recap `TeamTakeoverEnabled` 不等于当前团队充能或激活对象；本次未认证 |
| 保存与派生缓存 | 未写／未保存／未验收类型切换后的模板校验、刷新和持久性，不称永久修改成功 |

原生字段可读是实施依据，不是一次已完成切换；没有将次世代 Mamba Mentality 套用于本世代。

## 5. 佳得乐、训练和 Gym Rat 分开处理

以下偏移相对当前人物的 `BLACKTOPDATA`，只有 Gym Rat 候选位相对 `PLAYERDATA`。

| 状态 | 本次原生证据与读数 | 限制 |
| --- | --- | --- |
| GatoradePrimeChews | `+2`，16位原始整数，0 | 与未获得 UI相符；还未区分库存、场次与实际消费时机，不承诺写数量即可激活 |
| GatoradeThirstQuencher | `+4`，16位原始整数，0 | 同上；与属性耐力字段不同 |
| GatoradeRecover | `+6`，16位原始整数，0 | 同上；三类分别登记，不是一个总开关 |
| BoostGamesLeft_GYM_TURBO | `+0x78`，32位块bit16..23，0 | 是原生“剩余场次”字段名，不能冒充每周到期计时或额外体力条当前效果 |
| 每周锻炼 | 玩家 UI显示未训练 | 未定位已认证的周完成状态／时间戳／到期记录；不把故事奖励EarnedBoosts自动解释为每周训练 |
| Gym Rat | `PLAYERDATA +0x4C2` bit1 的 `CareerGymEliminatorBadge`=0 | 徽章存储候选；未证明UI和永久效果对应，本轮禁止徽章写入 |

玩家补充：佳得乐页面显示“未获得”、灰色图标，训练显示“未训练”。没有收到单独的 Gym Rat 图标／永久加成界面证据，不能从其未提及推定完整状态。

[2K 官方服务状态](https://support.2k.com/hc/en-us/articles/33058906107667-2K-Online-Services-Status)确认 NBA2K22 在线服务于2023-12-31停止；官方列出的离线模式包含MyLeague等，没有MyCAREER。这里应区分官方在线购买／账户授予不可用与玩家当前可以加载的本地 MC 环境：后者已实际读取，不能因停服就否定本地字段存在，也不能因本地字段存在声称商店／服务器资格恢复。没有访问账号、VC、商店交易或伪造授权。

社区 Gym Rat／周奖励覆盖讨论仅是候选线索。任务书链接的 [Current Gen 玩家原始帖子](https://www.reddit.com/r/NBA2k/comments/pouwos)搜索摘要提供周奖励可能遮盖Gym Rat显示的线索；本次完整页面未成功打开，不将其作为本存档事实或native字段认证。运动社区页面访问出现重定向循环，也没有据此认证动画效果。

## 6. 已交付接口与后续受控接口设计

本次已实现并在实机运行的是**只读研究接口**：

```powershell
python -B scripts/research_mc_features.py --output _exports/dev09/new_observation.json --mode-context PLAYER_CONFIRMED_MC --expected-mc-name "Tyrese Haliburton"
```

命令要求实际研究子进程有读游戏权限；本轮已由管理员只读子进程运行。输出必须是项目 `_exports/` 内的新 JSON，不覆盖旧证据。`--mode-context`和`--ui-side-context`是玩家提供的上下文，不能自动识别页面。可用 `--compare` 比较同进程／同对象／同profile的既有研究快照；字段门槛、版本和对象变化时失败。这个工具不会全量采集、入库、导出生产包或启动GM。

未来接口的具体约束：

1. `GLOBAL_GAMEPLAY_MOVEMENT`：明确USER或CPU、仅批准的Min字段、真实原值／目标UI值／float bytes、当前名人堂预设和整表前像；保持Max、无球、Game Speed、难度、人物能力不变。必须区别菜单setter自动切自定义与直接小字段写；不能调用一键设置或批量回放整个表。动画消费未确认时仍为实验接口，不承诺修复。
2. `MC_TAKEOVER_TYPE`：当前 MC／玩家确认存档与姓名、native身份／Blacktop关联、目标合法原生枚举、完整32位前像和mask、只读预检查、具体批准、单块masked写、读回及邻位核对；异常停止、按原值／目标值条件恢复。目标主宰尚由玩家选择，当前没有任何类型切换批准。
3. `MC_GATORADE_STATUS`：三类数量、Gym Turbo场次、周训练、Gym Rat分别提出。先验证数量和效果／覆盖关系；当前不能把它们合成“激活佳得乐”按钮。Gym Rat徽章位仍受本任务禁区约束，不能随接口开发放开。

任何未来写入测试须先交付精确人物／存档／字段、原值→目标值、保留位和恢复方案，玩家明确批准后另行执行。程序没有写入参数，JSON不能开启写入。当前交付不取代下一次正式受控执行器开发／验收／具体方案批准。

## 7. 验证和基线维护

- 新只读CLI已在 PID552 的终极联盟恢复现场及随后MC现场运行；最终MC CLI额外核验8项运动字段名称CRC、7类原生结构及人物索引／姓名，type2与玩家UI一致。原始输出在 `_exports/dev09/final_native_reader.json`、`mc_cli_final.json`。
- 最小离线负面验证：`python -B -m unittest discover -s tests -p test_mc_feature_research.py -v`，9项通过。覆盖拒绝RW、短读、未知构建、签名候选计数、侧列／非有限值、native字段漂移、进程绑定、恢复与自定义缓存差别、输出目录和MC姓名要求。没有以这些离线结果认证游戏写入。
- `python -B scripts/research_mc_features.py --help`已运行。不运行旧全套、JSON同步核验、游戏写入、比赛、保存或重启测试。
- 更新文档33/34/36、字段索引31及source_catalog的研究入口；生产 `full_verified_v1` 和玩家触发／明确Publish契约保持原样。本研究未将测试或MC探针拼入 `published/` 或SQLite。
