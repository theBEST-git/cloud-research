"""PH5 cleantext: the abstract cleaner, the switch between original and clean vectors, the comparison and verdict
logic, and (when the clean vectors exist) an end-to-end run on simulated outcomes (no real outcome is read).

    python -m unittest research/fashion/tests/test_ph5_cleantext.py
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import ph5_cleantext as m  # noqa: E402
import ph5_common  # noqa: E402
import ph5_pivot  # noqa: E402
import ph5_position  # noqa: E402


def cleaner():
    """research/topics/embed_specter2_clean.py's clean() (loaded by path: the two layers both have a common.py)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("embed_specter2_clean",
                                                  ROOT / "research" / "topics" / "embed_specter2_clean.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.clean


class Cleaner(unittest.TestCase):
    def test_clean(self):
        clean = cleaner()
        a = ("We propose X. It beats Y on Z. Code is available at https://github.com/lab/x. "
             "See www.example.org for more.")
        self.assertEqual(clean(a), "We propose X. It beats Y on Z. See for more.")
        self.assertEqual(clean("Our models are publicly released."), "")
        self.assertEqual(clean("No link here.  Two  spaces."), "No link here. Two spaces.")


class Compare(unittest.TestCase):
    def row(self, **kw):
        base = {"same_sign": True, "p_holm_clean": 0.2, "ci95_lo_clean": -0.06, "ci95_hi_clean": 0.0,
                "coef_committed": -0.05}
        return pd.Series({**base, **kw})

    def test_verdict(self):
        self.assertEqual(m.verdict(self.row(p_holm_clean=0.01)), "holds")
        self.assertEqual(m.verdict(self.row()), "attenuated")
        self.assertEqual(m.verdict(self.row(ci95_lo_clean=-0.02, ci95_hi_clean=0.01)), "does not hold")
        self.assertEqual(m.verdict(self.row(same_sign=False, p_holm_clean=0.01)), "does not hold")

    def test_compare_reads_committed(self):
        t = pd.read_csv(m.COMMITTED["pivot"])
        out = m.compare({"pivot": t})
        self.assertTrue((out.coef_clean == out.coef_committed).all())
        self.assertTrue(out.same_sign.all())
        self.assertEqual(out[out.key].test.tolist(), ["E1", "E4"])


@unittest.skipUnless(m.CLEAN.exists(), "clean vectors not built (research/topics/embed_specter2_clean.py)")
class Switch(unittest.TestCase):
    def tearDown(self):
        m.use(False)

    def test_vectors(self):
        changed = set(pd.read_csv(m.CHANGED).submission_id)
        ids = pd.read_csv(m.CACHE / "specter2_ids.csv").submission_id
        is_changed = ids.isin(changed).to_numpy()
        m.use(False)
        X0 = ph5_position.embeddings()
        m.use(True)
        X1 = ph5_position.embeddings()
        self.assertTrue(np.array_equal(X0[~is_changed], X1[~is_changed]))
        self.assertTrue((np.abs(X0[is_changed] - X1[is_changed]).max(axis=1) > 0).all())
        emb, _ = ph5_pivot.topic_layer().load_embeddings()
        self.assertTrue(np.array_equal(emb, np.load(m.CLEAN)))
        m.use(False)
        emb, _ = ph5_pivot.topic_layer().load_embeddings()
        self.assertTrue(np.array_equal(emb, np.load(m.CACHE / "specter2.npy")))

    def test_end_to_end_simulated(self):
        k = ph5_common.simulated_frame(seed=3)
        res = m.compute(k, nulls=3, check_hash=False)
        t = res["tests"]
        self.assertEqual(t.test.tolist(), ["E1", "E2", "E3", "E4", "P1a", "P1b", "P2", "P3", "P4", "P5", "P6", "P7"])
        self.assertEqual(set(t[t.key].verdict), set(t[t.key].verdict) & {"holds", "attenuated", "does not hold"})
        s = res["shift"]
        unchanged = s[(s.papers == "text unchanged") & (s.feature == "nov")]
        self.assertGreater(float(unchanged.corr.iloc[0]), 0.95)
        self.assertIs(ph5_position.embeddings, m._ORIGINAL["embeddings"])   # switched back
        with tempfile.TemporaryDirectory() as d:
            t.to_csv(Path(d) / "tests.csv", index=False)
            m.plot(Path(d))
            self.assertTrue((Path(d) / "PH5_cleantext.png").exists())


if __name__ == "__main__":
    unittest.main()
