"""Pooled inputs of the fashion layer (POOLED_SPEC D1/D5, PREREGISTRATION.md D14/D15; ICLR_CORPUS=pooled, common.py).
Outcome-free: it reads the two author tables and copies three frozen discovery files; no submissions table is read.

Writes (fixed paths, whatever ICLR_CORPUS is; never under research/fashion/output/):
- output_pooled/inputs/submission_authors.csv.gz (git-ignored; DATA when pooled): every author row of data/ and of
  data_confirmation_csv/ (same header, disjoint papers), stable-sorted by (year, submission_id, source_list_position).
  Both sources are already in that order, so each keeps its own row order. Every value is the exact source string
  (read as text, no NA conversion). Deterministic gzip (mtime 0), so the same sources give the same bytes.
- byte-identical copies of output/h2d_validation.json, output/resubmission_tau.json and output/specter2_centring_mean.npy
  in output_pooled/ (the H2d gate, τ and the D15 centring mean are frozen discovery constants, reused for D14).
- output_pooled/pooled_inputs.json (committed): sha256 of every source and written file, row and paper counts per split,
  and the gates below.
Gates (refuse on failure, nothing is half-written into the manifest):
- the two author tables have the same header and no paper in common;
- read back as text, the pooled table's discovery rows equal data/'s table and its confirmation rows equal
  data_confirmation_csv/'s table, row for row; read back with the pipeline's reader (variables.load_authors), the
  discovery papers' author keys are exactly the discovery table's (so team_size / has_author_key cannot move);
- each copy's sha256 equals its source and the source's FREEZE.json entry.
Prints counts and hashes only, never a name or an author id.

    python research/fashion/build_pooled_inputs.py
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import numpy as np
import pandas as pd

from common import DISCOVERY_OUTPUT, POOLED_OUTPUT, ROOT, write_csv_gz
from outcomes import FREEZE_DISCOVERY, sha256

SOURCES = {"discovery": ROOT / "data" / "submission_authors.csv.gz",
           "confirmation": ROOT / "data_confirmation_csv" / "submission_authors.csv.gz"}
INPUTS = POOLED_OUTPUT / "inputs"
AUTHORS = INPUTS / "submission_authors.csv.gz"
MANIFEST = POOLED_OUTPUT / "pooled_inputs.json"
COPIES = ["h2d_validation.json", "resubmission_tau.json", "specter2_centring_mean.npy"]
ORDER = ["year", "submission_id", "source_list_position"]


def read_text(path: Path) -> pd.DataFrame:
    """Every column as its exact source string (\\N and empty fields stay as they are)."""
    return pd.read_csv(path, dtype=str, keep_default_na=False, na_filter=False)


def read_keys(path: Path) -> pd.DataFrame:
    """variables.load_authors' reader (the pipeline's view of the table): paper, key, kind; rows without a key dropped."""
    a = pd.read_csv(path, keep_default_na=False, na_values=[r"\N"], usecols=["submission_id", "declared_id_key", "native_id_kind"])
    return a[a.declared_id_key.notna()].drop_duplicates(["submission_id", "declared_id_key"]).reset_index(drop=True)


def pooled_authors(parts: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Union of the split tables in (year, submission_id, source_list_position) order; the sort is stable."""
    cols = [list(t.columns) for t in parts.values()]
    if any(c != cols[0] for c in cols):
        raise SystemExit("the author tables do not share one header")
    ids = [set(t.submission_id) for t in parts.values()]
    if set.intersection(*ids):
        raise SystemExit("a paper is in both author tables")
    both = pd.concat(list(parts.values()), ignore_index=True)
    key = pd.DataFrame({"y": both.year.astype(int), "s": both.submission_id, "p": both.source_list_position.astype(int)})
    return both.iloc[key.sort_values(["y", "s", "p"], kind="stable").index].reset_index(drop=True)


def check_authors(path: Path, parts: dict[str, pd.DataFrame], sources: dict[str, Path]) -> dict:
    """Read the written table back and compare it with every source, as text and through the pipeline's reader."""
    back = read_text(path)
    out = {}
    for split, t in parts.items():
        mine = back[back.submission_id.isin(set(t.submission_id))].reset_index(drop=True)
        pd.testing.assert_frame_equal(mine, t.reset_index(drop=True))           # every value, row for row
        out[split] = {"rows": int(len(t)), "papers": int(t.submission_id.nunique())}
    if len(back) != sum(len(t) for t in parts.values()):
        raise SystemExit("the pooled author table has rows from neither source")
    keys = read_keys(path)
    disc = read_keys(sources["discovery"])
    mine = keys[keys.submission_id.isin(set(disc.submission_id))].reset_index(drop=True)
    pd.testing.assert_frame_equal(mine, disc)
    return out


def copy_constants(source_dir: Path, target_dir: Path, freeze_file: Path) -> dict:
    """Byte-identical copies of the frozen discovery constants; each must also match its FREEZE.json hash."""
    frozen = json.loads(freeze_file.read_text())["sha256"]
    out = {}
    for name in COPIES:
        src, dst = source_dir / name, target_dir / name
        rel = str(src.relative_to(ROOT)) if ROOT in src.parents else str(src)
        if frozen.get(rel) != sha256(src):
            raise SystemExit(f"{rel} differs from its FREEZE.json hash")
        shutil.copyfile(src, dst)
        if sha256(dst) != sha256(src):
            raise SystemExit(f"the copy of {name} is not byte-identical")
        out[name] = {"source": rel, "sha256": sha256(dst), "freeze_sha256": frozen[rel]}
    return out


def build(sources: dict[str, Path] = SOURCES, authors: Path = AUTHORS, source_dir: Path = DISCOVERY_OUTPUT,
          target_dir: Path = POOLED_OUTPUT, freeze_file: Path = FREEZE_DISCOVERY) -> dict:
    """Write the pooled author table and the copies; return the manifest (written by main)."""
    for p in (authors, target_dir):
        if p == DISCOVERY_OUTPUT or DISCOVERY_OUTPUT in p.parents:
            raise SystemExit(f"refusing to write {p}: it is a discovery output")
    parts = {split: read_text(path) for split, path in sources.items()}
    pooled = pooled_authors(parts)
    authors.parent.mkdir(parents=True, exist_ok=True)
    write_csv_gz(pooled, authors)
    counts = check_authors(authors, parts, sources)
    target_dir.mkdir(parents=True, exist_ok=True)
    rel = lambda p: str(p.relative_to(ROOT)) if ROOT in p.parents else str(p)
    return {"authors": {"path": rel(authors), "sha256": sha256(authors), "rows": int(len(pooled)), "order": ORDER,
                        "by_split": counts, "sources": {rel(p): sha256(p) for p in sources.values()},
                        "git_ignored": True},
            "copies": copy_constants(source_dir, target_dir, freeze_file),
            "gates": ["same header, disjoint papers", "pooled rows equal each source row for row (as text)",
                      "discovery author keys unchanged through variables.load_authors' reader",
                      "copies byte-identical to their sources and to FREEZE.json"],
            "numpy": np.__version__, "pandas": pd.__version__}


def main() -> None:
    manifest = build()
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"authors": {k: manifest["authors"][k] for k in ("path", "sha256", "rows", "by_split")},
                      "copies": {k: v["sha256"][:12] for k, v in manifest["copies"].items()}}, indent=1))


if __name__ == "__main__":
    main()
