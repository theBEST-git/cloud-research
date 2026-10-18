"""PH5 confirmation (POOLED_SPEC D6; PREREGISTRATION.md "Confirmation", D14, D15 and the PH5 declarations of
2026-10-17): the PH5 confirmation tests declared below (and as REGISTERED), run once on the released confirmation papers
inside run_confirmation.py (hook ph5_part -> compute(frames, out); with --simulate on simulated outcomes). They are
confirmatory only once PREREGISTRATION.md registers them before FREEZE_CONFIRMATION.json, which pins REGISTERED
(registered_ph5; run_confirmation.check_registration compares it). Status: a pre-registered out-of-sample
replication on the released former-holdout papers, not an untouched independent holdout. Every test is an association
within the stated fixed effects, as in discovery.

FEATURES (D14). run_confirmation.py sets ICLR_CORPUS=pooled before the first fashion import, so every outcome-free
feature cache of the PH5 modules (ph5_pivot.features, ph5_position.build / author_keys / early_columns,
ph5_teams.paper_features, ph5_kwtiming.features, ph5_premia.unit_sets) is built once on discovery + confirmation papers
with the frozen, unchanged module code; only then are the populations restricted to confirmation papers:
  pivot     author histories over discovery + confirmation submissions with the history-start rule of ph5_pivot (a
            2023-2026 paper uses an author's submissions from 2021 on; 2019-2020 papers from 2017 on); P_a excludes the
            paper's pooled probable earlier version (output_pooled/earlier_versions.csv.gz) and every paper with cos >=
            0.90; vectors centred with the frozen discovery mean (D15, output_pooled/specter2_centring_mean.npy = the
            discovery file); spline knots and contrast points are the frozen ph5_pivot.REF (never recomputed).
  position  novelty = 1 - the mean of the 10 largest cosines with every earlier-year pooled paper, the paper's chain of
            pooled probable earlier versions excluded; percentile within the pooled k100 topic x year cell (all
            submissions of both splits, any outcome); twins and sibling twins from pooled same-year pairs (shared author
            keys or normalised names over both author tables).
  teams     author types (novice / crossover / insider) from every earlier-year pooled submission of the author ID, any
            outcome; T1 (H1, and the unregistered H2) does not use `proven`, which ph5_teams.population computes from
            the confirmation acceptances only (discovery outcomes are not readable from run_confirmation.py).
  kwtiming  the keyword frame on the pooled corpus (confirmation keywords: keyword_map.normalize of the raw author
            keywords; the frozen 759-keyword vocabulary); onsets, age bins and momentum terciles from the pooled
            output_pooled/keyword_year.csv.gz (asserted by ph5_kwtiming.keyword_states).
  premia    unit memberships of the pooled frame (early map, k100, PH4 keywords, areas).
Frames, topics, hot, maturity, newcomer, labels and team sizes are the pooled panel.frame('k100') columns. Outcomes are
only those of the confirmation papers (the outcome block `out` of run_confirmation.py, real in the gated run); every
discovery paper is outside every population (rq3 = False). Models, controls, clustering and reference points are the
frozen PH5 code; fixed effects are estimated among the confirmation rows of each population.

ONE-SIDED p (run_confirmation.ONE_SIDED): p1 = p / 2 if the estimate has the predicted sign, else 1 - p / 2, where p is
the test's declared two-sided p (a wrong-sign estimate therefore has p1 >= 0.5). Missing estimates have p1 = NaN, which
Holm counts as 1, and the verdict 'not estimable'.

PRIMARY family (Holm over the two one-sided p, alpha 0.05; supported = predicted sign and Holm p < 0.05):
  E1   ph5_pivot P1 far-jump contrast, predicted < 0: the population curve at the frozen F_max p10 minus at p50.
       Population: confirmation RQ3 decided papers 2023-2026 with >= 1 experienced author. LPM accepted ~ RCS(F_max)
       + RCS(F_max) x (hot - the sample's hot share) + class (ref. method) + FM + log2 team + n_exp dummies (2, 3, 4+)
       + log(1 + n_prior_team) + has_earlier_version | k100 topic x year FE (ph5_pivot.declared). p_used = the larger
       of the CR1 p (by topic, t(G - 1)) and the calibrated p from NULLS = 200 simulated nulls on the same papers
       (accepted ~ Bernoulli(the paper's topic x year acceptance rate), P7's rule, seed E1_NULL_SEED): the pre-run
       calibration found the CR1 SE ~5% too small (SD / mean SE 1.054; one-sided size 5.0% at 0.025 over 400 null
       frames), and the max can only be more conservative. (compute(nulls=0) drops the calibrated p and says so.)
  P1b  ph5_position Q0 novelty Q1 minus Q3, predicted < 0. Population: confirmation RQ3 decided papers 2019-2026. LPM
       accepted ~ q1 + q2 + q4 + q5 (ref. Q3) + any_twin + class + FM + log2 team + newcomer + sibling_twin | k100
       topic x year FE; CR1 by topic, t(G - 1) (ph5_position.declared; p_used = the CR1 p, as declared).
SECONDARY (each one-sided at alpha 0.05, reported; no family, no family claim; supported = predicted sign and p1 <
0.05, plus the extra condition stated for A1 and the premia tests):
  E4   ph5_pivot P2 within-author slope per +0.1 cos, predicted > 0: one row per (confirmation paper of E1's
       population, experienced author), weight 1 / n_exp; accepted ~ prior_cos + log1p(|P_a|) + class + FM + log2 team
       | author FE + topic x year FE (singletons dropped); CR1 by topic with the author FE in the small-sample factor,
       t(G - 1). p = the CR1 p (as declared); the two-way (topic, author) p is reported (one-sided) as a check.
  P7   ph5_position Q5 within-author novelty slope per 10 percentile points, predicted > 0: confirmation papers
       2023-2026 of P1b's population, one row per (paper, author ID), weight 1 / the paper's author IDs; author + topic
       x year FE; p_used = the largest of the CR1 p, the two-way (topic, author) p and the calibrated p from NULLS =
       200 simulated nulls on the same papers (accepted ~ Bernoulli(the paper's topic x year acceptance rate),
       ph5_position.calibrated_p, seed ph5_position.SEED), as declared; then made one-sided. (compute(nulls=0) drops
       the calibrated p and says so in p_rule.)
  H1   ph5_teams T1 one topic insider vs none (the n_ins = 1 coefficient), predicted > 0. Population: confirmation RQ3
       decided papers 2023-2026 with an author ID. accepted ~ 1[n_ins = 1] + 1[n_ins >= 2] + team-size dummies (ref. 1)
       + n_exp dummies (ref. 0) + class + FM + has_earlier_version + log(1 + prior) | k100 topic x year FE; CR1 by
       topic, t(G - 1).
  A1   ph5_kwtiming Model A Emerging (young x rising) minus Mainstream (old x flat), predicted > 0. Population:
       eligible keyword uses of confirmation RQ3 decided papers 2019-2026, weights 1 / the paper's eligible keywords;
       accepted ~ 8 state dummies + class + FM + log2 team + newcomer + log(1 + V keywords) | k100 topic x year FE;
       two-way SE (keyword, topic), t(min G - 1). Reading rule as declared: also the null-frame p must be < 0.05, here
       one-sided: p_null = (1 + #{t_null >= t}) / (N_REF + 1) over N_REF = 200 null frames (decided set and acceptance
       of the confirmation papers from ph5_common.fake_outcomes, seeds 0-199).
  premia out of sample (ph5_premia (c), early map; k100, keywords and areas reported, no claim). Discovery premia:
       the committed discovery run's 2018-2022 window premia, raw (centred, w1) and EB-shrunk (eb1), with their
       variances (v1), from output/posthoc/ph5_premia/windows.csv (sha256 pinned in DISCOVERY_WINDOWS_SHA256; never
       re-estimated, so they are fixed predictions). Confirmation premia: per unit, the paper-weighted mean of the
       yearly gaps (acceptance of the unit's confirmation papers minus all other confirmation papers of the year) over
       2024-2026, variance sum (n_t / n)^2 p_t (1 - p_t) (1 / n_t + 1 / n0_t) (ph5_premia.cells / window_premia on the
       confirmation RQ3 decided papers). Units: the discovery window units with >= MIN_CELL = 15 decided confirmation
       papers in 2024-2026.
       b      WLS slope of the confirmation premium on the raw discovery premium, weights 1 / (v_W2 + tau_W2^2)
              (tau_W2^2 = DerSimonian-Laird across these units), HC3 SE, t(m - 2) (ph5_premia.wls_hc3); predicted
              0 < b < 1, tested as an intersection-union test: p = max(one-sided p of b > 0, one-sided p of b < 1).
       EB     D0 = mean_u y_u^2 - mean_u (y_u - eb1_u)^2 (unweighted over units; y = the confirmation premium centred
              at its 1/v-weighted mean): the EB-shrunk discovery premium against the no-information prediction 0,
              predicted > 0 (shrunk past premia carry out-of-sample signal): one-sided paired t (Diebold-Mariano),
              t(U - 1). Without persistence E[D0] = -E[eb1^2] < 0 (the test cannot pass by shrinkage alone); D0 > 0
              needs, roughly, a slope of y on eb1 above 1/2. Reported alongside: the three mean squared errors (zero,
              raw, EB), the 1 / (v_W2 + tau_W2^2)-weighted D0, a 999-draw unit-bootstrap percentile CI of D0 (centring
              redone per draw), and, descriptive only, D = mse(raw) - mse(EB) with its paired t (it favours shrinkage
              even when premia do not persist, so it says 'shrink past premia', nothing about persistence) and
              ph5_premia.winners on the same units (signal correlation rho_w, retention of the discovery top / bottom
              decile, quintile for areas).
Not registered for confirmation (reported, labelled so): E2, E3 and P1a, P2-P6 (they come out of the same declared
calls), teams H2 (T1, no `proven`) and the raw-vs-EB premia difference D.

OUTPUTS (run_confirmation.write_results -> posthoc.write_outputs): <run dir>/ph5/tests.csv (the registered rows,
verdicts, Holm p of the primary pair, calibrated MDE80 and power when present), pivot.csv, position.csv, teams.csv,
kwtiming.csv (every estimate of the declared calls, unregistered ones labelled), premia.csv, premia_units.csv,
premia_retention.csv and summary.json (registration, populations, verdict lines, timings; also under 'ph5' in the run's
summary.json). Run dir: output_pooled/confirmation_run (real) or output_pooled/confirmation_dryrun (--simulate).

CALIBRATION (calibrate(); outcome-free: simulated outcomes only, before the freeze; written to
output_pooled/ph5_confirm/calibration.json and attached to the run's E1 / P1b rows when present). ph5_common-style
fake outcomes over the confirmation papers of the pooled frame (decided ~ 74%, acceptance ~ Bernoulli of the
year-specific base rate 0.45 -> 0.32), with a probability-scale plant whose LPM target is the planted contrast:
E1: delta x ((B(F_max) - B(p50)) . c) / (c . c), B = the frozen RCS basis, c = B(p10) - B(p50); P1b: delta x 1[nov_pct
< 0.2]. Null frames give the one-sided size of each test and the family's any-Holm rate; planted frames at multiples of
the discovery estimates (E1 -5.4 pp, P1b -3.3 pp) give the power at the discovery effect and MDE80 (detected =
predicted sign and one-sided p < 0.05 / 2, Holm's first step; also at 0.05), with the bias and coverage against the
target (the same model fitted to the true probabilities on the same sample). It measures the CR1 p of both tests; E1's
registered max(CR1, calibrated) rule can only lower its size and power.

    python research/fashion/ph5_confirm.py calibrate [--nulls N] [--reps N] [--seed S]     (pooled; simulated outcomes)
"""
from __future__ import annotations

