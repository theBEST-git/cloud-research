"""The only file that reads acceptance or review columns (PREREGISTRATION.md D13). Everything else gets outcomes here.

load(mode, ...) returns one row per corpus paper with:
- rq3:            registered RQ3 population (ordinary submission, outcome_eligible == 1, decision accepted or rejected)
- accepted:       1/0 within rq3, missing elsewhere
- s9, s9_accepted: rq3 plus withdrawals after review (at least one review) counted as not accepted (S9)
- e3:             ordinary submissions and withdrawals (desk rejections excluded), for E3
- withdrawn_after_review, withdrawn_before_review: 1/0 within e3
Modes:
- "simulated": no file is read. Populations are random (rq3 74% of papers, s9 adds 4%, e3 all) and outcomes come from
  dgp.simulate on the given frame.
- "permuted":  the real derived block (populations and outcomes together) shuffled across papers within year: the real
  pipeline and per-year marginals, but no link between any paper and its real status or outcome (a true null).
- "real":      refuses unless called from run_frozen.py, FREEZE.json hashes match, and the git tree is clean.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from common import DATA, ROOT
from dgp import DGP, simulate

HERE = Path(__file__).resolve().parent
FREEZE = HERE / "FREEZE.json"
COLUMNS = ["submission_id", "year", "administrative_status", "decision", "outcome_eligible", "review_count"]
SOURCE = DATA / "submissions.csv.gz"                    # the only table with outcomes (hashed via sealed_files())


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


_VERIFIED: dict | None = None


def sealed_files() -> list[Path]:
    """The files that hold sealed columns (for hashing in freeze.py)."""
    return [SOURCE]


def require_frozen() -> dict:
    """Guard for every real-data run (RQ2 and RQ3): entry point, frozen hashes, clean tree. Verified once per process,
    so the frozen run can record its attempt before it loads real data."""
    global _VERIFIED
    if _VERIFIED is not None:
        return _VERIFIED
    main = getattr(sys.modules.get("__main__"), "__file__", "") or ""
    if Path(main).resolve() != HERE / "run_frozen.py":
        raise PermissionError("real outcomes are only available to research/fashion/run_frozen.py")
    if not FREEZE.exists():
        raise PermissionError("FREEZE.json is missing: the analysis is not frozen")
    freeze = json.loads(FREEZE.read_text())
    bad = [p for p, h in freeze["sha256"].items() if not (ROOT / p).exists() or sha256(ROOT / p) != h]
    if bad:
        raise PermissionError(f"files changed since the freeze: {bad}")
    dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    if dirty.strip():
        raise PermissionError(f"git tree is not clean:\n{dirty}")
    _VERIFIED = freeze
    return freeze


def _derive(s: pd.DataFrame) -> pd.DataFrame:
    ordinary = s.administrative_status == "ordinary_submission"
    withdrawn = s.administrative_status == "withdrawn"
    if s.review_count[withdrawn].isna().any():                # would code a withdrawal as neither before nor after review
        raise ValueError("withdrawn papers with a missing review_count")
    out = pd.DataFrame({"submission_id": s.submission_id.values, "year": s.year.values})
    out["rq3"] = (ordinary & (s.outcome_eligible == 1) & s.decision.isin(["accepted", "rejected"])).values
    out["accepted"] = np.where(out.rq3, (s.decision == "accepted").astype(float).values, np.nan)
    after = (withdrawn & (s.review_count >= 1)).values
    out["s9"] = out.rq3 | after
    out["s9_accepted"] = np.where(out.rq3, out.accepted, np.where(after, 0.0, np.nan))
    out["e3"] = (ordinary | withdrawn).values
    out["withdrawn_after_review"] = np.where(out.e3, after.astype(float), np.nan)
    out["withdrawn_before_review"] = np.where(out.e3, (withdrawn & (s.review_count == 0)).astype(float).values, np.nan)
    return out


@lru_cache(maxsize=1)
def _table() -> pd.DataFrame:
    s = pd.read_csv(SOURCE, keep_default_na=False, na_values=[r"\N"], usecols=COLUMNS, low_memory=False)
    return s.set_index("submission_id")


def _read(ids: pd.Series) -> pd.DataFrame:
    return _derive(_table().loc[ids.values].reset_index())


BLOCK = ["rq3", "accepted", "s9", "s9_accepted", "e3", "withdrawn_after_review", "withdrawn_before_review"]


def _shuffle_within_year(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """Move each paper's whole derived block (populations and outcomes) to a random paper of the same year."""
    out = df.copy()
    for _, idx in df.groupby("year").groups.items():
        perm = rng.permutation(len(idx))
        for c in BLOCK:
            out.loc[idx, c] = df.loc[idx, c].to_numpy()[perm]
    for c in ["rq3", "s9", "e3"]:
        out[c] = out[c].astype(bool)
    return out


def load(mode: str, ids: pd.Series, seed: int | None = None, frame: pd.DataFrame | None = None,
         dgp: DGP | None = None) -> pd.DataFrame:
    if mode == "real":
        require_frozen()
        return _read(ids)
    rng = np.random.default_rng(seed)
    if mode == "permuted":
        return _shuffle_within_year(_read(ids), rng)
    if mode == "simulated":
        if frame is None or dgp is None or not frame.submission_id.reset_index(drop=True).equals(ids.reset_index(drop=True)):
            raise ValueError("simulated mode needs a frame aligned with ids and a DGP")
        y = simulate(frame, dgp, rng)
        u = rng.random(len(ids))
        out = pd.DataFrame({"submission_id": ids.values, "year": frame.year.values})
        out["rq3"] = u < 0.74
        out["accepted"] = np.where(out.rq3, y, np.nan)
        out["s9"] = u < 0.78
        out["s9_accepted"] = np.where(out.rq3, y, np.where(out.s9, 0.0, np.nan))
        out["e3"] = True
        w = rng.random(len(ids))
        out["withdrawn_after_review"] = (w < 0.15).astype(float)
        out["withdrawn_before_review"] = ((w >= 0.15) & (w < 0.22)).astype(float)
        return out
    raise ValueError(f"unknown mode {mode}")
