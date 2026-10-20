-- ====================================================================
-- NBA 2K22 Antigravity 外部 GM 引擎标准数据底座 Schema
-- 适用于任何 MC 生涯、终极联盟 (MyLEAGUE) 或自定义名单存档
-- ====================================================================

CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY,           -- 2K 官方球队 ID；现役 30 队按校准集合保存 (含 CHA=31)
    abbreviation TEXT NOT NULL,             -- 球队缩写 (如 IND, LAL, GSW)
    city TEXT NOT NULL,                     -- 城市名 (如 Indiana, Los Angeles)
    name TEXT NOT NULL,                     -- 队名 (如 Pacers, Lakers)
    memory_address TEXT NOT NULL,           -- 兼容字段；新存档只存 RUNTIME_ONLY，不持久化绝对地址
    total_salary INTEGER NOT NULL,          -- 当前球队总薪资 (美元)
    payroll INTEGER,                        -- 球员实际发放薪水
    budget INTEGER,                         -- 老板运营预算
    chemistry REAL,                         -- 球队化学反应 (0.00% - 100.00%)
    fan_interest REAL,                      -- 球迷关注度
    primary_system TEXT,                    -- 主教练核心体系 (Pace & Space, Seven Seconds, Defense 等)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS coaches (
    coach_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,               -- 归属球队 ID
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    preferred_system TEXT NOT NULL,         -- 首选战术体系 (0: Balanced, 1: Grit&Grind, 2: Pace&Space, 6: 7-Seconds, 7: Defense)
    active_system TEXT NOT NULL,            -- 当前激活战术体系
    offense_grade INTEGER,                  -- 进攻战术等级
    defense_grade INTEGER,                  -- 防守战术等级
    style_preference_1 TEXT,                -- 风格偏好 1 (如 3PT_SHOOTING, TRANSITION, SIZE)
    style_preference_2 TEXT,                -- 风格偏好 2
    style_preference_3 TEXT,                -- 风格偏好 3
    memory_address TEXT NOT NULL,
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- Raw, snapshot-scoped staff source. Until a team mapping is independently
-- verified, keep the captured bytes and raw candidate ID without treating a
-- staff-pool slot as the current head coach of a franchise.
CREATE TABLE IF NOT EXISTS staff_pool_observations (
    snapshot_id TEXT NOT NULL,
    staff_slot INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    raw_team_id INTEGER,
    team_mapping_status TEXT NOT NULL,
    raw_struct BLOB NOT NULL,
    memory_address TEXT,
    PRIMARY KEY (snapshot_id, staff_slot),
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);

-- Extended sources are snapshot-scoped. Old captures receive no backfilled facts.
CREATE TABLE IF NOT EXISTS coaching_source_captures (
    snapshot_id TEXT PRIMARY KEY, save_id TEXT NOT NULL, observed_at TEXT NOT NULL,
    data_updated_at TEXT, context_json TEXT NOT NULL, metadata_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS coaching_team_observations (
    snapshot_id TEXT NOT NULL, team_id INTEGER NOT NULL, observation_json TEXT NOT NULL,
    PRIMARY KEY(snapshot_id,team_id)
);
CREATE TABLE IF NOT EXISTS player_source_details (
    snapshot_id TEXT NOT NULL, team_id INTEGER NOT NULL, roster_slot INTEGER NOT NULL,
    pool_slot INTEGER, player_name TEXT NOT NULL, face_id INTEGER NOT NULL,
    birth_date TEXT, age INTEGER, details_json TEXT NOT NULL, raw_struct BLOB NOT NULL,
    PRIMARY KEY(snapshot_id,team_id,roster_slot),
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);
CREATE TABLE IF NOT EXISTS staff_source_details (
    snapshot_id TEXT NOT NULL, staff_slot INTEGER NOT NULL, team_id INTEGER,
    role TEXT, team_mapping_status TEXT NOT NULL, details_json TEXT NOT NULL, raw_struct BLOB NOT NULL,
    PRIMARY KEY(snapshot_id,staff_slot),
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);
CREATE TABLE IF NOT EXISTS team_source_stats (
    snapshot_id TEXT NOT NULL, team_id INTEGER NOT NULL, stats_index INTEGER NOT NULL,
    totals_json TEXT NOT NULL, raw_struct BLOB NOT NULL,
    PRIMARY KEY(snapshot_id,team_id)
);
CREATE TABLE IF NOT EXISTS draft_asset_observations (
    snapshot_id TEXT NOT NULL, asset_slot INTEGER NOT NULL,
    current_owner_team_id INTEGER, original_owner_team_id INTEGER,
    draft_year INTEGER, draft_round INTEGER, protection TEXT,
    mapping_status TEXT NOT NULL, raw_struct BLOB NOT NULL,
    PRIMARY KEY(snapshot_id,asset_slot)
);

-- Legacy staff rows captured through an unverified slot-to-team mapping are
-- preserved here without a team foreign key, then removed from coaches.
CREATE TABLE IF NOT EXISTS coach_mapping_quarantine (
    legacy_coach_id INTEGER PRIMARY KEY,
    legacy_team_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    preferred_system TEXT,
    active_system TEXT,
    offense_grade INTEGER,
    defense_grade INTEGER,
    style_preference_1 TEXT,
    style_preference_2 TEXT,
    style_preference_3 TEXT,
    memory_address TEXT,
    quarantined_at TEXT NOT NULL,
    quarantine_reason TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_id INTEGER NOT NULL,               -- 归属现役球队 ID (按校准后的 30 队集合)
    contract_team_id INTEGER NOT NULL,      -- 合同归属球队 ID
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT NOT NULL,                 -- 主打位置 (PG, SG, SF, PF, C)
    secondary_position TEXT,                -- 次要位置
    height_cm INTEGER,                      -- 身高 (厘米)
    weight_lbs REAL,                        -- 体重 (磅)
    face_id INTEGER,                        -- 面补 ID (Cyberface ID)
    signature_id TEXT,                      -- 赛场互动专属动画签名 ID
    audio_sig_id TEXT,                      -- 赛场互动专属音频 ID
    
    -- 核心攻防能力 (游戏内 25~99 换算值)
    overall_rating INTEGER,                 -- 综合总评 (Overall)
    shot_close INTEGER,                     -- 近距离投篮
    mid_range INTEGER,                      -- 中距离投篮
    three_point INTEGER,                    -- 三分球属性
    free_throw INTEGER,                     -- 罚球
    driving_layup INTEGER,                  -- 切入上篮
    driving_dunk INTEGER,                   -- 切入扣篮
    ball_control INTEGER,                   -- 控球
    pass_accuracy INTEGER,                  -- 传球准确度
    pass_iq INTEGER,                        -- 传球球商
    pass_vision INTEGER,                    -- 传球视野
    perimeter_defense INTEGER,              -- 外线防守
    interior_defense INTEGER,               -- 内线防守
    steal INTEGER,                          -- 抢断
    block INTEGER,                          -- 盖帽
    offensive_rebound INTEGER,              -- 进攻篮板
    defensive_rebound INTEGER,              -- 防守篮板
    speed INTEGER,                          -- 速度
    speed_with_ball INTEGER,                -- 持球速度
    acceleration INTEGER,                   -- 加速度
    vertical INTEGER,                       -- 弹跳
    strength INTEGER,                       -- 力量
    stamina INTEGER,                        -- 体力
    
    -- 核心战术倾向 (0~100)
    shot_tendency INTEGER,                  -- 出手倾向
    pass_to_open_man INTEGER,               -- 突分助攻倾向
    on_ball_steal INTEGER,                  -- 持球抢断倾向
    contest_shot INTEGER,                   -- 贴防干扰倾向
    
    -- 战术角色分配 (PlayType)
    is_play_initiator BOOLEAN DEFAULT 0,    -- 是否为全队战术发起人 (Playmaker)
    play_type_1 TEXT,                       -- 战术类型 1 (如 P&R_BALL_HANDLER, SPOT_UP)
    play_type_2 TEXT,                       -- 战术类型 2
    play_type_3 TEXT,                       -- 战术类型 3
    play_type_4 TEXT,                       -- 战术类型 4
    
    -- 合同结构
    contract_years_left INTEGER,            -- 剩余年限
    salary_current_year INTEGER,            -- 本赛季薪水
    contract_option TEXT,                   -- 选项 (Player Option, Team Option, None)
    
    -- 性格与精神徽章
    is_expressive BOOLEAN DEFAULT 0,        -- 极具表现力
    is_friendly BOOLEAN DEFAULT 0,          -- 友善
    is_alpha_dog BOOLEAN DEFAULT 0,         -- 领头羊
    is_clutch_performer BOOLEAN DEFAULT 0,  -- 关键先生
    clutch_badge_level INTEGER DEFAULT 0,   -- 关键射手徽章等级 (0: 无, 1: 铜, 2: 银, 3: 金, 4: 紫)
    
    memory_address TEXT NOT NULL,           -- 主结构体内存地址
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

CREATE TABLE IF NOT EXISTS trade_manifests (
    trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_year INTEGER NOT NULL,
    trade_date TEXT NOT NULL,
    team_a_id INTEGER NOT NULL,
    team_b_id INTEGER NOT NULL,
    team_a_sent_players TEXT NOT NULL,      -- JSON 数组: 送出球员
    team_b_sent_players TEXT NOT NULL,      -- JSON 数组: 换回球员
    salary_diff INTEGER NOT NULL,           -- 薪资差额
    is_cba_legal BOOLEAN NOT NULL,          -- 是否符合 CBA 125%+10万 规则
    trade_status TEXT NOT NULL,             -- PENDING, APPROVED, EXECUTED, REJECTED
    execution_mode TEXT NOT NULL,           -- MYLEAGUE_OVERRIDE / MC_MEMORY_HOTSWAP
    reasoning TEXT NOT NULL                 -- GM 决策论述与双赢动机
);

CREATE INDEX IF NOT EXISTS idx_player_team ON players(team_id);
CREATE INDEX IF NOT EXISTS idx_coach_team ON coaches(team_id);

-- ====================================================================
-- 时间序列与月度数据跟踪系统 (Time-Series Monthly Data System)
-- ====================================================================

-- 1. 月度快照主表
CREATE TABLE IF NOT EXISTS monthly_snapshots (
    snapshot_id TEXT PRIMARY KEY,           -- 快照唯一编码 (如 2021-2022_M01_NOV, 2021-2022_M04_FEB_DEADLINE)
    season_year INTEGER NOT NULL,           -- 赛季年份 (如 2022)
    month_index INTEGER NOT NULL,           -- 月度序号 (1: 11月, 2: 12月, 3: 1月, 4: 2月交易截止日, 5: 3月, 6: 4月常规赛收官, 7: 季后赛)
    month_name TEXT NOT NULL,               -- 月度/阶段名称 (如 "11月常规赛初段", "2月全明星/交易截止日")
    snapshot_date TEXT NOT NULL,            -- 快照记录现实日期 (如 2021-11-30)
    games_in_period INTEGER DEFAULT 0,      -- 本周期内全联盟进行的比赛总场次
    total_games_played INTEGER DEFAULT 0,   -- 赛季至今累计比赛场次
    notes TEXT,                             -- 本月里程碑事件描述
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Metadata for a per-save database created from the reusable clean template.
CREATE TABLE IF NOT EXISTS save_metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

-- 2. 球队月度攻防与运营数据表 (全面存储实测财务、商业与战术字段)
CREATE TABLE IF NOT EXISTS team_monthly_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,              -- 关联月度快照
    team_id INTEGER NOT NULL,               -- 球队唯一 ID (按校准后的 30 队集合)
    team_abbr TEXT NOT NULL,                -- 缩写 (如 IND, GSW, LAL)
    
    -- 实测财务与经营 (直接从 0x1258 结构体读取)
    total_salary INTEGER,                   -- 球队总薪资 (0xCBC, 实测)
    payroll INTEGER,                        -- 实际发放薪资 (0xFF4, 实测)
    budget INTEGER,                         -- 运营预算 (0x1014, 实测)
    staff_budget INTEGER,                   -- 制服组预算 (0x1018, 实测)
    cash INTEGER,                           -- 现金储备 (0x1010, 实测)
    chemistry REAL,                         -- 球队化学反应 (0xEC4, 实测)
    
    -- 实测商业与物价 (直接从 0x1258 结构体读取)
    fan_interest REAL,                      -- 球迷热情度 (0xF7C, 实测 0.00 ~ 1.00)
    attendance_pct REAL,                    -- 主场上座率 (%)
    monthly_gate_revenue INTEGER,           -- 门票收入流水 (0xFD8, 实测)
    merch_revenue INTEGER,                  -- 特许商品流水 (0xFDC, 实测)
    media_revenue INTEGER,                  -- 转播媒体流水 (0xFE4, 实测)
    ticket_courtside REAL,                  -- 场边票价 (0xF98, 实测)
    ticket_lower REAL,                      -- 下层看台票价 (0xF8C, 实测)
    ticket_upper REAL,                      -- 上层看台票价 (0xF90, 实测)
    
    -- 实测战术 POE (直接从 0x1258 结构体读取)
    poe_off_pace INTEGER,                   -- 进攻节奏 POE (0xEB2, 实测)
    poe_fastbreak INTEGER,                  -- 快攻推进 POE (0xEB3, 实测)
    poe_off_reb INTEGER,                    -- 前板冲抢 POE (0xEB4, 实测)
    poe_def_reb INTEGER,                    -- 后板保护 POE (0xEB5, 实测)
    poe_on_ball INTEGER,                    -- 对球施压 POE (0xEB7, 实测)
    poe_off_ball INTEGER,                   -- 无球盯防 POE (0xEB8, 实测)
    poe_pnr_def INTEGER,                    -- 挡拆防守 POE (0xEB9, 实测)
    poe_help_def INTEGER,                   -- 协防轮转 POE (0xEBC, 实测)
    
    -- Competitive lifecycle is not directly observed by this source pipeline.
    current_lifecycle_state TEXT NOT NULL DEFAULT 'UNCLASSIFIED_INSUFFICIENT_RECORD_DATA',
    
    -- 赛况统计数据 (MC 模式内存未观测则严格为 NULL)
    total_games INTEGER,                    -- 累计比赛总场次 (未观测标为 NULL)
    total_wins INTEGER,                     -- 累计胜场 (未观测标为 NULL)
    total_losses INTEGER,                   -- 累计负场 (未观测标为 NULL)
    win_pct REAL,                           -- 累计总胜率 (未观测标为 NULL)
    conf_rank INTEGER,                      -- 分区当前排名 (未观测标为 NULL)
    month_games INTEGER,                    -- 本月进行场次 (未观测标为 NULL)
    month_wins INTEGER,                     -- 本月胜场 (未观测标为 NULL)
    month_losses INTEGER,                   -- 本月负场 (未观测标为 NULL)
    month_win_pct REAL,                     -- 本月胜率 (未观测标为 NULL)
    streak TEXT,                            -- 当前连胜/连败 (未观测标为 NULL)
    home_w_l TEXT,                          -- 主场战绩 (未观测标为 NULL)
    away_w_l TEXT,                          -- 客场战绩 (未观测标为 NULL)
    ppg REAL,                               -- 场均得分 (未观测标为 NULL)
    opp_ppg REAL,                           -- 场均失分 (未观测标为 NULL)
    net_rating REAL,                        -- 净胜分 (未观测标为 NULL)
    ortg REAL,                              -- 进攻效率 (未观测标为 NULL)
    drtg REAL,                              -- 防守效率 (未观测标为 NULL)
    pace REAL,                              -- 比赛节奏 (未观测标为 NULL)
    fg_pct REAL,                            -- 投篮命中率 (未观测标为 NULL)
    three_pt_pct REAL,                      -- 三分命中率 (未观测标为 NULL)
    three_pt_att REAL,                      -- 场均三分出手数 (未观测标为 NULL)
    ft_pct REAL,                            -- 罚球命中率 (未观测标为 NULL)
    rpg REAL,                               -- 场均总篮板 (未观测标为 NULL)
    apg REAL,                               -- 场均助攻 (未观测标为 NULL)
    tov_pg REAL,                            -- 场均失误 (未观测标为 NULL)
    
    data_source TEXT DEFAULT 'LIVE_MEMORY',
    observation_status TEXT DEFAULT 'OBSERVED_DIRECT',
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 3. 球员月度表现与能力出勤表
CREATE TABLE IF NOT EXISTS player_monthly_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,              -- 关联月度快照
    player_id INTEGER,                      -- 球员 ID
    team_id INTEGER NOT NULL,               -- 所属球队 ID
    player_name TEXT NOT NULL,              -- 球员姓名 (如 "Tyrese Haliburton")
    position TEXT,                          -- 实测主打位置 (如 PG, SG, SF, PF, C)
    
    -- 实测攻传防能力与合同 (来自实测内存指针)
    three_point_rating INTEGER,             -- 三分能力 (实测)
    pass_accuracy_rating INTEGER,           -- 传球准确度 (实测)
    speed_rating INTEGER,                   -- 速度能力 (实测)
    perimeter_defense_rating INTEGER,       -- 外线防守 (实测)
    salary_current_year INTEGER,            -- 本年年薪 (实测)
    contract_years_left INTEGER,            -- 合同剩余年限 (实测)
    face_id INTEGER,                        -- 原生面补 ID (实测)
    
    -- 赛事实时表现统计 (MC 模式内存未观测则严格为 NULL)
    overall_rating INTEGER,                 -- 综合能力 (若未实测则为 NULL)
    games_played INTEGER,                   -- 本月出场场次 (未观测标为 NULL)
    minutes_per_game REAL,                  -- 场均出场时间 (未观测标为 NULL)
    ppg REAL,                               -- 场均得分 (未观测标为 NULL)
    rpg REAL,                               -- 场均篮板 (未观测标为 NULL)
    apg REAL,                               -- 场均助攻 (未观测标为 NULL)
    spg REAL,                               -- 场均抢断 (未观测标为 NULL)
    bpg REAL,                               -- 场均盖帽 (未观测标为 NULL)
    tov_pg REAL,                            -- 场均失误 (未观测标为 NULL)
    fg_pct REAL,                            -- 投篮命中率 (未观测标为 NULL)
    three_pt_pct REAL,                      -- 三分命中率 (未观测标为 NULL)
    ft_pct REAL,                            -- 罚球命中率 (未观测标为 NULL)
    true_shooting_pct REAL,                 -- 真实命中率 (未观测标为 NULL)
    plus_minus REAL,                        -- 净胜正负值 (未观测标为 NULL)
    usage_rate REAL,                        -- 使用率 (未观测标为 NULL)
    per REAL,                               -- 效率值 (未观测标为 NULL)
    injury_status TEXT,                     -- 伤病状态 (未实测标为 NULL)
    injury_type TEXT,                       -- 伤病名称 (未实测标为 NULL)
    injury_days_left INTEGER,               -- 伤停天数 (未实测标为 NULL)
    
    data_source TEXT DEFAULT 'LIVE_MEMORY',
    observation_status TEXT DEFAULT 'OBSERVED_DIRECT',
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);

-- 4. 球员月度成长、徽章与属性异动历史表
CREATE TABLE IF NOT EXISTS player_growth_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,              -- 关联月度快照
    player_id INTEGER,                      -- 球员 ID
    player_name TEXT NOT NULL,              -- 球员姓名
    team_id INTEGER NOT NULL,               -- 所属球队 ID
    previous_ovr INTEGER,                   -- 上月能力值 (基准月可为 NULL)
    current_ovr INTEGER,                    -- 本月能力值 (基准月可为 NULL)
    ovr_delta INTEGER,                      -- 能力值变动 (基准月可为 NULL)
    mentor_name TEXT,                       -- 指派的老将导师
    trainer_tier TEXT,                      -- 制服组训练师等级
    badges_upgraded_json TEXT,              -- 获得/升级的徽章明细 (JSON)
    attribute_breakouts_json TEXT,          -- 关键突破属性明细 (JSON)
    growth_assessment TEXT,                 -- 成长综合评语
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);

-- 5. 球队月度战略审计、路线验证与决策决议表
CREATE TABLE IF NOT EXISTS team_monthly_evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,              -- 关联月度快照
    team_id INTEGER NOT NULL,               -- 球队唯一 ID
    team_abbr TEXT NOT NULL,                -- 缩写
    target_win_pct REAL,                    -- 档案设定的赛季基准预期胜率
    actual_win_pct REAL,                    -- 本月实际胜率 (未观测标为 NULL)
    win_pct_delta REAL,                     -- 胜率偏离度 (未观测标为 NULL)
    philosophy_status TEXT NOT NULL,        -- 赢球路线验证结论 (PASS: 达标, WARNING: 预警, CRITICAL: 路线崩溃, BASELINE: 建立基准)
    tactical_style_verdict TEXT NOT NULL,   -- 战术攻防风格符合度评估 (如 "外线三分空间拉满，但退防漏洞严重")
    identified_weaknesses TEXT NOT NULL,    -- 发现的核心技战术短板 (如 "内线护框虚弱", "第二阵容缺少持球发起点")
    closing_five_verdict TEXT NOT NULL,     -- 关键时刻关键终结 5 人组稳定性评价
    poe_adjustments_json TEXT NOT NULL,     -- 本月 POE 战术策略纠偏指令 (JSON)
    rotation_changes_json TEXT NOT NULL,    -- 轮换时间与人员调整建议 (JSON)
    trade_block_action TEXT NOT NULL,       -- 货架人员更新 (上架/下架)
    primary_reinforcement_need TEXT NOT NULL, -- 第一引援短板画像 (如 "3&D 侧翼", "吃饼护框中锋")
    secondary_reinforcement_need TEXT,      -- 次要引援需求
    coach_seat_status TEXT NOT NULL,        -- 主帅帅位状态 (SAFE, WATCH, HOT, FIRED)
    lifecycle_transition TEXT NOT NULL,     -- 生命周期状态流转 (如 "保持 CONTENDING", "由 BUYER 转为 STAND_PAT")
    executive_summary TEXT NOT NULL,        -- GM 月度总结与决策陈述
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 索引提升检索速度
CREATE INDEX IF NOT EXISTS idx_team_stats_snapshot ON team_monthly_stats(snapshot_id, team_id);
CREATE INDEX IF NOT EXISTS idx_player_stats_snapshot ON player_monthly_stats(snapshot_id, player_id);
CREATE INDEX IF NOT EXISTS idx_growth_snapshot ON player_growth_history(snapshot_id, player_id);
CREATE INDEX IF NOT EXISTS idx_eval_snapshot ON team_monthly_evaluations(snapshot_id, team_id);

-- ====================================================================
-- 多赛季纵向演进与王朝数据库 (Multi-Decade Dynasty & Longitudinal System)
-- 保障几十个赛季（从 2021-2022 至 2050+ 或跨年代历史重构）的动态数据完全同构规范化
-- ====================================================================

-- 6. 赛季元数据与联盟大盘表 (Seasons Master Ledger)
CREATE TABLE IF NOT EXISTS seasons (
    season_year INTEGER PRIMARY KEY,        -- 赛季年份 (如 2022 对应 2021-2022 赛季)
    season_code TEXT NOT NULL,              -- 赛季官方代号 (如 "2021-2022")
    salary_cap INTEGER NOT NULL,            -- 本季工资帽上限 (如 $112,414,000)
    luxury_tax_threshold INTEGER NOT NULL,  -- 本季奢侈税触发线 (如 $136,606,000)
    first_apron INTEGER,                    -- 第一土豪线 (Apron 1)
    second_apron INTEGER,                   -- 第二土豪线 (Apron 2)
    historical_draft_class_year INTEGER,    -- 挂接的历史选秀年 (如 1984 乔丹/大梦, 1996 科比/艾弗森, 2003 詹姆斯)
    champion_team_id INTEGER,               -- 最终总冠军球队 ID
    finals_mvp_name TEXT,                   -- FMVP 获得者
    regular_season_mvp_name TEXT,           -- 常规赛 MVP 获得者
    season_status TEXT DEFAULT 'ACTIVE',    -- ACTIVE(进行中), ARCHIVED(已归档完结)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(champion_team_id) REFERENCES teams(team_id)
);

-- 7. 球队跨赛季纵向履历与财务大账本 (Team Multi-Season History)
CREATE TABLE IF NOT EXISTS team_season_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_year INTEGER NOT NULL,           -- 赛季年份
    team_id INTEGER NOT NULL,               -- 球队唯一 ID
    team_abbr TEXT NOT NULL,                -- 球队缩写
    regular_wins INTEGER NOT NULL,          -- 常规赛总胜场
    regular_losses INTEGER NOT NULL,        -- 常规赛总负场
    win_pct REAL NOT NULL,                  -- 常规赛最终胜率
    conf_rank INTEGER NOT NULL,             -- 分区最终名次 (1-15)
    playoff_round_reached TEXT NOT NULL,    -- 季后赛阶段 (LOTTERY, FIRST_ROUND, CONF_SEMIS, CONF_FINALS, FINALS_RUNNER_UP, CHAMPION)
    season_ortg REAL NOT NULL,              -- 全季进攻效率估计
    season_drtg REAL NOT NULL,              -- 全季防守效率估计
    season_net_rating REAL NOT NULL,        -- 全季百回合净胜分
    season_pace REAL NOT NULL,              -- 全季比赛节奏
    total_payroll INTEGER NOT NULL,         -- 全季发放球员薪水总额
    luxury_tax_paid INTEGER DEFAULT 0,      -- 实际缴纳奢侈税总额
    gate_revenue_total INTEGER NOT NULL,    -- 全季主场门票总收入
    net_profit_total INTEGER NOT NULL,      -- 全季最终经营净利润 (Gate + 商业 - 薪资 - 税)
    coach_name TEXT NOT NULL,               -- 执教主教练
    primary_system TEXT NOT NULL,           -- 主打战术体系 (Pace & Space 等)
    lifecycle_end_state TEXT NOT NULL,      -- 赛季收官生命周期 (CONTENDING, REBUILDING 等)
    FOREIGN KEY(season_year) REFERENCES seasons(season_year),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 8. 球员跨赛季表现与历史档案库 (Player Multi-Season History)
CREATE TABLE IF NOT EXISTS player_season_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_year INTEGER NOT NULL,           -- 赛季年份
    player_id INTEGER,                      -- 球员 ID
    player_name TEXT NOT NULL,              -- 球员姓名
    team_id INTEGER NOT NULL,               -- 效力球队 ID
    age INTEGER NOT NULL,                   -- 赛季年龄
    games_played INTEGER NOT NULL,          -- 出场数
    games_started INTEGER NOT NULL,         -- 首发数
    mpg REAL NOT NULL,                      -- 场均出场时间
    ppg REAL NOT NULL,                      -- 场均得分
    rpg REAL NOT NULL,                      -- 场均篮板
    apg REAL NOT NULL,                      -- 场均助攻
    spg REAL NOT NULL,                      -- 场均抢断
    bpg REAL NOT NULL,                      -- 场均盖帽
    topg REAL NOT NULL,                     -- 场均失误
    fg_pct REAL NOT NULL,                   -- 投篮命中率
    three_pt_pct REAL NOT NULL,             -- 三分命中率
    ft_pct REAL NOT NULL,                   -- 罚球命中率
    ts_pct REAL NOT NULL,                   -- 真实命中率 (TS%)
    per REAL NOT NULL,                      -- 效率值 (PER)
    plus_minus_total REAL NOT NULL,         -- 赛季总正负值
    start_ovr INTEGER NOT NULL,             -- 赛季初起始能力值
    end_ovr INTEGER NOT NULL,               -- 赛季末结算能力值
    ovr_delta INTEGER NOT NULL,             -- 全年能力值升降净值
    annual_salary INTEGER NOT NULL,         -- 本年薪水
    awards_won TEXT,                        -- 获得荣誉 (如 "All-NBA 1st, All-Star, Assist Leader")
    FOREIGN KEY(season_year) REFERENCES seasons(season_year),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 9. 制服组跨赛季执教履历与胜率库 (Staff Dynasty Ledger)
CREATE TABLE IF NOT EXISTS staff_dynasty_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_year INTEGER NOT NULL,           -- 赛季年份
    staff_name TEXT NOT NULL,               -- 制服组姓名 (如 "Rick Carlisle", "Mike Brown")
    role TEXT NOT NULL,                     -- 职务 (HEAD_COACH, ASSOCIATE_HC, HEAD_TRAINER, TEAM_DOCTOR, CFO, CHIEF_SCOUT)
    team_id INTEGER NOT NULL,               -- 效力球队
    system_style TEXT,                      -- 主攻体系/风格
    offense_grade INTEGER,                  -- 进攻教鞭等级 (0-99)
    defense_grade INTEGER,                  -- 防守教鞭等级 (0-99)
    trainer_growth_mult REAL DEFAULT 1.0,   -- 训练师成长加成倍率 (如 S 级 1.25)
    doctor_injury_reduction REAL DEFAULT 0.0, -- 队医伤病削减率 (如 S 级 0.35)
    annual_salary INTEGER NOT NULL,         -- 年薪
    contract_years_left INTEGER NOT NULL,   -- 剩余年限
    regular_record TEXT,                    -- 本季执教战绩 (如 "54-28")
    playoff_record TEXT,                    -- 季后赛战绩 (如 "16-6")
    action_end_of_season TEXT NOT NULL,     -- 季末处置 (RETAINED, EXTENDED, FIRED, RETIRED)
    FOREIGN KEY(season_year) REFERENCES seasons(season_year),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 10. 选秀权与历史选秀追踪账本 (Draft Picks & History Ledger)
CREATE TABLE IF NOT EXISTS draft_picks_ledger (
    pick_id INTEGER PRIMARY KEY AUTOINCREMENT,
    draft_year INTEGER NOT NULL,            -- 选秀年份 (如 2022, 2023, 1984)
    round INTEGER NOT NULL,                 -- 轮次 (1: 首轮, 2: 次轮)
    original_team_id INTEGER NOT NULL,      -- 原始母队 ID
    current_owner_team_id INTEGER NOT NULL, -- 当前持有权球队 ID
    protections_desc TEXT NOT NULL,         -- 保护条款 (如 "Unprotected", "Top-4 Protected", "Lottery Protected")
    swap_rights_desc TEXT,                  -- 互换权约定 (如 "Swap with BKN best")
    is_executed BOOLEAN DEFAULT 0,          -- 是否已被正式兑现使用
    executed_pick_number INTEGER,           -- 兑现顺位 (1~60)
    selected_player_name TEXT,              -- 最终选中球员
    FOREIGN KEY(original_team_id) REFERENCES teams(team_id),
    FOREIGN KEY(current_owner_team_id) REFERENCES teams(team_id)
);

-- 11. 老带新导师传承代际谱系表 (Mentorship Dynasty Trees)
CREATE TABLE IF NOT EXISTS mentorship_dynasty_trees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    season_year INTEGER NOT NULL,           -- 赛季年份
    team_id INTEGER NOT NULL,               -- 球队 ID
    mentor_name TEXT NOT NULL,              -- 老将导师姓名 (如 "Mike Conley", "Draymond Green")
    mentee_name TEXT NOT NULL,              -- 青年学徒姓名 (如 "Tyrese Haliburton", "Jonathan Kuminga")
    target_badge_1 TEXT NOT NULL,           -- 目标传授徽章 1
    target_badge_2 TEXT,                    -- 目标传授徽章 2
    target_badge_3 TEXT,                    -- 目标传授徽章 3
    progress_pct REAL DEFAULT 0.0,          -- 传授进度 (0.0% ~ 100.0%)
    badge_unlocked_date TEXT,               -- 徽章完全习得解锁日期
    status TEXT DEFAULT 'IN_PROGRESS',      -- IN_PROGRESS, COMPLETED, INTERRUPTED_BY_TRADE
    FOREIGN KEY(season_year) REFERENCES seasons(season_year),
    FOREIGN KEY(team_id) REFERENCES teams(team_id)
);

-- 纵向检索索引
CREATE INDEX IF NOT EXISTS idx_team_season ON team_season_history(season_year, team_id);
CREATE INDEX IF NOT EXISTS idx_player_season ON player_season_stats(season_year, player_name);
CREATE INDEX IF NOT EXISTS idx_staff_season ON staff_dynasty_history(season_year, staff_name);
CREATE INDEX IF NOT EXISTS idx_draft_ledger ON draft_picks_ledger(draft_year, current_owner_team_id);
CREATE INDEX IF NOT EXISTS idx_mentor_tree ON mentorship_dynasty_trees(season_year, mentee_name);

-- ====================================================================
-- 全市场化资产池与动态交易撮合系统 (Market-Driven Dynamic Asset Pools)
-- 彻底实现数据驱动：新赛场数据 ──► 驱动挂牌入池 ──► 驱动他队看池 ──► 驱动市场博弈与交易
-- ====================================================================

-- 12. 真实球员交易货架公共市场池 (Market Trade Block Pool)
CREATE TABLE IF NOT EXISTS market_trade_block (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,              -- 关联快照
    team_abb TEXT NOT NULL,                 -- 挂牌母队
    player_id INTEGER,                      -- 球员 ID
    player_name TEXT NOT NULL,              -- 球员姓名 (如 "Domantas Sabonis", "Buddy Hield", "CJ McCollum")
    position TEXT NOT NULL,                 -- 位置 (PG, SG, SF, PF, C)
    age INTEGER NOT NULL,                   -- 年龄
    overall_rating INTEGER NOT NULL,        -- 当前能力值 (OVR)
    salary INTEGER NOT NULL,                -- 本季薪资
    contract_years_left INTEGER NOT NULL,   -- 合同剩余年限
    skill_archetype TEXT NOT NULL,          -- 技能标签 (如 "3&D_WING", "INSIDE_ALLSTAR_ANCHOR", "SHOT_CREATOR", "EXPIRING_SHOOTER")
    asking_price_tier TEXT NOT NULL,        -- 要价层级 (如 "HIGH_LOTTERY_PICK", "FIRST_ROUND_PLUS_YOUNG", "SALARY_RELIEF_AND_SECONDS")
    base_trade_value INTEGER NOT NULL,      -- 客观价值评分 (0~10,000 点)
    listing_reason TEXT NOT NULL,           -- 挂牌理由 (如 "战绩崩溃甩卖老将", "位置重叠腾出球权", "到期合同变现资产")
    listed_date TEXT NOT NULL,              -- 挂牌上架日期
    status TEXT DEFAULT 'AVAILABLE',        -- AVAILABLE (在售), TRADED (已成交), WITHDRAWN (撤销下架)
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);

-- 13. 市场交易谈判、竞价与成交大账本 (Market Trade Offers & Transactions)
CREATE TABLE IF NOT EXISTS market_trade_offers (
    offer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,              -- 关联快照
    buyer_team TEXT NOT NULL,               -- 求购买家球队 (如 "SAC", "NOP", "CLE")
    seller_team TEXT NOT NULL,              -- 挂牌卖家球队 (如 "IND", "POR", "BKN")
    target_player_name TEXT NOT NULL,       -- 求购目标球星
    buyer_offered_assets TEXT NOT NULL,     -- 买家送出的筹码清单 (JSON 数组: 球员 + 选秀权)
    seller_sent_assets TEXT NOT NULL,       -- 卖家送出的资产清单 (JSON 数组)
    buyer_net_gain INTEGER NOT NULL,        -- 买家主观得益点数 (Net Gain)
    seller_net_gain INTEGER NOT NULL,       -- 卖家主观得益点数 (Net Gain)
    salary_diff INTEGER NOT NULL,           -- 交易差额
    cba_legal BOOLEAN NOT NULL,             -- 是否满足 CBA 125% + 10万 配平
    trade_verdict TEXT NOT NULL,            -- 仲裁结论 (ACCEPTED_AND_EXECUTED, REJECTED_BY_SELLER, REJECTED_BY_CBA)
    verdict_reason TEXT NOT NULL,           -- 双方谈判博弈与成交/否决逻辑
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);

-- 14. 自由球员公共市场流动池 (Free Agency Pool)
CREATE TABLE IF NOT EXISTS market_free_agents (
    fa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    snapshot_id TEXT NOT NULL,
    player_name TEXT NOT NULL,
    position TEXT NOT NULL,
    age INTEGER NOT NULL,
    overall_rating INTEGER NOT NULL,
    expected_salary INTEGER NOT NULL,       -- 期望年薪
    skill_archetype TEXT NOT NULL,          -- 技能标签
    status TEXT DEFAULT 'AVAILABLE',        -- AVAILABLE, SIGNED
    FOREIGN KEY(snapshot_id) REFERENCES monthly_snapshots(snapshot_id)
);

CREATE INDEX IF NOT EXISTS idx_market_block ON market_trade_block(snapshot_id, status);
CREATE INDEX IF NOT EXISTS idx_trade_offers ON market_trade_offers(snapshot_id, trade_verdict);

-- ====================================================================
-- 15. 赛季全量常规赛/季后赛历史比赛数据系统 (Match & Box Score Ecosystem)
-- 适用于跨越 100 个赛季的历史纵向长周期数据库建库标准
-- 拓扑层级: match_seasons -> match_game_days -> match_games -> match_game_teams / match_game_players
-- ====================================================================

-- 15.1 赛季总账表 (可跨越 100 个赛季: 2021-2022 至 2120-2121 或 1984 历史年代)
CREATE TABLE IF NOT EXISTS match_seasons (
    season_id TEXT PRIMARY KEY,             -- 赛季唯一代号 (例如 '2021-2022', '1984-1985')
    season_year INTEGER NOT NULL,           -- 赛季结束年份 (例如 2022, 1985)
    season_name TEXT NOT NULL,              -- 赛季全称 (例如 '2021-22 NBA Regular Season')
    total_schedule_games INTEGER DEFAULT 1230, -- 赛程规划总场次 (常规赛通常为 1230 场)
    played_games INTEGER DEFAULT 0,         -- 已赛场次 (例如 238)
    current_game_date TEXT,                 -- 当前推进到的游戏日期 (YYYY-MM-DD)
    stage TEXT DEFAULT 'REGULAR_SEASON',    -- 赛程阶段 (PRESEASON / REGULAR_SEASON / PLAYOFFS / FINALS)
    allstar_game_index INTEGER,             -- 全明星赛在赛程中的槽位索引
    is_active BOOLEAN DEFAULT 1,            -- 是否为当前活跃正在进行的赛季
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now'))
);

-- 15.2 比赛日历索引表 (xx年月日维度聚合)
CREATE TABLE IF NOT EXISTS match_game_days (
    season_id TEXT NOT NULL,                -- 所属赛季
    game_date TEXT NOT NULL,                -- 比赛自然日 (YYYY-MM-DD, 例如 '2021-10-19')
    month INTEGER NOT NULL,                 -- 月份 (1-12)
    day INTEGER NOT NULL,                   -- 日期 (1-31)
    day_of_season INTEGER,                  -- 本赛季的第几天 (从揭幕战起计)
    scheduled_games INTEGER DEFAULT 0,      -- 当日计划场次
    played_games INTEGER DEFAULT 0,         -- 当日完赛场次
    PRIMARY KEY (season_id, game_date),
    FOREIGN KEY (season_id) REFERENCES match_seasons(season_id) ON DELETE CASCADE
);

-- 15.3 单场比赛总体数据表 (比赛数据表 1, 2, 3...)
CREATE TABLE IF NOT EXISTS match_games (
    game_uid TEXT PRIMARY KEY,              -- 全局唯一比赛标识符 (格式: '{season_id}_G{game_id:04d}')
    season_id TEXT NOT NULL,                -- 所属赛季 ID
    game_id INTEGER NOT NULL,               -- 2K 原生赛程中的 Game ID (1..1232)
    game_date TEXT NOT NULL,                -- 比赛日期 (YYYY-MM-DD)
    played_date TEXT,                       -- 实际完赛日期
    game_type TEXT NOT NULL,                -- 比赛类型 (PRESEASON / REGULAR / PLAYIN / PLAYOFF / ALLSTAR)
    home_team_id INTEGER NOT NULL,          -- 主队 2K ID (0..35)
    away_team_id INTEGER NOT NULL,          -- 客队 2K ID (0..35)
    home_team_abbr TEXT NOT NULL,           -- 主队简称 (例如 MIL, LAL, GSW)
    away_team_abbr TEXT NOT NULL,           -- 客队简称 (例如 IND, BOS, MIA)
    home_score INTEGER NOT NULL,            -- 主队全场总得分
    away_score INTEGER NOT NULL,            -- 客队全场总得分
    winner_team_id INTEGER NOT NULL,        -- 获胜球队 ID
    point_differential INTEGER NOT NULL,    -- 分差绝对值
    overtime_count INTEGER DEFAULT 0,       -- 加时赛节数 (0: 常规四节, 1: OT1, 2: OT2...)
    attendance INTEGER,                     -- 现场上座观众人数
    was_simulated BOOLEAN DEFAULT 1,        -- 是否为后台日历快速模拟完成 (1: 模拟, 0: 3D实机手打)
    status INTEGER DEFAULT 2,               -- 比赛状态 (0: 未开打, 1: 进行中, 2: 终局完赛 Final)
    is_nationally_televised BOOLEAN DEFAULT 0, -- 是否全美直播焦点战
    
    -- 四节与加时单节比分明细 (LineScore)
    home_q1 INTEGER NOT NULL, home_q2 INTEGER NOT NULL, home_q3 INTEGER NOT NULL, home_q4 INTEGER NOT NULL, home_ot INTEGER DEFAULT 0,
    away_q1 INTEGER NOT NULL, away_q2 INTEGER NOT NULL, away_q3 INTEGER NOT NULL, away_q4 INTEGER NOT NULL, away_ot INTEGER DEFAULT 0,
    
    FOREIGN KEY (season_id, game_date) REFERENCES match_game_days(season_id, game_date) ON DELETE CASCADE
);

-- 15.4 单场比赛-球队整体与高阶数据表 (每场 2 条记录: 主队一条，客队一条)
CREATE TABLE IF NOT EXISTS match_game_teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_uid TEXT NOT NULL,                 -- 关联比赛 UID
    season_id TEXT NOT NULL,                -- 赛季 ID
    game_date TEXT NOT NULL,                -- 比赛日期
    team_id INTEGER NOT NULL,               -- 本队 2K ID
    team_abbr TEXT NOT NULL,                -- 本队简称
    opponent_team_id INTEGER NOT NULL,      -- 对手 2K ID
    opponent_abbr TEXT NOT NULL,            -- 对手简称
    is_home BOOLEAN NOT NULL,               -- 是否主场 (1: 主场, 0: 客场)
    is_win BOOLEAN NOT NULL,                -- 是否赢球 (1: 胜利, 0: 失败)
    
    -- 基础传统技术统计 (Traditional Box Score)
    points INTEGER NOT NULL,                -- 本场总得分
    points_allowed INTEGER NOT NULL,        -- 本场失分
    fgm INTEGER NOT NULL, fga INTEGER NOT NULL, fg_pct REAL NOT NULL, -- 投篮命中/出手/命中率
    tpm INTEGER NOT NULL, tpa INTEGER NOT NULL, tp_pct REAL NOT NULL, -- 三分命中/出手/命中率
    ftm INTEGER NOT NULL, fta INTEGER NOT NULL, ft_pct REAL NOT NULL, -- 罚球命中/出手/命中率
    oreb INTEGER NOT NULL, dreb INTEGER NOT NULL, reb INTEGER NOT NULL, -- 前场板/后场板/总篮板
    ast INTEGER NOT NULL,                   -- 助攻数
    stl INTEGER NOT NULL,                   -- 抢断数
    blk INTEGER NOT NULL,                   -- 盖帽数
    tov INTEGER NOT NULL,                   -- 失误数
    pf INTEGER NOT NULL,                    -- 个人犯规总数
    
    -- 2K 原生专属比赛深层数据 (Game Specific Attributes)
    pts_paint INTEGER,                      -- 禁区内得分 (Points in Paint)
    pts_fastbreak INTEGER,                  -- 快攻反击得分 (Fast Break Points)
    pts_2nd_chance INTEGER,                 -- 二次进攻得分 (Second Chance Points)
    pts_off_to INTEGER,                     -- 利用失误得分 (Points off Turnovers)
    biggest_lead INTEGER,                   -- 本场最大领先优势分值
    possession_seconds INTEGER,             -- 全场控球时长 (秒数)
    possessions REAL NOT NULL,              -- 本场进攻回合数 (Possessions)
    
    -- 球队高级衍生数据 (Advanced Analytics)
    ortg REAL NOT NULL,                     -- 百回合进攻效率 (Offensive Rating: PTS / POSS * 100)
    drtg REAL NOT NULL,                     -- 百回合防守效率 (Defensive Rating: PA / POSS * 100)
    net_rating REAL NOT NULL,               -- 百回合净效率 (Net Rating: ORTG - DRTG)
    pace REAL NOT NULL,                     -- 48分钟标准比赛节奏 (Pace)
    efg_pct REAL NOT NULL,                  -- 有效命中率 (Effective FG%: (FGM + 0.5 * 3PM) / FGA)
    ts_pct REAL NOT NULL,                   -- 真实命中率 (True Shooting%: PTS / (2 * (FGA + 0.44 * FTA)))
    oreb_pct REAL NOT NULL,                 -- 进攻篮板冲抢率 (Offensive Rebound Pct)
    dreb_pct REAL NOT NULL,                 -- 防守篮板保护率 (Defensive Rebound Pct)
    reb_pct REAL NOT NULL,                  -- 全场总篮板争抢率 (Total Rebound Pct)
    ast_ratio REAL,                         -- 助攻率 / 助攻进球比 (AST / FGM)
    tov_pct REAL NOT NULL,                  -- 球队失误率 (Turnover Pct)
    
    FOREIGN KEY (game_uid) REFERENCES match_games(game_uid) ON DELETE CASCADE,
    UNIQUE(game_uid, team_id)
);

