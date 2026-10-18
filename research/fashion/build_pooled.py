"""Pooled fashion features (POOLED_SPEC D5; PREREGISTRATION.md D2, D3, D14, D15): every input panel.frame() reads,
built for the pooled corpus (discovery + the released confirmation papers) with the unchanged builders, then checked
and recorded in output_pooled/build_report.json. Outcome-free: no submissions table and no outcome is read, and no
label is related to any feature (labels are only checked for gaps).

Order (each builder in its own process with ICLR_CORPUS=pooled, so every path is pooled from the first import):
1. build_pooled_inputs.py      pooled author table (git-ignored) and byte-identical copies of the frozen constants
2. topic_maturity.py           maturity, shares and prior_growth over all 54,579 papers, every map
3. resubmissions.py --tau τ    the frozen discovery centring mean and τ (the builder refuses anything else); nearest
                               earlier neighbours and exact titles range over all earlier-year pooled papers
4. buzzwords.py                the frozen 759-keyword vocabulary (the byte-identical keyword_types.csv copy)
5. variables.py                incumbency on pooled history (D2), hot (D3), team size
then panel.frame(m) for every map of panel.MAPS in this process, split by run_confirmation's own mask.

Gates (all are evaluated and recorded; any failure exits non-zero after the report is written):
- frozen inputs: the topic layer's four frozen copies and the three output_pooled constants are byte-identical to the
  discovery files; the pooled author table matches its manifest; the vocabulary has 759 keywords; τ is the frozen one;
- shape: 54,579 papers (43,480 discovery + 11,099 confirmation) in pooled order P in every paper-level file and every
  map; the discovery rows of P are the discovery order and carry the discovery topics in every map;
- frames: panel.frame(m) has 54,579 rows for every map, 11,099 after the confirmation mask (which equals the topic
  layer's split file), no missing topic, label or maturity, and hot / prior_growth / incumbent / buzzword missing
  exactly where the builders define them as missing; the label table has no gap in primary_type, primary_class,
  foundation_model or uncertain;
- discovery invariants (pooling only adds earlier papers and authors): discovery rows keep team_size and
  has_author_key; no discovery paper loses incumbent or incumbent_w2; no discovery topic-year loses papers or prior
  papers; a discovery paper whose pooled nearest earlier paper is a discovery paper keeps its discovery neighbour and
  cosine (this also proves the frozen centring mean), otherwise its cosine can only rise; its exact-title match and its
  probable earlier version cannot disappear;
- untouched: the sha256 of every FREEZE.json-listed file, every file under research/fashion/output,
  research/topics/output, research/topics/output_pooled and data_confirmation_csv and the SPECTER2 caches, and
  `git status` of the discovery outputs and the FREEZE-listed files, are the same before and after the build.
Comparisons (reported, never gated), next to the probe values of the integration map (k100): hot changes, incumbency
rates and flips, maturity shifts, earlier versions and buzzword flags. Counts and rates only, no name, title or id.

Running it twice gives byte-identical feature files (deterministic gzip); only the report's timings change.
--check-only runs no builder: it re-checks the built files and rewrites the report (with no steps).

    python research/fashion/build_pooled.py [--check-only]
"""
from __future__ import annotations

import os

if __name__ == "__main__":                           # the corpus switch precedes every fashion import (common.py, D1)
    if (os.environ.get("ICLR_CORPUS") or "pooled") != "pooled":
        raise SystemExit("build_pooled.py builds the pooled corpus: unset ICLR_CORPUS or set it to 'pooled'")
    os.environ["ICLR_CORPUS"] = "pooled"

import argparse  # noqa: E402
import json  # noqa: E402
import platform  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import common  # noqa: E402
from build_pooled_inputs import AUTHORS, COPIES, MANIFEST  # noqa: E402
from common import DISCOVERY_OUTPUT, POOLED_OUTPUT, ROOT  # noqa: E402
from outcomes import FREEZE_DISCOVERY, sha256  # noqa: E402
from buzzwords import YEARS as BUZZ_YEARS  # noqa: E402
from topic_maturity import maturity  # noqa: E402
from variables import hot_flags, load_authors  # noqa: E402

