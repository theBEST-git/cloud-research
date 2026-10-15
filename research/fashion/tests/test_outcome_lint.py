"""Outcome-blind lint (PREREGISTRATION.md D13): only outcomes.py may name outcome or review columns, or read the
submissions table directly. The topic layer's corpus loader must not load them either.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import importlib.util
import re
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
            re.compile(r"\boutcomes\.(SOURCE|COLUMNS)\b|\bimport\b.*\b(SOURCE|COLUMNS)\b")]             # the raw table
PERMUTED = re.compile(r"""["']permuted["']""")                 # the permuted null reads the real table: dry-runs only
PERMUTED_OK = {"dryrun.py"}


def sources() -> list[Path]:
    files = [p for p in HERE.rglob("*") if p.suffix in {".py", ".js", ".ipynb", ".sh"} and p.resolve() not in ALLOWED]
    return [p for p in files if not {"__pycache__", "output"} & set(p.relative_to(HERE).parts)]


class OutcomeLint(unittest.TestCase):
    def test_no_file_but_outcomes_names_sealed_columns(self):
        hits, files = [], sources()
        names = {p.name for p in files}
        self.assertTrue({"analysis.py", "rq2_following.py", "rq3_reward.py", "variables.py"} <= names, "lint scans nothing")
        for p in files:
            for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                if any(pat.search(line) for pat in PATTERNS) or (PERMUTED.search(line) and p.name not in PERMUTED_OK):
                    hits.append(f"{p.relative_to(ROOT)}:{n}: {line.strip()}")
        self.assertEqual(hits, [], "outcome columns named outside outcomes.py:\n" + "\n".join(hits))

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

    def test_lint_catches_violations(self):
        for bad in ['x = df["decision"]', "y = s.outcome_eligible == 1", "pd.read_csv(DATA / 'submissions.csv.gz')",
                    "cols = ['review_count']", 'df.query("outcome_eligible == 1")', 'df.eval("decision == 1")',
                    "from outcomes import _read", "outcomes._derive(s)", "x = _read(ids)", "from outcomes import _table",
                    "oc._table()", "pd.read_csv(outcomes.SOURCE)", "usecols=outcomes.COLUMNS",
                    "from outcomes import SOURCE, load"]:
            self.assertTrue(any(p.search(bad) for p in PATTERNS), bad)
        self.assertTrue(PERMUTED.search('outcomes.load("permuted", ids)'))
        self.assertEqual(PERMUTED_OK, {"dryrun.py"})
        for ok in ["decision rule", "holm-adjusted decision", "def decide():"]:
            self.assertFalse(any(p.search(ok) for p in PATTERNS), ok)


if __name__ == "__main__":
    unittest.main()
