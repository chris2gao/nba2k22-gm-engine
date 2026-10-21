# K07 / K08 / K09 — NBA2K22终极联盟经营机制：薪资、合同、市场、财务、员工与选秀

> **DEV29 V3 / R05-A首轮正式研究（2026-10-21）**。范围为K07工资帽/合同与球队资金、K08市场签约/交易相关约束的首批机制。**R05-B研究球员及选秀权交易与市场规则，R05-C研究员工/球探/选秀、R05-D整合经营原料与版本缺口；R05未在本轮整体结案。**
>
> **工作定位**：这里只研究游戏中有什么真实信息、可选操作及值域、NBA2K20–23机制效果、PC22本机有什么实际数据接口与限制。**不为GM写报价决策程序、不设计球员谈判人格、不开发Agent/执行器、不修改游戏、不自动给出“最优薪资方案”**。游戏世界从2021–22开始、历史选秀按1984–2020轮回；法律参考不能反过来决定当前模拟世界发生过什么。来源见[SOURCES](../SOURCES.md) SRC-0114..0128及已有[SRC-0101](../SOURCES.md)、原仓库[FA P0研究](../../development_reviews/DEV_20261017_04_OFFSEASON_FA_P0_RESEARCH.md)、[签约执行](../../38_APPROVED_SIGNING_EXECUTION.md)、[财务工作台](../../GM_FINANCE_WORKBENCH.md)。

## 0. 经济世界的四套不同“真值”

| 对象 | 真值是谁 | 目前我们能做的事 | 容易导致错误的混同 |
|---|---|---|---|
| **2021–22现实NBA CBA** | 2021年联盟官方公告、当时劳资条款 | 提供现实Salary Cap、Tax、例外、Option、Bird/RFA等定义背景 | 不能把真实2021的金额假定为本存档2023–24以后每年的游戏数值 |
| **NBA2K22游戏真实规则** | 具体存档/赛季/模式的游戏UI、真实引擎/游戏状态 | 搜索真实可见菜单/用户同版观察并记录不同年份差别 | 即使NBA CBA允许某操作，2K模拟器可能简化、阻止或错误执行 |
| **本项目已采原生数据与衍生分析** | 正式同批source、SQLite、Profile、QuerySession | 对已有合同金额/球队财务做只读计算；区分OBSERVED/CONFIGURED/SCENARIO/UNKNOWN | 数据库有字段≠真正读到可用于签约资格的业务真值 |
| **本项目外挂世界规则** | 用户批准的`gameplay_policy.json`、正式具体执行协议 | 允许交易双方自愿成交等额外业务、限制选秀权3年窗口、实际写入须玩家批准 | 不能把“外部模型达成协议”当2K已签合同，也不能借开发研究修改游戏 |

由此有四个不同判断：`现实CBA可能合法`、`2K原生UI能够操作`、`当前项目数据足以核验并计算`、`玩家已批准具体原生执行`。任何一项为UNKNOWN，不能用另一项替代。

## 1. 工资帽、奢侈税、硬帽/apron、球队资金完全不同

### 1.1 2021–22官方现实参考，不是本局最新赛季实测

NBA官方2021-08-02新闻[SRC-0114]：

| 现实2021–22项目 | 美元金额 | 机制意义 |
|---|---:|---|
| Salary Cap 工资帽 | **112,414,000** | 软帽参照；超过后常规工资帽空间不足，但符合资格可使用例外 |
| Tax Level 奢侈税起征线 | **136,606,000** | 超线可能产生递增税务责任；**不等于所有签约自动非法** |
| 90% Minimum Team Salary | **101,173,000**（官方公告按千计近似） | 现实联盟最低工资支出 |
| Non-taxpayer Mid-Level | **9,536,000** | 现实非纳税球队中产例外的当年值 |
| Taxpayer Mid-Level | **5,890,000** | 现实纳税球队中产例外的当年值 |
| Room Mid-Level | **4,910,000** | 现实有工资帽空间球队可用例外的当年值 |

