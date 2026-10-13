"""Compare human gold labels (H) with Claude (C1, C2) and ChatGPT (G) on a gold block.

Inputs (outputs/claims_pilot/labels/): H_gold.json (exported from the annotation page's db),
C1_gold_b{B}.json, C2_gold_b{B}.json, optional G_gold_b{B}_batch*.jsonl.
Run: cd research/titles/src && /home/user/venv/bin/python -m claims.compare_gold BLOCK
Writes outputs/claims_pilot/gold_b{B}_comparison.json and gold_b{B}_disagreements.csv.
"""
from __future__ import annotations

import glob
import itertools
import json
import sys

import numpy as np
import pandas as pd

from analyses import _core as C
from claims.agreement_v1 import FLAGS, OV, TV, TYPES, _jsonl, pair_stats

OUT = C.OUT / "claims_pilot"
LAB = OUT / "labels"


def prep(rows):
    L = pd.DataFrame(rows).drop_duplicates("item_id").set_index("item_id")
    L["tv"] = L.title_vs_evidence.astype(str).str.lower().replace({"na": "NA"}).map(TV)
    L["ao"] = L.abstract_overreach.astype(str).str.lower().map(OV)
    for f in FLAGS:
        L[f] = L[f].fillna(0).astype(int)
    for t in TYPES:
        for p in "ta":
            L[f"{p}:{t}"] = L.types.map(lambda v, p=p, t=t: any(str(x).lower().replace(" ", "") == f"{p}:{t}" for x in (v or [])))
    L["t_over"], L["a_over"] = L.tv >= 1, L.ao >= 1
    L["joint"] = np.select([L.t_over & L.a_over, L.t_over, L.a_over], ["both", "title_only", "abstract_only"], "neither")
    return L


def main(block: int):
    labs = {}
    h = LAB / "H_gold.json"
    if h.exists():
        rows = [r for r in json.load(open(h)) if int(r.get("block", 0)) == block]
        if rows:
            labs["H"] = prep(rows)
    for tag in ["C1", "C2"]:
        f = LAB / f"{tag}_gold_b{block}.json"
        if f.exists():
            labs[tag] = prep(json.load(open(f)))
    g = sorted(glob.glob(str(LAB / f"G_gold_b{block}_batch*.jsonl")))
    if g:
        labs["G"] = prep(sum((_jsonl(x) for x in g), []))
    res = {k: {"n": int(len(v)), "title_over_rate": float(v.t_over[v.tv.notna()].mean()), "abstract_over_rate": float(v.a_over.mean()),
               **{f"rate_{f}": float(v[f].mean()) for f in FLAGS}} for k, v in labs.items()}
    for x, y in itertools.combinations(labs, 2):
        res[f"{x}_vs_{y}"] = pair_stats(labs[x], labs[y])
    json.dump(res, open(OUT / f"gold_b{block}_comparison.json", "w"), indent=1, default=str)
    if "H" in labs:
        H = labs["H"]
        rows = []
        for i in H.index:
            r = {"item_id": i, "H_ts": H.loc[i, "title_strength"], "H_tv": H.loc[i, "title_vs_evidence"], "H_ao": H.loc[i, "abstract_overreach"],
                 "H_types": ",".join(H.loc[i, "types"] or []), "H_note": H.loc[i].get("note", "")}
            for k in [k for k in labs if k != "H"]:
                if i in labs[k].index:
                    r[f"{k}_ts"], r[f"{k}_tv"], r[f"{k}_ao"] = labs[k].loc[i, "title_strength"], labs[k].loc[i, "title_vs_evidence"], labs[k].loc[i, "abstract_overreach"]
                    r[f"{k}_types"] = ",".join(labs[k].loc[i, "types"] or [])
            rows.append(r)
        pd.DataFrame(rows).to_csv(OUT / f"gold_b{block}_disagreements.csv", index=False)
    print(json.dumps(res, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main(int(sys.argv[1]))
