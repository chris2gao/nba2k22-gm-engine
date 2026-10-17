"""GM input semantics; not a JSON synchronization verifier."""
from .calculations import number

SOURCE_FIELDS = {
    "results": ("games_box_scores_standings", ("total_wins", "total_losses")),
    "efficiency": ("games_box_scores_standings", ("ortg", "drtg")),
    "finances": ("team_state", ("total_salary", "budget")),
    "offense": ("team_state", ("poe_off_pace", "poe_fastbreak", "poe_off_reb")),
    "defense": ("team_state", ("poe_def_reb", "poe_on_ball", "poe_off_ball", "poe_pnr_def", "poe_help_def")),
}


def source_available(data, source_id):
    sources = {entry["id"]: entry["status"] for entry in data.coverage.get("sources", [])}
    status = sources.get(source_id, "UNKNOWN")
    return status.startswith("VERIFIED") or status == "OBSERVED"


def state_value(data, team, key, source_id="team_state"):
    row = team.get("state", {})
    value = row.get(key)
    if not source_available(data, source_id) or row.get("data_source") != "LIVE_MEMORY" or value is None:
        return None
    return value


def player_value(data, player, key):
    if not source_available(data, "active_rosters_contracts") or player.get("data_source") != "LIVE_MEMORY":
        return None
    return player.get(key)


def assess(data, team, domain):
    source_id, keys = SOURCE_FIELDS[domain]
    values = {key: state_value(data, team, key, source_id) for key in keys}
    missing = [key for key, value in values.items() if not number(value)]
    return {"readiness": "READY" if not missing else ("BLOCKED" if len(missing) == len(keys) else "PARTIAL"),
            "values": values, "missing_data": missing}


def fact(value, source, field, availability="OBSERVED"):
    return {"value": value, "availability": availability if value is not None else "UNKNOWN",
            "source": source, "field": field}