2021–22现实apron**143,002,000**来自2021–22历史工资帽汇编[SRC-0115]及项目旧FA规格；不属于本次官方新闻明确给出的一项，故注明**SECONDARY_2021_ARCHIVE**。而且**apron成为某一交易或使用例外限制，并不意味着所有超apron球员签约都一律非法**；不同操作有不同适用条件。不存在一个能够单靠`payroll−cap`计算出的完整合法经营额度。

若游戏模拟到2022–23，不能继续用上一行。现实2022–23联盟后来宣布Salary Cap **123,655,000**、Tax Line **150,267,000**[SRC-0116]，但这仍只是现实参考；**实际游戏未来联赛工资帽可能由league设置、growth/sliders或事件影响**。我们的历史线不能拿现实2025–26新CBA（例如second apron）未经认证塞进2021 2K22原生制度。

### 1.2 六个常被错当同义词的经营金额

| 财务名称 | 可能包含或排除的对象 | 当前项目研究级别 |
|---|---|---|
| **Team Salary / Total Salary** | 游戏球队层的薪资总额；与逐人当期薪资、死钱/Cap Holds等不一定同口径 | native球队读数+月度发布存在，**与真正Salary Cap Table一致性未跨季实测** |
| **Payroll** | 薪资发放/球队财务栏所列支出，可能与上述合约薪资不同 | 现有队财务源有`payroll`，**单位/刷新时点和Total Salary差异待证** |
| **Budget** | 球队经营预算或总预算，是否为可支付“自由球员最高合同”由具体模式决定 | 现有`budget`静态字段；**不能自动当薪资帽空间** |
| **Staff Budget** | 受聘Coach/Trainer/Scout工资或员工预算 | 财务分析模块可能有`staff_budget`；**是否在同批真实数据已完整发布需要单独核对** |
| **Cash** | 游戏财务可见现金或符号整数 | 现有`cash`读数，编码有SIGNED解释假说未实机确认；**不能自动计算税款、球员报价资格** |
| **Cap Room / Cap Holds / Exceptions** | 球队在签约/自由市场某阶段的真实规则性容量，可能扣除自由球员预留金额、死钱、例外 | **本项目未认证完整动态Cap Holds/Exceptions/可签约额度原生来源**；`salary_cap_minus_payroll_proxy`严格只能叫Proxy |

**财务收入与票价也不等于签约资格**：现有`src/gm_core/finance.py`引用`fan_interest, ticket_courtside, ticket_lower, ticket_upper, monthly_gate_revenue`等候选。拥有售票价和关注度数据不意味着我们已证明比赛票价调高会带来多少现金、是否会降低上座、何时结算或者能用于直接超帽签约。早年MyGM Wiki列有场馆设施、媒体和广告、停车/商品等企业经营页[SRC-0127]；**这是旧模式的Business分类资料，不可认定PC22离线MyLEAGUE完整拥有所有设施、票价和老板目标菜单**。

## 2. 游戏真实可选的合同条款（不替GM决定选哪一种）

### 2.1 合同期限/金额与具体逐年薪资

2022-04 NBA2K22 MyNBA一手玩家讨论及原帖图片[SRC-0117]明确菜单出现以下**四种合同金额结构**：

| 可见报价方式 | 同版社区解释 | 原生/数值边界 |
|---|---|---|
| **Flat** | 每年金额基本不变 | 球员接受概率与UI年限合法性没有独立量化 |
| **Front-loaded / Front** | 首年较高、以后下降；回帖称每年约5% | 2K22次世代玩家说明，**不是PC22已认证固定5%的native codec** |
| **Back-loaded / Back** | 起始较低、以后逐年提高；回帖称约5% | 对球员吸引力“较高”是社区观察，不是所有球员都接受的算法 |
| **Bird** | 面向具备Bird续约资格的本队FA、同类后端递增，回帖称约8% | **Bird权利不是“只要球队有钱便总能使用”，也不保证PC本局同名菜单路径** |

上述是**报价方式/逐年向量**，并不是`contract_type`底层0..4的身份枚举（CORE/HARDSHIP/TWO_WAY/EURO_STASH/LINEUP）！不能把`contract_type=BIRD`写入，因为项目原生Enum中**没有BIRD**。所谓Bird是签约例外权/增幅资格，而非球员Roster Contract Type。

### 2.2 项目17个本机原生合同字段逐条枚举

