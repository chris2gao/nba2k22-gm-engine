# DEV23 — 核心Playbook语义与角色证据 V1

日期：2026-10-20。终结状态：**BPTI_DEV23_PARTIAL_REQUIRES_PLAYER_DESCRIPTION_TASK_CLOSED**。

本次独立研究从main `b3ace72c807dad412a8187fc9563f78ed19f02fb`开始；B1 PR #9已合入main（`f4d615c14f0b541fc9f1395b7035952b01e0e417`）。完整机读清单见[研究库存JSON](BPTI_DEV23_PLAYBOOK_SEMANTICS_INVENTORY_V1.json)。这是DEV23研究交付，不是B2 NativeBinding实现或GM来源安装。

## 1. 已完成与未完成

已完成三队各68槽的静态/只读内存盘点、历史对照、球员有序类型读取、核心动作研究线索和十家族B2建议。三本共204槽、148个非零槽；从本机PE静态字符串精确CRC匹配到89个不同CRC，覆盖111个槽位。37个非零槽名称继续UNKNOWN；56个空槽也逐项保留，未用其它书补齐。

**未认证任一具体战术的原生PlayType、发起人、第一受益人或第二选择。** 本轮没有实际比赛观察，所以不能宣布Motion、Creator-Midrange或Bam Hub已经完整落地。所有相关书槽修改保持HOLD。需要玩家另一次任务提供少量文字菜单事实，本任务交付后关闭。

| 当前本机研究对象 | book index / enum / unique_id | 非零槽 | 静态名称对应槽 | 未知名称非零槽 | 与历史同名书CRC差异 |
|---|---|---:|---:|---:|---:|
| CHI / Bulls Playbook | 2 / 2 / 3 | 44 | 19 | 25 | 0 |
| MIA / Heat Playbook | 8 / 8 / 10 | 41 | 35 | 6 | 0 |
| GSW / Warriors Playbook | 28 / 28 / 29 | 63 | 57 | 6 | 0 |

槽索引从0开始。按现有读取器分组：0–29 REGULAR、30–49 BENCH_GROUP、50–59 ENDGAME、60–67 FAVORITE。分组名称沿用项目结构，不证明调用时点。FAVORITE中如ISOLATION/POSTUP的静态标签可能是类别标识，不能把它们当成一条已解码的完整动作脚本。Heat的`FIST 14 POP`分别出现在槽2和8，保留两个槽，不能从重复数推出调用权重。

## 2. 来源、方法与可复核范围

机读文件E01–E08记录源码/文件SHA、批次、观察时间和证据用途；没有绝对内存地址、原始dump或可写请求。

- E01/E02：重新读取`coach_locator.py`、`tactical_reader.py`、`gm_state_io/registry.py`、`config/state_io_native/player.json`及provenance。PLAYBOOKDATA为0x168字节；68个uint32从相对偏移0x58起。四个PlayType位段在PLAYER相对0x168/0x169，Initiator在0x16a bit2。**相对结构布局不是当前对象地址**。
- E03：只读打开密封`query_snapshots/mc_haliburton_2021/2021-2022_M02_DEC12_FULL_20261018_bee1cb016256_e94b241a_TS2/league_state.sqlite`。原始来源批次`2021-2022_M02_DEC12_FULL_20261018`，观察时间`2026-10-18T12:12:12.253755+00:00`。从`coaching_source_captures.metadata_json.playbooks`读取84本的既存目录，只展开三本；对三队47条历史名单仅解码所需战术三字节。历史勇士缩写是`GS`，当前是`GSW`。
- E04：普通权限第一次OpenProcess被拒（Windows error 5）；玩家明确要求管理员权限后，以隐藏管理员Python进程执行现有`GameMemory(read_only=True)`与`CoachLocator.calibrate()`。重新验证模块/原生字段、球队/名单互指关系、当前教练绑定与三队书槽，读取46名当前球员的类型。进程读取权限仅QUERY_INFORMATION/VM_READ，句柄在finally关闭。没有调用正式采集、写入器或游戏UI。
- E05：本机`NBA2K22.exe`的PE timestamp为1652287197，当前模块SizeOfImage为115056640；静态文件与运行时timestamp相符。只在`.rdata`搜索NUL边界ASCII/UTF-16LE字符串，将标准CRC32与**已观测三本书的CRC集合**精确相交，保留可复核模块相对偏移。先前有限模块候选字符串读取也交叉观察到标签；不宣称对89条都逐一建立了运行时动作对象关系。
- E06：额外找到了game-root `config/play_catalog.json`（232条）及Antigravity `_research_generate_catalog.py`。该脚本穷举名称后匹配CRC，`categorize_play()`按prefix/substring猜类型；232条CRC数学上匹配，不等于类型原生认证。旧适配器所指自身`config/play_catalog.json`实际不存在，生成文件在游戏根config，不能把load函数存在当作已部署完整字典。
- E07/E08：读取M3 `attach_tactics`安全投影、DEV14同名书绑定、B0/B1契约、十张SystemCard、R1自主层级、R3映射及两份战术关系研究。旧文中的固定Touches/Shot阈值、2022结果和强受益人推论均未提升为本机事实，也没有加入普通GM可见知识。

