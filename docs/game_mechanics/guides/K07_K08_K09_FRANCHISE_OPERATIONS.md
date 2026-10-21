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

---

# DEV29 R05-B — NBA2K22球员与选秀权交易机制、真实资产与原生执行边界（2026-10-21）

> **状态：`R05_B_RESEARCH_PUBLISHED_WITH_TRADE_UI_AND_CBA_GAPS`。** 本轮研究K08交易体系及与K07工资帽、K09选秀相连的**真实可读取数据、游戏可选项、机制限制与效果**；不作GM交易估价算法、谈判流程/人格定义、不批准新交易、不运行游戏/执行器。继续保留R04研究结案与R05-A已出版状态。
>
> **来源**：新SRC-0129..0144；本项目 `config/gameplay_policy.json`、`config/draft_asset_profile.json`、`src/draft_assets.py`、`config/roster_association_profile.json`、`docs/37_APPROVED_TRADE_EXECUTOR.md` 等真实工程材料。可检索字段及游戏菜单研究词表见 [R05-B机读目录](../catalogs/R05B_TRADE_PICK_ROSTER_MECHANICS_V1.json)。引用真实NBA2021–22规则时优先以2017 CBA时期更新资料为依据，不使用2023以后新CBA的Second Apron交易惩罚。

## 8. 三套互不替代的交易规则

| 规则层 | 谁给出 | 已知信息与能够控制的对象 | 不能作出的断言 |
|---|---|---|---|
| **现实2021–22 NBA CBA** | 2017 CBA及2021–22工资帽参考 | 大小薪资匹配、税线前后、签换、TPE、Stepien、选秀权和现金限制 | 2K22的CPU报价接受条件不一定等于真实CBA；游戏可能遗漏/简化条款 |
| **NBA2K22 Franchise原生设置** | 2K22 MyNBA/MyLEAGUE真实菜单、同版玩家观察 | Trade Logic/Trade Difficulty、Financial Trade Rules、Recently Signed/Traded、Rookie Signing、Deadline、Stepien、Override、CPU Offers/CPU-to-CPU Trades | 在线攻略列出选项≠PC22当前存档已采到开关值；也不等于原生确认“交易已生效” |
| **本项目自定世界政策与有界执行器** | 用户批准的 `PLAYER_RULES_20261017_V3` + 本机只读字段/当前玩家批准 | 双方交易意愿由外部模型研究之外决定，具体批准后，受限执行器可变更**名单归属与简单选秀权当前持有队**；只允许接下来的3届无保护/无交换 | 不是自动满足完整CBA校验，也不自动获得签约/释放/双向/复杂多方执行能力。所有游戏写入需要本次真实玩家授权 |

**该项目“双方同意就可执行交易”的自定义玩法，不是说原生2K22 Financial Trade Rules、Stepien或税务限制在所有存档都天然失效**；只意味着原生交易准入及外部已批准资产搬迁需要分开研究。游戏Trade Override功能与我们的外部数据执行器也不是同一操作。

## 9. 同版2K22玩家可见的交易设置与其影响

[SRC-0131]于NBA2K22发布后列出本代 Franchise/Mynba 交易设置清单。以下为**菜单候选**；它显示某个页面可能有此项目，**并未认证这些开关在当前PC22离线MyLEAGUE全部存在、完全同名、可以逐项读写并在重启后维持**。

