"""PH7 titles (post hoc; declared in PREREGISTRATION.md on 2026-11-04 before it was run; it uses the PH5 entry point,
`ICLR_CORPUS=pooled python research/fashion/posthoc.py ph5 titles`): do branded titles, a short coined name and a
colon ("NAME: what it does"), go with higher acceptance? Branded titles are the plainest imitation-like spread in the
corpus (their share rose about fourfold, 2017-2026); the question is whether the gate rewards the spread form.
Exploratory association, not an effect of choosing a title.

Branded title (outcome-free; definitions frozen from the paper's Appendix G and title_share.py):
  prefix      the text before the title's first colon, 1-3 whitespace tokens, and a non-empty subtitle
  D1 broad    any such prefix
  D2 name     D1, every prefix token starts with an upper-case letter or a digit, the first token is not a GENERIC
              lead word (primary definition)
  D3 coined   exactly one token with >= 2 capitals, or a digit and >= 1 capital (BERT, LoRA, Llama-2)
  D4 onetoken D2 with exactly one token
Acceptance (gated): per split (discovery; confirmation = the released held-out papers), RQ3 decided papers 2018-2026.
  controls    accepted ~ branded + class dummies (ref. method) + fm + log2 team | k100 topic x year FE (ols.fe_ols),
              CR1 SE by topic, t(G - 1)                                                        (primary model)
  raw         accepted ~ branded | year FE, CR1 by topic (the scale of the earlier exploratory ratio)
  timing      controls model with branded x 1[2023-2026] (descriptive): does any premium change as the form spreads?
Declared test (held-out = confirmation split, D2, controls model): premium > 0, one-sided p < 0.05 -> supported
(rewarded imitation of form). Otherwise: 90% CI inside [-2, +2] pp -> "no premium of 2 pp or more" (SESOI as D12 for
H2a/H3c); else not supported, uninformative if |coef| < MDE80 = 2.486 SE. Discovery estimates are reported but are not
a test: an earlier exploratory analysis (disclosed before registration) had seen title style against acceptance on the
discovery papers (ratio 1.02).
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

import ols
import posthoc
from common import topic_layer

YEARS, LATE = (2018, 2026), (2023, 2026)
SPLITS = ("discovery", "confirmation")
DEFINITIONS = ("D2", "D1", "D3", "D4")
PRIMARY, SESOI = "D2", 0.02
MDE_FACTOR = stats.norm.ppf(0.95) + stats.norm.ppf(0.80)
CLASS_CONTROLS = ["cls_theory", "cls_empirical", "cls_dataset_benchmark", "cls_evaluation", "cls_other"]
GENERIC = {w.lower() for w in """Towards Toward Beyond Rethinking Revisiting On When Why How What Is Are Do Does Can
Learning Understanding Improving Scaling Not Less More Making Training Exploring Investigating Analyzing Analysing
Demystifying Unveiling Enhancing Bridging Boosting Unlocking Unleashing Mitigating Measuring Evaluating Benchmarking
Position Case Lessons Back A An The Deep Neural Efficient Robust Simple Generalization Representation""".split()}
PREFIX = re.compile(r"^([^:]+?)\s*:\s*(\S.*)$")
TOKEN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9\-\+\.'²³]*$")


def _tokens(title: str) -> list[str] | None:
    m = PREFIX.match(title)
    if not m:
        return None
    toks = m.group(1).split()
    return toks if 1 <= len(toks) <= 3 else None


def d1(t: str) -> bool:
    return _tokens(t) is not None


def d2(t: str) -> bool:
    toks = _tokens(t)
    if toks is None or toks[0].strip("\"'`").lower() in GENERIC:
        return False
    return all(re.match(r"^[\(\[\"'`$\\]*[A-Z0-9]", x) for x in toks)


def d3(t: str) -> bool:
    toks = _tokens(t)
    if toks is None or len(toks) != 1 or not TOKEN.match(toks[0]):
        return False
    caps = sum(c.isupper() for c in toks[0])
    return caps >= 2 or (any(c.isdigit() for c in toks[0]) and caps >= 1)


def d4(t: str) -> bool:
    toks = _tokens(t)
    return toks is not None and len(toks) == 1 and d2(t)


RULES = {"D1": d1, "D2": d2, "D3": d3, "D4": d4}


def branded(ids: pd.Series) -> pd.DataFrame:
    """Outcome-free: the four branded-title flags and the split for the papers in ids (corpus titles)."""
    c = topic_layer().embedded_corpus().set_index("submission_id")
    titles = c.title.reindex(ids.to_numpy()).fillna("").str.replace(r"\s+", " ", regex=True).str.strip()
    out = pd.DataFrame({"submission_id": ids.to_numpy()})
    for name, rule in RULES.items():
        out[name] = [float(rule(t)) for t in titles]
    out["split"] = (c.split.reindex(ids.to_numpy()).to_numpy() if "split" in c else "discovery")
    return out


def _row(r: pd.DataFrame, term: str, **meta) -> dict:
    coef, se, G = float(r.loc[term, "coef"]), float(r.loc[term, "se"]), int(r.loc[term, "clusters"])
    dof = G - 1
    q95, q90 = stats.t.ppf(0.975, dof), stats.t.ppf(0.95, dof)
    return {**meta, "term": term, "coef": coef, "se": se, "ci95_lo": coef - q95 * se, "ci95_hi": coef + q95 * se,
            "ci90_lo": coef - q90 * se, "ci90_hi": coef + q90 * se, "p_two_sided": float(r.loc[term, "p"]),
            "p_greater": float(stats.t.sf(coef / se, dof)), "mde80": MDE_FACTOR * se,
            "n": int(r.loc[term, "n"]), "clusters": G}


def shares(k: pd.DataFrame, flags: pd.DataFrame) -> pd.DataFrame:
    """Outcome-free: branded share by split and year, all submissions."""
    d = flags.assign(year=k.year.to_numpy())
    return (d.groupby(["split", "year"])[list(RULES)].mean().mul(100).round(2)
            .join(d.groupby(["split", "year"]).size().rename("papers")).reset_index())


def compute(k: pd.DataFrame) -> dict:
    k = posthoc.add_columns(k.reset_index(drop=True).copy())
    flags = branded(k.submission_id)
    for name in RULES:
        k[name] = flags[name].to_numpy()
    k["split"] = flags.split.to_numpy()
    k["late"] = k.year.between(*LATE).astype(float)
    rows, rates = [], []
    for s in SPLITS:
        d = k[k.rq3.astype(bool) & k.year.between(*YEARS) & (k.split == s)]
        if len(d) == 0:
            continue
        y = d.accepted.astype(float)
        for name in DEFINITIONS:
            X = d[[name] + CLASS_CONTROLS + ["fm", "log2_team"]].astype(float)
            rows.append(_row(ols.fe_ols(y, X, d.cell, d.topic), name, split=s, definition=name, model="controls"))
            rows.append(_row(ols.fe_ols(y, d[[name]].astype(float), d.year, d.topic), name, split=s,
                             definition=name, model="raw"))
            Xt = X.assign(**{f"{name}_x_late": d[name] * d.late})
            rt = ols.fe_ols(y, Xt, d.cell, d.topic)
            rows.append(_row(rt, f"{name}_x_late", split=s, definition=name, model="timing (x 2023-2026)"))
            for flag in (1.0, 0.0):
                sub = d[d[name] == flag]
                rates.append({"split": s, "definition": name, "branded": int(flag), "decided_papers": len(sub),
                              "acceptance_rate": float(sub.accepted.mean())})
    tests = pd.DataFrame(rows)
    rates = pd.DataFrame(rates)
    settings = {"years": list(YEARS), "late": list(LATE), "primary_definition": PRIMARY, "sesoi_pp": 100 * SESOI,
                "declared_test": "confirmation, D2, controls model: coef > 0, one-sided p < 0.05; else 90% CI inside "
                                 "+-2 pp -> no premium of 2 pp or more; else not supported (uninformative if "
                                 "|coef| < MDE80)",
                "note": "post hoc (declared before the run); associations, not effects of title choice"}
    held = tests[(tests.split == "confirmation") & (tests.definition == PRIMARY) & (tests.model == "controls")]
    if len(held):
        h = held.iloc[0]
        if h.coef > 0 and h.p_greater < 0.05:
            verdict = "supported (premium)"
        elif -SESOI < h.ci90_lo and h.ci90_hi < SESOI:
            verdict = "not supported; no premium of 2 pp or more (90% CI inside +-2 pp)"
        else:
            verdict = ("not supported (uninformative: |coef| < MDE80)" if abs(h.coef) < h.mde80
                       else "not supported")
        settings["held_out_verdict"] = verdict
    return {"tests": tests, "rates": rates, "shares": shares(k, flags), "settings": settings}


def plot(out_dir: Path) -> None:
    """Premium by definition, model and split, from the saved outputs only."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    t = pd.read_csv(out_dir / "tests.csv")
    t = t[t.model.isin(["controls", "raw"])]
    labels = [f"{d} {m}" for d in DEFINITIONS for m in ("controls", "raw")]
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    for off, (s, colour) in zip((-0.15, 0.15), [("discovery", "#2a78d6"), ("confirmation", "#eb6834")]):
        part = t[t.split == s].set_index(["definition", "model"])
        if part.empty:
            continue
        ys, xs, lo, hi = [], [], [], []
        for i, lab in enumerate(labels):
            dname, m = lab.split(" ")
            if (dname, m) in part.index:
                r = part.loc[(dname, m)]
                ys.append(i + off), xs.append(100 * r.coef), lo.append(100 * (r.coef - r.ci95_lo))
                hi.append(100 * (r.ci95_hi - r.coef))
        ax.errorbar(xs, ys, xerr=[lo, hi], fmt="o", ms=4, color=colour, lw=1, label=s)
    ax.axvline(0, color="#888", lw=0.8)
    ax.axvspan(-100 * SESOI, 100 * SESOI, color="#eee", zorder=0)
    ax.set_yticks(range(len(labels)), labels)
    ax.invert_yaxis()
    ax.set_xlabel("Branded minus other titles, acceptance (pp), 95% CI")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "ph7_titles.png", dpi=150)
    plt.close(fig)
