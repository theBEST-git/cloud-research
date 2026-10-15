"""Dry-runs before the freeze (PREREGISTRATION.md D12, D13, D16): size under nulls and power under planted effects.

Blinding: every RQ2 outcome-side column is simulated (rq2_following.SIMULATED; newcomer is derived from the simulated
incumbency), RQ3 uses only the sealed loader's simulated and permuted modes, and results keep coefficients, SEs,
p-values, sample sizes and verdicts only - never a mean of a real column.

Data-generating processes (D16):
- RQ2: each outcome's variance components (topic, year, topic trend, topic-year cell) are calibrated from that outcome's
  own topic-year cell means on k100 (dgp.calibrate; no regressor involved). Simulated incumbency is paper-level, so
  every map's variants see the same simulated newcomer.
- RQ3: no real acceptance information. Base 0.32, sd_topic 0.05, sd_year 0.03, and two settings for the components that
  drive the SE of a within-topic regressor: "lo" (sd_cell 0.02, sd_trend 0.004) and "hi" (sd_cell 0.04, sd_trend 0.016).
Scenarios:
  rq2_null_k100, rq2_null_early                      no effect; structure on the k100 / early map           (R)
  rq2_power_<H>_m<mult>                              one hypothesis planted at mult x SESOI, others null;
                                                     main specification of that hypothesis only             (P)
  rq2_fullrule_<H>_m<1.0|3.0>                        same, full decision rule with all counted variants     (F)
  rq3_permuted                                       real loader, whole derived block shuffled within year  (R)
  rq3_null_k100_lo, rq3_null_k100_hi, rq3_null_early_hi                                                     (R)
  rq3_power_<H>_m<mult>_hi (P), rq3_power_<H>_m<mult>_lo (P/2), rq3_fullrule_<H>_m<1.0|3.0>_hi (F)
Planted effects use the k100 regressor (H3b: the interaction centred on the mean method share, so H3a stays null).
The realised effect is the main-specification coefficient when the true probability is the outcome (so clipping is
accounted for). Detection = predicted sign and p < 0.05 / m in the main specification (m = family size: Bonferroni,
i.e. Holm's first step). MDE80 = realised effect at 80% detection, linearly interpolated over the multiples.
Criteria (fixed before running; D16): (a) main-specification size (two-sided p < 0.05) within [0.02, 0.08] for every
confirmatory hypothesis and null scenario; (b) the full decision rule supports a hypothesis in at most 5% of null
replications; (c) detection >= 80% at 3 x SESOI, otherwise the hypothesis is reported as underpowered.

    python research/fashion/dryrun.py [--reps 500] [--power-reps 200] [--full-reps 100] [--workers 4]
Clears and writes output/dryrun/: one CSV per scenario, provenance.json (code and input digest), summary.json.
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")                     # one BLAS thread per worker process

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import multiprocessing as mp  # noqa: E402
import shutil  # noqa: E402
import time  # noqa: E402
import zlib  # noqa: E402
from dataclasses import asdict, replace  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import outcomes  # noqa: E402
import panel  # noqa: E402
import rq2_following as rq2  # noqa: E402
import rq3_reward as rq3  # noqa: E402
from analysis import estimate  # noqa: E402
from common import OUTPUT, ROOT  # noqa: E402
from dgp import DGP, calibrate, simulate  # noqa: E402

HERE = Path(__file__).resolve().parent
OUT = OUTPUT / "dryrun"
MULTS = (0.5, 1.0, 1.5, 2.0, 3.0)
GATE = json.loads((OUTPUT / "h2d_validation.json").read_text())["gate"] == "pass"
RQ2_SPECS = {s.hid: s for s in rq2.SPECS if not s.gated or GATE}
RQ3_SPECS = {s.hid: s for s in rq3.SPECS if not s.gated or GATE}
PLANT = {"H2a": ("incumbent", "hot"), "H2b": ("method", "newcomer"), "H2c": ("measurement", "newcomer"),
         "H3a": ("accepted", "maturity"), "H3b": ("accepted", "maturity_x_method_c")}
RQ3_DGP = {"lo": DGP(base=0.32, sd_topic=0.05, sd_year=0.03, sd_cell=0.02, sd_trend=0.004),
           "hi": DGP(base=0.32, sd_topic=0.05, sd_year=0.03, sd_cell=0.04, sd_trend=0.016)}
CODE = ["analysis.py", "ols.py", "logit.py", "dgp.py", "panel.py", "variants.py", "outcomes.py", "rq2_following.py",
        "rq3_reward.py", "rq1_rise.py", "common.py", "topic_maturity.py", "dryrun.py"]
INPUTS = ["paper_variables.csv.gz", "paper_buzzword.csv.gz", "earlier_versions.csv.gz", "topic_year_maturity.csv.gz",
          "h2d_validation.json"]
FRAMES: dict[str, pd.DataFrame] = {}
CAL: dict[str, DGP] = {}


def digest() -> dict:
    """sha256 of the code and inputs the dry-run uses; freeze.py refuses a dry-run whose digest is not current."""
    files = [HERE / c for c in CODE] + [OUTPUT / i for i in INPUTS] + [ROOT / "research/topics/common.py"]
    per = {str(f.relative_to(ROOT)): outcomes.sha256(f) for f in files}
    return {"files": per, "combined": hashlib.sha256(json.dumps(per, sort_keys=True).encode()).hexdigest()}


def _setup() -> None:
    for m in panel.MAPS:
        FRAMES[m] = panel.frame(m)
    k = FRAMES["k100"]
    FRAMES["k100"] = k.assign(maturity_x_method_c=k.maturity * (k.method - k.method.mean()))
    keyed = k[k.has_author_key]
    for c in ["incumbent", "method", "measurement", "buzzword", "lists_hot"]:      # one column at a time (D16)
        CAL[c] = calibrate(keyed, c, (2019, 2026))


def rq2_outcomes(seed: int, dgp_map: str, planted: str | None, delta: float) -> tuple[dict, dict]:
    """Simulated RQ2 outcome-side columns (all of rq2_following.SIMULATED) and the true probabilities."""
    rng = np.random.default_rng(seed)
    k, f = FRAMES["k100"], FRAMES[dgp_map].assign(hot=FRAMES["k100"].hot.values)
    ids = k.submission_id.values
    eff = lambda h: {PLANT[h][1]: delta} if planted == h else {}
    inc, p_inc = simulate(f, replace(CAL["incumbent"], effects=eff("H2a")), rng, return_p=True)
    f = f.assign(newcomer=1 - inc)
    meth, p_meth = simulate(f, replace(CAL["method"], effects=eff("H2b")), rng, return_p=True)
    meas, p_meas = simulate(f, replace(CAL["measurement"], effects=eff("H2c")), rng, return_p=True)
    buzz = simulate(f, CAL["buzzword"], rng)
    lists = simulate(f, CAL["lists_hot"], rng)
    keep = rng.random(len(inc))
    ys = {"incumbent": inc, "incumbent_w2": inc * (keep < 0.8), "incumbent_s4": inc * (keep < 0.995), "method": meth,
          "measurement": meas, "buzzword": buzz * lists, "lists_hot": lists}
    ys = {c: pd.Series(v, index=ids) for c, v in ys.items()}
    return ys, {"incumbent": p_inc, "method": p_meth, "measurement": p_meas}


def realised(pop: pd.DataFrame, spec, p: np.ndarray, ids: np.ndarray) -> float:
    """Main-specification coefficient with the true probability as the outcome: the effect actually planted."""
    d = pop.assign(**{spec.y: pd.Series(p, index=ids).reindex(pop.submission_id).to_numpy()})
    return estimate(d, spec.y, spec.x, spec.controls, spec.fe, spec.years)["coef"]


def rows_of(res: dict, scenario: str, rep: int, planted: str | None, eff: float | None) -> list[dict]:
    out = []
    for h, v in res["verdicts"].items():
        out.append({"scenario": scenario, "rep": rep, "hypothesis": h, "planted": planted == h,
                    "realised_effect": eff if planted == h else np.nan, "coef": v["coef"], "se": v["se"], "p": v["p"],
                    "p_holm": v["p_holm"], "n": v["n"], "predicted_sign": v["predicted_sign"],
                    "robust": v["robustness_same_sign"], "hindsight": v["hindsight_variants_same_sign"],
                    "verdict": v["verdict"]})
    for _, x in res["rows"][res["rows"].variant == "logit"].iterrows():
        out.append({"scenario": scenario, "rep": rep, "hypothesis": x.hypothesis + ":logit", "coef": x.coef, "se": x.se,
                    "p": x.p, "n": x.n})
    return out


def main_only(pop: pd.DataFrame, spec, scenario: str, rep: int, eff: float) -> list[dict]:
    """Power replications: the planted hypothesis's main specification only (MDE80 needs nothing else)."""
    r = estimate(pop, spec.y, spec.x, spec.controls, spec.fe, spec.years)
    return [{"scenario": scenario, "rep": rep, "hypothesis": spec.hid, "planted": True, "realised_effect": eff,
             "coef": r["coef"], "se": r["se"], "p": r["p"], "n": r["n"], "predicted_sign": spec.sign}]


