# 网页 GM 数据入口

项目使用私有仓库，需要先给你的 ChatGPT GitHub 文件读取连接授予本仓库访问权限。不能读取时直接报告，不猜数据。

1. 读当前项目版本的 `web_gm/GM_INSTRUCTIONS.md`、`docs/26_GAMEPLAY_ROLES_AND_WORLDLINE_RULES.md` 与 `config/gameplay_policy.json`，记录规则 commit 和 policy_id；数据 commit 可以较早，不能因此继续执行已废止的旧规则。
2. 读 `published/index.json`，选择玩家指定的 career_id；当前为 `mc_haliburton_2021`。
3. 从 main 读取 `published/saves/mc_haliburton_2021/latest.json`，看 data_updated_at 和 uploaded_at，与上次或玩家提供的时间比较。
4. uploaded_at 已填入后，按 batch_path 读 SUMMARY.md、source_coverage.json、calculations.json；不做 JSON 哈希、全字段或数量检查。详见 docs/29_SIMPLE_DATABASE_SYNC.md。
5. 按任务读取 `teams/<缩写>.json`；历史新秀用 player_catalog 的姓名/选秀年索引。

每次开始决策前简要说明实际读到的存档、游戏日期、数据更新时间和上传时间即可。不要额外运行 JSON 验收。当前已发布数据的游戏日期为 **2021-11-20**，快照事件为 checkpoint，month_closed=false；以后以玩家触发的新数据入口为准。

数据库本体在对应私有 GitHub Release 的 ZIP 中，提供给可以下载并运行 SQLite/Python 的工具；常规文件检索优先读取小 JSON，不把 SQLite 文件的存在当作已经查询过它。
