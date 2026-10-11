"""WP7 / D3-H3c: vintage alignment across channels (PLAN.md D3).

Does the title register line up with the LLM generation visible in the same paper's abstract?
    logit  R24_title ~ F24 + F26 + year FE + topic100 FE + log authors + llm_topic + log title length   (2025-26 U)
H3c: OR(F24 -> R24) > OR(F26 -> R24); test of b(F24) - b(F26) > 0 with the cluster-robust (topic100) covariance.
Falsified if the OR ratio is <= 1. The mirror contrast (R26 outcome, F26 > F24 expected) is exploratory.

F24 = abstract has >= 1 RARE21 word (2024-generation list); F26 = abstract has >= 1 of {principled, reframe*, genuine*,
brittle, auditable, sharply, high-stakes} or U+2011 / en-dash letter compounds in title or abstract (features_v2).

Robustness: by year (2025, 2026; 2024 exploratory), NA pool, non-LLM subset, shared-lemma exclusions (RARE21 contains
'harness' and 'unveil', which are also R24 stems: F24 without them, R24 without them, both), F26 split into words and
typography, F24 >= 2 words, mutually exclusive fingerprint categories, LPM with topic100 x year FE, bge topics, no log
authors (pilot-like), no title-length control, pilot lexicons (design/pi/vintage_check.py regexes), and per-word R24
outcomes (exploratory).

Outputs (outputs/d3_register/): vintage_models.csv, vintage_results.json, fig_F3_3_vintage_forest.{pdf,png,csv}

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d3_vintage
"""
from __future__ import annotations

import re
import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

from analyses import _core as C
from analyses import d3_slots as D3

warnings.filterwarnings("ignore")
OUTDIR = D3.OUTDIR
CTRL = "C(year) + C(topic100) + log_authors + llm_topic + lnw"
SHARED = {"harness", "unveil"}
# pilot lexicons (design/pi/vintage_check.py), used only to reconcile with the pilot ORs
PILOT_RARE = (r"\b(delv\w*|intricate\w*|meticulous\w*|showcas\w*|underscor\w*|pivotal|notabl\w*|commendabl\w*|realm|"
              r"tapestr\w*|garner\w*|boast\w*|invaluable|seamless\w*|groundbreaking|noteworthy|surpass\w*|unveil\w*|"
              r"innovative)\b")
PILOT_GEN26 = r"\b(principled|reframe\w*|genuine\w*|brittle|auditable|sharply|high-stakes)\b"
PILOT_FAM24 = r"\b(enhancing|unleashing|harnessing|unveiling|empowering|leveraging|elevating|boosting)\b"
PILOT_FAM26 = r"\b(unified|unifying|beyond|bridging)\b"


