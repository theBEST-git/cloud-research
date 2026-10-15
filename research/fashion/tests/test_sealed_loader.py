"""The sealed loader on synthetic tables only (PREREGISTRATION.md D13). This file may name the loader's internals;
it never reads the real table (every test replaces it with a synthetic one).

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import outcomes  # noqa: E402


def synthetic(n: int = 3000, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    status = rng.choice(["ordinary_submission", "withdrawn", "desk_rejected"], n, p=[0.75, 0.22, 0.03])
    decision = np.where(status == "ordinary_submission", rng.choice(["accepted", "rejected"], n), status)
    return pd.DataFrame({"submission_id": [f"s{i}" for i in range(n)], "year": rng.integers(2018, 2027, n),
                         "administrative_status": status, "decision": decision,
                         "outcome_eligible": (rng.random(n) < 0.98).astype(int),
                         "review_count": np.where(rng.random(n) < 0.6, rng.integers(1, 5, n), 0)}).set_index("submission_id")


class SealedLoader(unittest.TestCase):
    def setUp(self):
        self.table = synthetic()
        self.orig = outcomes._table
        outcomes._table = lambda: self.table                    # never the real table

    def tearDown(self):
        outcomes._table = self.orig

    def test_derived_coding(self):
        d = outcomes._derive(self.table.reset_index())
        t = self.table.reset_index()
        rq3 = (t.administrative_status == "ordinary_submission") & (t.outcome_eligible == 1) & t.decision.isin(["accepted", "rejected"])
        self.assertTrue((d.rq3 == rq3).all())
        self.assertTrue((d.accepted[rq3] == (t.decision[rq3] == "accepted")).all())
        after = (t.administrative_status == "withdrawn") & (t.review_count >= 1)
        self.assertTrue((d.s9 == (rq3 | after)).all())
        self.assertTrue((d.s9_accepted[after] == 0).all())

    def test_permuted_block_covers_every_derived_column(self):
        derived = set(outcomes._derive(self.table.reset_index()).columns) - {"submission_id", "year"}
        self.assertEqual(set(outcomes.BLOCK), derived)

    def test_missing_review_count_of_a_withdrawal_is_an_error(self):
        t = self.table.reset_index()
        t["review_count"] = t.review_count.astype(float)
        t.loc[t.administrative_status == "withdrawn", "review_count"] = np.nan
        with self.assertRaises(ValueError):
            outcomes._derive(t)

    def test_permuted_mode_breaks_every_paper_link(self):
        ids = pd.Series(self.table.index)
        real = outcomes._derive(self.table.reset_index())
        perm = outcomes.load("permuted", ids, seed=1)
        for c in ["rq3", "s9", "e3"]:
            self.assertEqual(perm[c].dtype, bool)
            self.assertEqual(perm.groupby("year")[c].sum().tolist(), real.groupby("year")[c].sum().tolist())
        wd_real = (real.s9 & ~real.rq3).to_numpy()
        wd_perm = (perm.s9 & ~perm.rq3).to_numpy()
        self.assertLess((wd_real == wd_perm).mean(), 0.9)          # no longer the real withdrawal flag
        self.assertTrue(((perm.s9 & ~perm.rq3) <= perm.e3).all())   # each paper keeps a coherent block

    def test_permuted_mode_does_not_depend_on_the_requested_ids(self):
        ids = pd.Series(self.table.index)
        full = outcomes.load("permuted", ids, seed=3).set_index("submission_id")
        sub = ids.sample(frac=0.3, random_state=0)
        part = outcomes.load("permuted", sub, seed=3).set_index("submission_id")
        pd.testing.assert_frame_equal(part, full.loc[sub.values])
        real = outcomes._derive(self.table.reset_index()).set_index("submission_id")
        one = ids.groupby(self.table.year.values).head(1)                     # one paper per year
        agree = np.mean([(outcomes.load("permuted", one, seed=s).set_index("submission_id").rq3
                          == real.rq3.loc[one.values]).mean() for s in range(30)])
        self.assertLess(agree, 0.9)                                           # chance agreement, not the real block

    def test_entry_point_is_checked_on_every_call(self):
        outcomes._VERIFIED = {"sha256": {}}                                   # as if a frozen run had verified
        try:
            with self.assertRaises(PermissionError):
                outcomes.require_frozen()
        finally:
            outcomes.release()
        self.assertIsNone(outcomes._VERIFIED)

    def test_entry_point_must_be_the_repo_run_frozen(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp) / "run_frozen.py"
            fake.write_text(textwrap.dedent(f"""
                import sys; sys.path.insert(0, {str(HERE)!r})
                import outcomes
                try:
                    outcomes.require_frozen()
                except PermissionError as e:
                    print("REFUSED", e)
            """))
            r = subprocess.run([sys.executable, str(fake)], capture_output=True, text=True, timeout=120)
            self.assertIn("REFUSED", r.stdout)
            self.assertIn("research/fashion/run_frozen.py", r.stdout)


if __name__ == "__main__":
    unittest.main()
