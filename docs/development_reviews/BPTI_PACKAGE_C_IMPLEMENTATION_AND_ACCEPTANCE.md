# BPTI工作包C — B4/B5/B6实现与最小验收

日期2026-10-20。状态：BPTI_PACKAGE_C_COMPLETE_TASK_CLOSED。独立分支codex/bpti-package-c，交付Draft PR，未批准自动合并。

## 前置条件与范围

玩家批准PR #11合并后，main为04b194ab8b4644161242391e964051d3d9f9520a；本地main和origin/main已同步。包C单独从该主线启动，复用托管工作树；原E盘codex/season-match-history保留。权威范围为DEV22/DEV26/R4的B4→B5→B6，不包含DEV24、GM V4激活或实际30队经营。

仓库命令与五项检查在ADMIN=True的独立隐藏PowerShell执行。未打开游戏进程/活动数据库、未运行生产采集/游戏数据发布/存档推进/写入。

## 实际交付

- B4：gm_core/bpti_decision.py消费B0蓝图、B1/B2/B3日期过滤知识及M3密封DTO。当前技能角色、why_this_basketball、第一优势/反制/第二答案/自主权、身份与阵容/成本冲突进入真实D1–D6及原HOLD/INTERNAL/MARKET方案。内部动作须匹配支持候选；来源/知识/方向不明为HOLD，市场继续使用原M3缺口/内部比较。没有收益计算器或姓名巅峰规则。
- B5：gm_core/bpti_evolution.py实现六级候选演化记录、当前证据、前态体系/文化、保留与改变原因、教练适配、逆转条件。前态由CLI解析已有同career/同队不可变记录。文化延续优先，重构需长期和管理层语境；没有教练市场执行器或实际换帅。
- 现有decision_protocol与gm_decision新增submit-blueprint/record-evolution，复用decision_artifacts、run CAS、有界artifact/history和原导出。候选final/strategy带BPTI派生材料；不会自动保存正式M2状态或产生玩家批准。蓝图换版阻断旧评审/备选定稿。
- 选中动作仍走现有M3/DEV14纯规划，得到NOT_GRANTED的intent/approval tuple；不创建另一套数据库、市场、审批或内存执行器。更新AGENTS、33/34/36及GM手册索引。没有新原生能力或游戏来源，source_catalog/字段registry/执行白名单无需变动。

## 五项检查及结果

命令：python -B tests/test_bpti_package_c.py。最终 **Ran 5 tests in 17.700s — OK**。只引用旧测试模块的合成夹具，不运行其测试类或旧套件。

| 检查 | 实际覆盖 | 结果 |
|---|---|---|
| C-C1 | GSW Motion、CHI Creator/Midrange、MIA Defense-first三种合成体系有不同理由、角色和第二答案；可用知识裁剪；真实评估仍UNASSESSED | PASS |
| C-C2 | 真实M3 apply/store路径保存蓝图、D1–D6评审和三类备选；角色优先/机会成本、原市场内部比较门槛；蓝图换版后旧方案拒绝；历史版本保留，正式策略表无新增评定 | PASS |
| C-C3 | 合成历史姓名球星位于不同队，角色按该源可见技能；姓名不能替代技能；演化沿已有工作台追加并保留前态系统/文化，教练适配候选不自动重写文化，单月文化重构被拒 | PASS |
| C-C4 | 批次不符、RAW角色、早于历史证据、Tempo篮球方向未知均HOLD；实际CLI缺失源返回HOLD；不生成胜率/箱分预测 | PASS |
| C-C5 | 复用真实DEV14纯规划生成OFFLINE_PREPARED、未批准intent；合成源未变；Potential/OVERALL/Badge/unknown51/自由PlaybookID/无匹配槽动作不开放；伪批准与陈旧CAS拒绝，V4未启用、无真实30队评定 | PASS |

### 失败与直接修正记录

首次五项未通过（16.648s）：合成蓝图漏填B0必填status，返回HOLD。补齐后直接重跑五项（16.234s），暴露合成动作误用NATIVE_STATE（原M3契约为COACH_DEFAULT）及CLI测试导入路径遗漏。修正动作类型和导入路径时，一次进程在测试前因scripts/gm_state_io.py遮蔽包而退出；改为保留src优先级。最终五项通过。

另执行一次只读根因诊断，输出各蓝图的hold_reasons（BPTI_EXACT_OBJECT_CONTRACT_REQUIRED），不新增验收用例。没有已通过项目后的追加回归、性能/比赛效果测试、复跑旧套件或真实GM决策。各失败均保留临时管理员任务日志；修复直接对应已授权五项范围，未绕过保护。

## 交付限制

这是本地合成工程验收，不能声称真实生产GM消费、真实换帅/交易/签约、AI调用效果、赛场效果、存盘或游戏事实发布已验证。历史知识可读不等于本档阵容适配；当前缺失的精确CRC类型/受益人/ACE/调用频率/Tempo含义与比赛因果仍UNKNOWN。B4当前不从未知类型生成装载承诺，不改变底层既有同批全目录CRC、本队书及单独TEAM_BOOK_REBIND规则。

仍沿既有gm_core纯DTO、M3市场/M1财务、DEV14身份/字节校验/CAS/批准元组执行边界；Potential遮蔽不是球探能力，Intangibles只为既有软轮换例外，OVERALL只读。V3有效、GM_V4_NOT_ENABLED、实际30队UNASSESSED。源码分支/Draft发布与游戏数据-Publish分开。交付结束，不启动DEV24或后续任务。
