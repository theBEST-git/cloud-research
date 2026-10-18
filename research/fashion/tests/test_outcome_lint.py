"""Outcome-blind lint (PREREGISTRATION.md D13): only outcomes.py may name outcome or review columns, or read the
submissions table directly. The topic layer's corpus loader must not load them either, discovery or pooled.
Both sealed tables are covered (outcomes.SOURCE / SOURCES, sealed_files / sealed_files_all only where the freeze hashes
them), and the topic layer's code (research/topics, where the content readers of both submissions tables live) is
scanned with the same patterns: sealed names only in validate_outputs.py's guard list, the submissions tables only in
the content readers TOPIC_READERS, whose column lists are checked at runtime.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[1]
SEALED = {"decision", "outcome_eligible", "administrative_status", "review_count", "distinct_reviewers",
          "base_decision", "decision_evidence", "base_outcome_eligible", "outcome_source_release",
          "disagreement_eligible", "similarity_eligible"}
ALLOWED = {HERE / "outcomes.py", Path(__file__).resolve(), HERE / "tests" / "test_sealed_loader.py"}  # synthetic tables only
NAME = "|".join(sorted(SEALED, key=len, reverse=True))
COMPOUND = "|".join(sorted(SEALED - {"decision"}, key=len, reverse=True))   # never ordinary words
PATTERNS = [re.compile(rf"""["']({NAME})["']"""),              # string literal: df["decision"], usecols=[...]
            re.compile(rf"""\.({NAME})\b"""),                   # attribute access: df.decision
            re.compile(rf"""\b({COMPOUND})\b"""),               # anywhere, e.g. inside query("outcome_eligible == 1")
            re.compile(r"""["'][^"']*\bdecision\s*[=!<>]"""),     # decision inside a query/eval string
            re.compile(r"submissions\.csv"),                    # the only table that holds outcomes
            re.compile(r"\b_read\b|\b_derive\b|\b_table\b|\b_shuffle_within_year\b|outcomes\._"),  # private readers
            re.compile(r"\boutcomes\.(SOURCES?|COLUMNS)\b|\bimport\b.*\b(SOURCES?|COLUMNS)\b")]         # the raw tables
PERMUTED = re.compile(r"""["']permuted["']""")                 # the permuted null reads the real table: dry-runs only
PERMUTED_OK = {"dryrun.py"}
SEALED_LIST = re.compile(r"\bsealed_files(_all)?\s*\(")             # paths of the sealed tables: for hashing only
SEALED_LIST_OK = {HERE / f for f in ["freeze.py", "dryrun.py", "freeze_confirmation.py", "tests/test_protocol.py",
                                     "tests/test_confirmation_run.py"]}
TOPICS = ROOT / "research" / "topics"
NAME_PATTERNS = PATTERNS[:4]                                     # sealed column names
TABLE = PATTERNS[4]                                              # the submissions tables
TOPIC_GUARDS = {TOPICS / "validate_outputs.py"}                  # lists the sealed names to assert their absence
TOPIC_READERS = {TOPICS / "common.py", TOPICS / "keyword_map.py", TOPICS / "tests" / "test_pooled.py"}


def sources() -> list[Path]:
    files = [p for p in HERE.rglob("*") if p.suffix in {".py", ".js", ".ipynb", ".sh"} and p.resolve() not in ALLOWED]
    return [p for p in files if not {"__pycache__", "output"} & set(p.relative_to(HERE).parts)]


def topic_sources() -> list[Path]:
    files = [p for p in TOPICS.rglob("*") if p.suffix in {".py", ".js", ".ipynb", ".sh"}]
    return [p for p in files if not {"__pycache__", "output", "output_pooled", "cache"} & set(p.relative_to(TOPICS).parts)]