HERE = Path(__file__).resolve().parent
TOPICS_DIR = ROOT / "research" / "topics"
DISCOVERY_TOPICS, POOLED_TOPICS = TOPICS_DIR / "output", TOPICS_DIR / "output_pooled"
REPORT = POOLED_OUTPUT / "build_report.json"
LOG = POOLED_OUTPUT / "checks" / "build_stdout.txt"
BUILDERS = ["build_pooled_inputs.py", "topic_maturity.py", "resubmissions.py", "buzzwords.py", "variables.py"]
WRITTEN = ["topic_year_maturity.csv.gz", "earlier_versions.csv.gz", "keyword_year.csv.gz", "keyword_uses.csv.gz",
           "paper_buzzword.csv.gz", "paper_variables.csv.gz", "checks/resubmissions.json", "checks/buzzwords.json",
           "checks/buzzword_examples.md", "checks/variables.json"]
TOPIC_COPIES = ["topic_catalog.csv", "keyword_types.csv", "topic_model.npz", "hindsight_check.json"]
LABELS = ["primary_type", "primary_class", "foundation_model", "uncertain"]
PAPERS = {"discovery": 43480, "confirmation": 11099}
VOCABULARY = 759
FIRST_HOT = 2019                                   # hot / prior_growth need t-1 and t-2 (D3)
COS_TOL = 2e-5                                     # nn_cos is written with 5 decimals
PREDICTED = {"source": "integration map probe (pipeline_map.json, fashion variables), k100, pooled against discovery "
                       "history, before this build",
             "hot_topic_years_changed": "69 of 800", "discovery_papers_with_hot_changed_share": 0.081,
             "discovery_newcomer_to_incumbent": 1515, "discovery_incumbent_rate": "0.265 -> 0.300",
             "confirmation_incumbent_rate": 0.309, "discovery_probable_earlier_versions": "170 -> 224",
             "discovery_earlier_versions_pointing_to_confirmation": 54, "confirmation_probable_earlier_versions": 58,
             "confirmation_earlier_versions_pointing_to_discovery": 39, "maturity_level_shift": "about log 1.25"}


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT)) if ROOT in p.parents else str(p)


def rate(s: pd.Series) -> float | None:
    s = s.dropna()
    return round(float(s.mean()), 4) if len(s) else None


# ---------------------------------------------------------------- untouched files

def freeze_listed() -> list[str]:
    return list(json.loads(FREEZE_DISCOVERY.read_text())["sha256"])


def guarded() -> list[Path]:
    """Files the pooled build must not change: FREEZE-listed files, the discovery outputs of both layers, the pooled
    topic layer (read only here), the confirmation export and the SPECTER2 caches (git-ignored, so hashed)."""
    trees = [f for d in (DISCOVERY_OUTPUT, DISCOVERY_TOPICS, POOLED_TOPICS, ROOT / "data_confirmation_csv")
             for f in d.rglob("*") if f.is_file() and "__pycache__" not in f.parts]
    caches = [f for f in (TOPICS_DIR / "cache").glob("specter2*") if f.is_file()]
    return sorted(set([ROOT / p for p in freeze_listed()] + trees + caches))


def snapshot(paths: list[Path]) -> dict[str, str | None]:
    return {rel(p): sha256(p) if p.exists() else None for p in paths}


def git_status() -> str:
    paths = ["research/fashion/output", "research/topics/output", *freeze_listed()]
    return subprocess.run(["git", "status", "--porcelain", "--", *paths], cwd=ROOT, capture_output=True, text=True,
                          check=True).stdout


def changed(before: dict[str, str | None], after: dict[str, str | None]) -> list[str]:
    return sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))


# ---------------------------------------------------------------- builders

def run_builders(tau: float) -> list[dict]:
    """The unchanged builders, in order, each in a fresh process with ICLR_CORPUS=pooled; stdout goes to LOG."""
    env = {**os.environ, "ICLR_CORPUS": "pooled"}
    steps, log = [], []
    for script in BUILDERS:
        args = ["--tau", repr(tau)] if script == "resubmissions.py" else []
        shown = " ".join(["ICLR_CORPUS=pooled python", rel(HERE / script), *args])
        t0 = time.time()
        r = subprocess.run([sys.executable, str(HERE / script), *args], cwd=ROOT, env=env, capture_output=True, text=True)
        log.append(f"$ {shown}\n{r.stdout}{r.stderr}")
        LOG.parent.mkdir(parents=True, exist_ok=True)
        LOG.write_text("\n".join(log))
        if r.returncode:
            raise SystemExit(f"{shown} failed (exit {r.returncode}); see {rel(LOG)}\n{r.stderr[-4000:]}")
        steps.append({"command": shown, "seconds": round(time.time() - t0, 1)})
        print(f"{shown}: {steps[-1]['seconds']} s", flush=True)
    return steps


