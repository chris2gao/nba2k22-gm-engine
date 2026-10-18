"""Read-only DEV09 probe; all output is confined to _exports/."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from mc_feature_research import capture, compare_snapshots, observe_mc_candidate, load_profile


def output_path(value):
    path = Path(value)
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    exports = (ROOT / '_exports').resolve()
    if not path.is_relative_to(exports) or path.suffix.lower() != '.json':
        raise ValueError('RESEARCH_OUTPUT_MUST_BE_EXPORTS_JSON')
    if path.exists():
        raise FileExistsError('RESEARCH_EVIDENCE_ALREADY_EXISTS')
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode-context', choices=['UNKNOWN', 'PLAYER_CONFIRMED_MYLEAGUE_TEST', 'PLAYER_CONFIRMED_MC'], default='UNKNOWN')
    parser.add_argument('--ui-side-context', choices=['UNKNOWN', 'CPU', 'USER'], default='UNKNOWN')
    parser.add_argument('--compare', help='Optional earlier research snapshot; comparison never authorizes writes.')
    parser.add_argument('--expected-mc-name', help='Only with PLAYER_CONFIRMED_MC; verifies CAREERMODE index against this exact roster name.')
    args = parser.parse_args()
    path = output_path(args.output)
    if args.expected_mc_name and args.mode_context != 'PLAYER_CONFIRMED_MC':
        raise ValueError('MC_SCENE_CONFIRMATION_REQUIRED')
    previous = json.loads(Path(args.compare).read_text(encoding='utf-8')) if args.compare else None
    from coach_locator import live_memory
    mem = live_memory(read_only=True)
    try:
        result = capture(mem, args.mode_context, args.ui_side_context)
        if args.expected_mc_name:
            result['mc_candidate'] = observe_mc_candidate(mem, load_profile(), args.expected_mc_name)
    finally:
        mem.close()
    if previous:
        result['comparison'] = compare_snapshots(previous, result)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps({'status': result['status'], 'output': str(path), 'pid': result['process']['pid'],
                      'preset_raw': result['movement']['game_style_raw'], 'game_writes': 0}, ensure_ascii=False))


if __name__ == '__main__':
    main()