| 选项英文名（同版攻略） | 可观察/修改的游戏语义 | 需留待PC22验证的精确影响 |
|---|---|---|
| `Trade Logic` | CPU是否评估交易合理性 | 关掉是否使提案失效、还是只取消对方接受判断？2022 PC玩家报告设置不同仍有不落地案例 |
| `Trade Negotiation Difficulty` | 交易谈判的游戏难度滑块 | 取值范围/具体CPU系数及当前真实设置未知，不能把难度50当50%接受率 |
| `Financial Trade Rules` | 是否让原生菜单实施薪资配平及某些财务准入 | 不能凭Off认定所有二次库存/薪资/球队预算副作用也自动合法 |
| `Recently Signed Restrictions` | 新签球员交易等待期 | 应分清现实12/15、1/15、3月和游戏日历；同版玩家报告日期比较异常[SRC-0133] |
| `Recently Traded Restrictions` | 已经被交易人物的再次交易/工资合并限制 | 分清单独再交易与与别的薪资打包；PC22精确等待期未知 |
| `Rookie Signing Restrictions` | 新秀签约后交易的特殊等待期 | 不假设所有Draft rights/签名后球员受相同窗口约束 |
| `Trade Deadline` | 是否允许常规赛截止日以后原生交易 | 2021–22现实截止日是2022-02-10，不意味着当前世界以后年度日期固定 |
| `Stepien Rule` | 连续未来首轮被交易时的限制 | 真实规则与游戏开关均有资料，`On/Off`在本机实际存档尚未读到 |
| `Trade Override` | 原生UI强制批准或覆盖CPU拒绝的候选能力 | 不等于本项目`--approve-game-writes`，不能借此绕过实际玩家批准 |
| `CPU Trade Offers` | CPU主动向所管理球队提出交易 | 不等于CPU会自行完成双方都是CPU的交易 |
| `CPU-CPU Trades` | 两支非玩家控制球队之间的原生AI自动交易 | 用户项目原生CPU-CPU交易可能单独关闭，须用真实当前批次读值确证 |
| `Trade Finder / Trade Block / Propose Trade / Player Finder` | 有查找对手/市场、提出与回看交易的不同入口；旧版Front Office Wiki有三种方法[SRC-0140] | 旧版菜单分类不证明每个PC22原版页都有完全相同的参数或模型调用路径 |

**关键同版PC22反例**：2022-07 PC MyLEAGUE一位用户确认交易菜单接受后，球员仍在原球队；回复者报告`CPU-CPU`交易未能原生落地、需要控制双方球队、或以三方结构绕过等经验[SRC-0132]。这是**一手异常报告，不是已复现的本项目bug或普适修复方案**。单击Accept与实际roster/contract/pick readback是两种不同事实。2022-01的旧世代2K22用户报告游戏12/25仍要求“到12/15才能交易”，其余奖项日期也异常[SRC-0133]；不能凭字面比较日期就下结论人物永远禁止交易。

## 10. 2021–22现实CBA的工资匹配：不能统一硬写成125%＋$100,000

历史劳资协议问题86[SRC-0129]和NBA官方TPE说明[SRC-0130]给出“**双方按各自适用额度分别判断，通常看交易完成后的纳税身份**”的规则。仅当采用现实2017 CBA的**同时交易**且球队适用对应分支时，下列参考表才有意义：

| 真实球队状态（2017 CBA时代） | 发出球员工资总额 | 最大接收工资（现实规则参考） |
|---|---:|---|
| 交易完成后为非纳税球队 | 0–$6,533,333 | 发出额×175%＋$100,000 |
| 交易完成后为非纳税球队 | $6,533,334–$19,600,000 | 发出额＋$5,000,000 |
| 交易完成后为非纳税球队 | $19,600,000以上 | 发出额×125%＋$100,000 |
| 交易完成后为纳税球队 | 任何 | 发出额×125%＋$100,000 |
| 真实有工资帽空间球队 | 视其实际空间、借助其它合法例外 | **另按剩余空间或可适用的超帽规则判断** |

**注**：在恰好处于$19.6m分段边界、交易后纳税状态与Guaranteed/Base Year Compensation/奖金等特殊情况下，还要使用完整当年CBA细则；表只是有出处的历史机制原料，**不是经本项目PC22游戏引擎验证的计算器**。

例如：假设A发出$10m而交易后仍为非纳税队，历史参考通常允许收到至多$15m；假设其交易后为纳税队则至多$12.6m。**这一个反例已经说明“125%＋$100k对所有球队统一执行”不符合历史CBA**。如果另一队同时接受，另一队也须独立验其额度、可用空间和人员资格，不能凭两队合计工资持平判合规。

`Trade Exception (TPE)`：一笔符合条件的非同时交易可能生成未来限定期限内可用于吸纳合同的例外；它**不是球队Cash、不是无限交易抵用券，也不能自动把两个不同例外与其它工资相加**。现实2017 CBA[SRC-0129]有一年左右失效规则、合同保障及收支方向限制。当前PC22原生TPE列表、消耗及残值、可否执行/当期资格都**UNKNOWN**；2022次世代用户反映找不到原本世代Trade Exception管理入口[SRC-0119]只提供UI线索。