# ---------------------------------------------------------------- tables

def tables(fashion: Path, topics: Path) -> dict:
    """The built tables of one corpus (topic ids as text, as panel reads them), with the fine map's maturity."""
    fine = pd.read_csv(topics / "topic_assignments.csv.gz", usecols=["submission_id", "year", "fine"])
    mat = pd.read_csv(fashion / "topic_year_maturity.csv.gz", dtype={"topic": str})
    mat = pd.concat([mat, maturity(fine.fine, fine.year).assign(map="fine")], ignore_index=True)
    mat["topic"] = mat.topic.astype(str)
    return {"mat": mat, "var": pd.read_csv(fashion / "paper_variables.csv.gz", dtype={"topic": str}),
            "ev": pd.read_csv(fashion / "earlier_versions.csv.gz"), "buzz": pd.read_csv(fashion / "paper_buzzword.csv.gz"),
            "kw": pd.read_csv(fashion / "keyword_year.csv.gz"), "fine": fine}


def map_comparison(m: str, d: pd.DataFrame, p: pd.DataFrame, dm: pd.DataFrame, pm: pd.DataFrame,
                   conf: set) -> tuple[dict, dict]:
    """Gates and comparisons of one map. d / p: paper_variables rows of the map (discovery build, pooled build);
    dm / pm: its topic-year maturity."""
    d = d.reset_index(drop=True)
    pdisc = p[~p.submission_id.isin(conf)].reset_index(drop=True)
    pconf = p[p.submission_id.isin(conf)]
    gates = {"discovery_rows_in_discovery_order": bool(pdisc.submission_id.equals(d.submission_id))}
    if not gates["discovery_rows_in_discovery_order"]:
        return gates, {}
    gates["discovery_topics_unchanged"] = bool((pdisc.topic.values == d.topic.values).all())
    gates["discovery_team_size_and_has_author_key_unchanged"] = bool(
        (pdisc.team_size.values == d.team_size.values).all() and (pdisc.has_author_key.values == d.has_author_key.values).all())
    up = {c: int(((d[c] == 0) & (pdisc[c] == 1)).sum()) for c in ("incumbent", "incumbent_w2", "incumbent_s4")}
    down = {c: int(((d[c] == 1) & (pdisc[c] == 0)).sum()) for c in ("incumbent", "incumbent_w2", "incumbent_s4")}
    gates["no_discovery_paper_loses_incumbent_or_incumbent_w2"] = down["incumbent"] == 0 and down["incumbent_w2"] == 0

    key = ["topic", "year"]
    mm = dm.merge(pm, on=key, how="left", suffixes=("_d", "_p"), validate="1:1")
    gates["discovery_topic_years_keep_papers_and_prior_papers"] = bool(
        mm.papers_p.notna().all() and (mm.papers_p >= mm.papers_d).all() and (mm.cum_prior_papers_p >= mm.cum_prior_papers_d).all())
    later = mm[mm.cum_prior_papers_d > 0]
    delta = later.log_cum_prior_p - later.log_cum_prior_d

    hd, hp = hot_flags(dm), hot_flags(pm)
    h = hd.merge(hp, on=key, suffixes=("_d", "_p"))
    h = h[h.year >= FIRST_HOT]
    paper_hot = d.hot.notna() & (d.hot != pdisc.hot)
    keyed, keyed_p = d.has_author_key, pdisc.has_author_key
    recent = d.year >= FIRST_HOT
    cconf = pconf[pconf.has_author_key]
    comp = {
        "topics": int(dm.topic.nunique()),
        "hot": {"topic_years": int(len(h)), "changed": int((h.hot_d != h.hot_p).sum()),
                "on_to_off": int(((h.hot_d == 1) & (h.hot_p == 0)).sum()),
                "off_to_on": int(((h.hot_d == 0) & (h.hot_p == 1)).sum()),
                "discovery_papers_changed": int(paper_hot.sum()),
                "discovery_papers_changed_share": round(float(paper_hot.sum() / d.hot.notna().sum()), 4),
                "paper_share_in_hot_topics": {"discovery_build": rate(d.hot), "pooled_build_discovery_rows": rate(pdisc.hot),
                                              "pooled_build_confirmation_rows": rate(pconf.hot)}},
        "incumbent": {"discovery_rate_discovery_build": rate(d.incumbent[keyed]),
                      "discovery_rate_pooled_build": rate(pdisc.incumbent[keyed_p]),
                      "discovery_rate_2019_on_discovery_build": rate(d.incumbent[keyed & recent]),
                      "discovery_rate_2019_on_pooled_build": rate(pdisc.incumbent[keyed_p & recent]),
                      "confirmation_rate": rate(cconf.incumbent),
                      "confirmation_rate_2019_on": rate(cconf.incumbent[cconf.year >= FIRST_HOT]),
                      "discovery_newcomer_to_incumbent": up, "discovery_incumbent_to_newcomer": down},
        "maturity": {"discovery_topic_years_with_prior_papers": int(len(later)),
                     "mean_delta_log_cum_prior": round(float(delta.mean()), 4),
                     "prior_papers_ratio_geometric_mean": round(float(np.exp(delta.mean())), 4),
                     "topic_years_papers_up": int((mm.papers_p > mm.papers_d).sum())},
    }
    return gates, comp


