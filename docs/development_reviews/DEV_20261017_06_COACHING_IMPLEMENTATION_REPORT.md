# DEV-20261017-06 教练战术实施报告

2026-10-17。**工程实现已交付，完整实机验收未完成；正式游戏写入保持禁用。** 这不是正式赛季战术执行回执。任务与 DEV05 线索均在当前代码/进程重新核对。

## 实际实现

1. 撤销 `TEAM+0xEB2` 等旧 setter，在任何内存访问前拒绝；bootstrap 不再调用旧策略模板；停用的 monthly_pipeline 中旧调用也已删除。球票入口和原批准门槛保留。历史原始字节保留，来源说明及 GM 消费端标 LEGACY_UNVERIFIED，不追认旧 batch。
2. 当前模块原生 getter → 活动名单目录 → 按实际 ID 匹配球队 → 主教练岗位双向核验。反射元数据逐项验证 24 项字段布局及 enum CRC 标签，验证 COACHDATA/GAMEPLAN/防守/战术本类型大小。无生产堆绝对地址、无固定 PID、无 84 本数量常量。
3. 纯 codec 合并共享块、严格 int/enum、保护非目标位；离线 TACTIC_CHANGE 提案与包装协议；默认 dry-run；外部具体批准、完整前值、持久 preimage、幂等、条件回滚、源码指纹和本地日志。gm_core 不导入游戏模块。
4. 五项 Sim、两项体系、已加载有名战术本选择具备编码；滑块/Freelance 只读。对手计划、18 防守字段及普通轮换只读，指定对手方案可 PROPOSED，写入被显式拒绝。高级轮换、共享战术本内容、临场状态机未开放。

细分状态见 [字段矩阵](DEV_20261017_06_COACHING_FIELD_MATRIX.json)，操作契约见 [文档39](../39_COACHING_TACTICS.md)。

## 当前进程证据

当前反射证据：COACHDATA 142 个字段、大小 0x160；防守结构 18 字段、大小8；GAMEPLAN 大小0x370；战术本大小0x168。PE 时间戳和映像大小见 [脱敏技术证据](DEV_20261017_06_COACHING_TECHNICAL_EVIDENCE.json)。本轮读到 30 位主教练、每队29对手共870条、84本战术本（82有名可选）；这些计数是本次样例，不是目录上限。所有870条 IsInUse=0。

旧采集校准器的固定 Jordan 槽位在当前自定义名单中已被替换，直接复用会拒绝定位。新教练模块改用当前原生 getter，并验证目录结束指针、完整球队集合、岗位与大名单归属；没有修改旧生产采集校准器或全量更新路径。加载表两个空名条目被保留观测并排除选择。

隔离局技术测试：步行者 Rick Carlisle 与勇士 Steve Kerr 的 POEOffense 均从原始5改为2；每队一次4byte共享块写入；完整回读通过；重复 action 返回 idempotent；同一事务条件回滚通过。之后逐字节比对30位教练完整0x160记录均恢复原样，加载战术本名称/ID/68 CRC槽均未变。仅证明内存技术事务，不证明菜单采用或保存持久性。

最后新增的命令/源码指纹日志及 Gameplan 独立 codec 经离线测试，最后只读复核仍成功读取30队/870记录并验证战术本 ID 原生掩码；没有为这些无写入行为的调整重复写游戏。原始快照、含运行时地址的事务及管理员工程工具只留 `_exports/coaching_development/`，不进入 Git。公开技术证据为确定性抽取的脱敏开发证据，不是正式比赛源发布。

## 验证及边界

- `python -B -m unittest discover -s tests -p test_coaching_safety.py -v`：35项通过，含所有枚举子测试、保留位、合块、两队隔离、岗位/owner、非法来源、无批准/RW门槛、幂等/恢复、旧入口和 GM 包装。
- 对既有 GM 提案协议和来源覆盖的回归分别为8项、5项；最终结果及 CLI 检查见验收文档。测试全为明确的 synthetic/mock，不运行正式30队 GM 会商。
- UI 捕获在 NBA2K22 与项目 Mods Explorer 对照窗口都超时；恢复窗口、窗口模式、重置控制会话均未恢复。可访问性仅有游戏标题。全局失败记录位于 `~/.codex/FAILURE_LOG.md`。
- 未完成：菜单逐项映射、保存退出重进、真实新 PID 重启验收、其余字段实机写入认证、多球队原子批次、生产 SQLite/发布源集成。模拟 PID 变化拒绝已测，不能替代实际重启。
- 所有 production_enabled=false，不能标 TEST_SAVE_WRITE_VERIFIED 或 EXECUTOR_IMPLEMENTED_READY_FOR_PLAYER_APPROVAL。当前 POEOffense 仅 LIVE_MEMORY_WRITE_VERIFIED_UI_AND_PERSISTENCE_PENDING；其余按矩阵只读/SAFE_WRITE_PENDING。

## 交付与继续条件

开发分支 `codex/coaching-tactics-v1` 来自 origin/main 的 DEV06 任务版本，在独立 worktree 中工作，没有夹带原工作区的交易/签约改动。代码上传不等于事实源发布；没有调用全量采集、模型、GM正式会议或比赛推进。

GitHub 提交 SHA / PR 由最终交付回执给出；本文件随其源码提交，不填造预先不存在的 SHA。完整目标仍等待 UI/保存/真实重启验收，不能因提交代码就宣布全任务完成。可在控制组件恢复后按验收文档续接，无需重做已验证原生调查。
