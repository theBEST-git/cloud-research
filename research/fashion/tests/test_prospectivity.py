"""Every RQ2/RQ3 variable for a year-t paper uses only papers from before t (PREREGISTRATION.md D2, D3, D5, R1).

Each builder is checked against a brute-force reference on synthetic data, and by perturbing later papers.

    python -m unittest discover -s research/fashion/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from buzzwords import build  # noqa: E402
from resubmissions import nearest_earlier  # noqa: E402
from topic_maturity import maturity  # noqa: E402
from variables import hot_flags, incumbency  # noqa: E402

YEARS = np.arange(2017, 2023)


def synthetic_papers(rng: np.random.Generator, n: int = 400, topics: int = 5, keys: int = 60):
    ids = pd.Series([f"p{i}" for i in range(n)])
    year = pd.Series(rng.choice(YEARS, n))
    topic = pd.Series(rng.integers(0, topics, n))
    rows = [(ids[i], f"a{k}") for i in range(n) for k in rng.choice(keys, rng.integers(1, 4), replace=False)]
    authors = pd.DataFrame(rows, columns=["submission_id", "key"])
    return ids, year, topic, authors


def brute_incumbency(ids, year, topic, authors, earlier=None):
    by_paper = authors.groupby("submission_id").key.apply(set).to_dict()
    y, tp = dict(zip(ids, year)), dict(zip(ids, topic))
    chain = {}
    for s in ids:
        c, e = set(), (earlier or {}).get(s)
        while e is not None and e not in c:
            c.add(e)
            e = (earlier or {}).get(e)
        chain[s] = c
    out = {}
    for s in ids:
        others = [o for o in ids if tp[o] == tp[s] and y[o] < y[s]]
        mine = by_paper.get(s, set())
        inc = any(mine & by_paper.get(o, set()) for o in others)
        w2 = any(mine & by_paper.get(o, set()) for o in others if y[o] >= y[s] - 2)
        s4 = any(mine & by_paper.get(o, set()) for o in others if o not in chain[s])
        out[s] = (float(inc), float(w2), float(s4))
    return pd.DataFrame.from_dict(out, orient="index", columns=["incumbent", "incumbent_w2", "incumbent_s4"])


class Incumbency(unittest.TestCase):
    def test_matches_brute_force(self):
        rng = np.random.default_rng(0)
        ids, year, topic, authors = synthetic_papers(rng)
        # chains of earlier versions, including a 3-link chain and a cross-topic link that must be ignored
        order = ids[np.argsort(year.values, kind="stable")].tolist()
        earlier = {order[-1]: order[200], order[200]: order[50], order[-2]: order[10], order[-3]: order[-4]}
        got = incumbency(authors, topic, year, ids, pd.Series(earlier)).sort_index()
        want = brute_incumbency(ids.tolist(), year.tolist(), topic.tolist(), authors, earlier).sort_index()
        pd.testing.assert_frame_equal(got, want, check_names=False)

    def test_later_papers_do_not_matter(self):
        rng = np.random.default_rng(1)
        ids, year, topic, authors = synthetic_papers(rng)
        base = incumbency(authors, topic, year, ids)
        cut = 2020
        late = set(ids[year > cut])
        topic2 = topic.copy()
        topic2[year > cut] = rng.integers(0, 5, (year > cut).sum())
        authors2 = authors.copy()
        m = authors2.submission_id.isin(late)
        authors2.loc[m, "key"] = [f"a{k}" for k in rng.integers(0, 60, m.sum())]
        authors2 = authors2.drop_duplicates()
        pert = incumbency(authors2, topic2, year, ids)
        early = ids[year <= cut]
        pd.testing.assert_frame_equal(base.loc[early], pert.loc[early])


class Maturity(unittest.TestCase):
    def test_prior_growth_and_maturity_ignore_later_years(self):
        rng = np.random.default_rng(2)
        year = pd.Series(rng.choice(YEARS, 3000))
        topic = pd.Series(rng.integers(0, 12, 3000))
        base = maturity(topic, year)
        topic2 = topic.copy()
        topic2[year >= 2021] = rng.integers(0, 12, (year >= 2021).sum())
        pert = maturity(topic2, year)
        cols = ["topic", "year", "log_cum_prior", "prior_growth"]
        a = base[base.year <= 2021][cols].reset_index(drop=True)
        b = pert[pert.year <= 2021][cols].reset_index(drop=True)
        pd.testing.assert_frame_equal(a, b)

    def test_hot_is_top_quintile_per_year(self):
        mat = pd.DataFrame({"topic": np.tile(np.arange(10), 2), "year": np.repeat([2019, 2020], 10),
                            "prior_growth": np.r_[np.arange(10.0), np.arange(10.0)[::-1]]})
        hot = hot_flags(mat).set_index(["year", "topic"]).hot
        self.assertEqual(sorted(hot.loc[2019][hot.loc[2019] == 1].index), [8, 9])
        self.assertEqual(sorted(hot.loc[2020][hot.loc[2020] == 1].index), [0, 1])


def synthetic_keywords(rng: np.random.Generator, n: int = 2500, d: int = 16):
    years = rng.choice(np.arange(2015, 2027), n)
    x = rng.normal(size=(n, d))
    x /= np.linalg.norm(x, axis=1, keepdims=True)
    vocab = [f"k{i}" for i in range(8)]
    kws = pd.Series([list(rng.choice(vocab + ["noise"], rng.integers(0, 4), replace=False)) for _ in range(n)])
    return kws, years, x, set(vocab)


class Buzzwords(unittest.TestCase):
    def test_threshold_and_cosine_match_brute_force(self):
        rng = np.random.default_rng(3)
        kws, years, x, vocab = synthetic_keywords(rng)
        kw, uses = build(kws, years, x, vocab)
        for _, r in kw[kw.eligible].sample(6, random_state=0).iterrows():
            prior = [i for i in range(len(kws)) if r.keyword in kws[i] and years[i] < r.year]
            loo = []
            for i in prior:
                c = x[[j for j in prior if j != i]].sum(axis=0)
                loo.append(x[i] @ c / np.linalg.norm(c))
            self.assertAlmostEqual(r.threshold, np.percentile(loo, 10), places=10)
            cen = x[prior].sum(axis=0)
            cen /= np.linalg.norm(cen)
            cur = uses[(uses.keyword == r.keyword) & (uses.year == r.year)]
            np.testing.assert_allclose(cur.cos.to_numpy(), x[cur.paper.to_numpy()] @ cen, atol=1e-12)
            n_year = pd.Series(years).value_counts()
            c1 = sum(r.keyword in kws[i] and years[i] == r.year - 1 for i in range(len(kws)))
            c2 = sum(r.keyword in kws[i] and years[i] == r.year - 2 for i in range(len(kws)))
            self.assertAlmostEqual(r.growth, ((c1 + .5) / n_year[r.year - 1]) / ((c2 + .5) / n_year[r.year - 2]))
            self.assertEqual(r.eligible, len(prior) >= 10)

    def test_later_papers_do_not_matter(self):
        rng = np.random.default_rng(4)
        kws, years, x, vocab = synthetic_keywords(rng)
        kw, uses = build(kws, years, x, vocab)
        cut = 2020
        late = years > cut
        x2 = x.copy()
        x2[late] = rng.normal(size=(late.sum(), x.shape[1]))
        x2[late] /= np.linalg.norm(x2[late], axis=1, keepdims=True)
        kws2 = kws.copy()
        for i in np.where(late)[0]:
            kws2[i] = list(rng.choice(sorted(vocab), 2, replace=False))
        kw2, uses2 = build(kws2, years, x2, vocab)
        a = kw[kw.year <= cut].reset_index(drop=True)
        b = kw2[kw2.year <= cut].reset_index(drop=True)
        pd.testing.assert_frame_equal(a, b)
        key = ["keyword", "year", "paper"]
        a = uses[uses.year <= cut].sort_values(key).reset_index(drop=True)
        b = uses2[uses2.year <= cut].sort_values(key).reset_index(drop=True)
        pd.testing.assert_frame_equal(a, b)

    def test_same_year_papers_do_not_affect_each_other(self):
        rng = np.random.default_rng(5)
        kws, years, x, vocab = synthetic_keywords(rng)
        _, uses = build(kws, years, x, vocab)
        t = 2021
        same = np.where(years == t)[0]
        keep, move = same[: len(same) // 2], same[len(same) // 2:]
        x2 = x.copy()
        x2[move] = -x2[move]
        _, uses2 = build(kws, years, x2, vocab)
        key = ["keyword", "year", "paper"]
        a = uses[uses.paper.isin(keep)].sort_values(key).reset_index(drop=True)
        b = uses2[uses2.paper.isin(keep)].sort_values(key).reset_index(drop=True)
        pd.testing.assert_frame_equal(a, b)


class Resubmissions(unittest.TestCase):
    def test_nearest_earlier_matches_brute_force(self):
        rng = np.random.default_rng(6)
        years = rng.choice(YEARS, 500)
        x = rng.normal(size=(500, 8)).astype(np.float32)
        x /= np.linalg.norm(x, axis=1, keepdims=True)
        nn, cos = nearest_earlier(x, years)
        for i in range(500):
            earlier = np.where(years < years[i])[0]
            if not len(earlier):
                self.assertEqual(nn[i], -1)
                continue
            sims = x[earlier] @ x[i]
            self.assertEqual(nn[i], earlier[sims.argmax()])
            self.assertAlmostEqual(cos[i], sims.max(), places=5)


if __name__ == "__main__":
    unittest.main()
