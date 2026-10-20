"""Bounded knowledge search and same-batch native mapping; analysis only."""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from gm_core.knowledge import Knowledge
from gm_data_access.knowledge_inputs import load_context
from gm_data_access import AccessError


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=('search', 'show', 'franchise', 'rules',
                                    'bpti-claim', 'bpti-source', 'bpti-contract', 'bpti-validate'))
    p.add_argument('--claim-id')
    p.add_argument('--source-id')
    p.add_argument('--as-of', help='Explicit game date; real historical knowledge remains capped at 2021-10-19')
    p.add_argument('--audience', choices=('GM', 'RESEARCH'), default='GM')
    p.add_argument('--input', type=Path, help='One BPTI DTO, not a native intent')
    p.add_argument('--analysis-packet', type=Path, help='Existing static M3 packet for Blueprint contract validation')
    p.add_argument('--tag')
    p.add_argument('--field')
    p.add_argument('--team')
    p.add_argument('--text')
    p.add_argument('--card')
    p.add_argument('--rule')
    p.add_argument('--period', default='2021')
    p.add_argument('--limit', type=int, default=5)
    p.add_argument('--career')
    p.add_argument('--batch')
    p.add_argument('--query-root', type=Path, default=ROOT/'database/query_snapshots')
    p.add_argument('--published-root', type=Path, default=ROOT/'published')
    p.add_argument('--allow-local-audited', action='store_true')
    return p


def run(a):
    k = Knowledge(ROOT/'web_gm/knowledge')
    if not 1 <= a.limit <= 5:
        raise ValueError('KNOWLEDGE_LIMIT_1_TO_5')
    if a.action.startswith('bpti-'):
        from gm_core.bpti import CONTRACTS, VERSION, HISTORICAL_CUTOFF, validate_bpti_knowledge
        from gm_core.knowledge import read_json
        if a.action == 'bpti-contract':
            return dict(schema_version=VERSION, historical_cutoff=HISTORICAL_CUTOFF.isoformat(),
                        contracts={name:list(dto.__annotations__) for name,dto in CONTRACTS.items()},
                        authority='REFERENCE_ONLY_NO_GAME_APPROVAL')
        index = k.bpti()
        if a.action == 'bpti-claim':
            if not a.claim_id:
                raise ValueError('CLAIM_ID_REQUIRED')
            return index.claim(a.claim_id, as_of=a.as_of, audience=a.audience)
        if a.action == 'bpti-source':
            if not a.source_id:
                raise ValueError('SOURCE_ID_REQUIRED')
            return index.source(a.source_id, as_of=a.as_of, audience=a.audience)
        if not a.input:
            raise ValueError('BPTI_DTO_INPUT_REQUIRED')
        dto = validate_bpti_knowledge(read_json(a.input), index, as_of=a.as_of, audience=a.audience,
                                     analysis=read_json(a.analysis_packet) if a.analysis_packet else None)
        return dict(status='VALIDATED_REFERENCE_ONLY', object_type=dto['object_type'],
                    authority='NO_NATIVE_PLAN_OR_GAME_APPROVAL')
    if a.action == 'search':
        return k.search(a.tag, a.field, a.team, a.text, a.limit)
    if a.action == 'franchise':
        if not a.team:
            raise ValueError('TEAM_REQUIRED')
        return k.franchise(a.team, a.period)
    if a.action == 'rules':
        rows = [r for r in k.rules if (not a.rule or r['rule_id'] == a.rule)
                and (not a.text or a.text.casefold() in json.dumps(r, ensure_ascii=False).casefold())]
        return dict(total_matches=len(rows), truncated=len(rows) > a.limit, rules=rows[:a.limit])
    if not a.card:
        raise ValueError('CARD_REQUIRED')
    if a.batch and not a.career:
        raise ValueError('CAREER_REQUIRED_WITH_BATCH')
    native = load_context(a.query_root, a.published_root, ROOT/'config/coach_tactics_profile.json',
                          a.career, a.batch, a.allow_local_audited) if a.career else None
    return k.show(a.card, native)


def main():
    try:
        result = run(parser().parse_args())
        print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError, sqlite3.Error, AccessError) as exc:
        print(json.dumps(dict(status='ERROR', error=str(exc)), ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main())
