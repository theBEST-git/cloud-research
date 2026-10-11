"""Audit D1 / identification, check D: the H1c statistic telescopes. In the rolling design p_hat_y = obs_{y-1} +
content_step_y, so sum_{y in post} u_y = obs_2026 - obs_2023 - sum cs_post and sum_{pre} u_y = obs_2023 - obs_2018 -
sum cs_pre. Hence diff = (obs26 - obs23 - CSpost)/3 - (obs23 - obs18 - CSpre)/5: a year-level shock to the 2023 cohort
enters with weight -(1/3 + 1/5) = -8/15, 2026 with +1/3, 2018 with +1/5. The pre-registered paper bootstrap holds year
shocks fixed. Here: (1) verify the identity on the published steps; (2) add year-shock variance (tau from the REML
segmented meta-regression, LPM and logit scales) to the refit-bootstrap SE; (3) sensitivity of diff to the 2023 cohort
being at its smooth (segmented-model fitted) value instead of observed.
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
OUT = Path(__file__).resolve().parent
D1 = OUT.parents[1] / "d1_break"
S = pd.read_csv(D1 / "cf_rolling_steps.csv")
res = {}
for rep in ["R1", "R3", "R5"]:
    s = S[(S.rep == rep) & (S["pop"] == "U") & (S.outcome == "primary")].set_index("year")
    obs = s.obs.to_dict(); obs[2018] = float(s.loc[2019, "obs_calib"])
    cs = s.content_step
    pre, post = [2019, 2020, 2021, 2022, 2023], [2024, 2025, 2026]
    diff_direct = s.loc[post, "unexplained"].mean() - s.loc[pre, "unexplained"].mean()
    diff_tel = (obs[2026] - obs[2023] - cs[post].sum()) / 3 - (obs[2023] - obs[2018] - cs[pre].sum()) / 5
    res[rep] = {"diff_direct_pp": 100 * diff_direct, "diff_telescoped_pp": 100 * diff_tel}
# year-shock variance
re = json.loads((OUT / "ident_A2_re_metareg.json").read_text())
tau_lpm = re["U|lpm_adj"]["tau_year_shock"]
# logit tau converted at the relevant shares (2018 0.10, 2023 0.20, 2026 0.40)
tau_logit = re["U|logit_adj"]["tau_year_shock"]
w = {2018: 1 / 5, 2023: -(1 / 3 + 1 / 5), 2026: 1 / 3}
sh = {2018: 0.100, 2023: 0.203, 2026: 0.405}
sd_year_lpm = np.sqrt(sum(v ** 2 for v in w.values())) * tau_lpm
sd_year_logit = np.sqrt(sum((w[y] * tau_logit * sh[y] * (1 - sh[y])) ** 2 for y in w))
rb = json.loads((D1 / "refit_boot_R1.json").read_text())
se_boot = rb["diff_se"]
diff = res["R1"]["diff_direct_pp"] / 100
out = {}
for lab, sdy in [("tau_LPM_adj", sd_year_lpm), ("tau_logit_adj", sd_year_logit)]:
    se = np.sqrt(se_boot ** 2 + sdy ** 2)
    out[lab] = {"sd_diff_from_year_shocks_pp": 100 * sdy, "se_refit_boot_pp": 100 * se_boot, "se_total_pp": 100 * se,
                "z": diff / se, "p_one_sided": float(stats.norm.sf(diff / se)),
                "ci95_pp": [100 * (diff - 1.96 * se), 100 * (diff + 1.96 * se)],
                "holm_x3_p (H1c would be ranked 3rd of the 4 passing tests)": float(min(1, 3 * stats.norm.sf(diff / se)))}
res["year_shock_inflated_inference_R1"] = out
res["tau"] = {"lpm_pp": 100 * tau_lpm, "logit": tau_logit}
# (3) sensitivity: 2023 at its fitted segmented value. Use the raw-share LPM-scale year effects from A1: fitted values of
# the segmented-2024 model on raw shares (equal weights) and a local interpolation (mean of 2022 and 2024 logits)
yt = pd.DataFrame(json.loads((OUT / "ident_A_year_level_its.json").read_text())["year_table"]).set_index("year")
lg = yt.lg
interp = 1 / (1 + np.exp(-(lg[2022] + lg[2024]) / 2))
yrs = np.arange(2017, 2027); t = yrs - 2023; post_ = (yrs >= 2024).astype(float)
X = np.column_stack([np.ones(10), t, post_, post_ * t])
wls = 1 / yt.var_lg.to_numpy()
b = np.linalg.solve(X.T @ (X * wls[:, None]), X.T @ (wls * lg.to_numpy()))
fit23 = 1 / (1 + np.exp(-(X[6] @ b)))
s = S[(S.rep == "R1") & (S["pop"] == "U") & (S.outcome == "primary")].set_index("year")
o23 = float(s.loc[2023, "obs"])
for lab, v in [("logit-interpolation of 2022 and 2024", interp), ("segmented-2024 WLS fitted 2023", fit23)]:
    dd = (v - o23)
    res.setdefault("sens_2023_cohort", {})[lab] = {"obs_2023": o23, "counterfactual_2023": float(v),
                                                   "shift_pp": 100 * dd, "diff_pp_new": 100 * (diff - dd * 8 / 15)}
(OUT / "ident_D_h1c_telescoping.json").write_text(json.dumps(res, indent=1, default=float))
print(json.dumps(res, indent=1, default=float))
