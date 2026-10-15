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


def check_dryrun(dry: dict, prov: dict, families: dict) -> tuple[list[str], dict[str, str]]:
    """(fatal problems, remediable violations by hypothesis) under D16.

    Fatal: a dry-run not made from the current code and inputs, not at the registered replication counts, or missing a
    family hypothesis. Remediable (only by the registered wild cluster bootstrap): main-specification size above 0.08,
    or false support above 0.05. A size below 0.02 is only reported."""
    import dryrun
    fatal, remediable = [], {}
    if dry.get("code_digest") != dryrun.digest()["combined"]:
        fatal.append("dry-run digest differs from the current code/inputs: rerun dryrun.py")
    for k, v in dryrun.REGISTERED.items():
        if prov.get(k) != v:
            fatal.append(f"dry-run {k} = {prov.get(k)}, registered {v}")
    for h in families["rq2"] + families["rq3"]:
        if h not in dry["mde80"] or h not in dry["power"] and f"{h}_hi" not in dry["power"]:
            fatal.append(f"no power curve for {h}")
    for sc, sizes in dry["size"].items():
        for h, v in sizes.items():
            if v > 0.08:
                remediable[h] = remediable.get(h, "") + f" size {v} in {sc};"
    for sc, fs in dry["false_support"].items():
        for h, v in fs.items():
            if v > 0.05:
                remediable[h] = remediable.get(h, "") + f" false support {v} in {sc};"
    return fatal, remediable


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--created", required=True)
    p.add_argument("--remedy", action="append", default=[], metavar="bootstrap:<hypothesis>",
                   help="the registered remedy (D16) for a hypothesis that failed (a) upwards or (b)")
    a = p.parse_args()
    code = sorted(str(f.relative_to(ROOT)) for f in HERE.rglob("*") if f.suffix in {".py", ".js"}
                  and not {"__pycache__", "output"} & set(f.relative_to(HERE).parts))
    files = code + INPUTS + [f"research/fashion/output/{o}" for o in OUTPUTS]
    dry = json.loads((OUTPUT / "dryrun" / "summary.json").read_text())
    gate = json.loads((OUTPUT / "h2d_validation.json").read_text())
    tau = json.loads((OUTPUT / "resubmission_tau.json").read_text())
    families = {"rq2": [s.hid for s in rq2.SPECS if not s.gated or gate["gate"] == "pass"],
                "rq3": [s.hid for s in rq3.SPECS if not s.gated or gate["gate"] == "pass"]}
    prov = json.loads((OUTPUT / "dryrun" / "provenance.json").read_text())
    fatal, remediable = check_dryrun(dry, prov, families)
    if fatal:
        raise SystemExit("refusing to freeze:\n- " + "\n- ".join(fatal))
    asked = {r.split(":", 1)[1] for r in a.remedy if r.startswith("bootstrap:")}
    if len(asked) != len(a.remedy) or asked != set(remediable):
        raise SystemExit(f"remedies must be exactly bootstrap:<h> for each remediable violation {remediable}; got {a.remedy}")
    if asked:
        import analysis
        if not hasattr(analysis, "wild_cluster_bootstrap_p"):
            raise SystemExit("the registered wild cluster bootstrap is not implemented yet (D16): implement, validate, log")
    problems = [f"{h}:{v}" for h, v in remediable.items()]
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
        "mde80_note": dry.get("mde80_note", {}),
        "dryrun_dgp": {"rq2_calibrated": prov["calibrated_rq2_dgp"], "rq3": prov["rq3_dgp"], "reps": prov["reps"],
                       "power_reps": prov["power_reps"], "full_reps": prov["full_reps"], "code_digest": dry["code_digest"]},
        "sha256": {f: outcomes.sha256(ROOT / f) for f in files},
    }
    (HERE / "FREEZE.json").write_text(json.dumps(freeze, indent=2) + "\n")
    print(f"FREEZE.json: {len(files)} files hashed; gate {'pass' if freeze['h2d_gate_passed'] else 'fail'}; tau {freeze['tau']}")


if __name__ == "__main__":
    main()
