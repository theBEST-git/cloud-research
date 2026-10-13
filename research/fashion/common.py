"""Shared paths, label classes and topic maps for the research-fashion analyses."""
from __future__ import annotations

import gzip
import io
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / "data"
TOPICS = ROOT / "research" / "topics" / "output"
OUTPUT = HERE / "output"

TYPES = ["method", "model", "theory", "empirical", "system", "dataset_benchmark", "evaluation", "problem",
         "application", "recipe", "perspective", "survey_position"]
CLASS_OF = {"model": "method", "system": "other", "problem": "other", "application": "other", "recipe": "other",
            "perspective": "other", "survey_position": "other"}
CLASSES = ["method", "theory", "empirical", "dataset_benchmark", "evaluation", "other"]
MAIN_K = "k100"


def class_of(fine_type: str) -> str:
    return CLASS_OF.get(fine_type, fine_type)


def topic_maps() -> pd.DataFrame:
    """Middle-level topic of every paper under each available map; columns are map names, values topic ids.

    k100 is the published middle level (the main map); k75 / k150 come from the k sweep; balanced / early /
    middle_era / late come from the hindsight check (if it has been run)."""
    pub = pd.read_csv(TOPICS / "topic_assignments.csv.gz")
    maps = pub[["submission_id", "year"]].copy()
    maps["k100"] = pub.mid
    ks = pd.read_csv(TOPICS / "k_sensitivity_assignments.csv.gz")
    assert ks.submission_id.equals(pub.submission_id)
    for k in (75, 150):
        maps[f"k{k}"] = "k" + str(k) + "_" + ks[f"mid_k{k}"].astype(str)
    path = TOPICS / "hindsight_assignments.csv.gz"
    if path.exists():
        hs = pd.read_csv(path)
        assert hs.submission_id.equals(pub.submission_id)
        for name, col in [("balanced", "mid_balanced"), ("early", "mid_early"), ("middle_era", "mid_middle"), ("late", "mid_late")]:
            maps[name] = name + "_" + hs[col].astype(str)
    return maps


def write_csv_gz(df: pd.DataFrame, path: Path) -> None:
    """Deterministic gzip (fixed mtime), as in the topic layer."""
    text = df.to_csv(index=False, lineterminator="\n")
    with path.open("wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=6) as gz:
        with io.TextIOWrapper(gz, encoding="utf-8", newline="") as handle:
            handle.write(text)
