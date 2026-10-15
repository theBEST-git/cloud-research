"""Planned exploratory analyses E1-E10 (PREREGISTRATION.md pre-run log). Always labelled exploratory; never verdicts.

E1  foundation-model acceptance gap within topic-year          accepted ~ fm | topic x year (+ classes)
E2  acceptance by incumbency                                    accepted ~ newcomer | topic x year (+ classes, fm)
E3  withdrawal as an outcome, after vs before review            withdrawn_* ~ H3a / H3c regressors | topic + year
E4  era heterogeneity for H2b-c and H3a-b                       the confirmatory models within 2018/19-20, 21-23, 24-26
E5  newcomer x hot                                              H2b-c and acceptance with newcomer x hot | topic x year
E6  dose-response after removing fixed effects (H1d, H2a, H3a)  binned residual means (20 quantile bins)
E7  buzzword decomposition                                      listing a hot keyword vs atypical use
E8  acceptance of new-architecture papers by prior FM adoption  accepted ~ model x fm_adoption | topic + year
E9  equivalence (TOST) and MDE80 for non-supported hypotheses   assembled by run_frozen.py from verdicts and dry-runs
E10 acceptance by contribution class                            rates by class and year; class gaps | topic x year
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from analysis import estimate as _estimate
from ols import demean
from panel import CLASS_CONTROLS
from rq2_following import guard, with_columns
from rq2_following import population as rq2_population
from rq3_reward import BASE, OUTCOME_COLUMNS

ERAS_RQ3 = {"2018-2020": (2018, 2020), "2021-2023": (2021, 2023), "2024-2026": (2024, 2026)}
ERAS_RQ2 = {"2019-2020": (2019, 2020), "2021-2023": (2021, 2023), "2024-2026": (2024, 2026)}


def binned(df: pd.DataFrame, y: str, x: str, years: tuple[int, int], bins: int = 20) -> pd.DataFrame:
    """E6: y and x residualised on topic FE and year dummies (FWL), means added back, x cut into quantile bins."""
    d = df[(df.year >= years[0]) & (df.year <= years[1])].dropna(subset=[y, x]).reset_index(drop=True)
    yr = pd.get_dummies(d.year, drop_first=True).astype(float).to_numpy()
    Z = demean(yr, d.topic.to_numpy())

    def resid(v: np.ndarray) -> np.ndarray:
        r = demean(v, d.topic.to_numpy())
        b = np.linalg.lstsq(Z, r, rcond=None)[0]
        return r - Z @ b

    ry, rx = resid(d[y].to_numpy(float)) + d[y].mean(), resid(d[x].to_numpy(float)) + d[x].mean()
    q = pd.qcut(pd.Series(rx), bins, labels=False, duplicates="drop")
    out = pd.DataFrame({"x": rx, "y": ry, "bin": q}).groupby("bin").agg(x=("x", "mean"), y=("y", "mean"), n=("y", "size"))
    return out.reset_index()


BUZZ = {"buzzword", "lists_hot"}
FAILED = "uses the buzzword measure, which failed its blind validation (H2d gate)"


def run(frames: dict[str, pd.DataFrame], out: pd.DataFrame, gate: bool, ys: dict[str, pd.Series] | None = None) -> dict:
    guard(ys)
    describe = ys is None
    k = with_columns(frames["k100"], ys)
    for c in OUTCOME_COLUMNS:
        k[c] = out[c].to_numpy()
    k["newcomer_x_hot"] = k.newcomer * k.hot
    k["model_x_fm_adoption"] = k.model * k.fm_adoption
    rq3 = k[k.rq3]
    rq3_keyed = rq3[rq3.has_author_key]
    rq2 = rq2_population(k)
    rows = []

    def estimate(df, y, x, controls=(), fe="topic+year", years=None):
        r = _estimate(df, y, x, controls, fe, years, describe=describe)
        r["_uses"] = {y, x, *controls}
        return r

    def add(eid: str, label: str, r: dict, tested: str) -> None:
        uses = r.pop("_uses")
        status = FAILED if (not gate and uses & BUZZ) else ""
        rows.append({"analysis": eid, "kind": "exploratory", "label": label, "tested": tested, "measure_status": status, **r})

    add("E1", "accepted ~ fm | topic x year + classes", estimate(rq3, "accepted", "fm", CLASS_CONTROLS, "cell", (2018, 2026)), "fm")
    add("E1", "accepted ~ fm | topic x year (no class controls)", estimate(rq3, "accepted", "fm", (), "cell", (2018, 2026)), "fm")
    add("E2", "accepted ~ newcomer | topic x year + classes + fm", estimate(rq3_keyed, "accepted", "newcomer", BASE, "cell", (2019, 2026)), "newcomer")
    add("E2", "accepted ~ newcomer, ID-consistent years", estimate(rq3_keyed[rq3_keyed.year.isin([2019, 2020, 2023, 2024, 2025, 2026])],
                                                                   "accepted", "newcomer", BASE, "cell", (2019, 2026)), "newcomer")
    e3 = k[k.e3]
    for y in ["withdrawn_after_review", "withdrawn_before_review"]:
        add("E3", f"{y} ~ maturity + classes + fm | topic + year", estimate(e3, y, "maturity", BASE, "topic+year", (2018, 2026)), "maturity")
        add("E3", f"{y} ~ buzzword + classes + fm | topic + year", estimate(e3, y, "buzzword", BASE, "topic+year", (2019, 2026)), "buzzword")
    for era, yrs in ERAS_RQ2.items():
        add("E4", f"H2b method ~ newcomer, {era}", estimate(rq2, "method", "newcomer", (), "cell", yrs), "newcomer")
        add("E4", f"H2c measurement ~ newcomer, {era}", estimate(rq2, "measurement", "newcomer", (), "cell", yrs), "newcomer")
    for era, yrs in ERAS_RQ3.items():
        add("E4", f"H3a accepted ~ maturity, {era}", estimate(rq3, "accepted", "maturity", BASE, "topic+year", yrs), "maturity")
        add("E4", f"H3b accepted ~ maturity x method, {era}", estimate(rq3, "accepted", "maturity_x_method", ("maturity",) + BASE,
                                                                        "topic+year", yrs), "maturity_x_method")
    add("E5", "method ~ newcomer + newcomer x hot | topic x year", estimate(rq2, "method", "newcomer_x_hot", ("newcomer",), "cell", (2019, 2026)), "newcomer_x_hot")
    add("E5", "measurement ~ newcomer + newcomer x hot | topic x year", estimate(rq2, "measurement", "newcomer_x_hot", ("newcomer",), "cell", (2019, 2026)), "newcomer_x_hot")
    add("E5", "accepted ~ newcomer + newcomer x hot | topic x year + classes + fm",
        estimate(rq3_keyed, "accepted", "newcomer_x_hot", ("newcomer",) + BASE, "cell", (2019, 2026)), "newcomer_x_hot")
    add("E7", "lists_hot ~ newcomer | topic x year", estimate(rq2, "lists_hot", "newcomer", (), "cell", (2019, 2026)), "newcomer")
    add("E7", "buzzword ~ newcomer | topic x year, among papers listing a hot keyword",
        estimate(rq2[rq2.lists_hot == 1], "buzzword", "newcomer", (), "cell", (2019, 2026)), "newcomer")
    add("E7", "accepted ~ lists_hot + buzzword + classes + fm | topic + year", estimate(rq3, "accepted", "lists_hot", ("buzzword",) + BASE,
                                                                                       "topic+year", (2019, 2026)), "lists_hot")
    add("E7", "accepted ~ buzzword + lists_hot + classes + fm | topic + year", estimate(rq3, "accepted", "buzzword", ("lists_hot",) + BASE,
                                                                                       "topic+year", (2019, 2026)), "buzzword")
    add("E8", "accepted ~ model x fm_adoption + model + fm_adoption + classes + fm | topic + year",
        estimate(rq3, "accepted", "model_x_fm_adoption", ("model", "fm_adoption") + BASE, "topic+year", (2018, 2026)), "model_x_fm_adoption")
    for c in CLASS_CONTROLS:
        others = tuple(x for x in CLASS_CONTROLS if x != c) + ("fm",)
        add("E10", f"accepted ~ {c[4:]} (vs method) | topic x year", estimate(rq3, "accepted", c, others, "cell", (2018, 2026)), c)
    rates = (rq3[rq3.year.between(2018, 2026)].groupby(["year", "primary_class"]).accepted.agg(["mean", "size"])
             .rename(columns={"mean": "acceptance_rate", "size": "papers"}).reset_index())
    dose = pd.concat([binned(k, "model", "fm_adoption", (2018, 2026)).assign(analysis="E6", label="H1d model ~ fm_adoption"),
                      binned(rq2.assign(log_prior_growth=np.log(rq2.prior_growth)), "incumbent", "log_prior_growth", (2019, 2026))
                      .assign(analysis="E6", label="H2a incumbent ~ log prior growth"),
                      binned(rq3, "accepted", "maturity", (2018, 2026)).assign(analysis="E6", label="H3a accepted ~ maturity")])
    return {"estimates": pd.DataFrame(rows), "acceptance_by_class_year": rates, "dose_response": dose}
