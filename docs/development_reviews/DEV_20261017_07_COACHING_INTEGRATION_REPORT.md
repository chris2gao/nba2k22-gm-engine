# DEV-20261017-07 教练 V2 集成报告

状态：`PARTIAL_BLOCKED`。开发分支 `codex/coaching-tactics-v1`，交付至现有 PR#1；未部署 main，不自动合并。V2 的 A–E 范围保持不变，不能把下面的分项通过写成完整机制已完成。

本报告对应实施源码提交：`8473d7f9c1687135694443d39ddbd719f8fce2c3`。报告/索引补充提交可能在其后；该SHA用于定位本次证据，不作为新任务的固定HEAD。

## 当前验收结论

| 模块 | 已完成 | 剩余限制 |
| --- | --- | --- |
| A：19 项默认教练设置 | 19项读取合同；18项支持提案/受控执行。六POE、五数值设置、双体系和命名手册14项有实机写回证据；四Freelance使用34种完整原生枚举、已验证布局和有序codec | Tempo80尚未对应当前UI，保持只读。四Freelance未直接查看本局比赛内页面，不冒充UI或持久性测试。玩家要求撤销9–10测试白名单，BenchDepth由GM按实际阵容选人数，仅保留原生整数格式保护，不猜完整UI端点 |
| B：指定对手整体防守 | PHI→IND UI差分、程序同范围操作、用户菜单确认、恢复；18原生字段合法值及8字节掩码，整体组身份保护 | 直接配对的中文为持球压迫AUTO/GAP；其他字段保留原生英文，不猜翻译；不承诺模拟效果 |
| C：1–30队批次 | 整批RO预验、RW前再次预验、外部精确批准、持久preimage/lock、共享块masked写、逆序条件恢复；30队离线与两类对象隔离实机通过 | 软件事务不是物理同时生效；缓存回执不证明当前值，第三方修改转人工审阅 |
| D：正常采集与发布接入 | 原RO采集handle→snapshot-scoped SQLite→源审计→既有导出器33个轻量文件；临时库和导出器守卫测试通过 | 未跑真实全量生产入口或GitHub数据发布，未部署main；不能把本地开发快照补入旧包 |
| E：两份操作手册 | GM手册、执行手册40、32/33/34/36、28、39历史提示、源注册表、SOP和角色索引已同步 | 当前门槛随剩余A/D验收继续维护 |

## 实机证据

- [整体防守证据](DEV_20261017_07_OVERALL_DEFENSE_EVIDENCE.json)：整体页面没有额外All选择。UI把所选字段批量写入该对手14条有效matchup，空槽不写；保留各player/defender ID，不提供逐球员接口。退出UI观察到IsInUse从0到1，不能将0解释为禁用。
- [五数值证据](DEV_20261017_07_SLIDER_EVIDENCE.json)：PHI协防50→51、执行战术70→71、联防1→2、替补使用40→41、板凳深度9→10，用户确认五项一致；事务恢复后30队教练及manager原始块完全一致。板凳深度是轮换人数上限；其余四项倾向0–100、步长1。
- [混合批次证据](DEV_20261017_07_MIXED_BATCH_EVIDENCE.json)：PreferredSystem1→5、ActiveSystem4→3、Playbook0→动态加载的Bucks1在同一4字节块合并写；另一个对象为PHIvsIND持球压迫0→1、14个有效块，共15次写入。用户确认当前体系“主打内线→主打外线”、手册“76人→雄鹿”。PreferredSystem原生枚举/独立位域/回读通过，未单独看到其UI；用户停止同类重复菜单验证。15块按日志条件恢复，所有捕获块一致。交付前代码审查又补齐了显式rollback的逆序，与失败自动恢复保持一致；提交标记恢复顺序由离线测试覆盖，未重复实机测试。

上述仅用于玩家确认的新开终极联盟隔离测试存档，没有正式存档修改、日期推进、比赛模拟、保存/重启复测。此前六POE持久性证据仍按DEV06原报告，不扩张成本次其他字段的落盘证明。

## 实现与来源边界

纯编码位于`coach_codec.py`、`defense_codec.py`、`coaching_overall.py`；GM纯离线合同位于`gm_core/coaching_batch.py`。执行器为`coaching_batch_executor.py`，当前对象解析为`coaching_targets.py`，CLI为`scripts/coaching_batch.py`。原单动作CLI继续兼容默认范围，旧`VS_OPPONENT`预设不执行，新整体作用域是`VS_OPPONENT_DEFENSE`。

`coaching_source.py`冻结采集时profile，旧批次不受较新readiness追认。写入允许范围只限制目标，不能用开发期窄范围过滤真实原生观测或否认原值。五项Sim在GM提案/编码处一律禁用。旧TEAM策略语义/setter保持撤销。

## 验证命令与结果

从开发工作树运行，全部为离线测试或帮助命令，不连接游戏，不发布数据：

```powershell
python -m unittest discover -s tests -p 'test_coaching*.py' -q
python -m unittest discover -s tests -p 'test_gm*.py' -q
python scripts/coaching_snapshot.py --help
python scripts/coaching_validate.py --help
python scripts/coaching_execute.py --help
python scripts/coaching_batch.py --help
```

结果：74项教练测试、40项GM测试通过；4个帮助入口通过。修正了两处旧测试假设：TEAM旧枚举不再允许；当前已发布批次已有赛季统计，不能继续断言所有球队生命周期均不可评估。生命周期实现及正式决策文件没有改动。

## 后续入口

后续工程补充：顺序脚本执行保持不变，两个执行器增加跨state-root的共享进程锁，未完整恢复或最终journal未落盘时保留锁供人工审阅；新增7项离线覆盖。四个已确认百分比字段增加独立观测范围检查，非法101不能发布；BenchDepth的9–10人为白名单已按玩家明确要求撤销，真实11可以观察、GM也可以选择11、12等人数。四Freelance不再因没做重复菜单检查而禁用，其完整原生枚举/布局和有序codec已核对；未追加实机UI声明。新增2项来源与2项批次合同覆盖。当前教练测试85项、GM40项均通过，没有新增实机测试、采集或数据发布。历史8473d7f的实机证据仍按原记录，不将新能力称为当时已实机验证。

剩余实质缺口是Tempo真实UI/业务映射，以及玩家另行触发真实正常采集/发布后的D验收。玩家已要求停止重复菜单和保存重启测试，并撤销测试样本白名单；Freelance按已核对的原生编号保存顺序，板凳深度由GM基于阵容选人数，不把未知UI端点变成人为上限。不能因此捏造缺失证据，也不能偷偷启动全量采集。本任务目标保持19项及A–E，当前不宣称完整完成。
