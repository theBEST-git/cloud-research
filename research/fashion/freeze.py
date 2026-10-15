"""Write FREEZE.json (PREREGISTRATION.md D13): sha256 of every file the real run reads or executes, plus the frozen
settings (gate, tau, variant lists, SESOIs, MDE80 and the dry-run criteria). Commit it before run_frozen.py.

    python research/fashion/freeze.py --created 2026-10-15T00:00:00Z
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import outcomes
import rq2_following as rq2
import rq3_reward as rq3
import variants
from common import OUTPUT, ROOT

HERE = Path(__file__).resolve().parent
INPUTS = [
    str(outcomes.SOURCE.relative_to(ROOT)), "data/submission_authors.csv.gz",
    "research/topics/common.py",
    "research/topics/output/topic_assignments.csv.gz", "research/topics/output/k_sensitivity_assignments.csv.gz",
    "research/topics/output/hindsight_assignments.csv.gz", "research/topics/output/paper_contributions.csv.gz",
    "research/topics/output/paper_topic_stability.csv.gz", "research/topics/output/topic_catalog.csv",
    "research/topics/output/keyword_types.csv",
    "research/topics/annotation/contribution_types/pilot_gold_facets.csv",
    "research/topics/annotation/contribution_types/training/training_labels.csv",
    "research/fashion/PREREGISTRATION.md",
]
OUTPUTS = ["topic_year_maturity.csv.gz", "paper_variables.csv.gz", "paper_buzzword.csv.gz", "earlier_versions.csv.gz",
           "keyword_uses.csv.gz", "keyword_year.csv.gz", "h2d_validation.json", "resubmission_tau.json",
           "specter2_centring_mean.npy", "checks/variables.json", "rq1_results.csv", "dryrun/summary.json"]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--created", required=True)
    a = p.parse_args()
    code = sorted(str(f.relative_to(ROOT)) for f in HERE.rglob("*") if f.suffix in {".py", ".js"}
                  and not {"__pycache__", "output"} & set(f.relative_to(HERE).parts))
    files = code + INPUTS + [f"research/fashion/output/{o}" for o in OUTPUTS]
    dry = json.loads((OUTPUT / "dryrun" / "summary.json").read_text())
    gate = json.loads((OUTPUT / "h2d_validation.json").read_text())
    tau = json.loads((OUTPUT / "resubmission_tau.json").read_text())
    freeze = {
        "created_utc": a.created,
        "h2d_gate_passed": gate["gate"] == "pass",
        "tau": tau["tau"],
        "families": {"rq2": [s.hid for s in rq2.SPECS if not s.gated or gate["gate"] == "pass"],
                     "rq3": [s.hid for s in rq3.SPECS if not s.gated or gate["gate"] == "pass"]},
        "sesoi": {s.hid: s.sesoi for s in rq2.SPECS + rq3.SPECS},
        "counted_variants": {"rq2": list(variants.counted(2)), "rq3": list(variants.counted(3))},
        "hindsight_variants": list(variants.HINDSIGHT_VARIANTS), "robust_share": variants.ROBUST_SHARE,
        "mde80": dry["mde80"], "dryrun_criteria": dry["criteria"],
        "sha256": {f: outcomes.sha256(ROOT / f) for f in files},
    }
    (HERE / "FREEZE.json").write_text(json.dumps(freeze, indent=2) + "\n")
    print(f"FREEZE.json: {len(files)} files hashed; gate {'pass' if freeze['h2d_gate_passed'] else 'fail'}; tau {freeze['tau']}")


if __name__ == "__main__":
    main()