本项目`config/memory_field_profile.json`已有**17项PLAYER.contract子字段**，其中：
- `bird_years`：+0x356 start_bit6 width4，跨字节4bit；**Bird年数≠已验证Bird/Early-Bird签约资格**。
- `original_contract_years` +0x341 bit4 width3；`years_left_on_contract` +0x32E bit2 width4；不能从“1”断言下一赛季已进入UFA池。
- `contract_option` +0x317 bit4 width2：0 NULL /1 TEAM_OPTION /2 PLAYER_OPTION /3 2_YEAR_TEAM_OPTION。
- `extension_length` +0x341 bit7 width3，`extension_option` +0x342 bit2 width2，`no_trade` +0x346 bit4 width1，`extension_no_trade` +0x31C bit5 width1。
- `contract_year_1..6`分别+0x1A4、+0x1A8、+0x1AC、+0x1B0、+0x1B4、+0x1B8，**每槽31-bit整数，剩余高位含共享保留标记，不能整块覆盖**。
- `contract_type` +0x344 bit3 width3，代码0 CORE/1 HARDSHIP/2 TWO_WAY/3 EURO_STASH/4 LINEUP；`euro_stash_years_left` +0x293 bit5 width2，`two_way_days_left` +0x15F bit2 width6。

以上为**项目字段注册**，不是本次从游戏进程新抓取，也不证明合同每项已经在公开SQLite中对所有球员有真实值。尤其`六薪资槽代表哪个赛季`在固定游戏阶段/合同Option/延期不同情况下仍**未经正式跨休赛期认证**。具体字段Machine目录见[R05-A字段与经营动作研究索引](../catalogs/R05A_FINANCE_CONTRACT_MARKET_RESEARCH_V1.json)。

**另一个关键归属点**：游戏内球员current team指针+0x60与contract team指针+0xA8可能不同，签约需核对球员本人、两队名单、队伍人数和合同归属；不能只写一个current_team_id当做合约已生效。[项目签约执行文档](../../38_APPROVED_SIGNING_EXECUTION.md)

## 3. Bird / Early Bird / Non-Bird、RFA/QO与工资帽保留额（Cap Holds）

### 3.1 相同人物可能有完全不同的市场身份

| 身份/操作 | 现实2021系列参考机制 | NBA2K22原生证据及待证 |
|---|---|---|
| UFA 不受限自由球员 | 可以与任何球队签约；母队通常不能强制同价匹配 | 当前项目`market_free_agents`某历史批次**0行**；不能说“没有FA”或“自动有母队匹配权” |
| RFA 受限制自由球员 | 需真正有效的Qualifying Offer等条件，原队可匹配对方Offer Sheet | 2K22及相邻版本玩家报告单年QO覆盖多年合同的现象[SRC-0118]；本局是否已复现UNKNOWN |
| Bird Rights | 现实符合3年连续资历等条件，母队可使用相应超帽续约途径 | Registry有`bird_years`，仍缺符合资格、cap hold、renounce与实机签约校验 |
| Early Bird / Non-Bird | 满足较短年限/原合同路径的有限额超帽续约 | 2K22 PC全部资格、合同年限和可见UI编码未认证 |
| Team Option / Player Option | 控制权不同：Team由队伍决定是否继续，Player由球员控制是否延续 | 2K22历史归档可见；项目Enum可读，但**选项节点前/后years_left和薪资滚动未知** |
| Cap Hold / Renounce Rights | 未续约FA对球队薪资空间可产生预留，主动放弃权利可以释放空间，但也可能牺牲Bird续约权 | 2K22玩家说明旧本世代可在Salary Cap Table放弃Cap Holds，次世代MyNBA迁至独立Cap Holds入口[SRC-0119]；这是**同版菜单路径差异**，不是PC已认证按钮 |
| Trade Exception / Disabled Player Exception | 现实NBA特例有不同签约/交易约束 | 不可直接当做游戏PC22真实可消费特例；见R05-B交易与合同特例研究 |

**现实NBA2021–22的税帽参数来自SRC-0114，RFA、QO、Bird、各类例外的定义参见NBA官方历史说明[SRC-0120]及2022自由市场真实案例[SRC-0121]。** 必须防止把如今NBA.com随2026更新的通用文章中的新CBA变化误当作2021 2K22规则。**当前无认证RFA资格来源时不能把队伍主观“拥有Bird”当自动可强制匹配的法律地位。**

