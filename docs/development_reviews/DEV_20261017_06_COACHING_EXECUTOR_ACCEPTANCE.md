# DEV06 执行器验收记录与剩余门槛

2026-10-17。结论：**工程及两队内存事务已验证；正式执行验收未通过，production 全部禁用。**

| 要求 | 本次证据 | 结论 |
| --- | --- | --- |
| 旧 TEAM writer 及调用者 | setter 先拒绝；bootstrap 票价 helper；AST 扫描 src 无 setter 调用 | PASS |
| 六项5bit与所有合法枚举 | codec 子测试逐合法/非法值；完整块比较；bit30/31保护 | PASS |
| 同块多项只写一次 | 假内存与真实单项事务日志；codec 合并生成1个4byte块 | PASS（实机多字段合块尚未另测） |
| 原生字段/enum/模块 | 当前 metadata CRC、类型尺寸、getter 指令、PE 证据，逐次校准 | PASS 当前进程 |
| 球队/主教练/岗位/名单 | 当前30队双向引用；重复、错岗位、非下标 ID 的 mock 拒绝 | PASS 当前进程；真实换帅/跨存档场景未实操 |
| 无批准不得 RW | 默认 dry-run/非法提案零handle；前值/PID/身份失效仅 RO，无RW | PASS mock |
| 两队实机写/回读/恢复 | IND/GS POEOffense 5→2→5；幂等；全部30教练字节恢复、战术本未变 | PASS 内存层 |
| 并发/失败恢复 | 当前值不等于本执行目标不覆盖；故障、回读差异、条件恢复、日志先落盘 | PASS mock |
| 菜单可见与重开 | 截图组件对游戏及Explorer均超时 | NOT_VERIFIED |
| 保存退出重进 | 未做；没有替玩家保存错误状态 | NOT_VERIFIED |
| 实际进程重启重定位 | 新PID实际验证未做；模拟 PID变化拒绝已测 | NOT_VERIFIED |
| Sim/体系/手册/滑块 | 原生只读及 codec；无独立实机写入认证 | READ_ONLY / SAFE_WRITE_PENDING |
| 对手Gameplan启用 | 870条全0；读/排序/预设；明确拒绝setter/IsInUse | BLOCKED_NOT_ACTIVATED |
| 18防守与轮换 | 原生掩码、enum CRC 和capture-local引用只读 | READ_ONLY |
| 正式源集成/多球队原子批次 | 独立本地JSON；一次一个action；未实现生产入库/发布或跨队事务 | NOT_IMPLEMENTED |
| 比赛效果 | 未模拟/推进；等待玩家正常月份与后续触发 | SIM_EFFECT_PENDING_PLAYER_MONTH |

命令：

```powershell
python -B -m unittest discover -s tests -p test_coaching_safety.py -v
python -B -m unittest discover -s tests -p test_gm_decision_protocol.py -v
python -B -m unittest discover -s tests -p test_gm_coverage.py -v
python -B scripts/coaching_snapshot.py --help
python -B scripts/coaching_validate.py --help
python -B scripts/coaching_execute.py --help
```

本轮新安全套件35项、协议8项、覆盖5项。第一次新增 GM 包装测试因 fixture 使用 Txx 合成球队而错误写成 IND 失败，修正为对应 T20 后通过；未降低身份校验门槛。最终命令/帮助及无句柄预演结果由本地验证输出保留。没有运行 verify_web_export、同步 hash/下载比较或比赛模拟。

## 恢复验收的明确流程

1. 玩家确认并载入隔离副本；记录其名称、赛季、日期（日期未知只用于测试）。正式存档不能用于这一验证。恢复能返回图像的控制组件后，打开玩家指定“终极联盟 → 执教 → 教练比赛计划”。
2. 读取新快照，辨认球队、教练和当前“默认/全部对手/指定对手”作用域；确认当前对象确为默认 COACHDATA 字段对应 UI，不猜对手 IsInUse。
3. 对一队以独立 action 最小改变一个合法POE：回读完整块、重开菜单看值，保存该测试副本并退出重进，再读回值；恢复原值、保存并确认。第二队重复。
4. 实际重启游戏进程，重新校准、读新快照，验证新进程定位；旧快照/方案必须报失效。需要变更时重新形成版本并明确批准，不复用旧地址或悄悄更新已批计划。
5. 仅按具体完成字段调整 profile/readiness。内存成功但菜单/保存不接受标 WRITE_NOT_ACCEPTED_OR_NOT_PERSISTENT；缺证据保持禁用。不能把仅验证 POEOffense 扩大为其他 POE/Sim/体系/手册均验收。
6. 对手启用、防守/轮换是独立验收项目，未验证不解锁。效果评估由玩家一个月之后按来源批次/已执行回执关联进行；不因技术验收宣称提高胜率。
