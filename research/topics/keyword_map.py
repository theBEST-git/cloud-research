"""Author keywords for papers without curated normalisation: the confirmation split (POOLED_SPEC D3).

Discovery papers carry curated normalised keywords (normalized_keywords_json, joined in from the external keyword
export). The confirmation export has raw author keywords only. A lookup table T from raw form to normalised keyword
is learned from the discovery split alone (raw `keywords` against normalized_keywords_json; content columns only):
A1. f(s) = " ".join(s.strip().lower().split()); nothing else (no NFKC, no casefold).
A2. Per discovery paper: FR = its distinct non-empty f(raw) forms, N = its normalised list.
A3. Identity evidence: every x in FR that is also in N votes x -> x.
A4. Single residual: if exactly one form of FR is outside N and exactly one keyword of N is outside FR, that pair votes.
A5. Two further passes over the papers whose residual forms A4 left unpaired: a residual form whose current majority
    target is in N votes for it; if exactly one form and one keyword are then left, that pair votes.
A6. T(x) = the target with most votes; a tie goes to x itself if x is tied, otherwise to the alphabetically first.
A7. normalize(raw): parse the JSON list; y = f(x) per element (empty ones dropped); y = T.get(y, y), so an unseen form
    stays f(raw) and no concept assignment is invented; no splitting on ';'; deduplicate and sort.
A8. Discovery lists are never re-normalised: T does not reproduce every curated (partly context-dependent) list.

Writes output_pooled/keyword_map.csv.gz (raw form, keyword, its votes, all votes) and keyword_map_report.json: the
table's sha256, in-sample replication, recall/precision over 3 random 80/20 splits of discovery (learn on 80%, apply
to 20%) for the frozen 759-keyword buzzword vocabulary, the 68 PH4 keywords and 'federated learning', and coverage
on the confirmation split.

    python research/topics/keyword_map.py
"""
from __future__ import annotations

import collections
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
TABLE = HERE / "output_pooled" / "keyword_map.csv.gz"
REPORT = HERE / "output_pooled" / "keyword_map_report.json"
COLUMNS = ["submission_id", "keywords", "normalized_keywords_json"]
V759_TYPES = ("research_area", "specific_topic")                                         # fashion/buzzwords.TYPES
PH4_TYPES, PH4_MIN_PAPERS = ("research_area", "specific_topic", "property", "application_domain"), 200  # fashion/posthoc
FL_KEYWORD = "federated learning"
PASSES, CV_REPS, CV_TEST_SHARE, CV_SEED = 2, 3, 0.2, 0


def f(s: str) -> str:
    return " ".join(s.strip().lower().split())


def as_list(value) -> list[str]:
    """A keyword cell as a list: the exports store JSON lists; null is no keyword."""
    if isinstance(value, str):
        return json.loads(value)
    return [] if value is None or (isinstance(value, float) and np.isnan(value)) else list(value)


def target(votes: collections.Counter, x: str) -> str:
    """Majority target of raw form x; ties go to x itself if tied, otherwise to the alphabetically first."""
    top = max(votes.values())
    tied = sorted(k for k, v in votes.items() if v == top)
    return x if x in tied else tied[0]


def learn(raw_lists, norm_lists) -> tuple[dict[str, collections.Counter], dict]:
    """Votes raw form -> normalised keyword (rules A2-A5), and counts of the evidence behind them."""
    votes: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    stats = collections.Counter()
    pending = []
    for raw, norm in zip(raw_lists, norm_lists):
        fr = list(dict.fromkeys(y for y in map(f, raw) if y))
        ns = set(norm)
        for x in fr:
            if x in ns:
                votes[x][x] += 1
                stats["identity_votes"] += 1
        ur = [x for x in fr if x not in ns]
        un = [k for k in norm if k not in set(fr)]
        if len(ur) == 1 and len(un) == 1:
            votes[ur[0]][un[0]] += 1
            stats["single_residual_votes"] += 1
        elif ur:
            pending.append((ur, un, ns))
    stats["papers_with_unpaired_residuals"] = len(pending)
    for _ in range(PASSES):
        left_over = []
        for ur, un, ns in pending:
            used, left = set(), []
            for x in ur:
                t = target(votes[x], x) if x in votes else None
                if t is not None and t in ns:
                    votes[x][t] += 1
                    used.add(t)
                    stats["pass_majority_votes"] += 1
                else:
                    left.append(x)
            un = [k for k in un if k not in used]
            if len(left) == 1 and len(un) == 1:
                votes[left[0]][un[0]] += 1
                stats["pass_pair_votes"] += 1
            elif left and un:
                left_over.append((left, un, ns))
        pending = left_over
    stats["papers_unresolved_after_passes"] = len(pending)
    return dict(votes), dict(stats)


