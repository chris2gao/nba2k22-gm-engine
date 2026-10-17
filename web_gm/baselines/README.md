# ChatGPT 网页版专用：三类基线入口

> **只适用于 Web GPT（ChatGPT 网页/连接 GitHub 的聊天）。** 请勿与 Codex 的 `docs/32_DATA_CAPTURE_BASELINE_PROMPT.md` / `docs/33_DEVELOPMENT_BASELINE_PROMPT.md` 混用。角色与持久记忆协议：`docs/35_WEB_GPT_BASELINES_AND_MEMORY_PROTOCOL.md`。

## 选择基线

| 网页 GPT 窗口 | 基线文件 | 角色 | 任务产物 |
| --- | --- | --- | --- |
| **GM** | [GM_BASELINE.md](GM_BASELINE.md) | 30 队独立建队、运营、交易、历史线取舍 | 待批准 GM 方案、经营总结与记忆 |
| **开发规划** | [DEVELOPMENT_BASELINE.md](DEVELOPMENT_BASELINE.md) | 架构、规格、Codex 开发任务书与审查 | 开发任务/验收报告与记忆 |
| **数据整理分析** | [ANALYTICS_BASELINE.md](ANALYTICS_BASELINE.md) | GitHub 已发布数据 → Python/SQL → 分析结果回写 GitHub | `docs/gm_analysis/` Markdown/JSON 与记忆 |

## 三份可复制的初始化指令

### GM 基线

```text
请使用 GitHub 连接读取 chris2gao/nba2k22-gm-engine 仓库的 web_gm/baselines/GM_BASELINE.md，按其中的最小读取顺序初始化「Web GPT GM 基线」。只读取并报告当前基线版本与待办状态，不启动 GM 回合、不生成交易、不改游戏和仓库。等待我从本基线新开任务窗口给出指令。
```

### 开发规划基线

```text
请使用 GitHub 连接读取 chris2gao/nba2k22-gm-engine 仓库的 web_gm/baselines/DEVELOPMENT_BASELINE.md，初始化「Web GPT 开发规划基线」。只建立工程与职责上下文，不向 Codex 下发任务、不改代码、不触发采集/测试/发布/GM 或游戏执行。等待我的具体开发需求。
```

### 数据整理分析基线

```text
请使用 GitHub 连接读取 chris2gao/nba2k22-gm-engine 仓库的 web_gm/baselines/ANALYTICS_BASELINE.md，初始化「Web GPT 数据整理分析基线」。只读取规则、入口与最近分析记忆并报告就绪；不开始新的分析、不发布、不运行游戏、不触发 GM。等待我从本基线另开分析任务窗口。
```

## 从基线新开任务窗口

在产品中由**玩家手动**从基线聊天新开新对话或新分支；如果新对话未继承文字上下文，必须发送「读取上述基线文件，按对应基线执行本次任务：……」才可开始。**即使产品复制了聊天历史，仍必须检查 GitHub 文件最新版**。不要假设模型已自动收到其他聊天的结论。

每个任务完成后：写任务成果 → 写 `web_gm/memory/<role>/sessions/<run_id>.md` → 更新所属 `*_CURRENT.md` → 报告链接/实际提交 SHA → 停止。未成功上传不能声称已有持久记忆。

这三个基线**不能自动互相唤起**；窗口之间通过仓库文件交接。只需要按需读取本岗位文件，不要一次性加载三个基线和全部 30 队完整 JSON。
