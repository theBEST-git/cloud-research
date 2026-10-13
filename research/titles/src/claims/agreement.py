"""Claims codebook pilot: inter-annotator agreement per field and a disagreement file for adjudication.

Run: cd research/titles/src && /home/user/venv/bin/python -m claims.agreement ROUND
Writes outputs/claims_pilot/round{R}_agreement.json and round{R}_disagreements.jsonl.
"""
from __future__ import annotations

import glob
import json
import sys

import numpy as np
import pandas as pd

from analyses import _core as C

OUT = C.OUT / "claims_pilot"
OV = {"none": 0, "mild": 1, "clear": 2}
TYPES = ["scope", "certainty", "magnitude", "novelty", "causal"]


def kappa(a, b, weights=None, cats=None):
    a, b = np.asarray(a), np.asarray(b)
    cats = sorted(set(a) | set(b)) if cats is None else cats
    k = len(cats)
    if k < 2:
        return float("nan")
    idx = {c: i for i, c in enumerate(cats)}
    O = np.zeros((k, k))
    for x, y in zip(a, b):
        O[idx[x], idx[y]] += 1
    O /= O.sum()
    E = np.outer(O.sum(1), O.sum(0))
    if weights == "quadratic":
        W = np.array([[(i - j) ** 2 for j in range(k)] for i in range(k)]) / (k - 1) ** 2
    else:
        W = 1 - np.eye(k)
    return float(1 - (W * O).sum() / (W * E).sum()) if (W * E).sum() > 0 else float("nan")


def load(tag, rnd):
    rows = []
    for f in sorted(glob.glob(str(OUT / "labels" / f"{tag}_r{rnd}_chunk*.json"))):
        rows += json.load(open(f))
    L = pd.DataFrame(rows).drop_duplicates("item_id").set_index("item_id")
    return L


def norm_types(t, prefix):
    out = set()
    for x in (t or []):
        x = str(x).lower().strip()
        if x.startswith(prefix + ":"):
            out.add(x.split(":", 1)[1].strip())
    return out


def main(rnd: int):
    A, B = load("C1", rnd), load("C2", rnd)
    ids = A.index.intersection(B.index)
    A, B = A.loc[ids], B.loc[ids]
    res = {"n": int(len(ids))}
    res["type"] = {"agree": float((A.type == B.type).mean()), "kappa": kappa(A.type, B.type)}
    for f, w in [("title_strength", "quadratic"), ("abstract_strength", "quadratic")]:
        a, b = A[f].astype(int), B[f].astype(int)
        res[f] = {"exact": float((a == b).mean()), "within1": float(((a - b).abs() <= 1).mean()),
                  "kappa_w": kappa(a, b, "quadratic", sorted(set(a) | set(b))),
                  "dist_C1": a.value_counts().sort_index().to_dict(), "dist_C2": b.value_counts().sort_index().to_dict()}
    for f in ["title_overreach", "abstract_overreach"]:
        a, b = A[f].astype(str).str.lower(), B[f].astype(str).str.lower()
        m = a.isin(OV) & b.isin(OV)
        aa, bb = a[m].map(OV), b[m].map(OV)
        res[f] = {"n_rated_both": int(m.sum()), "exact": float((aa == bb).mean()),
                  "kappa_w3": kappa(aa, bb, "quadratic", [0, 1, 2]),
                  "kappa_any": kappa(aa > 0, bb > 0), "kappa_clear": kappa(aa == 2, bb == 2),
                  "prev_any_C1": float((aa > 0).mean()), "prev_any_C2": float((bb > 0).mean()),
                  "prev_clear_C1": float((aa == 2).mean()), "prev_clear_C2": float((bb == 2).mean()),
                  "NA_mismatch": int(((a == "na") != (b == "na")).sum())}
    tk = {}
    for p in ["t", "a"]:
        for t in TYPES:
            x = A.types.map(lambda v: t in norm_types(v, p))
            y = B.types.map(lambda v: t in norm_types(v, p))
            tk[f"{p}:{t}"] = {"kappa": kappa(x, y), "prev_C1": float(x.mean()), "prev_C2": float(y.mean())}
    res["types"] = tk
    json.dump(res, open(OUT / f"round{rnd}_agreement.json", "w"), indent=1)
    items = {}
    for f in glob.glob(str(OUT / f"round{rnd}_items_chunk*.jsonl")):
        for line in open(f):
            if line.strip():
                o = json.loads(line)
                items[o["item_id"]] = o
    with open(OUT / f"round{rnd}_disagreements.jsonl", "w") as fh:
        for i in ids:
            a, b = A.loc[i], B.loc[i]
            diff = [f for f in ["title_strength", "abstract_strength", "title_overreach", "abstract_overreach"]
                    if str(a[f]).lower() != str(b[f]).lower()]
            if diff:
                fh.write(json.dumps({"item_id": i, "title": items[i]["title"], "abstract": items[i]["abstract"], "fields": diff,
                                     "C1": {k: a[k] for k in A.columns if k in ["type", "title_strength", "abstract_strength", "title_overreach", "abstract_overreach", "types", "rationale"]},
                                     "C2": {k: b[k] for k in B.columns if k in ["type", "title_strength", "abstract_strength", "title_overreach", "abstract_overreach", "types", "rationale"]}},
                                    default=str) + "\n")
    print(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    main(int(sys.argv[1]))