SQLite连接使用`mode=ro`；调查用脚本/日志留在本地`_exports/dev23`，不入Git。核心历史投影相当于：

```sql
SELECT snapshot_id, save_id, observed_at, context_json, metadata_json
FROM coaching_source_captures WHERE snapshot_id = :batch;
SELECT team_id, observation_json FROM coaching_team_observations
WHERE snapshot_id = :batch AND team_id IN (3,10,29);
SELECT team_id, roster_slot, pool_slot, player_name, face_id,
       length(raw_struct), substr(raw_struct,361,3)
FROM player_source_details WHERE snapshot_id = :batch AND team_id IN (3,10,29);
```

SQLite substr从1起，361对应相对0x168。此次是专项研究派生，**没有修订历史数据库、脱敏旧库或绕过`require_gm_sanitized()`**。当前游戏存档身份/日期未经玩家确认，因此当前内存只有独立DEV23研究批次，不挂接`mc_haliburton_2021`。两次书槽相等不证明是同一个存档；47条历史名单与46条当前名单分别保存，不按旧pool_slot拼接成当期GM球员。

## 3. 三个证明层与真实覆盖

| 分类 | 本次结果 | 可推出什么 |
|---|---|---|
| UI_OR_STATIC_LABEL_VERIFIED | 111槽 / 89不同CRC | 本机静态字样存在，精确CRC与原生槽一致；没有观察UI |
| RUNTIME_ASSIGNEE_OBSERVED | 0 | 已读coach→book和player→PlayTypes，不等于某条战术分给某球员 |
| IN_GAME_EXECUTION_OBSERVED | 0 | 未开展比赛，不证明ACE按该动作执行 |
| PLAYTYPE_COVERED | 0 | 没有认证的逐战术native type |
| TYPE_MATCH_ONLY / TYPE_MATCHED_ONLY | 0 | 只有类型交集认证后才可使用，当前不输出假匹配 |
| STATIC_PLAY_TYPE_UNSERVED | 0条可认证结论 | 这是缺证据，不代表所有球员都被服务；统一TYPE_UNKNOWN |
| BENEFICIARY_UNKNOWN | 所有111条具名槽记录 | 发起、第一/第二受益人全部UNKNOWN |
| UNSUPPORTED | 实时scram/peel、保证末段指定人、保证reset/re-screen分支 | 未有认证专用控制，不是宣称原版游戏绝不发生这些动作 |

68槽的反射字段有enum descriptor，但本次读取槽0所引用descriptor的entry_count为0；没有得到可解码的“Play CRC→PlayType/actor”表。不能把字段有enum指针、球员type名称或某个`GIVE`字样当成已经找到了类型对应表。

本机静态名与CRC的对应仍是严格限定的**字符串/数学关联**，不是完整动作定义解析；若同CRC出现多字符串应保留歧义。当前库存不把一条CRC绑定到唯一球员；相同CRC在不同本/不同槽分别保留，之后发现实际分配冲突可多态追加。没有认证运行时分配时，不能先宣布其随阵容变化已得到实证。

两个旧合成候选仍隔离：CHI槽0 `0x5bc642a3`/`FIST 21 FLARE`；槽13 `0xdadcf884`/`GIVE 15 CROSS`。本轮未找到其静态字符串佐证；不指控它们不存在，也不借其猜测类型做匹配。

## 4. 三种哲学和核心动作线索

下表中“角色/用途”是篮球或名称推论，**所有原生actor、primary option、secondary option均UNKNOWN**。完整槽证据和UNKNOWN项在JSON。不是跨队借书建议。

