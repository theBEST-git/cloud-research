"""Shared frame for the 'research-fashion guide' study (exploratory, with explore/confirm halves).

One row per submission (discovery universe, 2017-2026). Columns:
- outcomes: acc_rev (accepted among reviewed ACC/REJ/WD; NaN otherwise), wd, rev (in reviewed pool),
  cites / y (accepted & S2-matched, 2017-2025 only), top10 (within-year top decile of citations among
  matched accepted papers), hit (accepted & top10; defined for reviewed papers 2017-2025);
- topic dynamics known BEFORE submission (topic100 = fixed bge clusters): share_prev (t-1), share_prev2 (t-2),
  mom = log share growth t-2 -> t-1, size_pct (percentile of share_prev within year), stage_ex_ante;
  realised: share_cur (t), growth_next (t -> t+1, ex post, descriptive only);
- differentiation: nov_topic = 1 - mean cos to 20 nearest same-topic papers of t-1 (name-masked bge);
  nov_prior = 1 - mean cos to 20 nearest papers of t-1..t-2 (any topic); crowd_cycle = # same-year
  papers with cos >= 0.85 (idea-level competition);
- team: log_authors, lprior_acc (2022+ valid), newcomer_team (share_new_authors == 1, 2023+);
- title features G1..G6 (as in cites.core) for every submission;
- half: 'A' (explore) / 'B' (confirm), by a hash of submission_id.
Writes outputs/fashion/frame.parquet.
"""
from __future__ import annotations

import hashlib

import numpy as np
import pandas as pd

from analyses import _core as C
from cites import core as K

OUT = C.OUT / "fashion"
EPS = 1e-4


def _norm(E):
    n = np.linalg.norm(E, axis=1, keepdims=True)
    n[n == 0] = 1
    return (E / n).astype(np.float32)


