"""Outcome-free analysis frames for RQ2 and RQ3: one row per paper for a given topic map.

Joins the contribution labels, topic-year maturity, prior foundation-model adoption, the RQ2 variables
(variables.py), the buzzword measure (buzzwords.py) and probable earlier versions (resubmissions.py). Acceptance
outcomes are never loaded here; they come only from outcomes.py.

Columns: submission_id, year, map, topic, cell (topic x year), labels (primary_class, primary_type, fm, uncertain),
class indicators (method, measurement, model, cls_<class> for the non-reference classes), maturity, maturity_x_method,
fm_adoption, log_papers_prev, prior_growth, hot, incumbent / newcomer (and _w2, _s4 versions), has_author_key,
team_size, log_team, buzzword, lists_hot, n_eligible_keywords, has_earlier_version, stable, mixed_topic.
"""
from __future__ import annotations

from functools import lru_cache

import numpy as np
import pandas as pd

from common import CLASSES, OUTPUT, TOPICS, topic_maps
from topic_maturity import maturity as maturity_table

MAPS = ("k100", "k75", "k150", "balanced", "early", "middle_era", "late", "fine")
CLASS_CONTROLS = [f"cls_{c}" for c in CLASSES if c != "method"]       # reference class: method (D7)


@lru_cache(maxsize=None)
def _inputs() -> dict:
    maps = topic_maps()
    fine = pd.read_csv(TOPICS / "topic_assignments.csv.gz")
    assert fine.submission_id.equals(maps.submission_id)
    maps["fine"] = fine.fine
    lab = pd.read_csv(TOPICS / "paper_contributions.csv.gz")
    assert lab.submission_id.equals(maps.submission_id), "labels and topic maps are not aligned"
    mat = pd.read_csv(OUTPUT / "topic_year_maturity.csv.gz")
    mat = pd.concat([mat, maturity_table(maps.fine, maps.year).assign(map="fine")], ignore_index=True)
    mat["topic"] = mat.topic.astype(str)
    var = pd.read_csv(OUTPUT / "paper_variables.csv.gz")
    var["topic"] = var.topic.astype(str)
    buzz = pd.read_csv(OUTPUT / "paper_buzzword.csv.gz")
    assert buzz.submission_id.equals(maps.submission_id)
    ev = pd.read_csv(OUTPUT / "earlier_versions.csv.gz")
    assert ev.submission_id.equals(maps.submission_id)
    stab = pd.read_csv(TOPICS / "paper_topic_stability.csv.gz")
    assert stab.submission_id.equals(maps.submission_id)
    cat = pd.read_csv(TOPICS / "topic_catalog.csv", keep_default_na=False)
    mixed = set(cat[(cat.level == "mid") & (cat.coherence == "mixed")].topic)
    return {"maps": maps, "lab": lab, "mat": mat, "var": var, "buzz": buzz, "ev": ev, "stab": stab, "mixed": mixed}


@lru_cache(maxsize=None)
def frame(map_name: str) -> pd.DataFrame:
    """Analysis frame for one map, all papers and years (filters come later, D9). Cached; do not mutate."""
    d = _inputs()
    maps, lab = d["maps"], d["lab"]
    df = pd.DataFrame({"submission_id": maps.submission_id, "year": maps.year, "map": map_name,
                       "topic": maps[map_name].astype(str)})
    df["cell"] = df.topic + ":" + df.year.astype(str)
    df["primary_class"], df["primary_type"] = lab.primary_class.values, lab.primary_type.values
    df["fm"] = (lab.foundation_model == "yes").astype(float).values
    df["uncertain"] = lab.uncertain.astype(bool).values
    df["method"] = (df.primary_class == "method").astype(float)
    df["measurement"] = df.primary_class.isin(["dataset_benchmark", "evaluation"]).astype(float)
    df["model"] = (df.primary_type == "model").astype(float)
    for c in CLASS_CONTROLS:
        df[c] = (df.primary_class == c[4:]).astype(float)

    mat = d["mat"][d["mat"]["map"] == map_name]
    df = df.merge(mat[["topic", "year", "log_cum_prior", "prior_growth"]], on=["topic", "year"], how="left", validate="m:1")
    df = df.rename(columns={"log_cum_prior": "maturity"})
    prev = mat[["topic", "year", "papers"]].assign(year=lambda m: m.year + 1)          # papers in t - 1
    df = df.merge(prev.rename(columns={"papers": "papers_prev"}), on=["topic", "year"], how="left", validate="m:1")
    df["log_papers_prev"] = np.log1p(df.papers_prev)
    fm = df.groupby(["topic", "year"]).fm.mean().rename("fm_adoption").reset_index()
    fm["year"] += 1                                                                    # FM share in t - 1 (RQ1)
    df = df.merge(fm, on=["topic", "year"], how="left", validate="m:1")
    df["maturity_x_method"] = df.maturity * df.method

    var = d["var"][d["var"]["map"] == map_name].set_index("submission_id")
    assert (var.loc[df.submission_id, "topic"].values == df.topic.values).all(), "variables built on another map version"
    for c in ["has_author_key", "team_size", "incumbent", "newcomer", "incumbent_w2", "incumbent_s4", "hot"]:
        df[c] = var.loc[df.submission_id, c].values
    df["has_author_key"] = df.has_author_key.astype(bool)
    df["newcomer_w2"] = 1 - df.incumbent_w2
    df["newcomer_s4"] = 1 - df.incumbent_s4
    df["log_team"] = np.log(df.team_size.where(df.team_size > 0))

    buzz = d["buzz"]
    for c in ["buzzword", "lists_hot", "n_eligible_keywords"]:
        df[c] = buzz[c].values
    ev = d["ev"]
    if "probable_earlier_version" in ev:
        df["has_earlier_version"] = ev.probable_earlier_version.notna().astype(float).values
    else:
        df["has_earlier_version"] = np.nan
    df["stable"] = (d["stab"].mid_stability >= 2 / 3 - 1e-9).values
    df["mixed_topic"] = df.topic.isin(d["mixed"]) if map_name == "k100" else False
    return df