def table_of(votes: dict[str, collections.Counter]) -> dict[str, str]:
    return {x: target(v, x) for x, v in votes.items()}


def normalize(raw, table: dict[str, str] | None = None) -> list[str]:
    """Rule A7: raw author keywords (JSON list or list) -> sorted, deduplicated normalised keywords."""
    table = load_table() if table is None else table
    return sorted({table.get(y, y) for y in map(f, as_list(raw)) if y})


def table_frame(votes: dict[str, collections.Counter]) -> pd.DataFrame:
    rows = [(x, t, v[t], sum(v.values())) for x, v in votes.items() for t in [target(v, x)]]
    return pd.DataFrame(rows, columns=["raw", "keyword", "votes", "total_votes"]).sort_values("raw").reset_index(drop=True)


def load_table(path: Path = TABLE) -> dict[str, str]:
    """The written table T (every field a string: forms such as 'nan' or 'null' stay text)."""
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing; run research/topics/keyword_map.py first")
    t = pd.read_csv(path, dtype=str, keep_default_na=False, na_filter=False)
    return dict(zip(t.raw, t.keyword))


def scores(pred, truth, vocab: set[str] | None = None) -> dict:
    """Micro recall/precision of predicted keyword uses against the curated lists (optionally within a vocabulary)."""
    tp = fp = fn = 0
    for p, t in zip(pred, truth):
        p, t = set(p), set(t)
        if vocab is not None:
            p, t = p & vocab, t & vocab
        tp, fp, fn = tp + len(p & t), fp + len(p - t), fn + len(t - p)
    return {"recall": round(tp / max(tp + fn, 1), 4), "precision": round(tp / max(tp + fp, 1), 4), "true_uses": tp + fn}


def evaluate(raw, norm, table: dict[str, str], vocabs: dict) -> dict:
    pred = [normalize(r, table) for r in raw]
    return {"paper_exact": round(float(np.mean([p == list(n) for p, n in zip(pred, norm)])), 4),
            **{name: scores(pred, norm, v) for name, v in vocabs.items()}}


def cross_validate(raw: pd.Series, norm: pd.Series, vocabs: dict) -> dict:
    """Learn T on a random 80% of discovery papers, score the held-out 20% (lookup + identity vs identity only)."""
    rng = np.random.default_rng(CV_SEED)
    reps = []
    for _ in range(CV_REPS):
        test = rng.random(len(raw)) < CV_TEST_SHARE
        table = table_of(learn(raw[~test], norm[~test])[0])
        uses = [f(x) for r in raw[test] for x in r if f(x)]
        reps.append({"seen_raw_use_share": round(sum(u in table for u in uses) / len(uses), 4),
                     "lookup_identity": evaluate(raw[test], norm[test], table, vocabs),
                     "identity_only": evaluate(raw[test], norm[test], {}, vocabs)})

    def mean(get) -> float:
        return round(float(np.mean([get(r) for r in reps])), 4)
    out = {"reps": CV_REPS, "test_share": CV_TEST_SHARE, "seed": CV_SEED,
           "seen_raw_use_share": mean(lambda r: r["seen_raw_use_share"])}
    for rule in ("lookup_identity", "identity_only"):
        out[rule] = {"paper_exact": mean(lambda r: r[rule]["paper_exact"])}
        for v in vocabs:
            out[rule][v] = {m: mean(lambda r: r[rule][v][m]) for m in ("recall", "precision")}
            out[rule][v]["true_uses"] = sum(r[rule][v]["true_uses"] for r in reps)
    out["by_rep"] = reps
    return out