def knn_mean(Q, R, k=20, block=2000):
    out = np.full(len(Q), np.nan, np.float32)
    if len(R) == 0:
        return out
    kk = min(k, len(R))
    for s in range(0, len(Q), block):
        S = Q[s:s + block] @ R.T
        part = np.partition(S, -kk, axis=1)[:, -kk:]
        out[s:s + block] = part.mean(1)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    df = C.load_analysis_frame(universe_cols=["submission_id", "year", "title", "abstract", "emb_row", "topic50", "topic100", "pool",
                                              "ACC", "REJ", "WD", "DR", "log_authors", "max_prior_accs", "exp_valid",
                                              "share_new_authors", "llm_topic"]).reset_index(drop=True)
    # outcomes
    df["rev"] = df.ACC | df.REJ | df.WD
    df["acc_rev"] = np.where(df.rev, df.ACC.astype(float), np.nan)
    df["wd"] = np.where(df.rev, df.WD.astype(float), np.nan)
    M = pd.read_parquet(C.OUT / "cites" / "matched_venue.parquet")[["submission_id", "matched", "citationCount"]]
    df = df.merge(M, on="submission_id", how="left")
    ok = df.ACC & df.matched.fillna(False).astype(bool) & (df.year <= 2025)
    df["cites"] = np.where(ok, df.citationCount, np.nan)
    df["y"] = np.log1p(df.cites)
    df["cite_pct"] = df[ok].groupby("year").cites.rank(pct=True)
    df["top10"] = np.where(ok, (df.cite_pct > 0.9).astype(float), np.nan)
    # hit: reviewed papers 2017-2025; accepted-but-unmatched set to NaN
    hit = np.where(df.rev & (df.year <= 2025), 0.0, np.nan)
    hit = np.where(ok & (df.top10 == 1), 1.0, hit)
    hit = np.where(df.ACC & ~ok & (df.year <= 2025), np.nan, hit)
    df["hit"] = hit
    # topic dynamics
    sh = df.groupby(["year", "topic100"]).size().unstack(fill_value=0)
    sh = sh.div(sh.sum(1), axis=0)
    get = lambda yy, kk: sh.loc[yy, kk] if yy in sh.index else np.nan
    df["share_cur"] = [get(y, k) for y, k in zip(df.year, df.topic100)]
    df["share_prev"] = [get(y - 1, k) for y, k in zip(df.year, df.topic100)]
    df["share_prev2"] = [get(y - 2, k) for y, k in zip(df.year, df.topic100)]
    df["growth_next"] = [np.log((get(y + 1, k) + EPS) / (get(y, k) + EPS)) if (y + 1) in sh.index else np.nan for y, k in zip(df.year, df.topic100)]
    df["mom"] = np.log((df.share_prev + EPS) / (df.share_prev2 + EPS))
    tk = pd.DataFrame({"year": sh.index.repeat(sh.shape[1]), "topic100": np.tile(sh.columns, sh.shape[0]), "s": sh.to_numpy().ravel()})
    tk["size_pct"] = tk.groupby("year").s.rank(pct=True)
    tk["year"] = tk.year + 1  # percentile of the PREVIOUS year's share, known at submission
    df = df.merge(tk[["year", "topic100", "size_pct"]], on=["year", "topic100"], how="left")
    # ex-ante stage from t-1 size and t-2 -> t-1 momentum (terciles within year)
    mom_t = df.groupby("year").mom.transform(lambda s: s.rank(pct=True))
    big, small = df.size_pct >= 2 / 3, df.size_pct < 1 / 3
    rising, falling = mom_t >= 2 / 3, mom_t < 1 / 3
    df["stage_ex_ante"] = np.select([small & rising, ~big & rising, big & rising, big & ~rising & ~falling, falling],
                                    ["emerging", "growing", "hot_rising", "mature", "declining"], "steady")
    df.loc[df.mom.isna(), "stage_ex_ante"] = np.nan
    # differentiation (name-masked bge; unmasked fallback for 2017)
    Em, found = C.load_masked_embedding(df)
    Ea = C.load_embedding(df, "abstract", "bge-small-en-v1.5")
    E = _norm(np.where(found[:, None], Em, Ea))
    years = df.year.to_numpy()
    topics = df.topic100.to_numpy()
    nov_topic = np.full(len(df), np.nan, np.float32)
    nov_prior = np.full(len(df), np.nan, np.float32)
    crowd = np.zeros(len(df), np.int32)
    for y in sorted(df.year.unique()):
        qi = np.where(years == y)[0]
        pi = np.where((years == y - 1) | (years == y - 2))[0]
        if len(pi):
            nov_prior[qi] = 1 - knn_mean(E[qi], E[pi])
        for k in np.unique(topics[qi]):
            q = qi[topics[qi] == k]
            r = np.where((years == y - 1) & (topics == k))[0]
            if len(r) >= 5:
                nov_topic[q] = 1 - knn_mean(E[q], E[r])
        for s in range(0, len(qi), 2000):
            S = E[qi[s:s + 2000]] @ E[qi].T
            crowd[qi[s:s + 2000]] = (S >= 0.85).sum(1) - 1
    df["nov_topic"], df["nov_prior"], df["crowd_cycle"] = nov_topic, nov_prior, crowd
    # team
    df["lprior_acc"] = np.where(df.exp_valid == 1, np.log1p(df.max_prior_accs.fillna(0)), np.nan)
    df["newcomer_team"] = np.where(df.year >= 2023, (df.share_new_authors == 1).astype(float), np.nan)
    # title features (same definitions as the citation study)
    b = lambda c: df[c].fillna(False).astype(bool)
    df["G1_name"] = b("name_primary").astype(int)
    df["G3_question"] = b("question").astype(int)
    df["G2_assertive"] = (df.title.map(lambda t: bool(K.ASSERT.search(t))) & ~b("question")).astype(int)
    df["G4_llm_words"] = b("r24_any").astype(int)
    df["G5a_length5"] = df.n_words / 5.0
    df["G6a_meme"] = df[K.MEME].fillna(False).astype(bool).any(axis=1).astype(int)
    df["G6b_tentative"] = df[K.TENTATIVE].fillna(False).astype(bool).any(axis=1).astype(int)
    Et = _norm(C.load_embedding(df, "title", "bge-small-en-v1.5"))
    Eab = _norm(Ea)
    df["title_abs_cos"] = (Et * Eab).sum(1)
    df["G5b_informative"] = df.groupby("year").title_abs_cos.transform(lambda s: (s - s.mean()) / s.std())
    df["log_abs_words"] = np.log(df.abstract.str.split().str.len().clip(lower=1))
    df["half"] = df.submission_id.map(lambda s: "A" if int(hashlib.sha256(s.encode()).hexdigest(), 16) % 2 == 0 else "B")
    keep = ["submission_id", "year", "title", "topic50", "topic100", "llm_topic", "pool", "ACC", "REJ", "WD", "DR", "rev", "acc_rev", "wd",
            "cites", "y", "cite_pct", "top10", "hit", "share_cur", "share_prev", "share_prev2", "mom", "size_pct", "growth_next",
            "stage_ex_ante", "nov_topic", "nov_prior", "crowd_cycle", "log_authors", "lprior_acc", "newcomer_team", "log_abs_words",
            "G1_name", "G2_assertive", "G3_question", "G4_llm_words", "G5a_length5", "G5b_informative", "G6a_meme", "G6b_tentative",
            "ortho_mixed_case", "ortho_all_caps", "ortho_word", "half", "emb_row"]
    F = df[keep]
    F.to_parquet(OUT / "frame.parquet")
    print(F.shape)
    print(F.groupby("year").agg(n=("submission_id", "size"), rev=("rev", "sum"), acc=("ACC", "sum"), cites=("cites", "count"),
                                 hit_n=("hit", "count"), nov_topic=("nov_topic", "count"), stage=("stage_ex_ante", "count")))
    print(F.stage_ex_ante.value_counts(dropna=False))
    print(F.half.value_counts())


if __name__ == "__main__":
    main()
