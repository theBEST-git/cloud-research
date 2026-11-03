"""Outcome-free, descriptive (tier E): are newcomer papers more or less novel in content than incumbent papers,
within the same k100 topic x year cell?

Added during paper writing (not pre-registered; 2026-11-03). Reads only outcome-free inputs:
  research/topics/cache/specter2.npy + specter2_ids.csv     SPECTER2 vectors of the 43,480 discovery papers
  research/fashion/output/specter2_centring_mean.npy         frozen discovery centring mean (as ph5_position.embeddings)
  research/fashion/output/earlier_versions.csv.gz            probable earlier-version links (chain excluded, as ph5)
  research/fashion/output/paper_variables.csv.gz             map, topic, year, newcomer, incumbent(_s4), team_size
  research/topics/output/paper_contributions.csv.gz          primary_class, primary_type, foundation_model
  data/submission_authors.csv.gz (submission_id, declared_id_key only)   for the own-work-excluded variant
No decision or acceptance column is read anywhere; author keys are used only to match papers and are never written.

Novelty (reimplements ph5_position.novelty, main K = 10 only; the module is not imported):
  vectors centred by the frozen mean and L2-normalised; nov = 1 - mean of the 10 largest cosines with all discovery
  papers of strictly earlier years (any topic), the paper's own chain of probable earlier versions excluded; NaN for
  the first year (2017). pct = (average rank - 0.5) / n of nov within the k100 topic x year cell over ALL submissions in
  the cell (as ph5_position.cell_pct), reported x 100 (percentile points).
Population: k100, years 2019-2026, has_author_key (the RQ2 population).
Estimator: OLS with k100 topic x year FE absorbed by demeaning; CR1 SE clustered by topic, t with G - 1 df (as ols.fe_ols).
Variant nov_selfx: the same novelty with every earlier paper that shares an author key with the paper removed from
its reference set (so incumbents are not 'less novel' merely because their own earlier papers are nearby).
Writes research/fashion/output/paper_novelty/ (novelty_newcomer.json, novelty_newcomer.csv; no per-paper file).

    python research/fashion/paper/analysis/novelty_newcomer.py
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse, stats

ROOT = Path(__file__).resolve().parents[3]                              # research/
OUT = ROOT / "fashion" / "output" / "paper_novelty"
K = 10
CHUNK = 1500


# ---------------------------------------------------------------- novelty
def load_frame() -> pd.DataFrame:
    ids = pd.read_csv(ROOT / "topics/cache/specter2_ids.csv").submission_id
    v = pd.read_csv(ROOT / "fashion/output/paper_variables.csv.gz")
    v = v[v["map"] == "k100"].set_index("submission_id")
    c = pd.read_csv(ROOT / "topics/output/paper_contributions.csv.gz",
                    usecols=["submission_id", "primary_class", "primary_type", "foundation_model"]).set_index("submission_id")
    ev = pd.read_csv(ROOT / "fashion/output/earlier_versions.csv.gz",
                     usecols=["submission_id", "probable_earlier_version"]).set_index("submission_id")
    df = pd.DataFrame({"submission_id": ids})
    df = df.join(v, on="submission_id").join(c, on="submission_id").join(ev, on="submission_id")
    assert df.topic.notna().all() and df.primary_class.notna().all() and len(df) == 43480
    return df.reset_index(drop=True)


def chains(df: pd.DataFrame) -> list[np.ndarray]:
    pos = {s: i for i, s in enumerate(df.submission_id)}
    link = dict(zip(df.submission_id, df.probable_earlier_version))
    out = []
    for s in df.submission_id:
        ch, e = [], link.get(s)
        while isinstance(e, str) and e in pos and pos[e] not in ch:
            ch.append(pos[e])
            e = link.get(e)
        out.append(np.array(ch, int))
    return out


def author_keys(df: pd.DataFrame) -> sparse.csr_matrix:
    """Papers x author keys (declared_id_key), aligned with df; used only to mask shared-author pairs."""
    a = pd.read_csv(ROOT.parent / "data" / "submission_authors.csv.gz", usecols=["submission_id", "declared_id_key"],
                    keep_default_na=False, na_values=[r"\N"]).dropna()
    pos = pd.Series(np.arange(len(df)), index=df.submission_id.to_numpy())
    a = a[a.submission_id.isin(pos.index)].drop_duplicates()
    codes, _ = pd.factorize(a.declared_id_key)
    return sparse.csr_matrix((np.ones(len(a)), (pos[a.submission_id].to_numpy(), codes)), shape=(len(df), codes.max() + 1))


def novelty(X: np.ndarray, years: np.ndarray, ch: list[np.ndarray] | None,
            A: sparse.csr_matrix | None = None) -> np.ndarray:
    nov = np.full(len(years), np.nan)
    for y in np.unique(years):
        R, Q = np.flatnonzero(years < y), np.flatnonzero(years == y)
        if len(R) < K:
            continue
        XR = X[R].T
        for s in range(0, len(Q), CHUNK):
            q = Q[s:s + CHUNK]
            S = X[q] @ XR
            if ch is not None:
                for a, i in enumerate(q):
                    c = ch[i][years[ch[i]] < y]
                    if len(c):
                        S[a, np.searchsorted(R, c)] = -2.0
            if A is not None:                                  # drop earlier papers sharing an author key
                shared = (A[q] @ A[R].T).tocoo()
                S[shared.row, shared.col] = -2.0
            nov[q] = 1 - np.partition(S, -K, axis=1)[:, -K:].mean(axis=1)
            del S
    return nov


def cell_pct(x: pd.Series, groups: list[pd.Series]) -> np.ndarray:
    g = x.groupby([s.to_numpy() for s in groups])
    return ((g.rank(method="average") - 0.5) / g.transform("count")).to_numpy()


# ---------------------------------------------------------------- estimator (as ols.fe_ols)
def demean(values: np.ndarray, groups: np.ndarray) -> np.ndarray:
    codes, inv = np.unique(groups, return_inverse=True)
    sums = np.zeros((len(codes),) + values.shape[1:])
    np.add.at(sums, inv, values)
    counts = np.bincount(inv, minlength=len(codes)).reshape((-1,) + (1,) * (values.ndim - 1))
    return values - (sums / counts)[inv]


def fe_ols(d: pd.DataFrame, y: str, xs: list[str], absorb: str = "cell", cluster: str = "topic") -> dict:
    d = d.dropna(subset=[y] + xs)
    yv, Xv = d[y].to_numpy(float), d[xs].to_numpy(float)
    g, c = d[absorb].to_numpy(), d[cluster].to_numpy()
    yd, Xd = demean(yv, g), demean(Xv, g)
    xtx_inv = np.linalg.pinv(Xd.T @ Xd)
    beta = xtx_inv @ Xd.T @ yd
    resid = yd - Xd @ beta
    _, cinv = np.unique(c, return_inverse=True)
    G, n, k = cinv.max() + 1, len(yd), Xd.shape[1]
    scores = np.zeros((G, k))
    np.add.at(scores, cinv, Xd * resid[:, None])
    vcov = (G / (G - 1)) * ((n - 1) / (n - k)) * xtx_inv @ (scores.T @ scores) @ xtx_inv
    se = np.sqrt(np.diag(vcov))
    j = 0
    tcrit = stats.t.ppf(0.975, G - 1)
    t = beta[j] / se[j]
    # cells that identify the coefficient: both newcomer and incumbent papers present
    both = d.groupby(absorb)[xs[0]].agg(lambda s: s.nunique() > 1)
    return {"coef": float(beta[j]), "se": float(se[j]), "t": float(t), "p": float(2 * stats.t.sf(abs(t), G - 1)),
            "ci_lo": float(beta[j] - tcrit * se[j]), "ci_hi": float(beta[j] + tcrit * se[j]), "n": int(n),
            "clusters": int(G), "cells": int(d[absorb].nunique()), "cells_with_both": int(both.sum()),
            "n_in_cells_with_both": int(d[d[absorb].map(both)].shape[0]),
            "newcomer_share": float(d[xs[0]].mean()),
            "mean_y_newcomer": float(d.loc[d[xs[0]] == 1, y].mean()),
            "mean_y_incumbent": float(d.loc[d[xs[0]] == 0, y].mean()), "controls": xs[1:]}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    df = load_frame()
    years = df.year.to_numpy()
    X0 = np.load(ROOT / "topics/cache/specter2.npy").astype(np.float32)
    mu = np.load(ROOT / "fashion/output/specter2_centring_mean.npy").astype(np.float32)
    ch = chains(df)

    X = X0 - mu
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    df["nov"] = novelty(X, years, ch)
    df["nov_selfx"] = novelty(X, years, ch, author_keys(df))
    del X
    # sensitivity: uncentred vectors, no chain exclusion (the plain definition in the task text)
    Xr = X0 / np.linalg.norm(X0, axis=1, keepdims=True)
    del X0
    df["nov_plain"] = novelty(Xr, years, None)
    del Xr

    df["cell"] = df.topic.astype(str) + ":" + df.year.astype(str)
    df["pct"] = 100 * cell_pct(df.nov, [df.topic, df.year])
    df["pct_plain"] = 100 * cell_pct(df.nov_plain, [df.topic, df.year])
    df["pct_selfx"] = 100 * cell_pct(df.nov_selfx, [df.topic, df.year])
    df["nov_x100"] = 100 * df.nov                      # raw-cosine version, in hundredths of cosine
    df["log2_team"] = np.log2(df.team_size.where(df.team_size > 0))
    df["fm"] = (df.foundation_model == "yes").astype(float)
    df["has_ev"] = df.probable_earlier_version.notna()
    df["newcomer_s4"] = 1 - df.incumbent_s4
    for cl in sorted(df.primary_class.unique()):
        if cl != "method":
            df[f"cls_{cl}"] = (df.primary_class == cl).astype(float)
    cls_ctrl = [c for c in df.columns if c.startswith("cls_")]

    pop = df[df.year.between(2019, 2026) & df.has_author_key.astype(bool)].copy()
    assert pop.nov.notna().all()
    meth = pop[pop.primary_class == "method"]
    early, late = pop[pop.year <= 2022], pop[pop.year >= 2023]

    R: dict[str, dict] = {}
    R["main_pct"] = fe_ols(pop, "pct", ["newcomer"])
    R["method_only_pct"] = fe_ols(meth, "pct", ["newcomer"])
    R["method_type_only_pct"] = fe_ols(pop[pop.primary_type == "method"], "pct", ["newcomer"])
    R["team_ctrl_pct"] = fe_ols(pop, "pct", ["newcomer", "log2_team"])
    R["team_class_fm_ctrl_pct"] = fe_ols(pop, "pct", ["newcomer", "log2_team", "fm"] + cls_ctrl)
    R["method_only_team_ctrl_pct"] = fe_ols(meth, "pct", ["newcomer", "log2_team"])
    R["era_2019_2022_pct"] = fe_ols(early, "pct", ["newcomer"])
    R["era_2023_2026_pct"] = fe_ols(late, "pct", ["newcomer"])
    R["era_2019_2022_team_pct"] = fe_ols(early, "pct", ["newcomer", "log2_team"])
    R["era_2023_2026_team_pct"] = fe_ols(late, "pct", ["newcomer", "log2_team"])
    pe = pop.assign(nc_late=pop.newcomer * (pop.year >= 2023))
    R["era_difference_pct"] = fe_ols(pe, "pct", ["nc_late", "newcomer"])   # coef = late minus early gap
    R["raw_cosine_nov_x100"] = fe_ols(pop, "nov_x100", ["newcomer"])
    R["raw_cosine_nov_x100_team"] = fe_ols(pop, "nov_x100", ["newcomer", "log2_team"])
    R["raw_cosine_method_only"] = fe_ols(meth, "nov_x100", ["newcomer"])
    # sensitivities
    R["excl_2021_pct"] = fe_ols(pop[pop.year != 2021], "pct", ["newcomer"])
    R["newcomer_s4_pct"] = fe_ols(pop.dropna(subset=["newcomer_s4"]), "pct", ["newcomer_s4"])
    R["no_earlier_version_pct"] = fe_ols(pop[~pop.has_ev], "pct", ["newcomer"])
    R["plain_def_pct"] = fe_ols(pop, "pct_plain", ["newcomer"])
    R["own_work_excluded_pct"] = fe_ols(pop, "pct_selfx", ["newcomer"])
    R["own_work_excluded_team_pct"] = fe_ols(pop, "pct_selfx", ["newcomer", "log2_team"])
    R["own_work_excluded_method_only_pct"] = fe_ols(pop[pop.primary_class == "method"], "pct_selfx", ["newcomer"])
    for y in range(2019, 2027):
        R[f"year_{y}_pct"] = fe_ols(pop[pop.year == y], "pct", ["newcomer"])

    desc = {
        "population_n": int(len(pop)), "cells": int(pop.cell.nunique()), "topics": int(pop.topic.nunique()),
        "newcomer_share": float(pop.newcomer.mean()),
        "nov_mean_sd_by_year": pop.groupby("year").nov.agg(["mean", "std", "size"]).round(4).reset_index().to_dict("records"),
        "nov_sd_within_cell": float(np.sqrt(np.mean(demean(pop.nov.to_numpy(), pop.cell.to_numpy()) ** 2))),
        "newcomer_share_by_year": pop.groupby("year").newcomer.mean().round(4).to_dict(),
        "corr_nov_vs_plain": float(pop[["nov", "nov_plain"]].corr().iloc[0, 1]),
        "corr_pct_vs_plain": float(pop[["pct", "pct_plain"]].corr().iloc[0, 1]),
        "team_size_zero_dropped_in_team_specs": int((pop.team_size <= 0).sum()),
        "method_class_n": int(len(meth)),
    }
    json.dump({"results": R, "descriptives": desc}, open(OUT / "novelty_newcomer.json", "w"), indent=1)
    rows = pd.DataFrame(R).T
    rows.to_csv(OUT / "novelty_newcomer.csv")
    pd.set_option("display.width", 250)
    print(rows[["coef", "se", "t", "p", "ci_lo", "ci_hi", "n", "clusters", "cells", "cells_with_both",
                "newcomer_share", "mean_y_newcomer", "mean_y_incumbent"]].to_string())
    print(json.dumps(desc, indent=1))


if __name__ == "__main__":
    main()
