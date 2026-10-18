"""The single confirmatory run on the released confirmation papers (PREREGISTRATION.md "Confirmation", D14, the post-run
registrations of 2026-10-15 and 2026-10-17; POOLED_SPEC D6). Run once, after FREEZE_CONFIRMATION.json is committed:

    python research/fashion/run_confirmation.py [--rerun-reason R]
    python research/fashion/run_confirmation.py --simulate SEED [--mde-reps N]     (before the freeze: plumbing and MDE)

The script switches itself to the pooled corpus (ICLR_CORPUS=pooled, common.py) and refuses any other setting.
Status: a pre-registered out-of-sample replication on the released former-holdout papers, not an untouched independent
holdout (data_confirmation_csv/LOCAL_WORKAROUND.md).

Features (D14): every variable is built on discovery + confirmation with the frozen code (pooled history, frozen
centring mean, τ, keyword list); panel.frame(m) is built on the pooled corpus for every map and only then filtered to
the confirmation papers (one mask for all maps; split from the pooled topic layer, checked against the embedding id
lists). Outcomes come from outcomes.load("real"), which serves run_confirmation.py the confirmation table only.

Registered tests (REGISTERED; the frozen models, variants and decision rule, with a one-sided p):
  H1d    model ~ fm_adoption: rq1_rise.fit (topic + year FE, CR1 by topic, t(G-1)), 2018-2026     < 0   {H1d}
  H2b'   method ~ newcomer: rq2 H2b's model (topic x year), wild cluster bootstrap p (FREEZE remedy)  > 0   {H2b', H2c'}
  H2c'   measurement ~ newcomer: rq2 H2c's model, wild cluster bootstrap p                         < 0
  H3a    accepted ~ maturity: rq3 H3a's model (class + FM controls, topic + year FE), CR1          < 0   {H3a}
  H4-FL  primary: PH4 level of 'federated learning' (posthoc.ph4_set; t(m-1))                      < 0   {H4-FL}
         secondary: PH4 trend (t(m-2)), only if m >= 4 years with >= 10 FL papers, else 'not estimable'
H2b' and H2c' reverse the discovery predictions (new hypotheses). H2a and H3b come out of the unchanged rq2/rq3 run()
and are labelled 'not registered for confirmation'.
One-sided p: p1 = p / 2 if the estimate has the predicted sign, else 1 - p / 2, where p is the main specification's
two-sided p of the discovery method. Holm on p1 within each family. Supported = predicted sign, Holm p1 < 0.05, >= 75%
of counted variants with the predicted sign and both hindsight variants (analysis.decide, unchanged; H4-FL has no
variants). A wrong-sign estimate has p1 >= 0.5, so 'significant in the opposite direction' cannot occur. Reported with
each verdict: the two-sided p, TOST at the discovery SESOI (none for H1d and H4-FL), the fragile flag, the S11 qualifier
(S11 p made one-sided the same way, Holm in the family), and for H2b'/H2c' the stress sensitivity (t / dry-run v3
inflation, one-sided) and the exact one-sided share of bootstrap t* beyond t (same draws; sensitivity only).
Label reliability (D11) next to H2b'/H2c': the second-pass agreement and kappa of the confirmation papers' own 5%
second pass (method and measurement indicators, main class); rq2's block (pooled second pass, S8 discovery reference
rates) is reported alongside, labelled.
PH5: ph5_part() is the hook for the PH5 confirmation module (ph5_confirm.compute; its registration ph5_confirm.REGISTERED
is pinned in FREEZE_CONFIRMATION.json as registered_ph5). --without-ph5 is for --simulate only: the real run refuses it
(and refuses to start without ph5_confirm.py), logs with_ph5, and only a finished attempt WITH PH5 opens the pooled
gates (outcomes.confirmation_finished), so the registered PH5 tests run in the attempt that unlocks pooled results.

Real run: refuses before anything is verified if output_pooled/confirmation_run/attempts.jsonl holds an attempt and no
--rerun-reason is given, and refuses any attempt (a rerun included) once a pooled read of confirmation outcomes may have
happened or pooled labels were crossed (POOLED_READS: output_pooled/frozen_run/attempts.jsonl,
output_pooled/posthoc/access_log.jsonl, output_pooled/rq1_results.csv or output_pooled/figures exists); then
outcomes.require_frozen (entry, corpus, every FREEZE_CONFIRMATION.json hash, clean tree); the attempt is logged before
any real data is touched, and a failure records its traceback. Writes
output_pooled/confirmation_run/{h1d,rq2_rows,rq3_rows,h4fl,h4fl_cells}.csv, summary.json, run_info.json, stdout.txt
(and ph5/); commit them immediately.
--simulate SEED: no guard and no real outcome. The RQ1/RQ2 outcome-side labels are simulated (variance components
calibrated on the discovery rows only, as dryrun.py; newcomer follows the simulated incumbency) and acceptance comes
from outcomes.load("simulated"); writes output_pooled/confirmation_dryrun/ (cleared first). --mde-reps N adds the
detection rate of every registered test over a grid of planted effects and its MDE80 (mde.json).
"""
from __future__ import annotations

import os

if __name__ == "__main__":                           # the corpus switch precedes every fashion import (common.py, D1)
    if (os.environ.get("ICLR_CORPUS") or "pooled") != "pooled":
        raise SystemExit("run_confirmation.py runs on the pooled corpus: unset ICLR_CORPUS or set it to 'pooled'")
    os.environ["ICLR_CORPUS"] = "pooled"

import argparse  # noqa: E402
import importlib  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import platform  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402
import traceback  # noqa: E402
from dataclasses import replace  # noqa: E402
from pathlib import Path  # noqa: E402
from typing import Callable  # noqa: E402

import matplotlib  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import scipy  # noqa: E402
from scipy import stats  # noqa: E402

import common  # noqa: E402
import outcomes  # noqa: E402
import panel  # noqa: E402
import posthoc  # noqa: E402
import rq1_rise  # noqa: E402
import rq2_following as rq2  # noqa: E402
import rq3_reward as rq3  # noqa: E402
import run_frozen  # noqa: E402
import variants  # noqa: E402
from analysis import ALPHA, BOOT_DRAWS, BOOT_SEED, Spec, apply_bootstrap, decide, fit, wild_cluster_bootstrap_p  # noqa: E402
from common import DISCOVERY_OUTPUT, POOLED_OUTPUT, ROOT, topic_layer  # noqa: E402
from dgp import DGP, calibrate, simulate  # noqa: E402
from variants import holm  # noqa: E402

