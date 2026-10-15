"""Score the resubmission calibration and set tau (PREREGISTRATION.md R1, D15).

Rebuilds the key with sample.draw() and checks the judged batch files. A pair is a revised version if at least 2 of 3
judges say yes. tau = the lowest bin edge at which that bin and all higher bins are >= 90% yes; if no bin qualifies,
tau = the lower edge of the top bin (exact titles are flagged either way).

    python research/fashion/annotation/resubmission_pairs/score.py
Writes research/fashion/output/resubmission_tau.json.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from sample import JUDGES, batches_for, draw  # noqa: E402
from stats import fleiss_kappa, wilson  # noqa: E402

sys.path.insert(0, str(HERE.parents[1]))
from resubmissions import TAU_BINS  # noqa: E402

OUT = HERE.parents[1] / "output" / "resubmission_tau.json"
MIN_YES = 0.90


def main() -> None:
    sample, _ = draw()
    manifest = json.loads((HERE / "manifest.json").read_text())["files"]
    for j, judge in enumerate(JUDGES):
        for b, items in enumerate(batches_for(sample, j)):
            f = manifest[f"batches/{judge}/b{b}.md"]
            assert f["items"] == items, f"{judge}/b{b}: batch differs from the sampler"
            assert hashlib.sha256((HERE / "batches" / judge / f"b{b}.md").read_bytes()).hexdigest() == f["sha256"]
    audit = json.loads((HERE / "returned" / "audit.json").read_text())
    for judge in JUDGES:
        ans = {r["item_id"]: r for r in map(json.loads, (HERE / "returned" / f"{judge}.jsonl").open())}
        missing = set(sample.pair_id) - set(ans)
        assert not missing, f"{judge}: {len(missing)} pairs unanswered"
        sample[judge] = sample.pair_id.map(lambda i: ans[i]["judgment"] == "yes").astype(int)
    sample["votes"] = sample[list(JUDGES)].sum(axis=1)
    sample["yes"] = (sample.votes >= 2).astype(int)
    share = sample.groupby("bin").yes.mean()
    ok = [all(share[c] >= MIN_YES for c in range(b, len(TAU_BINS))) for b in range(len(TAU_BINS))]
    first = next((b for b in range(len(TAU_BINS)) if ok[b]), None)
    tau = TAU_BINS[first][0] if first is not None else TAU_BINS[-1][0]
    res = {
        "tau": tau, "rule": f"lowest bin edge where that bin and all higher bins have >= {MIN_YES:.0%} majority yes",
        "fallback_used": first is None,
        "bins": {f"[{lo},{hi})": {"yes_share": round(float(share[b]), 4),
                                   "ci95": wilson(int(sample[sample.bin == b].yes.sum()), int((sample.bin == b).sum())),
                                   "n": int((sample.bin == b).sum()),
                                   "per_judge": {j: round(float(sample[sample.bin == b][j].mean()), 4) for j in JUDGES}}
                 for b, (lo, hi) in enumerate(TAU_BINS)},
        "fleiss_kappa": fleiss_kappa(np.c_[sample.votes, 3 - sample.votes]),
        "audit_violations": len(audit["violations"]),
    }
    OUT.write_text(json.dumps(res, indent=2, default=int) + "\n")
    print(json.dumps(res, indent=1, default=int))


if __name__ == "__main__":
    main()