def job(task: tuple) -> list[dict]:
    kind, scenario, rep, params = task
    seed = zlib.crc32(scenario.encode()) * 1000 + rep
    planted, mult, full = params.get("planted"), params.get("mult", 0.0), params.get("full", True)
    ids = FRAMES["k100"].submission_id
    if kind == "rq2":
        s = RQ2_SPECS.get(planted)
        delta = s.sign * mult * s.sesoi if s else 0.0
        ys, ps = rq2_outcomes(seed, params["map"], planted, delta)
        eff = None
        if s:
            pop = rq2.population(rq2.with_columns(FRAMES["k100"], ys))
            eff = realised(pop, s, ps[s.y], ids.values)
            if not full:
                return main_only(pop, s, scenario, rep, eff)
        res = rq2.run(FRAMES, GATE, ys=ys, supplementary=False)
        return rows_of(res, scenario, rep, planted, eff)
    if params["mode"] == "permuted":
        out = outcomes.load("permuted", ids, seed=seed)
        return rows_of(rq3.run(FRAMES, out, GATE, supplementary=False), scenario, rep, None, None)
    s = RQ3_SPECS.get(planted)
    base = RQ3_DGP[params["dgp"]]
    dgp = replace(base, effects={PLANT[planted][1]: s.sign * mult * s.sesoi}) if s else base
    f = FRAMES[params["map"]].assign(**{c: FRAMES["k100"][c].values for c in ["maturity", "maturity_x_method_c"]})
    y, p = simulate(f, dgp, np.random.default_rng(seed), return_p=True)
    out = outcomes.load("simulated", ids, seed=seed, frame=f, dgp=base)       # populations; outcome replaced below
    out["accepted"] = np.where(out.rq3, y, np.nan)
    out["s9_accepted"] = np.where(out.rq3, y, np.where(out.s9, 0.0, np.nan))
    eff = None
    if s:
        pop = rq3.attach(FRAMES["k100"], out)
        pop = pop[pop.rq3]
        eff = realised(pop, s, p, ids.values)
        if not full:
            return main_only(pop, s, scenario, rep, eff)
    res = rq3.run(FRAMES, out, GATE, supplementary=False)
    return rows_of(res, scenario, rep, planted, eff)