def coverage(lists, vocabs: dict) -> dict:
    """Papers listing at least one keyword of each vocabulary."""
    hits = {name: sum(bool(set(k) & v) for k in lists) for name, v in vocabs.items() if v is not None}
    return {name: {"papers": int(h), "share": round(h / len(lists), 4)} for name, h in hits.items()}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    from common import CONFIRMATION, DATA, DISCOVERY_OUTPUT, read_table, write_csv_gz
    TABLE.parent.mkdir(exist_ok=True)
    d = read_table("submissions.csv.gz", COLUMNS)
    raw, norm = d.keywords.map(as_list), d.normalized_keywords_json.map(as_list)
    votes, stats = learn(raw, norm)
    table = table_of(votes)
    write_csv_gz(table_frame(votes), TABLE)
    if load_table() != table:
        raise RuntimeError("keyword_map.csv.gz does not read back as the learned table")

    kt = pd.read_csv(DISCOVERY_OUTPUT / "keyword_types.csv", keep_default_na=False)
    vocabs = {"V759": set(kt[kt.type.isin(V759_TYPES)].keyword),
              "PH4_68": set(kt[kt.type.isin(PH4_TYPES) & (kt.papers >= PH4_MIN_PAPERS)].keyword),
              "federated_learning": {FL_KEYWORD}, "all": None}
    if (len(vocabs["V759"]), len(vocabs["PH4_68"])) != (759, 68) or FL_KEYWORD not in vocabs["PH4_68"]:
        raise RuntimeError("The frozen keyword vocabularies changed")

    c = read_table("submissions.csv.gz", ["submission_id", "keywords"], CONFIRMATION)
    c_raw = c.keywords.map(as_list)
    c_kw = c_raw.map(lambda r: normalize(r, table))
    c_id = c_raw.map(lambda r: normalize(r, {}))
    empty = (c_kw.str.len() == 0) & c_raw.map(lambda r: any(f(x) for x in r))
    if empty.any():
        raise RuntimeError(f"{int(empty.sum())} confirmation papers lost every keyword")
    uses = [f(x) for r in c_raw for x in r if f(x)]
    multi = {x: v for x, v in votes.items() if len(v) > 1}
    tied = sorted(x for x, v in votes.items() if list(v.values()).count(max(v.values())) > 1)
    report = {
        "rule": __doc__.split("\n\n")[1],
        "table": {"path": str(TABLE.relative_to(HERE.parents[1])), "sha256": sha256(TABLE), "raw_forms": len(table),
                  "non_identity_forms": sum(x != t for x, t in table.items()),
                  "context_dependent_forms": len(multi), "tie_resolved_forms": tied,
                  "largest_context_dependent": {x: dict(v.most_common(4)) for x, v in
                                                sorted(multi.items(), key=lambda kv: (-sum(kv[1].values()), kv[0]))[:15]},
                  **stats},
        "inputs": {"discovery_submissions_sha256": sha256(DATA / "submissions.csv.gz"),
                   "confirmation_submissions_sha256": sha256(CONFIRMATION / "submissions.csv.gz"),
                   "keyword_types_sha256": sha256(DISCOVERY_OUTPUT / "keyword_types.csv"),
                   "discovery_papers": len(d), "confirmation_papers": len(c)},
        "vocabularies": {k: (len(v) if v is not None else "every keyword") for k, v in vocabs.items()},
        "in_sample": evaluate(raw, norm, table, vocabs),
        "cross_validated": cross_validate(raw, norm, vocabs),
        "confirmation": {"raw_uses": len(uses), "seen_raw_use_share": round(sum(u in table for u in uses) / len(uses), 4),
                         "distinct_unseen_forms": len({u for u in uses if u not in table}),
                         "papers_changed_by_table": int((c_kw != c_id).sum()),
                         "papers_with_semicolon_element": int(c_raw.map(lambda r: any(";" in x for x in r)).sum()),
                         "coverage_table": coverage(c_kw, vocabs), "coverage_identity_only": coverage(c_id, vocabs)},
        "discovery_coverage_curated": coverage(norm, vocabs),
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("table", "in_sample")}, indent=1)[:3000])
    print(json.dumps({k: v for k, v in report["cross_validated"].items() if k != "by_rep"}, indent=1))
    print(json.dumps(report["confirmation"], indent=1), json.dumps(report["discovery_coverage_curated"]))


if __name__ == "__main__":
    main()
