"""Small immutable finance runs and optimistic strategy revisions."""
from contextlib import closing
import json
from pathlib import Path
import sqlite3


def dump(value):
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True)


class Store:
    def __init__(self, path, readonly=False):
        self.path = Path(path).resolve()
        parts = {s.casefold() for s in self.path.parts}
        if self.path.name != 'gm_workbench.sqlite' or parts.intersection({'saves', 'query_snapshots'}):
            raise ValueError('WORKBENCH_PATH_REQUIRED_NOT_FACTS')
        self.readonly = readonly
        if readonly:
            self.c = sqlite3.connect(self.path.as_uri()+'?mode=ro', uri=True, timeout=3)
            self.c.execute('PRAGMA query_only=ON')
        else:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.c = sqlite3.connect(self.path, timeout=3)
        self.c.execute('PRAGMA foreign_keys=ON')
        if not readonly:
            self.c.executescript('''
                CREATE TABLE IF NOT EXISTS workbench_metadata(version INTEGER PRIMARY KEY);
                INSERT OR IGNORE INTO workbench_metadata VALUES(1);
                CREATE TABLE IF NOT EXISTS finance_runs(
                    run_id TEXT PRIMARY KEY, career_id TEXT NOT NULL, batch_id TEXT NOT NULL,
                    snapshot_id TEXT NOT NULL, base_season TEXT NOT NULL, calculation_version TEXT NOT NULL,
                    rule_set_id TEXT, source_binding_json TEXT NOT NULL, assumptions_json TEXT NOT NULL,
                    status TEXT NOT NULL, created_at TEXT NOT NULL, run_json TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS finance_team_years(
                    run_id TEXT REFERENCES finance_runs(run_id), team_id INTEGER, season TEXT,
                    result_json TEXT NOT NULL, PRIMARY KEY(run_id,team_id,season));
                CREATE TABLE IF NOT EXISTS finance_scenarios(
                    run_id TEXT REFERENCES finance_runs(run_id), scenario_id TEXT, kind TEXT NOT NULL,
                    result_json TEXT NOT NULL, PRIMARY KEY(run_id,scenario_id));
            ''')
        if self.c.execute('SELECT version FROM workbench_metadata').fetchall() != [(1,)]:
            self.close()
            raise ValueError('UNSUPPORTED_WORKBENCH_VERSION')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def close(self):
        self.c.close()

    def save_run(self, run):
        b = run['source_binding']
        with self.c:
            self.c.execute('INSERT INTO finance_runs VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
                (run['run_id'], b['career_id'], b['batch_id'], b['snapshot_id'], run['base_season'],
                 run['calculation_version'], run['rule_set_id'], dump(b), dump(run['assumptions']),
                 run['status'], run['created_at'], dump(run)))
            for team in run['teams']:
                for year in team['years']:
                    self.c.execute('INSERT INTO finance_team_years VALUES(?,?,?,?)',
                                   (run['run_id'], team['team_id'], year['season'], dump(year)))

    def load_run(self, run_id):
        row = self.c.execute('SELECT run_json FROM finance_runs WHERE run_id=?', (run_id,)).fetchone()
        if row is None:
            raise ValueError('FINANCE_RUN_NOT_FOUND')
        result = json.loads(row[0])
        result['scenarios'] = [json.loads(r[0]) for r in self.c.execute(
            'SELECT result_json FROM finance_scenarios WHERE run_id=? ORDER BY scenario_id', (run_id,))]
        return result

    def save_scenario(self, result):
        with self.c:
            self.c.execute('INSERT INTO finance_scenarios VALUES(?,?,?,?)',
                           (result['source_run_id'], result['scenario_id'], result['kind'], dump(result)))

    def list_runs(self, career):
        return [dict(zip(('run_id','batch_id','base_season','created_at'), row)) for row in self.c.execute(
            'SELECT run_id,batch_id,base_season,created_at FROM finance_runs WHERE career_id=? ORDER BY created_at DESC LIMIT 20', (career,))]