def tasks(reps: int, power_reps: int, full_reps: int) -> list[tuple]:
    t = []
    for m in ["k100", "early"]:
        t += [("rq2", f"rq2_null_{m}", r, {"map": m}) for r in range(reps)]
    for h in RQ2_SPECS:
        for mult in MULTS:
            t += [("rq2", f"rq2_power_{h}_m{mult}", r, {"map": "k100", "planted": h, "mult": mult, "full": False})
                  for r in range(power_reps)]
        for mult in (1.0, 3.0):
            t += [("rq2", f"rq2_fullrule_{h}_m{mult}", r, {"map": "k100", "planted": h, "mult": mult}) for r in range(full_reps)]
    t += [("rq3", "rq3_permuted", r, {"mode": "permuted"}) for r in range(reps)]
    for m, d in [("k100", "lo"), ("k100", "hi"), ("early", "hi")]:
        t += [("rq3", f"rq3_null_{m}_{d}", r, {"mode": "simulated", "map": m, "dgp": d}) for r in range(reps)]
    for h in RQ3_SPECS:
        for mult in MULTS:
            for d, n in [("hi", power_reps), ("lo", power_reps // 2)]:
                t += [("rq3", f"rq3_power_{h}_m{mult}_{d}", r, {"mode": "simulated", "map": "k100", "dgp": d,
                                                                "planted": h, "mult": mult, "full": False}) for r in range(n)]
        for mult in (1.0, 3.0):
            t += [("rq3", f"rq3_fullrule_{h}_m{mult}_hi", r, {"mode": "simulated", "map": "k100", "dgp": "hi",
                                                               "planted": h, "mult": mult}) for r in range(full_reps)]
    return t


def mde80(curve: list[tuple[float, float]]) -> float | None:
    """curve: (realised effect, detection rate) by increasing multiple; linear interpolation at 0.8."""
    for i, (x, y) in enumerate(curve):
        if y >= 0.8:
            if i == 0:
                return x
            x0, y0 = curve[i - 1]
            return x0 + (0.8 - y0) * (x - x0) / (y - y0)
    return None


def summarise(df: pd.DataFrame) -> dict:
    conf = df[~df.hypothesis.str.contains(":")].copy()
    fam = {"rq2": len(RQ2_SPECS), "rq3": len(RQ3_SPECS)}
    conf["m"] = np.where(conf.hypothesis.str.startswith("H2"), fam["rq2"], fam["rq3"])
    conf["detected"] = (conf.p < 0.05 / conf.m) & (np.sign(conf.coef) == conf.predicted_sign)
    out = {"size": {}, "false_support": {}, "logit_size": {}, "power": {}, "mde80": {}, "mde80_lo": {}}
    nulls = [sc for sc in df.scenario.unique() if "null" in sc or "permuted" in sc]
    for sc in nulls:
        g = conf[conf.scenario == sc]
        out["size"][sc] = g.groupby("hypothesis").p.apply(lambda p: round(float((p < 0.05).mean()), 4)).to_dict()
        out["false_support"][sc] = g.groupby("hypothesis").verdict.apply(lambda v: round(float((v == "supported").mean()), 4)).to_dict()
        lg = df[(df.scenario == sc) & df.hypothesis.str.endswith(":logit")]
        if len(lg):
            out["logit_size"][sc] = lg.groupby("hypothesis").p.apply(lambda p: round(float((p < 0.05).mean()), 4)).to_dict()
    for h in list(RQ2_SPECS) + list(RQ3_SPECS):
        for tag, key in ([("", "mde80")] if h.startswith("H2") else [("_hi", "mde80"), ("_lo", "mde80_lo")]):
            curve, table = [], {}
            for mult in MULTS:
                sc = f"rq{2 if h.startswith('H2') else 3}_power_{h}_m{mult}{tag}"
                g = conf[(conf.scenario == sc) & (conf.hypothesis == h)]
                if not len(g):
                    continue
                det = float(g.detected.mean())
                eff = float(g.realised_effect.mean())
                curve.append((abs(eff), det))
                table[str(mult)] = {"realised_effect": round(eff, 5), "detected_alpha_over_m": round(det, 4),
                                    "main_p05_right_sign": round(float(((g.p < 0.05) & (np.sign(g.coef) == g.predicted_sign)).mean()), 4),
                                    "reps": int(len(g))}
                fr = conf[(conf.scenario == sc.replace("_power_", "_fullrule_")) & (conf.hypothesis == h)]
                if len(fr):
                    table[str(mult)]["full_rule"] = round(float((fr.verdict == "supported").mean()), 4)
                    table[str(mult)]["full_rule_reps"] = int(len(fr))
            if table:
                out["power"][h + tag] = table
                v = mde80(curve)
                out[key][h] = None if v is None else round(v, 5)
    sizes = [v for sc in out["size"].values() for v in sc.values()]
    fs = [v for sc in out["false_support"].values() for v in sc.values()]
    top = {h: t[str(MULTS[-1])]["detected_alpha_over_m"] for h, t in out["power"].items() if not h.endswith("_lo")}
    out["criteria"] = {
        "a_size_within_2_8pct": bool(sizes) and all(0.02 <= s <= 0.08 for s in sizes),
        "a_size_range": [min(sizes), max(sizes)] if sizes else None,
        "a_size_violations": {sc: {h: v for h, v in d.items() if not 0.02 <= v <= 0.08} for sc, d in out["size"].items()
                              if any(not 0.02 <= v <= 0.08 for v in d.values())},
        "b_false_support_at_most_5pct": bool(fs) and all(v <= 0.05 for v in fs),
        "c_detected_80pct_at_3x_sesoi": {h: v >= 0.8 for h, v in top.items()},
    }
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--reps", type=int, default=500)
    p.add_argument("--power-reps", type=int, default=200)
    p.add_argument("--full-reps", type=int, default=100)
    p.add_argument("--workers", type=int, default=4)
    a = p.parse_args()
    if OUT.exists():
        shutil.rmtree(OUT)                              # never mix scenarios from different code (D16)
    OUT.mkdir(parents=True)
    prov = digest()
    _setup()
    prov["calibrated_rq2_dgp"] = {c: {k: round(v, 5) for k, v in asdict(d).items() if k != "effects"} for c, d in CAL.items()}
    prov["rq3_dgp"] = {k: {kk: vv for kk, vv in asdict(d).items() if kk != "effects"} for k, d in RQ3_DGP.items()}
    prov["reps"], prov["power_reps"], prov["full_reps"] = a.reps, a.power_reps, a.full_reps
    todo = tasks(a.reps, a.power_reps, a.full_reps)
    t0, rows = time.time(), []
    with mp.get_context("fork").Pool(a.workers) as pool:
        for i, r in enumerate(pool.imap_unordered(job, todo, chunksize=4)):
            rows += r
            if (i + 1) % 500 == 0:
                print(f"{i + 1}/{len(todo)} jobs, {time.time() - t0:.0f}s", flush=True)
    df = pd.DataFrame(rows).sort_values(["scenario", "rep", "hypothesis"])
    for sc, g in df.groupby("scenario"):
        g.to_csv(OUT / f"{sc}.csv", index=False)
    prov["jobs"], prov["seconds"] = len(todo), round(time.time() - t0)
    (OUT / "provenance.json").write_text(json.dumps(prov, indent=2) + "\n")
    s = summarise(df)
    s["code_digest"] = prov["combined"]
    (OUT / "summary.json").write_text(json.dumps(s, indent=2) + "\n")
    print(json.dumps({k: s[k] for k in ["criteria", "mde80", "mde80_lo"]}, indent=1))


if __name__ == "__main__":
    main()
