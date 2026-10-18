from .coverage import assess
from .models import module_result


def check_field(policy, field, value):
    from coach_codec import load_profile, validate_value
    definition=load_profile()["fields"].get(field)
    if not definition or field.startswith("poe_"):
        return {"valid":False,"reason":"LEGACY_OR_UNKNOWN_TACTICAL_FIELD","execution_ready":False}
    try:
        validate_value(definition,value)
    except ValueError as exc:
        return {"valid":False,"reason":str(exc),"execution_ready":False}
    return {"valid":True,"reason":None,"execution_ready":False,
            "enum_status":definition["readiness"],"snapshot_validation_required":True}


def analyze(data, team, side):
    availability = assess(data, team, side)
    missing = availability["missing_data"] + ["阵容角色、轮换、比赛效率和对手表现，尚不足以确认战术优劣"]
    if side == "defense":
        missing.append("历史 TEAM POE 语义已撤销；请另附 coaching_snapshot 与原生字段提案")
    return module_result(side, availability["values"],
                         ["历史 poe_* 只保留原始观测，不作为教练战术事实。"], missing,
                         ["由 GM 用实测阵容与表现讨论方向；数值提案只能引用已登记枚举，执行另行验收。"])
