"""The sealed loader on synthetic tables only (PREREGISTRATION.md D13). This file may name the loader's internals;
it never reads the real table (every test replaces it with a synthetic one).

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

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


def as_main(name: str, directory: Path = HERE):
    """__main__ posing as research/fashion/<name> (or the same name elsewhere)."""
    return mock.patch.object(sys.modules["__main__"], "__file__", str(directory / name), create=True)


def lines(path: Path, statuses: list[str]) -> None:
    path.write_text("".join(json.dumps({"attempt": 1, "status": s}) + "\n" for s in statuses))


class SplitAwareReads(unittest.TestCase):
    """Synthetic discovery and confirmation tables (written to a temporary directory) stand in for outcomes.SOURCES;
    the real tables are never read. Covers the split-aware cached reads, the refusal of out-of-split ids, the entry
    dispatch (run_frozen.py / run_confirmation.py / run_pooled.py), the corpus checks, the pooled gate and the
    pooled posthoc gate (POOLED_SPEC D6)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.disc = synthetic(400, 1)
        self.conf = synthetic(150, 2).rename(index=lambda s: "c" + s)
        self.paths = {"discovery": d / "disc.csv.gz", "confirmation": d / "conf.csv.gz"}
        self.disc.reset_index().to_csv(self.paths["discovery"], index=False)
        self.conf.reset_index().to_csv(self.paths["confirmation"], index=False)
        self.patches = [mock.patch.dict(outcomes.SOURCES, self.paths)]
        for x in self.patches:
            x.start()
        outcomes._table.cache_clear()
        outcomes.release()

    def tearDown(self):
        for x in self.patches:
            x.stop()
        outcomes._table.cache_clear()
        outcomes.release()
        self.tmp.cleanup()

    def frozen(self, good: bool = True) -> Path:
        """A FREEZE_CONFIRMATION-like file hashing one synthetic file (absolute path), right or wrong."""
        f = Path(self.tmp.name) / "hashed.txt"
        f.write_text("frozen")
        h = hashlib.sha256(b"frozen").hexdigest() if good else "0" * 64
        path = Path(self.tmp.name) / "FREEZE_CONFIRMATION.json"
        path.write_text(json.dumps({"tau": 0.9, "sha256": {str(f): h}}))
        return path

    def test_sealed_files_are_unchanged_and_both_tables_are_listed(self):
        self.assertEqual(outcomes.SOURCE, outcomes.ROOT / "data" / "submissions.csv.gz")
        self.assertEqual(outcomes.sealed_files(), [outcomes.SOURCE])
        self.assertEqual(outcomes.sealed_files_all(), [self.paths["discovery"], self.paths["confirmation"]])
        self.assertEqual(outcomes.ENTRY, {"run_frozen.py": "discovery", "run_confirmation.py": "confirmation",
                                          "run_pooled.py": "pooled"})

    def test_tables_per_split_and_the_pooled_union(self):
        d, c, p = outcomes._table("discovery"), outcomes._table("confirmation"), outcomes._table("pooled")
        self.assertEqual(list(d.index), list(self.disc.index))
        self.assertEqual(list(c.index), list(self.conf.index))
        self.assertEqual(list(p.index), list(self.disc.index) + list(self.conf.index))
        self.assertTrue(p.index.is_unique)
        self.assertTrue((p.loc[c.index].decision == self.conf.decision).all())

    def test_a_paper_in_both_splits_is_an_error(self):
        clash = self.conf.reset_index()
        clash.loc[0, "submission_id"] = self.disc.index[0]
        clash.to_csv(self.paths["confirmation"], index=False)
        outcomes._table.cache_clear()
        with self.assertRaises(ValueError):
            outcomes._table("pooled")

    def test_reads_refuse_papers_outside_the_split(self):
        d, c = pd.Series(self.disc.index[:5]), pd.Series(self.conf.index[:5])
        for ids, split in [(c, "discovery"), (d, "confirmation"), (pd.concat([d, c]), "discovery"),
                           (pd.concat([d, c]), "confirmation"), (pd.Series(["nowhere"]), "pooled")]:
            with self.assertRaises(PermissionError):
                outcomes._read(ids, split)
        got = outcomes._read(c, "confirmation")
        pd.testing.assert_frame_equal(got, outcomes._derive(self.conf.loc[c.values].reset_index()))
        both = outcomes._read(pd.concat([c, d]), "pooled")
        self.assertEqual(list(both.submission_id), list(c) + list(d))

    def test_entry_dispatch(self):
        for name, split in outcomes.ENTRY.items():
            with as_main(name):
                self.assertEqual(outcomes.entry(), split)
        for main in [HERE / "posthoc.py", HERE / "dryrun.py", Path(self.tmp.name) / "run_confirmation.py",
                     Path(self.tmp.name) / "run_pooled.py"]:
            with as_main(main.name, main.parent), self.assertRaises(PermissionError) as e:
                outcomes.require_frozen()
            self.assertIn("research/fashion/run_frozen.py", str(e.exception))

    def test_the_corpus_must_match_the_entry(self):
        for name, corpus in [("run_confirmation.py", "discovery"), ("run_pooled.py", "discovery"),
                             ("run_frozen.py", "pooled")]:
            with as_main(name), mock.patch.object(outcomes, "CORPUS", corpus), self.assertRaises(PermissionError) as e:
                outcomes.require_frozen()
            self.assertIn("ICLR_CORPUS=" + ("discovery" if corpus == "pooled" else "pooled"), str(e.exception))

    def test_confirmation_entry_checks_every_hash_and_reads_the_confirmation_table_only(self):
        ids_c, ids_d = pd.Series(self.conf.index[:20]), pd.Series(self.disc.index[:3])
        with as_main("run_confirmation.py"), mock.patch.object(outcomes, "CORPUS", "pooled"), \
                mock.patch.object(outcomes, "clean_tree", lambda *a: None):
            for path, msg in [(Path(self.tmp.name) / "absent.json", "is missing"), (self.frozen(False), "files changed")]:
                with mock.patch.object(outcomes, "FREEZE_CONFIRMATION", path), self.assertRaises(PermissionError) as e:
                    outcomes.require_frozen()
                self.assertIn(msg, str(e.exception))
            with mock.patch.object(outcomes, "FREEZE_CONFIRMATION", self.frozen()):
                try:
                    self.assertEqual(outcomes.require_frozen()["tau"], 0.9)
                    got = outcomes.load("real", ids_c)
                    self.assertEqual(list(got.submission_id), list(ids_c))
                    with self.assertRaises(PermissionError):
                        outcomes.load("real", ids_d)                     # discovery outcomes are not this entry's
                finally:
                    outcomes.release()

    def test_discovery_entry_never_reads_a_confirmation_paper(self):
        with as_main("run_frozen.py"), mock.patch.object(outcomes, "require_frozen", lambda: {}):
            self.assertEqual(len(outcomes.load("real", pd.Series(self.disc.index[:4]))), 4)
            with self.assertRaises(PermissionError):
                outcomes.load("real", pd.Series(self.conf.index[:1]))

    def test_pooled_entry_needs_a_finished_confirmation_attempt(self):
        log = Path(self.tmp.name) / "attempts.jsonl"
        ids = pd.Series(list(self.disc.index[:3]) + list(self.conf.index[:3]))
        with as_main("run_pooled.py"), mock.patch.object(outcomes, "CORPUS", "pooled"), \
                mock.patch.object(outcomes, "CONFIRMATION_ATTEMPTS", log), \
                mock.patch.object(outcomes, "FREEZE_CONFIRMATION", self.frozen(False)), \
                mock.patch.object(outcomes, "clean_tree", lambda *a: None):
            for statuses in [None, [], ["started"], ["started", "failed"]]:
                if statuses is not None:
                    lines(log, statuses)
                with self.assertRaises(PermissionError) as e:
                    outcomes.load("real", ids)
                self.assertIn("confirmation run has finished", str(e.exception))
            lines(log, ["started", "finished"])
            try:                                      # exploratory: the settings are loaded without a hash match
                self.assertEqual(list(outcomes.load("real", ids).submission_id), list(ids))
            finally:
                outcomes.release()

    def test_permuted_null_is_refused_when_pooled(self):
        with mock.patch.object(outcomes, "CORPUS", "pooled"), self.assertRaises(PermissionError):
            outcomes.load("permuted", pd.Series(self.disc.index[:3]), seed=1)

    def test_pooled_posthoc_needs_the_confirmation_run_and_reads_the_pooled_table(self):
        tmp = Path(self.tmp.name)
        conf_log, main_log, access = tmp / "confirmation.jsonl", tmp / "frozen.jsonl", tmp / "access.jsonl"
        lines(main_log, ["started", "finished"])
        ids = pd.Series(list(self.conf.index[:2]) + list(self.disc.index[:2]))
        with as_main("posthoc.py"), mock.patch.object(outcomes, "CORPUS", "pooled"), \
                mock.patch.object(outcomes, "CONFIRMATION_ATTEMPTS", conf_log), \
                mock.patch.object(outcomes, "ATTEMPTS", main_log), mock.patch.object(outcomes, "POSTHOC_LOG", access), \
                mock.patch.object(outcomes, "clean_tree", lambda *a: None):
            for statuses in [[], ["started"], ["started", "failed"]]:
                lines(conf_log, statuses)
                with self.assertRaises(PermissionError) as e:
                    outcomes.load("posthoc", ids)
                self.assertIn("confirmation run has finished", str(e.exception))
            self.assertFalse(access.exists())
            lines(conf_log, ["started", "finished"])
            lines(main_log, ["started"])
            with self.assertRaises(PermissionError) as e:              # the pooled main run must have finished too
                outcomes.load("posthoc", ids)
            self.assertIn("frozen run has finished", str(e.exception))
            lines(main_log, ["started", "finished"])
            self.assertEqual(list(outcomes.load("posthoc", ids).submission_id), list(ids))
            self.assertEqual(json.loads(access.read_text().splitlines()[-1])["corpus"], "pooled")

    def test_discovery_posthoc_reads_discovery_only_and_logs_as_before(self):
        tmp = Path(self.tmp.name)
        main_log, access = tmp / "frozen.jsonl", tmp / "access.jsonl"
        lines(main_log, ["started", "finished"])
        with as_main("posthoc.py"), mock.patch.object(outcomes, "ATTEMPTS", main_log), \
                mock.patch.object(outcomes, "POSTHOC_LOG", access), mock.patch.object(outcomes, "clean_tree", lambda *a: None):
            self.assertEqual(len(outcomes.load("posthoc", pd.Series(self.disc.index[:3]))), 3)
            with self.assertRaises(PermissionError):
                outcomes.load("posthoc", pd.Series(self.conf.index[:1]))
        self.assertEqual(set(json.loads(access.read_text().splitlines()[0])),
                         {"at_utc", "git_head", "posthoc_sha256", "argv"})


if __name__ == "__main__":
    unittest.main()
