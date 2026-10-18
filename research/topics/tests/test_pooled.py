"""Pooled corpus mode of the topic layer (POOLED_SPEC D1-D4): the ICLR_CORPUS switch, pooled order P, the keyword
lookup for confirmation papers (keyword_map.py) and the pooled topic outputs (pooled_topics.py). Content columns only.

    python -m unittest discover -s research/topics/tests -p 'test_*.py'
"""
from __future__ import annotations

import collections
import gzip
import hashlib
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

TOPICS = Path(__file__).resolve().parents[1]
ROOT = TOPICS.parents[1]
FROZEN, POOLED, CACHE = TOPICS / "output", TOPICS / "output_pooled", TOPICS / "cache"
TABLES = ["topic_assignments", "k_sensitivity_assignments", "hindsight_assignments", "paper_topic_stability",
          "paper_contributions"]
COPIES = ["topic_catalog.csv", "keyword_types.csv", "topic_model.npz", "hindsight_check.json"]
CONTENT_COLUMNS = ["submission_id", "year", "title", "abstract", "normalized_keywords_json", "primary_area"]
N_POOLED, N_DISCOVERY, N_CONFIRMATION = 54579, 43480, 11099


def by_path(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def topic_layer(corpus: str | None):
    """A fresh copy of topics/common.py under ICLR_CORPUS=corpus (None: unset), loaded by path like fashion's topic_layer()."""
    env = {k: v for k, v in os.environ.items() if k != "ICLR_CORPUS"}
    env |= {} if corpus is None else {"ICLR_CORPUS": corpus}
    with mock.patch.dict(os.environ, env, clear=True):
        return by_path(f"topics_common_test_{corpus}", TOPICS / "common.py")


km = by_path("topics_keyword_map_test", TOPICS / "keyword_map.py")


def frozen_load_corpus() -> pd.DataFrame:
    """The loader as frozen before the switch (research/topics/common.py, FREEZE.json sha256 b829e5cf...), verbatim."""
    s = pd.read_csv(ROOT / "data" / "submissions.csv.gz", keep_default_na=False, na_values=[r"\N"], usecols=CONTENT_COLUMNS,
                    low_memory=False)
    s["keywords"] = s.normalized_keywords_json.map(lambda v: json.loads(v) if isinstance(v, str) else [])
    s["has_text"] = s.abstract.fillna("").str.split().str.len() >= 30
    return s


def lines(path: Path) -> list[str]:
    return gzip.decompress(path.read_bytes()).decode("utf-8").split("\n")


class Switch(unittest.TestCase):
    def test_unset_and_discovery_keep_the_frozen_paths(self):
        for value in (None, "", "discovery"):
            m = topic_layer(value)
            self.assertEqual(m.CORPUS, "discovery")
            self.assertEqual((m.DATA, m.OUTPUT, m.CACHE), (ROOT / "data", FROZEN, CACHE))
            self.assertEqual((m.MIN_ABSTRACT_WORDS, m.CONTENT_COLUMNS), (30, CONTENT_COLUMNS))

    def test_only_the_pooled_builders_run_pooled(self):
        """D2: under pooled every other topic-layer script is refused as __main__ (no refit, no overwrite of the frozen
        copies, no pooled chunks in CACHE); in a subprocess so the guard sees a real __main__."""
        m = topic_layer("pooled")
        for name in ["assign_topics.py", "evaluate_topics.py", "k_sensitivity.py", "hindsight_check.py", "build_topics.py",
                     "embed_specter2.py", "embed_specter2_released.py", "derive_features.py",
                     "annotation/contribution_types/llm_labeling/merge_released.py"]:
            with self.assertRaises(SystemExit) as e:
                m.check_pooled_entry(str(TOPICS / name))
            self.assertIn("cannot run under ICLR_CORPUS=pooled", str(e.exception))
        for main in [TOPICS / "pooled_topics.py", TOPICS / "keyword_map.py", TOPICS / "tests" / "test_pooled.py",
                     ROOT / "research" / "fashion" / "run_confirmation.py", ""]:
            m.check_pooled_entry(str(main) if main else "")
        topic_layer(None).check_pooled_entry(str(TOPICS / "assign_topics.py"))      # discovery: unchanged
        import subprocess
        import sys
        env = {**{k: v for k, v in os.environ.items() if k != "ICLR_CORPUS"}, "ICLR_CORPUS": "pooled"}
        code = (f"import sys; sys.modules['__main__'].__file__ = {str(TOPICS / 'k_sensitivity.py')!r}; "   # a stand-in
                f"sys.path.insert(0, {str(TOPICS)!r}); import common")          # __main__: nothing could run if broken
        r = subprocess.run([sys.executable, "-c", code], cwd=ROOT, env=env, capture_output=True, text=True, timeout=300)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("cannot run under ICLR_CORPUS=pooled", r.stderr)

    def test_pooled_paths(self):
        m = topic_layer("pooled")
        self.assertEqual((m.CORPUS, m.OUTPUT, m.DISCOVERY_OUTPUT, m.DATA, m.CACHE),
                         ("pooled", POOLED, FROZEN, ROOT / "data", CACHE))

    def test_unknown_value_is_refused(self):
        with self.assertRaises(ValueError):
            topic_layer("confirmation")

    def test_unset_loaders_are_unchanged(self):
        m = topic_layer(None)
        frozen = frozen_load_corpus()
        pd.testing.assert_frame_equal(m.load_corpus(), frozen)
        pd.testing.assert_frame_equal(m.embedded_corpus(), frozen[frozen.has_text].reset_index(drop=True))
        if (CACHE / "specter2.npy").exists():
            emb, ids = m.load_embeddings()
            self.assertTrue(ids.equals(pd.read_csv(CACHE / "specter2_ids.csv").submission_id))
            self.assertTrue(np.array_equal(emb, np.load(CACHE / "specter2.npy")))


@unittest.skipUnless(km.TABLE.exists(), "run research/topics/keyword_map.py first")
class PooledCorpus(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.disc, cls.pooled = topic_layer(None), topic_layer("pooled")
        cls.d, cls.p = cls.disc.load_corpus(), cls.pooled.load_corpus()

    def test_pooled_order_and_discovery_subset(self):
        p = self.p
        self.assertEqual(p.split.value_counts().to_dict(), {"discovery": 43516, "confirmation": 11113})
        self.assertTrue(p.submission_id.is_unique)
        key = list(zip(p.year, p.submission_id))
        self.assertEqual(key, sorted(key))
        sub = p[p.split == "discovery"].drop(columns="split").reset_index(drop=True)
        pd.testing.assert_frame_equal(sub, self.d)                      # discovery rows, order and keyword lists untouched
        self.assertTrue(set(p.columns) <= set(CONTENT_COLUMNS) | {"keywords", "split", "has_text"})

    def test_confirmation_keywords_are_the_lookup_of_raw_keywords(self):
        raw = self.pooled.read_table("submissions.csv.gz", ["submission_id", "keywords"], self.pooled.CONFIRMATION)
        c = self.p[self.p.split == "confirmation"].set_index("submission_id")
        table = km.load_table()
        self.assertEqual(c.keywords.loc[raw.submission_id].tolist(), [km.normalize(r, table) for r in raw.keywords])
        self.assertTrue(c.normalized_keywords_json.isna().all())
        self.assertTrue(all(k == sorted(set(k)) for k in c.keywords))

    def test_embedded_corpus_and_embeddings(self):
        e = self.pooled.embedded_corpus()
        self.assertEqual((len(e), int((e.split == "confirmation").sum())), (N_POOLED, N_CONFIRMATION))
        pd.testing.assert_frame_equal(e[e.split == "discovery"].drop(columns="split").reset_index(drop=True),
                                      self.disc.embedded_corpus())
        if not (CACHE / "specter2_released.npy").exists():
            return
        released = pd.read_csv(CACHE / "specter2_released_ids.csv").submission_id
        self.assertTrue(e.submission_id[e.split == "confirmation"].reset_index(drop=True).equals(released))
        emb, ids = self.pooled.load_embeddings()
        self.assertTrue(ids.equals(e.submission_id))
        new = (e.split == "confirmation").to_numpy()
        self.assertTrue(np.array_equal(emb[~new], np.load(CACHE / "specter2.npy")))
        self.assertTrue(np.array_equal(emb[new], np.load(CACHE / "specter2_released.npy")))


class KeywordMap(unittest.TestCase):
    def test_f_lowercases_and_collapses_whitespace_only(self):
        self.assertEqual(km.f("  Graph   Neural\tNetworks "), "graph neural networks")
        self.assertEqual(km.f("Self-Supervised (SSL)."), "self-supervised (ssl).")

    def test_learn_identity_single_residual_and_passes(self):
        lm, rlhf = "large language models", "reinforcement learning from human feedback"
        raw = [["LLM", "Agents"], ["LLM"], ["llm"], ["Diffusion"], ["LLM", "RLHF"], ["Diffusion Model", "Diffusion Models."]]
        norm = [["agents", lm], [lm], ["llm"], ["diffusion models"], [lm, rlhf], ["diffusion models"]]
        votes, stats = km.learn(raw, norm)
        self.assertEqual(votes["agents"], collections.Counter({"agents": 1}))                    # identity
        self.assertEqual(votes["diffusion"], collections.Counter({"diffusion models": 1}))        # single residual
        # paper 5: llm goes to its majority target (in N) in the first pass; rlhf and the last keyword then pair up
        self.assertEqual(votes["llm"], collections.Counter({lm: 3, "llm": 1}))
        self.assertEqual(votes["rlhf"], collections.Counter({rlhf: 1}))
        self.assertNotIn("diffusion model", votes)          # paper 6: two forms against one keyword, no pair is guessed
        self.assertEqual((stats["pass_majority_votes"], stats["pass_pair_votes"], stats["papers_unresolved_after_passes"]),
                         (1, 1, 1))
        self.assertEqual(km.table_of(votes)["llm"], lm)

    def test_majority_and_ties(self):
        C = collections.Counter
        self.assertEqual(km.target(C({"x": 3, "y": 5}), "x"), "y")
        self.assertEqual(km.target(C({"b": 2, "a": 2, "x": 2}), "x"), "x")          # identity wins a tie
        self.assertEqual(km.target(C({"b": 2, "a": 2}), "x"), "a")                   # else alphabetical

    def test_normalize(self):
        table = {"llm": "large language models", "gans": "generative adversarial networks"}
        self.assertEqual(km.normalize('["LLM", " GANs ", "Large Language Models", "Unseen  Form", "a; b", "  "]', table),
                         ["a; b", "generative adversarial networks", "large language models", "unseen form"])
        self.assertEqual(km.normalize(["LLM"], table), ["large language models"])
        self.assertEqual(km.normalize(np.nan, table), [])
        self.assertEqual(km.normalize("[]", table), [])

    def test_table_round_trip_keeps_odd_forms_as_text(self):
        votes = {x: collections.Counter({t: 2, x: 1}) for x, t in
                 [("nan", "not a number"), ("null", "null hypothesis"), ('a "quoted", form', "quoted form"), ("na", "na")]}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "t.csv.gz"
            topic_layer(None).write_csv_gz(km.table_frame(votes), path)
            self.assertEqual(km.load_table(path), km.table_of(votes))

    @unittest.skipUnless(km.TABLE.exists(), "run research/topics/keyword_map.py first")
    def test_written_table_is_learned_from_discovery(self):
        d = topic_layer(None).read_table("submissions.csv.gz", km.COLUMNS)
        votes, _ = km.learn(d.keywords.map(km.as_list), d.normalized_keywords_json.map(km.as_list))
        self.assertEqual(km.load_table(), km.table_of(votes))
        report = json.loads(km.REPORT.read_text())
        self.assertEqual(report["table"]["sha256"], hashlib.sha256(km.TABLE.read_bytes()).hexdigest())
        self.assertEqual(report["vocabularies"]["V759"], 759)
        self.assertEqual(report["vocabularies"]["PH4_68"], 68)


@unittest.skipUnless((POOLED / "pooled_topics_report.json").exists(), "run research/topics/pooled_topics.py first")
class PooledOutputs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.split = pd.read_csv(POOLED / "split.csv.gz")
        cls.disc = (cls.split.split == "discovery").to_numpy()
        cls.report = json.loads((POOLED / "pooled_topics_report.json").read_text())

    def test_split_file_is_pooled_order(self):
        ta = pd.read_csv(POOLED / "topic_assignments.csv.gz")
        self.assertEqual((len(self.split), int(self.disc.sum())), (N_POOLED, N_DISCOVERY))
        self.assertTrue(ta.submission_id.equals(self.split.submission_id))
        key = list(zip(ta.year, ta.submission_id))
        self.assertEqual(key, sorted(key))

    def test_discovery_rows_equal_the_discovery_files(self):
        for t in TABLES:
            p, d = lines(POOLED / f"{t}.csv.gz"), lines(FROZEN / f"{t}.csv.gz")
            self.assertEqual(p[0], d[0], t)
            self.assertEqual(len(p) - 2, N_POOLED, t)
            self.assertEqual(np.asarray(p[1:-1], dtype=object)[self.disc].tolist(), d[1:-1], t)
            ids = pd.read_csv(POOLED / f"{t}.csv.gz", usecols=["submission_id"]).submission_id
            self.assertTrue(ids.equals(self.split.submission_id), t)
        p = lines(POOLED / "paper_contributions.csv.gz")
        self.assertEqual(np.asarray(p[1:-1], dtype=object)[~self.disc].tolist(),
                         lines(FROZEN / "paper_contributions_released.csv.gz")[1:-1])

    def test_copies_are_byte_identical(self):
        for name in COPIES:
            self.assertEqual((POOLED / name).read_bytes(), (FROZEN / name).read_bytes(), name)

    def test_every_new_paper_is_placed(self):
        new = ~self.disc
        for t in ["topic_assignments", "k_sensitivity_assignments", "hindsight_assignments"]:
            self.assertFalse(pd.read_csv(POOLED / f"{t}.csv.gz")[new].isna().any().any(), t)
        lab = pd.read_csv(POOLED / "paper_contributions.csv.gz")
        self.assertFalse(lab[["primary_type", "primary_class", "foundation_model", "uncertain"]].isna().any().any())
        stab = pd.read_csv(POOLED / "paper_topic_stability.csv.gz")[new]
        gate = self.report["stability"]["gate_discovery_mid_stability_reproduced"]
        self.assertEqual(stab.mid_stability.notna().all(), gate)
        self.assertTrue(stab.coarse_stability.isna().all() and stab.fine_stability.isna().all())

    def test_report_gates(self):
        r = self.report
        self.assertTrue(r["k100"]["discovery_reproduced_exactly"])
        for col, m in r["maps"].items():                    # the label convention follows the gate
            self.assertEqual(m["convention"] == "exact re-derived centres", m["gate_discovery_labels_reproduced"], col)
        c = r["checks"]
        self.assertTrue(all(c["discovery_rows_byte_identical"].values()) and all(c["copies_byte_identical"].values()))
        self.assertTrue(c["protected_files_unchanged"] and c["frozen_artefacts_match_FREEZE_json"])
        for name, digest in r["files"].items():
            self.assertEqual(hashlib.sha256((POOLED / name).read_bytes()).hexdigest(), digest, name)


if __name__ == "__main__":
    unittest.main()
