"""RQ1 (rise): how a topic's contribution mix changes as it matures. Implements PREREGISTRATION.md, section RQ1.

Paper-level linear probability models, years 2018-2026, topic and year fixed effects, SE clustered by topic:
  H1a  method                        on maturity            (predicted < 0)
  H1b  measurement (dataset_benchmark or evaluation) on maturity   (> 0)
  H1c  empirical                     on maturity            (> 0)
  H1d  model (new architecture)      on prior FM adoption   (< 0)
  H1e  empirical or evaluation       on prior FM adoption   (> 0)
maturity = log(1 + papers in the topic before year t); prior FM adoption = share of the topic's year t - 1 papers
labelled foundation_model = yes. Both use only earlier years.

Main specification: map k100 (published middle topics), all labelled papers. Robustness variants: maps k75, k150,
balanced and early (if available); k100 restricted to stable papers, coherent topics, certain labels, or 2018-2025.
Verdict per hypothesis: supported if, in the main specification, the sign is as predicted and the Holm-adjusted
p < 0.05 (over H1a-H1e), and the sign is as predicted in at least 75% of robustness variants.

    python research/fashion/rq1_rise.py [--labels <paper_contributions.csv.gz>] [--out <dir>]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from common import OUTPUT, TOPICS, topic_maps
from ols import fe_ols

YEARS = (2018, 2026)
HYPOTHESES = {   # id: (outcome, regressor, predicted sign)
    "H1a": ("method", "maturity", -1),
    "H1b": ("measurement", "maturity", +1),
    "H1c": ("empirical", "maturity", +1),
    "H1d": ("model", "fm_adoption", -1),
    "H1e": ("studies_models", "fm_adoption", +1),
}
ROBUST_SHARE = 0.75


def outcomes(lab: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        "method": lab.primary_class.eq("method"),
        "measurement": lab.primary_class.isin(["dataset_benchmark", "evaluation"]),
        "empirical": lab.primary_class.eq("empirical"),
        "model": lab.primary_type.eq("model"),
        "studies_models": lab.primary_class.isin(["empirical", "evaluation"]),
    }).astype(float)


def holm(p: pd.Series) -> pd.Series:
    order = p.sort_values().index
    m, running, adj = len(p), 0.0, {}
    for i, idx in enumerate(order):
        running = max(running, min(1.0, (m - i) * p[idx]))
        adj[idx] = running
    return pd.Series(adj)[p.index]


def frame_for(map_name: str, base: pd.DataFrame, maps: pd.DataFrame, maturity: pd.DataFrame) -> pd.DataFrame:
    df = base.assign(topic=maps[map_name].values)
    mat = maturity[maturity["map"] == map_name][["topic", "year", "log_cum_prior"]]
    df = df.merge(mat, on=["topic", "year"], how="left").rename(columns={"log_cum_prior": "maturity"})
    fm = (df.groupby(["topic", "year"]).foundation_model.apply(lambda s: (s == "yes").mean())
          .rename("fm_share").reset_index())
    fm["year"] += 1                                        # adoption in t = FM share of the topic's papers in t - 1
    df = df.merge(fm, on=["topic", "year"], how="left").rename(columns={"fm_share": "fm_adoption"})
    return df


def fit(df: pd.DataFrame, outcome: str, regressor: str) -> pd.Series:
    d = df[(df.year >= YEARS[0]) & (df.year <= YEARS[1])]
    if d[outcome].nunique() < 2:                          # e.g. a type that never occurs: nothing to estimate
        return pd.Series({"coef": np.nan, "se": np.nan, "p": np.nan, "n": len(d), "clusters": d.topic.nunique()})
    years = pd.get_dummies(d.year, prefix="y", drop_first=True).astype(float)
    X = pd.concat([d[[regressor]].reset_index(drop=True), years.reset_index(drop=True)], axis=1)
    res = fe_ols(d[outcome].reset_index(drop=True), X, d.topic.reset_index(drop=True), d.topic.reset_index(drop=True))
    return res.loc[regressor]


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--labels", type=Path, default=TOPICS / "paper_contributions.csv.gz")
    p.add_argument("--out", type=Path, default=OUTPUT)
    a = p.parse_args()
    lab = pd.read_csv(a.labels)
    maps = topic_maps()
    if not lab.submission_id.equals(maps.submission_id):
        raise SystemExit("labels and topic maps are not aligned")
    maturity = pd.read_csv(OUTPUT / "topic_year_maturity.csv.gz")
    stability = pd.read_csv(TOPICS / "paper_topic_stability.csv.gz")
    catalog = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False)
    mixed = set(catalog[(catalog.level == "mid") & (catalog.coherence == "mixed")].topic)
    base = pd.concat([lab[["submission_id", "year", "foundation_model", "uncertain"]], outcomes(lab)], axis=1)
    if not stability.submission_id.equals(lab.submission_id):
        raise SystemExit("labels and paper stability are not aligned")
    base["stable"] = (stability.mid_stability >= 2 / 3 - 1e-9).values

    variants = {"main": ("k100", None)}
    for m in ["k75", "k150", "balanced", "early"]:
        if m in maps:
            variants[m] = (m, None)
    variants.update({"stable_papers": ("k100", lambda d: d.stable), "coherent_topics": ("k100", lambda d: ~d.topic.isin(mixed)),
                     "certain_labels": ("k100", lambda d: ~d.uncertain.astype(bool)), "years_2018_2025": ("k100", lambda d: d.year <= 2025)})
    frames = {m: frame_for(m, base, maps, maturity) for m in {v[0] for v in variants.values()}}
    rows = []
    for variant, (m, keep) in variants.items():
        df = frames[m] if keep is None else frames[m][keep(frames[m])]
        for h, (y, x, sign) in HYPOTHESES.items():
            r = fit(df, y, x)
            rows.append({"hypothesis": h, "variant": variant, "map": m, "outcome": y, "regressor": x, "predicted_sign": sign,
                         "coef": r.coef, "se": r.se, "p": r.p, "n": int(r.n), "clusters": int(r.clusters),
                         "outcome_mean": float(df[(df.year >= YEARS[0])][y].mean())})
    res = pd.DataFrame(rows)
    main_res = res[res.variant == "main"].set_index("hypothesis")
    main_res["p_holm"] = holm(main_res.p)
    summary = {}
    for h, (y, x, sign) in HYPOTHESES.items():
        rob = res[(res.hypothesis == h) & (res.variant != "main")]
        same = float((np.sign(rob.coef) == sign).mean())
        r = main_res.loc[h]
        ok = bool(np.sign(r.coef) == sign and r.p_holm < 0.05 and same >= ROBUST_SHARE)
        summary[h] = {"outcome": y, "regressor": x, "predicted_sign": sign, "coef": round(float(r.coef), 5),
                      "ci95": [round(float(r.coef - 1.96 * r.se), 5), round(float(r.coef + 1.96 * r.se), 5)],
                      "p": float(r.p), "p_holm": float(r.p_holm), "robustness_same_sign": round(same, 3),
                      "robustness_variants": int(len(rob)), "verdict": "supported" if ok else "not supported"}
    a.out.mkdir(parents=True, exist_ok=True)
    res.to_csv(a.out / "rq1_results.csv", index=False)
    (a.out / "rq1_summary.json").write_text(json.dumps({"labels": str(a.labels), "variants": list(variants), "hypotheses": summary},
                                                       indent=2) + "\n")
    for h, s in summary.items():
        print(f"{h} {s['outcome']:15s} ~ {s['regressor']:12s} coef {s['coef']:+.4f} CI {s['ci95']} p_holm {s['p_holm']:.3g} "
              f"robust {s['robustness_same_sign']:.0%} -> {s['verdict']}")


if __name__ == "__main__":
    main()
