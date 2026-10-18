# DEV-20261017-07 批次执行验收

状态：`BATCH_TECHNICAL_ACCEPTANCE_PASSED / OVERALL_GOAL_PARTIAL_BLOCKED`。正常正式批次仍逐字段受profile门槛约束、逐批需要玩家批准；工程测试授权不是正式游戏战术许可。

实施源码提交：`8473d7f9c1687135694443d39ddbd719f8fce2c3`。逆序显式恢复的最后补充检查仍为17项批次测试通过，未再安排实机写入。

## 受控合同

`COACHING_BATCH_CHANGE`绑定career/source_batch/game_season/game_date/policy/snapshot和batch_id/decision_id/version。1–30个参与球队可为HOLD、COACH_DEFAULT或VS_OPPONENT_DEFENSE，唯一键为team+scope+opponent。HOLD队不能同时改值，重复动作ID/作用域拒绝，JSON自填授权拒绝。

外部批准必须完整匹配career/batch/decision/version/action_ids/digest。无批准、编辑页未退出、正式字段未就绪时零进程句柄；纯离线inspect及全HOLD同样零句柄。`--coach-editor-closed`是玩家操作确认，不是UI自动检测。

先RO校验整批，最后一个目标失效也不得取得RW。RW取得后再校验整批，全部preimage及代码来源写日志并fsync后首写。掩码合并保护共享位；指定对手操作只接受认证的整体组全部有效块，不能由来源文件指定任意地址或单个球员。提交标记最后写。

每块写前重验、写后回读、末尾全批回读。失败按逆序且仅在当前块仍等于本事务写值时恢复，第三方变化保留并转人工审计。换进程、换帅、换名单、同批前值变化及手册目录变化均拒绝旧方案。

## 离线失败注入

`python -m unittest discover -s tests -p 'test_coaching_batch.py' -q`：17项通过，包括：

- 30队最后目标漂移导致零RW/零写；修复合成数据后30块提交及逆序恢复完整。
- 缺批准/缺编辑页确认/批准动作不完整；重复作用域、HOLD冲突、Sim禁用。
- 默认块与整体组混合提交；第二对象失败恢复第一对象；第三方改值不盲目覆盖。
- 认证组子集或伪造offset拒绝；UI提交标记最后写，恢复时逆序处理。
- 重复事务只返回历史缓存，显式`NOT_REVALIDATED_CACHED_RECEIPT`；不假称重新核对当前游戏。

另有原单动作/位域安全38项、整体模型4项等纳入教练总计74项，不需要逐一实机执行30队或全部870对手。

## 隔离局两对象最小验证

[混合证据](DEV_20261017_07_MIXED_BATCH_EVIDENCE.json)：PHI默认共享块（手册和两个体系）+PHIvsIND整体持球压迫14块，15块同批提交并回读。其他29教练、其他28对手、其他29manager没有变化。玩家确认手册和当前体系页面生效后退出，条件恢复15块，30队全部已捕获原始块与写前相同。

这一验证没有重做已通过的六POE、没有开比赛或推进日期。玩家明确停止其余同类UI验证，不要求再保存/重启。内存恢复不扩写为落盘恢复。

## 限制与操作

使用[执行手册40](../40_COACHING_EXECUTION_RUNBOOK.md)中的同一snapshot/batch/state-root进行执行和恢复，不更换目录重复执行同一批次。软件事务不提供物理同时写或无条件跨重启回滚。崩溃锁、不完整日志和`PARTIAL_UNRECOVERED_MANUAL_REVIEW`由执行角色联合人工审查，不能删除日志强行重试。
