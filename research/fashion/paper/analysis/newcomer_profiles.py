"""Outcome-free, descriptive (tier E): what the newcomer reversal is made of.

Added during the paper revision (not pre-registered; 2026-11-04). Splits the registered newcomer contrast (H2b/H2c)
into three author profiles within the same k100 topic x year cell:
  first_time          no author ID has any earlier ICLR submission (ph5_fmwave.features().first_time)
  returning_newcomer  a topic newcomer paper (no author has an earlier submission in this topic) with an author who
                      has one in another topic
  incumbent           some author has an earlier submission in this topic (newcomer == 0)
Outcomes: method, measurement (dataset/benchmark or evaluation) and the six primary classes, from the LLM labels.
Population: the RQ2 population (k100, 2019-2026, has_author_key), discovery papers only.
Estimator: ols.fe_ols, k100 topic x year FE absorbed, CR1 SE clustered by topic, t(G - 1). Two parametrisations give
all three contrasts with their own SEs: (newcomer, first_time) and (first_time, returning_newcomer), reference
incumbent in the second. Each with and without log2 team size (capped at 16, as posthoc.add_columns).
Also by era (2019-20, 2021-23, 2024-26) for method and measurement, and raw shares by profile and year.
Reads panel.frame('k100') and ph5_fmwave.features(): no decision or acceptance column is read anywhere.
Writes research/fashion/output/paper_profiles/ (profiles.json, profiles.csv, shares.csv; no per-paper file).

    python research/fashion/paper/analysis/newcomer_profiles.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve()
FASHION = HERE.parents[2]
sys.path.insert(0, str(FASHION))

import ols  # noqa: E402
import panel  # noqa: E402
import ph5_fmwave  # noqa: E402

OUT = FASHION / "output" / "paper_profiles"
TEAM_CAP = 16
CLASSES = {"method": "method", "measurement": "measurement", "theory": "cls_theory", "empirical": "cls_empirical",
           "dataset_benchmark": "cls_dataset_benchmark", "evaluation": "cls_evaluation", "other": "cls_other"}
ERAS = {"2019-2020": (2019, 2020), "2021-2023": (2021, 2023), "2024-2026": (2024, 2026)}


def frame() -> pd.DataFrame:
    k = panel.frame("k100").reset_index(drop=True)
    f = ph5_fmwave.features()
    assert (f.submission_id.to_numpy() == k.submission_id.to_numpy()).all()
    k["first_time"] = f.first_time.to_numpy()
    d = k[k.has_author_key.astype(bool) & k.year.between(2019, 2026)].copy()
    assert d.first_time.notna().all() and d.newcomer.notna().all()
    assert ((d.first_time == 1) <= (d.newcomer == 1)).all(), "a first-time team must be a topic newcomer"
    d["returning_newcomer"] = ((d.newcomer == 1) & (d.first_time == 0)).astype(float)
    d["log2_team"] = np.log2(d.team_size.clip(lower=1, upper=TEAM_CAP))
    d["profile"] = np.where(d.first_time == 1, "first_time",
                            np.where(d.newcomer == 1, "returning_newcomer", "incumbent"))
    return d


def contrasts(d: pd.DataFrame, y: str, team: bool) -> list[dict]:
    extra = ["log2_team"] if team else []
    rows = []
    for xs, labels in ((["newcomer", "first_time"], {"newcomer": "returning_newcomer - incumbent",
                                                     "first_time": "first_time - returning_newcomer"}),
                       (["first_time", "returning_newcomer"], {"first_time": "first_time - incumbent"})):
        r = ols.fe_ols(d[y].astype(float), d[xs + extra].astype(float), d.cell, d.topic)
        for x, lab in labels.items():
            c, s = r.loc[x, "coef"], r.loc[x, "se"]
            t_crit = 1.959964 if r.loc[x, "clusters"] > 1000 else float(
                __import__("scipy.stats", fromlist=["t"]).t.ppf(0.975, r.loc[x, "clusters"] - 1))
            rows.append({"outcome": y, "team_control": team, "contrast": lab, "pp": 100 * c,
                         "lo": 100 * (c - t_crit * s), "hi": 100 * (c + t_crit * s), "p": r.loc[x, "p"],
                         "n": int(r.loc[x, "n"]), "clusters": int(r.loc[x, "clusters"])})
    return rows


def main() -> None:
    d = frame()
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for name, col in CLASSES.items():
        d[name] = d[col].astype(float)
        for team in (False, True):
            rows += [{**r, "era": "2019-2026"} for r in contrasts(d, name, team)]
    for era, (a, b) in ERAS.items():
        e = d[d.year.between(a, b)]
        for name in ("method", "measurement"):
            rows += [{**r, "era": era} for r in contrasts(e, name, False)]
    res = pd.DataFrame(rows)
    res.to_csv(OUT / "profiles.csv", index=False, float_format="%.6g")

    # check: the single newcomer contrast on this population (cf. registered H2b +3.71 / H2c -1.70, which drop
    # singleton cells); reported for orientation only.
    chk = {y: 100 * float(ols.fe_ols(d[y].astype(float), d[["newcomer"]].astype(float), d.cell, d.topic)
                           .loc["newcomer", "coef"]) for y in ("method", "measurement")}
    sizes = d.profile.value_counts().to_dict()
    shares = (d.groupby(["profile"])[list(CLASSES)].mean() * 100).round(2)
    shares_year = (d.groupby(["year", "profile"])[["method", "measurement"]].mean() * 100).round(2).reset_index()
    team = d.groupby("profile").team_size.median().to_dict()
    shares_year.to_csv(OUT / "shares.csv", index=False)
    summary = {
        "population": {"papers": int(len(d)), "profiles": {k: int(v) for k, v in sizes.items()},
                       "profile_share_pct": {k: round(100 * v / len(d), 1) for k, v in sizes.items()},
                       "median_team_size": {k: float(v) for k, v in team.items()}},
        "check_single_newcomer_pp": chk,
        "raw_class_shares_pct": shares.to_dict(orient="index"),
        "contrasts_main": res[(res.era == "2019-2026") & res.outcome.isin(["method", "measurement"])]
        .round(3).to_dict(orient="records"),
        "note": "descriptive (E), outcome-free, discovery only, added during revision; not registered",
    }
    (OUT / "profiles.json").write_text(json.dumps(summary, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
