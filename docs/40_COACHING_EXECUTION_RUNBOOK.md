# 教练批量执行操作规程

DEV07 V2 开发中的真实 CLI 规程。源码尚未部署 main；19项默认字段中18项支持提案/受控执行：六POE、五数值设置、双体系及命名手册14项有实机写回证据，四Freelance依据完整原生枚举/布局与有序codec放行，未冒充实机UI验收。Tempo尚未对应UI，保持只读。BenchDepth是轮换人数上限，GM依据实际阵容选人数，不受9–10测试样本限制；其他四个已确认百分比字段为0–100。指定对手整体防守及默认/整体两对象混合批次已完成隔离局写入/条件恢复验证。正式存档不在开发测试范围。核对 `docs/34_BASELINE_CURRENT_STATE.md`、最新V2字段矩阵和profile，不从历史聊天推定能力。玩家已停止同类重复菜单/保存重启测试，不能编造未看见的UI或持久性结果。

## 输入与来源

主入口 `scripts/coaching_batch.py`；不带执行开关时完全离线，不打开游戏句柄。`--snapshot` 可读同批发布的 `coaching/teams.json`，对手动作按需重复传 `--opponent-source coaching/opponents/<TEAM>.json`。每个文件的 career/batch/date/data_updated_at 必须一致，一个 owner 文件必须恰有其他 29 队，禁止重复挂接或对自己。

执行模型按玩家要求顺序调用脚本，一个批准批次结束后再处理下一个。不安排多个教练执行脚本并发操作游戏。

也可使用隔离开发只读快照，但必须明确 `environment=ISOLATED_TEST`、存档确为隔离副本，并单独传 `--test-save-confirmed`。不要把开发快照补进正式发布包。正式动作必须来自本局最新可信同批来源；PID/创建时间绑定不符则重新采集，不用旧绝对地址。

## 离线生成与审阅

将 GM 的具体请求保存为 `_exports/coaching/requests.json`。路径示例中的 `<career>/<batch>` 必须换成玩家选中的实际来源；以下命令不代替玩家的执行批准。

```powershell
python -B scripts/coaching_batch.py --snapshot published/saves/<career>/batches/<batch>/coaching/teams.json --opponent-source published/saves/<career>/batches/<batch>/coaching/opponents/PHI.json --requests _exports/coaching/requests.json --batch-id COACH_BATCH_001 --decision-id COACH_DECISION_001 --version 1 --proposal-output _exports/coaching/batch.json --output _exports/coaching/dry_run.json
```

离线结果含 prepared_actions、blocked_action_ids 和 batch_digest。审阅每队 HOLD/APPLIED 目标、旧/新值、scope、对手、coach identity、整体组身份及所有共享块。只有实际 `production_enabled` 白名单可以正式执行；JSON 自填 approved=true 会被拒绝。缺失日期的开发来源不能用于正式提案。

## 只读预校验与逐批批准

```powershell
python -B scripts/coaching_batch.py --snapshot <same-snapshot> --opponent-source <same-owner-file> --batch _exports/coaching/batch.json --preflight --output _exports/coaching/preflight.json
```

`--preflight` 只打开 RO 句柄，校验全部目标，任何对象、旧整块、主教练、阵容、动态 Playbook 目录或原生布局变化就失败。此命令不自动启动采集或修改菜单。未就绪字段会在取得游戏句柄前被正式门槛拒绝。

玩家批准必须具体绑定 career_id、batch_id、decision_id、version、完整 action_ids 集合和离线输出 digest；部分批准不能套用到原整批。要求玩家退出 Coach Gameplan 编辑页，停在日历或主界面。`--coach-editor-closed` 是操作者根据玩家确认作出的声明，脚本不能自动看见菜单；打开编辑页的缓存可能覆盖内存写入。

## 执行与回执

