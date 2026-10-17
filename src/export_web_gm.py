"""Export an audited SQLite capture into immutable, small files for a web GM.

No game memory, network, LLM, or game writes are used. SQLite remains the source;
JSON is a derived reading surface. Publication is a separate explicit operation.
"""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import tempfile
import zipfile

from data_context import decode_context
from gm_engine import GMEngine
from historical_rookies import is_historical_rookie
from save_context import save_paths
from snapshot_integrity import file_sha256, snapshot_digest, write_json_atomic

ROOT = Path(__file__).resolve().parent.parent
PUBLISHED = ROOT / "published"
ARCHIVES = ROOT / "_exports" / "archives"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def connect(path):
    conn = sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def write(path, value):
    write_json_atomic(str(path), value)


def public_row(row, excluded=()):
    return {key: row[key] for key in row.keys() if key not in set(excluded) | {"raw_struct", "memory_addr", "memory_address"}}


def verify_bundle(directory, expected_hash=None):
    directory = Path(directory).resolve()
    manifest_path = directory / "manifest.json"
    if expected_hash and file_sha256(str(manifest_path)) != expected_hash:
        raise RuntimeError("Published manifest hash mismatch")
    manifest = load(manifest_path)
    if not manifest.get("files") or manifest.get("audit_verdict") != "PASS_VERIFIED":
        raise RuntimeError("Invalid or unaudited bundle")
    for relative, meta in manifest["files"].items():
        path = (directory / relative).resolve()
        if not path.is_relative_to(directory) or not path.is_file():
            raise RuntimeError(f"Missing or unsafe bundle path: {relative}")
        if path.stat().st_size != meta["bytes"] or file_sha256(str(path)) != meta["sha256"]:
            raise RuntimeError(f"Bundle file changed: {relative}")
    return manifest


def compare_rows(before, after, keys):
    def indexed(rows):
        result = {}
        for row in rows:
            key = tuple(row[field] for field in keys)
            if key in result:
                raise RuntimeError(f"Ambiguous comparison identity: {key}")
            result[key] = row
        return result
    left, right = indexed(before), indexed(after)
    changed = []
    for key in sorted(left.keys() & right.keys(), key=repr):
        fields = {field: {"before": left[key].get(field), "after": right[key].get(field)}
                  for field in left[key].keys() | right[key].keys()
                  if left[key].get(field) != right[key].get(field)}
        if fields:
            changed.append({"identity": list(key), "fields": fields})
    return {"added": [right[key] for key in sorted(right.keys() - left.keys(), key=repr)],
            "removed": [left[key] for key in sorted(left.keys() - right.keys(), key=repr)], "changed": changed}