OUT = POOLED_OUTPUT / "confirmation_run"
DRY = POOLED_OUTPUT / "confirmation_dryrun"
POOLED_READS = (POOLED_OUTPUT / "frozen_run" / "attempts.jsonl",      # run_pooled.py (pooled RQ2/RQ3/E1-E10)
                POOLED_OUTPUT / "posthoc" / "access_log.jsonl",       # pooled post hoc (PH1-PH5)
                POOLED_OUTPUT / "rq1_results.csv",                    # pooled RQ1 (H1d's labels x regressor)
                POOLED_OUTPUT / "figures")                            # pooled figures (F2: labels by year)
FL = posthoc.FL_KEYWORD
_RQ2 = {s.hid: s for s in rq2.SPECS}
H1D = Spec("H1d", "model", "fm_adoption", -1, np.nan, "topic+year", rq1_rise.YEARS,
           note="the RQ1 model (rq1_rise.fit); RQ1 registered no SESOI, so no TOST or equivalence label")
SPECS2 = [replace(_RQ2["H2b"], hid="H2b'", sign=+1, note="new hypothesis: reverses the discovery prediction of H2b"),
          replace(_RQ2["H2c"], hid="H2c'", sign=-1, note="new hypothesis: reverses the discovery prediction of H2c")]
SPECS3 = [next(s for s in rq3.SPECS if s.hid == "H3a")]
SOURCE = {"H1d": "H1d", "H2b'": "H2b", "H2c'": "H2c", "H3a": "H3a"}      # registered test -> discovery model it reuses
SIGN = {"H1d": -1, "H2b'": +1, "H2c'": -1, "H3a": -1, "H4-FL": -1}
FAMILIES = {"rq1": ["H1d"], "rq2": ["H2b'", "H2c'"], "rq3": ["H3a"], "h4fl": ["H4-FL"]}
ONE_SIDED = "one-sided: p / 2 if the estimate has the predicted sign, else 1 - p / 2 (p: the two-sided p of the discovery method)"
NOT_REGISTERED = "not registered for confirmation"
STATUS = ("pre-registered out-of-sample replication on the released former-holdout papers (not an untouched "
          "independent holdout)")
REGISTERED = {
    "status": STATUS,
    "population": "confirmation papers with text; features built on discovery + confirmation with the frozen code, "
                  "frames filtered to the confirmation papers after construction (D14)",
    "hypotheses": {
        "H1d": {"model": "model ~ fm_adoption | topic + year FE (rq1_rise.fit), 2018-2026", "sign": -1,
                "p": "CR1 by topic, t(G-1)", "variants": "variants.SHARED"},
        "H2b'": {"model": "method ~ newcomer | topic x year FE (rq2 H2b), 2019-2026", "sign": 1,
                 "p": "wild cluster restricted bootstrap (FREEZE remedy bootstrap:H2b)", "variants": "variants.RQ2",
                 "note": "new hypothesis, reverses discovery's H2b"},
        "H2c'": {"model": "measurement ~ newcomer | topic x year FE (rq2 H2c), 2019-2026", "sign": -1,
                 "p": "wild cluster restricted bootstrap (FREEZE remedy bootstrap:H2c)", "variants": "variants.RQ2",
                 "note": "new hypothesis, reverses discovery's H2c"},
        "H3a": {"model": "accepted ~ maturity + class + fm | topic + year FE (rq3 H3a), 2018-2026, RQ3 population",
                "sign": -1, "p": "CR1 by topic, t(G-1)", "variants": "variants.RQ3"},
        "H4-FL": {"model": "PH4 level: paper-weighted mean yearly gap in acceptance, papers listing 'federated "
                           "learning' minus all other papers of the year (posthoc.ph4_set), 2018-2026, RQ3 population",
                  "sign": -1, "p": "t(m-1), m = years with >= 10 FL papers", "variants": "none",
                  "secondary": "PH4 trend (pp per year), one-sided, only if m >= 4; otherwise not estimable"},
    },
    "families": FAMILIES,
    "one_sided_rule": ONE_SIDED + "; Holm on p1 within each family; alpha 0.05",
    "decision_rule": "supported = predicted sign, Holm p1 < 0.05, >= 75% of counted variants with the predicted sign and "
                     "both hindsight variants (analysis.decide); H4-FL: predicted sign and p1 < 0.05",
    "fl_rule": "member = 'federated learning' in the paper's pooled normalised keyword list (posthoc.ph4_members; "
               "confirmation papers: keyword_map.normalize of the raw author keywords)",
    "sensitivities": ["S11 two-way clustering, p made one-sided, Holm in the family (qualifier only)",
                      "stress: CR1 t / dry-run v3 inflation, one-sided (H2b', H2c')",
                      "exact one-sided share of wild bootstrap t* beyond t, same draws (H2b', H2c')"],
    "not_registered": ["H2a", "H3b"],
    "reporting": {"h1d_ci": "t(G-1) quantiles, as RQ2/RQ3 (the discovery rq1_rise summary printed coef +- 1.96 SE); the "
                            "p is fe_ols's t(G-1) p in both",
                  "label_reliability": "second-pass agreement and kappa (method, measurement, main class) of the "
                                       "confirmation papers' own second pass; rq2's pooled block and S8 discovery "
                                       "reference rates alongside",
                  "underpowered_at_3x_sesoi": "None (not applicable) for hypotheses without a SESOI (H1d, H4-FL)",
                  "pooled_gates": "pooled runs, pooled post hoc, pooled RQ1 and pooled figures need a finished "
                                  "confirmation attempt with PH5 (outcomes.confirmation_finished); no confirmation "
                                  "attempt once output_pooled/frozen_run or output_pooled/posthoc has read outcomes "
                                  "or pooled RQ1 / figures exist"},
}
RQ3_DGP_HI = DGP(base=0.32, sd_topic=0.05, sd_year=0.03, sd_cell=0.04, sd_trend=0.016)   # = dryrun.RQ3_DGP["hi"]
MULTS = (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0)                                                # = dryrun.MULTS
GRID = {"H1d": (0.02, 0.04, 0.06, 0.08, 0.12, 0.16, 0.24),            # pp per unit of fm_adoption (no SESOI)
        "H2b'": tuple(round(0.02 * m, 4) for m in MULTS), "H2c'": tuple(round(0.01 * m, 4) for m in MULTS),
        "H3a": tuple(round(0.01 * m, 4) for m in MULTS),
        "H4-FL": (0.02, 0.04, 0.06, 0.08, 0.12, 0.16, 0.24)}           # acceptance gap of an FL paper
CORE = {"coef", "se", "p", "dof", "n", "clusters", "ci95_lo", "ci95_hi", "ci90_lo", "ci90_hi"}


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit(message)


def one_sided(p: float, coef: float, sign: int) -> float:
    """p1 = p / 2 if the estimate has the predicted sign, else 1 - p / 2; missing stays missing (Holm counts it as 1)."""
    if not (np.isfinite(p) and np.isfinite(coef)):
        return np.nan
    return float(p / 2 if np.sign(coef) == sign else 1 - p / 2)


