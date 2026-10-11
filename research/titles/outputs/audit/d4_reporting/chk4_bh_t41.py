"""Reporting audit D4: BH (q=0.05) over all T4.1 continuation-ratio feature tests (PLAN s0 multiple-testing rule)."""
import pandas as pd, numpy as np
t = pd.read_csv("/home/user/cloud-research/research/titles/outputs/d4_filter/T4_1_continuation_ratio.csv").dropna(subset=["p"])
p = t.p.to_numpy(); m = len(p); o = np.argsort(p); q = np.empty(m)
q[o] = np.minimum.accumulate((p[o] * m / np.arange(1, m + 1))[::-1])[::-1]
t["q_bh"] = np.minimum(q, 1)
cited = [("2024-26","desk","NAME"),("2024-26","desk","question_opener"),("2024-26","desk","F26"),("2024-26","desk","emdash"),
         ("2024-26","desk","style_density"),("2024-26","decision","title_case"),("2024-26","decision","all_caps_title"),
         ("2024-26","desk","L_union"),("2024-26","exit","L_union"),("2018-23","exit","L_union"),("2018-23","decision","L_union"),
         ("2024-26","exit","all_caps_title"),("2024-26","exit","NAME"),("2024-26","decision","NAME")]
print("m =", m)
print(t.set_index(["era","stage","feature"]).loc[cited, ["OR","p","q_bh"]].round(4).to_string())
