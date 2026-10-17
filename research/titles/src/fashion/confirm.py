"""Frozen confirmatory analysis for the research-fashion guide (docs/FASHION_PREREG.md).

Every measure for a paper of year t is computed against the SAME fixed reference: discovery submissions of t-1 and
t-2 (name-masked bge-small abstract embeddings). Percentiles are the discovery ECDF of the paper's year, and the
nearest-predecessor residual uses per-year coefficients fitted on discovery. Discovery papers and held-out papers
therefore go through identical code; the discovery dry run reproduces the exploration estimates.

Stages
    python -m fashion.confirm calibrate                  # discovery reference + frozen calibration (outputs/fashion/frozen/)
    python -m fashion.confirm dryrun                     # H1-H6 + secondaries on discovery -> outputs/fashion/dryrun.json
    python -m fashion.confirm check                      # held-out code path on a discovery sample (raw CSV rows)
    python -m fashion.confirm heldout <submissions.csv.gz> <submission_authors.csv.gz>   # ONCE -> heldout.json
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from collections import defaultdict

import numpy as np
import pandas as pd
import pyfixest as pf
from scipy import stats

from analyses import _core as C

OUT = C.OUT / "fashion"
FROZEN = OUT / "frozen"
GUARD = OUT / "heldout_started.json"
TAU = 0.80               # neighbour threshold (cosine) for local density
NN_BOUND = 0.05          # H2 non-inferiority bound: momentum's acceptance effect (bottom -> top percentile) < +5 pp
ALPHA = 0.05
YEARS_ACC, YEARS_CIT, YEARS_TEAM_ACC, YEARS_TEAM_CIT = (2019, 2026), (2019, 2025), (2022, 2026), (2022, 2025)


# --------------------------------------------------------------------------------------------
# Reference (discovery) and measures
# --------------------------------------------------------------------------------------------
def _norm(E):
    E = np.asarray(E, np.float32)
    n = np.linalg.norm(E, axis=1, keepdims=True)
    n[n == 0] = 1
    return E / n


def reference():
    f = pd.read_parquet(OUT / "frame.parquet")[["submission_id", "year", "emb_row", "ACC", "cites", "top10"]]
    Em, found = C.load_masked_embedding(f)
    Ea = C.load_embedding(f, "abstract", "bge-small-en-v1.5")
    E = _norm(np.where(found[:, None], Em, Ea))
    a = pd.read_csv(C.DATA / "submission_authors.csv.gz", usecols=["submission_id", "declared_id_key"],
                    keep_default_na=False, na_values=[r"\N"]).dropna()
    a = a[a.submission_id.isin(f.submission_id)]
    return dict(f=f.reset_index(drop=True), E=E, year=f.year.to_numpy(), acc=f.ACC.to_numpy().astype(bool),
                N=f.year.value_counts().to_dict(), keys_of=a.groupby("submission_id").declared_id_key.apply(list).to_dict(),
                rows_of_key=_rows_of_key(a, f))


def _rows_of_key(a, f):
    idx = dict(zip(f.submission_id, range(len(f))))
    d = defaultdict(list)
    for s, k in zip(a.submission_id, a.declared_id_key):
        d[k].append(idx[s])
    return {k: np.array(v) for k, v in d.items()}


def heat(Eq, yq, R, block=2000):
    """loc1, loc2 (neighbours per 1,000 discovery submissions of t-1, t-2), loc_mom, nn_prev for query papers."""
    n = len(Eq)
    out = {c: np.full(n, np.nan) for c in ["loc1", "loc2", "loc_mom", "nn_prev"]}
    for t in np.unique(yq):
        qi = np.where(yq == t)[0]
        p1, p2 = np.where(R["year"] == t - 1)[0], np.where(R["year"] == t - 2)[0]
        if not len(p1):
            continue
        c1, c2 = np.zeros(len(qi)), np.zeros(len(qi))
        mx = np.full(len(qi), -1.0)
        for s in range(0, len(qi), block):
            Q = Eq[qi[s:s + block]]
            S1 = Q @ R["E"][p1].T
            c1[s:s + block] = (S1 >= TAU).sum(1)
            mx[s:s + block] = S1.max(1)
            if len(p2):
                S2 = Q @ R["E"][p2].T
                c2[s:s + block] = (S2 >= TAU).sum(1)
                mx[s:s + block] = np.maximum(mx[s:s + block], S2.max(1))
        out["loc1"][qi] = 1000 * c1 / R["N"][t - 1]
        out["nn_prev"][qi] = mx
        if len(p2):
            out["loc2"][qi] = 1000 * c2 / R["N"][t - 2]
            out["loc_mom"][qi] = np.log((c1 + 1) / R["N"][t - 1]) - np.log((c2 + 1) / R["N"][t - 2])
    return pd.DataFrame(out)


def team(sids, years, Eq, keys_of, R):
    """entry (newcomer / entrant / insider) and lprior_acc against the discovery panel of earlier submissions."""
    ent, lp, nprev = [], [], []
    for i, (s, t) in enumerate(zip(sids, years)):
        rows = [R["rows_of_key"][k] for k in keys_of.get(s, []) if k in R["rows_of_key"]]
        if rows:
            P = np.unique(np.concatenate(rows))
            P = P[R["year"][P] < t]
        else:
            P = np.array([], int)
        # max over authors of # earlier accepted discovery submissions
        accs = [int((R["acc"][r] & (R["year"][r] < t)).sum()) for r in rows]
        lp.append(np.log1p(max(accs)) if accs else 0.0)
        nprev.append(len(P))
        if not len(P):
            ent.append("newcomer")
        else:
            ent.append("insider" if float((R["E"][P] @ Eq[i]).max()) >= TAU else "entrant")
    return pd.DataFrame({"entry": ent, "lprior_acc": lp, "team_prev_n": nprev})


def calibrate():
    """Discovery measures + frozen per-year calibration (ECDF support, nn residual coefficients, top-10 thresholds)."""
    FROZEN.mkdir(parents=True, exist_ok=True)
    R = reference()
    H = heat(R["E"], R["year"], R)
    H["submission_id"], H["year"] = R["f"].submission_id.to_numpy(), R["year"]
    cal = {"tau": TAU, "years": {}}
    for t, g in H.groupby("year"):
        if g.loc1.notna().sum() == 0:
            continue
        ok = g.nn_prev.notna() & g.loc1.notna()
        coef = np.polyfit(np.log1p(g.loc1[ok]), g.nn_prev[ok], 2).tolist()
        res = g.nn_prev[ok] - np.polyval(coef, np.log1p(g.loc1[ok]))
        thr = R["f"][(R["f"].year == t) & (R["f"].top10 == 1)].cites.min()
        cal["years"][int(t)] = {"nn_coef": coef, "top10_min_cites": None if pd.isna(thr) else float(thr)}
        np.save(FROZEN / f"ecdf_{t}_loc1.npy", np.sort(g.loc1.dropna().to_numpy()))
        np.save(FROZEN / f"ecdf_{t}_nnres.npy", np.sort(res.to_numpy()))
        if g.loc_mom.notna().any():
            np.save(FROZEN / f"ecdf_{t}_mom.npy", np.sort(g.loc_mom.dropna().to_numpy()))
    (FROZEN / "calibration.json").write_text(json.dumps(cal, indent=1))
    H.to_parquet(FROZEN / "discovery_heat.parquet")
    print("calibrated", len(cal["years"]), "years")


def _ecdf(x, t, name):
    p = FROZEN / f"ecdf_{t}_{name}.npy"
    if not p.exists():
        return np.full(len(x), np.nan)
    ref = np.load(p)
    x = np.asarray(x, float)
    out = np.searchsorted(ref, x, side="right") / len(ref)
    out[np.isnan(x)] = np.nan
    return out


def derive(df):
    """Percentiles and residuals from the frozen calibration (identical for discovery and held-out)."""
    cal = json.loads((FROZEN / "calibration.json").read_text())["years"]
    df = df.copy()
    for c in ["size_p", "mom_p", "nnr_p", "nn_res"]:
        df[c] = np.nan
    for t, g in df.groupby("year"):
        if str(t) not in cal:
            continue
        coef = cal[str(t)]["nn_coef"]
        res = g.nn_prev - np.polyval(coef, np.log1p(g.loc1))
        df.loc[g.index, "nn_res"] = res
        df.loc[g.index, "size_p"] = _ecdf(g.loc1, t, "loc1")
        df.loc[g.index, "mom_p"] = _ecdf(g.loc_mom, t, "mom")
        df.loc[g.index, "nnr_p"] = _ecdf(res, t, "nnres")
        thr = cal[str(t)]["top10_min_cites"]
        if thr is not None and "cites" in df:
            df.loc[g.index, "top10"] = np.where(g.cites.notna(), (g.cites >= thr).astype(float), np.nan)
    df["rev"] = (df.ACC + df.REJ + df.WD) > 0
    df["acc_rev"] = np.where(df.rev, df.ACC.astype(float), np.nan)
    hit = np.where(df.rev & (df.year <= 2025), 0.0, np.nan)
    hit = np.where(df.top10 == 1, 1.0, hit)
    df["hit"] = np.where((df.ACC == 1) & df.top10.isna() & (df.year <= 2025), np.nan, hit)
    df["ins"] = (df.entry == "insider").astype(int)
    df["ent"] = (df.entry == "entrant").astype(int)
    df["y"] = np.log1p(df.cites)
    ter = lambda c: pd.cut(df[c], [-0.001, 1 / 3, 2 / 3, 1.0001], labels=["lo", "mid", "hi"])
    df["size3"], df["mom3"] = ter("size_p"), ter("mom_p")
    return df


# --------------------------------------------------------------------------------------------
# Frozen tests
# --------------------------------------------------------------------------------------------
def _fit(d, y, rhs, coef, null=0.0, direction=">"):
    m = pf.feols(f"{y} ~ {rhs} | year", data=d, vcov={"CRV1": "topic100"})
    t = m.tidy()
    k = [i for i in t.index if set(i.split(":")) == set(coef.split(":"))][0]
    b, se = float(t.loc[k, "Estimate"]), float(t.loc[k, "Std. Error"])
    G = d.topic100.nunique()
    z = (b - null) / se
    p1 = float(stats.t.sf(z, G - 1)) if direction == ">" else float(stats.t.cdf(z, G - 1))
    return {"coef": coef, "estimate": b, "se": se, "ci95": [b - 1.96 * se, b + 1.96 * se], "null": null,
            "direction": direction, "p_one_sided": p1, "n": int(m._N), "clusters": int(G), "base_rate": float(d[y].mean())}


def _sample(df, outcome, years, teams=False, experienced=False):
    d = df[df[outcome].notna() & df.year.between(*years) & df.mom_p.notna() & df.size_p.notna() & df.nnr_p.notna()]
    if experienced:
        d = d[d.entry.isin(["insider", "entrant"])]
    return d


BASE = "size_p + mom_p + nnr_p + log_authors"
TESTS = {
    "H1": dict(title="Readers reward momentum: P(top-10% cited | accepted) rises with ex-ante local momentum",
               y="top10", years=YEARS_CIT, rhs=BASE, coef="mom_p"),
    "H2": dict(title="Reviewers do not reward momentum: acceptance effect of momentum < +5 pp (non-inferiority)",
               y="acc_rev", years=YEARS_ACC, rhs=BASE, coef="mom_p", null=NN_BOUND, direction="<"),
    "H3": dict(title="Reviewers reward established neighbourhoods: acceptance rises with local size",
               y="acc_rev", years=YEARS_ACC, rhs=BASE, coef="size_p"),
    "H4": dict(title="The wave's payoff goes to insiders: momentum raises P(hit) more for insiders than entrants",
               y="hit", years=YEARS_TEAM_CIT, rhs="ins*mom_p + size_p + nnr_p + log_authors + lprior_acc", coef="ins:mom_p",
               experienced=True),
    "H5": dict(title="Switching areas costs acceptance: insiders vs entrants",
               y="acc_rev", years=YEARS_TEAM_ACC, rhs="ins + " + BASE + " + lprior_acc", coef="ins", experienced=True),
    "H6": dict(title="Naming pays in rising areas: NAME-title x momentum on P(top-10% | accepted)",
               y="top10", years=YEARS_CIT, rhs="G1_name*mom_p + size_p + nnr_p + log_authors", coef="G1_name:mom_p"),
}
SECONDARY = {
    "S1_nnr_acc": dict(y="acc_rev", years=YEARS_ACC, rhs=BASE, coef="nnr_p", direction="<"),
    "S2_nnr_top10": dict(y="top10", years=YEARS_CIT, rhs=BASE, coef="nnr_p"),
    "S3a_nnr_x_mom_acc": dict(y="acc_rev", years=YEARS_ACC, rhs="nnr_p*mom_p + size_p + log_authors", coef="nnr_p:mom_p", direction="<"),
    "S3b_nnr_x_mom_top10": dict(y="top10", years=YEARS_CIT, rhs="nnr_p*mom_p + size_p + log_authors", coef="nnr_p:mom_p"),
    "S4_size_x_mom_top10": dict(y="top10", years=YEARS_CIT, rhs="size_p*mom_p + nnr_p + log_authors", coef="size_p:mom_p"),
    "S5_name_x_mom_acc": dict(y="acc_rev", years=YEARS_ACC, rhs="G1_name*mom_p + size_p + nnr_p + log_authors", coef="G1_name:mom_p"),
    "S6_informative_x_size_logcites": dict(y="y", years=YEARS_CIT, rhs="G5b_informative*size_p + mom_p + nnr_p + log_authors + G1_name",
                                           coef="G5b_informative:size_p", direction="<"),
    "S7_entrant_vs_newcomer_acc": dict(y="acc_rev", years=YEARS_TEAM_ACC, rhs="ent + ins + " + BASE + " + lprior_acc", coef="ent"),
}


def holm(p):
    keys = sorted(p, key=p.get)
    m, adj, run = len(keys), {}, 0.0
    for i, k in enumerate(keys):
        run = max(run, min(1.0, (m - i) * p[k]))
        adj[k] = run
    return adj


def tables(df):
    """Descriptive decision tables (conditional probabilities), raw within the sample."""
    out = {}
    for name, (a, b, yrs) in {"entry_x_momentum": ("entry", "mom3", YEARS_TEAM_ACC), "size_x_momentum": ("size3", "mom3", YEARS_ACC)}.items():
        rows = []
        for o in ["acc_rev", "top10", "hit"]:
            d = df[df[o].notna() & df.year.between(*yrs) & df[a].notna() & df[b].notna()]
            g = d.groupby([a, b], observed=True)[o].agg(["mean", "size"]).reset_index()
            g["outcome"] = o
            rows.append(g)
        out[name] = pd.concat(rows).astype({a: str, b: str}).to_dict(orient="records")
    return out


def run_all(df):
    res = {}
    for k, s in TESTS.items():
        d = _sample(df, s["y"], s["years"], experienced=s.get("experienced", False))
        res[k] = dict(title=s["title"], **_fit(d, s["y"], s["rhs"], s["coef"], s.get("null", 0.0), s.get("direction", ">")))
    adj = holm({k: r["p_one_sided"] for k, r in res.items()})
    for k in res:
        res[k]["p_holm"] = adj[k]
        res[k]["verdict"] = "confirmed" if adj[k] < ALPHA else (
            "same direction, not significant" if (res[k]["estimate"] - res[k]["null"]) * (1 if res[k]["direction"] == ">" else -1) > 0
            else "not replicated")
    sec = {}
    for k, s in SECONDARY.items():
        d = _sample(df, s["y"], s["years"])
        sec[k] = _fit(d, s["y"], s["rhs"], s["coef"], 0.0, s.get("direction", ">"))
    return {"primary": res, "secondary": sec, "tables": tables(df)}


# --------------------------------------------------------------------------------------------
# Frames
# --------------------------------------------------------------------------------------------
def discovery_frame():
    u = C.load_analysis_frame(universe_cols=["submission_id", "year", "emb_row", "topic100", "llm_topic", "ACC", "REJ", "WD",
                                             "log_authors"]).reset_index(drop=True)
    fr = pd.read_parquet(OUT / "frame.parquet")[["submission_id", "cites", "G1_name", "G5b_informative"]]
    df = u[["submission_id", "year", "topic100", "llm_topic", "ACC", "REJ", "WD", "log_authors"]].merge(fr, on="submission_id")
    H = pd.read_parquet(FROZEN / "discovery_heat.parquet").drop(columns="year")
    df = df.merge(H, on="submission_id", how="left")
    R = reference()
    Ri = dict(zip(R["f"].submission_id, range(len(R["f"]))))
    q = df.year >= 2019
    T = team(df.submission_id[q].tolist(), df.year[q].tolist(), R["E"][[Ri[s] for s in df.submission_id[q]]], R["keys_of"], R)
    for c in T:
        df.loc[q, c] = T[c].to_numpy()
    for c in ["ACC", "REJ", "WD"]:
        df[c] = df[c].astype(int)
    df["split"] = "discovery"
    return derive(df)


def embed_bge(texts):
    import torch
    from sentence_transformers import SentenceTransformer
    torch.set_num_threads(4)
    m = SentenceTransformer("BAAI/bge-small-en-v1.5", device="cpu")
    m.max_seq_length = 512
    return m.encode(list(texts), batch_size=32, normalize_embeddings=True, convert_to_numpy=True,
                    show_progress_bar=False).astype(np.float32)


def raw_frame(s, a, split):
    """Held-out code path: raw submissions/author rows -> analysis frame (pools, title features, topics via the
    frozen discovery centroids, masked-abstract bge embeddings, heat against discovery, team, citations)."""
    import features as F
    from analyses import prereg_confirm as PC
    from analyses.features_v2 import mask_abstract
    from cites import match as MT
    fz = PC.load_frozen()
    df, counts = PC.prepare_frame(s, fz, split=split)
    leads = [F.lead_segment(t)[0] for t in df.title_nfkc]
    masked = [mask_abstract(x, l) for x, l in zip(df.abstract, leads)]
    t0 = time.time()
    Em = embed_bge(masked)
    Ea = embed_bge(df.abstract)
    Et = embed_bge(df.title)
    print(f"embedded {len(df)} x3 in {(time.time() - t0) / 60:.1f} min", flush=True)
    R = reference()
    H = heat(Em, df.year.to_numpy(), R)
    for c in H:
        df[c] = H[c].to_numpy()
    keys_of = a.dropna(subset=["declared_id_key"]).groupby("submission_id").declared_id_key.apply(list).to_dict()
    T = team(df.submission_id.tolist(), df.year.tolist(), Em, keys_of, R)
    for c in T:
        df[c] = T[c].to_numpy()
    df.loc[df.year < 2019, ["entry", "lprior_acc"]] = np.nan
    df["G1_name"] = df.name_primary.fillna(0).astype(int)
    cos = (Et * Ea).sum(1)
    # G5b standardised with the DISCOVERY mean/sd of the year (frozen in calibration_g5b.json)
    g5 = json.loads((FROZEN / "calibration_g5b.json").read_text())
    df["G5b_informative"] = [(c - g5[str(y)][0]) / g5[str(y)][1] for c, y in zip(cos, df.year)]
    # citations: same S2 venue cache and matching rule as cites/match.py
    S = MT.load_s2()
    acc = df[df.ACC == 1][["submission_id", "year", "title"]].copy()
    acc["key"] = acc.title.map(MT.norm)
    cand = acc.merge(S[["key", "year", "citationCount"]].rename(columns={"year": "s2_year"}), on="key", how="inner")
    cand = cand[(cand.s2_year <= cand.year) & (cand.s2_year >= cand.year - 2)]
    best = cand.sort_values("citationCount", ascending=False).drop_duplicates("submission_id")
    df = df.merge(best[["submission_id", "citationCount"]], on="submission_id", how="left")
    df["cites"] = np.where((df.ACC == 1) & (df.year <= 2025), df.citationCount, np.nan)
    df["split"] = split
    keep = ["submission_id", "year", "topic100", "llm_topic", "ACC", "REJ", "WD", "log_authors", "cites", "G1_name",
            "G5b_informative", "loc1", "loc2", "loc_mom", "nn_prev", "entry", "lprior_acc", "team_prev_n", "split"]
    return derive(df[keep]), counts


def calibrate_g5b():
    fr = pd.read_parquet(OUT / "frame.parquet")
    Et = _norm(C.load_embedding(fr, "title", "bge-small-en-v1.5"))
    Ea = _norm(C.load_embedding(fr, "abstract", "bge-small-en-v1.5"))
    fr["cos"] = (Et * Ea).sum(1)
    g = fr.groupby("year").cos.agg(["mean", "std"])
    (FROZEN / "calibration_g5b.json").write_text(json.dumps({str(k): [float(v["mean"]), float(v["std"])] for k, v in g.iterrows()}))


def sha256_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main(argv):
    stage = argv[0]
    if stage == "calibrate":
        calibrate()
        calibrate_g5b()
    elif stage == "dryrun":
        df = discovery_frame()
        df.to_parquet(OUT / "dryrun_frame.parquet")
        r = run_all(df)
        r["n_rows"] = len(df)
        (OUT / "dryrun.json").write_text(json.dumps(r, indent=1, default=float))
        for k, v in r["primary"].items():
            print(k, f"{v['estimate']:+.4f} (se {v['se']:.4f}) p1={v['p_one_sided']:.2g} holm={v['p_holm']:.2g} n={v['n']} {v['verdict']}")
        for k, v in r["secondary"].items():
            print(k, f"{v['estimate']:+.4f} (se {v['se']:.4f}) p1={v['p_one_sided']:.2g} n={v['n']}")
    elif stage == "check":
        # held-out code path on a 1,500-row discovery sample (2019-2025), compared with the discovery frame
        from analyses import prereg_confirm as PC
        s = PC.read_raw(C.DATA / "submissions.csv.gz")
        a = PC.read_raw(C.DATA / "submission_authors.csv.gz")
        s = s[s.year.between(2019, 2025)].sample(1500, random_state=7)
        a = a[a.submission_id.isin(s.submission_id)]
        h, _ = raw_frame(s, a, "check")
        d = pd.read_parquet(OUT / "dryrun_frame.parquet")
        m = h.merge(d, on="submission_id", suffixes=("_h", "_d"))
        rep = {"n": len(m)}
        for c in ["topic100", "ACC", "G1_name", "entry", "top10", "acc_rev"]:
            rep[c + "_agree"] = float((m[c + "_h"].astype(str) == m[c + "_d"].astype(str)).mean())
        for c in ["loc1", "loc_mom", "nn_prev", "size_p", "mom_p", "nnr_p", "lprior_acc", "G5b_informative", "log_authors", "cites"]:
            ok = m[c + "_h"].notna() & m[c + "_d"].notna()
            rep[c + "_corr"] = float(np.corrcoef(m[c + "_h"][ok], m[c + "_d"][ok])[0, 1])
            rep[c + "_maxabs"] = float((m[c + "_h"][ok] - m[c + "_d"][ok]).abs().max())
        (OUT / "pipeline_check.json").write_text(json.dumps(rep, indent=1))
        print(json.dumps(rep, indent=1))
    elif stage == "heldout":
        if GUARD.exists() or (OUT / "heldout.json").exists():
            raise SystemExit("held-out run already started; each test runs once")
        sub_path, auth_path = argv[1], argv[2]
        GUARD.write_text(json.dumps({"started": time.strftime("%Y-%m-%d %H:%M:%S"), "prereg_sha256": sha256_file(C.STUDY / "docs" / "FASHION_PREREG.md"),
                                     "submissions_sha256": sha256_file(sub_path), "authors_sha256": sha256_file(auth_path)}))
        from analyses import prereg_confirm as PC
        h, counts = raw_frame(PC.read_raw(sub_path), PC.read_raw(auth_path), "heldout")
        h.to_parquet(OUT / "heldout_frame.parquet")
        r = run_all(h)
        d = pd.read_parquet(OUT / "dryrun_frame.parquet")
        pooled = pd.concat([d, h[d.columns.intersection(h.columns)]], ignore_index=True)
        r["pooled_primary"] = {k: _fit(_sample(pooled, s["y"], s["years"], experienced=s.get("experienced", False)), s["y"], s["rhs"],
                                       s["coef"], s.get("null", 0.0), s.get("direction", ">")) for k, s in TESTS.items()}
        r["counts"] = counts.to_dict(orient="records")
        (OUT / "heldout.json").write_text(json.dumps(r, indent=1, default=float))
        for k, v in r["primary"].items():
            print(k, f"{v['estimate']:+.4f} (se {v['se']:.4f}) holm={v['p_holm']:.2g} {v['verdict']}")


if __name__ == "__main__":
    main(sys.argv[1:])