import os

if __name__ == "__main__":                           # the corpus switch precedes every fashion import (common.py, D1)
    if (os.environ.get("ICLR_CORPUS") or "pooled") != "pooled":
        raise SystemExit("ph5_confirm.py runs on the pooled corpus: unset ICLR_CORPUS or set it to 'pooled'")
    os.environ["ICLR_CORPUS"] = "pooled"

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402
from typing import Callable  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import stats  # noqa: E402
from scipy.special import logit  # noqa: E402

import common  # noqa: E402
import panel  # noqa: E402
import ph5_common  # noqa: E402
import ph5_kwtiming  # noqa: E402
import ph5_pivot  # noqa: E402
import ph5_position  # noqa: E402
import ph5_premia  # noqa: E402
import ph5_teams  # noqa: E402
from common import DISCOVERY_OUTPUT, POOLED_OUTPUT, topic_layer  # noqa: E402
from ph5_common import POSTHOC_COLUMNS  # noqa: E402
from variants import holm  # noqa: E402

ALPHA = 0.05
FLAGS = ("rq3", "s9", "e3")                                   # population flags of the outcome block
PRIMARY = ("E1", "P1b")
SIGN = {"E1": -1, "P1b": -1, "E4": +1, "P7": +1, "H1": +1, "A1": +1, "premia_b": +1, "premia_eb": +1}
MODULE = {"E1": "ph5_pivot", "P1b": "ph5_position", "E4": "ph5_pivot", "P7": "ph5_position", "H1": "ph5_teams",
          "A1": "ph5_kwtiming", "premia_b": "ph5_premia", "premia_eb": "ph5_premia"}
