"""Acceptance patterns by title, abstract and team features on one harmonised specification.

Descriptive companion to D4 (not part of the pre-registered plan). For each binary feature it reports,
over 2018-2026: prevalence among decided papers, the year-standardised raw acceptance gap, and logit ORs
for (a) acceptance among decided papers, (b) acceptance among all submissions (withdrawal and desk
rejection count as failure) and (c) withdrawal among all submissions. Adjusted models use year FE,
log #authors and topic100 FE with SEs clustered by topic100; the 2022+ model also adds the log of the
team's prior ICLR acceptances (declared-key history). Accepted papers' titles may be camera-ready
versions, so acceptance associations are descriptive (see outputs/snapshot for the audit gate).

Outputs: outputs/acceptance/{acceptance_by_year.csv, feature_associations.csv, team_gradients.csv}.
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from . import _core as core

OUT = core.OUT / "acceptance"

FEATURES = {
    "name_primary": "NAME: subtitle title",
    "ortho_mixed_case": "NAME lead in mixed case (LoRA-style)",
    "ortho_all_caps": "NAME lead in ALL CAPS (CRISP-style)",
    "compound": "Any colon/dash compound title",
    "question": "Question title",
    "case_sentence_case": "Sentence-case title",
    "case_all_caps": "Whole title in ALL CAPS",
    "has_digit": "Digit in title (3D, GPT-4, ...)",
    "long_title": "Long title (>= 13 words)",
    "using_word": "'using' in title",
    "mentions_llm": "Title mentions LLMs/LMs",
    "r24_any": "2024-style LLM title word (enhanc*, leverag*, unveil*, ...)",
    "r26_any": "2026-style title word (unified, beyond, bridging)",
    "tpl_towards": "'Towards ...' title",
    "F_any": "Abstract carries an LLM-style fingerprint",
}


def load() -> pd.DataFrame:
    u = pd.read_parquet(core.OUT / "core" / "universe.parquet")
    f = pd.read_parquet(core.OUT / "features" / "features_v2.parquet")
    d = u.merge(f.drop(columns=["year"]), on="submission_id")
    d = d[d.year >= 2018].copy()
    d["long_title"] = d.n_words >= 13
    d["using_word"] = d.title_nfkc.map(lambda t: bool(re.search(r"\busing\b", t, re.I)))
    d["accepted_any"] = d.ACC.astype(int)
    d["withdrawn"] = d.WD.astype(int)
    d["lprior_acc"] = np.log1p(d.max_prior_accs.fillna(0))
    for c in FEATURES:
        d[c] = d[c].fillna(False).astype(int)
    return d


def logit_or(data: pd.DataFrame, y: str, x: str, controls: str) -> tuple[float, float, float]:
    m = smf.logit(f"{y} ~ {x} + {controls}", data).fit(
        disp=0, method="bfgs", maxiter=2000,
        cov_type="cluster", cov_kwds={"groups": data["topic100"].to_numpy()})
    b, se = m.params[x], m.bse[x]
    return float(np.exp(b)), float(np.exp(b - 1.96 * se)), float(np.exp(b + 1.96 * se))


def year_std_gap(dec: pd.DataFrame, x: str) -> float:
    """Mean over years (weighted by decided papers) of acc(x=1) - acc(x=0), in pp."""
    rows = []
    for _, g in dec.groupby("year"):
        a, b = g[g[x] == 1], g[g[x] == 0]
        if len(a) >= 5 and len(b) >= 5:
            rows.append((len(g), a.ACC.mean() - b.ACC.mean()))
    w = np.array([r[0] for r in rows]); v = np.array([r[1] for r in rows])
    return float(100 * (w * v).sum() / w.sum())


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    d = load()
    dec = d[d.ACC | d.REJ].copy()
    dec["acc"] = dec.ACC.astype(int)

    by_year = d.groupby("year").agg(submissions=("submission_id", "size"), accepted=("ACC", "sum"),
                                    decided=("in_acc_pop", "sum"), withdrawn=("WD", "sum"), desk=("DR", "sum"))
    by_year["acc_rate_decided"] = by_year.accepted / by_year.decided
    by_year["acc_rate_all"] = by_year.accepted / by_year.submissions
    by_year["withdrawal_rate"] = by_year.withdrawn / by_year.submissions
    by_year.round(4).to_csv(OUT / "acceptance_by_year.csv")

    ctrl = "C(year) + log_authors + C(topic100)"
    rows = []
    for x, label in FEATURES.items():
        n1 = int(dec[x].sum())
        r = {"feature": x, "label": label, "n_decided_with": n1, "share_decided": dec[x].mean(),
             "acc_rate_with": dec.loc[dec[x] == 1, "acc"].mean(), "acc_rate_without": dec.loc[dec[x] == 0, "acc"].mean(),
             "year_std_gap_pp": year_std_gap(dec, x)}
        r["OR_year"], r["OR_year_lo"], r["OR_year_hi"] = logit_or(dec, "acc", x, "C(year)")
        r["OR_adj"], r["OR_adj_lo"], r["OR_adj_hi"] = logit_or(dec, "acc", x, ctrl)
        late = dec[dec.year >= 2022]
        r["OR_adj_exp_2022"], r["OR_adj_exp_2022_lo"], r["OR_adj_exp_2022_hi"] = logit_or(late, "acc", x, ctrl + " + lprior_acc")
        r["OR_all_adj"], r["OR_all_adj_lo"], r["OR_all_adj_hi"] = logit_or(d, "accepted_any", x, ctrl)
        r["OR_withdraw_adj"], r["OR_withdraw_adj_lo"], r["OR_withdraw_adj_hi"] = logit_or(d, "withdrawn", x, ctrl)
        rows.append(r)
        print(x, round(r["OR_adj"], 3), flush=True)
    pd.DataFrame(rows).round(4).to_csv(OUT / "feature_associations.csv", index=False)

    team = []
    bins = pd.cut(dec.declared_name_count, [0, 1, 2, 3, 4, 5, 7, 10, 15, 200], labels=["1", "2", "3", "4", "5", "6-7", "8-10", "11-15", "16+"])
    for k, g in dec.groupby(bins, observed=True):
        team.append({"gradient": "team_size", "bin": str(k), "n": len(g), "acc_rate": g.acc.mean()})
    late = dec[dec.year >= 2022]
    pbins = pd.cut(late.max_prior_accs.fillna(0), [-1, 0, 1, 3, 7, 1000], labels=["0", "1", "2-3", "4-7", "8+"])
    for k, g in late.groupby(pbins, observed=True):
        team.append({"gradient": "team_prior_iclr_acceptances_2022plus", "bin": str(k), "n": len(g), "acc_rate": g.acc.mean()})
    pd.DataFrame(team).round(4).to_csv(OUT / "team_gradients.csv", index=False)


if __name__ == "__main__":
    main()