def one_sided_main(m: dict, spec: Spec) -> dict:
    """The main estimate with p replaced by its one-sided p (decide then applies Holm to it)."""
    return {**m, "p": one_sided(m["p"], m["coef"], spec.sign), "p_two_sided": m["p"], "p_cr1": m.get("p_cr1", m["p"])}


def check_corpus() -> None:
    """The run's features must be the pooled ones (D14), and nothing may be written into the discovery outputs."""
    need(common.CORPUS == "pooled" and panel.OUTPUT == POOLED_OUTPUT and panel.TOPICS == common.TOPICS,
         "run_confirmation.py needs ICLR_CORPUS=pooled from the start of the process")
    for p in (OUT, DRY, posthoc.OUT):
        need(POOLED_OUTPUT in p.parents and DISCOVERY_OUTPUT not in p.parents, f"{p} is not under {POOLED_OUTPUT}")


# ---------------------------------------------------------------- frames (D14: build on the pooled corpus, then filter)

def split_mask(ids: pd.Series, corpus: pd.DataFrame, released: pd.Series, discovery: pd.Series) -> np.ndarray:
    """Confirmation rows of the pooled frames, from the pooled corpus's split column; the pooled order must be the
    corpus order, the confirmation ids the released embedding ids and the discovery rows the discovery order."""
    need(corpus.submission_id.reset_index(drop=True).equals(ids.reset_index(drop=True)),
         "the pooled frames are not in the pooled corpus order")
    need(corpus.split.isin(["discovery", "confirmation"]).all(), "unknown split in the pooled corpus")
    conf = corpus.split.eq("confirmation").to_numpy()
    need(not set(released) & set(discovery), "the released and discovery embeddings share papers")
    need(set(ids[conf]) == set(released), "the confirmation papers are not the released embedded papers")
    need(ids[~conf].reset_index(drop=True).equals(discovery.reset_index(drop=True)),
         "the discovery rows of the pooled order are not the discovery order")
    return conf


def confirmation_mask(k100: pd.DataFrame) -> np.ndarray:
    tl = topic_layer()
    corpus = tl.embedded_corpus()
    need("split" in corpus, "the topic layer has no split column: the pooled corpus is not active")
    return split_mask(k100.submission_id, corpus, pd.read_csv(tl.CACHE / "specter2_released_ids.csv").submission_id,
                      pd.read_csv(tl.CACHE / "specter2_ids.csv").submission_id)


def split_frames(pooled: dict[str, pd.DataFrame], mask: np.ndarray) -> dict[str, pd.DataFrame]:
    """Every map's frame filtered by one mask after construction (pooled history kept; rows stay aligned across maps,
    as rq3.attach requires)."""
    ids = pooled["k100"].submission_id.to_numpy()
    for m, f in pooled.items():
        need(len(f) == len(ids) and (f.submission_id.to_numpy() == ids).all(), f"map {m} is not in the k100 row order")
    return {m: f[mask].reset_index(drop=True) for m, f in pooled.items()}


def pooled_frames() -> tuple[dict[str, pd.DataFrame], dict[str, pd.DataFrame], np.ndarray]:
    pooled = {m: panel.frame(m) for m in panel.MAPS}
    mask = confirmation_mask(pooled["k100"])
    return pooled, split_frames(pooled, mask), mask


# ---------------------------------------------------------------- registered tests

MISSING = {"coef": np.nan, "se": np.nan, "p": np.nan, "dof": np.nan, "n": 0, "clusters": 0, "ci95_lo": np.nan,
           "ci95_hi": np.nan, "ci90_lo": np.nan, "ci90_hi": np.nan}


def estimate_rq1(d: pd.DataFrame, y: str = "model", x: str = "fm_adoption") -> dict:
    """rq1_rise.fit (topic + year FE, CR1 by topic, t(G - 1)) as an analysis.estimate-style dict. An estimate that cannot
    be made is missing, which decide counts as the wrong sign (D9)."""
    try:
        r = rq1_rise.fit(d, y, x)
    except (ValueError, IndexError, ZeroDivisionError, np.linalg.LinAlgError) as e:
        return {**MISSING, "note": f"not estimable: {e}"}
    coef, se, G = float(r.coef), float(r.se), int(r.clusters)
    if not (np.isfinite(coef) and np.isfinite(se)) or G < 2:
        return {**MISSING, "n": int(r.n), "clusters": G, "note": "no variation"}
    dof = G - 1
    q95, q90 = stats.t.ppf(0.975, dof), stats.t.ppf(0.95, dof)
    return {"coef": coef, "se": se, "p": float(r.p), "dof": dof, "n": int(r.n), "clusters": G, "ci95_lo": coef - q95 * se,
            "ci95_hi": coef + q95 * se, "ci90_lo": coef - q90 * se, "ci90_hi": coef + q90 * se, "note": ""}


def h1d(frames: dict[str, pd.DataFrame], model: pd.Series | None = None) -> tuple[dict, pd.DataFrame]:
    """H1d: main (k100) and every counted RQ1 variant (variants.SHARED; without_2026 is RQ1's years_2018_2025).
    model = simulated labels by submission_id (--simulate), else the real label."""
    def data(v: variants.Variant) -> pd.DataFrame:
        d = variants.apply(frames[v.map], v)
        return d if model is None else d.assign(model=model.reindex(d.submission_id).to_numpy())
    main = estimate_rq1(data(variants.MAIN))
    counted = {name: estimate_rq1(data(v)) for name, v in variants.SHARED.items()}
    rows = [{"hypothesis": "H1d", "variant": "main", "kind": "main", "map": "k100", **main}]
    rows += [{"hypothesis": "H1d", "variant": n, "kind": "counted", "map": variants.SHARED[n].map, **r} for n, r in counted.items()]
    v = decide([H1D], {"H1d": one_sided_main(main, H1D)}, {"H1d": counted}, {})
    v["H1d"].update(p_two_sided=main["p"], sidedness=ONE_SIDED, discovery_counterpart="H1d", note=H1D.note)
    return v, pd.DataFrame(rows)


def records(rows: pd.DataFrame, h: str, kind: str) -> dict[str, dict]:
    """Estimates of one hypothesis and kind from an rq2/rq3 rows table, by variant (optional keys that are missing
    in a row are dropped, so decide sees what the estimate dict had)."""
    sub = rows[(rows.hypothesis == h) & (rows.kind == kind)]
    return {r["variant"]: {k: v for k, v in r.items() if k in CORE or not (isinstance(v, float) and np.isnan(v))}
            for r in sub.to_dict("records")}


