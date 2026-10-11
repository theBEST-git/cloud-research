"""Reporting audit D4: (a) ITS / colon-premium ratio-of-OR scale artefact in the H4e atlas;
(b) Holm over a D4 confirmatory family using the reported one-sided p-values; (c) post hoc H4c baseline vs 0.9 rule."""
import json, numpy as np, pandas as pd
from pathlib import Path
D = Path("/home/user/cloud-research/research/titles/outputs/d4_filter")
r = json.loads((D / "results.json").read_text())
its = pd.read_csv(D / "its_pools.csv"); its = its[its.spec.eq("primary")].set_index("pool")
a = pd.read_csv(D / "atlas.csv").set_index("label")
row = a.loc["ITS slope-change OR (NAME)"]
print("ITS logOR all(s0) =", np.log(row.T_s0).round(4), " accepted(s3) =", np.log(row.T_s3).round(4),
      " accepted/all on log scale =", (np.log(row.T_s3) / np.log(row.T_s0)).round(3))
print("ACC pool slope-change p =", its.loc["ACC", "slope_change_p"].round(3), "; REJ p =", its.loc["REJ", "slope_change_p"].round(4))
cp = a.loc["Colon premium OR, 2024-26 (decided-only)"]
print("colon premium logOR all =", np.log(cp.T_s0).round(4), " decided-only =", np.log(cp.T_s2).round(4),
      " ratio of log-ORs =", (np.log(cp.T_s2) / np.log(cp.T_s0)).round(2))
# Holm over D4 confirmatory tests (one-sided p as reported); family = H4a TOST, H4b L total, H4b O total, H4b L predec, H4c 2024 (ratio<=0.85), H4d diff
h = r["hypotheses"]
tost = h["H4a"]["estimates"]["pooled_2024_26_std"]  # 90% CI inside margins -> TOST p < .05; use 0 as optimistic
fam = {"H4a_TOST": 0.0, "H4b_L_total": h["H4b"]["estimates"]["L_union_total"]["p_ge1"],
       "H4b_O_total": h["H4b"]["estimates"]["O_union_total"]["p_ge1"],
       "H4b_L_predec": h["H4b"]["estimates"]["L_union_predec"]["p_ge1"],
       "H4c_2024_ratio_le_0.85": h["H4c"]["estimates"]["ratio_acc_all"]["2024"]["p_ge_0p85"],
       "H4d_diff": h["H4d"]["estimates"]["diff_pp"]["p_one_sided"]}
ps = sorted(fam.items(), key=lambda kv: kv[1]); m = len(ps); stop = False
for i, (k, p) in enumerate(ps):
    thr = 0.05 / (m - i); rej = (p < thr) and not stop; stop = stop or not rej
    print(f"Holm {k:24s} p={p:.4f} thr={thr:.4f} reject={rej}")
k = pd.read_csv(D / "kobak_bounds.csv")
x = k[(k.marker == "F24") & (k.baseline == "max2122") & (k.set == "ratio_acc_all")][["year", "bound", "lo95", "hi95"]]
print("post hoc max(2021,2022) ratios:\n", x.to_string(index=False), "\n>=0.9 in 2024 and 2025:",
      bool((x.set_index("year").loc[["2024", "2025"], "bound"] >= 0.9).all()))