def export_snapshot(save_id, snapshot_id):
    paths = save_paths(save_id)  # Does not create or reset a career.
    for name in ("db_path", "player_pool_db_path"):
        if not Path(paths[name]).is_file():
            raise FileNotFoundError(paths[name])
    audit = GMEngine(db_path=paths["db_path"], snapshots_dir=paths["snapshots_dir"],
                     player_pool_db_path=paths["player_pool_db_path"]).verify_snapshot_gate(snapshot_id)
    source_manifest_path = Path(paths["snapshots_dir"]) / f"ingest_manifest_{snapshot_id}.json"
    source_manifest = load(source_manifest_path)
    source_manifest_hash = file_sha256(str(source_manifest_path))
    source_pool_hash = file_sha256(paths["player_pool_db_path"])
    league, pool = connect(paths["db_path"]), connect(paths["player_pool_db_path"])
    try:
        metadata = league.execute("SELECT * FROM monthly_snapshots WHERE snapshot_id=?", (snapshot_id,)).fetchone()
        context = decode_context(metadata["notes"])
        if context.get("career_id", save_id) != save_id:
            raise RuntimeError("Context career does not match the selected database")
        if context.get("game_date") and int(context["game_date"][:4]) not in (metadata["season_year"] - 1, metadata["season_year"]):
            raise RuntimeError("Player-confirmed game date does not match the selected season")
        context_hash = hashlib.sha256(json.dumps(context, sort_keys=True).encode()).hexdigest()[:8]
        batch_id = f"{snapshot_id}_{source_manifest_hash[:12]}_{context_hash}"
        final_dir = PUBLISHED / "saves" / save_id / "batches" / batch_id
        pointer_path = PUBLISHED / "saves" / save_id / "latest.json"
        if final_dir.exists():
            existing = verify_bundle(final_dir)
            if existing["source_binding"]["ingest_manifest_sha256"] != source_manifest_hash:
                raise RuntimeError("Existing immutable batch belongs to a different capture")
            return existing

        teams = [public_row(row, {"id", "snapshot_id"}) for row in league.execute(
            "SELECT * FROM team_monthly_stats WHERE snapshot_id=? ORDER BY team_id", (snapshot_id,))]
        identities = {row["team_id"]: public_row(row) for row in league.execute("SELECT team_id, abbreviation,city,name FROM teams")}
        players = [public_row(row, {"id", "snapshot_id", "player_id"}) for row in league.execute(
            "SELECT * FROM player_monthly_stats WHERE snapshot_id=? ORDER BY team_id, player_name, face_id", (snapshot_id,))]
        staff = [{"staff_slot": row["staff_slot"], "first_name": row["first_name"], "last_name": row["last_name"],
                  "observed_candidate_team_id": row["raw_team_id"], "team_id": None,
                  "team_mapping_status": row["team_mapping_status"]} for row in league.execute(
            "SELECT * FROM staff_pool_observations WHERE snapshot_id=? ORDER BY staff_slot", (snapshot_id,))]
        models = []
        for row in pool.execute("SELECT * FROM player_pool ORDER BY slot_id"):
            model = public_row(row)
            model["model_category"] = "HISTORICAL_ROOKIE" if is_historical_rookie(row["raw_struct"]) else "OTHER_UNCLASSIFIED"
            models.append(model)
        counts = {"teams": len(teams), "active_players": len(players), "staff_observations": len(staff),
                  "player_models": len(models), "historical_rookie_models": sum(row["model_category"] == "HISTORICAL_ROOKIE" for row in models)}
        if counts["teams"] != 30 or counts["active_players"] != audit["counts"]["player_monthly_stats"] or counts["player_models"] != audit["player_pool_records"]:
            raise RuntimeError("Export counts disagree with the audited source")
        rules = dict(league.execute("SELECT * FROM seasons WHERE season_year=?", (metadata["season_year"],)).fetchone())
        source_catalog = load(ROOT / "config" / "source_catalog.json")
        previous = load(pointer_path) if pointer_path.exists() else None
        change_report = {"status": "INITIAL_BASELINE", "previous_batch_id": None, "monthly_game_statistics_available": False}
        if previous:
            previous_dir = PUBLISHED / previous["batch_path"]
            previous_manifest = verify_bundle(previous_dir, previous["manifest_sha256"])
            if previous_manifest["context"].get("purpose") != context.get("purpose"):
                raise RuntimeError("Production and validation streams must use different save IDs")
            old_league = load(previous_dir / "league.json")
            old_players = [player for team in old_league["teams"] for player in load(previous_dir / "teams" / f"{team['team_abbr']}.json")["roster"]]
            change_report.update({"status": "COMPARED_TO_PREVIOUS_PUBLISHED_CAPTURE", "previous_batch_id": previous["batch_id"],
                                  "teams": compare_rows(old_league["teams"], teams, ("team_id",)),
                                  "rosters": compare_rows(old_players, players, ("team_id", "player_name", "face_id"))})
        ARCHIVES.mkdir(parents=True, exist_ok=True)
        staging_root = ROOT / "_exports" / "staging"
        staging_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="web_gm_", dir=staging_root) as temp:
            temporary = Path(temp)
            bundle = temporary / "bundle"
            bundle.mkdir()
            write(bundle / "league.json", {"teams": teams, "rules": rules, "counts": counts})
            for team in teams:
                write(bundle / "teams" / f"{team['team_abbr']}.json", {"identity": identities[team["team_id"]], "state": team,
                      "roster": [row for row in players if row["team_id"] == team["team_id"]]})
            write(bundle / "staff.json", {"ownership_verified": False, "complete_global_employee_pool_verified": False, "records": staff})
            write(bundle / "source_coverage.json", source_catalog)
            write(bundle / "changes.json", change_report)
            calculations = {"method": "deterministic_python_v1", "currency": "USD", "financial_room_is_proxy_not_certified_CBA_room": True,
                            "teams": [{"team_id": team["team_id"], "abbr": team["team_abbr"],
                                       "salary_cap_minus_observed_payroll_proxy": rules["salary_cap"] - team["total_salary"],
                                       "observed_payroll_minus_luxury_tax_line": team["total_salary"] - rules["luxury_tax_threshold"],
                                       "observed_roster_salary_sum": sum(player["salary_current_year"] for player in players if player["team_id"] == team["team_id"])} for team in teams]}
            write(bundle / "calculations.json", calculations)
            by_year = defaultdict(list)
            for row in models:
                by_year[str(row["draft_year"]) if row["draft_year"] is not None else "unknown"].append(row)
            catalog, names = {}, defaultdict(list)
            for year, records in sorted(by_year.items()):
                catalog[year] = []
                for start in range(0, len(records), 200):
                    relative = f"player_catalog/{year}_{start // 200 + 1}.json"
                    write(bundle / relative, {"records": records[start:start + 200]})
                    catalog[year].append(relative)
                    for row in records[start:start + 200]:
                        names[row["full_name"].casefold()].append({"slot_id": row["slot_id"], "model_category": row["model_category"], "file": relative})
            write(bundle / "player_catalog/index.json", {"years": catalog, "model_count": len(models), "identity_scope": "Model slots are not persistent person IDs across roster replacements"})
            write(bundle / "player_catalog/name_index.json", dict(sorted(names.items())))
            write(bundle / "audit.json", {key: audit[key] for key in ("snapshot_id", "audit_timestamp", "verifier", "verdict", "checks", "counts", "database_digest_sha256", "player_pool_sha256")})
            (bundle / "SUMMARY.md").write_text(
                f"# {save_id}: {context.get('game_date') or 'GAME DATE UNCONFIRMED'}\n\n"
                f"Purpose: {context['purpose']}; event: {context.get('event')}; game date source: {context.get('game_date_provenance')}.\n\n"
                f"Audited {len(audit['checks'])}/{len(audit['checks'])}; {len(teams)} teams; {len(players)} active players; {len(models)} player models.\n\n"
                "Read manifest.json, source_coverage.json, calculations.json, then only the teams needed. Null means unavailable, never zero.\n\n"
                "Game results, monthly box scores, injuries, full CBA ledger and staff ownership are unavailable. Financial differences are proxies.\n"
                "Historical/real-world scenarios are separate from observed game facts. All decisions remain proposals requiring player approval.\n",
                encoding="utf-8")
            backups = temporary / "databases"
            backups.mkdir()
            for name, conn in (("league_state.sqlite", league), ("player_pool.sqlite", pool)):
                destination = sqlite3.connect(backups / name)
                try:
                    conn.backup(destination)
                finally:
                    destination.close()
            backup_conn = connect(backups / "league_state.sqlite")
            try:
                if snapshot_digest(backup_conn, snapshot_id) != audit["database_digest_sha256"]:
                    raise RuntimeError("SQLite archive backup does not match the audited snapshot")
            finally:
                backup_conn.close()
            archive = ARCHIVES / f"{batch_id}.zip"
            archive_tmp = archive.with_suffix(".zip.tmp")
            with zipfile.ZipFile(archive_tmp, "w", compression=zipfile.ZIP_DEFLATED) as target:
                for database in backups.iterdir():
                    target.write(database, database.name)
                target.write(source_manifest_path, "ingest_manifest.json")
                target.writestr("context.json", json.dumps(context, ensure_ascii=False))
                target.writestr("audit.json", json.dumps(audit, ensure_ascii=False))
            os.replace(archive_tmp, archive)
            files = {path.relative_to(bundle).as_posix(): {"sha256": file_sha256(str(path)), "bytes": path.stat().st_size}
                     for path in sorted(bundle.rglob("*")) if path.is_file()}
            if max(item["bytes"] for item in files.values()) > 900_000:
                raise RuntimeError("A web reading file exceeded the 900 KB size limit")
            manifest = {"schema_version": 1, "batch_id": batch_id, "save_id": save_id, "snapshot_id": snapshot_id,
                        "captured_at_utc": source_manifest["timestamp"], "exported_at_utc": datetime.now(timezone.utc).isoformat(),
                        "context": context, "gm_decisions_allowed": context["purpose"] == "production",
                        "audit_verdict": "PASS_VERIFIED", "audit_check_count": len(audit["checks"]), "counts": counts,
                        "source_binding": {"snapshot_digest_sha256": audit["database_digest_sha256"], "ingest_manifest_sha256": source_manifest_hash,
                                           "player_pool_sha256": source_pool_hash, "exporter_source_sha256": file_sha256(__file__)},
                        "archive": {"filename": archive.name, "sha256": file_sha256(str(archive)), "bytes": archive.stat().st_size, "release_tag": f"data-{batch_id}"},
                        "files": files, "null_policy": "UNOBSERVED_IS_NULL_NOT_ZERO", "game_write_policy": "PLAYER_APPROVAL_REQUIRED",
                        "reader_contract": "Resolve latest once, pin the containing Git commit, and read every file from that commit and batch."}
            write(bundle / "manifest.json", manifest)
            verify_bundle(bundle)
            # Reject a concurrent recapture before changing the visible pointer.
            if file_sha256(paths["player_pool_db_path"]) != source_pool_hash or file_sha256(str(source_manifest_path)) != source_manifest_hash or snapshot_digest(league, snapshot_id) != audit["database_digest_sha256"]:
                raise RuntimeError("Sources changed during export; latest remains unchanged")
            final_dir.parent.mkdir(parents=True, exist_ok=True)
            os.replace(bundle, final_dir)
        pointer = {"save_id": save_id, "batch_id": batch_id, "batch_path": final_dir.relative_to(PUBLISHED).as_posix(),
                   "manifest_sha256": file_sha256(str(final_dir / "manifest.json")), "game_date": context.get("game_date"), "purpose": context["purpose"]}
        write(pointer_path, pointer)
        index_path = PUBLISHED / "index.json"
        index = load(index_path) if index_path.exists() else {"schema_version": 1, "careers": {}}
        index["careers"][save_id] = {"latest": pointer_path.relative_to(PUBLISHED).as_posix(), "game_date": context.get("game_date"), "purpose": context["purpose"]}
        write(index_path, index)
        print(f"[PASS] Exported {batch_id}: {counts}; archive={archive.name}")
        return manifest
    finally:
        league.close()
        pool.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--save-id", required=True)
    parser.add_argument("--snapshot", required=True)
    args = parser.parse_args()
    export_snapshot(args.save_id, args.snapshot)