def redecide(rows: pd.DataFrame, specs: list[Spec]) -> dict:
    """Verdicts of registered confirmation hypotheses from the rows of an unchanged rq2/rq3 run: the main estimate's
    two-sided p becomes one-sided for the registered sign, then analysis.decide over this family only (Holm, 75% and
    hindsight rules, D12 labels, TOST, fragile flag), as frozen."""
    main = {s.hid: one_sided_main(records(rows, SOURCE[s.hid], "main")["main"], s) for s in specs}
    counted = {s.hid: records(rows, SOURCE[s.hid], "counted") for s in specs}
    supp = {s.hid: records(rows, SOURCE[s.hid], "supplementary") for s in specs}
    v = decide(specs, main, counted, supp)
    for s in specs:
        v[s.hid].update(p_two_sided=main[s.hid]["p_two_sided"], sidedness=ONE_SIDED, discovery_counterpart=SOURCE[s.hid],
                        note=s.note)
    return v


def label_rows(rows: pd.DataFrame) -> pd.DataFrame:
    """rq2/rq3 rows with the registered hypothesis each belongs to (H2a, H3b: not registered for confirmation)."""
    reg = {src: h for h, src in SOURCE.items()}
    return rows.assign(confirmation_hypothesis=rows.hypothesis.map(reg).fillna(NOT_REGISTERED))


def s11_one_sided(rows: pd.DataFrame, specs: list[Spec]) -> dict:
    """S11 (two-way clustering) per registered hypothesis, its p made one-sided for the registered sign."""
    s11 = run_frozen.s11_of(rows)
    return {s.hid: {**s11[SOURCE[s.hid]], "p_two_sided": s11[SOURCE[s.hid]]["p"],
                    "p": one_sided(s11[SOURCE[s.hid]]["p"], s11[SOURCE[s.hid]]["coef"], s.sign)}
            for s in specs if SOURCE[s.hid] in s11}


def stressed_one_sided(verdicts: dict, specs: list[Spec], inflation: dict) -> dict:
    """run_frozen.stressed with one-sided p: CR1 t divided by its dry-run v3 inflation, t(G - 1), one-sided, Holm in the
    family (the other hypotheses keep their p1). Sensitivity only."""
    hs = [s.hid for s in specs if s.hid in inflation]
    if not hs:
        return {}
    p = {}
    for s in specs:
        v = verdicts[s.hid]
        if s.hid in inflation:
            t = v["coef"] / v["se"] / inflation[s.hid] if v["se"] > 0 else np.nan
            p2 = float(2 * stats.t.sf(abs(t), v["clusters"] - 1)) if np.isfinite(t) else np.nan
            p[s.hid] = one_sided(p2, v["coef"], s.sign)
        else:
            p[s.hid] = v["p"]
    ph = holm(pd.Series(p, dtype=float).fillna(1.0))
    return {h: {"t_inflation": inflation[h], "p_stress": p[h], "p_holm_stress": float(ph[h]),
                "note": run_frozen.STRESS_NOTE + "; one-sided"} for h in hs}


def bootstrap_one_sided(pop: pd.DataFrame, spec: Spec, clusters: int) -> dict:
    """Sensitivity: the exact one-sided share of wild bootstrap t* at or beyond t in the registered direction, from the
    registered draws (Rademacher, BOOT_SEED, BOOT_DRAWS; the same draws as the main p when clusters is its G)."""
    if clusters < 2:
        return {"p_exact_one_sided": np.nan, "note": "not estimable"}
    W = np.random.default_rng(BOOT_SEED).choice([-1.0, 1.0], size=(BOOT_DRAWS, clusters))
    b = wild_cluster_bootstrap_p(pop, spec.y, spec.x, spec.controls, spec.fe, spec.years, weights=W)
    if b.get("t_star") is None or not np.isfinite(b["t"]):
        return {"p_exact_one_sided": np.nan, "note": "not estimable"}
    return {"p_exact_one_sided": float(np.mean(spec.sign * b["t_star"] >= spec.sign * b["t"])),
            "p_two_sided_same_draws": b["p"], "t": b["t"], "draws": b["draws"]}


def fl_member(d: pd.DataFrame) -> np.ndarray:
    """PH4's keyword membership for 'federated learning' (posthoc.ph4_members: the frozen PH4 vocabulary; a paper is a
    member if its normalised keyword list contains the keyword), aligned with d. Reads no outcome."""
    names, K = posthoc.ph4_members(d)["K"]
    need(FL in names, f"{FL!r} is not in the frozen PH4 keyword vocabulary")
    return K[:, names.index(FL)]


def fl_gap(d: pd.DataFrame, member: np.ndarray) -> dict:
    """The PH4 core (posthoc.cell_counts + gap_summary) for one unit: level, recent level and trend of the gap."""
    years = np.arange(posthoc.PH4_YEARS[0], posthoc.PH4_YEARS[1] + 1)
    n_in, k_in, n_all, k_all = posthoc.cell_counts(member[:, None], d.year.to_numpy() - posthoc.PH4_YEARS[0],
                                                   d.accepted.to_numpy(float), len(years))
    return posthoc.gap_summary(n_in[0], k_in[0], n_all - n_in[0], k_all - k_in[0], years)


def h4fl(k: pd.DataFrame, out: pd.DataFrame, member: Callable[[pd.DataFrame], np.ndarray] | None = None) -> dict:
    """H4-FL with the PH4 code: population = RQ3 filter, 2018-2026 (posthoc.add_columns), units = ['federated
    learning'], posthoc.ph4_set (level, recent, trend, adjusted level, 200 within-year permutations, PH4_SEED). If the
    adjusted-level check cannot be estimated, level and trend come from the same PH4 core without it (noted)."""
    need((out.submission_id.to_numpy() == k.submission_id.to_numpy()).all(), "outcomes are not aligned with the frame")
    k = k.reset_index(drop=True).assign(rq3=out.rq3.to_numpy(), accepted=out.accepted.to_numpy())
    d = posthoc.add_columns(k[k.rq3 & k.year.between(*posthoc.PH4_YEARS)].copy()).reset_index(drop=True)
    m = (member or fl_member)(d)
    note = ""
    try:
        res, cells, calib = posthoc.ph4_set(d, [FL], m[:, None], np.random.default_rng(posthoc.PH4_SEED))
    except (ValueError, np.linalg.LinAlgError) as e:
        res, cells, calib = pd.DataFrame([{"unit": FL, **fl_gap(d, m)}]), pd.DataFrame(), {}
        note = f"adjusted level and calibration not estimable ({e}); level and trend from the PH4 core"
    r = res.iloc[0]
    p1 = one_sided(r.level_p, r.level, SIGN["H4-FL"])
    p_holm = float(holm(pd.Series({"H4-FL": p1}).fillna(1.0))["H4-FL"])
    primary = {"estimand": "level: paper-weighted mean yearly gap (FL minus all other papers of the year)",
               "predicted_sign": SIGN["H4-FL"], "coef": r.level, "se": r.level_se, "ci95": [r.level_ci_lo, r.level_ci_hi],
               "p_two_sided": r.level_p, "p": p1, "p_holm": p_holm, "p_method": "t(m-1), SE x max(1, sqrt(phi))",
               "sidedness": ONE_SIDED, "population_papers": int(len(d)), "fl_papers": int(m.sum()),
               "years_with_min_cell": int(r.years_with_min_cell), "phi": r.phi,
               "adjusted_level": r.get("adjusted_level", np.nan), "adjusted_level_p": r.get("adjusted_level_p", np.nan),
               "verdict": "supported" if np.isfinite(p1) and r.level < 0 and p_holm < ALPHA else "not supported",
               "note": note}
    if int(r.years_with_min_cell) >= posthoc.PH4_MIN_YEARS and np.isfinite(r.trend_p):
        t1 = one_sided(r.trend_p, r.trend, SIGN["H4-FL"])
        secondary = {"estimand": "trend of the yearly gap (pp per year, WLS)", "coef": r.trend, "se": r.trend_se,
                     "ci95": [r.trend_ci_lo, r.trend_ci_hi], "p_two_sided": r.trend_p, "p": t1,
                     "verdict": "supported" if r.trend < 0 and t1 < ALPHA else "not supported"}
    else:
        secondary = {"estimand": "trend of the yearly gap", "verdict": "not estimable",
                     "note": f"{int(r.years_with_min_cell)} years with >= {posthoc.PH4_MIN_CELL} FL papers "
                             f"(needs {posthoc.PH4_MIN_YEARS})"}
    return {"res": res, "cells": cells, "calibration": calib, "primary": primary, "secondary": secondary}


