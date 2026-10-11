"""Audit D1 / identification, check B2: is the R1 'content' share partly abstract RHETORIC (promotional / artefact-
announcement / LLM-polish vocabulary) that co-moves with title fashion rather than research content?

(a) Attribution: fixed-window R1 model (train 2021-23, chosen C, same vectoriser). Contribution of each feature to the
    2023 -> 2026 change in the mean linear score = coef_j * (mean x_j,2026 - mean x_j,2023); grouped by category.
(b) Refit R1 with every uni/bigram containing a token from the rhetoric lists removed ('R1s', substantive-only), in the
    fixed window and the rolling design (same folds, same C as the published R1 window), and recompute the content
    shares, u_pre / u_post. Lists are fixed a priori below (not tuned on results).
"""
import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.special import expit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d1_content_cf as CF  # noqa: E402

warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
t0 = time.time()

PROMO = set("""achieve achieves achieving achieved outperform outperforms outperforming outperformed state art sota
significantly significant consistently superior superiority substantially substantial remarkable remarkably notably
effective effectively extensive extensively comprehensive comprehensively competitive impressive promising surpass
surpasses surpassing surpassed improves improved improving improvement improvements gains boosts strong stronger
demonstrate demonstrates demonstrating demonstrated showcase showcases showcasing highlights underscores pivotal crucial
excellent exceptional unprecedented powerful versatile seamless seamlessly efficiently respectively existing""".split())
ANNOUNCE = set("""introduce introduces introducing we propose proposes proposed present presents presenting framework
frameworks novel named called dubbed termed coined paper work our ours this textbf textsc emph texttt textit mathtt
mathsf code github available release released publicly https http com io project page""".split())
# LLM-polish vocabulary: RARE21 + R24/R26 stems (lexicons.json) as prefixes
LLM_STEMS = ("delve", "intricat", "showcas", "pivotal", "underscor", "realm", "meticulous", "commendabl", "innovativ",
             "garner", "harness", "encompass", "noteworth", "unveil", "bolster", "adept", "formidabl", "endeavo",
             "groundbreak", "multifacet", "unparallel", "enhanc", "leverag", "unleash", "empower", "elevat", "boost",
             "unlock", "unifi", "unify", "beyond", "bridg", "principled", "refram", "genuine", "brittle", "auditabl",
             "sharply", "seamless", "robustly")
# do not drop 'we' alone (function word) -- 'we propose' etc are caught via 'propose'; keep 'propose' in ANNOUNCE
ANNOUNCE |= {"propose"}


def category(tok: str) -> str:
    if tok in ANNOUNCE:
        return "announce"
    if tok in PROMO:
        return "promo"
    if tok.startswith(LLM_STEMS):
        return "llm_style"
    return "other"


def feat_category(f: str) -> str:
    cats = [category(t) for t in f.split()]
    for c in ("announce", "promo", "llm_style"):
        if c in cats:
            return c
    return "other"


df = CF.load_frame()
texts = CF.r1_texts(df)
yrs = df.year.to_numpy()
Y = df.name_primary.to_numpy()
meta_roll = json.loads((CF.SCORES / "R1__U__primary__rolling.json").read_text())
meta_fix = json.loads((CF.SCORES / "R1__U__primary__fixed.json").read_text())


def lr(Cv):
    return LogisticRegression(C=Cv, max_iter=5000, tol=1e-5)


def fit_window(train_years, test_years, calib, Cv, drop_cats=()):
    tr = np.where(np.isin(yrs, train_years))[0]
    te = np.where(np.isin(yrs, test_years))[0]
    vec = TfidfVectorizer(min_df=5, max_df=0.5, ngram_range=(1, 2), sublinear_tf=True, max_features=50000,
                          dtype=np.float32)
    Xtr = vec.fit_transform(texts[tr])
    feats = vec.get_feature_names_out()
    cats = np.array([feat_category(f) for f in feats])
    if drop_cats:
        keep = [f for f, c in zip(feats, cats) if c not in drop_cats]
        vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, vocabulary=keep, dtype=np.float32)
        Xtr = vec.fit_transform(texts[tr])
        feats = vec.get_feature_names_out()
        cats = np.array([feat_category(f) for f in feats])
    Xte = vec.transform(texts[te])
    ytr = Y[tr]
    folds = list(StratifiedKFold(5, shuffle=True, random_state=0).split(np.zeros(len(tr)), ytr))
    oof = np.zeros(len(tr))
    for a, b in folds:
        oof[b] = lr(Cv).fit(Xtr[a], ytr[a]).decision_function(Xtr[b])
    m = lr(Cv).fit(Xtr, ytr)
    cal = yrs[tr] == calib
    c = CF.shift_for(oof[cal], ytr[cal].mean())
    st = m.decision_function(Xte)
    out = {}
    for yv in test_years:
        mm = yrs[te] == yv
        out[yv] = dict(obs=float(Y[te][mm].mean()), p_hat=float(expit(st[mm] + c).mean()), obs_calib=float(ytr[cal].mean()))
    return out, m, vec, cats, Xtr, tr