def by_path(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class OutcomeLint(unittest.TestCase):
    def test_no_file_but_outcomes_names_sealed_columns(self):
        hits, files = [], sources()
        names = {p.name for p in files}
        self.assertTrue({"analysis.py", "rq2_following.py", "rq3_reward.py", "variables.py"} <= names, "lint scans nothing")
        for p in files:
            for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if any(pat.search(line) for pat in PATTERNS) or (PERMUTED.search(line) and p.name not in PERMUTED_OK) \
                        or (SEALED_LIST.search(line) and p.resolve() not in SEALED_LIST_OK):
                    hits.append(f"{p.relative_to(ROOT)}:{n}: {line.strip()}")
        self.assertEqual(hits, [], "outcome columns named outside outcomes.py:\n" + "\n".join(hits))

    def test_topic_layer_names_no_sealed_column_and_reads_the_tables_only_in_its_readers(self):
        hits, files = [], topic_sources()
        self.assertTrue({TOPICS / "common.py", TOPICS / "keyword_map.py", TOPICS / "pooled_topics.py"} <= set(files))
        for p in files:
            for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                bad = [pat for pat in PATTERNS if pat.search(line)]
                bad = [pat for pat in bad if not (pat in NAME_PATTERNS and p in TOPIC_GUARDS)
                       and not (pat is TABLE and p in TOPIC_READERS)]
                if bad or PERMUTED.search(line) or SEALED_LIST.search(line):
                    hits.append(f"{p.relative_to(ROOT)}:{n}: {line.strip()}")
        self.assertEqual(hits, [], "sealed columns or tables in the topic layer:\n" + "\n".join(hits))
        km = by_path("topics_keyword_map_lint", TOPICS / "keyword_map.py")       # the readers' column lists
        self.assertFalse(SEALED & (set(km.COLUMNS) | {"keywords"}))

    def test_corpus_loader_reads_content_columns_only(self):
        spec = importlib.util.spec_from_file_location("topics_common_lint", ROOT / "research" / "topics" / "common.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertFalse(SEALED & set(mod.CONTENT_COLUMNS))

    def test_corpus_has_no_sealed_column_at_runtime(self):
        spec = importlib.util.spec_from_file_location("topics_common_rt", ROOT / "research" / "topics" / "common.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertFalse(SEALED & set(mod.embedded_corpus().columns))

    def test_pooled_corpus_has_no_sealed_column_at_runtime(self):
        """The pooled loader (discovery + confirmation tables) in its own process under ICLR_CORPUS=pooled."""
        code = ("import importlib.util, json, sys; "
                f"spec = importlib.util.spec_from_file_location('tc', {str(TOPICS / 'common.py')!r}); "
                "m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); c = m.embedded_corpus(); "
                "print(json.dumps({'corpus': m.CORPUS, 'columns': sorted(c.columns), 'split': sorted(set(c.split))}))")
        env = {**{k: v for k, v in os.environ.items() if k != "ICLR_CORPUS"}, "ICLR_CORPUS": "pooled"}
        r = subprocess.run([sys.executable, "-c", code], cwd=ROOT, env=env, capture_output=True, text=True, timeout=600)
        self.assertEqual(r.returncode, 0, r.stderr)
        got = json.loads(r.stdout.strip().splitlines()[-1])
        self.assertEqual((got["corpus"], got["split"]), ("pooled", ["confirmation", "discovery"]))
        self.assertFalse(SEALED & set(got["columns"]))

    def test_lint_catches_violations(self):
        for bad in ['x = df["decision"]', "y = s.outcome_eligible == 1", "pd.read_csv(DATA / 'submissions.csv.gz')",
                    "cols = ['review_count']", 'df.query("outcome_eligible == 1")', 'df.eval("decision == 1")',
                    "from outcomes import _read", "outcomes._derive(s)", "x = _read(ids)", "from outcomes import _table",
                    "oc._table()", "pd.read_csv(outcomes.SOURCE)", "usecols=outcomes.COLUMNS",
                    "from outcomes import SOURCE, load", 'pd.read_csv(outcomes.SOURCES["confirmation"])',
                    "from outcomes import SOURCES", "pd.read_csv(ROOT / 'data_confirmation_csv' / 'submissions.csv.gz')"]:
            self.assertTrue(any(p.search(bad) for p in PATTERNS), bad)
        for bad in ["pd.read_csv(outcomes.sealed_files_all()[1])", "t = sealed_files()"]:
            self.assertTrue(SEALED_LIST.search(bad), bad)
        self.assertFalse(SEALED_LIST.search("both sealed tables (outcomes.sealed_files_all) and"))
        self.assertTrue(PERMUTED.search('outcomes.load("permuted", ids)'))
        self.assertEqual(PERMUTED_OK, {"dryrun.py"})
        for ok in ["decision rule", "holm-adjusted decision", "def decide():"]:
            self.assertFalse(any(p.search(ok) for p in PATTERNS), ok)


if __name__ == "__main__":
    unittest.main()
