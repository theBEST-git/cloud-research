"""Write FREEZE_CONFIRMATION.json (POOLED_SPEC D6; PREREGISTRATION.md "Confirmation" and the confirmation registrations):
the frozen discovery settings (FREEZE.json, copied verbatim), the confirmation registration (run_confirmation.REGISTERED,
and ph5_confirm.REGISTERED as registered_ph5) and the sha256 of every file the confirmation run reads or executes.
Commit it, then run run_confirmation.py once: outcomes.require_frozen refuses that run unless every hash below still
matches and the git tree is clean.

Hashed (paths relative to the repository root):
- code: every .py / .js under research/fashion (output directories and caches excluded) and
  research/topics/{common, assign_topics, released, keyword_map, pooled_topics}.py;
- research/fashion/PREREGISTRATION.md and the discovery FREEZE.json;
- both sealed tables (outcomes.sealed_files_all) and both author tables (data/, data_confirmation_csv/);
- the git-ignored SPECTER2 caches the pooled layer reads (specter2.npy, specter2_ids.csv and every specter2_released*
  file), which the clean-tree check cannot see;
- every file under research/topics/output_pooled and research/fashion/output_pooled, the git-ignored pooled author table
  included, except output_pooled/confirmation_run/ (the run's own outputs);
- the label references of rq2_following.label_reliability, and the discovery files the pooled build reuses or the
  registration rests on (output/h2d_validation.json, resubmission_tau.json, specter2_centring_mean.npy,
  output/frozen_run/summary.json, and the discovery window premia output/posthoc/ph5_premia/windows.csv that the PH5
  premia tests use as fixed predictions).
Refuses if a confirmation attempt exists, if the PH5 module (ph5_confirm.py) is missing, if a required file is
missing, if a pooled copy of the three discovery constants differs from its FREEZE.json hash, or if the pooled author
table differs from its manifest
(output_pooled/pooled_inputs.json). The confirmation dry-run's MDE80 (output_pooled/confirmation_dryrun/mde.json), if
present, is recorded as confirmation_mde80 (run_confirmation reports it with the verdicts).

    python research/fashion/freeze_confirmation.py --created 2026-10-18T00:00:00Z
"""
from __future__ import annotations

import argparse
import importlib
import json
from pathlib import Path

import outcomes
from build_pooled_inputs import AUTHORS, COPIES, MANIFEST
from common import DISCOVERY_OUTPUT, POOLED_OUTPUT, ROOT
from run_confirmation import DRY, OUT, REGISTERED, ph5_available

HERE = Path(__file__).resolve().parent
TARGET = outcomes.FREEZE_CONFIRMATION
TOPICS_DIR = ROOT / "research" / "topics"
POOLED_TOPICS = TOPICS_DIR / "output_pooled"
CACHE = TOPICS_DIR / "cache"
TOPIC_CODE = ["common.py", "assign_topics.py", "released.py", "keyword_map.py", "pooled_topics.py"]
AUTHOR_TABLES = [ROOT / "data" / "submission_authors.csv.gz", ROOT / "data_confirmation_csv" / "submission_authors.csv.gz"]
REFERENCES = [TOPICS_DIR / "annotation" / "contribution_types" / "pilot_gold_facets.csv",
              TOPICS_DIR / "annotation" / "contribution_types" / "training" / "training_labels.csv"]
DISCOVERY_RECORDS = ([DISCOVERY_OUTPUT / c for c in COPIES] + [DISCOVERY_OUTPUT / "frozen_run" / "summary.json"]
                     + [DISCOVERY_OUTPUT / "posthoc" / "ph5_premia" / "windows.csv"])


def under(root: Path, skip: set[str] = frozenset()) -> list[Path]:
    """Every file below root (none if it does not exist), without __pycache__ and the top-level directories in skip."""
    if not root.exists():
        return []
    return sorted(f for f in root.rglob("*") if f.is_file() and "__pycache__" not in f.parts
                  and f.relative_to(root).parts[0] not in skip)


def code_files() -> list[Path]:
    return sorted(f for f in HERE.rglob("*") if f.suffix in {".py", ".js"} and f.is_file()
                  and not any(p == "__pycache__" or p.startswith("output") for p in f.relative_to(HERE).parts))


