# 私有 GitHub 数据发布与网页 GM

目标仓库：`chris2gao/nba2k22-gm-engine`，要求 private。仓库保存项目代码、清洁模板、规范和小型 JSON 阅读文件；审计通过的 SQLite 备份打包为私有 GitHub Release 附件。当前 live 文件、运行时地址缓存、诊断日志、临时文件和凭据文件不进入 Git。

分工以 [文档 26](26_GAMEPLAY_ROLES_AND_WORLDLINE_RULES.md) 为准：网页连接授权/读取测试由玩家完成；Codex 验收本地来源、项目上传与远端数据库内容，不继续代测网页账号。网页 GM 先读取当前规则 commit 下的文档 26 和 `config/gameplay_policy.json`，再读取固定数据 commit 的批次；分别记录规则版本与事实版本，避免旧数据 commit 附带的旧提示词覆盖新规则。

## 三层产物

1. 本地 SQLite：采集事实的主数据源。写入由确定性脚本完成，GM 不直接读取游戏内存。
2. SQLite ZIP：可复现归档，内含 SQLite 一致性备份、原始入库清单、审计、上下文。ZIP 有 SHA-256，上传后重新下载校验。其原始模型 BLOB 是本局数据证据，不可用于新进程写回。
3. GitHub JSON：面向网页读取，严格从审计数据库导出，按球队/选秀年拆分，不包含 raw BLOB、运行时指针或本机绝对路径。JSON 是派生阅读面，不能取代 SQLite 的真实性检查。

私有链接本身不会授予网页 GPT 访问权。网页侧要有能够读取该仓库文件的已授权连接；连接/角色可用性和外部服务授权是独立条件。官方说明：[OpenAI 插件与连接权限](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)。此项目不假设网页连接会直接查询 SQLite，也不假设搜索索引立即刷新。

GitHub Contents API 可按 commit/branch/tag 的 ref 读取文件，私有仓库要求相应 Contents 读取权限：[GitHub Contents API](https://docs.github.com/en/rest/repos/contents)。大二进制文件的版本存储与小文本阅读用途不同，数据库归档放 Release，避免每次把整份变化的 SQLite 塞进 Git 历史；参见 [GitHub 仓库限制](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)。

## 阅读目录

```text
web_gm/START_HERE.md
web_gm/GM_INSTRUCTIONS.md
published/index.json
published/saves/<career_id>/latest.json
published/saves/<career_id>/batches/<batch_id>/
  manifest.json
  SUMMARY.md
  source_coverage.json
  audit.json
  league.json
  calculations.json
  changes.json
  staff.json
  teams/IND.json ... 30 队
  player_catalog/index.json
  player_catalog/name_index.json
  player_catalog/<选秀年>_<分片>.json
```

每个阅读文件小于 900 KB。需要某队时只读取该队及交易对手；查历史新秀先查姓名/年份索引，再读对应分片，不将 3,319 个模型全部塞入对话。

## 发布门槛

`src/export_web_gm.py` 检查审计、SQLite 快照摘要、球员池文件哈希和玩家上下文。先构建完整不可变批次、校验文件哈希，再更新本地 latest。每个文件有 SHA-256 和字节数；Git 禁止对 published 文件转换换行，以保持远端字节与清单相同。

`scripts/verify_web_export.py` 独立逐项比较所有导出球队、阵容、员工观测、全局模型字段和历史新秀分类，重算 financial proxy，并打开 ZIP 中的 SQLite 验证备份。NULL 原样保留。这里的财务差额只是静态工资规则代理，不是完整 CBA 可用空间。

`scripts/publish_web_snapshot.py` 要求配置仓库确实私有、origin/branch 正确、没有混入其他待提交文件，以正常提交和正常 push 发布 JSON，再上传对应 SQLite ZIP 到私有 Release。随后读取固定 commit 的远端 latest/manifest，并下载归档复核哈希，最后写本地 `_exports/receipts/` 回执。推送和创建 Release 是两步远端操作；只有两者验证成功才报告整体发布成功。

发布脚本不修改凭据，不 force push，不执行网页模型提交的脚本或游戏决策。源代码版本更新与数据更新独立提交。

## 网页 GM 每次的必读协议

先读取 `web_gm/START_HERE.md` 和 `GM_INSTRUCTIONS.md`。将玩家这次提供的发布回执作为预期版本：核对 career_id、游戏日期、batch_id、commit SHA；从该固定 commit 获取 latest/manifest，并且所有后续文件都读取同一 commit 与 batch。搜索结果中的旧快照不能自动当作最新。

若连接不能按版本读到预期文件，必须说明当前读到的版本或无法读取，停止用旧数据冒充最新。数据导出成功、GitHub 上传成功、用户网页 GPT 连接读取成功是三个分别验收的环节；前两者不能代替第三者。

网页 GM 可基于已观测事实制定建队、角色、训练和策略建议；战绩、伤病或选秀权未知时明确写“未观测”。需要新数值时用 Python/数据分析工具基于已读取文件计算；没有执行工具时输出 calculation_request 交给本地计算，不能用模型心算替代。

历史线、现实线、玩家自定义世界线分别标注来源和有效日期。真实 NBA 资料只作为参考，不自动覆盖本局名单、战绩、合同或已批准的历史分支。

## 决策返回与审批

所有方案标为 PROPOSED，至少包含 decision_id、career_id、source_batch_id、source_commit、引用文件/字段、预期效果、计算结果引用、需要补齐的数据。玩家批准的必须是明确方案版本。未取得批准不能修改游戏、正式球队决策档案或执行脚本；提交一个写着 approved=true 的网页模型文件不构成人类批准。

远端 proposals 自动取回/校验/执行接口尚未实现。当前网页 GM 的方案由玩家带回本地，核对数据版本并批准后再交给受控执行入口。后续可补结构化执行回执和执行后重新采集验证，但不能把当前导出器描述为已打通自动游戏写回。

## 当前玩家确认的日期

当前 career_id：`mc_haliburton_2021`。2021-2022 赛季，游戏日期 2021-11-20，当日比赛已结束，来源为玩家确认；这是检查点而非月末。当前捕获能力不包括逐场比赛结果，因此“当日比赛结束”的上下文不能被解释成已经获得全部比赛技术统计。