def earlier_comparison(d: pd.DataFrame, p: pd.DataFrame, conf: set) -> tuple[dict, dict]:
    """Probable earlier versions: discovery build vs pooled build (discovery rows), and the confirmation rows."""
    pdisc = p[~p.submission_id.isin(conf)].reset_index(drop=True)
    pconf = p[p.submission_id.isin(conf)]
    gates = {"discovery_rows_in_discovery_order": bool(pdisc.submission_id.equals(d.submission_id))}
    if not gates["discovery_rows_in_discovery_order"]:
        return gates, {}
    has = d.nn_id.notna()
    same_side = has & ~pdisc.nn_id.isin(conf)                    # pooled neighbour is a discovery paper
    other = has & pdisc.nn_id.isin(conf)
    gates["discovery_rows_with_a_discovery_neighbour_keep_it_and_its_cosine"] = bool(
        (pdisc.nn_id[same_side] == d.nn_id[same_side]).all()
        and ((pdisc.nn_cos[same_side] - d.nn_cos[same_side]).abs() <= COS_TOL).all())
    gates["discovery_rows_with_a_confirmation_neighbour_gain_cosine"] = bool((pdisc.nn_cos[other] >= d.nn_cos[other] - COS_TOL).all())
    gates["discovery_rows_have_a_neighbour_iff_before"] = bool((pdisc.nn_id.notna() == has).all())
    ex = d.exact_title_id.notna()
    gates["discovery_exact_title_matches_kept"] = bool(pdisc.exact_title_id[ex].notna().all() and (
        pdisc.exact_title_id[ex & ~pdisc.exact_title_id.isin(conf)] == d.exact_title_id[ex & ~pdisc.exact_title_id.isin(conf)]).all())
    fd, fp = d.probable_earlier_version.notna(), pdisc.probable_earlier_version.notna()
    gates["no_discovery_paper_loses_its_probable_earlier_version"] = bool(fp[fd].all())
    fc = pconf.probable_earlier_version.notna()
    comp = {"tau": None,
            "discovery_flagged_discovery_build": int(fd.sum()), "discovery_flagged_pooled_build": int(fp.sum()),
            "discovery_flagged_pointing_to_confirmation": int(pdisc.probable_earlier_version[fp].isin(conf).sum()),
            "discovery_flagged_target_changed": int((fd & fp & (pdisc.probable_earlier_version != d.probable_earlier_version)).sum()),
            "discovery_nearest_neighbour_now_confirmation": int(other.sum()),
            "discovery_exact_title_matches": {"discovery_build": int(ex.sum()), "pooled_build": int(pdisc.exact_title_id.notna().sum())},
            "confirmation_flagged": int(fc.sum()),
            "confirmation_flagged_pointing_to_discovery": int((~pconf.probable_earlier_version[fc].isin(conf)).sum()),
            "confirmation_exact_title_matches": int(pconf.exact_title_id.notna().sum()),
            "confirmation_papers_with_earlier_year": int(pconf.nn_id.notna().sum())}
    return gates, comp


