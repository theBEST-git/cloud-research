"""Shared paths, label classes and topic maps for the research-fashion analyses.

Corpus switch (PREREGISTRATION.md D14; ICLR_CORPUS, read once at import, so set it per process before the first fashion
import):
- unset or "discovery": every path as before (data/, research/topics/output/, research/fashion/output/).
- "pooled" (discovery + released confirmation papers): TOPICS = research/topics/output_pooled (a sibling of output/, so
  rq2_following.REFERENCE still resolves), OUTPUT = research/fashion/output_pooled and DATA = output_pooled/inputs (the
  git-ignored pooled author table of build_pooled_inputs.py). Every derived path (variables.CHECKS, posthoc.OUT,
  figures.FIG, run_frozen.OUT, ...) follows, so no pooled build or run can write into the discovery outputs.
  The topic layer (topic_layer()) reads the same variable and must agree (checked when pooled).
"""
from __future__ import annotations

import gzip
import importlib.util
import io
import os
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DISCOVERY_OUTPUT = HERE / "output"                     # the committed discovery results (never written when pooled)
POOLED_OUTPUT = HERE / "output_pooled"
CORPUS = os.environ.get("ICLR_CORPUS") or "discovery"
if CORPUS not in ("discovery", "pooled"):
    raise ValueError(f"ICLR_CORPUS must be unset, 'discovery' or 'pooled', not {CORPUS!r}")
if CORPUS == "pooled":
    DATA = POOLED_OUTPUT / "inputs"
    TOPICS = ROOT / "research" / "topics" / "output_pooled"
    OUTPUT = POOLED_OUTPUT
    assert OUTPUT != DISCOVERY_OUTPUT and DISCOVERY_OUTPUT not in OUTPUT.parents, "pooled outputs must not be discovery outputs"
else:
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


def topic_layer():
    """The topic layer's common.py (embedded_corpus, load_embeddings, load_corpus), loaded under its own name."""
    spec = importlib.util.spec_from_file_location("topics_common", ROOT / "research" / "topics" / "common.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if CORPUS == "pooled" and Path(mod.OUTPUT).resolve() != TOPICS:
        raise RuntimeError(f"the topic layer writes to {mod.OUTPUT}, not {TOPICS}: ICLR_CORPUS changed after import?")
    return mod
