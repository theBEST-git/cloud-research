"""Score the H2d blind validation and write the gate (PREREGISTRATION.md D6, D10).

Rebuilds the key with sample.draw(), checks that the judged batch files are the ones the sampler produces, and applies
the registered rule: an item is peripheral if at least 2 of 3 judges say so; the gate passes if
p_flag >= 0.50 and p_flag >= 2 * p_nonflag. One attempt only.

    python research/fashion/annotation/keyword_centrality/score.py
Writes research/fashion/output/h2d_validation.json.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from sample import JUDGES, batches_for, draw  # noqa: E402
from stats import fleiss_kappa, wilson  # noqa: E402

OUT = HERE.parents[1] / "output" / "h2d_validation.json"
P_MIN, RATIO = 0.50, 2.0


def main() -> None:
    sample, _ = draw()
    manifest = json.loads((HERE / "manifest.json").read_text())["files"]
    for j, judge in enumerate(JUDGES):
        for b, items in enumerate(batches_for(sample, j)):
            f = manifest[f"batches/{judge}/b{b}.md"]
            assert f["items"] == items, f"{judge}/b{b}: batch differs from the sampler"
            assert hashlib.sha256((HERE / "batches" / judge / f"b{b}.md").read_bytes()).hexdigest() == f["sha256"]
    audit = json.loads((HERE / "returned" / "audit.json").read_text())
    ans = {}
    for judge in JUDGES:
        rows = [json.loads(l) for l in (HERE / "returned" / f"{judge}.jsonl").open()]
        ans[judge] = {r["item_id"]: r for r in rows}
        missing = set(sample.item_id) - set(ans[judge])
        assert not missing, f"{judge}: {len(missing)} items unanswered"
    for judge in JUDGES:
        sample[judge] = sample.item_id.map(lambda i: ans[judge][i]["judgment"] == "peripheral").astype(int)
    sample["votes"] = sample[list(JUDGES)].sum(axis=1)
    sample["peripheral"] = (sample.votes >= 2).astype(int)
    f, nf = sample[sample.role == "flagged"], sample[sample.role == "nonflagged"]
    p_flag, p_non = f.peripheral.mean(), nf.peripheral.mean()
    passed = bool(p_flag >= P_MIN and p_flag >= RATIO * p_non)
    counts = np.c_[sample.votes, 3 - sample.votes]
    conf = pd.concat([pd.DataFrame(ans[j].values()).assign(judge=j) for j in JUDGES])
    res = {
        "gate": "pass" if passed else "fail",
        "rule": f"p_flag >= {P_MIN} and p_flag >= {RATIO} * p_nonflag; peripheral = at least 2 of 3 judges",
        "p_flag": round(float(p_flag), 4), "p_flag_ci95": wilson(int(f.peripheral.sum()), len(f)),
        "p_nonflag": round(float(p_non), 4), "p_nonflag_ci95": wilson(int(nf.peripheral.sum()), len(nf)),
        "ratio": round(float(p_flag / p_non), 3) if p_non > 0 else None,
        "n_flagged": len(f), "n_nonflagged": len(nf),
        "fleiss_kappa": fleiss_kappa(counts),
        "per_judge": {j: {"p_flag": round(float(f[j].mean()), 4), "p_nonflag": round(float(nf[j].mean()), 4)} for j in JUDGES},
        "unanimous_share": round(float(((sample.votes == 0) | (sample.votes == 3)).mean()), 4),
        "pairwise_agreement": {f"{a}~{b}": round(float((sample[a] == sample[b]).mean()), 4)
                               for i, a in enumerate(JUDGES) for b in JUDGES[i + 1:]},
        "confidence_shares": conf.confidence.value_counts(normalize=True).round(4).to_dict(),
        "p_flag_by_year": f.groupby("year").peripheral.mean().round(3).to_dict(),
        "audit_violations": len(audit["violations"]),
        "h2d_in_family": passed, "h3c_in_family": passed,
    }
    OUT.write_text(json.dumps(res, indent=2, default=int) + "\n")
    print(json.dumps(res, indent=1, default=int))


if __name__ == "__main__":
    main()