def buzzword_comparison(d: pd.DataFrame, p: pd.DataFrame, dkw: pd.DataFrame, pkw: pd.DataFrame, conf: set,
                        vocab: set[str]) -> tuple[dict, dict]:
    """Buzzword flags: discovery build vs pooled build (discovery rows), and the confirmation rows' shares."""
    pdisc = p[~p.submission_id.isin(conf)].reset_index(drop=True)
    pconf = p[p.submission_id.isin(conf)]
    gates = {"discovery_rows_in_discovery_order": bool(pdisc.submission_id.equals(d.submission_id)),
             "keywords_from_the_frozen_vocabulary": set(dkw.keyword) <= set(pkw.keyword) <= vocab}
    if not gates["discovery_rows_in_discovery_order"]:
        return gates, {}
    yr = d.year.between(*BUZZ_YEARS)
    flips = {c: {"off_to_on": int(((d[c] == 0) & (pdisc[c] == 1) & yr).sum()),
                 "on_to_off": int(((d[c] == 1) & (pdisc[c] == 0) & yr).sum())} for c in ("lists_hot", "buzzword")}
    by = lambda kw, c: {int(y): int(v) for y, v in kw[kw[c]].groupby("year").size().items()}
    comp = {"keywords_in_vocabulary_used": {"discovery_build": int(dkw.keyword.nunique()), "pooled_build": int(pkw.keyword.nunique())},
            "eligible_keywords_by_year": {"discovery_build": by(dkw, "eligible"), "pooled_build": by(pkw, "eligible")},
            "hot_keywords_by_year": {"discovery_build": by(dkw, "hot"), "pooled_build": by(pkw, "hot")},
            "discovery_paper_flips_2019_2026": flips,
            "share_2019_2026": {c: {"discovery_build": rate(d[c][yr]), "pooled_build_discovery_rows": rate(pdisc[c][yr]),
                                    "pooled_build_confirmation_rows": rate(pconf[c][pconf.year.between(*BUZZ_YEARS)])}
                                for c in ("lists_hot", "buzzword")},
            "share_with_an_eligible_keyword_2019_2026": {
                "discovery_build": rate((d.n_eligible_keywords > 0)[yr]),
                "pooled_build_confirmation_rows": rate((pconf.n_eligible_keywords > 0)[pconf.year.between(*BUZZ_YEARS)])}}
    return gates, comp


# ---------------------------------------------------------------- frames

def frame_violations(f: pd.DataFrame) -> dict[str, int]:
    """Rows where a frame column is missing although the builders define it (0 everywhere when the build is whole)."""
    text = lambda s: s.astype(object).where(s.notna(), "nan").astype(str)
    none = lambda s: text(s).isin(["nan", "None", ""]) | text(s).str.endswith("_nan")
    early = f.year < FIRST_HOT
    return {"topic": int(none(f.topic).sum()), "topic_early": int(none(f.topic_early).sum()),
            "primary_class": int(f.primary_class.isna().sum()), "primary_type": int(f.primary_type.isna().sum()),
            "maturity": int(f.maturity.isna().sum()), "prior_growth": int((f.prior_growth.isna() != early).sum()),
            "hot": int((f.hot.isna() != early).sum()), "incumbent": int((f.incumbent.isna() != ~f.has_author_key).sum()),
            "buzzword": int((f.buzzword.isna() != ~f.year.between(*BUZZ_YEARS)).sum()),
            "has_earlier_version": int(f.has_earlier_version.isna().sum())}


def frame_checks(split: pd.Series) -> tuple[dict, dict]:
    """panel.frame(m) for every map, split with run_confirmation's mask (the confirmation run's own path)."""
    import panel
    import run_confirmation as rc
    pooled, conf_frames, mask = rc.pooled_frames()
    ids = pooled["k100"].submission_id
    gates = {"mask_equals_topic_layer_split_file": bool((mask == split.reindex(ids).eq("confirmation").to_numpy()).all()),
             "frames_in_pooled_order": bool(ids.equals(split.index.to_series().reset_index(drop=True)))}
    out = {}
    for m in panel.MAPS:
        f, c = pooled[m], conf_frames[m]
        v = frame_violations(f)
        out[m] = {"rows": int(len(f)), "confirmation_rows": int(len(c)), "discovery_rows": int((~mask).sum()),
                  "violations": v, "fm_adoption_missing": {"discovery": int(f.fm_adoption[~mask].isna().sum()),
                                                           "confirmation": int(c.fm_adoption.isna().sum())}}
        gates[f"{m}_rows"] = len(f) == sum(PAPERS.values()) and len(c) == PAPERS["confirmation"]
        gates[f"{m}_no_missing"] = not any(v.values())
    return gates, out


