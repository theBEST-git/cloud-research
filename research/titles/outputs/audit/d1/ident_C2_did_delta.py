"""Audit D1 / identification, check C (part 2): selection-corrected delta. Pre-LLM (2021-23) papers that carry the
abstract fingerprint are human writers with an 'LLM-like' register; if that register predicts naming on its own, the
post-period delta mixes selection with tool. DiD: NAME ~ F + F x post + log_authors | topic100 x year, 2021-26,
clustered by topic100; delta_DiD = coef(F x post). Also the precision-corrected delta (pre-period F rate = false
positives with zero effect): delta / precision_y.
"""
import json, sys, warnings
from pathlib import Path
import numpy as np
import pandas as pd
sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C
warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
df = C.load_analysis_frame(feature_cols=["name_primary", "f24_2", "f26", "title_typo", "F_any"],
                           universe_cols=["submission_id", "year", "topic100", "log_authors"])
for c in ["name_primary", "f24_2", "f26", "title_typo", "F_any"]:
    df[c] = df[c].astype(int)
df["F_d1"] = ((df.f24_2 + df.f26 + df.title_typo) > 0).astype(int)
d = df[df.year >= 2021].copy()
d["post"] = (d.year >= 2024).astype(int)
d["ty"] = C.fe_interact(d.topic100, d.year)
res = {}
dname = df.loc[df.year == 2026, "name_primary"].mean() - df.loc[df.year == 2023, "name_primary"].mean()
for F in ["F_d1", "F_any"]:
    d[f"{F}_post"] = d[F] * d.post
    r = C.feols(d, "name_primary", [F, f"{F}_post", "log_authors"], fe=["ty"], cluster="topic100")
    ci = r.conf_int()
    k = f"{F}_post"
    fp = df.loc[df.year.isin([2021, 2022, 2023]), F].mean()
    prec = {int(y): float(max(0, df.loc[df.year == y, F].mean() - fp) / df.loc[df.year == y, F].mean()) for y in (2024, 2025, 2026)}
    res[F] = {"delta_pre_pp": 100 * float(r.params[F]), "delta_DiD_pp": 100 * float(r.params[k]),
              "DiD_lo_pp": 100 * float(ci.loc[k, "lo"]), "DiD_hi_pp": 100 * float(ci.loc[k, "hi"]),
              "precision_by_year_(1-FP/share)": prec,
              "tool_share_A0.39_DiD": float(r.params[k] * 0.39 / dname), "tool_share_A0.39_DiD_hi": float(ci.loc[k, "hi"] * 0.39 / dname),
              "tool_share_A1.0_DiD_hi": float(ci.loc[k, "hi"] * 1.0 / dname)}
print(json.dumps(res, indent=1))
(OUT / "ident_C2_did_delta.json").write_text(json.dumps(res, indent=1))
