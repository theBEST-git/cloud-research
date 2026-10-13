"""Agreement for codebook v1.1 (round >= 2) across annotators C1, C2 (Claude) and G (ChatGPT, manual app).

Inputs: labels/C1_r{R}_chunk*.json, labels/C2_r{R}_chunk*.json (JSON arrays) and
labels/G_r{R}_batch*.jsonl (JSON lines, one object per line; code fences tolerated).
Run: cd research/titles/src && /home/user/venv/bin/python -m claims.agreement_v1 ROUND
Writes outputs/claims_pilot/round{R}_agreement_v1.json and round{R}_merged.parquet.
"""
from __future__ import annotations

import glob
import itertools
import json
import re
import sys

import numpy as np
import pandas as pd

from analyses import _core as C
from claims.agreement import kappa

OUT = C.OUT / "claims_pilot"
TV = {"understated": -1, "matched": 0, "mild": 1, "clear": 2}
OV = {"none": 0, "mild": 1, "clear": 2}
FLAGS = ["hedge", "booster", "superlative", "universal", "quantified", "scoped"]
TYPES = ["scope", "certainty", "magnitude", "novelty", "causal", "unsupported"]


def _jsonl(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip().strip("`")
        if not line or not line.startswith("{"):
            continue
        rows.append(json.loads(line))
    return rows


def load(tag, rnd):
    rows = []
    for f in sorted(glob.glob(str(OUT / "labels" / f"{tag}_r{rnd}_*"))):
        rows += json.load(open(f)) if f.endswith(".json") else _jsonl(f)
    if not rows:
        return None
    L = pd.DataFrame(rows).drop_duplicates("item_id").set_index("item_id")
    if "title_vs_abstract" in L.columns and "title_vs_evidence" not in L.columns:
        L = L.rename(columns={"title_vs_abstract": "title_vs_evidence"})
    L["tv"] = L.title_vs_evidence.astype(str).str.lower().map(TV)
    L["ao"] = L.abstract_overreach.astype(str).str.lower().map(OV)
    for t in TYPES:
        for p in "ta":
            L[f"{p}:{t}"] = L.types.map(lambda v, p=p, t=t: any(str(x).lower().replace(" ", "") == f"{p}:{t}" for x in (v or [])))
    L["t_over"] = L.tv >= 1
    L["a_over"] = L.ao >= 1
    L["joint"] = np.select([L.t_over & L.a_over, L.t_over, L.a_over], ["both", "title_only", "abstract_only"], "neither")
    return L


def pair_stats(A, B):
    ids = A.index.intersection(B.index)
    A, B = A.loc[ids], B.loc[ids]
    r = {"n": int(len(ids)), "type_kappa": kappa(A.type, B.type)}
    a, b = A.title_strength.astype(int), B.title_strength.astype(int)
    r["title_strength"] = {"exact": float((a == b).mean()), "kappa_w": kappa(a, b, "quadratic", [0, 1, 2, 3])}
    m = A.tv.notna() & B.tv.notna()
    r["title_vs_evidence"] = {"n": int(m.sum()), "exact": float((A.tv[m] == B.tv[m]).mean()),
                              "kappa_w": kappa(A.tv[m], B.tv[m], "quadratic", [-1, 0, 1, 2]),
                              "kappa_over": kappa(A.tv[m] >= 1, B.tv[m] >= 1),
                              "prev_over": [float((A.tv[m] >= 1).mean()), float((B.tv[m] >= 1).mean())]}
    r["abstract_overreach"] = {"exact": float((A.ao == B.ao).mean()), "kappa_w": kappa(A.ao, B.ao, "quadratic", [0, 1, 2]),
                               "kappa_over": kappa(A.ao >= 1, B.ao >= 1), "prev_over": [float((A.ao >= 1).mean()), float((B.ao >= 1).mean())]}
    r["flags"] = {f: {"kappa": kappa(A[f].astype(int), B[f].astype(int)), "prev": [float(A[f].astype(int).mean()), float(B[f].astype(int).mean())]} for f in FLAGS}
    r["types"] = {f"{p}:{t}": kappa(A[f"{p}:{t}"], B[f"{p}:{t}"]) for p in "ta" for t in TYPES}
    r["joint"] = {"kappa": kappa(A.joint, B.joint), "crosstab": {f"{x}|{y}": int(v) for (x, y), v in pd.crosstab(A.joint, B.joint).stack().items()}}
    return r


def main(rnd: int):
    labs = {t: load(t, rnd) for t in ["C1", "C2", "G"]}
    labs = {k: v for k, v in labs.items() if v is not None}
    res = {k: {"n": int(len(v))} for k, v in labs.items()}
    for x, y in itertools.combinations(labs, 2):
        res[f"{x}_vs_{y}"] = pair_stats(labs[x], labs[y])
    merged = pd.concat({k: v for k, v in labs.items()}, axis=1)
    merged.columns = [f"{a}__{b}" for a, b in merged.columns]
    merged.astype(str).to_parquet(OUT / f"round{rnd}_merged.parquet")
    json.dump(res, open(OUT / f"round{rnd}_agreement_v1.json", "w"), indent=1, default=str)
    print(json.dumps(res, indent=1, default=str))


if __name__ == "__main__":
    main(int(sys.argv[1]))
