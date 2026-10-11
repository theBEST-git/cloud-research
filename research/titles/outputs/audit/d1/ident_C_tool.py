"""Audit D1 / identification, check C: is the H1e tool bound identified?
C1  power of criterion (i): how large a NAME uplift among F=1 papers would be needed to push the F=0/all rise ratio
    below 0.85 (prediction) or 0.70 (falsification)? analytic + injection (flip NAME 0->1 among 2024-26 F=1 papers).
C2  the only TITLE-level LLM marker (title typography: U+2011 or letter-en dash-letter in the raw title) vs NAME,
    split by component and conditioned on the title having any intra-word dash at all (hyphenation opportunity),
    and the tool share it would imply if used in place of the abstract fingerprint.
C3  pre-period placebo delta: the same LPM in 2021-23 (pre-LLM false positives = 'LLM-ish' human writers) to sign
    the selection bias in delta.
"""
import json
import re
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import _core as C  # noqa: E402

warnings.filterwarnings("ignore")
OUT = Path(__file__).resolve().parent
df = C.load_analysis_frame(feature_cols=["name_primary", "f24_2", "f26", "title_typo", "F_any", "title_nbhyphen",
                                         "title_endash_compound", "name_compound", "n_words"],
                           universe_cols=["submission_id", "year", "title", "topic100", "log_authors", "llm_topic", "NA",
                                          "non_llm"])
for c in ["name_primary", "f24_2", "f26", "title_typo", "F_any", "title_nbhyphen", "title_endash_compound",
          "name_compound", "llm_topic", "NA", "non_llm"]:
    df[c] = df[c].astype(int)
df["F_d1"] = ((df.f24_2 + df.f26 + df.title_typo) > 0).astype(int)
res = {}

# ---------- C1 ----------
a, b = df[df.year == 2023], df[df.year == 2026]
pF = b.F_d1.mean()
pF23 = a.F_d1.mean()
rise_all = b.name_primary.mean() - a.name_primary.mean()
rise0 = b.loc[b.F_d1 == 0, "name_primary"].mean() - a.loc[a.F_d1 == 0, "name_primary"].mean()
# analytic: if F=1 papers in 2026 had NAME share s0_2026 + delta (and F was independent otherwise),
# all-rise = rise0 + pF * delta (2023 F=1 share ~ F=0 share). ratio = rise0 / (rise0 + pF * delta)
need = {thr: (rise0 / thr - rise0) / pF for thr in (0.85, 0.70)}
res["C1_analytic"] = {"share_F_2026": pF, "share_F_2023": pF23, "rise_all_pp": 100 * rise_all, "rise_F0_pp": 100 * rise0,
                      "delta_needed_for_ratio_below_0.85_pp": 100 * need[0.85],
                      "delta_needed_for_ratio_below_0.70_pp": 100 * need[0.70],
                      "max_possible_delta_pp_(F1 share->100%)": 100 * (1 - b.loc[b.F_d1 == 1, "name_primary"].mean())}
# injection: flip NAME 0->1 among 2026 F=1 papers to create a true uplift delta; recompute ratio and LPM delta
rng = np.random.default_rng(0)
inj = []
post = df[df.year.isin([2024, 2025, 2026])].copy()
post["ty"] = C.fe_interact(post.topic100, post.year)
for dl in (0.05, 0.10, 0.20, 0.30):
    d = df.copy()
    m = (d.year >= 2024) & (d.F_d1 == 1) & (d.name_primary == 0)
    base1 = d.loc[(d.year >= 2024) & (d.F_d1 == 1), "name_primary"].mean()
    p_flip = dl / (1 - base1)
    flip = m & (rng.random(len(d)) < p_flip)
    d.loc[flip, "name_primary"] = 1
    a2, b2 = d[d.year == 2023], d[d.year == 2026]
    r_all = b2.name_primary.mean() - a2.name_primary.mean()
    r0 = b2.loc[b2.F_d1 == 0, "name_primary"].mean() - a2.loc[a2.F_d1 == 0, "name_primary"].mean()
    pp = d[d.year >= 2024].copy()
    pp["ty"] = C.fe_interact(pp.topic100, pp.year)
    fr = C.feols(pp, "name_primary", ["F_d1", "log_authors"], fe=["ty"], cluster="topic100")
    inj.append({"injected_uplift_pp": 100 * dl, "ratio_F0_all": r0 / r_all, "lpm_delta_pp": 100 * fr.params["F_d1"],
                "tool_share_at_A0.39_using_lpm_delta": fr.params["F_d1"] * 0.39 / r_all,
                "true_tool_share_of_rise_2026": (r_all - r0) / r_all})
res["C1_injection"] = inj

