"""The single real run of RQ2 and RQ3 (PREREGISTRATION.md D13). Run once, after FREEZE.json is committed:

    python research/fashion/run_frozen.py

Refuses to start unless the frozen hashes match and the git tree is clean (outcomes.require_frozen). Every attempt is
appended to output/frozen_run/attempts.jsonl before any real data is touched, and a failure records its traceback there,
so an attempt can never go unrecorded. A second run needs --rerun-reason (D13: a bug found afterwards is fixed, rerun,
both reported, and logged). Order: RQ2 confirmatory + supplementary (real labels), then the real acceptance outcomes,
RQ3 confirmatory + supplementary, then the planned exploratory analyses. Results are written only after everything has
run; output/frozen_run/ is committed immediately.
"""
from __future__ import annotations

import argparse
import json
import platform
import subprocess
import sys
import traceback
from datetime import datetime, timezone

import matplotlib
import scipy

import numpy as np
import pandas as pd

import exploratory
import outcomes
import panel
import rq2_following as rq2
import rq3_reward as rq3
from common import OUTPUT, ROOT

OUT = OUTPUT / "frozen_run"


def clean(o):
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


def equivalence_table(verdicts: dict, mde: dict) -> list[dict]:
    """E9: TOST and MDE80 for every hypothesis that is not supported."""
    return [{"hypothesis": h, "verdict": v["verdict"], "coef": v["coef"], "ci90": v["ci90"], "sesoi": v["sesoi"],
             "tost_p": v["tost_p"], "mde80": mde.get(h)} for h, v in verdicts.items() if v["verdict"] != "supported"]


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rerun-reason", help="required if output/frozen_run/ already holds an attempt")
    a = p.parse_args()
    started = now()
    freeze = outcomes.require_frozen()
    log = OUT / "attempts.jsonl"
    previous = [json.loads(line) for line in log.open()] if log.exists() else []
    if previous and not a.rerun_reason:
        raise SystemExit(f"{len(previous)} earlier attempt(s) recorded in {log}; a rerun needs --rerun-reason")
    OUT.mkdir(parents=True, exist_ok=True)
    attempt = {"attempt": len(previous) + 1, "started_utc": started, "freeze_sha256": outcomes.sha256(outcomes.FREEZE),
               "rerun_reason": a.rerun_reason}
    with log.open("a") as f:
        f.write(json.dumps({**attempt, "status": "started"}) + "\n")
    try:
        run(freeze, started)
    except BaseException:
        with log.open("a") as f:
            f.write(json.dumps({**attempt, "status": "failed", "at_utc": now(), "traceback": traceback.format_exc()}) + "\n")
        raise
    with log.open("a") as f:
        f.write(json.dumps({**attempt, "status": "finished", "at_utc": now()}) + "\n")


def run(freeze: dict, started: str) -> None:
    gate_file = json.loads((OUTPUT / "h2d_validation.json").read_text())
    gate = gate_file["gate"] == "pass"
    assert gate == freeze["h2d_gate_passed"], "gate differs from the frozen value"
    tau = json.loads((OUTPUT / "resubmission_tau.json").read_text())["tau"]
    assert tau == freeze["tau"], "tau differs from the frozen value"
    variables = json.loads((OUTPUT / "checks" / "variables.json").read_text())
    assert variables["s4_available"], "paper_variables.csv.gz was built before tau was applied"

    frames = {m: panel.frame(m) for m in panel.MAPS}
    assert frames["k100"].has_earlier_version.notna().all(), "earlier_versions.csv.gz has no probable_earlier_version"
    res2 = rq2.run(frames, gate)
    out = outcomes.load("real", frames["k100"].submission_id)
    res3 = rq3.run(frames, out, gate, describe=True)
    exp = exploratory.run(frames, out, gate)
    finished = now()

    res2["rows"].to_csv(OUT / "rq2_results.csv", index=False)
    res3["rows"].to_csv(OUT / "rq3_results.csv", index=False)
    exp["estimates"].to_csv(OUT / "exploratory_estimates.csv", index=False)
    exp["acceptance_by_class_year"].to_csv(OUT / "acceptance_by_class_year.csv", index=False)
    exp["dose_response"].to_csv(OUT / "dose_response.csv", index=False)
    mde = freeze.get("mde80", {})
    summary = {
        "rq2": {"family": res2["family"], "verdicts": res2["verdicts"], "label_reliability": res2["label_reliability"]},
        "rq3": {"family": res3["family"], "verdicts": res3["verdicts"], "counts": res3["counts"]},
        "h2d_gate": gate_file, "tau": tau,
        "e9_equivalence": equivalence_table({**res2["verdicts"], **res3["verdicts"]}, mde),
        "dropped_hypotheses": [] if gate else ["H2d", "H3c"],
        "exploratory_caveat": sorted(set(exp["estimates"].loc[exp["estimates"].measure_status != "", "label"])),
    }
    (OUT / "summary.json").write_text(json.dumps(clean(summary), indent=2) + "\n")
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    info = {"started_utc": started, "finished_utc": finished, "git_head": head,
            "freeze_sha256": outcomes.sha256(outcomes.FREEZE), "python": sys.version.split()[0],
            "numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__,
            "matplotlib": matplotlib.__version__, "platform": platform.platform()}
    (OUT / "run_info.json").write_text(json.dumps(info, indent=2) + "\n")
    for part in ("rq2", "rq3"):
        for h, v in summary[part]["verdicts"].items():
            print(f"{h} {v['outcome']:12s} ~ {v['regressor']:18s} coef {v['coef']:+.4f} CI95 [{v['ci95'][0]:+.4f}, "
                  f"{v['ci95'][1]:+.4f}] p_holm {v['p_holm']:.3g} robust {v['robustness_same_sign']:.0%} "
                  f"hindsight {'ok' if v['hindsight_variants_same_sign'] else 'FAIL'} -> {v['verdict']}"
                  f"{' (fragile)' if v['fragile'] else ''}")


if __name__ == "__main__":
    main()