def rq_part(frames: dict[str, pd.DataFrame], settings: dict, load: Callable[[pd.Series], pd.DataFrame],
            ys: dict[str, pd.Series] | None = None, model: pd.Series | None = None,
            describe: bool = False) -> tuple[dict, pd.DataFrame]:
    """H1d, RQ2 (H2b', H2c'), then the outcomes (load), RQ3 (H3a) and H4-FL, in run_frozen's order. ys / model: the
    simulated RQ2 / RQ1 outcome-side labels (--simulate); without them rq2.run's guard demands the frozen entry point."""
    gate = bool(settings["h2d_gate_passed"])
    remedies = run_frozen.remedies_of(settings)
    rq2.guard(ys)                                        # real labels only inside a verified run (before H1d reads one)
    v1, rows1 = h1d(frames, model)
    res2 = rq2.run(frames, gate, ys=ys, remedies=remedies)
    v2 = redecide(res2["rows"], SPECS2)
    pop2 = rq2.population(rq2.with_columns(frames["k100"], ys))
    exact = {s.hid: bootstrap_one_sided(pop2, s, int(v2[s.hid]["clusters"])) for s in SPECS2 if SOURCE[s.hid] in remedies}
    out = load(frames["k100"].submission_id)
    res3 = rq3.run(frames, out, gate, describe=describe, remedies=remedies)
    v3 = redecide(res3["rows"], SPECS3)
    inflation = {s.hid: settings["stress_t_inflation"][SOURCE[s.hid]] for s in SPECS2 + SPECS3 if SOURCE[s.hid] in remedies}
    res = {"gate": gate, "remedies": list(remedies),
           "rq1": {"verdicts": v1, "rows": rows1},
           "rq2": {"verdicts": v2, "rows": res2["rows"], "s11": s11_one_sided(res2["rows"], SPECS2),
                   "stress": stressed_one_sided(v2, SPECS2, inflation), "bootstrap_exact": exact,
                   "label_reliability": {
                       "confirmation_second_pass": label_reliability(frames["k100"].submission_id),
                       "pooled_second_pass_and_s8_reference": res2["label_reliability"],
                       "note": "the confirmation block describes the labels H2b'/H2c' use; rq2.label_reliability pools "
                               "the discovery and confirmation second pass (S8 rates: discovery random-stratum "
                               "reference papers, which S8 uses)"}},
           "rq3": {"verdicts": v3, "rows": res3["rows"], "s11": s11_one_sided(res3["rows"], SPECS3),
                   "stress": stressed_one_sided(v3, SPECS3, inflation), "counts": res3["counts"]},
           "h4fl": h4fl(frames["k100"], out)}
    return res, out


def label_reliability(ids: pd.Series, labels: pd.DataFrame | None = None) -> dict:
    """D11 for the confirmation labels: second-pass agreement and kappa (rq2.label_reliability's definition) of the
    method and measurement indicators, and the main-class kappa of the label-quality gate (registered: >= 0.80), on the
    second pass of the papers in ids only. Labels are read, never an outcome."""
    lab = pd.read_csv(common.TOPICS / "paper_contributions.csv.gz") if labels is None else labels
    sp = lab[lab.submission_id.isin(set(ids)) & lab.second_pass_primary_type.notna()]
    first, second = sp.primary_type.map(common.class_of), sp.second_pass_primary_type.map(common.class_of)
    out = {"second_pass_papers": int(len(sp))}
    if not len(sp):
        return {**out, "note": "no second-pass paper"}
    po = float((first == second).mean())
    pe = float(sum(first.eq(c).mean() * second.eq(c).mean() for c in set(first) | set(second)))
    out["main_class"] = {"agreement": round(po, 4), "kappa": round((po - pe) / (1 - pe), 4) if pe < 1 else None,
                         "gate_kappa_ge_0_80": bool(pe < 1 and (po - pe) / (1 - pe) >= 0.80)}
    for name, pos in [("method", {"method"}), ("measurement", {"dataset_benchmark", "evaluation"})]:
        a, b = first.isin(pos), second.isin(pos)
        po = float((a == b).mean())
        pe = float(a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean()))
        out[name] = {"second_pass_agreement": round(po, 4),
                     "second_pass_kappa": round((po - pe) / (1 - pe), 4) if pe < 1 else None}
    return out


# ---------------------------------------------------------------- PH5 hook (component C)

def ph5_available() -> bool:
    return "ph5_confirm" in sys.modules or importlib.util.find_spec("ph5_confirm") is not None


def ph5_part(frames: dict[str, pd.DataFrame], out: pd.DataFrame) -> dict | None:
    """HOOK for the PH5 confirmation analyses: ph5_confirm.compute(frames, out) -> {name: DataFrame | JSON-able},
    written to <run dir>/ph5/ by posthoc.write_outputs (non-DataFrame parts also go into summary.json).
    frames = the confirmation frames (pooled features, filtered after construction; D14), out = the outcome block of
    frames['k100'] (real in the gated run, simulated with --simulate). None when ph5_confirm.py does not exist."""
    if not ph5_available():
        return None
    return importlib.import_module("ph5_confirm").compute(frames, out)


# ---------------------------------------------------------------- summary and outputs

