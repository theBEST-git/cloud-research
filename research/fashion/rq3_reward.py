"""RQ3 (reward): is following rewarded with acceptance? Implements PREREGISTRATION.md RQ3, D7, D8, R1, S1, S5-S7, S9, S10.

Population: registered RQ3 filter (outcomes.py), years 2018-2026; linear probability models of `accepted` with topic FE,
year dummies, contribution-class dummies (reference method) and the foundation-model dummy; SE clustered by topic.
  H3a  accepted ~ maturity                          predicted < 0
  H3b  accepted ~ maturity x method (+ maturity)    predicted < 0
  H3c  accepted ~ buzzword, 2019-2026               predicted < 0, only if the D6 gate passed (D10)
Counted variants: variants.RQ3 (nine shared + logit + R1 no probable earlier version).
"""
from __future__ import annotations

import pandas as pd

import variants
from analysis import Spec, decide, fit
from panel import CLASS_CONTROLS
from rq2_following import NEK, with_columns

BASE = tuple(CLASS_CONTROLS) + ("fm",)
SPECS = [
    Spec("H3a", "accepted", "maturity", -1, 0.01, "topic+year", (2018, 2026), BASE),
    Spec("H3b", "accepted", "maturity_x_method", -1, 0.01, "topic+year", (2018, 2026), ("maturity",) + BASE),
    Spec("H3c", "accepted", "buzzword", -1, 0.02, "topic+year", (2019, 2026), BASE, gated=True),
]
OUTCOME_COLUMNS = ["rq3", "accepted", "s9", "s9_accepted", "e3", "withdrawn_after_review", "withdrawn_before_review"]


def attach(frame: pd.DataFrame, out: pd.DataFrame) -> pd.DataFrame:
    """Frame with outcome columns from outcomes.load (aligned by submission_id)."""
    assert frame.submission_id.reset_index(drop=True).equals(out.submission_id.reset_index(drop=True))
    df = with_columns(frame, None)
    for c in OUTCOME_COLUMNS:
        df[c] = out[c].to_numpy()
    return df


def run(frames: dict[str, pd.DataFrame], out: pd.DataFrame, gate: bool, supplementary: bool = True,
        describe: bool = False) -> dict:
    """describe=True (frozen real run only) adds sample means to the main estimates."""
    specs = [s for s in SPECS if not s.gated or gate]
    full = {m: attach(f, out) for m, f in frames.items()}
    pop = {m: f[f.rq3] for m, f in full.items()}
    main = {s.hid: fit(pop["k100"], s, describe=describe) for s in specs}
    counted = {s.hid: {} for s in specs}
    rows = [{"hypothesis": h, "variant": "main", "kind": "main", **r} for h, r in main.items()]
    for name, v in variants.counted(3).items():
        d = variants.apply(pop[v.map], v)
        for s in specs:
            r = fit(d, s, v.estimator)
            counted[s.hid][name] = r
            rows.append({"hypothesis": s.hid, "variant": name, "kind": "counted", **r})
    supp = {s.hid: {} for s in specs}
    if supplementary:
        k = pop["k100"]
        by = {s.hid: s for s in specs}
        add = lambda h, name, r: (supp[h].__setitem__(name, r), rows.append({"hypothesis": h, "variant": name, "kind": "supplementary", **r}))
        s9 = full["k100"][full["k100"].s9].assign(accepted=lambda d: d.s9_accepted)
        for s in specs:
            add(s.hid, "S1_log_team", fit(k, s, extra_controls=("log_team",)))
            if "fine" in pop:
                add(s.hid, "S5_fine", fit(pop["fine"], s))
            add(s.hid, "S9_withdrawn_after_review_as_rejected", fit(s9, s))
            add(s.hid, "S10_newcomer_control", fit(k, s, extra_controls=("newcomer",)))
        if "H3c" in by:
            add("H3c", "S6_lists_hot_keyword", fit(k[k.lists_hot == 1], by["H3c"]))
            add("H3c", "S7_eligible_keyword_fe", fit(k, by["H3c"], extra_controls=tuple(NEK)))
    verdicts = decide(specs, main, counted, supp)
    counts = {"rq3_papers_2018_2026": int(pop["k100"].year.between(2018, 2026).sum()),
              "s9_extra_withdrawn_after_review": int((full["k100"].s9 & ~full["k100"].rq3).sum())}
    return {"family": [s.hid for s in specs], "gate": gate, "verdicts": verdicts, "rows": pd.DataFrame(rows), "counts": counts}
