"""Audit: recompute the look-ahead-free neighbourhood measures under alternative definitions (discovery data only).

For every submission of year t >= 2019 (same embeddings and reference sets as frame2.py):
- c1_xx / c2_xx: raw neighbour counts in t-1 / t-2 at cos >= 0.78, 0.80, 0.82, 0.85 (xx = 78, 80, 82, 85);
- c1_95 / c2_95: near-duplicates (cos >= 0.95) in t-1 / t-2;
- c1_team / c2_team: neighbours at cos >= 0.80 that share >= 1 declared author key with the paper (own earlier
  versions / same-team papers); c1_nt / c2_nt = c1_80 - c1_team etc.;
- nn_nt: max cos to any t-1..t-2 paper NOT sharing an author key; nn_nd: max cos below 0.95 (no near-duplicates);
- c3_80: neighbours in t-3 (for t-1 vs t-3 momentum); hub1: mean cos to all t-1 papers (embedding hubness);
- team_n12: number of t-1/t-2 submissions sharing an author key (any cosine).
Writes outputs/fashion/explore/audit/loc_variants.parquet.
"""
from __future__ import annotations

from collections import defaultdict

import numpy as np
import pandas as pd

from analyses import _core as C
from fashion.frame import _norm

TAUS = [0.78, 0.80, 0.82, 0.85]
OUT = C.OUT / "fashion" / "explore" / "audit"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    f = pd.read_parquet(C.OUT / "fashion" / "frame2.parquet")[["submission_id", "year", "emb_row", "loc1", "loc_mom", "nn_prev"]]
    Em, found = C.load_masked_embedding(f)
    Ea = C.load_embedding(f, "abstract", "bge-small-en-v1.5")
    E = _norm(np.where(found[:, None], Em, Ea))
    yr = f.year.to_numpy()
    a = pd.read_csv(C.DATA / "submission_authors.csv.gz", usecols=["submission_id", "declared_id_key"],
                    keep_default_na=False, na_values=[r"\N"]).dropna()
    idx = dict(zip(f.submission_id, range(len(f))))
    a = a[a.submission_id.isin(idx)]
    by_key = defaultdict(list)
    for s, k in zip(a.submission_id, a.declared_id_key):
        by_key[k].append(idx[s])
    keys_of = a.groupby("submission_id").declared_id_key.apply(list).to_dict()
    sid = f.submission_id.to_numpy()
    n = len(f)
    cols = defaultdict(lambda: np.full(n, np.nan))
    for t in range(2019, 2027):
        qi = np.where(yr == t)[0]
        refs = {lag: np.where(yr == t - lag)[0] for lag in (1, 2, 3)}
        pos = {lag: pd.Series(np.arange(len(r)), index=r) for lag, r in refs.items()}
        # team members of each query in t-1, t-2
        team = {}
        for i in qi:
            team[i] = {j for k in keys_of.get(sid[i], []) for j in by_key[k] if yr[j] in (t - 1, t - 2)}
        cols["team_n12"][qi] = [len(team[i]) for i in qi]
        nn_nt = np.full(len(qi), -np.inf)
        nn_nd = np.full(len(qi), -np.inf)
        for lag in (1, 2, 3):
            R = refs[lag]
            if len(R) == 0:
                continue
            if lag == 1:
                cols["hub1"][qi] = E[qi] @ E[R].mean(0)
            for s in range(0, len(qi), 2000):
                q = qi[s:s + 2000]
                S = E[q] @ E[R].T
                if lag == 3:
                    cols["c3_80"][q] = (S >= 0.80).sum(1)
                    continue
                for tau in TAUS:
                    cols[f"c{lag}_{int(round(tau * 100))}"][q] = (S >= tau).sum(1)
                cols[f"c{lag}_95"][q] = (S >= 0.95).sum(1)
                Snd = np.where(S >= 0.95, -np.inf, S)
                nn_nd[s:s + len(q)] = np.fmax(nn_nd[s:s + len(q)], Snd.max(1))
                rr, cc = [], []
                for r, i in enumerate(q):
                    js = [pos[lag][j] for j in team[i] if yr[j] == t - lag]
                    rr += [r] * len(js)
                    cc += js
                rr, cc = np.array(rr, int), np.array(cc, int)
                tm = np.zeros(len(q))
                if len(rr):
                    np.add.at(tm, rr, (S[rr, cc] >= 0.80).astype(float))
                    S[rr, cc] = -np.inf
                cols[f"c{lag}_team"][q] = tm
                nn_nt[s:s + len(q)] = np.fmax(nn_nt[s:s + len(q)], S.max(1))
        cols["nn_nt"][qi] = nn_nt
        cols["nn_nd"][qi] = nn_nd
        print(t, len(qi), "team80 t-1:", int(np.nansum(cols["c1_team"][qi])), "t-2:", int(np.nansum(cols["c2_team"][qi])),
              "dup95 t-1:", int(np.nansum(cols["c1_95"][qi])), flush=True)
    out = pd.DataFrame({"submission_id": sid, "year": yr, **{k: v for k, v in cols.items()}})
    out = out[out.year >= 2019]
    N = pd.Series(yr).value_counts().to_dict()
    # consistency with frame2 (tau 0.80)
    chk = out.merge(f, on=["submission_id", "year"])
    l1 = 1000 * chk.c1_80 / chk.year.map(lambda y: N[y - 1])
    print("max |loc1 - recomputed|:", float(np.nanmax(np.abs(l1 - chk.loc1))))
    out.to_parquet(OUT / "loc_variants.parquet")
    print(out.describe().T)


if __name__ == "__main__":
    main()
