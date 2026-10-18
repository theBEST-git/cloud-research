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
- "permuted":  the real derived block (populations and outcomes together) of the WHOLE table shuffled across papers
  within year, then the requested ids selected: the real pipeline and per-year marginals, and a true null for any set
  of requested ids. The shuffle is seeded so that dry-runs are reproducible; it hides real outcomes from analysis code,
  not from someone who deliberately re-creates the seeded shuffle (which, like reading the table, the protocol forbids).
- "real":      refuses unless called from run_frozen.py, FREEZE.json hashes match, and the git tree is clean.
- "posthoc":   post hoc exploratory analyses after the single frozen run (PREREGISTRATION.md post-run record). Refuses
  unless called from posthoc.py, output/frozen_run/attempts.jsonl records a finished attempt, no debugger is attached
  and the git tree is clean (so the code that reads outcomes is committed before it runs); every access is appended
  to output/posthoc/access_log.jsonl with the commit and the script's sha256.

Splits (D14 and the confirmation registrations). SOURCES holds the discovery table (data/) and the confirmation table
(data_confirmation_csv/, the released former holdout); "pooled" is their union (ids must be unique). Reads are
split-aware: _read(ids, split) refuses any id outside the split, so a discovery entry point can never read a
confirmation outcome. The split of a real read is fixed by the entry script (ENTRY), and the corpus switch
(common.CORPUS, ICLR_CORPUS) must match it:
- run_frozen.py       -> discovery     ICLR_CORPUS unset; FREEZE.json, every hash, clean tree (unchanged)
- run_confirmation.py -> confirmation  ICLR_CORPUS=pooled; FREEZE_CONFIRMATION.json, every hash, clean tree
- run_pooled.py       -> pooled        ICLR_CORPUS=pooled; exploratory, only after a finished confirmation attempt
                                       that ran PH5 (confirmation_finished: output_pooled/confirmation_run/attempts.jsonl);
                                       FREEZE_CONFIRMATION.json settings without a hash match (its sha256 is recorded by
                                       the run); clean tree
Under ICLR_CORPUS=pooled, "posthoc" also needs that finished confirmation attempt, reads the pooled table and logs (with
the corpus) to output_pooled/posthoc/access_log.jsonl; ATTEMPTS then resolves to output_pooled/frozen_run, so the
pooled main run (run_pooled.py) must have finished as well. "permuted" reads the discovery table only and is refused
under ICLR_CORPUS=pooled (a pooled shuffle would expose confirmation outcomes and change every discovery null).
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

from common import CORPUS, OUTPUT, POOLED_OUTPUT, ROOT
from dgp import DGP, simulate

HERE = Path(__file__).resolve().parent
FREEZE_DISCOVERY = HERE / "FREEZE.json"
FREEZE_CONFIRMATION = HERE / "FREEZE_CONFIRMATION.json"
FREEZE = FREEZE_DISCOVERY if CORPUS == "discovery" else FREEZE_CONFIRMATION     # the freeze a run of this corpus records
COLUMNS = ["submission_id", "year", "administrative_status", "decision", "outcome_eligible", "review_count"]
SOURCES = {"discovery": ROOT / "data" / "submissions.csv.gz",                    # the only tables with outcomes
           "confirmation": ROOT / "data_confirmation_csv" / "submissions.csv.gz"}
SOURCE = SOURCES["discovery"]                           # hashed via sealed_files() (FREEZE.json, dryrun.digest)
SPLITS = ("discovery", "confirmation", "pooled")
ENTRY = {"run_frozen.py": "discovery", "run_confirmation.py": "confirmation", "run_pooled.py": "pooled"}
CONFIRMATION_ATTEMPTS = POOLED_OUTPUT / "confirmation_run" / "attempts.jsonl"     # fixed, whatever the corpus


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


_VERIFIED: dict | None = None                           # hashes and clean tree, checked once per frozen run


def sealed_files() -> list[Path]:
    """The files that hold sealed columns (for hashing in freeze.py and dryrun.digest: the discovery table)."""
    return [SOURCE]


def sealed_files_all() -> list[Path]:
    """Both sealed tables, discovery and confirmation (for hashing in freeze_confirmation.py)."""
    return [SOURCES["discovery"], SOURCES["confirmation"]]


def release() -> None:
    """Forget the verification (run_frozen.py calls this when it ends, however it ends)."""
    global _VERIFIED
    _VERIFIED = None


