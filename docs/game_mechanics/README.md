# NBA2K20–23 终极联盟游戏机制知识库

> **研究工作主入口**：面向所有网页GPT、GM、数据分析、Codex和Antigravity。主研究版本为NBA2K22 PC本世代MyLEAGUE；NBA2K20/21/22次世代MyNBA/23系列用于理解机制、攻略、查漏与版本对照。**内容仍处于资料库建立阶段，空缺不等于游戏没有该功能。**

- **[最新正式研究路线（DEV29 V3，多角色自主涌现）](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V3.md)**（[V2网页GPT多轮交付规范](../development_tasks/DEV_20261020_29_NBA2K20_23_FRANCHISE_MECHANICS_INTELLIGENCE_PREREQUISITE_V2.md)继续适用）
- [研究进度与恢复指针](PROGRESS.md)
- **[R04-A 球员个人资料、能力、耐久、徽章和自然成长中文指南](guides/K03_K12_PLAYER_PROFILE_AGENCY.md)**：39项当前已命名非耐久属性、16项身体部位耐久，以及职业档案和成长机制；[72项原生+37项候选字段与权限矩阵](catalogs/PLAYER_FIELD_AND_RIGHTS_MATRIX.json)、[80技能徽章+20人格候选参考目录](catalogs/PLAYER_BADGES_R04_A_REFERENCE.json)。
- [R03-A/B/C历史研究结项](R03_COMPLETION_REVIEW_CHECKPOINT.md)：用户已批准研究结项，原生健康数据欠账继续保留；当前进度以已成功更新的[PROGRESS](PROGRESS.md)为准。
- [R03-A历史断点](R03_A_PROGRESS_CHECKPOINT.md)：保留首次训练研究与用户跨代复用的原始记载
- [可追溯的资料来源登记](SOURCES.md)
- [机制卡片写作模板](MECHANISM_CARD_TEMPLATE.md)
- [游戏截图及媒体资料规范](visuals/README.md)
- [外部截图/图文证据索引](visuals/EXTERNAL_VISUALS.md)

## 主研究领域（K01–K12）
K01逐场比赛/赛程；K02球队和球员普通/高级统计；K03球员和名单；K04教练和攻防/Playbook；K05实时3D游戏设置；K06训练/伤病/疲劳/成长；K07财务/交易/合同；K08选秀/球探/休赛期；K09员工/球队文化；K10历史/奖项/纪录/媒体；K11存档、自动化与跨期覆盖；**K12球员自主权/人格/关系及合同偏好到原生系统的桥接**。

## 每轮工作原则
研究窗口在每轮任务中**先搜索玩家社区/攻略及官方游戏说明**，核对所引用材料的2K版本/平台/模式；从已有资料链接与图文截取准确事实，用自己中文文字解释**是什么、怎么操作、为什么有效、联动什么、GM怎样决策、需要什么输入与输出**。每轮将新增的主题文档保存到`guides/`，使用稳定`K##`能力标识和可追溯`SRC-####`、`VIS-####`来源/图片ID；更新本页/PROGRESS/SOURCES后完成当前轮，不在未完成研究中等待用户。

**跨世代研究原则（用户2026-10-21确认）**：终极联盟类机制在NBA2K22次世代与PC本世代之间大体可复用，尤其训练、经营、教练、球员发展和角色可选行为；**优先采纳次世代资料作为机制与角色原料**，而不是一概排除。具体新增页面、精确菜单、游戏原生字段、数值和执行能力仍分别核实；物理/比赛引擎差异另行研究。

**不要从“已经拿到的内存字段”反向定义整个游戏功能全集。** 原生字段认证与“可看见/可选/可写/可保存”是独立状态；没采到逐场比赛≠游戏没有逐场比赛。旧版本和次世代可用于机制理解，不自动证明PC22内存相同。