| 重点 | 本队已见静态名称与槽示例 | 角色/用途研究方向 | 精确不足 / fallback |
|---|---|---|---|
| Warriors Motion | 槽3 FLOPPY；槽4 QUICK 32 HORNS；QUICK 2 SPLIT FIST | 移动射手接掩护、掩护连接者、第二侧选择 | 不能由名字保证Offscreen 3、Curry/Klay第一受益或split阅读；HOLD槽修改 |
| Warriors cut/handoff | 槽11 GIVE WARRIOR FIST；12 GIVE WARRIOR FIST 2；14/15 CUT POINT 2/3 | cutter与connector的球权衔接 | GIVE不是原生13/12已认证映射；切入是否来自掩护后、谁传给谁未知 |
| Bulls Creator-Midrange | 槽19 QUICK 12 PINDOWN；GIVE 32 ANGLE；FIST 25 DOWN | 接球进入创造、次持球接应的研究起点 | 公牛25个非零槽仍无静态名称；不能宣告缺ISO，也不能把pindown当保证中投/face-up；需菜单文字 |
| Heat Butler持球/攻框 | 槽2/8 FIST 14 POP；18 GIVE 52 CLEAR；24 CUT 15 LOOP | 持球创造与切入第二选择 | CLEAR≠原生Isolation enum，不能保证Butler接球；HOLD |
| Heat Bam高位策应 | 槽15 GIVE 52 RUB；16 GIVE 51 FLIP 12 | handoff passer、receiver和弱侧cutter职责假说 | 未见Bam具体分配；当前Bam PlayTypes并非据此自动改成Handoff Passer |
| PnR持球/顺下/外弹 | Heat槽5 FIST 5 SLIP DIVE；6 FIST 5 SHORT ROLL；2/8 FIST 14 POP | handler/roller/popper/短接应角色假说 | SHORT ROLL字符串不认证4v3脚本及受益人，无法保证roll/pop选择 |
| Post/High-Low | Warriors槽16 PUNCH POINT；19 PUNCH 12 HIGH；23 PUNCH 81 ANGLE；三本槽56 HIGH 4 PINCH END | post threat、entry passer和高位连接者 | 低位/高位类型、face-up、high-low第二入口未认证 |
| Elbow/Hub | GIVE HORNS QUICK、HIGH 4 PINCH END与本队已见GIVE系列 | elbow接应→手递手/空切研究 | 不因HORNS/PINCH词创建“Point-Center原生按钮”；不能借其它书的CRC |
| late-clock/reset | 三本都有ISO 1 END、ISO 1 GO END、ISO 1 FIST END、FIST 5 END等ENDGAME槽 | bailout creator、reset connector | 可确认末段组名称，不能确认时间阈值、调用概率、指定人、reset/re-screen分支 |

`QUICK 12 PINDOWN`本次匹配在**公牛**，没有在勇士已读槽中对应到该标签。它可作为研究概念示例，不能因为Motion需要就声称勇士已有该条。

## 5. 球员四有序PlayTypes与Initiator

当前46人和历史47人分别列于JSON；以下仅当前内存观测，姓名按易读顺序显示，JSON保留原生姓/名短串顺序。字段原值不是球员能力评价，Initiator=false也不是证明该人绝不能被原版AI持球使用。

| 当前球员 | 有序四槽 raw | Initiator |
|---|---|---|
| Stephen Curry | 14,13,1,12 | true |
| Klay Thompson | 14,11,12,13 | false |
| Draymond Green | 8,6,7,11 | false |
| Zach LaVine | 4,1,13,14 | true |
| DeMar DeRozan | 4,13,10,1 | false |
| Jimmy Butler | 6,1,11,10 | false |
| Bam Adebayo | 11,7,1,8 | false |

项目静态目录：0 None；1 Isolation；2 Isolation Point；3 Isolation Wing；4 P&R Ball Handler；5 P&R Point；6 P&R Wing；7 P&R Roll Man；8 Post Up Low；9 Post Up High；10 Guard Post Up；11 Cutter；12 Handoff Receiver；13 Handoff Passer；14 Mid Range；15 3 PT。这是项目沿用原生目录的标签层，本轮没有重新做UI枚举验证。

匹配规则：只对**已认证逐战术类型**做球员有序type与本队可用类型交集；完整相关元数据且交集为空才能STATIC_PLAY_TYPE_UNSERVED。当前只有名称/CRC，不满足该前提，所以46人全部TYPE_UNKNOWN；不从Curry没有15就宣布勇士无球三分失效，不把DeRozan的Initiator直接改true，不从Bam没有13就提出未经批准的改值。四槽顺序不转换成平均调用概率。

## 6. 额外发现：真实同名书匹配阻断

当前教练PlaybookID分别为2/8/28，与Bulls/Heat/Warriors本队已加载书一致；原生book identity也可读。但`src/gm_state_io/team_book.py:team_book()`将书**完整规范化名称**与team.name、abbreviation、city+name相等比较，没有处理` Playbook`后缀。

因此三队实际运行该纯匹配函数都返回`TEAM_NAMED_BOOK_MISSING_OR_AMBIGUOUS`。本轮仅为研究按明确字面`team.name + ' Playbook'`查到唯一原生对象，报告当前教练ID相符；**不修改匹配器、不绕开M3/DEV14业务限制、不生成可执行意图**。M3安全投影捕获此ValueError后书状态会保持NOT_OBSERVED，这会影响真实标签下的own-book提案入口。

