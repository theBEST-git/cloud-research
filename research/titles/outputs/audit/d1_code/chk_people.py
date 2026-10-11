"""Audit D1-H1d: the newcomer dimension uses share_new_authors = share of keys with NO prior submission since the
start of the export (growing history window; profile keys only start in 2021, so 2021 is ~98% 'all-new').
 (1) DFL with a fixed 2-year lookback newcomer share (comparable 2023 vs 2024-26) vs the pipeline bins.
 (2) Shapley 'people' value: the P model is trained on 2021-23 where 2021 newcomer status is an artefact.
     Refit P / R1 / R1P fixed-window models (a) on 2022-23 only, (b) on 2021-23 with cells without newcomer bins,
     (c) on 2021-23 with fixed-lookback newcomer bins, and recompute v and Shapley shares (point estimates).
Writes nothing outside outputs/audit/d1_code.
"""
import json, sys, time, warnings
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from scipy import sparse
from scipy.special import expit
from common import read_table
from analyses import d1_content_cf as CF
from analyses import d1_decompose as DC

OUT = "/home/user/cloud-research/research/titles/outputs/audit/d1_code"
t0 = time.time()
df = DC.load()
a = read_table("submission_authors")[["submission_id", "year", "declared_id_key", "native_id_kind"]]
a = a[a.declared_id_key.notna()]
print(a.groupby("year").native_id_kind.value_counts(normalize=True).unstack().round(3))
seen = a.groupby("declared_id_key").year.apply(lambda s: set(s.unique())).to_dict()
def fixed_new(sub):
    y = int(sub.year.iloc[0])
    ks = sub.declared_id_key.unique()
    return float(np.mean([not ({y - 1, y - 2} & seen[k]) for k in ks]))
fn = a.groupby("submission_id").apply(fixed_new).rename("share_new_fixed2")
df = df.merge(fn, left_on="submission_id", right_index=True, how="left")
print("mean share_new (pipeline) vs fixed 2y lookback by year")
print(df.groupby("year")[["share_new_authors", "share_new_fixed2"]].mean().round(3).T.to_string())
df["newb_f2"] = DC.new_bin(df.share_new_fixed2)
res = {}
for name, cols in {"pipeline full": ["sizeb", "newb", "llm_topic"], "fixed-2y full": ["sizeb", "newb_f2", "llm_topic"],
                   "pipeline size x new": ["sizeb", "newb"], "fixed-2y size x new": ["sizeb", "newb_f2"]}.items():
    r = DC.dfl(df, cols, n_boot=200)
    res[f"dfl|{name}"] = {int(k): {"share": v["share"], "ci": v["share_ci"]} for k, v in r.items()}
    print(name, {k: round(v["share"], 3) for k, v in r.items()}, flush=True)

# ---------------- Shapley variants ----------------
yrs = df.year.to_numpy(); yv_ = df.name_primary.to_numpy()
r1 = CF.Reps(df, need=("R1",))
def cells(cols):
    return pd.factorize(df[cols].astype(str).agg("|".join, axis=1))[0]
def oh(code, idx):
    K = int(code.max()) + 1
    return sparse.csr_matrix((np.ones(len(idx), dtype=np.float32), (np.arange(len(idx)), code[idx])), shape=(len(idx), K))
def fit_v(rep, train, cellcode=None):
    tr = np.where(np.isin(yrs, train))[0]; te = np.where(np.isin(yrs, CF.POST_Y))[0]
    if rep in ("R1", "R1P"):
        Xtr, Xte, _ = r1.build("R1", tr, te)
    if rep == "P":
        Xtr, Xte = oh(cellcode, tr), oh(cellcode, te)
    if rep == "R1P":
        Xtr, Xte = sparse.hstack([Xtr, oh(cellcode, tr)]).tocsr(), sparse.hstack([Xte, oh(cellcode, te)]).tocsr()
    grid = CF.GRID_ONEHOT if rep == "P" else CF.GRID_SPARSE
    best, oof, ll = CF.cv_select(Xtr, yv_[tr], grid, rep)
    m = CF._lr(best, rep).fit(Xtr, yv_[tr])
    cal = yrs[tr] == 2023
    c = CF.shift_for(oof[cal], yv_[tr][cal].mean())
    s = m.decision_function(Xte)
    o0 = yv_[tr][cal].mean()
    out = {}
    for y in CF.POST_Y:
        mt = yrs[te] == y
        out[y] = float(expit(s[mt] + c).mean() - o0)
    return out, best
variants = {
    "pipeline (2021-23, size x new x llm)": ((2021, 2022, 2023), ["sizeb", "newb", "llm_topic"]),
    "train 2022-23, size x new x llm": ((2022, 2023), ["sizeb", "newb", "llm_topic"]),
    "2021-23, size x llm (no newcomer)": ((2021, 2022, 2023), ["sizeb", "llm_topic"]),
    "2021-23, size x new(fixed 2y) x llm": ((2021, 2022, 2023), ["sizeb", "newb_f2", "llm_topic"]),
}
o23 = yv_[yrs == 2023].mean()
v_r1 = {}
for vname, (train, cols) in variants.items():
    cc = cells(cols)
    if train not in v_r1:
        v_r1[train] = fit_v("R1", train)[0]
    vP, cP = fit_v("P", train, cc)
    vB, cB = fit_v("R1P", train, cc)
    vC = v_r1[train]
    sh = {}
    for y in CF.POST_Y:
        dl = yv_[yrs == y].mean() - o23
        phiC = 0.5 * (vC[y] + vB[y] - vP[y]); phiP = 0.5 * (vP[y] + vB[y] - vC[y])
        sh[y] = dict(people_first_people=vP[y] / dl, shapley_people=phiP / dl, shapley_content=phiC / dl,
                     residual=1 - vB[y] / dl, content_alone=vC[y] / dl)
    res[f"shapley|{vname}"] = sh
    print(vname, {y: {k: round(v, 3) for k, v in d.items()} for y, d in sh.items()}, f"{time.time() - t0:.0f}s", flush=True)
json.dump(res, open(f"{OUT}/people_check.json", "w"), indent=1, default=float)
print("done", f"{time.time() - t0:.0f}s")
