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
ALLOWED = {HERE / "outcomes.py", Path(__file__).resolve()}
NAME = "|".join(sorted(SEALED, key=len, reverse=True))
PATTERNS = [re.compile(rf"""["']({NAME})["']"""),              # string literal: df["decision"], usecols=[...]
            re.compile(rf"""\.({NAME})\b"""),                   # attribute access: df.decision
            re.compile(r"submissions\.csv")]                    # the only table that holds outcomes


def sources() -> list[Path]:
    files = [p for p in HERE.rglob("*") if p.suffix in {".py", ".js"} and p.resolve() not in ALLOWED]
    return [p for p in files if "__pycache__" not in p.parts and "output" not in p.parts]


class OutcomeLint(unittest.TestCase):
    def test_no_file_but_outcomes_names_sealed_columns(self):
        hits = []
        for p in sources():
            for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                code = line.split("#", 1)[0] if p.suffix == ".py" else line
                if any(pat.search(code) for pat in PATTERNS):
                    hits.append(f"{p.relative_to(ROOT)}:{n}: {line.strip()}")
        self.assertEqual(hits, [], "outcome columns named outside outcomes.py:\n" + "\n".join(hits))

    def test_corpus_loader_reads_content_columns_only(self):
        spec = importlib.util.spec_from_file_location("topics_common_lint", ROOT / "research" / "topics" / "common.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertFalse(SEALED & set(mod.CONTENT_COLUMNS))

    def test_lint_catches_violations(self):
        for bad in ['x = df["decision"]', "y = s.outcome_eligible == 1", "pd.read_csv(DATA / 'submissions.csv.gz')",
                    "cols = ['review_count']"]:
            self.assertTrue(any(p.search(bad) for p in PATTERNS), bad)
        for ok in ["decision rule", "holm-adjusted decision", "def decide():"]:
            self.assertFalse(any(p.search(ok) for p in PATTERNS), ok)


if __name__ == "__main__":
    unittest.main()
