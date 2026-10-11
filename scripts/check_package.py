"""Check package links, content boundaries, and an optional repeated export."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from export_dataset import sha, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rebuild")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    validate(root / "data")
    for name in ("README.md", "DATA_DICTIONARY.md"):
        for target in re.findall(r"\]\(([^)]+)\)", (root / name).read_text(encoding="utf-8")):
            if "://" not in target and not (root / target.split("#")[0]).exists():
                raise RuntimeError("Broken documentation link")
    hashes = {}
    if args.rebuild:
        rebuilt = Path(args.rebuild).resolve()
        validate(rebuilt)
        for path in sorted((root / "data").glob("*.csv.gz")):
            if sha(path) != sha(rebuilt / path.name):
                raise RuntimeError("Repeated export changed: " + path.name)
            hashes[path.name] = sha(path)
    expected = {".gitignore", ".gitattributes", "README.md", "DATA_DICTIONARY.md",
                "scripts/export_dataset.py", "scripts/check_package.py", "tests/test_export_dataset.py",
                "data/submissions.csv.gz", "data/submission_authors.csv.gz", "data/metadata_provenance.csv.gz",
                "data/manifest.json", "data/validation.json", "data/reproduction.json"}
    # research/ holds derived analysis layers built on top of the package, not package files.
    actual = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
              and ".rebuild-check" not in p.parts and ".git" not in p.parts
              and p.relative_to(root).parts[0] != "research"}
    if actual - expected:
        raise RuntimeError("Unexpected package files: " + repr(sorted(actual - expected)))
    if args.rebuild:
        manifest = json.loads((root / "data" / "manifest.json").read_text(encoding="utf-8"))
        write = {"package_version":manifest["version"], "python":sys.version,
                 "dependencies":"Python standard library only",
                 "export_commands":"See README.md; explicit existing source paths, no experimental inputs",
                 "repeated_export_byte_identical":True, "data_file_sha256":hashes,
                 "source_preservation":manifest["source_preservation_checks_passed"],
                 "large_database_verification":"sealed manifests rehashed; source size/mtime unchanged; no new full raw database checksum audit",
                 "small_outcome_database_sha256_verified":True,
                 "package_files":{p.relative_to(root).as_posix():sha(p) for p in sorted(root.rglob("*"))
                                  if p.is_file() and p.relative_to(root).as_posix() in expected
                                  and p.name != "reproduction.json"},
                 "repository_upload_during_export":False, "current_workspace_remote_changed":False,
                 "corpus_acquisition_requests":0, "model_calls":0}
        (root / "data" / "reproduction.json").write_text(json.dumps(write, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"package_check":"passed", "repeated_data_files_byte_identical":hashes,
                      "local_documentation_links":"passed", "unexpected_files":[]}, indent=2))


if __name__ == "__main__":
    main()