ESTIMAND = {"E1": "far jump: P(accept) at F_max p10 minus p50 (frozen REF)",
            "P1b": "novelty Q1 minus Q3 (Q0)",
            "E4": "within-author slope per +0.1 cos",
            "P7": "within-author slope per 10 novelty percentile points (2023-2026)",
            "H1": "one topic insider vs none (T1)",
            "A1": "Emerging (young x rising) minus Mainstream (old x flat) (Model A)",
            "premia_b": "slope b of the 2024-2026 confirmation premium on the raw 2018-2022 discovery premium (early "
                        "map); predicted 0 < b < 1",
            "premia_eb": "D0: mean squared error of the zero prediction minus that of the EB-shrunk discovery premium "
                         "as predictions of the centred confirmation premium (early map); predicted > 0"}
NULLS, N_REF, BOOT = ph5_position.NULLS, ph5_kwtiming.N_REF, ph5_premia.BOOT          # 200, 200, 999
E1_NULL_SEED = 20261018                                       # E1's calibrated p (P7 uses ph5_position.SEED)
REGISTERED_UNIT = "early"
DISCOVERY_WINDOWS = DISCOVERY_OUTPUT / "posthoc" / "ph5_premia" / "windows.csv"
DISCOVERY_WINDOWS_SHA256 = "7d79df7ac3ebb62c82f2cf6703e19e479bd6fe28ce1a8df135f144399b548347"
DISCOVERY_EFFECT = {"E1": -0.054, "P1b": -0.033}             # the discovery estimates (pp / 100): calibration plants
MULTS = (0.5, 1.0, 1.5, 2.0, 3.0)
CALIBRATION = POOLED_OUTPUT / "ph5_confirm" / "calibration.json"
NOT_REGISTERED = "not registered for confirmation"
ONE_SIDED = ("one-sided: p / 2 if the estimate has the predicted sign, else 1 - p / 2 (p: the test's declared "
             "two-sided p)")
STATUS = ("pre-registered out-of-sample replication on the released former-holdout papers (not an untouched "
          "independent holdout)")
REGISTERED = {
    "status": STATUS,
    "features": "built on discovery + confirmation papers with the frozen PH5 code (pooled histories, novelty against "
                "all earlier pooled papers, pooled cell percentiles, pooled twins, pooled keyword_year; frozen centring "
                "mean, ph5_pivot.REF and keyword vocabulary); populations restricted to confirmation papers (D14)",
    "one_sided_rule": ONE_SIDED,
    "primary": {"tests": list(PRIMARY), "correction": "Holm over the two one-sided p", "alpha": ALPHA,
                "E1": {"sign": -1, "population": "confirmation RQ3 decided papers 2023-2026 with >= 1 experienced author",
                       "p": "max(CR1 by topic t(G - 1), calibrated p from 200 simulated nulls on the same papers: "
                            "Bernoulli of the topic x year acceptance rate, seed 20261018)",
                       "code": "ph5_pivot.declared"},
                "P1b": {"sign": -1, "population": "confirmation RQ3 decided papers 2019-2026",
                        "p": "CR1 by topic, t(G - 1)", "code": "ph5_position.declared"}},
    "secondary": {"family": "none (each one-sided at 0.05, reported)",
                  "E4": {"sign": 1, "p": "CR1 (author FE in the small-sample factor); two-way reported"},
                  "P7": {"sign": 1, "p": "max(CR1, two-way, calibrated p from 200 nulls)"},
                  "H1": {"sign": 1, "p": "CR1 by topic, t(G - 1)"},
                  "A1": {"sign": 1, "p": "two-way (keyword, topic), t(min G - 1)",
                         "reading": "also one-sided p over 200 null frames < 0.05"},
                  "premia_b": {"prediction": "0 < b < 1", "p": "intersection-union of two one-sided t(m - 2) HC3 tests",
                               "units": "early map; discovery window units with >= 15 decided confirmation papers "
                                        "2024-2026", "discovery": "output/posthoc/ph5_premia/windows.csv (sha256 "
                                        + DISCOVERY_WINDOWS_SHA256 + ")"},
                  "premia_eb": {"sign": 1, "statistic": "D0 = mean(y^2) - mean((y - eb1)^2), y centred",
                                "p": "one-sided paired t(U - 1) of the squared-error differences",
                                "reading": "the EB-shrunk discovery premium beats the no-information prediction 0; "
                                           "without persistence E[D0] < 0"}},
    "not_registered": ["E2", "E3", "P1a", "P2", "P3", "P4", "P5", "P6", "teams H2", "premia k100 / keywords / areas",
                       "premia D = mse(raw) - mse(EB) (descriptive)"],
}


def need(ok: bool, message: str) -> None:
    if not ok:
        raise SystemExit(message)


def one_sided(p: float, coef: float, sign: int) -> float:
    """p1 = p / 2 if the estimate has the predicted sign, else 1 - p / 2; missing stays missing (= run_confirmation's)."""
    if not (np.isfinite(p) and np.isfinite(coef)):
        return np.nan
    return float(p / 2 if np.sign(coef) == sign else 1 - p / 2)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean(o):
    """JSON-safe copy: numpy scalars to Python, non-finite floats to None (as run_frozen.clean)."""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple, np.ndarray)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


# ---------------------------------------------------------------------------------------------------- the pooled frame
def confirmation_mask(k: pd.DataFrame) -> np.ndarray:
    """The confirmation papers of the pooled frame, from the pooled corpus's split column (pooled corpus only)."""
    corpus = topic_layer().embedded_corpus()
    need(common.CORPUS == "pooled" and "split" in corpus, "the PH5 confirmation needs ICLR_CORPUS=pooled")
    need((corpus.submission_id.to_numpy() == k.submission_id.to_numpy()).all(), "the pooled frame is not in corpus order")
    return corpus.split.eq("confirmation").to_numpy()


def pooled_frame(conf: pd.DataFrame, out: pd.DataFrame, check_split: bool = True) -> tuple[pd.DataFrame, np.ndarray]:
    """The pooled k100 frame (every paper, panel order) with the outcome block of the confirmation papers attached;
    every other paper is outside every population (rq3, s9, e3 False; outcomes missing). Returns (frame, mask of the
    confirmation papers). check_split: the papers of `conf` must be exactly the pooled corpus's confirmation split
    (tests on the discovery corpus pass False and a stand-in subset)."""
    k = panel.frame("k100").reset_index(drop=True)
    ids = conf.submission_id.reset_index(drop=True)
    need(out.submission_id.reset_index(drop=True).equals(ids), "the outcome block is not aligned with the frame")
    mask = k.submission_id.isin(set(ids)).to_numpy()
    need(int(mask.sum()) == len(ids) == ids.nunique(), "the confirmation frame is not a set of pooled papers")
    need((k.submission_id.to_numpy()[mask] == ids.to_numpy()).all(), "the confirmation frame is not in pooled order")
    if check_split:
        need(np.array_equal(confirmation_mask(k), mask), "the frame's papers are not the confirmation split")
    o = out.reset_index(drop=True)
    block = {}
    for c in POSTHOC_COLUMNS:
        v = np.zeros(len(k), bool) if c in FLAGS else np.full(len(k), np.nan)
        v[mask] = o[c].to_numpy(bool if c in FLAGS else float)
        block[c] = v
    return k.assign(**block), mask