def summarise(res: dict, settings: dict, mode: str, frames: dict[str, pd.DataFrame]) -> dict:
    """The verdicts with run_frozen's labels (S11 qualifier from the one-sided S11 p, MDE80 from the confirmation
    dry-run if FREEZE_CONFIRMATION.json carries it), E9 for every hypothesis that is not supported, H4-FL and PH5."""
    mde = (settings.get("confirmation_mde80") or {}).get("mde80", {})
    sesoi = {s.hid: s.sesoi for s in [H1D] + SPECS2 + SPECS3}
    no_sesoi = {h for h in [*mde, *sesoi, "H4-FL"] if not np.isfinite(sesoi.get(h, np.nan))}    # H1d, H4-FL
    powered = {h: bool(m is not None and m <= 3 * sesoi[h]) for h, m in mde.items() if h not in no_sesoi} or None
    v1 = {h: {**v, "ci_tost_method": run_frozen.CI_METHOD, "qualifier": "", "s11_agrees": None, "mde80": mde.get(h),
              "underpowered_at_3x_sesoi": None}                  # RQ1 registered no SESOI: not applicable
          for h, v in res["rq1"]["verdicts"].items()}
    v2 = run_frozen.labelled(res["rq2"]["verdicts"], res["rq2"]["s11"], mde, powered)
    v3 = run_frozen.labelled(res["rq3"]["verdicts"], res["rq3"]["s11"], mde, powered)
    notes = {h: ("" if h in mde else "confirmation MDE80 not computed (run_confirmation.py --simulate --mde-reps)")
             + ("; no SESOI registered: underpowered_at_3x_sesoi not applicable" if h in no_sesoi else "")
             for h in [*v1, *v2, *v3]}
    e9 = run_frozen.equivalence_table({**v1, **v2, **v3}, mde, powered or {}, notes)
    for r in e9:
        if powered is None or r["hypothesis"] in no_sesoi:       # unknown without a confirmation MDE, or no SESOI:
            r["underpowered_at_3x_sesoi"] = None                 # not "underpowered"
    ph5 = res.get("ph5")
    return {
        "mode": mode, "status": STATUS, "registered": REGISTERED, "families": FAMILIES,
        "rq1": {"family": FAMILIES["rq1"], "verdicts": v1},
        "rq2": {"family": FAMILIES["rq2"], "verdicts": v2, "s11_twoway_one_sided": res["rq2"]["s11"],
                "stress_sensitivity": res["rq2"]["stress"], "bootstrap_exact_one_sided": res["rq2"]["bootstrap_exact"],
                "label_reliability": res["rq2"]["label_reliability"], NOT_REGISTERED: ["H2a"]},
        "rq3": {"family": FAMILIES["rq3"], "verdicts": v3, "s11_twoway_one_sided": res["rq3"]["s11"],
                "stress_sensitivity": res["rq3"]["stress"], "counts": res["rq3"]["counts"], NOT_REGISTERED: ["H3b"]},
        "h4fl": {"family": FAMILIES["h4fl"], "primary": {**res["h4fl"]["primary"], "mde80": mde.get("H4-FL"),
                                                         "underpowered_at_3x_sesoi": None},
                 "secondary": res["h4fl"]["secondary"],
                 "calibration_within_year_permutations": res["h4fl"]["calibration"]},
        "e9_equivalence": e9,
        "ph5": "not run (no ph5_confirm.py or --without-ph5)" if ph5 is None else
               {k: v for k, v in ph5.items() if not isinstance(v, pd.DataFrame)},
        "remedies": res["remedies"], "h2d_gate_passed": res["gate"], "tau": settings.get("tau"),
        "withdrawn_review_status_unknown": res.get("withdrawn_review_status_unknown"),
        "papers": {"confirmation_frame": int(len(frames["k100"])),
                   "by_year": frames["k100"].groupby("year").size().to_dict()},
    }


def verdict_lines(summary: dict) -> list[str]:
    lines = [f"[{summary['mode']}] {summary['status']}"]
    for part in ("rq1", "rq2", "rq3"):
        for h, v in summary[part]["verdicts"].items():
            lines.append(f"{h:5s} {v['outcome']:11s} ~ {v['regressor']:11s} coef {v['coef']:+.4f} CI95 [{v['ci95'][0]:+.4f}, "
                         f"{v['ci95'][1]:+.4f}] p1 {v['p']:.3g} (two-sided {v['p_two_sided']:.3g}) p_holm {v['p_holm']:.3g} "
                         f"robust {v['robustness_same_sign']:.0%} hindsight {'ok' if v['hindsight_variants_same_sign'] else 'FAIL'}"
                         f" -> {v['verdict']}{' (fragile)' if v['fragile'] else ''}"
                         f"{' (' + v['qualifier'] + ')' if v.get('qualifier') else ''}")
    p, s = summary["h4fl"]["primary"], summary["h4fl"]["secondary"]
    lines.append(f"H4-FL level {p['coef']:+.4f} CI95 [{p['ci95'][0]:+.4f}, {p['ci95'][1]:+.4f}] p1 {p['p']:.3g} "
                 f"(two-sided {p['p_two_sided']:.3g}) FL papers {p['fl_papers']} years>=10 {p['years_with_min_cell']} "
                 f"-> {p['verdict']}; trend: " + (f"{s['coef']:+.4f} p1 {s['p']:.3g} -> {s['verdict']}"
                                                  if s["verdict"] != "not estimable" else "not estimable"))
    return lines


