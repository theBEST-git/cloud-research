"""Shared paths and loaders for the title study (reads the exported corpus, never writes to data/)."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
STUDY = Path(__file__).resolve().parents[1]
CACHE = STUDY / "cache"
OUT = STUDY / "outputs"
FIG = OUT / "figures"
TAB = OUT / "tables"


def read_table(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA / f"{name}.csv.gz", keep_default_na=False, na_values=[r"\N"], low_memory=False)


def load_submissions() -> pd.DataFrame:
    """Submissions in export order (year, submission_id); this order defines embedding rows."""
    return read_table("submissions")


def acceptance_population(s: pd.DataFrame) -> pd.Series:
    """Documented filter: ordinary submissions with an eligible binary outcome."""
    return (s.administrative_status.eq("ordinary_submission") & s.outcome_eligible.eq(1)
            & s.decision.isin(["accepted", "rejected"]))
