"""Publish only a verified career reading bundle to the configured private repo.

Normal pushes only. No force pushes, credentials, external decision execution,
or unrelated staged/source changes are accepted by this data-only publisher.
"""
import argparse
import base64
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from snapshot_integrity import file_sha256, write_json_atomic
from verify_web_export import verify


def command(args, check=True):
    result = subprocess.run(args, cwd=ROOT, text=True, encoding="utf-8", errors="replace", capture_output=True)
    if check and result.returncode:
        raise RuntimeError(f"{args[0]} {args[1]} failed: {result.stderr[-1200:]}")
    return result


def github_file(repository, path, commit):
    response = command(["gh", "api", f"repos/{repository}/contents/{path}?ref={commit}"])
    return base64.b64decode(json.loads(response.stdout)["content"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--save-id", required=True)
    args = parser.parse_args()
    manifest = verify(args.save_id)
    config = json.loads((ROOT / "config/github_sync.json").read_text(encoding="utf-8"))
    repository, branch = config["repository"], config["branch"]
    remote = json.loads(command(["gh", "repo", "view", repository, "--json", "nameWithOwner,isPrivate,url"]).stdout)
    if remote["nameWithOwner"].casefold() != repository.casefold() or not remote["isPrivate"]:
        raise RuntimeError("Destination is not the configured private repository")
    origin = command(["git", "remote", "get-url", "origin"]).stdout.strip().removesuffix(".git")
    if origin not in (f"git@github.com:{repository}", f"https://github.com/{repository}"):
        raise RuntimeError("Git origin does not match the configured repository")
    if command(["git", "branch", "--show-current"]).stdout.strip() != branch:
        raise RuntimeError("Data publication must run from the configured branch")
    allowed = (f"published/saves/{args.save_id}/", "published/index.json")
    def allowed_path(path):
        return path == allowed[1] or path.startswith(allowed[0])
    staged = command(["git", "diff", "--cached", "--name-only"]).stdout.splitlines()
    if any(not allowed_path(path) for path in staged):
        raise RuntimeError("Unrelated files are staged; data publisher will not commit them")
    dirty_source = command(["git", "diff", "--name-only", "--", "src", "scripts", "config"]).stdout.splitlines()
    if dirty_source:
        raise RuntimeError("Capture/export source or configuration differs from the committed version")
    command(["git", "fetch", "origin", branch])
    command(["git", "merge-base", "--is-ancestor", f"origin/{branch}", "HEAD"])
    unpublished = command(["git", "diff", "--name-only", f"origin/{branch}..HEAD"]).stdout.splitlines()
    if any(not allowed_path(path) for path in unpublished):
        raise RuntimeError("Unpublished source changes require separate review before a data-only push")
    pending = command(["git", "diff", "--name-only", "--", "published"]).stdout.splitlines()
    pending += command(["git", "ls-files", "--others", "--exclude-standard", "--", "published"]).stdout.splitlines()
    if any(not allowed_path(path) for path in pending):
        raise RuntimeError("Another career or reading-protocol update is pending; refusing a mixed publication")
    command(["git", "add", "--", allowed[0].rstrip("/"), allowed[1]])
    changed = command(["git", "diff", "--cached", "--quiet"], check=False)
    if changed.returncode == 1:
        command(["git", "commit", "-m", f"data: publish {manifest['batch_id']}"])
    elif changed.returncode:
        raise RuntimeError("Could not inspect staged data changes")
    command(["git", "push", "origin", f"HEAD:{branch}"])
    commit = command(["git", "rev-parse", "HEAD"]).stdout.strip()
    archive = ROOT / "_exports/archives" / manifest["archive"]["filename"]
    tag = manifest["archive"]["release_tag"]
    release = command(["gh", "release", "view", tag, "--repo", repository, "--json", "url"], check=False)
    if release.returncode:
        with tempfile.TemporaryDirectory(prefix="gm_release_notes_") as temporary:
            notes = Path(temporary) / "notes.md"
            notes.write_text(f"Verified player-triggered capture for {manifest['save_id']} at game date {manifest['context'].get('game_date')}.\n\n"
                             f"Snapshot: `{manifest['snapshot_id']}`\nCommit: `{commit}`\nArchive SHA-256: `{manifest['archive']['sha256']}`\n\n"
                             "SQLite backups are for reproducibility. Web GMs read the small JSON files under published/. Unobserved fields remain null.\n", encoding="utf-8")
            command(["gh", "release", "create", tag, str(archive), "--repo", repository, "--target", commit,
                     "--title", f"Verified data {manifest['context'].get('game_date')} / {manifest['batch_id']}", "--notes-file", str(notes)])
    pointer_path = f"published/saves/{args.save_id}/latest.json"
    pointer_bytes = github_file(repository, pointer_path, commit)
    local_pointer = (ROOT / pointer_path).read_bytes()
    if pointer_bytes != local_pointer:
        raise RuntimeError("GitHub pointer differs from the local verified bytes")
    pointer = json.loads(pointer_bytes)
    remote_manifest = github_file(repository, "published/" + pointer["batch_path"] + "/manifest.json", commit)
    import hashlib
    if hashlib.sha256(remote_manifest).hexdigest() != pointer["manifest_sha256"]:
        raise RuntimeError("GitHub manifest does not match the committed pointer")
    with tempfile.TemporaryDirectory(prefix="gm_release_verify_") as temporary:
        command(["gh", "release", "download", tag, "--repo", repository, "--pattern", archive.name, "--dir", temporary])
        if file_sha256(str(Path(temporary) / archive.name)) != manifest["archive"]["sha256"]:
            raise RuntimeError("Downloaded GitHub database archive hash mismatch")
    receipt = {"repository": repository, "visibility": "private", "commit": commit, "batch_id": manifest["batch_id"],
               "game_date": manifest["context"].get("game_date"), "remote_pointer_and_manifest_verified": True,
               "downloaded_database_archive_verified": True, "verified_at_utc": datetime.now(timezone.utc).isoformat(),
               "entry_url": f"https://github.com/{repository}/blob/{commit}/{pointer_path}",
               "release_url": f"https://github.com/{repository}/releases/tag/{tag}",
               "chatgpt_web_connection_verified": False}
    write_json_atomic(str(ROOT / "_exports/receipts" / f"{manifest['batch_id']}.json"), receipt)
    print(json.dumps(receipt, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