`Sign-and-Trade`是**先通过合格签约权建立新合同，再立刻交换球员合同**的复合市场操作，不等于普通已签合同球员换队。真正的合约年薪、时间节点、硬帽和名单变化都可能需要一起验证；**本项目签约执行器`approved_signing_v1_unvalidated`尚未验收，R05-B不能因交易器存在就声称已支持原生签换**。

## 11. 2021–22选秀权：现实可交易保护/交换≠本项目简化资产

### 11.1 游戏世界同时存在三个独立的年度概念

- **游戏选秀年度**：2022、2023、2024等，是原生选秀权记录上的`draft_year`及未来3届窗口。
- **历史新秀班年份**：从1984年乔丹届开始到2020年再循环；2022游戏年选秀导入可以是1984真实历史届，但**它不是“1984年选秀权资产”**。
- **实际游戏赛季与最新已完成选秀**：由当前存档/来源批次或玩家确认，不是脚本运行了几次就推进。即使2022新秀真实举行，也不意味本世界已完成。

**项目真实Native资产布局**：`config/draft_asset_profile.json`证据记录每项**32字节**、`+0x00`当前持有队uint64、`+0x08`原队uint64、`+0x10`已指派球员uint64、`+0x1C`元数据；year offset(0–4)、round code(0/1)、pick_index及实际游戏年份由原生代码证据支持。

`src/draft_assets.py`要求可识别连续**5个未来游戏选秀年×2轮×30个原队=300条真实未来选秀权**，每组必须完全一致、不可重复，并核实下一届年份。**这五届是可完整原生读取的资产覆盖范围**，不代表本外挂全部可被交易。

### 11.2 你的世界规则：只交易下一次起的3届、无保护无交换

`config/gameplay_policy.json`中的`draft_pick_trades`明确：

| 项 | 已获用户确认的本世界规则 |
|---|---|
| 可交易选秀权 | `YEAR + ROUND + ORIGINAL_TEAM + CURRENT_OWNER_TEAM` |
| 最远 | **下一届、下下一届、下下下一届，合计3届尚未完成的年度选秀** |
| 举例 | `verified_next_draft_year=2022`，则`2022,2023,2024`，**2025、2026虽在Native表可读仍不能按当前规则交易** |
| Round | 1或2轮；完整原生每届原队30×2条 |
| 保护（Protections） | **NOT_USED**：本外挂不创建新保护条款 |
| 顺位交换（Swap Rights） | **NOT_USED**：本外挂不创建新交换权 |
| 原队与持有人 | 必须通过当前batch真实所有权数据，不能依赖GM提出“我有此签”的描述 |
| 真实游戏写入 | **另需本次玩家批准**；不得通过脚本中的“approved=true”自行授权 |

**微妙差异**：原生记录`protection`字段来源当前保持`null`或未用，不等于游戏中历史已有保护/交换条款已经被清除。**用户“本外挂不使用保护/交换”≠“原版游戏不存在该能力”**。现实NBA保护顺延和转换是独立规则，历史Stepien会因潜在未兑现保护而限制未来可交易首轮[SRC-0137]；相邻游戏中有保护/交换行为的玩家报告[SRC-0135/0136]，不能强迫本外挂采用。

### 11.3 Stepien、保护与Swap：知识价值和可操作权限完全不同

- **真实Stepien原则**限制球队通过交易陷入连续未来年份没有首轮选择的状态。2022年现实NBA专门报道列明保护顺延导致后续可交易首轮年份复杂[SRC-0137]。
- 同版2K22规则网页列出`Stepien Rule`开关，并不表明当前PC22默认On或其数学逻辑已完整校验。
- **Protections**：现实首轮签可有乐透保护、Top-N保护、顺延/次轮折算等；2K23新世代玩家[SRC-0135]报告无法为某些签直接设置保护，这说明菜单版本和交互容易混淆，**不能推断2K22 PC无保护功能**。
- **Swaps**：另一位玩家2022-12在PS5 MyNBA中讨论Swap Best/Worst及Trade Finder的价值排序[SRC-0136]，亦属之后年度邻近版本/同系列社区证据；当前项目**明确不交易交换权**。
- **现实七年期限/其它变体**不能替换当前玩家的三年窗口[SRC-0137]；三年属于本项目业务边界、不是NBA2K22原生只能存三年。

