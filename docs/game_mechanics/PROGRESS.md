# 游戏机制资料库：研究进度与断点恢复

状态：`KNOWLEDGE_BASE_SCAFFOLD_READY`，最近更新2026-10-20。**此处仅说明进度，不宣称知识已经研究完毕。**

权威总计划：[DEV29 V2](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)。

| 轮次 | 游戏主题 | 状态 | 核心文档 | 下一步 |
|---|---|---|---|---|
| R01 | 逐场赛程、Game Logs、每场Box、Advanced/Shot Chart | NOT_STARTED | 待建立 `guides/K01_K02_GAME_STATS.md` | **优先启动**；避免重蹈只采赛季累计的遗漏 |
| R02 | 教练、Playbook、战术类型/纪律与攻防 | NOT_STARTED | 待建立 `guides/K04_COACH_AND_PLAYS.md` | 后续 |
| R03 | 球员、训练、疲劳、伤病、成长 | NOT_STARTED | 待建立 `guides/K03_K06_PLAYER_TRAINING.md` | 后续 |
| R04 | 合同、财务、员工、球探/选秀、休赛期 | NOT_STARTED | 待建立 `guides/K07_K09_FRANCHISE_OPERATIONS.md` | 后续 |
| R05 | 实时3D设置、历史纪元、联赛规则、游戏自动化 | NOT_STARTED | 待建立 `guides/K05_K10_K11_WORLD_SETTINGS.md` | 后续 |
| R06 | 全域查漏、跨机制关系、决策证据及索引合并 | NOT_STARTED | 待建立 `catalogs/`机读清单 | 后续 |
| FINAL-CODEX | 源/图/能力矩阵工程收尾 | NOT_STARTED | 待生成工程回执 | **只在网页研究完成后启动** |

## 下一轮窗口开始时
1. 读取`README.md`、本文件、DEV29 V2，检查最新 GitHub 主线及是否有该轮此前的主题文档。
2. 优先从玩家社区、图文攻略、官方手册里研究**R01逐场比赛与高级统计**，不要在同轮铺开K01–K11的宽泛资料简介。
3. 本轮交付至少包含：具体菜单/数据名称及版本、核心玩法说明、逐场与累计/Advanced区别、GM分析需求、来源ID与图源ID、未知PC22本机事项。
4. 将文档和新来源写入GitHub；把本轮状态更新为`COMPLETE/INCOMPLETE_WITH_OPEN_ITEMS`，保存下一轮具体切入点；用户再触发下一轮即可，不依赖长对话恢复。

## 研究型验收
- `DOCUMENTED`：有来源、实际游戏机制和使用方法；
- `VERIFIED_FOR_VERSION`：准确标注适用版本/模式；
- `PC22_NATIVE_PENDING`：需要后续目标游戏读取认证；
- `DEV28_GAP_OPEN`：研究发现GM需要但当前源/执行缺失。

重要：`INCOMPLETE_WITH_OPEN_ITEMS`可以结束单轮研究，但不能冒充全资料库完成。