# ---------------------------------------------------------------- report

def frozen_input_gates(tau: float) -> tuple[dict, dict]:
    copies = {n: [DISCOVERY_TOPICS / n, POOLED_TOPICS / n] for n in TOPIC_COPIES}
    copies |= {n: [DISCOVERY_OUTPUT / n, POOLED_OUTPUT / n] for n in COPIES}
    same = {n: sha256(a) == sha256(b) for n, (a, b) in copies.items()}
    manifest = json.loads(MANIFEST.read_text())
    kt = pd.read_csv(POOLED_TOPICS / "keyword_types.csv", keep_default_na=False)
    vocab = int(kt.type.isin({"research_area", "specific_topic"}).sum())
    checks = {n: json.loads((POOLED_OUTPUT / "checks" / f"{n}.json").read_text()) for n in ("resubmissions", "buzzwords")}
    gates = {f"byte_identical_{n}": ok for n, ok in same.items()}
    gates["pooled_author_table_matches_manifest"] = sha256(AUTHORS) == manifest["authors"]["sha256"]
    gates["vocabulary_759"] = vocab == VOCABULARY and checks["buzzwords"]["vocabulary"] == VOCABULARY
    gates["frozen_tau_used"] = checks["resubmissions"]["tau"] == tau
    info = {"frozen_copies_sha256": {n: sha256(b) for n, (_, b) in copies.items()},
            "pooled_author_table": {"sha256": manifest["authors"]["sha256"], "rows": manifest["authors"]["rows"],
                                    "by_split": manifest["authors"]["by_split"]},
            "vocabulary": vocab, "tau": tau,
            "pooled_topic_layer_sha256": {f.name: sha256(f) for f in sorted(POOLED_TOPICS.glob("*.csv.gz"))}}
    return gates, info


