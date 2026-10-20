-- ====================================================================
-- NBA 2K22 赛季全量常规赛/季后赛历史比赛数据系统 (Match & Box Score Ecosystem)
-- 支持跨越 100 个赛季的历史纵向长周期数据库建库标准
-- 拓扑层级: match_seasons -> match_game_days -> match_games -> match_game_teams / match_game_players
-- ====================================================================

PRAGMA foreign_keys = ON;

-- 1. 赛季总账表 (可跨越 100 个赛季: 2021-2022 至 2120-2121 或 1984 历史年代)
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

-- 2. 比赛日历索引表 (xx年月日维度聚合)
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

-- 3. 单场比赛总体数据表 (比赛数据表 1, 2, 3...)
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

-- 4. 单场比赛-球队整体与高阶数据表 (每场 2 条记录: 主队一条，客队一条)
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

-- 5. 单场比赛-各队球员技术统计与高阶数据表 (每场约 20~26 条记录: 双方各 10~13 名球员)
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

-- ====================================================================
-- 性能高频索引 (保障百个赛季几百万条记录微秒级毫秒级检索)
-- ====================================================================
CREATE INDEX IF NOT EXISTS idx_match_games_season_date ON match_games(season_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_games_teams ON match_games(home_team_id, away_team_id);
CREATE INDEX IF NOT EXISTS idx_match_game_teams_query ON match_game_teams(season_id, team_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_game_players_query ON match_game_players(season_id, player_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_game_players_team ON match_game_players(season_id, team_id, game_date);
CREATE INDEX IF NOT EXISTS idx_match_game_players_performance ON match_game_players(season_id, points, game_score);
