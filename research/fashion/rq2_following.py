"""RQ2 (following): who joins hot topics, and what they bring. Implements PREREGISTRATION.md RQ2 and the pre-run log.

Population: papers with at least one author key (D2), years 2019-2026, SE clustered by topic.
  H2a  incumbent   ~ hot        topic FE + year dummies    predicted < 0
  H2b  method      ~ newcomer   topic x year FE (D4)       predicted < 0
  H2c  measurement ~ newcomer   topic x year FE            predicted > 0
  H2d  buzzword    ~ newcomer   topic x year FE            predicted > 0, only if the D6 gate passed (D10)
Counted variants: variants.RQ2 (nine shared + R2 ID-consistent years). Supplementary S1-S8 (never in the verdict).

run(frames, gate, ys) needs either simulated outcome columns `ys` (dry-runs) or, for the real labels, the frozen
entry point (outcomes.require_frozen); the RQ2 outcomes are not sealed by the loader, so this guard keeps them unseen.
"""
from __future__ import annotations

import json

import numpy as np
import pandas as pd

import variants
from analysis import Spec, corrected, decide, fit, misclassification_rates
from common import TOPICS, class_of

YEARS = (2019, 2026)
SPECS = [
    Spec("H2a", "incumbent", "hot", -1, 0.02, "topic+year", YEARS),
    Spec("H2b", "method", "newcomer", -1, 0.02, "cell", YEARS),
    Spec("H2c", "measurement", "newcomer", +1, 0.01, "cell", YEARS),
    Spec("H2d", "buzzword", "newcomer", +1, 0.01, "cell", YEARS, gated=True),
]
NEK = ["nek_1", "nek_2", "nek_3", "nek_4", "nek_5plus"]                 # S7: number of eligible keywords (ref. 0)
REFERENCE = TOPICS.parent / "annotation" / "contribution_types"
# Every column that is an outcome on some side of an RQ2 analysis (confirmatory, supplementary or exploratory). A dry-run
# must simulate all of them; the newcomer columns are then derived from the simulated incumbency, so no real outcome-side
# column ever meets a real regressor before the freeze.
SIMULATED = {"incumbent", "incumbent_w2", "incumbent_s4", "method", "measurement", "buzzword", "lists_hot"}


def population(df: pd.DataFrame) -> pd.DataFrame:
    return df[df.has_author_key]


def guard(ys: dict[str, pd.Series] | None) -> None:
    """Real RQ2 labels only through the frozen run; otherwise every outcome-side column must be simulated (fails closed)."""
    if ys is None:
        from outcomes import require_frozen
        require_frozen()
        return
    missing = SIMULATED - set(ys)
    if missing:
        raise ValueError(f"simulated outcomes missing for {sorted(missing)}: refusing to fall back to real labels")


def with_columns(df: pd.DataFrame, ys: dict[str, pd.Series] | None) -> pd.DataFrame:
    df = df.copy()
    if ys is not None:
        for c, s in ys.items():
            df[c] = s.reindex(df.submission_id).to_numpy()
        for w in ["", "_w2", "_s4"]:
            df[f"newcomer{w}"] = np.where(df.has_author_key, 1 - df[f"incumbent{w}"], np.nan)
    k = df.n_eligible_keywords.clip(upper=5)
    for i, c in enumerate(NEK, start=1):
        df[c] = (k == i).astype(float)
    return df


def label_reliability() -> dict:
    """D11: second-pass agreement for the method and measurement indicators, and S8 misclassification rates."""
    lab = pd.read_csv(TOPICS / "paper_contributions.csv.gz")
    sp = lab[lab.second_pass_primary_type.notna()]
    first, second = sp.primary_type.map(class_of), sp.second_pass_primary_type.map(class_of)
    out = {"second_pass_papers": int(len(sp))}
    # random stratum only: the enriched strata over-represent rare classes, so their error rates would not be the corpus's
    pilot = pd.read_csv(REFERENCE / "pilot_gold_facets.csv").query("stratum == 'random'")
    pilot = pilot[["submission_id", "gold_primary"]].rename(columns={"gold_primary": "ref"})
    train = pd.read_csv(REFERENCE / "training" / "training_labels.csv").query("stratum == 'random'")
    train = train[["submission_id", "primary_type"]].rename(columns={"primary_type": "ref"})
    ref = pd.concat([pilot, train]).drop_duplicates("submission_id").merge(lab[["submission_id", "primary_type"]], on="submission_id")
    for name, pos in [("method", {"method"}), ("measurement", {"dataset_benchmark", "evaluation"})]:
        a, b = first.isin(pos), second.isin(pos)
        po = float((a == b).mean())
        pe = float(a.mean() * b.mean() + (1 - a.mean()) * (1 - b.mean()))
        a0, a1, n = misclassification_rates(ref.primary_type.map(class_of), ref.ref.map(class_of), pos)
        out[name] = {"second_pass_agreement": round(po, 4), "second_pass_kappa": round((po - pe) / (1 - pe), 4),
                     "reference_n": n, "false_positive_rate": round(a0, 4), "false_negative_rate": round(a1, 4)}
    return out


def run(frames: dict[str, pd.DataFrame], gate: bool, ys: dict[str, pd.Series] | None = None,
        supplementary: bool = True) -> dict:
    guard(ys)
    specs = [s for s in SPECS if not s.gated or gate]
    pop = {m: population(with_columns(f, ys)) for m, f in frames.items()}
    main = {s.hid: fit(pop["k100"], s, describe=ys is None) for s in specs}
    counted = {s.hid: {} for s in specs}
    rows = [{"hypothesis": h, "variant": "main", "kind": "main", **r} for h, r in main.items()]
    for name, v in variants.counted(2).items():
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
        for s in specs:
            add(s.hid, "S1_log_team", fit(k, s, extra_controls=("log_team",)))
            if "fine" in pop:
                add(s.hid, "S5_fine", fit(pop["fine"], s))
        add("H2a", "S2_pool_controls", fit(k, by["H2a"], extra_controls=("maturity", "log_papers_prev", "log_team")))
        w2 = (2023, 2026)
        add("H2a", "S3_window_2023_2026", fit(k, Spec("H2a", "incumbent_w2", "hot", -1, 0.02, "topic+year", w2)))
        add("H2a", "S4_without_own_versions", fit(k, Spec("H2a", "incumbent_s4", "hot", -1, 0.02, "topic+year", YEARS)))
        for s in specs[1:]:
            add(s.hid, "S3_window_2023_2026", fit(k, s, x="newcomer_w2", years=w2))
            add(s.hid, "S4_without_own_versions", fit(k, s, x="newcomer_s4"))
        if "H2d" in by:
            add("H2d", "S6_lists_hot_keyword", fit(k[k.lists_hot == 1], by["H2d"]))
            add("H2d", "S7_eligible_keyword_fe", fit(k, by["H2d"], extra_controls=tuple(NEK)))
        rel = label_reliability()
        for h, cls in [("H2b", "method"), ("H2c", "measurement")]:
            add(h, "S8_misclassification", corrected(main[h], rel[cls]["false_positive_rate"], rel[cls]["false_negative_rate"]))
    verdicts = decide(specs, main, counted, supp)
    return {"family": [s.hid for s in specs], "gate": gate, "verdicts": verdicts, "rows": pd.DataFrame(rows),
            "label_reliability": label_reliability() if supplementary else None}


def to_json(res: dict) -> str:
    return json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=2, default=lambda o: None if o is np.nan else o)
