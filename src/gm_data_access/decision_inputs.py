"""Selected offline coaching sources, never game-memory or executor modules."""
import json
from pathlib import Path
from gm_core.data_reader import attach_coaching_opponents


def coaching_source(published_root,binding,requests):
    directory=Path(published_root)/'saves'/binding['career_id']/'batches'/binding['batch_id']/'coaching'
    snapshot=json.loads((directory/'teams.json').read_text(encoding='utf-8-sig'))
    owners={r['team_id'] for r in requests if r.get('scope')=='VS_OPPONENT_DEFENSE'}
    for owner in sorted(owners):
        team=next(t for t in snapshot['teams'] if t['team_id']==owner)
        # Export contract names the file explicitly; use its team abbreviation only as a fallback.
        path=directory/'opponents'/('team_'+str(owner)+'.json')
        if not path.is_file():
            candidates=[p for p in (directory/'opponents').glob('*.json') if p.stem in (str(owner),team.get('abbreviation'),team.get('team_abbr'),team.get('team'))]
            if len(candidates)!=1:
                raise ValueError('SELECTED_COACH_OWNER_SOURCE_UNAVAILABLE:'+str(owner))
            path=candidates[0]
        attach_coaching_opponents(snapshot,json.loads(path.read_text(encoding='utf-8-sig')))
    return snapshot