def files() -> list[Path]:
    """Every file FREEZE_CONFIRMATION.json hashes (existence is checked by main)."""
    caches = [CACHE / "specter2.npy", CACHE / "specter2_ids.csv",
              *sorted(f for f in CACHE.glob("specter2_released*") if f.is_file())]
    out = (code_files() + [TOPICS_DIR / c for c in TOPIC_CODE] + [HERE / "PREREGISTRATION.md", outcomes.FREEZE_DISCOVERY]
           + outcomes.sealed_files_all() + AUTHOR_TABLES + caches + REFERENCES + DISCOVERY_RECORDS
           + under(POOLED_TOPICS) + under(POOLED_OUTPUT, {OUT.name}))
    return sorted(set(out))


def check_pooled_inputs(frozen: dict) -> None:
    """The pooled copies of the frozen discovery constants equal their FREEZE.json hashes (D15), and the git-ignored
    pooled author table is the one build_pooled_inputs.py recorded."""
    for name in COPIES:
        rel = str((DISCOVERY_OUTPUT / name).relative_to(ROOT))
        if not (POOLED_OUTPUT / name).exists() or outcomes.sha256(POOLED_OUTPUT / name) != frozen["sha256"][rel]:
            raise SystemExit(f"output_pooled/{name} is missing or differs from the frozen {rel}")
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    if not AUTHORS.exists() or manifest.get("authors", {}).get("sha256") != outcomes.sha256(AUTHORS):
        raise SystemExit("the pooled author table is missing or differs from output_pooled/pooled_inputs.json")


def confirmation_mde() -> dict | None:
    path = DRY / "mde.json"
    if not path.exists():
        return None
    mde = json.loads(path.read_text())
    return {"mde80": mde["mde80"], "source": str(path.relative_to(ROOT)), "sha256": outcomes.sha256(path),
            "reps": {h: v["reps"] for h, v in mde["by_test"].items()}}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--created", required=True)
    a = p.parse_args()
    if outcomes.CONFIRMATION_ATTEMPTS.exists():
        raise SystemExit(f"{outcomes.CONFIRMATION_ATTEMPTS} exists: the confirmation run has been attempted, refusing to freeze")
    if TARGET == outcomes.FREEZE_DISCOVERY:
        raise SystemExit("refusing to overwrite FREEZE.json")
    if not ph5_available():
        raise SystemExit("ph5_confirm.py is missing: the confirmation run needs the PH5 module, refusing to freeze")
    discovery = json.loads(outcomes.FREEZE_DISCOVERY.read_text())
    paths = files()
    missing = [str(f) for f in paths if not f.exists()]
    if missing or not under(POOLED_TOPICS) or not under(POOLED_OUTPUT, {OUT.name}):
        raise SystemExit("refusing to freeze; missing:\n- " + "\n- ".join(missing or ["research/topics/output_pooled or "
                                                                                  "research/fashion/output_pooled"]))
    check_pooled_inputs(discovery)
    rel = lambda f: str(f.relative_to(ROOT))
    freeze = {
        "created_utc": a.created, "discovery_created_utc": discovery["created_utc"],
        "discovery_freeze_sha256": outcomes.sha256(outcomes.FREEZE_DISCOVERY),
        **{k: v for k, v in discovery.items() if k not in ("sha256", "created_utc")},
        "registered": REGISTERED,
        "registered_ph5": importlib.import_module("ph5_confirm").REGISTERED,
        "confirmation_mde80": confirmation_mde(),
        "ph5_hook_present": True,
        "note": "mde80, dryrun_criteria and stress_t_inflation above are discovery-design quantities (FREEZE.json)",
        "sha256": {rel(f): outcomes.sha256(f) for f in paths},
    }
    TARGET.write_text(json.dumps(freeze, indent=2) + "\n")
    print(f"{TARGET.name}: {len(paths)} files hashed; gate {'pass' if freeze['h2d_gate_passed'] else 'fail'}; "
          f"tau {freeze['tau']}; confirmation MDE80 {'recorded' if freeze['confirmation_mde80'] else 'not computed'}; "
          f"PH5 hook {'present' if freeze['ph5_hook_present'] else 'absent'}")


if __name__ == "__main__":
    main()
