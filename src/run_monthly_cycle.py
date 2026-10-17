# -*- coding: utf-8 -*-
"""Unified, fail-closed monthly workflow: capture -> audit -> DB-only GM."""
import argparse
import os
import sqlite3
from datetime import datetime, timezone

from auto_pipeline_ingest import run_automated_ingestion
from audit_sampling import run_ai_sampling_audit
from gm_engine import GMEngine
from save_context import resolve_context
from snapshot_integrity import write_json_atomic


def _write_report(path: str, manifest: dict, audit: dict, proposals: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = [
        f"# NBA 2K22 GM 月度数据与决策报告：{manifest['snapshot_id']}",
        "",
        f"- 存档 ID：`{manifest['save_id']}`",
        f"- 入库时间 (UTC)：`{manifest['timestamp']}`",
        f"- 脚本质检：`{audit['verdict']}` | 校验项：{sum(audit['checks'].values())}/{len(audit['checks'])}",
        f"- 数据摘要：`{audit['database_digest_sha256']}`",
        f"- 球队：{manifest['ingested_counts']['teams']} 支；现役球员：{manifest['ingested_counts']['active_players']} 人；"
        f"制服组原始结构：{manifest['ingested_counts']['staff_pool_observations']} 条",
        "- 教练球队归属：未验证，因此本次未将制服组数据当作正式教练映射。",
        "- 战绩/比赛统计：仅使用内存未观测字段的 NULL 值，不以工资或 POE 推导战绩。",
        "",
        "## GM 候选建议",
        "",
        f"- 超过静态奢侈税线球队数：{proposals['financial_landscape']['luxury_tax_teams_count']}",
        f"- 工资总额低于静态工资帽的代理球队数：{proposals['financial_landscape']['below_cap_proxy_teams_count']}",
        f"- 建议状态：`{proposals['execution_policy']}`",
        "",
    ]
    trades = proposals.get("proposed_trades", [])
    if trades:
        lines.extend(["### 交易候选", ""])
        for deal in trades:
            lines.extend([
                f"- `{deal['status']}`：{deal['team_a']['abbr']} → {deal['team_b']['abbr']}，候选球员 {deal['team_a']['assets_offered'][0]['player_name']}。",
                f"  CBA 核验：未通过/未完成（`{deal['cba_validation']['rule']}`）；不可直接执行。",
            ])
    else:
        lines.extend(["本批次没有基于当前可验证字段生成交易候选。", ""])
    lines.extend([
        "",
        "## 可复核产物",
        "",
        f"- 入库清单：`{os.path.basename(manifest['artifacts']['manifest_json'])}`",
        f"- 抽样审计：`{os.path.basename(audit['artifact_path'])}`",
        f"- GM 建议 JSON：`{os.path.basename(proposals['artifact_path'])}`",
        "",
    ])
    temp_path = path + ".tmp"
    with open(temp_path, "w", encoding="utf-8") as target:
        target.write("\n".join(lines))
        target.flush()
        os.fsync(target.fileno())
    os.replace(temp_path, path)


def run_cycle(
    season_year: int = 2022,
    month_idx: int = 1,
    month_name: str = "NOV",
    notes: str = "",
    save_id: str = None,
):
    context = resolve_context(save_id)
    db_path = context["db_path"]
    os.makedirs(context["backups_dir"], exist_ok=True)
    if os.path.isfile(db_path):
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(
            context["backups_dir"],
            f"league_state_{context['save_id']}_{season_year}_M{month_idx:02d}_{timestamp}.sqlite",
        )
        source = sqlite3.connect(db_path)
        backup = sqlite3.connect(backup_path)
        try:
            source.backup(backup)
        finally:
            backup.close()
            source.close()
        print(f"[+] 数据库备份已创建: {backup_path}")

    manifest = run_automated_ingestion(
        season_year=season_year,
        month_idx=month_idx,
        month_name=month_name,
        save_id=save_id,
        db_path=db_path,
        snapshots_dir=context["snapshots_dir"],
        player_pool_db_path=context["player_pool_db_path"],
        notes=notes,
    )
    snapshot_id = manifest["snapshot_id"]
    audit = run_ai_sampling_audit(
        snapshot_id=snapshot_id,
        save_id=save_id,
        db_path=db_path,
        snapshots_dir=context["snapshots_dir"],
        player_pool_db_path=context["player_pool_db_path"],
    )
    audit_file = os.path.join(context["snapshots_dir"], f"ai_sampling_audit_{snapshot_id}.json")
    audit["artifact_path"] = audit_file

    engine = GMEngine(
        db_path=db_path,
        snapshots_dir=context["snapshots_dir"],
        player_pool_db_path=context["player_pool_db_path"],
    )
    proposals = engine.generate_gm_proposals(snapshot_id)
    proposals["artifact_path"] = os.path.join(
        context["snapshots_dir"], f"gm_decision_manifest_{snapshot_id}.json"
    )
    report_file = os.path.join(context["evaluations_dir"], f"GM_REPORT_{snapshot_id}.md")
    _write_report(report_file, manifest, audit, proposals)
    print(f"[+] 月度数据闭环完成。审计凭证: {audit_file}")
    print(f"[+] 数据库驱动 GM 建议: {proposals['artifact_path']}")
    print(f"[+] 报告: {report_file}")
    return {
        "snapshot_id": snapshot_id,
        "manifest": manifest,
        "audit": audit,
        "proposals": proposals,
        "report_file": report_file,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="采集真实数据、完成脚本抽检、输出数据库驱动 GM 建议")
    parser.add_argument("--season", type=int, default=2022)
    parser.add_argument("--month", type=int, default=1)
    parser.add_argument("--name", type=str, default="NOV")
    parser.add_argument("--notes", type=str, default="")
    parser.add_argument("--save-id", type=str, default=None, help="游戏存档 ID；省略时沿用旧共享数据库")
    args = parser.parse_args()
    run_cycle(args.season, args.month, args.name, args.notes, args.save_id)
