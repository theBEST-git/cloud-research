"""Topic-year maturity variables for every topic map (outcome-blind, label-free).

All variables for year t use only papers from years before t (what an author could know when submitting),
except `papers` and `share`, which describe year t itself.

- papers, share:          submissions in the topic in year t, and their share of all year-t submissions
- cum_prior_papers:       submissions in the topic in all years before t; log_cum_prior = log(1 + that)
- cum_prior_share:        cum_prior_papers / all submissions before t
- prior_share:            the topic's share in year t - 1
- prior_growth:           share in t - 1 over share in t - 2 (counts + 0.5)
- years_since_first10:    t minus the first earlier year with >= 10 papers in the topic (missing if none yet)

Writes output/topic_year_maturity.csv.gz (one row per map, topic and year).

    python research/fashion/topic_maturity.py
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import OUTPUT, topic_maps, write_csv_gz


def maturity(topic: pd.Series, year: pd.Series) -> pd.DataFrame:
    counts = pd.crosstab(topic, year)                         # topics x years, zeros included
    years = list(counts.columns)
    totals = counts.sum(axis=0)
    rows = []
    for t_idx, t in enumerate(years):
        prior = counts.iloc[:, :t_idx]
        cum = prior.sum(axis=1)
        frame = pd.DataFrame({"topic": counts.index, "year": t, "papers": counts[t].values,
                              "share": (counts[t] / totals[t]).values, "cum_prior_papers": cum.values})
        frame["log_cum_prior"] = np.log1p(frame.cum_prior_papers)
        frame["cum_prior_share"] = (cum / totals.iloc[:t_idx].sum()).values if t_idx else np.nan
        frame["prior_share"] = (counts.iloc[:, t_idx - 1] / totals.iloc[t_idx - 1]).values if t_idx >= 1 else np.nan
        if t_idx >= 2:
            a = (counts.iloc[:, t_idx - 1] + 0.5) / totals.iloc[t_idx - 1]
            b = (counts.iloc[:, t_idx - 2] + 0.5) / totals.iloc[t_idx - 2]
            frame["prior_growth"] = (a / b).values
        else:
            frame["prior_growth"] = np.nan
        first10 = [next((y for y in years[:t_idx] if counts.at[c, y] >= 10), None) for c in counts.index]
        frame["years_since_first10"] = [t - f if f is not None else np.nan for f in first10]
        rows.append(frame)
    return pd.concat(rows, ignore_index=True)


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    maps = topic_maps()
    names = [c for c in maps.columns if c not in ("submission_id", "year")]
    out = pd.concat([maturity(maps[m], maps.year).assign(map=m) for m in names], ignore_index=True)
    out = out[["map", "topic", "year", "papers", "share", "cum_prior_papers", "log_cum_prior", "cum_prior_share",
               "prior_share", "prior_growth", "years_since_first10"]]
    for col in ["share", "log_cum_prior", "cum_prior_share", "prior_share", "prior_growth"]:
        out[col] = out[col].round(6)
    write_csv_gz(out, OUTPUT / "topic_year_maturity.csv.gz")
    print(out.groupby("map").agg(topics=("topic", "nunique"), rows=("topic", "size")).to_string())


if __name__ == "__main__":
    main()
