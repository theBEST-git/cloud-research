"""Audit D1-H1b/H1c content counterfactual (R1), three checks on the rolling / fixed / placebo designs:

 (a) reproduce the pipeline's p_hat (full-data model scores on test rows, shift from 5-fold OOF scores of y-1);
 (b) calibration-consistency: shift is estimated on OOF fold-model scores but applied to the FULL model's test
     scores. Replace the test scores by the 5 fold models' scores (average of probabilities) so calibration and
     prediction use the same models;
 (c) temporal confounding: the content logit has no training-year term, so any token whose prevalence trends
     within the 3-year training window picks up the within-window rise in NAME. Add (nearly unpenalised) training-
     year dummies, score test rows at the calibration year y-1, recalibrate as in the pipeline.

Run: cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python ../outputs/audit/d1_code/chk_content_model.py [R1]
"""
import json, sys, time, warnings
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from scipy import sparse
from scipy.special import expit
from sklearn.model_selection import StratifiedKFold
from analyses import d1_content_cf as CF

OUT = "/home/user/cloud-research/research/titles/outputs/audit/d1_code"
rep = sys.argv[1] if len(sys.argv) > 1 else "R1"
SCALE = 5.0
t0 = time.time()
df = CF.load_frame()
R = CF.Reps(df, need=(rep,))
yrs = df.year.to_numpy()
y = df.name_primary.to_numpy()
rows = []
for design in ["rolling", "fixed", "placebo"]:
    meta = json.loads((CF.SCORES / f"{rep}__U__primary__{design}.json").read_text())
    Sst = pd.read_parquet(CF.SCORES / f"{rep}__U__primary__{design}.parquet")
    for w in CF.windows(design):
        if w["name"] not in meta["windows"]:
            continue
        Cv = meta["windows"][w["name"]]["C"]
        tr = np.where(np.isin(yrs, w["train"]))[0]
        te = np.where(np.isin(yrs, w["test"]))[0]
        Xtr, Xte, info = R.build(rep, tr, te)
        ytr = y[tr]
        folds = list(StratifiedKFold(5, shuffle=True, random_state=0).split(np.zeros(len(tr)), ytr))
        cal = yrs[tr] == w["calib"]
        # year dummies (drop first training year), scaled so the L2 penalty on them is negligible
        tyears = sorted(set(yrs[tr]))
        def ydum(years_vec):
            cols = [(years_vec == yy).astype(np.float32) * SCALE for yy in tyears[1:]]
            return sparse.csr_matrix(np.column_stack(cols)) if cols else sparse.csr_matrix((len(years_vec), 0))
        Ytr_d = ydum(yrs[tr])
        Yte_d = ydum(np.full(len(te), w["calib"]))
        XtrY = sparse.hstack([Xtr, Ytr_d]).tocsr()
        XteY = sparse.hstack([Xte, Yte_d]).tocsr()
        res = {}
        for variant, (A, B) in {"base": (Xtr, Xte), "yearFE": (XtrY, XteY)}.items():
            oof = np.zeros(len(tr))
            te_fold = []
            for trf, vaf in folds:
                m = CF._lr(Cv, rep).fit(A[trf], ytr[trf])
                oof[vaf] = m.decision_function(A[vaf])
                te_fold.append(m.decision_function(B))
            m = CF._lr(Cv, rep).fit(A, ytr)
            s_full = m.decision_function(B)
            c = CF.shift_for(oof[cal], ytr[cal].mean())
            res[variant] = dict(oof=oof, s_full=s_full, te_fold=np.array(te_fold), c=c)
        obs_cal = float(ytr[cal].mean())
        for yv in w["test"]:
            mt = yrs[te] == yv
            obs = float(y[te][mt].mean())
            b = res["base"]; f = res["yearFE"]
            ph_base = float(expit(b["s_full"][mt] + b["c"]).mean())
            ph_ens = float(expit(b["te_fold"][:, mt] + b["c"]).mean())
            ph_yfe = float(expit(f["s_full"][mt] + f["c"]).mean())
            ph_yfe_ens = float(expit(f["te_fold"][:, mt] + f["c"]).mean())
            # pipeline value for comparison
            st = Sst[(Sst.window == w["name"]) & (Sst.role == "test") & (Sst.year == yv)]
            cs = Sst[(Sst.window == w["name"]) & (Sst.role == "calib")]
            ph_pipe = float(expit(st.score.to_numpy() + CF.shift_for(cs.score.to_numpy(), cs.y.mean())).mean())
            rows.append(dict(design=design, window=w["name"], year=int(yv), C=Cv, obs=obs, obs_calib=obs_cal,
                             p_pipeline=ph_pipe, p_base=ph_base, p_fold_ens=ph_ens, p_yearFE=ph_yfe,
                             p_yearFE_ens=ph_yfe_ens))
        print(design, w["name"], f"{time.time() - t0:.0f}s", flush=True)
D = pd.DataFrame(rows)
D.to_csv(f"{OUT}/content_model_check_{rep}.csv", index=False)
pd.set_option("display.width", 250)
print(D.round(4).to_string())

def summarise(D, col):
    out = {}
    r = D[D.design == "rolling"].set_index("year")
    u = r.obs - r[col]
    cs = r[col] - r.obs_calib
    st = r.obs - r.obs_calib
    pre, post = [2019, 2020, 2021, 2022, 2023], [2024, 2025, 2026]
    out["u_pre"], out["u_post"] = float(u[pre].mean()), float(u[post].mean())
    out["diff"], out["ratio"] = out["u_post"] - out["u_pre"], out["u_post"] / out["u_pre"]
    out["rolling_content_share"] = float(cs[post].sum() / st[post].sum())
    out["content_step_pre_mean"] = float(cs[pre].mean())
    f = D[D.design == "fixed"].set_index("year")
    for yy in (2024, 2025, 2026):
        out[f"fixed_share_{yy}"] = float((f.loc[yy, col] - f.loc[yy, "obs_calib"]) / (f.loc[yy, "obs"] - f.loc[yy, "obs_calib"]))
    p = D[D.design == "placebo"].set_index("year")
    out["placebo_share_2023"] = float((p.loc[2023, col] - p.loc[2023, "obs_calib"]) / (p.loc[2023, "obs"] - p.loc[2023, "obs_calib"]))
    return out
summ = {col: summarise(D, col) for col in ["p_pipeline", "p_base", "p_fold_ens", "p_yearFE", "p_yearFE_ens"]}
print(pd.DataFrame(summ).round(4).to_string())
json.dump(summ, open(f"{OUT}/content_model_check_{rep}.json", "w"), indent=1)
print(f"done {time.time() - t0:.0f}s")