## 12. 交易名单容量、当前归属、合同归属与外部执行：不能只改一支球队

当前`config/roster_association_profile.json`和经过玩家验收的[受限交易执行器](../../37_APPROVED_TRADE_EXECUTOR.md)提供**NBA2K22这一本机版本**的真实结构：

| NBA2K22本机球队结构 | 原生位置 | 当前已证用途 |
|---|---|---|
| 常规名单 | `TEAM +0x00`起连续15个8字节引用 | **15槽上限**，受限执行器可交换/迁移普通球员 |
| 常规名单人数 | `TEAM +0xCB1` uint8 | 必须与真实非空连续普通名单一致 |
| 双向人员 | `TEAM +0xA8,+0xB0`两个8字节引用 | **最多2名双向**；当前受限交易执行器不支持双向转移 |
| 双向人数 | `TEAM +0x1047`低2位 | 作为本机实际读到的人数 |
| 活动名单 | `TEAM +0xD0`起13个8字节引用 | **13槽**，可含合法双向球员；不是普通球员Roster 13人上限 |
| 活动人数 | `TEAM +0x1047`高4位 | 参与游戏真实索引，不可只改引用不改人数 |
| 保留/其它引用槽 | `TEAM +0x78..+0xA7`，6个槽 | 当前为空、原样保留；不是额外6个普通球员席位 |
| 其它球队/战术引用 | `TEAM +0xD28..+0xE67`等 | 经本机转队试验涉及，具体规划器只处理安全子集 |
| 球员当前队与合同队 | `PLAYER +0x60`和`PLAYER +0xA8`各8字节指针 | **都须维护一致性**，但不得借此同时擅改工资或合约年限 |
| 简单选秀权持有队 | `DRAFT_ASSET +0x00` uint64 | 受限执行器只改这一项，保留原队/选秀元数据 |

**已发生的真实本机工程教训**：CHI/DET交易先因`+0xCB1`人数未同步和活动人员计数不一致，造成球员虽在结构中却不被名单计数覆盖；经受控修复后用户接受CHI/DET游戏UI结果。首次修复缺失数据不能被后来的成功回读涂掉；另有DAL/HOU内存/重启后结果证据，存盘/再次载入的完整一致性仍需按实际版本复核。这是**原生交易写入技术要求**，不是GM/球员谈判逻辑。

当前Trade Executor有`plan→execute→verify`入口，真实人物由姓名+faceID+生日或其他消歧确认，跨会话地址重新校准，原值不符则拒绝；不会自动选择非目标名单成员腾位置，不会补其他球员加能力，也没有原子交易/通用失败自动回滚。**已支持的只是该受控范围内的名单归属与简单选秀权**：同队连续多笔相互依赖交易、同时多方复杂交换、双向人员转移、签约和释放、无法完整对应的5人组和超过15人球队都阻断，不能宣称全类型交易可执行。

## 13. 本项目可用的真实交易信息与未完成的实时来源

