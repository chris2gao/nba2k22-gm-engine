# NBA2K20–23 终极联盟游戏机制知识库

> **研究工作主入口**：面向所有网页GPT、GM、数据分析、Codex和Antigravity。主研究版本为NBA2K22 PC本世代MyLEAGUE；NBA2K20/21/22次世代MyNBA/23系列用于理解机制、攻略、查漏与版本对照。**内容仍处于资料库建立阶段，空缺不等于游戏没有该功能。**

- **[最新正式研究路线（DEV29 V3，多角色自主涌现）](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V3.md)**（[V2网页GPT多轮交付规范](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)继续适用）
- [研究进度与恢复指针](PROGRESS.md)
- [可追溯的资料来源登记](SOURCES.md)
- [机制卡片写作模板](MECHANISM_CARD_TEMPLATE.md)
- [游戏截图及媒体资料规范](visuals/README.md)
- [外部截图/图文证据索引](visuals/EXTERNAL_VISUALS.md)

## 主研究的11个领域
K01逐场比赛/赛程；K02球队和球员普通/高级统计；K03球员和名单；K04教练和攻防/Playbook；K05实时3D游戏设置；K06训练/伤病/疲劳/成长；K07财务/交易/合同；K08选秀/球探/休赛期；K09员工/球队文化；K10历史/奖项/纪录/媒体；K11存档、自动化与跨期覆盖；**K12球员自主权/人格/关系及合同偏好到原生系统的桥接**。

## 每轮工作原则
研究窗口在每轮任务中**先搜索玩家社区/攻略及官方游戏说明**，核对所引用材料的2K版本/平台/模式；从已有资料链接与图文截取准确事实，用自己中文文字解释**是什么、怎么操作、为什么有效、联动什么、GM怎样决策、需要什么输入与输出**。每轮将新增的主题文档保存到`guides/`，使用稳定`K##`能力标识和可追溯`SRC-####`、`VIS-####`来源/图片ID；更新本页/PROGRESS/SOURCES后完成当前轮，不在未完成研究中等待用户。

**不要从“已经拿到的内存字段”反向定义整个游戏功能全集。** 原生字段认证与“可看见/可选/可写/可保存”是独立状态；没采到逐场比赛≠游戏没有逐场比赛。旧版本和次世代可用于机制理解，不自动证明PC22内存相同。

新研究文档必须能帮助：
1. GM知道可以做哪些真正有篮球意义的经营与战术决定；
2. Analytics知道支持决定的真实比赛/球员数据及可派生指标；
3. Antigravity知道应该到哪个游戏页面和原生结构定向寻找缺少的来源；
4. Codex能在研究结束时生成DEV28最小补齐清单，不重复架构和执行器。

**视觉材料**：优先记录第三方页面和图片链接、使用位置、图片证据点；确有传播许可或玩家自供的图片才纳入GitHub。不得绕过水印/假定可自由再分发；研究卡片即使没有图片二进制也必须完整可读。

**当前状态（2026-10-20）**：**R01-A/B/C/D公开资料研究全部结束**，正式研究终态为 `R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`；这不是NBA2K22 PC原生菜单/内存/历史逐场数据已完全认证。核心攻略：[K01/K02 §§0–22](guides/K01_K02_GAME_STATS.md)，来源登记`SRC-0001..0029`：[SOURCES.md](SOURCES.md)，图证索引`VIS-0001..0007`（本轮无合格新图证）：[EXTERNAL_VISUALS.md](visuals/EXTERNAL_VISUALS.md)。**六大PC22统计UI目标全部保持`UNKNOWN`，未来需从原版PC游戏只读截图或经玩家另行批准的Antigravity/DEV28定向认证**。R01不再重复网上检索，最小4张优先截图需求见[PROGRESS.md](PROGRESS.md)与[图源清单](visuals/EXTERNAL_VISUALS.md)。**R02-A正式教练战术攻略现已发布**：[K04 教练、Playbook、Freelance、ACE与逐人防守](guides/K04_COACH_AND_PLAYS.md)；来源扩展至SRC-0039，图证索引新增VIS-0008（非目标PC菜单像素认证）。**当前下一轮为R02-B：原版PC22教练/战术界面、ACE覆盖及个人防守特殊字段补证**，具体入口在[PROGRESS](PROGRESS.md)。

## 新增球员系统研究与涌现方向

玩家确定：所有游戏机制知识必须让**GM/球员/教练/媒体作为独立角色**拥有真实可观察状态、合法可选行为、协商权、信息限制与比赛/历史反馈，而非强制产生最优决策。R03仍研究训练/恢复一般机制；**R04独立研究NBA2K20–23的全部球员身份、属性、潜力、倾向、徽章、人格徽章、耐久/伤病、合同偏好（Play for Win/Financial Security/Loyalty）、球员职业自主权及字段双语义**；原经营R04顺延R05，其余后移。详情：[R04专项任务书](../development_tasks/DEV29_R04_PLAYER_FULL_PROFILE_AND_AGENCY_RESEARCH_SPEC_V1.md)。原生Ability/Potential/Badge仅正常读取观察，自主Agent同意与**真实玩家的存档写入批准**分开；人格记忆优先外挂SQLite，不擅占仍有效的原生字段。**当前研究仍是R02，R02-A已交付，接续R02-B**。