新研究文档必须能帮助：
1. GM知道可以做哪些真正有篮球意义的经营与战术决定；
2. Analytics知道支持决定的真实比赛/球员数据及可派生指标；
3. Antigravity知道应该到哪个游戏页面和原生结构定向寻找缺少的来源；
4. Codex能在研究结束时生成DEV28最小补齐清单，不重复架构和执行器。

**视觉材料**：优先记录第三方页面和图片链接、使用位置、图片证据点；确有传播许可或玩家自供的图片才纳入GitHub。不得绕过水印/假定可自由再分发；研究卡片即使没有图片二进制也必须完整可读。

**当前权威研究状态（2026-10-21）**：**R01与R02公开资料研究均已结案，PC22原版UI缺口封存，不是原生游戏数据/执行器已全面认证**。R01：[K01/K02 §§0–22](guides/K01_K02_GAME_STATS.md)，`R01_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`；R02：[K04 教练、攻防、Playbook、Freelance、ACE及角色原料 §§0–21](guides/K04_COACH_AND_PLAYS.md)，`R02_RESEARCH_CLOSED_WITH_PC22_UI_GAPS`。研究来源登记至**SRC-0048**：[SOURCES](SOURCES.md)，视觉索引为**VIS-0001..0008**：[EXTERNAL_VISUALS](visuals/EXTERNAL_VISUALS.md)（其中没有被认证为目标原版PC22全部Coach菜单的新增图证）。**新增纯研究、不可执行的多角色能力原料目录**：[K04_ROLE_CAPABILITY_RESEARCH_V1.json](catalogs/K04_ROLE_CAPABILITY_RESEARCH_V1.json)；只描述观察/候选选择/角色拥有者/权限/反馈来源，不开发Agent、不产生游戏写入许可。**R03-A/B/C全系列研究已由用户批准结项**：[K06中文攻略 §§0–15](guides/K06_TRAINING_HEALTH_GROWTH.md)、[R03审核报告](reviews/R03_COMPLETENESS_AUDIT_V1.md)；来源SRC-0049..0071，VIS-0009/0010；[11项训练原料目录](catalogs/K06_TRAINING_ROLE_INPUTS_RESEARCH_V1.json)及[8项健康事件目录](catalogs/K06_HEALTH_EVENTS_AND_ROLE_RIGHTS_V1.json)。**原生健康动态数据与Agent执行层仍未就绪**；用户已批准开始R04-A，并已正式发表，具体接力与停止条件见[PROGRESS](PROGRESS.md)。
**R04-A已提交**：SOURCES新增SRC-0072..0082、VIS登记目标版菜单待取证；同世代球员资料/徽章/耐久可复用，PC内存与GM发布批次继续单独标证。详见上方K03/K12和PROGRESS，R04-B为下一研究轮。

## 新增球员系统研究与涌现方向

玩家确定：所有游戏机制知识必须让**GM/球员/教练/媒体作为独立角色**拥有真实可观察状态、合法可选行为、协商权、信息限制与比赛/历史反馈，而非强制产生最优决策。R03仍研究训练/恢复一般机制；**R04独立研究NBA2K20–23的全部球员身份、属性、潜力、倾向、徽章、人格徽章、耐久/伤病、合同偏好（Play for Win/Financial Security/Loyalty）、球员职业自主权及字段双语义**；原经营R04顺延R05，其余后移。详情：[R04专项任务书](../development_tasks/DEV29_R04_PLAYER_FULL_PROFILE_AND_AGENCY_RESEARCH_SPEC_V1.md)。原生Ability/Potential/Badge仅正常读取观察，自主Agent同意与**真实玩家的存档写入批准**分开；人格记忆优先外挂SQLite，不擅占仍有效的原生字段。**当前R01/R02已结案，R03研究经用户批准结项，R04-A已发表，下一轮R04-B待用户触发**。今后研究窗口只负责各R轮研究交付，独立完整性审核由其他模型负责。