| 对象 | 已有来源等级 | 重要未知 |
|---|---|---|
| 球员合同、当前队/合同队、常规名单与真实人数 | 静态Native结构/历史批次/受控实时校准已有 | 若当前batch与实际加载游戏不同，所有历史交易候选都必须重新核对；原生可交易等待期/交易否决权当前值未知 |
| 选秀权5届（共300条） | NativeGetter字节证据＋实际读源算法，按Game Year、Pick Index、原队、当前队 | 用户下一届选秀年份是否已推进需验证；游戏原生Protection/Swap的可靠完整解码未完成 |
| 可交易3届窗口 | 用户`PLAYER_RULES_20261017_V3` | 用户未来改变规则需独立政策版本；当期没有自动确认游戏日期时不能猜下一届 |
| 交易报价/对手态度 | 真实游戏UI/CPU Offer/Trade Finder一般机制已有系列文献 | 当前本局CPU报价、对手对任何具体资产价值评估**未实际捕获**；`Trade Difficulty`不是成功概率 |
| Salary Matching/TPE/Hard Cap | 2017现实CBA详细表及2K22选项文字 | **当前PC22游戏是否完整计算对应分档、实际队伍是否拥有TPE、每笔交易引发税/预算影响均未认证** |
| 成交与报表刷新 | 某些本机玩家批准交易成功回读 | 球队`total_salary/payroll/cash`真实刷新时点、实机保存持久化、联盟新闻/交易历史自动记录范围UNKNOWN |
| 截止日与Recently Signed | 2022同版社区有日期异常报告 | 当期`game_date`自动观测仍不可用，游戏日历是否处交易窗口需独立来源 |

**涉及项目旧规范的冲突**：[旧Trade Valuation文档](../../14_TRADE_VALUATION_AND_ASSET_POOLS.md)中的“超巨绝对非卖、统一10000点评分、125%＋$100k通用硬规则、连续未来5年选秀权/保护和交换”等，与最新用户核准的真实政策、DEV29原料边界不一致；它是**旧设想，不能当现行游戏机制、外部人物真实意愿或授权执行规则**。本轮只把其名称/区别放进来源说明，不开发或替模型定义交易估价、人生选择或双赢充要条件。

## 14. 怎样正确观察交易“真的发生”及其原生后果？

以下是**研究事实的不同类别**，不是执行工作流开发：

- `TRADE_OFFER_VISIBLE`：真实游戏或外部模型显示了某个报价；**不是成交**。
- `TRADE_ACCEPTED_BY_NATIVE_UI`：按钮显示接受或页面弹出确认；2022 PC22一手玩家报告此时可能名单尚未变[SRC-0132]，必须重读。
- `PLAYER_APPROVED_PROPOSAL`：真实用户批准外挂具体交易方案；**尚不能说已执行**。
- `ROSTER_AND_PICK_OWNERSHIP_READBACK`：经过受控操作，玩家当前/合同队、双方名单/人数和资产持有权正确；可称**本次内存状态已核实**。
- `SAVED_RELOADED_PERSISTENCE`：用户保存、重开并有对应批次同一玩家/资产身份源；与即时readback不同。
- `NEXT_GAME_ENGINE_FEEDBACK`：实际比赛、工资汇总更新、球队化学反应或联盟新闻若可采，才是真实下一阶段后果；**不预测或强行写入球员属性或化学反应**。

## 15. R05-B本轮研究交付及后续R05-C

**本轮新增**：
1. 同版NBA2K22交易设置清单及PC版接受但未成交的玩家报告、旧世代日期限制异常、Trade Finder/Block/三队交易UI候选；
2. 2017 CBA、2021–22适用的**非纳税队三档与纳税队统一125%的工资匹配分支**、TPE、签换、实际NBA Stepien与保护限制；
3. **原生5年300枚选秀权≠本项目只准交易3年、无保护/交换的规则**；原生32字节资产构造与下一届年份；
4. 球队15常规＋2双向＋13活动名单及两个独立人数位域、PLAYER当前队/合同队、选秀权归属的精确可追溯Native证据；
5. 本项目**受限交易执行已通过某些玩家确认，但尚未提供通用双向、签换/多方、免规则的财务校验**；旧程序评分方案非DEV29规范；
6. 全部资料按现实2021 CBA、2K22同版社区、其它模式/年度、Native已知和当前存档UNKNOWN分级；仍**没有完整PC22原版交易设置/限制页面逐像素认证**。

**下一轮R05-C**：K09员工与Scouting、选秀前可见/未知信息、Scouting Reports、Prospect/历史Draft Class与真实选秀结果/权利、职位/Staff工资与球队Business，要求同样的游戏信息/可选项/效果目录。R05-D最后整合经营领域资料，**不设计/训练/部署GM/Coach/Player人格，不写交易规则决策程序，也不在DEV29独立审核**。R05-B没有触发任何游戏进程、采集、真实GM交易、DEV28/Codex或执行修改。