def free(k: pd.DataFrame) -> pd.DataFrame:
    """k without its outcome block (the modules' prepare() then adds no outcome-based column)."""
    return k.drop(columns=[c for c in POSTHOC_COLUMNS if c in k])


def attach(prepared: pd.DataFrame, k: pd.DataFrame) -> pd.DataFrame:
    """A module's prepared frame (panel order) with k's outcome block."""
    need((prepared.submission_id.to_numpy() == k.submission_id.to_numpy()).all(), "prepared frame out of order")
    return prepared.assign(**{c: k[c].to_numpy() for c in POSTHOC_COLUMNS})


# ---------------------------------------------------------------------------------------------------- the PH5 tests
def e1_null_t(d: pd.DataFrame, rng: np.random.Generator, draws: int = NULLS) -> np.ndarray:
    """E1's t under `draws` simulated nulls on the same papers (d: ph5_pivot.declared's design): accepted ~
    Bernoulli(the paper's topic x year acceptance rate), so nothing but the cell predicts acceptance (P7's null,
    ph5_position.calibrated_p). NaN where E1 is not identified."""
    rate = d.groupby("cell").accepted.transform("mean").to_numpy(float)
    Y = rng.random((len(d), draws)) < rate[:, None]
    t = np.full(draws, np.nan)
    for s in range(draws):
        e = ph5_pivot.p1(d.assign(accepted=Y[:, s].astype(float)))[0]["E1"]
        t[s] = e["coef"] / e["se"] if np.isfinite(e["se"]) and e["se"] > 0 else np.nan
    return t


def pivot_part(k: pd.DataFrame, nulls: int = NULLS) -> tuple[pd.DataFrame, dict]:
    """ph5_pivot's declared E1-E4 on the confirmation papers (E1 and E4 registered; E2, E3 not), and E1's calibrated p
    from `nulls` simulated nulls: p_calibrated = (1 + #{|t_null| >= |t|}) / (nulls + 1), p_used = max(CR1 p,
    p_calibrated) (= the CR1 p when nulls = 0)."""
    kp = attach(ph5_pivot.prepare(free(k)), k)
    _, ar = ph5_pivot.features()
    pop = ph5_pivot.population(kp)
    rows, _, d = ph5_pivot.declared(pop, ar)
    rows = rows.drop(columns="p_holm").assign(confirmation_test=lambda r: r.test.where(r.test.isin(["E1", "E4"]),
                                                                                         NOT_REGISTERED))
    rows["p_used"] = rows.p
    i = rows.index[rows.test == "E1"][0]
    if nulls:
        tn = e1_null_t(d, np.random.default_rng(E1_NULL_SEED), nulls)
        ok, obs = np.isfinite(tn), abs(rows.at[i, "coef"] / rows.at[i, "se"]) if rows.at[i, "se"] > 0 else np.nan
        pc = float((1 + (np.abs(tn[ok]) >= obs).sum()) / (ok.sum() + 1)) if np.isfinite(obs) else np.nan
        rows.loc[i, ["p_calibrated", "null_t_sd", "null_frames"]] = [pc, float(np.std(tn[ok])), int(ok.sum())]
        rows.at[i, "p_used"] = max(rows.at[i, "p"], pc) if np.isfinite(pc) else np.nan
    return rows, {"papers": int(len(d)), "hot_share": float(d.hot.mean()), "acceptance_rate": float(d.accepted.mean()),
                  "n_exp": {str(c): int(v) for c, v in d.n_exp.clip(upper=4).value_counts().sort_index().items()},
                  "e1_calibration_nulls": nulls}


def position_part(k: pd.DataFrame, nulls: int = NULLS) -> tuple[pd.DataFrame, dict]:
    """ph5_position's Family 1 on the confirmation papers, calibrated p (P3-P7) from `nulls` simulated nulls (P1b and
    P7 registered; the others not)."""
    kq = attach(ph5_position.prepare(free(k)), k)
    d = ph5_position.design(ph5_position.population(kq))
    tests, _ = ph5_position.declared(d)
    if nulls:
        tests = ph5_position.calibrated_p(d, tests, np.random.default_rng(ph5_position.SEED), nulls)
    tests = tests.drop(columns="p_holm").assign(
        confirmation_test=lambda r: r.test.where(r.test.isin(["P1b", "P7"]), NOT_REGISTERED))
    return tests, {"papers": int(len(d)), "papers_by_year": d.groupby("year").size().to_dict(),
                   "acceptance_rate": float(d.accepted.mean()), "any_twin_share": float(d.any_twin.mean()),
                   "calibration_nulls": nulls}


