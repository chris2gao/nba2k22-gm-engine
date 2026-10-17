"""v1 describes constraints and observed salaries; v2 negotiation is deferred."""
from .calculations import salary_exchange, result
from .coverage import player_value
from .models import module_result


def player_valuation(player):
    fields = ("overall_rating", "age", "potential", "salary_current_year", "contract_years_left")
    missing = [key for key in fields if player.get(key) is None]
    return result(reason="MISSING_OBSERVED_FIELDS: " + ",".join(missing) if missing else "VALUATION_MODEL_DEFERRED_V2",
                  inputs={key: player.get(key) for key in fields})


def constraints(data, assets):
    errors = []
    missing = []
    seen = set()
    for asset in assets:
        identity = (asset.get("kind"), asset.get("asset_id"))
        if not identity[1]:
            errors.append("ASSET_ID_REQUIRED")
        elif identity in seen:
            errors.append("DUPLICATE_ASSET")
        seen.add(identity)
        if str(asset.get("player_name", "")).casefold().strip() in {name.casefold().strip() for name in data.gm_policy["protected_player_names"]}:
            errors.append("PROTECTED_PLAYER")
        if asset.get("kind") == "draft_pick" and not asset.get("observed_owner"):
            missing.append("DRAFT_PICK_OWNERSHIP_UNKNOWN")
    return {"legality": "ILLEGAL" if errors else "UNKNOWN", "errors": errors,
            "missing_data": missing + ["完整实际合同/签约权/例外/选秀权权属/游戏交易规则；v2 法律模型未启用"],
            "executable": False, "approval_status": "NOT_GRANTED"}


def analyze(data, team):
    salaries = [player_value(data, player, "salary_current_year") for player in team["roster"]]
    return module_result("trades", {"observed_player_salaries": salaries or None},
        ["可以讨论需求或询价；本模块不自动撮合、不估造 OVR，不把主观动机当成成交或合法性。"],
        ["球员完整能力/年龄/潜力、选秀资产和完整 CBA 账本"],
        ["由双方独立表达利益，正式方案待数据补齐并由玩家批准。"])


def exchange(outgoing, incoming):
    return salary_exchange(outgoing, incoming)