def prep(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d["lnw"] = np.log(d.n_words.clip(lower=1))
    words = d.f24_words.fillna("").astype(str).str.split("|")
    d["f24_noshared"] = words.map(lambda ws: any(w and w not in SHARED for w in ws)).astype(int)
    d["r24_noshared"] = d[[f"r24_{w}" for w in ("enhanc", "leverag", "unleash", "empower", "elevat", "boost")]] \
        .any(axis=1).astype(int)
    d["f24_only"] = ((d.f24 == 1) & (d.f26 == 0)).astype(int)
    d["f26_only"] = ((d.f26 == 1) & (d.f24 == 0)).astype(int)
    d["f_both"] = ((d.f24 == 1) & (d.f26 == 1)).astype(int)
    for w in ("enhanc", "leverag", "unveil", "unleash", "harness", "empower", "elevat", "boost", "unified", "unifying",
              "beyond", "bridging"):
        c = f"r24_{w}" if f"r24_{w}" in d else f"r26_{w}"
        d[c] = d[c].astype(int)
    tl = d.title.fillna("").str.lower()
    al = d.abstract.fillna("").str.lower()
    ab = d.abstract.fillna("")
    d["v24_pilot"] = C.rx_contains(al, PILOT_RARE).astype(int)
    d["v26_pilot"] = (C.rx_contains(al, PILOT_GEN26) | C.rx_contains(ab, "‑") |
                      C.rx_contains(ab, r"[A-Za-z]–[A-Za-z]")).astype(int)
    d["t24_pilot"] = C.rx_contains(tl, PILOT_FAM24).astype(int)
    d["t26_pilot"] = C.rx_contains(tl, PILOT_FAM26).astype(int)
    d["f26_words_i"] = d.f26_words.astype(int)
    d["f26_typo_i"] = d.f26_typo.astype(int)
    return d


def drop_nonvarying(d: pd.DataFrame, y: str, fe: str) -> pd.DataFrame:
    v = d.groupby(fe)[y].transform("std").fillna(0)
    return d[v > 0]


def contrast(res, a: str, b: str) -> dict:
    V = res.cov_params()
    diff = float(res.params[a] - res.params[b])
    se = float(np.sqrt(V.loc[a, a] + V.loc[b, b] - 2 * V.loc[a, b]))
    return dict(log_ratio=diff, se_log_ratio=se, ratio=np.exp(diff), ratio_lo=np.exp(diff - 1.96 * se),
                ratio_hi=np.exp(diff + 1.96 * se), p_one=float(stats.norm.sf(diff / se)))


def fit(d: pd.DataFrame, y: str, xa: str, xb: str, label: str, ctrl: str = CTRL, fe_col: str = "topic100",
        extra_x: str = "") -> dict:
    dd = drop_nonvarying(d, y, fe_col)
    fml = f"{y} ~ {xa} + {xb}{extra_x} + {ctrl}"
    r = C.logit(fml, dd, cluster=fe_col)
    t = C.or_table(r, [xa, xb])
    out = dict(label=label, outcome=y, x_a=xa, x_b=xb, nobs=int(r.nobs), n_y=int(dd[y].sum()),
               n_xa=int(dd[xa].sum()), n_xb=int(dd[xb].sum()),
               OR_a=t.loc[xa, "OR"], OR_a_lo=t.loc[xa, "OR_lo"], OR_a_hi=t.loc[xa, "OR_hi"], p_a=t.loc[xa, "p"],
               OR_b=t.loc[xb, "OR"], OR_b_lo=t.loc[xb, "OR_lo"], OR_b_hi=t.loc[xb, "OR_hi"], p_b=t.loc[xb, "p"])
    out.update(contrast(r, xa, xb))
    return out


def main():
    t0 = time.time()
    df = prep(D3.load_frame())
    d2526 = df[df.year.isin([2025, 2026])].copy()
    rows = []

    def add(r, family, outcome_family):
        r["family"], r["outcome_family"] = family, outcome_family
        rows.append(r)
        print(f"  {r['label'][:52]:52s} {r['outcome']:13s} OR_a {r['OR_a']:.2f} [{r['OR_a_lo']:.2f},{r['OR_a_hi']:.2f}]"
              f" OR_b {r['OR_b']:.2f} [{r['OR_b_lo']:.2f},{r['OR_b_hi']:.2f}] ratio {r['ratio']:.2f} "
              f"[{r['ratio_lo']:.2f},{r['ratio_hi']:.2f}] p1={r['p_one']:.3g}")

    for y, fam in [("r24_any", "R24"), ("r26_any", "R26")]:
        add(fit(d2526, y, "f24", "f26", "primary 2025-26"), "primary", fam)
        for yr in (2025, 2026, 2024):
            dy = df[df.year == yr]
            add(fit(dy, y, "f24", "f26", f"{yr} only", ctrl=CTRL.replace("C(year) + ", "")), "by year", fam)
        add(fit(d2526[d2526.NA == 1], y, "f24", "f26", "NA pool (camera-ready-free)"), "pool", fam)
        add(fit(d2526[d2526.non_llm == 1], y, "f24", "f26", "non-LLM subset", ctrl=CTRL.replace(" + llm_topic", "")),
            "subset", fam)
        add(fit(d2526, y, "f24", "f26", "bge topic100 FE", ctrl=CTRL.replace("topic100", "topic100_bge"),
                fe_col="topic100_bge"), "fixed effects", fam)
        add(fit(d2526, y, "f24", "f26", "no log authors (pilot-like controls)",
                ctrl=CTRL.replace(" + log_authors", "")), "controls", fam)
        add(fit(d2526, y, "f24", "f26", "no title-length control", ctrl=CTRL.replace(" + lnw", "")), "controls", fam)
        add(fit(d2526, y, "f24_2", "f26", "F24 >= 2 RARE21 words"), "fingerprint definition", fam)
        add(fit(d2526, y, "f24", "f26_words_i", "F26 split: words (typography as covariate)",
                extra_x=" + f26_typo_i"), "fingerprint definition", fam)
        add(fit(d2526, y, "f24", "f26_typo_i", "F26 split: typography (words as covariate)",
                extra_x=" + f26_words_i"), "fingerprint definition", fam)
        add(fit(d2526, y, "f24_only", "f26_only", "exclusive categories (F24 only vs F26 only; both as covariate)",
                extra_x=" + f_both"), "fingerprint definition", fam)
    # shared-lemma exclusions (R24 outcome only)
    add(fit(d2526, "r24_any", "f24_noshared", "f26", "F24 without harness/unveil"), "shared lemma", "R24")
    add(fit(d2526, "r24_noshared", "f24", "f26", "R24 without harness/unveil"), "shared lemma", "R24")
    add(fit(d2526, "r24_noshared", "f24_noshared", "f26", "both without harness/unveil"), "shared lemma", "R24")
    # pilot lexicons (reconciliation with design/pi/vintage_check.py)
    add(fit(d2526, "t24_pilot", "v24_pilot", "v26_pilot", "pilot lexicons, pilot controls (no log authors)",
            ctrl=CTRL.replace(" + log_authors", "")), "pilot reconciliation", "R24")
    add(fit(d2526, "t24_pilot", "v24_pilot", "v26_pilot", "pilot lexicons, PLAN controls"), "pilot reconciliation",
        "R24")
    add(fit(d2526, "r24_any", "v24_pilot", "v26_pilot", "pilot fingerprints, v2 R24"), "pilot reconciliation", "R24")
    add(fit(d2526, "t24_pilot", "f24", "f26", "v2 fingerprints, pilot R24 (-ing forms)"), "pilot reconciliation",
        "R24")
    add(fit(d2526, "t26_pilot", "v26_pilot", "v24_pilot", "pilot lexicons (mirror)"), "pilot reconciliation", "R26")
    # per-word R24 / R26 outcomes (exploratory)
    for w in ("enhanc", "leverag", "unleash", "harness", "empower", "boost", "unveil", "elevat"):
        c = f"r24_{w}"
        if d2526[c].sum() >= 40:
            add(fit(d2526, c, "f24", "f26", f"per word: {w}*"), "per word (exploratory)", "R24")
    for w in ("unified", "unifying", "beyond", "bridging"):
        c = f"r26_{w}"
        if d2526[c].sum() >= 40:
            add(fit(d2526, c, "f24", "f26", f"per word: {w}"), "per word (exploratory)", "R26")
    M = pd.DataFrame(rows)

    # LPM with topic100 x year FE
    lpm = []
    for y in ("r24_any", "r26_any"):
        r = C.feols(d2526.assign(ty=C.fe_interact(d2526.topic100, d2526.year)), y,
                    ["f24", "f26", "log_authors", "llm_topic", "lnw"], fe=["ty"], cluster="topic100")
        b = r.params[["f24", "f26"]]
        V = r.vcov.loc[["f24", "f26"], ["f24", "f26"]].to_numpy()
        diff = float(b["f24"] - b["f26"])
        se = float(np.sqrt(V[0, 0] + V[1, 1] - 2 * V[0, 1]))
        lpm.append(dict(outcome=y, pp_f24=100 * b["f24"], se_f24=100 * r.se["f24"], pp_f26=100 * b["f26"],
                        se_f26=100 * r.se["f26"], diff_pp=100 * diff, diff_lo=100 * (diff - 1.96 * se),
                        diff_hi=100 * (diff + 1.96 * se), p_one_f24_gt_f26=float(stats.norm.sf(diff / se)),
                        nobs=int(r.nobs), base_rate=float(d2526[y].mean())))
    lpm = pd.DataFrame(lpm)
    M.to_csv(OUTDIR / "vintage_models.csv", index=False)
    lpm.to_csv(OUTDIR / "vintage_lpm.csv", index=False)
    print(lpm.to_string())

    # descriptive cell rates (2025-26)
    desc = d2526.assign(cat=np.select([d2526.f_both == 1, d2526.f24_only == 1, d2526.f26_only == 1],
                                      ["both", "F24 only", "F26 only"], "neither")) \
        .groupby(["year", "cat"]).agg(n=("r24_any", "size"), r24_per1k=("r24_any", "mean"),
                                      r26_per1k=("r26_any", "mean")).reset_index()
    desc[["r24_per1k", "r26_per1k"]] *= 1000
    desc.to_csv(OUTDIR / "vintage_cells.csv", index=False)
    prev = df[df.year >= 2021].groupby("year")[["f24", "f26", "f26_words_i", "f26_typo_i", "F_any", "r24_any",
                                                "r26_any"]].mean()
    prev.to_csv(OUTDIR / "fingerprint_prevalence_by_year.csv")

    # ---- figure F3.3
    import matplotlib.ticker as mticker
    from matplotlib.lines import Line2D
    XMIN, XMAX = 0.4, 4.0
    fig, axes = C.new_fig("double", height=2.7, ncols=2, sharex=True, gridspec_kw={"wspace": 0.32})
    fd = []
    order = ["primary 2025-26", "2025 only", "2026 only", "2024 only"]
    names = {"primary 2025-26": "2025-26 pooled", "2025 only": "2025", "2026 only": "2026",
             "2024 only": "2024 (exploratory)"}
    for ax, fam, title in [(axes[0], "R24", "Outcome: R24 word in title"),
                           (axes[1], "R26", "Outcome: R26 word in title (exploratory)")]:
        sub = M[(M.outcome_family == fam) & M.label.isin(order) & M.x_a.eq("f24") & M.x_b.eq("f26")]
        sub = sub.set_index("label").loc[order].reset_index()
        labels, est, lo, hi, cols = [], [], [], [], []
        for _, r in sub.iterrows():
            nm = names[r.label]
            for key, fp, col in [("a", "F24", C.COLORS[0]), ("b", "F26", C.COLORS[1])]:
                labels.append(f"{nm}: {fp}")
                est.append(r[f"OR_{key}"])
                lo.append(max(r[f"OR_{key}_lo"], XMIN))
                hi.append(min(r[f"OR_{key}_hi"], XMAX))
                cols.append(col)
                fd.append(dict(outcome=fam, sample=nm, fingerprint=fp, OR=r[f"OR_{key}"], lo=r[f"OR_{key}_lo"],
                               hi=r[f"OR_{key}_hi"], ratio_F24_over_F26=r.ratio, ratio_lo=r.ratio_lo,
                               ratio_hi=r.ratio_hi, p_one_ratio_gt1=r.p_one, nobs=r.nobs,
                               truncated_lo=bool(r[f"OR_{key}_lo"] < XMIN), truncated_hi=bool(r[f"OR_{key}_hi"] > XMAX)))
        C.forest(ax, labels, est, lo, hi, ref=1.0, log=True, colors=cols)
        ypos = np.arange(len(labels))[::-1]
        for yv, f in zip(ypos, fd[-len(labels):]):
            if f["truncated_lo"]:
                ax.plot([XMIN], [yv], marker="<", color=C.COLORS[0] if f["fingerprint"] == "F24" else C.COLORS[1],
                        ms=5, clip_on=False)
        ax.set_xlim(XMIN, XMAX)
        ax.xaxis.set_minor_formatter(mticker.NullFormatter())
        ax.set_xticks([0.5, 0.75, 1, 1.5, 2, 3], ["0.5", "0.75", "1", "1.5", "2", "3"])
        ax.set_title(title, loc="left", fontsize=9)
        ax.set_xlabel("odds ratio (95% CI), log scale")
        mids, mlabs = [], []
        for k, (_, r) in enumerate(sub.iterrows()):
            mids.append((ypos[2 * k] + ypos[2 * k + 1]) / 2)
            mlabs.append(f"{names[r.label]}\nF24/F26 {r.ratio:.2f} [{r.ratio_lo:.2f}, {r.ratio_hi:.2f}]")
            if k:
                ax.axhline(ypos[2 * k] + 0.5, color=C.GRID, lw=0.6)
        ax.set_yticks(mids, mlabs, fontsize=7)
    fig.legend(handles=[Line2D([], [], color=C.COLORS[0], marker="o", lw=1.6, label="F24 abstract fingerprint (2024 vintage)"),
                        Line2D([], [], color=C.COLORS[1], marker="o", lw=1.6, label="F26 abstract fingerprint (2026 vintage)")],
               loc="lower center", ncol=2, fontsize=7.5, bbox_to_anchor=(0.45, -0.02))
    fig.subplots_adjust(left=0.2, right=0.98, bottom=0.27, top=0.9, wspace=0.62)
    C.save_fig(fig, "fig_F3_3_vintage_forest", OUTDIR, data=pd.DataFrame(fd))

    prim24 = M[(M.outcome_family == "R24") & (M.label == "primary 2025-26")].iloc[0]
    prim26 = M[(M.outcome_family == "R26") & (M.label == "primary 2025-26")].iloc[0]
    verdict = dict(OR_F24_R24=prim24.OR_a, OR_F26_R24=prim24.OR_b, ratio=prim24.ratio, ratio_lo=prim24.ratio_lo,
                   ratio_hi=prim24.ratio_hi, p_one=prim24.p_one, prediction_ratio_gt1=bool(prim24.ratio > 1),
                   ratio_CI_excludes_1=bool(prim24.ratio_lo > 1), falsified=bool(prim24.ratio <= 1),
                   mirror_R26_ratio_F26_over_F24=float(1 / prim26.ratio),
                   mirror_R26_ratio_lo=float(1 / prim26.ratio_hi), mirror_R26_ratio_hi=float(1 / prim26.ratio_lo))
    res = dict(hypothesis="H3c", models=M.to_dict(orient="records"), lpm=lpm.to_dict(orient="records"),
               cells=desc.to_dict(orient="records"),
               fingerprint_prevalence={int(k): v for k, v in prev.round(4).to_dict(orient="index").items()},
               verdict_inputs=verdict, runtime_s=round(time.time() - t0, 1))
    D3.write_json(res, OUTDIR / "vintage_results.json")
    print("verdict", verdict, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