### 3.2 “报价被接受→合同不正确”的游戏风险

2021-07 OS 2K系列玩家[SRC-0118]报告有资格报价的RFA，休赛期Moratorium里协商过长年合同，推进后球员仍拿到**单年QO**。该帖子**最早发生于2K22正式发售之前**，不能证明当时玩的已是2K22；论坛用户档案“2k22 MyNBA”可能在其后更新。2022-02的同版玩家另报告类似现象[SRC-0122]。2023-07仍有人抱怨多年QO被覆盖[SRC-0123]。

**这组资料的研究价值是“签约菜单认可≠合同持久生效、跨阶段读回必要”，而不是证明所有2K22 PC签约都有BUG**。不能为了规避难题将`原游戏没写成功`篡改为`球员突然不忠诚`，更不能不经批准直接替换合同。

## 4. 休赛期自由市场的可观察阶段与原生AI干扰

**现实2021–22流程序列**：赛季结束→Draft前后资格/球队与球员Option/QO决策→报价窗口及Moratorium→可正式签约→名单确定/进入下一季[SRC-0120/0121]。**PC22实际游戏季后赛到下季的节点必须在原版游戏逐阶段核对**，不应按现实日期强行安排外部系统触发。

本仓库FA P0记录[SRC-PROJECT-FA-P0]（[研究报告](../../development_reviews/DEV_20261017_04_OFFSEASON_FA_P0_RESEARCH.md)）发现：
- 已有历史归档30队、466人大名单六薪资槽与多种合同状态；正式`market_free_agents`**0行**，不证明真正FA自由市场候选池已获得；
- 当前日历识别、选项变动、QO有效性、合同Slot跨季滚动、CPU原生自动签约能否关闭/安全停点、正式签约写入持久性都**未在测试副本实机验证**；
- `docs/38_APPROVED_SIGNING_EXECUTION.md`的`SIGNING_LAYOUT_VALIDATED=False`、`SIGNING_EXECUTION_ENABLED=False`仍关闭，状态`approved_signing_v1_unvalidated`。**源码存在≠可以执行游戏签约**；
- 现有`scripts/offseason_plan.py`是离线规划器，用历史字段与假设数据演示，不是完整FA竞价已经获得真实世界源或原生选项。

**DEV29研究的合法动作词表（非系统工作流设计）**：查看Salary Cap Table/队伍薪资、原队Offer Rights、选择是否执行Option、发QO或放弃、保留/放弃Cap Holds、对UFA出价、合法RFA Offer Sheet/匹配、给予各种合同年薪曲线、最小合同/各种例外、教练员工预算，以及交易相关Cap Exceptions。**只记游戏可支持的选择及真实未知，不定义Player Agent为什么选择某个报价，也不假装这些功能当前全部有执行接口。**

## 5. 现实NBA财务与球队Business不是“玩家签约资金池”

旧MyGM/Business Wiki[SRC-0127]列入场馆维护/升级、Ticket/Merchandise/Concessions/Parking价格、媒体收入、球衣销售、业主目标。**至少“旧版游戏有Business栏目”这一点有文本来源**，但MyGM与MyLEAGUE的Owner Budget权限不同：不可没有PC22菜单就说本世界所有30队GM可以改球票、改球馆、给财务垫资。

2K22**PS5 MyNBA**官方[SRC-0128]另有独立的MySTAFF，包括Front Office、Coaching、Scouting、Sports Medicine四部门，要求权衡员工预算；这些属于经营概念可复用的同版设计，但**不能把17个次世代员工岗位直接当作PC MyLEAGUE人事字段**，Staff/Scout的精确字段与职位在R05-C集中清点。

真实球员薪水、团队薪资总额、Staff Salary、当前合同年薪、球队现金和票价都可能属于不同经济对象；对未来GM最重要的是**真实来源、单位、入账时点和可配置选择**, 而不是让本研究指定统一“赢球最佳预算”。

## 6. 目前项目能可靠提供的“财务事实”及缺口