-- 15.5 单场比赛-各队球员技术统计与高阶数据表 (每场约 20~26 条记录: 双方各 10~13 名球员)
CREATE TABLE IF NOT EXISTS match_game_players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_uid TEXT NOT NULL,                 -- 关联比赛 UID
    season_id TEXT NOT NULL,                -- 赛季 ID
    game_date TEXT NOT NULL,                -- 比赛日期
    player_id INTEGER NOT NULL,             -- 2K 原生 Player ID
    player_name TEXT NOT NULL,              -- 球员全名 (例如 'Giannis Antetokounmpo')
    team_id INTEGER NOT NULL,               -- 所在球队 ID
    team_abbr TEXT NOT NULL,                -- 所在球队简称
    opponent_team_id INTEGER NOT NULL,      -- 对阵对手球队 ID
    opponent_abbr TEXT NOT NULL,            -- 对阵对手简称
    is_home BOOLEAN NOT NULL,               -- 是否主场作战
    is_starter BOOLEAN NOT NULL,            -- 是否首发出战 (1: 首发五虎, 0: 替补轮换)
    minutes INTEGER NOT NULL,               -- 出场时间 (实机分钟数)
    
    -- 个人基础技术统计
    points INTEGER NOT NULL,                -- 得分 (PTS)
    fgm INTEGER NOT NULL, fga INTEGER NOT NULL, fg_pct REAL, -- 投篮
    tpm INTEGER NOT NULL, tpa INTEGER NOT NULL, tp_pct REAL, -- 三分
    ftm INTEGER NOT NULL, fta INTEGER NOT NULL, ft_pct REAL, -- 罚球
    oreb INTEGER NOT NULL, dreb INTEGER NOT NULL, reb INTEGER NOT NULL, -- 篮板 (前板/后板/总板)
    ast INTEGER NOT NULL,                   -- 助攻 (AST)
    stl INTEGER NOT NULL,                   -- 抢断 (STL)
    blk INTEGER NOT NULL,                   -- 盖帽 (BLK)
    tov INTEGER NOT NULL,                   -- 失误 (TOV)
    pf INTEGER NOT NULL,                    -- 犯规 (PF)
    plus_minus INTEGER NOT NULL,            -- 正负值 (+/-)
    
    -- 2K 原生对位防守技术统计 (Matchup Defense Attributes)
    defensive_fgm INTEGER,                  -- 对位防守时被进球数
    defensive_fga INTEGER,                  -- 对位防守时被出手数
    defensive_fg_pct REAL,                  -- 对位防守限制命中率
    defensive_pts_allowed INTEGER,          -- 对位防守失分
    possessions INTEGER,                    -- 个人在场参与回合数
    
    -- 球员个人高级进阶数据 (Player Advanced Analytics)
    ts_pct REAL,                            -- 个人真实命中率 (TS%)
    efg_pct REAL,                           -- 个人有效命中率 (eFG%)
    usg_pct REAL,                           -- 个人球权使用率估算 (USG%)
    game_score REAL,                        -- John Hollinger 综合比赛表现分 (Game Score)
    pie REAL,                               -- 球员影响力估值预估 (Player Impact Estimate)
    ast_to_tov REAL,                        -- 助攻失误比 (AST / TOV)
    double_double BOOLEAN DEFAULT 0,        -- 是否拿到两双 (PTS/REB/AST/STL/BLK 任意两项>=10)
    triple_double BOOLEAN DEFAULT 0,        -- 是否拿到三双 (任意三项>=10)
    
    FOREIGN KEY (game_uid) REFERENCES match_games(game_uid) ON DELETE CASCADE,
    UNIQUE(game_uid, player_id)
);

-- 15.6 比赛历史性能高频索引
CREATE INDEX IF NOT EXISTS idx_match_games_season_date ON match_games(season_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_games_teams ON match_games(home_team_id, away_team_id);
CREATE INDEX IF NOT EXISTS idx_match_game_teams_query ON match_game_teams(season_id, team_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_game_players_query ON match_game_players(season_id, player_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_game_players_team ON match_game_players(season_id, team_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_game_players_performance ON match_game_players(season_id, points, game_score);