这是三队实际对象支持的具体缺口，不是对所有30队/所有路径的全量断言。建议下一次由玩家单独授权最小后缀匹配修正及直接相关检查；本轮不实施、不测试、不修Issue #6。现有源注册表和执行白名单能力不变，不能宣称该研究已经修复书操作。

## 7. 给B2的限范围建议

机读文件为十个SystemCard逐一保留角色要求、已有字段类别、相关核心动作、UNKNOWN和HOLD，不填B0的native_binding_refs，不改B1 Claim/GM可读覆盖。

1. 八原生体系、正常18 coach、Freelance、四type/Initiator、具名48倾向、PERSONAL18、训练/软轮换可按既有认证字段做**方向级**研究映射；十家族与八体系不是一一对应，不生成统一固定数值。
2. Motion只可提出射手/connector/cutter责任及已知字段方向；Triangle/Post保留入口与高低位未知；Spread PnR区分持球、顺下、外弹及第二处理，不能凭FIST名称签发类型覆盖。
3. Creator-Midrange维持创造权与中投价值的篮球意图，先受B1历史可读边界约束，不能用未来DeRozan结果填当前判断；Point-Center保留hub职责，不假装有专属原生开关。
4. Transition不能解释Tempo raw为每回合秒数；护框/换防只走具体PERSONAL字段方向，OVERALL继续只读；Adaptive只是玩家触发的赛前有限方案，不是实时ACE改写。Scram/peel没有认证专用控制，UNSUPPORTED。
5. 书槽方向需要先解决实际业务匹配，再依赖新同批合规源/认证类型/具体批准。本研究CRC和旧库不能当作后续正式批次的执行许可或Desired载荷。类型未知时局部HOLD，**不阻断B3历史seed或其它已认证字段的B2工作**。
6. 普通GM来源仍须`require_gm_sanitized()`；Intangibles不当能力，OVERALL/自由PlaybookID/51匿名倾向/Ability/Potential/Badge边界不变。未启动B2–B6或DEV24，V3有效、V4未启用、真实30队UNASSESSED。

## 8. 下一次任务才处理的三个文字问题

不需要截图、比赛或玩家预先停在某页面；如果菜单没有对应项/分配栏，说明没有即可。

1. 勇士本队编辑战术/分配菜单中，`FLOPPY`或`QUICK 32 HORNS`显示的PlayType是什么？若菜单显示指定球员/位置，抄一项完整分配；若没有分配栏，说明没有。
2. 公牛本队战术中，选一项实际看到的单打/中距离/面框战术，抄完整名称、PlayType和菜单显示的球员/位置（如有）；不要沿用旧合成候选名。
3. 热火`GIVE 51 FLIP 12`或`GIVE 52 RUB`显示什么PlayType？是否显示Bam/Butler或位置分配？若没有条目/分配栏，照实说明。

任何后续文字都先记PLAYER_REPORTED_UI，不能提升成内存认证，更不能当IN_GAME_EXECUTION_OBSERVED。本任务没有交互提问、后台监听或等待检查点；玩家以后以新任务处理回答。

## 9. 交付审计

| DEV23要求 | 本次权威证据 / 结论 |
|---|---|
| 从最新main独立调查、读取任务/契约/十卡/M3/DEV14 | base main与E01/E02/E07/E08；独立DEV23分支 |
| 每个有效槽的标识/名称/类型/批次/书身份 | JSON books逐项204槽；37非零名UNKNOWN，全部native type UNKNOWN |
| 球员四有序type、Initiator和静态匹配 | JSON players/archived_players；46当前+47历史独立来源，TYPE_UNKNOWN |
| 可行的只读进程调查 | E04原生布局/对象与受限模块字符串读取；管理员脚本已退出，句柄已关闭 |
| 名称、类型、角色、证据层与fallback | 111条play_semantics完整记录；9组core_action_research；无假受益人 |
| 至少三哲学与PnR/Post/Elbow/late-clock | 本文第4节与核心清单，明确本队候选/不足/HOLD |
| 十家族B2建议与准确限制 | JSON ten_family_B2_recommendations与本文第7节；未实现B2 |
| 机读、Markdown、问题和任务终结 | 本文+JSON，三个文字问题；PARTIAL_TASK_CLOSED |
| 不写、不采、不比赛、不扩展测试 | 只读研究/确定性提取；没有运行自动测试、旧测试、正式采集、UI、保存/重启或数据发布 |

**本次研究提取和证据审阅不是测试通过声明。** 独立Draft PR只交付研究文件及基线索引，不自动合并。所有未完成的逐战术类型/分配和比赛行为均保留未知；该部分交付状态不冒充完整语义认证。
