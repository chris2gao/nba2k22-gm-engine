"""Read published JSON only. No source hashes, databases, network or game imports."""
from datetime import date, datetime
import json
from pathlib import Path
import re
import subprocess

from .models import PublishedData, Source


def load_json(path):
    with Path(path).open(encoding="utf-8-sig") as stream:
        return json.load(stream)


def safe_child(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Path leaves its data directory")
    return path


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,95}", value):
        raise ValueError("Invalid career/run identifier")
    return value


def timestamp(value):
    if not isinstance(value, str):
        raise ValueError("A published timestamp is required")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timestamp must include its timezone")
    return parsed


def git_revision(root, relative):
    result = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%H", "--", relative],
                            capture_output=True, text=True)
    return result.stdout.strip() or None


class DataReader:
    def __init__(self, project_root):
        self.root = Path(project_root).resolve()

    def read(self, career_id, previous_data_updated_at=None):
        career_id = identifier(career_id)
        published = self.root / "published"
        entry = load_json(published / "index.json")["careers"][career_id]
        pointer_path = safe_child(published, entry["latest"])
        expected = published / "saves" / career_id / "latest.json"
        if pointer_path != expected.resolve():
            raise ValueError("Index does not select the requested career")
        pointer = load_json(pointer_path)
        if pointer.get("save_id") != career_id or pointer.get("purpose") != "production":
            raise ValueError("GM preparation requires the selected production career")
        updated = timestamp(pointer.get("data_updated_at"))
        uploaded = timestamp(pointer.get("uploaded_at"))
        if uploaded < updated:
            raise ValueError("Upload time precedes the data update")
        if pointer.get("upload_status") != "UPLOADED":
            raise ValueError("Publication has not completed")
        if previous_data_updated_at and updated < timestamp(previous_data_updated_at):
            raise ValueError("Data predates the selected previous run; use a separate branch")
        date.fromisoformat(pointer["game_date"])
        directory = safe_child(published / "saves" / career_id, Path(pointer["batch_path"]).relative_to(f"saves/{career_id}"))
        league = load_json(directory / "league.json")
        teams = {}
        for state in league["teams"]:
            abbreviation = state["team_abbr"]
            if not re.fullmatch(r"[A-Z0-9]{2,4}", abbreviation) or abbreviation in teams:
                raise ValueError("Ambiguous team identity")
            team = load_json(directory / "teams" / f"{abbreviation}.json")
            if team["identity"].get("abbreviation") != abbreviation or team["identity"].get("team_id") != state.get("team_id"):
                raise ValueError("Team identity does not match the selected published team")
            teams[abbreviation] = team
        gameplay = load_json(self.root / "config/gameplay_policy.json")
        source = Source(career_id, pointer["batch_id"], pointer["data_updated_at"], pointer["uploaded_at"],
                        pointer["game_date"], pointer.get("source_commit") or git_revision(self.root, pointer_path.relative_to(self.root).as_posix()),
                        pointer["batch_path"])
        staff_path = directory / "staff.json"
        return PublishedData(source, gameplay, load_json(self.root / "config/gm_policy.json"),
                             git_revision(self.root, "config/gameplay_policy.json"), league, teams,
                             load_json(directory / "source_coverage.json"), load_json(directory / "calculations.json"),
                             load_json(staff_path) if staff_path.exists() else {}, self.root, directory)

    def draft_catalog(self, data, year):
        catalog_root = data.batch_directory / "player_catalog"
        index = load_json(catalog_root / "index.json")
        records = []
        for relative in index["years"].get(str(year), []):
            records.extend(load_json(safe_child(data.batch_directory, relative))["records"])
        return records