def build_report(tau: float, steps: list[dict], untouched: dict) -> dict:
    split = pd.read_csv(POOLED_TOPICS / "split.csv.gz").set_index("submission_id").split
    conf = set(split.index[split == "confirmation"])
    gates: dict[str, dict] = {"untouched": untouched["gates"]}
    gates["frozen_inputs"], inputs = frozen_input_gates(tau)
    D, P = tables(DISCOVERY_OUTPUT, DISCOVERY_TOPICS), tables(POOLED_OUTPUT, POOLED_TOPICS)
    order = split.index.to_series().reset_index(drop=True)
    shape = {"papers": int(len(split)), "by_split": {k: int(v) for k, v in split.value_counts().items()},
             "pooled_files_in_P_order": {}}
    for name, t in (("earlier_versions", P["ev"]), ("paper_buzzword", P["buzz"]), ("topic_assignments", P["fine"])):
        shape["pooled_files_in_P_order"][name] = bool(t.submission_id.reset_index(drop=True).equals(order))
    names = list(P["var"]["map"].drop_duplicates())
    for m in names:
        shape["pooled_files_in_P_order"][f"paper_variables:{m}"] = bool(
            P["var"].submission_id[P["var"]["map"] == m].reset_index(drop=True).equals(order))
    years = sorted(P["fine"].year.unique())
    shape["topic_year_rows"] = {m: int((P["mat"]["map"] == m).sum()) for m in names}
    gates["shape"] = {"papers_by_split": shape["by_split"] == PAPERS,
                      "maps": names == list(D["var"]["map"].drop_duplicates()) and len(names) == 8,
                      "every_file_in_P_order": all(shape["pooled_files_in_P_order"].values()),
                      "topic_year_rows_complete": all(P["mat"][P["mat"]["map"] == m].groupby("topic").size().eq(len(years)).all()
                                                      for m in names)}
    lab = pd.read_csv(POOLED_TOPICS / "paper_contributions.csv.gz", usecols=["submission_id", *LABELS])
    gates["labels"] = {"in_P_order": bool(lab.submission_id.equals(order)),
                       "no_missing_label": int(lab[LABELS].isna().sum().sum()) == 0}
    gates["frames"], frames = frame_checks(split)

    comps, gates["maps"] = {}, {}
    for m in names:
        g, c = map_comparison(m, D["var"][D["var"]["map"] == m], P["var"][P["var"]["map"] == m],
                              D["mat"][D["mat"]["map"] == m], P["mat"][P["mat"]["map"] == m], conf)
        gates["maps"] |= {f"{m}:{k}": v for k, v in g.items()}
        comps[m] = c
    gates["earlier_versions"], ev = earlier_comparison(D["ev"], P["ev"], conf)
    ev["tau"] = tau
    kt = pd.read_csv(POOLED_TOPICS / "keyword_types.csv", keep_default_na=False)
    gates["buzzwords"], buzz = buzzword_comparison(D["buzz"], P["buzz"], D["kw"], P["kw"], conf,
                                                   set(kt.keyword[kt.type.isin({"research_area", "specific_topic"})]))

    authors = load_authors(split.index.to_series())               # pooled DATA: the git-ignored union table
    team = authors.groupby("submission_id").key.nunique()
    keys = {s: set(authors.key[authors.submission_id.isin(set(split.index[split == s]))]) for s in PAPERS}
    authors_info = {"papers_with_author_key_share": {s: rate(pd.Series(split.index[split == s]).isin(team.index).astype(float))
                                                     for s in PAPERS},
                    "mean_team_size_keyed": {s: round(float(team.reindex(split.index[split == s]).dropna().mean()), 3)
                                             for s in PAPERS},
                    "distinct_author_keys": {s: len(k) for s, k in keys.items()},
                    "distinct_author_keys_in_both_splits": len(keys["discovery"] & keys["confirmation"])}

    outputs = {}
    for name in WRITTEN:
        f = POOLED_OUTPUT / name
        outputs[rel(f)] = {"sha256": sha256(f), **({"rows": int(len(pd.read_csv(f)))} if f.suffixes[-2:] == [".csv", ".gz"] else {})}
    flat = {f"{group}:{k}": bool(v) for group, g in gates.items() for k, v in g.items()}
    return {"what": "pooled fashion features (POOLED_SPEC D5; PREREGISTRATION.md D2, D3, D14, D15), built with the "
                    "unchanged builders under ICLR_CORPUS=pooled; outcome-free",
            "passed": all(flat.values()), "failed_gates": sorted(k for k, v in flat.items() if not v),
            "built": {"utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "steps": steps,
                      "git_head": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip(),
                      "python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__,
                      "stdout": rel(LOG)},
            "corpus": {**shape, "years": [int(y) for y in years]},
            "inputs": inputs, "outputs": outputs, "frames": frames, "authors": authors_info,
            "comparisons": {"predicted": PREDICTED, "by_map": comps, "earlier_versions": ev, "buzzwords": buzz},
            "untouched": untouched["info"], "gates": gates}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check-only", action="store_true", help="run no builder; check the built files and rewrite the report")
    a = p.parse_args()
    if common.CORPUS != "pooled" or common.OUTPUT != POOLED_OUTPUT or POOLED_OUTPUT == DISCOVERY_OUTPUT:
        raise SystemExit("build_pooled.py needs ICLR_CORPUS=pooled from the start of the process")
    tau = json.loads((DISCOVERY_OUTPUT / "resubmission_tau.json").read_text())["tau"]
    files = guarded()
    before, status_before = snapshot(files), git_status()
    freeze = json.loads(FREEZE_DISCOVERY.read_text())["sha256"]
    steps = [] if a.check_only else run_builders(tau)
    after, status_after = snapshot(sorted(set(files) | set(guarded()))), git_status()
    diff = changed(before, after)
    untouched = {"gates": {"guarded_files_unchanged": not diff, "git_status_unchanged": status_before == status_after,
                           "discovery_outputs_clean_in_git": not any(line[3:].startswith(("research/fashion/output/", "research/topics/output/"))
                                                                     for line in status_after.splitlines())},
                 "info": {"guarded_files": len(after), "changed": diff, "git_status_lines": len(status_after.splitlines()),
                          "check_only": a.check_only,
                          "freeze_listed_files_differing_from_FREEZE_json": sorted(k for k, h in freeze.items()
                                                                                    if after.get(k) != h)}}
    report = build_report(tau, steps, untouched)
    REPORT.write_text(json.dumps(report, indent=2, default=int) + "\n")
    print(json.dumps({"passed": report["passed"], "failed_gates": report["failed_gates"],
                      "frames": {m: [f["rows"], f["confirmation_rows"]] for m, f in report["frames"].items()}}, indent=1))
    if not report["passed"]:
        raise SystemExit(f"gates failed: {report['failed_gates']} (see {rel(REPORT)})")


if __name__ == "__main__":
    main()