def entry() -> str:
    """The split the running entry script may read (ENTRY: the script must be that file in research/fashion)."""
    main = getattr(sys.modules.get("__main__"), "__file__", "") or ""
    path = Path(main).resolve()
    if path.parent != HERE or path.name not in ENTRY:
        raise PermissionError("real outcomes are only available to research/fashion/run_frozen.py (discovery), "
                              "run_confirmation.py (confirmation) and run_pooled.py (pooled)")
    return ENTRY[path.name]


def finished(log: Path) -> bool:
    """Whether an attempts log records a finished attempt."""
    lines = [json.loads(x) for x in log.read_text().splitlines()] if log.exists() else []
    return any(x.get("status") == "finished" for x in lines)


def confirmation_finished(log: Path | None = None) -> bool:
    """Whether the confirmation run has finished WITH its PH5 part (a 'finished' line with with_ph5 true): the gate of
    everything pooled that reads or crosses confirmation outcomes or labels (run_pooled.py, pooled post hoc, pooled
    RQ1 and figures). A run without PH5 opens nothing, so PH5 can never be confirmed after pooled results were seen."""
    log = CONFIRMATION_ATTEMPTS if log is None else log
    lines = [json.loads(x) for x in log.read_text().splitlines()] if log.exists() else []
    return any(x.get("status") == "finished" and x.get("with_ph5") is True for x in lines)


def verify(freeze_file: Path) -> dict:
    """The frozen settings, after every sha256 they list matches (paths relative to the repository root)."""
    if not freeze_file.exists():
        raise PermissionError(f"{freeze_file.name} is missing: the analysis is not frozen")
    freeze = json.loads(freeze_file.read_text())
    bad = [p for p, h in freeze["sha256"].items() if not (ROOT / p).exists() or sha256(ROOT / p) != h]
    if bad:
        raise PermissionError(f"files changed since the freeze: {bad}")
    return freeze


def clean_tree(note: str = "") -> None:
    dirty = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    if dirty.strip():
        raise PermissionError(f"git tree is not clean{note}:\n{dirty}")


def require_frozen() -> dict:
    """Guard for every real-data run: entry point (checked on every call; it fixes the split), then once per run the
    corpus switch, the freeze (hashes, or for the pooled run a finished confirmation attempt) and a clean tree (so the
    run can record its attempt before it loads real data; released at its end). The discovery path is unchanged."""
    global _VERIFIED
    split = entry()
    if sys.gettrace() is not None or sys.flags.inspect or sys.flags.interactive:
        raise PermissionError("the frozen run cannot run under a debugger or an interactive session")
    if _VERIFIED is not None:
        return _VERIFIED
    corpus = "discovery" if split == "discovery" else "pooled"
    if CORPUS != corpus:
        raise PermissionError(f"{split} outcomes need ICLR_CORPUS={corpus} (unset for discovery); this process has {CORPUS}")
    if split == "pooled":
        if not confirmation_finished():
            raise PermissionError("the pooled run is only allowed after the confirmation run has finished (with PH5)")
        if not FREEZE_CONFIRMATION.exists():
            raise PermissionError("FREEZE_CONFIRMATION.json is missing")
        freeze = json.loads(FREEZE_CONFIRMATION.read_text())    # settings only: exploratory (D6); the run records its sha
    else:
        freeze = verify(FREEZE_DISCOVERY if split == "discovery" else FREEZE_CONFIRMATION)
    clean_tree()
    _VERIFIED = freeze
    return freeze


POSTHOC = HERE / "posthoc.py"
ATTEMPTS = OUTPUT / "frozen_run" / "attempts.jsonl"
POSTHOC_LOG = OUTPUT / "posthoc" / "access_log.jsonl"


def require_posthoc() -> None:
    """Guard for post hoc analyses: only after the confirmatory run has finished, only from committed code, logged.
    Under ICLR_CORPUS=pooled also only after the confirmation run has finished (and ATTEMPTS is the pooled main run's)."""
    main = getattr(sys.modules.get("__main__"), "__file__", "") or ""
    if Path(main).resolve() != POSTHOC:
        raise PermissionError("post hoc outcomes are only available to research/fashion/posthoc.py")
    if sys.gettrace() is not None or sys.flags.inspect or sys.flags.interactive:
        raise PermissionError("post hoc analyses cannot run under a debugger or an interactive session")
    pooled = CORPUS == "pooled"
    if pooled and not confirmation_finished():
        raise PermissionError("pooled post hoc analyses are only allowed after the confirmation run has finished "
                              "(with PH5)")
    if not finished(ATTEMPTS):
        raise PermissionError("post hoc analyses are only allowed after the single frozen run has finished"
                              + (" (pooled: run_pooled.py)" if pooled else ""))
    clean_tree(" (post hoc code must be committed before it reads outcomes)")
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    POSTHOC_LOG.parent.mkdir(parents=True, exist_ok=True)
    with POSTHOC_LOG.open("a") as f:
        f.write(json.dumps({"at_utc": pd.Timestamp.now(tz="UTC").isoformat(timespec="seconds"), "git_head": head,
                            "posthoc_sha256": sha256(POSTHOC), "argv": sys.argv[1:],
                            **({"corpus": CORPUS} if pooled else {})}) + "\n")