def teams_part(k: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """ph5_teams T1 on the confirmation papers: H1 (registered) and H2 (not). Neither uses `proven` (T2's term), which
    ph5_teams.population computes from confirmation acceptances only."""
    d = ph5_teams.population(k)
    fam = ph5_teams.family_table(ph5_teams.fit_models(d, only=["T1"]), adjust=False).rename(columns={"estimate": "coef"})
    fam["confirmation_test"] = fam.test.where(fam.test == "H1", NOT_REGISTERED)
    n_ins = d.n_ins.clip(upper=ph5_teams.INS_CAP).astype(int)
    return fam, {"papers": int(len(d)), "acceptance_rate": float(d.accepted.mean()),
                 "papers_by_n_ins": n_ins.value_counts().sort_index().to_dict()}


def outcome_block(n: int, mask: np.ndarray, o: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    """rq3 and accepted for all n pooled papers from an outcome block of the confirmation papers (others outside)."""
    rq3, acc = np.zeros(n, bool), np.full(n, np.nan)
    rq3[mask], acc[mask] = o.rq3.to_numpy(bool), o.accepted.to_numpy(float)
    return rq3, acc


def kwtiming_part(k: pd.DataFrame, mask: np.ndarray, n_ref: int = N_REF) -> tuple[pd.DataFrame, dict]:
    """ph5_kwtiming Model A on the confirmation papers: A1 with its two-way p and the null-frame p over n_ref frames
    (decided set and acceptance of the confirmation papers from ph5_common.fake_outcomes, seeds 0..n_ref-1)."""
    kk = attach(ph5_kwtiming.prepare(free(k)), k)
    f, r = ph5_kwtiming.model_a(kk)
    a1 = f.lincom(ph5_kwtiming.A_TESTS["A1"])
    t = a1["coef"] / a1["se"] if a1["se"] > 0 else np.nan
    tn, bn = np.full(n_ref, np.nan), np.full(n_ref, np.nan)
    for s in range(n_ref):
        rq3, acc = outcome_block(len(kk), mask, ph5_common.fake_outcomes(kk[mask], s))
        e = ph5_kwtiming.model_a(kk.assign(rq3=rq3, accepted=acc))[0].lincom(ph5_kwtiming.A_TESTS["A1"])
        tn[s], bn[s] = (e["coef"] / e["se"] if e["se"] > 0 else np.nan), e["coef"]
    ok = np.isfinite(tn)
    row = {"test": "A1", "label": ph5_kwtiming.TESTS[0][2], **a1, "null_frames": int(ok.sum()),
           "p_null_frames": float((1 + (np.abs(tn[ok]) >= abs(t)).sum()) / (ok.sum() + 1)) if np.isfinite(t) else np.nan,
           "p_null_frames_one_sided": float((1 + (SIGN["A1"] * tn[ok] >= SIGN["A1"] * t).sum()) / (ok.sum() + 1))
           if np.isfinite(t) else np.nan,
           "size_in_null_frames": float(np.mean(np.abs(tn[ok]) >= stats.t.ppf(0.975, a1["dof"]))) if ok.any() else np.nan,
           "mde80_simulated": float((stats.t.ppf(0.975, a1["dof"]) + stats.t.ppf(0.8, a1["dof"])) * np.nanstd(bn, ddof=1))
           if ok.sum() > 1 else np.nan, "confirmation_test": "A1"}
    return pd.DataFrame([row]), {"use_rows": int(len(r)), "papers": int(r.i.nunique()),
                                 "uses_by_state": r.state.value_counts().sort_index().to_dict(), "null_frames": n_ref}


def discovery_windows() -> pd.DataFrame:
    """The committed discovery run's window premia (output/posthoc/ph5_premia/windows.csv, pinned by its sha256): the
    fixed predictions of the out-of-sample premia tests."""
    need(DISCOVERY_WINDOWS.exists() and sha256(DISCOVERY_WINDOWS) == DISCOVERY_WINDOWS_SHA256,
         f"{DISCOVERY_WINDOWS} is missing or not the committed discovery file")
    return pd.read_csv(DISCOVERY_WINDOWS, usecols=["unit_type", "unit", "w1", "v1", "eb1"])


def premia_stats(x: np.ndarray, vx: np.ndarray, eb: np.ndarray, y: np.ndarray, vy: np.ndarray, rng: np.random.Generator,
                 boot: int = BOOT, tail: float = 0.1) -> dict:
    """Out-of-sample premia statistics for aligned units: discovery raw (x, variance vx) and EB (eb) premia, confirmation
    premia y (variance vy). b: WLS slope of y on x, weights 1 / (vy + tau_y^2), HC3 SE, t(U - 2), with the one-sided p
    of b > 0 and of b < 1 and their intersection-union p; D: mean squared error of x minus that of eb as predictions of
    y centred at its 1/v-weighted mean, paired one-sided t(U - 1), weighted D and a unit-bootstrap CI (descriptive);
    D0: mean squared error of the prediction 0 minus that of eb (the registered EB test), with the same statistics;
    descriptive ph5_premia.winners on the same units."""
    U = len(x)
    if U < ph5_premia.MIN_UNITS:
        return {"units": U, "note": f"not estimable: {U} units (needs {ph5_premia.MIN_UNITS})"}
    ty = max(float(ph5_premia.dl(y[:, None], vy[:, None], np.ones((U, 1), bool), np.ones((1, U)))[0][0, 0]), 0.0)
    omega = 1 / (vy + ty)
    b, se, p2, dof = ph5_premia.wls_hc3(x, y, omega)
    q = stats.t.ppf(0.975, dof)
    p_pos, p_lt1 = float(stats.t.sf(b / se, dof)), float(stats.t.cdf((b - 1) / se, dof))
    centre = lambda yy, vv: yy - (yy / vv).sum() / (1 / vv).sum()  # noqa: E731
    yc = centre(y, vy)
    qD = stats.t.ppf(0.975, U - 1)

    def paired(d: np.ndarray, name: str) -> dict:
        m, sd = float(d.mean()), float(d.std(ddof=1))
        se = sd / np.sqrt(U)
        t = m / se if sd > 0 else np.nan
        return {name: m, f"{name}_se": se, f"{name}_ci95_lo": m - qD * se, f"{name}_ci95_hi": m + qD * se,
                f"{name}_p_one_sided": float(stats.t.sf(t, U - 1)) if np.isfinite(t) else np.nan,
                f"{name}_p_two_sided": float(2 * stats.t.sf(abs(t), U - 1)) if np.isfinite(t) else np.nan,
                f"{name}_weighted": float((omega * d).sum() / omega.sum())}

    d, d0 = (yc - x) ** 2 - (yc - eb) ** 2, yc ** 2 - (yc - eb) ** 2
    idx = rng.integers(0, U, (boot, U))
    Db, D0b = np.empty(boot), np.empty(boot)
    for j, i in enumerate(idx):
        c = centre(y[i], vy[i])
        Db[j], D0b[j] = ((c - x[i]) ** 2 - (c - eb[i]) ** 2).mean(), (c ** 2 - (c - eb[i]) ** 2).mean()
    shrink, retention, _ = ph5_premia.winners(x, vx, y, vy, tail, rng, boot)
    return {"units": U, "tau_w2_pp": np.sqrt(ty) * 100, "b": b, "b_se": se, "b_dof": dof, "b_p_two_sided": p2,
            "b_ci95_lo": b - q * se, "b_ci95_hi": b + q * se, "p_b_gt_0": p_pos, "p_b_lt_1": p_lt1,
            "p_iut": max(p_pos, p_lt1), **paired(d0, "D0"), "D0_boot_ci95": list(ph5_premia.pct(D0b)),
            **paired(d, "D"), "D_boot_ci95": list(ph5_premia.pct(Db)), "boot": boot,
            "mse_zero": float((yc ** 2).mean()), "mse_raw": float(((yc - x) ** 2).mean()),
            "mse_eb": float(((yc - eb) ** 2).mean()),
            "rho_w": shrink["rho_w"], "rho_w_ci95": [shrink["rho_w_ci95_lo"], shrink["rho_w_ci95_hi"]],
            "retention": retention}


def premia_part(k: pd.DataFrame, boot: int = BOOT) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Discovery 2018-2022 window premia (fixed, from the committed discovery run) against the 2024-2026 premia of the
    confirmation papers, per unit type (early map registered). Returns (statistics per unit type, unit table)."""
    sets, disc = ph5_premia.unit_sets(), discovery_windows()
    s = ph5_premia.sample(k, years=ph5_premia.W2)
    Y = ph5_premia.year_matrix(s.yi, len(ph5_premia.YEARS))
    stats_rows, units = [], []
    for j, ut in enumerate(ph5_premia.UNIT_TYPES):
        names, M = sets[ut]
        c = ph5_premia.cells(M[s.rows].T.tocsr(), Y, s.y)
        y, vy, ny = ph5_premia.window_premia(c, ph5_premia.W2)
        w = disc[disc.unit_type == ut].reset_index(drop=True)
        pos = pd.Series(np.arange(len(names)), index=names)
        need(w.unit.isin(pos.index).all(), f"discovery {ut} units missing from the pooled unit sets")
        i = pos[w.unit].to_numpy()
        ok = (ny[i] >= ph5_premia.MIN_CELL) & np.isfinite(vy[i]) & (vy[i] > 0) & np.isfinite(y[i])
        units.append(w.assign(w2=y[i], v2=vy[i], papers_w2=ny[i], used=ok))
        u = w[ok]
        r = premia_stats(u.w1.to_numpy(float), u.v1.to_numpy(float), u.eb1.to_numpy(float), y[i][ok], vy[i][ok],
                         np.random.default_rng([ph5_premia.SEED, 30 + j]), boot, ph5_premia.TAIL.get(ut, 0.1))
        stats_rows.append({"unit_type": ut, "registered": ut == REGISTERED_UNIT, "discovery_units": int(len(w)), **r})
    return pd.DataFrame(stats_rows), pd.concat(units, ignore_index=True)


# ---------------------------------------------------------------------------------------------------- verdicts
def verdict_row(test: str, r: dict | pd.Series, p_two: float, p_rule: str, extra: dict | None = None) -> dict:
    """One registered test: the estimate, its declared two-sided p made one-sided for the predicted sign, the verdict."""
    r = dict(r)
    coef = r.get("coef", np.nan)
    p1 = one_sided(p_two, coef, SIGN[test])
    return {"family": "primary" if test in PRIMARY else "secondary", "test": test, "module": MODULE[test],
            "estimand": ESTIMAND[test], "predicted_sign": SIGN[test], "coef": coef, "se": r.get("se", np.nan),
            "ci95_lo": r.get("ci95_lo", np.nan), "ci95_hi": r.get("ci95_hi", np.nan), "p_two_sided": p_two,
            "p_rule": p_rule, "p": p1, "n": r.get("n", r.get("rows", np.nan)), "clusters": r.get("clusters", np.nan),
            "dof": r.get("dof", np.nan), "note": r.get("note", ""), **(extra or {})}


def decide(rows: list[dict]) -> pd.DataFrame:
    """Holm over the primary family; verdicts (supported / not supported / not estimable)."""
    t = pd.DataFrame(rows)
    prim = t.family == "primary"
    t.loc[prim, "p_holm"] = holm(t.loc[prim, "p"].fillna(1.0)).to_numpy()
    def verdict(r) -> str:
        if not np.isfinite(r.p):
            return "not estimable"
        p = r.p_holm if r.family == "primary" else r.p
        ok = p < ALPHA and (0 < r.coef < 1 if r.test == "premia_b" else np.sign(r.coef) == r.predicted_sign)
        if r.test == "A1":
            ok = ok and r.p_null_frames_one_sided < ALPHA
        return "supported" if ok else "not supported"
    t["verdict"] = [verdict(r) for r in t.itertuples()]
    return t


def registered(piv: pd.DataFrame, pos: pd.DataFrame, tea: pd.DataFrame, kw: pd.DataFrame, prem: pd.DataFrame,
               nulls: int = NULLS) -> pd.DataFrame:
    """The registered rows: primary E1, P1b (Holm); secondary E4, P7, H1, A1, premia b and EB (early map)."""
    get = lambda t, name: t[t.test == name].iloc[0]  # noqa: E731
    e1, e4, p1b, p7, h1, a1 = (get(piv, "E1"), get(piv, "E4"), get(pos, "P1b"), get(pos, "P7"), get(tea, "H1"),
                               get(kw, "A1"))
    rows = [verdict_row("E1", e1, e1.p_used, "max(CR1 by topic t(G - 1), calibrated)" if nulls else
                        "CR1 by topic, t(G - 1); no calibrated p (nulls = 0)",
                        {"p_cr1": e1.p, "p_calibrated": e1.get("p_calibrated", np.nan)}),
            verdict_row("P1b", p1b, p1b.p_used, "CR1 by topic, t(G - 1) (p_used)"),
            verdict_row("E4", e4, e4.p, "CR1 by topic with the author FE in the small-sample factor, t(G - 1)",
                        {"p_twoway_one_sided": one_sided(e4.p_twoway, e4.coef, SIGN["E4"]), "papers": e4.papers}),
            verdict_row("P7", p7, p7.p_used, "max(CR1, two-way, calibrated)" if nulls else "max(CR1, two-way); no "
                        "calibrated p (nulls = 0)",
                        {"p_cr1": p7.p, "p_twoway": p7.p_twoway, "p_calibrated": p7.get("p_calibrated", np.nan),
                         "papers": p7.papers, "authors": p7.authors}),
            verdict_row("H1", h1, h1.p, "CR1 by topic, t(G - 1)", {"mde80_se": h1.mde80_se}),
            verdict_row("A1", a1, a1.p, "two-way (keyword, topic), t(min G - 1)",
                        {"p_null_frames_one_sided": a1.p_null_frames_one_sided, "p_null_frames": a1.p_null_frames,
                         "mde80_simulated": a1.mde80_simulated, "papers": a1.papers})]
    e = prem[prem.unit_type == REGISTERED_UNIT].iloc[0]
    if np.isfinite(e.get("b", np.nan)):
        rows.append({**verdict_row("premia_b", {"coef": e.b, "se": e.b_se, "ci95_lo": e.b_ci95_lo, "ci95_hi": e.b_ci95_hi,
                                                "n": e.units, "clusters": np.nan}, e.b_p_two_sided,
                                   "intersection-union: max(one-sided p of b > 0, one-sided p of b < 1), HC3, t(m - 2)",
                                   {"p_b_gt_0": e.p_b_gt_0, "p_b_lt_1": e.p_b_lt_1}), "p": e.p_iut})
        rows.append({**verdict_row("premia_eb", {"coef": e.D0, "se": e.D0_se, "ci95_lo": e.D0_ci95_lo,
                                                 "ci95_hi": e.D0_ci95_hi, "n": e.units, "clusters": np.nan},
                                   e.D0_p_two_sided, "D0 vs the zero prediction: paired t(U - 1) of the squared-error "
                                   "differences (Diebold-Mariano)",
                                   {"mse_zero": e.mse_zero, "mse_raw": e.mse_raw, "mse_eb": e.mse_eb,
                                    "D0_weighted": e.D0_weighted, "D_raw_minus_eb_descriptive": e.D,
                                    "D_p_one_sided_descriptive": e.D_p_one_sided}),
                     "p": e.D0_p_one_sided})
    else:
        rows += [verdict_row(t, {"note": e.get("note", "not estimable")}, np.nan, "") for t in ("premia_b", "premia_eb")]
    return decide(rows)


def calibration_record() -> dict | None:
    """The pre-run calibration (calibrate()), if it has been written: its MDE80, power and size, and its sha256."""
    if not CALIBRATION.exists():
        return None
    c = json.loads(CALIBRATION.read_text())
    return {"source": str(CALIBRATION.relative_to(common.ROOT)), "sha256": sha256(CALIBRATION),
            **{key: c[key] for key in ("mde80", "power_at_discovery_effect", "null_size", "family_any_holm_null")}}


def lines(tests: pd.DataFrame) -> list[str]:
    out = []
    for r in tests.itertuples():
        holm_ = f" p_holm {r.p_holm:.3g}" if r.family == "primary" else ""
        out.append(f"PH5 {r.family:9s} {r.test:9s} coef {r.coef:+.4f} CI95 [{r.ci95_lo:+.4f}, {r.ci95_hi:+.4f}] "
                   f"p1 {r.p:.3g} (two-sided {r.p_two_sided:.3g}){holm_} -> {r.verdict}")
    return out


def compute(frames: dict[str, pd.DataFrame], out: pd.DataFrame, nulls: int = NULLS, n_ref: int = N_REF,
            boot: int = BOOT, check_split: bool = True) -> dict:
    """The registered PH5 confirmation tests (module docstring) on the confirmation frame frames['k100'] and its outcome
    block out (run_confirmation.ph5_part). Primary tests fail loudly; a secondary part that cannot be estimated on the
    outcomes is reported as 'not estimable' with its error."""
    seconds, info = {}, {}
    t0 = time.time()
    k, mask = pooled_frame(frames["k100"], out, check_split)
    seconds["frame"] = time.time() - t0

    def timed(name: str, fn: Callable[[], tuple], soft: bool = False):
        t = time.time()
        try:
            res = fn()
        except (ValueError, IndexError, KeyError, ZeroDivisionError, RuntimeError, np.linalg.LinAlgError) as e:
            if not soft:
                raise
            res = None, {"error": repr(e)}
        seconds[name] = time.time() - t
        info[name] = res[1]
        return res[0]

    piv = timed("pivot", lambda: pivot_part(k, nulls))
    pos = timed("position", lambda: position_part(k, nulls))
    tea = timed("teams", lambda: teams_part(k), soft=True)
    kw = timed("kwtiming", lambda: kwtiming_part(k, mask, n_ref), soft=True)
    t = time.time()
    try:
        prem, prem_units = premia_part(k, boot)
    except (ValueError, IndexError, KeyError, ZeroDivisionError, RuntimeError, np.linalg.LinAlgError) as e:
        prem = pd.DataFrame([{"unit_type": REGISTERED_UNIT, "note": f"not estimable: {e!r}"}])
        prem_units = pd.DataFrame()
    seconds["premia"] = time.time() - t
    tea = tea if tea is not None else pd.DataFrame([{"test": "H1", "note": f"not estimable: {info['teams']['error']}"}])
    kw = kw if kw is not None else pd.DataFrame([{"test": "A1", "note": f"not estimable: {info['kwtiming']['error']}"}])
    for name, t_ in (("teams", tea), ("kwtiming", kw)):
        for c in ("coef", "se", "p", "p_twoway", "p_null_frames", "p_null_frames_one_sided", "mde80_simulated",
                  "mde80_se", "papers", "ci95_lo", "ci95_hi"):
            if c not in t_:
                t_[c] = np.nan
    tests = registered(piv, pos, tea, kw, prem, nulls)
    cal = calibration_record()
    if cal is not None:
        for h in PRIMARY:
            tests.loc[tests.test == h, "mde80_calibrated"] = cal["mde80"][h]["alpha_holm_first_step"]
            tests.loc[tests.test == h, "power_at_discovery_effect"] = cal["power_at_discovery_effect"][h]
    summary = {"status": STATUS, "registered": REGISTERED,
               "confirmation_papers": int(mask.sum()), "pooled_papers": int(len(k)),
               "decided_confirmation_papers": int(k.rq3.sum()),
               "verdicts": {r.test: {"family": r.family, "coef": r.coef, "p": r.p, "p_two_sided": r.p_two_sided,
                                     **({"p_holm": r.p_holm} if r.family == "primary" else {}), "verdict": r.verdict}
                            for r in tests.itertuples()},
               "populations": info, "premia": prem.drop(columns=["retention"], errors="ignore").to_dict("records"),
               "calibration": cal or "not computed (python research/fashion/ph5_confirm.py calibrate)",
               "seconds": {key: round(v, 1) for key, v in seconds.items()}, "lines": lines(tests),
               "note": "associations within the stated fixed effects, not causal effects"}
    return {"tests": tests, "pivot": piv, "position": pos, "teams": tea, "kwtiming": kw,
            "premia": prem.drop(columns=["retention"], errors="ignore"),
            "premia_retention": pd.DataFrame([{"unit_type": r["unit_type"], **x} for r in prem.to_dict("records")
                                              for x in (r["retention"] if isinstance(r.get("retention"), list) else [])]),
            "premia_units": prem_units, "summary": clean(summary)}


# ---------------------------------------------------------------------------------------------------- calibration
def unit_plants(kp: pd.DataFrame, kq: pd.DataFrame) -> dict[str, np.ndarray]:
    """Probability-scale plants of a unit effect whose LPM target is the registered contrast (panel order): E1, the
    frozen RCS curve ((B(F_max) - B(p50)) . c) / (c . c) with c = B(p10) - B(p50) (= 1 at p10, 0 at p50, linear beyond
    the outer knots; 0 without F_max); P1b, 1[nov_pct < 0.2] (0 without a percentile)."""
    ref = ph5_pivot.REF["F_max"]
    c = ph5_pivot.rcs(ref["p10"], ref["knots"])[0] - ph5_pivot.rcs(ref["p50"], ref["knots"])[0]
    f = kp.F_max.to_numpy(float)
    e1 = np.zeros(len(f))
    ok = np.isfinite(f)
    e1[ok] = (ph5_pivot.rcs(f[ok], ref["knots"]) - ph5_pivot.rcs(ref["p50"], ref["knots"])[0]) @ c / (c @ c)
    pct = kq.pct.to_numpy(float)
    return {"E1": e1, "P1b": np.where(np.isfinite(pct), (pct < 0.2).astype(float), 0.0)}


def base_rate(years: np.ndarray) -> np.ndarray:
    """ph5_common.fake_outcomes's year-specific base acceptance rate."""
    return pd.Series(years).map(ph5_pivot.BASE_RATES).fillna(0.4).to_numpy(float)


def primary_estimates(kp: pd.DataFrame, kq: pd.DataFrame, rq3: np.ndarray, acc: np.ndarray, p_true: np.ndarray,
                      which: tuple[str, ...] = PRIMARY) -> dict[str, dict]:
    """E1 and P1b (the registered code) on one outcome draw, with the target: the same model on the true probabilities."""
    out = {}
    if "E1" in which:
        pop = ph5_pivot.population(kp.assign(rq3=rq3, accepted=acc))
        e = ph5_pivot.p1(ph5_pivot.design(pop))[0]["E1"]
        tgt = ph5_pivot.p1(ph5_pivot.design(pop.assign(accepted=p_true[pop.index.to_numpy()])))[0]["E1"]["coef"]
        out["E1"] = {**e, "target": tgt}
    if "P1b" in which:
        d = ph5_position.design(ph5_position.population(kq.assign(rq3=rq3, accepted=acc)))
        xs = ph5_position.xs("Q0")
        e = ph5_position.Fit(d, "accepted", xs).lincom({"q1": 1.0})
        tgt = ph5_position.Fit(d.assign(accepted=p_true[d.index.to_numpy()]), "accepted", xs).lincom({"q1": 1.0})["coef"]
        out["P1b"] = {**e, "target": tgt}
    return out


def mde80(grid: list[float], power: list[float]) -> float | None:
    """Smallest effect with 80% detection, linearly interpolated over the grid (None if never reached; =
    run_confirmation.mde80)."""
    for i, (g, p) in enumerate(zip(grid, power)):
        if p >= 0.8:
            return float(g) if i == 0 else float(grid[i - 1] + (0.8 - power[i - 1]) * (g - grid[i - 1]) / (p - power[i - 1]))
    return None


def calibrate(nulls: int = 400, reps: int = 200, mults: tuple[float, ...] = MULTS, seed: int = 0,
              mask: np.ndarray | None = None) -> dict:
    """Size, power and MDE80 of E1 and P1b on simulated outcomes of the confirmation papers (module docstring). Null
    frames: both tests on the same frames (one-sided size at 0.05, two-sided size, any-Holm family rate, SD of the
    estimates vs the mean SE). Planted frames: each test with its own plant at mults x the discovery estimate, the
    other test not estimated. mask: the confirmation papers (default: the pooled corpus's split)."""
    k = panel.frame("k100").reset_index(drop=True)
    mask = confirmation_mask(k) if mask is None else mask
    kp, kq = ph5_pivot.prepare(free(k)), ph5_position.prepare(free(k))
    unit = unit_plants(kp, kq)
    base = base_rate(k.year.to_numpy())
    conf = k[mask]

    def draw(s: int, shift: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        p = np.clip(base + shift, 0.005, 0.995)
        lo = (logit(p) - logit(base))[mask]
        o = ph5_common.fake_outcomes(conf, s, planted=lambda _: lo)
        rq3, acc = outcome_block(len(k), mask, o)
        return rq3, acc, np.where(mask, p, np.nan)

    rows = []
    for i in range(nulls):
        s = seed * 10_000_000 + i
        est = primary_estimates(kp, kq, *draw(s, np.zeros(len(k))))
        rows += [{"test": h, "mult": 0.0, "frame": s, **e} for h, e in est.items()]
    for j, h in enumerate(PRIMARY):
        for m_i, m in enumerate(mults):
            for r in range(reps):
                s = seed * 10_000_000 + 1_000_000 * (j + 1) + 10_000 * (m_i + 1) + r
                est = primary_estimates(kp, kq, *draw(s, m * DISCOVERY_EFFECT[h] * unit[h]), which=(h,))
                rows.append({"test": h, "mult": m, "frame": s, **est[h]})
    r = pd.DataFrame(rows)
    r["p1"] = [one_sided(p, c, SIGN[t]) for p, c, t in zip(r.p, r.coef, r.test)]
    r["detect_05"], r["detect_holm"] = r.p1 < ALPHA, r.p1 < ALPHA / len(PRIMARY)
    r["covered"] = (r.ci95_lo <= r.target) & (r.target <= r.ci95_hi)
    per = (r.groupby(["test", "mult"]).agg(frames=("coef", "size"), mean_coef=("coef", "mean"), sd_coef=("coef", "std"),
                                           mean_se=("se", "mean"), mean_target=("target", "mean"),
                                           power_05=("detect_05", "mean"), power_holm=("detect_holm", "mean"),
                                           reject_two_sided=("p", lambda p: float((p < ALPHA).mean())),
                                           coverage=("covered", "mean")).reset_index())
    per["bias"] = per.mean_coef - per.mean_target
    nul = r[r.mult == 0].pivot(index="frame", columns="test", values="p1")
    fam = float(np.mean([(holm(row.fillna(1.0)) < ALPHA).any() for _, row in nul.iterrows()])) if len(nul) else None
    out = {"per_test": per.to_dict("records"), "family_any_holm_null": fam, "null_size": {},
           "power_at_discovery_effect": {}, "mde80": {}, "discovery_effect": DISCOVERY_EFFECT, "mults": list(mults),
           "nulls": nulls, "reps": reps, "seed": seed, "confirmation_papers": int(mask.sum()),
           "plants": {"E1": "delta x ((B(F_max) - B(p50)) . c) / (c . c), probability scale",
                      "P1b": "delta x 1[nov_pct < 0.2], probability scale"},
           "detection": "predicted sign and one-sided p < 0.05 / 2 (Holm's first step); also < 0.05"}
    for h in PRIMARY:
        g = per[per.test == h].sort_values("mult")
        grid = list(g.mean_target.abs())
        out["null_size"][h] = {"one_sided_05": float(g.power_05.iloc[0]), "one_sided_holm": float(g.power_holm.iloc[0]),
                               "two_sided_05": float(g.reject_two_sided.iloc[0]),
                               "sd_coef_over_mean_se": float(g.sd_coef.iloc[0] / g.mean_se.iloc[0])}
        at1 = g[g.mult == 1.0]
        out["power_at_discovery_effect"][h] = (float(at1.power_holm.iloc[0]) if len(at1) else None)
        out["mde80"][h] = {"alpha_holm_first_step": mde80(grid, list(g.power_holm)),
                           "alpha_05": mde80(grid, list(g.power_05)), "unit": "probability (target scale)"}
    return clean(out)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("what", choices=["calibrate"])
    p.add_argument("--nulls", type=int, default=400)
    p.add_argument("--reps", type=int, default=200)
    p.add_argument("--seed", type=int, default=0)
    a = p.parse_args()
    need(common.CORPUS == "pooled" and common.OUTPUT == POOLED_OUTPUT, "ph5_confirm.py needs ICLR_CORPUS=pooled")
    t = time.time()
    cal = calibrate(a.nulls, a.reps, seed=a.seed)
    cal["seconds"] = round(time.time() - t, 1)
    CALIBRATION.parent.mkdir(parents=True, exist_ok=True)
    need(DISCOVERY_OUTPUT not in CALIBRATION.parents, f"refusing to write into {CALIBRATION}")
    CALIBRATION.write_text(json.dumps(cal, indent=2) + "\n")
    print(json.dumps({key: cal[key] for key in ("null_size", "family_any_holm_null", "power_at_discovery_effect",
                                                "mde80", "seconds")}, indent=1))


if __name__ == "__main__":
    main()
