"""Twin feasibility, step 3: labeller agreement, twin precision by stratum, projected yield, power.

Reads outputs/twins_feas/labels/L{1,2}_chunk*.json and pilot_key.parquet. Decisions are NOT read:
the power section uses only the base acceptance rate of the candidate population (a pooled
marginal), never pair-level outcomes. Writes pilot_labels_merged.parquet and pilot_summary.json.
"""
from __future__ import annotations

import glob
import json

import numpy as np
import pandas as pd

from analyses import _core as C

OUT = C.OUT / "twins_feas"


def kappa(a, b):
    cats = sorted(set(a) | set(b))
    a, b = np.asarray(a), np.asarray(b)
    po = (a == b).mean()
    pe = sum((a == c).mean() * (b == c).mean() for c in cats)
    return float((po - pe) / (1 - pe)) if pe < 1 else float("nan")


def load_labels(tag):
    rows = []
    for f in sorted(glob.glob(str(OUT / "labels" / f"{tag}_chunk*.json"))):
        rows += json.load(open(f))
    L = pd.DataFrame(rows).drop_duplicates("item_id")
    return L.rename(columns={c: f"{c}_{tag}" for c in L.columns if c != "item_id"})


def main():
    K = pd.read_parquet(OUT / "pilot_key.parquet")
    M = K.merge(load_labels("L1"), on="item_id", how="left").merge(load_labels("L2"), on="item_id", how="left")
    both = M.label_L1.notna() & M.label_L2.notna()
    print("labelled by both:", int(both.sum()), "of", len(M))
    B = M[both].copy()
    B["T1"], B["T2"] = B.label_L1.eq("T"), B.label_L2.eq("T")
    B["TP1"], B["TP2"] = B.label_L1.isin(["T", "P"]), B.label_L2.isin(["T", "P"])
    summ = {
        "n_both": int(both.sum()),
        "agreement_4class": float((B.label_L1 == B.label_L2).mean()),
        "kappa_4class": kappa(B.label_L1, B.label_L2),
        "kappa_T_vs_rest": kappa(B.T1, B.T2),
        "kappa_TP_vs_rest": kappa(B.TP1, B.TP2),
        "confusion": {f"{a}|{b}": int(v) for (a, b), v in pd.crosstab(B.label_L1, B.label_L2).stack().items()},
    }
    # consensus: T only if both T; T-lenient if either T; P-or-better if both in {T,P}
    B["T_strict"] = B.T1 & B.T2
    B["T_lenient"] = B.T1 | B.T2
    B["TP_strict"] = B.TP1 & B.TP2
    summ["controls"] = {
        "known_positive": B[B.kind == "known_positive"][["label_L1", "label_L2"]].values.tolist(),
        "random_same_topic": {"/".join(k): int(v) for k, v in B[B.kind == "random_same_topic"][["label_L1", "label_L2"]].apply(tuple, axis=1).value_counts().items()},
    }
    cand = B[B.kind == "candidate"]
    g = cand.groupby(["band", "era"])
    st = g.agg(n=("item_id", "size"), N=("N_stratum", "first"), T_strict=("T_strict", "mean"),
               T_lenient=("T_lenient", "mean"), TP_strict=("TP_strict", "mean")).reset_index()
    for c in ["T_strict", "T_lenient", "TP_strict"]:
        st[f"proj_{c}"] = st[c] * st.N
    st.to_csv(OUT / "pilot_precision_by_stratum.csv", index=False)
    print(st.round(3).to_string())
    tot = {c: float(st[f"proj_{c}"].sum()) for c in ["T_strict", "T_lenient", "TP_strict"]}
    # stratified SE for projected totals
    for c in ["T_strict", "T_lenient", "TP_strict"]:
        var = (st.N ** 2 * st[c] * (1 - st[c]) / st.n.clip(lower=2)).sum()
        tot[c + "_se"] = float(np.sqrt(var))
    summ["projected_totals"] = tot
    summ["precision_by_band"] = cand.groupby("band")[["T_strict", "T_lenient", "TP_strict"]].mean().round(3).to_dict()
    summ["precision_by_era"] = cand.groupby("era")[["T_strict", "T_lenient", "TP_strict"]].mean().round(3).to_dict()
    summ["mutual_vs_not_T_strict"] = cand.groupby("mutual_masked").T_strict.agg(["mean", "size"]).to_dict()

    # power for concordance (no outcomes): reviewed pool acceptance base rate p among ACC/REJ/WD
    u = pd.read_parquet(C.UNIVERSE_PATH, columns=["year", "pool"])
    u = u[u.year >= 2018]
    p = float((u.pool == "ACC").mean() / u.pool.isin(["ACC", "REJ", "WD"]).mean())
    base = p * p + (1 - p) * (1 - p)
    pw = {}
    for n in [150, 300, 500, 1000]:
        se = np.sqrt(base * (1 - base) / n)
        pw[n] = {"chance_concordance": round(base, 3), "se": round(float(se), 3), "mde_80pct_2sided": round(float(2.8 * se), 3)}
    summ["power_concordance"] = {"p_accept_reviewed": round(p, 3), "by_n_pairs": pw}
    M.to_parquet(OUT / "pilot_labels_merged.parquet")
    json.dump(summ, open(OUT / "pilot_summary.json", "w"), indent=1, default=str)
    print(json.dumps({k: v for k, v in summ.items() if k != "confusion"}, indent=1, default=str))


if __name__ == "__main__":
    main()