```powershell
python -B scripts/coaching_batch.py --snapshot <same-snapshot> --opponent-source <same-owner-file> --batch _exports/coaching/batch.json --execute --approve-career-id <approved-career> --approve-batch-id COACH_BATCH_001 --approve-decision-id COACH_DECISION_001 --approve-version 1 --approve-action-id PHI_DEFAULT_TEMPO --approve-action-id PHI_VS_IND_PRESSURE --approve-plan-digest <approved-digest> --coach-editor-closed --state-root _exports/coaching/execution --output _exports/coaching/receipt.json
```

隔离局技术验收额外加 `--test-save-confirmed`；正式局不能通过伪造环境跳过字段验收。输出和 state-root 必须在本仓库 `_exports` 下，不提交这些本地文件。

除各自事务锁外，单动作与批次执行器在任何游戏句柄之前取得同一份进程绑定锁。它位于当前执行账户的 `tempfile.gettempdir()/Antigravity_GM_Engine/coaching_execution_locks_v1/<process_binding>.lock`，不随 state-root 或仓库工作树改变；更换career标签也不能让同一进程同时被两个入口操作。它只是误开窗口的防护，不改变顺序执行方式。锁仅存本地元数据和对应journal路径，不进入Git。

先 RO 校验全批，RO 关闭后才取得 RW，再重新校验全批。全部目标 preimage 持久化并 fsync 后才首写。共享块合并 mask，保护未知位；整体动作必定覆盖认证组全部有效记录并保留 player/defender IDs，空槽不写，提交标记最后处理。每块读回，结束再读全批。运行失效或并发变化会停止并按逆序条件恢复。

这是软件事务，不是跨 30 队的物理瞬时原子操作。成功为 `COMMITTED_VERIFIED_IN_MEMORY`，只证明内存，不代表游戏存档已保存。全 HOLD 批次返回 `NO_WRITE_NEEDED`，零游戏句柄。重复已完成事务只返回缓存回执，并标 `NOT_REVALIDATED_CACHED_RECEIPT`；不能把缓存回执当成当前游戏仍保持目标值的证明。

## 恢复与异常

恢复使用同一 batch、snapshot、state-root、完整批准元组，执行命令把 `--execute` 换成 `--rollback`。同样先关闭编辑页，并先 RO 校验整批当前值仍等于已批准的目标块。成功为 `ROLLED_BACK_VERIFIED_IN_MEMORY`。

失败期间只在当前块仍等于本事务刚写值时恢复旧值，避免覆盖第三方修改。`FAILED_ROLLED_BACK_TO_OPERATION_PREIMAGE` 表示此次操作已经条件恢复；`PARTIAL_UNRECOVERED_MANUAL_REVIEW` 表示仍有不确定块，停止后续写入并检查 journal，不能宣称全批恢复。锁文件提示崩溃或并发时不自动删除锁或强行重跑，先读取对应日志和当前状态。

共享锁只有在首写前失败，或已持久保存成功/完整恢复的最终journal后才释放。部分恢复、首写后的进程崩溃、最终journal写盘失败都会留下共享锁，阻止从别的state-root再次执行。根据锁内 `journal_path_local_only` 定位日志，人工核对当前进程、所有未恢复块和处理决定后，由具体获批的执行窗口处理；不提供自动解锁或强制重跑参数。日志目录仍须沿用，不用更换目录规避历史回执。

换帅、换局、换进程、原生布局变化、动态手册目录变化或任一旧块漂移，都要求重新取得来源和提案。不得用强制选项绕过检查。源代码和配置哈希记录在本地 journal 便于审查，不作为网页 JSON 同步契约。

## 保存、采集和发布各自触发

执行完成后停止游戏写入。玩家自行保存；玩家另行触发数据更新时，正常 `scripts/run_data_update.ps1` 才在原来的只读采集会话捕获教练来源，写入 snapshot-scoped SQLite、审计、导出轻量文件，`-Publish` 才使用已有发布器同步 GitHub。不带 `-Publish` 只本地导出。开发窗口不能为证明本功能自动运行全量采集或发布。

该来源接入代码在当前开发分支；端到端来源/发布验收尚未完成，也未部署 main。缺队、非法值、身份歧义或审计缺失必须拒绝新包并保留 last-good/latest。历史批次没有教练来源时保持缺失，不回填新观察。