| 本仓库模块 | 能提供/已实现 | **不提供/尚未验收** |
|---|---|---|
| `config/memory_field_profile.json` | PLAYER17个Contract字段，STAFF24-bit Salary（+0xF8），部分球队钱/名单字段另在Source/P0记录 | 真实球员薪资槽对应赛季的最终认证、实际Salary Cap exceptions、真实球员报价意愿 |
| `src/source_extensions.py`及旧Source Pipeline | 月度已采`total_salary/payroll/budget/cash`等，历史归档有用 | 当前球员FA全部身份、动态Cap Holds/合规空间、签到合同持久性 |
| `src/gm_core/finance.py` | `payroll_minus_tax_line`、`salary_cap_minus_payroll_proxy`及观察工资合计；Business可以列Staff Budget、Fan Interest/票价候选 | 不能直接从代理差额判断新签可行，不能从`cash`做税金自动扣账 |
| `docs/GM_FINANCE_WORKBENCH.md` | 独立只读的三年（最多六年）合同情景工作台、候选交易/签约方案逐年薪资比较；记录SCENARIO、UNKNOWN与条件分支 | 不做报价竞价、不给合法资格，`signing_capacity=UNKNOWN`，不操作游戏；M02六薪资槽年份映射只是`SLOT_SEQUENCE`情景 |
| `docs/37_APPROVED_TRADE_EXECUTOR.md` | 玩家批准后的具体交易身份/资产/读回安全能力 | 不等于工资帽/FA全合同条例覆盖；R05-B专门研究真实交易规则 |
| `docs/38_APPROVED_SIGNING_EXECUTION.md` | 存在有约束的最小签约源码、合同解码规则和身份反作弊保护 | **尚未实机验收，默认不可写游戏**；不能在R05研究过程中擅自打开开关 |
| `config/source_catalog.json` | 已准确把工资规则模板/Source与衍生财务工作台区别 | `game_calendar_detection=NOT_OBSERVED`、`offseason_development=P0_PARTIAL_REAL_GAME_NOT_VERIFIED`、`finance_semantics=RAW_PRESERVED_SIGNED_CASH_HYPOTHESIS_UNVERIFIED` |

若未来资料显示`total_salary=150m、salary_cap=112.414m`，只能得出**按该口径高于现实参考软帽37.586m**，**不能得出不能再签一名球员、能用Bird签任意金额或必须扣税某金额**。理由可能是该队的Cap Holds、例外、Option决策、应计年度、apron触发条件、已支付合同、预算与游戏设置未知。

## 7. R05-A研究结论：可选动作和禁推断清单

- 工资帽、税线、apron、现金/预算、员工薪资、球员逐年合同和球队营业收入是不同层次，**不合并为一种球队“有钱”指标**。
- 2022同版提供Flat/Front/Back/Bird合同曲线**可见玩法参考**，而已采Player.contract的`contract_type`是另一组Roster枚举，不能错写。
- UFA、RFA、Bird、QO、Cap Holds、Options可作为未来模型需要认识的市场对象，**RFA匹配权不等于Bird续约权，也不等于母队所有UFA的强制回购权**。
- 对所有规则保留`2021_REAL_NBA`、`2K22_CROSS_GEN_OBSERVED`、`PC22_TARGET_UI_UNVERIFIED`、`PROJECT_NATIVE_PROFILE_ONLY`、`CURRENT_GAME_SOURCE_UNKNOWN`的证据等级。
- **研究不直接定义谈判权重、出价顺序、模型行为或实现协议**。用户批准游戏修改的原则不变；普通经营禁止直接编辑Ability/Potential/Badge。
- 后续R05-B应具体覆盖球员/选秀权交易、工资匹配、TPE、签约交易、交易截止日/15人名单与本项目简化3年选秀权政策；R05-C再查员工、球探、历史选秀、Draft Stash和球队经营预算；R05-D作跨域来源/游戏设置清单而非自审人格系统。

**本轮状态**：`R05_A_RESEARCH_PUBLISHED_WITH_FINANCE_EXECUTION_GAPS`，**下一轮R05-B尚未启动**。没有运行游戏或测试存档，没有采集、开发Agent、启动DEV28/Codex、进行真实GM合同决策或修改游戏数据。
