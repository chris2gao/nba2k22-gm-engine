from .coverage import assess
from .models import module_result


def check_field(policy, field, value):
    definition = policy.get("tactical_enums", {}).get(field)
    if not definition or not definition.get("values"):
        return {"valid": False, "reason": "UNVERIFIED_ENUM", "execution_ready": False}
    valid = type(value) is int and value in definition["values"]
    return {"valid": valid, "reason": None if valid else "OUTSIDE_DOCUMENTED_ENUM",
            "execution_ready": False, "enum_status": definition["status"]}


def analyze(data, team, side):
    availability = assess(data, team, side)
    missing = availability["missing_data"] + ["阵容角色、轮换、比赛效率和对手表现，尚不足以确认战术优劣"]
    if side == "defense":
        missing.append("poe_on_ball 的完整语义枚举未验证；旧 0–4 注释与实测 7 冲突，禁止推到 12")
    return module_result(side, availability["values"],
                         ["当前 POE 只作为已观测设置，不按薪资自动增加压迫或改变体系。"], missing,
                         ["由 GM 用实测阵容与表现讨论方向；数值提案只能引用已登记枚举，执行另行验收。"])
