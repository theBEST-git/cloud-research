"""Dry-runs before the freeze (PREREGISTRATION.md D12, D13): size under nulls and power under planted effects.

No real RQ2 outcome is used (the label-based outcomes are replaced by simulated ones), and RQ3 uses only the sealed
loader's permuted and simulated modes. Results keep coefficients, p-values and verdicts only, never outcome means.

Scenarios (R replications each):
  rq2_null_k100 / rq2_null_early   simulated outcomes clustered on the k100 / early map, no effect
  rq2_power_m{0.5,1,2,3}           planted effect = multiple x SESOI on the main regressor, predicted direction
  rq3_permuted                     real populations, acceptance shuffled within year (loader's permuted mode)
  rq3_null_k100 / rq3_null_early   simulated acceptance clustered on the k100 / early map
  rq3_power_H3a_m* / rq3_power_H3b_m*   planted effect on maturity / maturity x method
Pass criteria (fixed before running): main-specification size at alpha = 0.05 within 2-8% for every hypothesis and null;
the full decision rule supports a hypothesis in at most 5% of null replications; at the largest planted effect it does
so in at least 80%. MDE80 = smallest planted effect with >= 80% support under the full rule (linear interpolation).

    python research/fashion/dryrun.py [--reps 200] [--power-reps 100] [--workers 4] [--only rq2,rq3]
Writes output/dryrun/<scenario>.csv and output/dryrun/summary.json.
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")                     # one BLAS thread per worker process

import argparse
import json
import multiprocessing as mp
import time
import zlib

import numpy as np
import pandas as pd

import outcomes
import panel
import rq2_following as rq2
import rq3_reward as rq3
from common import OUTPUT
from dgp import DGP, simulate

OUT = OUTPUT / "dryrun"
MULTS = (0.5, 1.0, 2.0, 3.0)
GATE = json.loads((OUTPUT / "h2d_validation.json").read_text())["gate"] == "pass"
FRAMES: dict[str, pd.DataFrame] = {}
BASE_RQ2 = {}                                  # marginal means of the RQ2 outcomes (no joint information)
KEEP = ["coef", "se", "p", "n", "clusters"]


def _frames() -> None:
    for m in panel.MAPS:
        FRAMES[m] = panel.frame(m)
    k = FRAMES["k100"]
    keyed = k[k.has_author_key & k.year.between(2019, 2026)]
    for c in ["incumbent", "incumbent_w2", "incumbent_s4", "method", "measurement", "buzzword"]:
        BASE_RQ2[c] = float(keyed[c].mean())


def _rq2_ys(seed: int, dgp_map: str, effects: dict[str, dict]) -> dict[str, pd.Series]:
    rng = np.random.default_rng(seed)
    f = FRAMES[dgp_map]
    ids = FRAMES["k100"].submission_id
    if dgp_map != "k100":                       # planted effects always use the main-map regressor
        f = f.assign(hot=FRAMES["k100"].hot.values, newcomer=FRAMES["k100"].newcomer.values)
    return {c: pd.Series(simulate(f, DGP(base=b, effects=effects.get(c, {})), rng), index=ids.values)
            for c, b in BASE_RQ2.items()}


def _summarise(res: dict, scenario: str, rep: int) -> list[dict]:
    rows = []
    for h, v in res["verdicts"].items():
        rows.append({"scenario": scenario, "rep": rep, "hypothesis": h, **{k: v[k] for k in ["coef", "se", "p", "p_holm", "n"]},
                     "predicted_sign": v["predicted_sign"], "robust": v["robustness_same_sign"],
                     "hindsight": v["hindsight_variants_same_sign"], "verdict": v["verdict"]})
    r = res["rows"]
    lg = r[r.variant == "logit"]
    for _, x in lg.iterrows():                  # logit variant p-values, for the logit's own size
        rows.append({"scenario": scenario, "rep": rep, "hypothesis": x.hypothesis + ":logit", "coef": x.coef, "se": x.se,
                     "p": x.p, "p_holm": np.nan, "n": x.n})
    return rows


def job(task: tuple) -> list[dict]:
    kind, scenario, rep, params = task
    seed = zlib.crc32(scenario.encode()) * 1000 + rep
    if kind == "rq2":
        ys = _rq2_ys(seed, params["map"], params.get("effects", {}))
        res = rq2.run(FRAMES, GATE, ys=ys, supplementary=False)
    else:
        ids = FRAMES["k100"].submission_id
        if params["mode"] == "permuted":
            out = outcomes.load("permuted", ids, seed=seed)
        else:
            f = FRAMES[params["map"]]
            out = outcomes.load("simulated", ids, seed=seed, frame=f.assign(**{c: FRAMES["k100"][c].values for c in
                                                                              ["maturity", "maturity_x_method"]}),
                                dgp=DGP(base=0.32, effects=params.get("effects", {})))
        res = rq3.run(FRAMES, out, GATE, supplementary=False)
    return _summarise(res, scenario, rep)


def tasks(reps: int, power_reps: int, only: set[str]) -> list[tuple]:
    t = []
    if "rq2" in only:
        for m in ["k100", "early"]:
            t += [("rq2", f"rq2_null_{m}", r, {"map": m}) for r in range(reps)]
        for mult in MULTS:
            eff = {"incumbent": {"hot": -mult * 0.02}, "method": {"newcomer": -mult * 0.02},
                   "measurement": {"newcomer": +mult * 0.01}}
            t += [("rq2", f"rq2_power_m{mult}", r, {"map": "k100", "effects": eff}) for r in range(power_reps)]
    if "rq3" in only:
        t += [("rq3", "rq3_permuted", r, {"mode": "permuted"}) for r in range(reps)]
        for m in ["k100", "early"]:
            t += [("rq3", f"rq3_null_{m}", r, {"mode": "simulated", "map": m}) for r in range(reps)]
        for h, col in [("H3a", "maturity"), ("H3b", "maturity_x_method")]:
            for mult in MULTS:
                t += [("rq3", f"rq3_power_{h}_m{mult}", r, {"mode": "simulated", "map": "k100",
                                                           "effects": {col: -mult * 0.01}}) for r in range(power_reps)]
    return t


def summarise(df: pd.DataFrame) -> dict:
    out = {"size": {}, "false_support": {}, "power": {}, "mde80": {}, "criteria": {}}
    conf = df[~df.hypothesis.str.contains(":")]
    for sc, g in df.groupby("scenario"):
        if "null" in sc or "permuted" in sc:
            out["size"][sc] = g.groupby("hypothesis").p.apply(lambda p: round(float((p < 0.05).mean()), 4)).to_dict()
            gc = conf[conf.scenario == sc]
            out["false_support"][sc] = gc.groupby("hypothesis").verdict.apply(lambda v: round(float((v == "supported").mean()), 4)).to_dict()
    sesoi = {"H2a": 0.02, "H2b": 0.02, "H2c": 0.01, "H3a": 0.01, "H3b": 0.01}
    for h in sesoi:
        curve = {}
        for mult in MULTS:
            sc = f"rq2_power_m{mult}" if h.startswith("H2") else f"rq3_power_{h}_m{mult}"
            g = conf[(conf.scenario == sc) & (conf.hypothesis == h)]
            if len(g):
                curve[mult] = {"full_rule": round(float((g.verdict == "supported").mean()), 4),
                               "main_p05_right_sign": round(float(((g.p < 0.05) & (np.sign(g.coef) == g.predicted_sign)).mean()), 4)}
        if not curve:
            continue
        out["power"][h] = curve
        xs = [m * sesoi[h] for m in curve]
        ys = [curve[m]["full_rule"] for m in curve]
        mde = None
        for i, (x, y) in enumerate(zip(xs, ys)):
            if y >= 0.8:
                mde = x if i == 0 else xs[i - 1] + (0.8 - ys[i - 1]) * (x - xs[i - 1]) / (y - ys[i - 1])
                break
        out["mde80"][h] = None if mde is None else round(float(mde), 4)
    sizes = [v for sc in out["size"].values() for h, v in sc.items() if ":" not in h]
    fs = [v for sc in out["false_support"].values() for v in sc.values()]
    top = [c[max(c)]["full_rule"] for c in out["power"].values()]
    out["criteria"] = {"main_size_within_2_8pct": bool(sizes and all(0.02 <= s <= 0.08 for s in sizes)),
                       "size_range": [min(sizes), max(sizes)] if sizes else None,
                       "false_support_at_most_5pct": bool(fs and all(v <= 0.05 for v in fs)),
                       "largest_effect_detected_80pct": bool(top and all(v >= 0.8 for v in top))}
    return out


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--reps", type=int, default=200)
    p.add_argument("--power-reps", type=int, default=100)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--only", default="rq2,rq3")
    a = p.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    _frames()
    todo = tasks(a.reps, a.power_reps, set(a.only.split(",")))
    t0, rows = time.time(), []
    with mp.get_context("fork").Pool(a.workers) as pool:
        for i, r in enumerate(pool.imap_unordered(job, todo, chunksize=2)):
            rows += r
            if (i + 1) % 50 == 0:
                print(f"{i + 1}/{len(todo)} jobs, {time.time() - t0:.0f}s", flush=True)
    df = pd.DataFrame(rows).sort_values(["scenario", "rep", "hypothesis"])
    for sc, g in df.groupby("scenario"):
        g.to_csv(OUT / f"{sc}.csv", index=False)
    prev = json.loads((OUT / "summary.json").read_text()) if (OUT / "summary.json").exists() else {}
    allrows = pd.concat([pd.read_csv(f) for f in sorted(OUT.glob("*.csv"))], ignore_index=True)
    s = summarise(allrows)
    s["runs"] = {**prev.get("runs", {}), a.only: {"reps": a.reps, "power_reps": a.power_reps, "jobs": len(todo),
                                                  "seconds": round(time.time() - t0)}}
    (OUT / "summary.json").write_text(json.dumps(s, indent=2) + "\n")
    print(json.dumps(s, indent=1))


if __name__ == "__main__":
    main()