def write_results(res: dict, summary: dict, out_dir: Path) -> None:
    need(DISCOVERY_OUTPUT not in out_dir.parents and out_dir != DISCOVERY_OUTPUT, f"refusing to write into {out_dir}")
    out_dir.mkdir(parents=True, exist_ok=True)
    res["rq1"]["rows"].to_csv(out_dir / "h1d.csv", index=False)
    label_rows(res["rq2"]["rows"]).to_csv(out_dir / "rq2_rows.csv", index=False)
    label_rows(res["rq3"]["rows"]).to_csv(out_dir / "rq3_rows.csv", index=False)
    res["h4fl"]["res"].to_csv(out_dir / "h4fl.csv", index=False)
    res["h4fl"]["cells"].to_csv(out_dir / "h4fl_cells.csv", index=False)
    if res.get("ph5") is not None:
        posthoc.write_outputs(res["ph5"], out_dir / "ph5")
    (out_dir / "summary.json").write_text(json.dumps(run_frozen.clean(summary), indent=2) + "\n")
    lines = verdict_lines(summary)
    (out_dir / "stdout.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def check_registration(freeze: dict) -> None:
    """The frozen registration is this file's REGISTERED, the freeze was made with the PH5 module, and its PH5
    registration is ph5_confirm.REGISTERED."""
    need(freeze.get("registered") == json.loads(json.dumps(REGISTERED)), "the registration differs from the frozen one")
    need(freeze.get("ph5_hook_present") is True and ph5_available(), "the freeze was made without the PH5 module")
    need(freeze.get("registered_ph5") == json.loads(json.dumps(importlib.import_module("ph5_confirm").REGISTERED)),
         "the PH5 registration differs from the frozen one")


def check_settings(freeze: dict) -> None:
    """The frozen settings the run relies on: the pooled copies of the H2d gate and τ equal the frozen values, the
    discovery FREEZE.json is the one recorded (and its settings were copied verbatim), the registration is this file's
    and the PH5 registration ph5_confirm's (the freeze was made with the PH5 module), and the pooled variables were
    built after τ was applied."""
    gate = json.loads((common.OUTPUT / "h2d_validation.json").read_text())["gate"] == "pass"
    need(gate == freeze["h2d_gate_passed"], "the H2d gate differs from the frozen value")
    need(json.loads((common.OUTPUT / "resubmission_tau.json").read_text())["tau"] == freeze["tau"], "tau differs from the frozen value")
    need(outcomes.sha256(outcomes.FREEZE_DISCOVERY) == freeze["discovery_freeze_sha256"], "FREEZE.json is not the recorded one")
    discovery = json.loads(outcomes.FREEZE_DISCOVERY.read_text())
    need(all(freeze.get(k) == v for k, v in discovery.items() if k not in ("sha256", "created_utc")),
         "FREEZE_CONFIRMATION.json does not carry the discovery settings verbatim")
    check_registration(freeze)
    missing = set(run_frozen.remedies_of(freeze)) - set(freeze.get("stress_t_inflation", {}))
    need(not missing, f"no stress_t_inflation for remedied {sorted(missing)}")
    need(json.loads((common.OUTPUT / "checks" / "variables.json").read_text())["s4_available"],
         "paper_variables.csv.gz was built before tau was applied")


def run(freeze: dict, started: str) -> None:
    """The real run (always with the registered PH5 tests)."""
    check_settings(freeze)
    _, frames, _ = pooled_frames()
    need(bool(frames["k100"].has_earlier_version.notna().all()), "earlier_versions.csv.gz has no probable_earlier_version")
    res, out = rq_part(frames, freeze, lambda ids: outcomes.load("real", ids), describe=True)
    res["withdrawn_review_status_unknown"] = outcomes.UNKNOWN_REVIEW.get("confirmation")   # registered contingency
    res["ph5"] = ph5_part(frames, out)
    need(res["ph5"] is not None, "the PH5 part did not run")
    finished = run_frozen.now()
    write_results(res, summarise(res, freeze, "real", frames), OUT)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    info = {"started_utc": started, "finished_utc": finished, "git_head": head, "corpus": common.CORPUS,
            "freeze_sha256": outcomes.sha256(outcomes.FREEZE_CONFIRMATION), "with_ph5": True,
            "python": sys.version.split()[0], "numpy": np.__version__, "pandas": pd.__version__,
            "scipy": scipy.__version__, "matplotlib": matplotlib.__version__, "platform": platform.platform()}
    (OUT / "run_info.json").write_text(json.dumps(info, indent=2) + "\n")


# ---------------------------------------------------------------- --simulate (no guard, no real outcome)

def calibrations(frame: pd.DataFrame) -> dict[str, DGP]:
    """Variance components of every simulated label (dgp.calibrate: one column at a time, from its own topic-year cell
    means, no regressor), from the given frame: the pooled frame's discovery rows, so no confirmation label shapes them."""
    keyed = frame[frame.has_author_key]
    cal = {c: calibrate(keyed, c, rq2.YEARS) for c in ["incumbent", "method", "measurement", "buzzword", "lists_hot"]}
    cal["model"] = calibrate(frame, "model", rq1_rise.YEARS)
    return cal


def simulated_labels(k: pd.DataFrame, cal: dict[str, DGP], rng: np.random.Generator, plant: str | None = None,
                     delta: float = 0.0) -> tuple[dict[str, pd.Series], pd.Series]:
    """Simulated RQ2 outcome-side columns (all of rq2.SIMULATED, as dryrun.rq2_outcomes; newcomer follows the simulated
    incumbency) and a simulated RQ1 'model' label. plant (H1d, H2b' or H2c') adds delta in the registered direction
    (probability points per unit of the regressor) to that outcome only."""
    eff = lambda h, x: {x: delta * SIGN[h]} if plant == h else {}
    inc = simulate(k, cal["incumbent"], rng)
    f = k.assign(newcomer=1 - inc)
    meth = simulate(f, replace(cal["method"], effects=eff("H2b'", "newcomer")), rng)
    meas = simulate(f, replace(cal["measurement"], effects=eff("H2c'", "newcomer")), rng)
    buzz, lists = simulate(f, cal["buzzword"], rng), simulate(f, cal["lists_hot"], rng)
    model = simulate(k, replace(cal["model"], effects=eff("H1d", "fm_adoption")), rng)
    keep = rng.random(len(inc))
    ids = k.submission_id.to_numpy()
    ys = {"incumbent": inc, "incumbent_w2": inc * (keep < 0.8), "incumbent_s4": inc * (keep < 0.995), "method": meth,
          "measurement": meas, "buzzword": buzz * lists, "lists_hot": lists}
    return {c: pd.Series(v, index=ids) for c, v in ys.items()}, pd.Series(model, index=ids)


def simulated_outcomes(k: pd.DataFrame, seed: int, plant: str | None = None, delta: float = 0.0,
                       fl: np.ndarray | None = None) -> pd.DataFrame:
    """The sealed loader's simulated mode (dry-run v3's RQ3 'hi' setting); plant H3a (maturity) or H4-FL (FL papers)."""
    eff = {"maturity": delta * SIGN["H3a"]} if plant == "H3a" else {"fl": delta * SIGN["H4-FL"]} if plant == "H4-FL" else {}
    frame = k if fl is None else k.assign(fl=fl.astype(float))
    return outcomes.load("simulated", k.submission_id, seed=seed, frame=frame, dgp=replace(RQ3_DGP_HI, effects=eff))


def detected(h: str, frames: dict[str, pd.DataFrame], cal: dict[str, DGP], delta: float, seed: int,
             fl: np.ndarray, remedies: tuple[str, ...]) -> bool:
    """One replication: the registered main specification on outcomes with a planted effect; detected = one-sided
    p1 < 0.05 / m in the predicted direction (m = family size: Holm's first step, as in dryrun.py)."""
    k = frames["k100"]
    m = len(next(f for f in FAMILIES.values() if h in f))
    if h in ("H1d", "H2b'", "H2c'"):
        ys, model = simulated_labels(k, cal, np.random.default_rng(seed), plant=h, delta=delta)
        if h == "H1d":
            e = estimate_rq1(k.assign(model=model.to_numpy()))
        else:
            s = next(s for s in SPECS2 if s.hid == h)
            pop = rq2.population(rq2.with_columns(k, ys))
            e = fit(pop, s)
            e = apply_bootstrap(e, pop, s) if SOURCE[h] in remedies else e
    else:
        o = simulated_outcomes(k, seed, plant=h, delta=delta, fl=fl)
        if h == "H3a":
            full = rq3.attach(k, o)
            e = fit(full[full.rq3], SPECS3[0])
        else:
            kk = k.assign(rq3=o.rq3.to_numpy(), accepted=o.accepted.to_numpy())
            keep = (kk.rq3 & kk.year.between(*posthoc.PH4_YEARS)).to_numpy()
            g = fl_gap(kk[keep], fl[keep])
            e = {"coef": g["level"], "p": g["level_p"]}
    p1 = one_sided(e["p"], e["coef"], SIGN[h])
    return bool(np.isfinite(p1) and p1 < ALPHA / m)


def mde80(grid: tuple[float, ...], power: list[float]) -> float | None:
    """Smallest planted effect with 80% detection, linearly interpolated over the grid (None if never reached)."""
    for i, (g, p) in enumerate(zip(grid, power)):
        if p >= 0.8:
            return float(g) if i == 0 else float(grid[i - 1] + (0.8 - power[i - 1]) * (g - grid[i - 1]) / (p - power[i - 1]))
    return None


def mde_grid(frames: dict[str, pd.DataFrame], cal: dict[str, DGP], settings: dict, reps: int, seed: int,
             fl: np.ndarray) -> dict:
    """Detection rate per registered test and planted effect (GRID; reps replications each) and MDE80. Effects are
    probability points per unit of the regressor (H4-FL: for an FL paper) before clipping to [0.005, 0.995]."""
    remedies = run_frozen.remedies_of(settings)
    rng = np.random.default_rng([seed, 2])
    out = {}
    for h, grid in GRID.items():
        power = [float(np.mean([detected(h, frames, cal, d, int(rng.integers(2 ** 31)), fl, remedies) for _ in range(reps)]))
                 for d in grid]
        out[h] = {"grid": list(grid), "power": power, "mde80": mde80(grid, power), "reps": reps,
                  "alpha": ALPHA / len(next(f for f in FAMILIES.values() if h in f))}
    return {"mde80": {h: v["mde80"] for h, v in out.items()}, "by_test": out,
            "dgp": "RQ2/RQ1 labels: dgp.calibrate on the discovery rows; acceptance: dry-run v3 RQ3 'hi' setting",
            "detection": "predicted sign and one-sided p1 < 0.05 / family size in the main specification"}


def simulate_run(frames: dict[str, pd.DataFrame], calib: pd.DataFrame, settings: dict, seed: int, out_dir: Path,
                 mde_reps: int = 0, with_ph5: bool = True) -> dict:
    """The whole confirmation pipeline on simulated outcomes (plumbing), written to out_dir (cleared first); with
    mde_reps > 0 also the MDE grid (mde.json). No real outcome, and no real label as an outcome, is used."""
    need(DISCOVERY_OUTPUT not in out_dir.parents and out_dir != DISCOVERY_OUTPUT, f"refusing to write into {out_dir}")
    if out_dir.exists():
        shutil.rmtree(out_dir)
    k = frames["k100"]
    cal = calibrations(calib)
    ys, model = simulated_labels(k, cal, np.random.default_rng(seed))
    res, out = rq_part(frames, settings, lambda ids: simulated_outcomes(k, seed), ys=ys, model=model)
    res["ph5"] = ph5_part(frames, out) if with_ph5 else None
    summary = summarise(res, settings, f"SIMULATED outcomes, seed {seed} (plumbing only)", frames)
    if mde_reps:
        summary["mde"] = mde_grid(frames, cal, settings, mde_reps, seed, fl_member(k))
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "mde.json").write_text(json.dumps(run_frozen.clean(summary["mde"]), indent=2) + "\n")
    write_results(res, summary, out_dir)
    return summary


