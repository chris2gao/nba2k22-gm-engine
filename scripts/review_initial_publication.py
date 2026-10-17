"""Review staged filenames/bytes without displaying candidate credential values."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent


def git(*arguments):
    result = subprocess.run(["git", *arguments], cwd=ROOT, capture_output=True, check=True)
    return result.stdout


def main():
    files = git("diff", "--cached", "--name-only", "-z").decode().strip("\0").split("\0")
    allowed_roots = {"src", "scripts", "config", "docs", "web_gm", "published"}
    allowed_files = {"README.md", "AGENTS.md", ".gitignore", ".gitattributes", "requirements.txt", "database/schema.sql", "database/templates/save_template.json"}
    suspicious, sizes = [], {}
    credential_patterns = [rb"github_pat_[A-Za-z0-9_]{25,}", rb"gh[pousr]_[A-Za-z0-9]{25,}", rb"sk-(?:proj-)?[A-Za-z0-9_-]{30,}", rb"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"]
    for name in files:
        path = Path(name)
        if name not in allowed_files and path.parts[0] not in allowed_roots:
            raise RuntimeError(f"Unexpected staged path: {name}")
        if path.suffix in {".sqlite", ".zip", ".key", ".pem", ".log"} or path.name.startswith(".env") or "__pycache__" in path.parts:
            raise RuntimeError(f"Local/private artifact incorrectly staged: {name}")
        content = git("show", f":{name}")
        sizes[name] = len(content)
        if any(re.search(pattern, content) for pattern in credential_patterns):
            suspicious.append(name)
    if suspicious:
        raise RuntimeError(f"Credential-shaped content detected; values withheld. Paths: {suspicious}")
    index = json.loads(git("show", ":published/index.json"))
    for career in index["careers"].values():
        pointer = json.loads(git("show", ":published/" + career["latest"]))
        manifest_bytes = git("show", ":published/" + pointer["batch_path"] + "/manifest.json")
        if hashlib.sha256(manifest_bytes).hexdigest() != pointer["manifest_sha256"]:
            raise RuntimeError("Git altered published manifest bytes")
        manifest = json.loads(manifest_bytes)
        for relative, metadata in manifest["files"].items():
            content = git("show", ":published/" + pointer["batch_path"] + "/" + relative)
            if len(content) != metadata["bytes"] or hashlib.sha256(content).hexdigest() != metadata["sha256"]:
                raise RuntimeError(f"Git altered published data bytes: {relative}")
    print(json.dumps({"staged_files": len(files), "staged_bytes": sum(sizes.values()), "credential_pattern_matches": 0,
                      "published_git_bytes_verified": True, "largest_file_bytes": max(sizes.values())}, indent=2))


if __name__ == "__main__":
    main()