UNKNOWN_REVIEW: dict[str, int] = {}   # per split read: withdrawn confirmation papers whose review status is unknown


def _derive(s: pd.DataFrame, lenient: np.ndarray | None = None) -> pd.DataFrame:
    """Derived outcome columns. lenient (confirmation rows only; registered 2026-10-18 before the confirmation run): a
    withdrawal with a missing review_count there is coded as review status unknown, i.e. outside S9's after-review set,
    missing in both withdrawal outcomes and outside e3. Anywhere else (all discovery rows) it is an error."""
    ordinary = s.administrative_status == "ordinary_submission"
    withdrawn = s.administrative_status == "withdrawn"
    unknown = (withdrawn & s.review_count.isna()).to_numpy()
    if (unknown & ~(np.zeros(len(s), bool) if lenient is None else lenient)).any():
        raise ValueError("withdrawn papers with a missing review_count")  # would be neither before nor after review
    out = pd.DataFrame({"submission_id": s.submission_id.values, "year": s.year.values})
    out["rq3"] = (ordinary & (s.outcome_eligible == 1) & s.decision.isin(["accepted", "rejected"])).values
    out["accepted"] = np.where(out.rq3, (s.decision == "accepted").astype(float).values, np.nan)
    after = (withdrawn & (s.review_count >= 1)).values
    out["s9"] = out.rq3 | after
    out["s9_accepted"] = np.where(out.rq3, out.accepted, np.where(after, 0.0, np.nan))
    out["e3"] = (ordinary | withdrawn).values & ~unknown
    out["withdrawn_after_review"] = np.where(out.e3, after.astype(float), np.nan)
    out["withdrawn_before_review"] = np.where(out.e3, (withdrawn & (s.review_count == 0)).astype(float).values, np.nan)
    return out


@lru_cache(maxsize=None)
def _table(split: str = "discovery") -> pd.DataFrame:
    """The sealed columns of one split, indexed by submission_id; "pooled" = discovery then confirmation rows."""
    if split not in SPLITS:
        raise ValueError(f"unknown split {split!r}")
    if split == "pooled":
        s = pd.concat([_table("discovery"), _table("confirmation")])
    else:
        s = pd.read_csv(SOURCES[split], keep_default_na=False, na_values=[r"\N"], usecols=COLUMNS,
                        low_memory=False).set_index("submission_id")
    if not s.index.is_unique:
        raise ValueError(f"submission ids are not unique in the {split} table")
    return s


def _read(ids: pd.Series, split: str = "discovery") -> pd.DataFrame:
    """Derived outcomes of the requested papers; refuses (before deriving anything) if any of them is outside the split."""
    t = _table(split)
    outside = ~pd.Index(ids.values).isin(t.index)
    if outside.any():
        raise PermissionError(f"{int(outside.sum())} requested papers are not in the {split} split: refused")
    rows = t.loc[ids.values].reset_index()
    lenient = None if split == "discovery" else rows.submission_id.isin(_table("confirmation").index).to_numpy()
    UNKNOWN_REVIEW[split] = int(((rows.administrative_status == "withdrawn") & rows.review_count.isna()).sum())
    return _derive(rows, lenient)


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
        return _read(ids, entry())
    if mode == "posthoc":
        require_posthoc()
        return _read(ids, "pooled" if CORPUS == "pooled" else "discovery")
    rng = np.random.default_rng(seed)
    if mode == "permuted":
        if CORPUS != "discovery":
            raise PermissionError("the permuted null reads the discovery table only: refused under ICLR_CORPUS=pooled")
        full = _shuffle_within_year(_derive(_table().reset_index()), rng)      # never depends on the requested ids
        return full.set_index("submission_id").loc[ids.values].reset_index()
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