def simulate_main(seed: int, mde_reps: int, with_ph5: bool) -> None:
    pooled, frames, mask = pooled_frames()
    settings = json.loads(outcomes.FREEZE_DISCOVERY.read_text())       # the frozen remedies, gate and stress settings
    simulate_run(frames, pooled["k100"][~mask].reset_index(drop=True), settings, seed, DRY, mde_reps, with_ph5)


# ---------------------------------------------------------------- entry

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rerun-reason", help="required if output_pooled/confirmation_run/ already holds an attempt")
    p.add_argument("--simulate", type=int, metavar="SEED", help="simulated outcomes, no guard; writes confirmation_dryrun/")
    p.add_argument("--mde-reps", type=int, default=0, help="with --simulate: replications per planted effect (MDE80)")
    p.add_argument("--without-ph5", action="store_true",
                   help="with --simulate: run without the PH5 hook (the real run refuses it)")
    a = p.parse_args()
    check_corpus()
    if a.simulate is not None:
        simulate_main(a.simulate, a.mde_reps, not a.without_ph5)
        return
    started = run_frozen.now()
    log = OUT / "attempts.jsonl"
    previous = run_frozen.started_attempts(log)
    if previous and not a.rerun_reason:                        # refuse before anything is verified or loaded
        raise SystemExit(f"{len(previous)} earlier attempt(s) recorded in {log}; a rerun needs --rerun-reason")
    seen = [str(f.relative_to(ROOT)) for f in POOLED_READS if f.exists()]
    if seen:                                                   # no confirmation (re)run after pooled outcomes were read
        raise SystemExit(f"pooled confirmation outcomes may have been read ({', '.join(seen)}): no confirmation attempt, "
                         "rerun included, is allowed any more")
    if a.without_ph5:
        raise SystemExit("--without-ph5 is for --simulate only: the real run always runs the registered PH5 tests")
    if not ph5_available():
        raise SystemExit("ph5_confirm.py (the PH5 hook) is missing: the real run needs it")
    try:
        freeze = outcomes.require_frozen()
        OUT.mkdir(parents=True, exist_ok=True)
        attempt = {"attempt": len(previous) + 1, "started_utc": started, "rerun_reason": a.rerun_reason,
                   "freeze_sha256": outcomes.sha256(outcomes.FREEZE_CONFIRMATION), "with_ph5": True}
        with log.open("a") as f:
            f.write(json.dumps({**attempt, "status": "started"}) + "\n")
        try:
            run(freeze, started)
        except BaseException:
            with log.open("a") as f:
                f.write(json.dumps({**attempt, "status": "failed", "at_utc": run_frozen.now(),
                                    "traceback": traceback.format_exc()}) + "\n")
            raise
        with log.open("a") as f:
            f.write(json.dumps({**attempt, "status": "finished", "at_utc": run_frozen.now()}) + "\n")
    finally:
        outcomes.release()


if __name__ == "__main__":
    main()