# ---------- C2: title-level typography ----------
t = df.title.fillna("")
df["any_wordhyphen"] = C.rx_contains(t, r"[A-Za-z][\-‐‑–][A-Za-z]").astype(int)
df["ascii_hyphen_only"] = (C.rx_contains(t, r"[A-Za-z]-[A-Za-z]") & ~C.rx_contains(t, r"‑|[A-Za-z]–[A-Za-z]")).astype(int)
desc = df[df.year >= 2024].groupby("year").agg(n=("title_typo", "size"), typo=("title_typo", "sum"),
                                                nbh=("title_nbhyphen", "sum"), endash=("title_endash_compound", "sum"),
                                                anyhyph=("any_wordhyphen", "mean"))
res["C2_counts"] = desc.reset_index().to_dict(orient="records")
pre = df[df.year.isin([2021, 2022, 2023])]
res["C2_pre_typo_rate"] = {"title_typo_2021_23": float(pre.title_typo.mean()), "nbh_2021_23": int(pre.title_nbhyphen.sum()),
                           "endash_2021_23": int(pre.title_endash_compound.sum())}
post = df[df.year.isin([2024, 2025, 2026])].copy()
post["ty"] = C.fe_interact(post.topic100, post.year)
rows = []
for lab, d, var in [("title_typo, all 2024-26", post, "title_typo"),
                    ("U+2011 in title, all 2024-26", post, "title_nbhyphen"),
                    ("en-dash compound in title, all 2024-26", post, "title_endash_compound"),
                    ("title_typo | title has any intra-word dash", post[post.any_wordhyphen == 1], "title_typo"),
                    ("U+2011 | title has any intra-word dash", post[post.any_wordhyphen == 1], "title_nbhyphen"),
                    ("title_typo, 2026 only", post[post.year == 2026], "title_typo"),
                    ("title_typo | dash, 2026 only", post[(post.year == 2026) & (post.any_wordhyphen == 1)], "title_typo"),
                    ("title_typo | dash, NA pool", post[(post.NA == 1) & (post.any_wordhyphen == 1)], "title_typo"),
                    ("title_typo | dash, + n_words control (bad-control check)", post[post.any_wordhyphen == 1], "title_typo")]:
    ctr = ["log_authors"] + (["n_words"] if "n_words" in lab else [])
    fr = C.feols(d, "name_primary", [var] + ctr, fe=["ty"], cluster="topic100")
    ci = fr.conf_int()
    rows.append({"spec": lab, "n": int(fr.nobs), "n_marker": int(d[var].sum()),
                 "name_share_marker": float(d.loc[d[var] == 1, "name_primary"].mean()),
                 "name_share_nomarker": float(d.loc[d[var] == 0, "name_primary"].mean()),
                 "delta_pp": 100 * float(fr.params[var]), "lo_pp": 100 * float(ci.loc[var, "lo"]),
                 "hi_pp": 100 * float(ci.loc[var, "hi"]), "p": float(fr.pvalue[var])})
res["C2_title_typo_delta"] = rows
dname = rise_all
for r in rows[:1] + rows[3:4]:
    res.setdefault("C2_implied_tool_share", {})[r["spec"]] = {
        str(A): {"share": r["delta_pp"] / 100 * A / dname, "lo": r["lo_pp"] / 100 * A / dname,
                 "hi": r["hi_pp"] / 100 * A / dname} for A in (0.24, 0.39, 1.0)}
# pre-period placebo for the title-level marker (pre-LLM en-dash users, e.g. 'Kullback–Leibler')
pre = pre.copy()
pre["ty"] = C.fe_interact(pre.topic100, pre.year)
pre["any_wordhyphen"] = df.loc[pre.index, "any_wordhyphen"]
fr = C.feols(pre[pre.any_wordhyphen == 1], "name_primary", ["title_typo", "log_authors"], fe=["ty"], cluster="topic100")
res["C2_pre_placebo_title_typo|dash_2021_23"] = {"delta_pp": 100 * float(fr.params["title_typo"]),
                                                 "se_pp": 100 * float(fr.se["title_typo"]),
                                                 "n_marker": int(pre.loc[pre.any_wordhyphen == 1, "title_typo"].sum())}

# ---------- C3: pre-period placebo delta for the abstract fingerprint ----------
rows = []
for F in ["F_d1", "F_any", "f24_2", "f26"]:
    fr = C.feols(pre, "name_primary", [F, "log_authors"], fe=["ty"], cluster="topic100")
    ci = fr.conf_int()
    rows.append({"F": F, "years": "2021-23", "share_F": float(pre[F].mean()), "delta_pp": 100 * float(fr.params[F]),
                 "lo_pp": 100 * float(ci.loc[F, "lo"]), "hi_pp": 100 * float(ci.loc[F, "hi"])})
res["C3_pre_placebo_delta"] = rows
(OUT / "ident_C_tool.json").write_text(json.dumps(res, indent=1, default=float))
print(json.dumps(res, indent=1, default=float))
ex = df[(df.year >= 2024) & (df.title_typo == 1)].sample(25, random_state=1)[["year", "title", "name_primary"]]
print(ex.to_string())