res = {}
# (a) attribution on the fixed-window model
out, m, vec, cats, Xtr, tr = fit_window((2021, 2022, 2023), (2024, 2025, 2026), 2023, meta_fix["windows"]["fixed"]["C"])
X23 = Xtr[yrs[tr] == 2023]
X26 = vec.transform(texts[yrs == 2026])
dmean = np.asarray(X26.mean(0)).ravel() - np.asarray(X23.mean(0)).ravel()
contrib = m.coef_.ravel() * dmean
tot = contrib.sum()
A = pd.DataFrame({"feature": vec.get_feature_names_out(), "cat": cats, "coef": m.coef_.ravel(), "dmean": dmean,
                  "contrib": contrib})
res["a_total_dscore_2023_2026"] = float(tot)
res["a_share_by_category"] = (A.groupby("cat").contrib.sum() / tot).round(3).to_dict()
res["a_n_features_by_category"] = A.cat.value_counts().to_dict()
res["a_top30_contributors"] = A.sort_values("contrib", ascending=False).head(30)[["feature", "cat", "coef", "dmean", "contrib"]].round(4).to_dict(orient="records")
A.sort_values("contrib", ascending=False).to_csv(OUT / "ident_B2_feature_contrib_fixed_2023_2026.csv", index=False)
res["a_fixed_share_2026_orig"] = (out[2026]["p_hat"] - out[2026]["obs_calib"]) / (out[2026]["obs"] - out[2026]["obs_calib"])
print(json.dumps({k: v for k, v in res.items() if k != "a_top30_contributors"}, indent=1), flush=True)
print(pd.DataFrame(res["a_top30_contributors"]).to_string(), flush=True)

# (b) refits without rhetoric
for lab, drop in [("R1s (no announce/promo/llm_style)", ("announce", "promo", "llm_style")),
                  ("R1 minus llm_style only", ("llm_style",))]:
    o, *_ = fit_window((2021, 2022, 2023), (2024, 2025, 2026), 2023, meta_fix["windows"]["fixed"]["C"], drop)
    entry = {"fixed_share": {y: (o[y]["p_hat"] - o[y]["obs_calib"]) / (o[y]["obs"] - o[y]["obs_calib"]) for y in o}}
    steps = []
    for yv in range(2019, 2027):
        w = meta_roll["windows"][f"roll{yv}"]
        o2, *_ = fit_window(tuple(range(yv - 3, yv)), (yv,), yv - 1, w["C"], drop)
        r = o2[yv]
        steps.append(dict(year=yv, step=r["obs"] - r["obs_calib"], content=r["p_hat"] - r["obs_calib"], u=r["obs"] - r["p_hat"]))
        print(f"{lab} roll{yv}: content={100*(r['p_hat']-r['obs_calib']):.2f} u={100*(r['obs']-r['p_hat']):.2f} {time.time()-t0:.0f}s", flush=True)
    S = pd.DataFrame(steps).set_index("year")
    pre, post = list(range(2019, 2024)), [2024, 2025, 2026]
    entry.update({"rolling_content_share": float(S.loc[post, "content"].sum() / S.loc[post, "step"].sum()),
                  "u_pre_pp": float(100 * S.loc[pre, "u"].mean()), "u_post_pp": float(100 * S.loc[post, "u"].mean()),
                  "diff_pp": float(100 * (S.loc[post, "u"].mean() - S.loc[pre, "u"].mean())),
                  "ratio": float(S.loc[post, "u"].mean() / S.loc[pre, "u"].mean()),
                  "content_steps_pp": {int(k): round(100 * v, 2) for k, v in S.content.items()}})
    res[f"b|{lab}"] = entry
    print(lab, json.dumps(entry, indent=1), flush=True)
(OUT / "ident_B2_rhetoric.json").write_text(json.dumps(res, indent=1, default=float))
print(f"done {time.time()-t0:.0f}s")
