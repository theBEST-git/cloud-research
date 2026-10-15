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
    *[str(f.relative_to(ROOT)) for f in outcomes.sealed_files()], "data/submission_authors.csv.gz",
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
           "specter2_centring_mean.npy", "checks/variables.json", "rq1_results.csv", "dryrun/summary.json",
           "dryrun/provenance.json"]


def check_dryrun(dry: dict, families: dict) -> list[str]:
    """The dry-run must come from the current code and inputs, cover every family hypothesis, and pass (a) and (b)."""
    import dryrun
    problems = []
    if dry.get("code_digest") != dryrun.digest()["combined"]:
        problems.append("dry-run digest differs from the current code/inputs: rerun dryrun.py")
    for h in families["rq2"] + families["rq3"]:
        if dry["mde80"].get(h, "missing") == "missing":
            problems.append(f"no power curve for {h}")
    if not dry["criteria"]["a_size_within_2_8pct"]:
        problems.append(f"size criterion (a) failed: {dry['criteria']['a_size_violations']}")
    if not dry["criteria"]["b_false_support_at_most_5pct"]:
        problems.append("false-support criterion (b) failed")
    return problems


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--created", required=True)
    p.add_argument("--remedy", action="append", default=[],
                   help="a registered remedy (D16) applied for a failed dry-run criterion; recorded in FREEZE.json")
    a = p.parse_args()
    code = sorted(str(f.relative_to(ROOT)) for f in HERE.rglob("*") if f.suffix in {".py", ".js"}
                  and not {"__pycache__", "output"} & set(f.relative_to(HERE).parts))
    files = code + INPUTS + [f"research/fashion/output/{o}" for o in OUTPUTS]
    dry = json.loads((OUTPUT / "dryrun" / "summary.json").read_text())
    gate = json.loads((OUTPUT / "h2d_validation.json").read_text())
    tau = json.loads((OUTPUT / "resubmission_tau.json").read_text())
    families = {"rq2": [s.hid for s in rq2.SPECS if not s.gated or gate["gate"] == "pass"],
                "rq3": [s.hid for s in rq3.SPECS if not s.gated or gate["gate"] == "pass"]}
    problems = check_dryrun(dry, families)
    if problems and not a.remedy:
        raise SystemExit("refusing to freeze:\n- " + "\n- ".join(problems))
    prov = json.loads((OUTPUT / "dryrun" / "provenance.json").read_text())
    freeze = {
        "created_utc": a.created,
        "dryrun_problems": problems, "remedies": a.remedy,
        "h2d_gate_passed": gate["gate"] == "pass",
        "tau": tau["tau"],
        "families": families,
        "sesoi": {s.hid: s.sesoi for s in rq2.SPECS + rq3.SPECS},
        "counted_variants": {"rq2": list(variants.counted(2)), "rq3": list(variants.counted(3))},
        "hindsight_variants": list(variants.HINDSIGHT_VARIANTS), "robust_share": variants.ROBUST_SHARE,
        "mde80": dry["mde80"], "mde80_rq3_lo_variance": dry["mde80_lo"], "dryrun_criteria": dry["criteria"],
        "dryrun_dgp": {"rq2_calibrated": prov["calibrated_rq2_dgp"], "rq3": prov["rq3_dgp"],
                       "reps": prov["reps"], "power_reps": prov["power_reps"], "code_digest": dry["code_digest"]},
        "sha256": {f: outcomes.sha256(ROOT / f) for f in files},
    }
    (HERE / "FREEZE.json").write_text(json.dumps(freeze, indent=2) + "\n")
    print(f"FREEZE.json: {len(files)} files hashed; gate {'pass' if freeze['h2d_gate_passed'] else 'fail'}; tau {freeze['tau']}")


if __name__ == "__main__":
    main()
