# 网页 GM 数据入口

项目使用私有仓库，需要先给你的 ChatGPT GitHub 文件读取连接授予本仓库访问权限。不能读取时直接报告，不猜数据。

1. 读 `web_gm/GM_INSTRUCTIONS.md`。
2. 读 `published/index.json`，选择玩家指定的 career_id；当前为 `mc_haliburton_2021`。
3. 获取本次发布回执中的 commit SHA，用固定 commit 读取 `published/saves/mc_haliburton_2021/latest.json`。
4. 核对预期 game_date/batch_id；再读其 batch_path 下的 manifest.json、SUMMARY.md、source_coverage.json、calculations.json。
5. 按任务读取 `teams/<缩写>.json`；历史新秀用 player_catalog 的姓名/选秀年索引。

首次连接自检：只回答实际读到的 career_id、game_date、batch_id、audit_check_count、counts、缺失的数据来源，并指出读取的 commit。不要先生成交易建议。当前预期游戏日期为 **2021-11-20**，快照事件为 checkpoint，month_closed=false。

数据库本体在对应私有 GitHub Release 的 ZIP 中，提供给可以下载并运行 SQLite/Python 的工具；常规文件检索优先读取小 JSON，不把 SQLite 文件的存在当作已经查询过它。
