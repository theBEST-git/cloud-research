"""Reporting audit of D1 (outputs/d1_break/RESULTS.md): recompute a sample of reported numbers
from the raw analysis frame and from the CSV/JSON outputs. Read-only on the direction's files.

Run: cd research/titles/src && OMP_NUM_THREADS=1 /home/user/venv/bin/python -m analyses._audit_tmp  (or as a file)
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path("/home/user/cloud-research/research/titles")
sys.path.insert(0, str(ROOT / "src"))
from analyses import _core as C  # noqa: E402

D1 = ROOT / "outputs" / "d1_break"
OUT = ROOT / "outputs" / "audit" / "d1_reporting"
res = {}

# ---------------------------------------------------------------- raw frame checks
df = C.load_analysis_frame(
    feature_cols=["name_primary", "f24_2", "f24", "f26", "title_typo", "F_any"],
    universe_cols=["submission_id", "year", "llm_topic", "NA", "declared_name_count", "share_new_authors",
                   "non_llm"])
for c in ["name_primary", "f24_2", "f24", "f26", "title_typo", "F_any", "llm_topic", "NA", "non_llm"]:
    df[c] = df[c].astype(int)
df["F_d1"] = ((df.f24_2 == 1) | (df.f26 == 1) | (df.title_typo == 1)).astype(int)
res["n_U"] = int(len(df))
sh = df.groupby("year").name_primary.mean()
res["name_share_by_year"] = sh.round(4).to_dict()
res["dNAME_2023_2026_pp"] = round(100 * (sh[2026] - sh[2023]), 2)
g = df[df.year.isin([2023, 2026])].groupby("year")
res["mean_declared_authors"] = g.declared_name_count.mean().round(3).to_dict()
res["mean_share_new"] = g.share_new_authors.mean().round(3).to_dict()
res["llm_topic_share"] = g.llm_topic.mean().round(3).to_dict()
res["F_d1_share_by_year"] = df[df.year >= 2023].groupby("year").F_d1.mean().round(4).to_dict()
res["missing_share_new_by_year"] = df[df.share_new_authors.isna()].groupby("year").size().to_dict()
res["name_F0_F1_2023_2026"] = df[df.year.isin([2023, 2026])].groupby(["year", "F_d1"]).name_primary.mean() \
    .round(4).rename(lambda x: str(x)).to_dict() if False else \
    {f"{y}|F{f}": round(v, 4) for (y, f), v in df[df.year.isin([2023, 2026])].groupby(["year", "F_d1"]).name_primary.mean().items()}
res["n_by_subset_2024_26"] = {
    "U": int((df.year >= 2024).sum()), "NA": int(((df.year >= 2024) & (df.NA == 1)).sum()),
    "non_llm": int(((df.year >= 2024) & (df.non_llm == 1)).sum())}
# title_typo overlap with NAME (mechanical-correlation check for the tool fingerprint)
post = df[df.year >= 2024]
res["NAME_rate_by_title_typo_2024_26"] = post.groupby("title_typo").name_primary.mean().round(3).to_dict()
res["title_typo_n_2024_26"] = int(post.title_typo.sum())

# ---------------------------------------------------------------- DFL primary point estimate (recomputed)
def sbin(n):
    return pd.cut(n, [-1, 2, 3, 4, 5, 7, 10**6], labels=["1-2", "3", "4", "5", "6-7", "8+"]).astype(str)


def nbin(s):
    return np.select([s.eq(0), s.gt(0) & s.le(0.5), s.gt(0.5)], ["0", "(0,.5]", "(.5,1]"], "NA")


d = df[df.year.isin([2023, 2026])].copy()
d["cell"] = sbin(d.declared_name_count) + "|" + nbin(d.share_new_authors) + "|" + d.llm_topic.astype(str)
d = d[~d.cell.str.contains("NA")]
ref, tgt = d[d.year == 2023], d[d.year == 2026]
pref = ref.cell.value_counts(normalize=True)
rate_t = tgt.groupby("cell").name_primary.mean()
cf = float((pref * rate_t.reindex(pref.index).fillna(tgt.name_primary.mean())).sum())
res["dfl_primary_2026_recomputed"] = round((tgt.name_primary.mean() - cf) /
                                           (tgt.name_primary.mean() - ref.name_primary.mean()), 4)
res["dfl_dropped_rows_2023_2026"] = int(df[df.year.isin([2023, 2026])].shape[0] - d.shape[0])

# ---------------------------------------------------------------- H1c year-level tests (from by_year u)
R = json.load(open(D1 / "results.json"))
u = {r["year"]: r["unexplained"] for r in R["H1c"]["by_year"]}
pre = np.array([u[y] for y in range(2019, 2024)])
pos = np.array([u[y] for y in range(2024, 2027)])
allu = np.array(list(pre) + list(pos))
obs = pos.mean() - pre.mean()
cnt = 0
for comb in itertools.combinations(range(8), 3):
    m = np.zeros(8, bool); m[list(comb)] = True
    cnt += (allu[m].mean() - allu[~m].mean()) >= obs - 1e-12
res["H1c_perm_p_recomputed"] = round(cnt / 56, 4)
w = stats.ttest_ind(pos, pre, equal_var=False, alternative="greater")
res["H1c_welch_recomputed"] = {"t": round(float(w.statistic), 3), "p": round(float(w.pvalue), 3)}
res["H1c_content_step_means_pp"] = {
    "pre": round(100 * np.mean([r["content_step"] for r in R["H1c"]["by_year"] if r["year"] < 2024]), 2),
    "post": round(100 * np.mean([r["content_step"] for r in R["H1c"]["by_year"] if r["year"] >= 2024]), 2)}
res["H1c_observed_step_means_pp"] = {
    "pre": round(100 * np.mean([r["step"] for r in R["H1c"]["by_year"] if r["year"] < 2024]), 2),
    "post": round(100 * np.mean([r["step"] for r in R["H1c"]["by_year"] if r["year"] >= 2024]), 2)}

# ---------------------------------------------------------------- refit bootstrap: ratio thresholds
rb = pd.read_csv(D1 / "refit_boot_R1.csv")
ub = {y: rb[f"obs_{y}"] - rb[f"phat_{y}"] for y in range(2019, 2027)}
upre = sum(ub[y] for y in range(2019, 2024)) / 5
upost = sum(ub[y] for y in range(2024, 2027)) / 3
ratio = upost / upre
res["refit_boot"] = {"B": int(len(rb)), "diff_ci": [round(float(x), 4) for x in np.percentile(upost - upre, [2.5, 97.5])],
                     "ratio_ci": [round(float(x), 3) for x in np.percentile(ratio, [2.5, 97.5])],
                     "P_ratio_lt_1.2": round(float(np.mean(ratio < 1.2)), 4),
                     "P_ratio_lt_1.5": round(float(np.mean(ratio < 1.5)), 4),
                     "P_upre_le_0": round(float(np.mean(upre <= 0)), 4)}
# conditional ratio CI rounding
res["H1c_ratio_ci_conditional_raw"] = R["H1c"]["ratio_ci_conditional"]

# ---------------------------------------------------------------- Holm recompute
raw = R["holm"]["raw_p"]
order = sorted(raw, key=raw.get)
adj, run = {}, 0.0
for i, k in enumerate(order):
    run = max(run, min(1.0, (len(order) - i) * raw[k]))
    adj[k] = round(run, 5)
res["holm_recomputed"] = adj

# ---------------------------------------------------------------- rounding spot checks vs RESULTS.md
txt = (D1 / "RESULTS.md").read_text()
spot = {
    "R1@0.5 rolling share (T1_2)": (pd.read_csv(D1 / "T1_2_representations.csv").query(
        "rep=='R1@0.5' and design=='rolling'").content_share.iloc[0], "0.476" in txt),
    "F_any 2024 F0 ratio": (R["H1e"]["f0_rise"]["F_any"]["2024"]["ratio_F0_all"], "0.86 [0.73, 0.96]" in txt),
    "content step 2025 pp": (100 * [r for r in R["H1c"]["by_year"] if r["year"] == 2025][0]["content_step"], "+5.7" in txt),
    "fixed new-topic gap pp": (100 * R["new_topic_placebo"]["R1|fixed_2024_26"]["gap_diff"], "8.9 pp [7.7, 10.0]" in txt),
    "conditional ratio lo": (R["H1c"]["ratio_ci_conditional"][0], "[1.22, 3.14]" in txt),
}
res["spot_checks"] = {k: {"value": round(float(v), 4), "string_in_RESULTS": s} for k, (v, s) in spot.items()}

(OUT / "chk_numbers.json").write_text(json.dumps(res, indent=1, default=str))
print(json.dumps(res, indent=1, default=str))
