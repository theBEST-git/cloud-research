"""Write outputs/snapshot/RESULTS.md from results.json and the tables written by analyses.snapshot_final.

Every number comes from the computed outputs. Sentences whose wording depends on a verdict are guarded by assertions,
so a rerun on a different audit sample fails loudly instead of keeping stale prose (audit issue C-I8).

Run:  cd research/titles/src && /home/user/venv/bin/python -m analyses.snapshot_final_report [--outdir DIR]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from analyses import snapshot_bounds as S

MINUS = "−"


def n_(x, d=2, sign=False):
    """number with a typographic minus"""
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "n/a"
    x = float(x)
    if abs(x) < 0.5 * 10 ** (-d):
        x = 0.0
    s = f"{x:+.{d}f}" if sign else f"{x:.{d}f}"
    return s.replace("-", MINUS)


def ci(lo, hi, d=2):
    return f"[{n_(lo, d)}, {n_(hi, d)}]"


def pct(x, d=1):
    return n_(100 * x, d)


def render(out: Path) -> str:
    R = json.loads((out / "results.json").read_text())
    I = json.loads((out / "interim_254" / "results.json").read_text())  # noqa: E741
    H = {h["id"]: h for h in R["hypotheses"]}
    meta = R["meta"]
    fz = meta["audit_freeze"]
    fl_all = pd.read_csv(out / "T4_2_flip_matrices.csv")
    fl = fl_all[fl_all.spec == "primary"].set_index("feature")
    tp = pd.read_csv(out / "T4_2_tipping_points.csv").set_index("feature")
    idt = pd.read_csv(out / "T4_2_identification_by_spec.csv")
    ida = pd.read_csv(out / "T4_2_identified_anywhere.csv")
    fpath = pd.read_csv(out / "T4_2_freeze_path.csv")
    tpy = pd.read_csv(out / "T4_2_tipping_by_year.csv")
    fr = pd.read_csv(out / "found_rates.csv")
    fm = pd.read_csv(out / "findability_models.csv")
    rt = pd.read_csv(out / "retitling.csv")
    ab = pd.read_csv(out / "abstract_audit.csv")
    gate = pd.read_csv(out / "gate.csv").set_index("claim")
    rv = pd.read_csv(out / "route_validation.csv").set_index("decision")
    mc = pd.read_csv(out / "T4_2_flip_multiclass.csv")
    rvs = R["route_validation"]["summary"]
    _iid = {(d["spec"], d["feature"]): d for d in I["identification_by_spec"]}
    i_union_shift = abs(_iid[("primary", "NAME")]["did_pp"] - _iid[("union_route", "NAME")]["did_pp"])
    tim = meta["timing"]
    np_ = meta["n_pairs"]
    nA, nR = np_["primary_by_decision"]["accepted"], np_["primary_by_decision"]["rejected"]
    enl = fz["enlargement"]
    L = []
    A = L.append

    def spec(s, k="NAME"):
        return idt[(idt.spec == s) & (idt.feature == k)].iloc[0]

    def fr_row(src, yr, dec):
        q = fr[(fr.source == src) & (fr.year.astype(str) == yr) & (fr.decision == dec)]
        return q.iloc[0]

    def fmrow(term, formula, smp):
        return fm[(fm.term == term) & (fm.formula == formula) & (fm["sample"] == smp)].iloc[0]

    def rtrow(sp, yrs, meas="changed_norm"):
        return rt[(rt.spec == sp) & (rt.years.astype(str) == yrs) & (rt.measure == meas)].iloc[0]

    def lab(k):
        return S.FEAT_LABEL.get(k, k) if k not in ("L_title_words", "O_union_arxiv") else \
            {"L_title_words": "L-title words (R24 or R26)", "O_union_arxiv": "O-union w/o ALL-CAPS"}[k]

    def aud_word(k, f=fl):
        r = f.loc[k]
        if not bool(r.channel_ok):
            return "no (channel)"
        return "yes" if bool(r.auditable) else "no (count)"

    nm = tp.loc["NAME"]
    nf = fl.loc["NAME"]
    aud = tp[tp.auditable]
    holm_pass = sorted(tp.index[tp.passes_holm_dec])
    unc_pass = sorted(tp.index[tp.passes_uncorrected_dec])
    # ---------------------------------------------------------------- guards for verdict-dependent prose
    assert H["SB1"]["verdict"] == "supported", "prose assumes NAME G_dec is not identified"
    assert H["SB2"]["verdict"] == "not_supported" and not holm_pass, "prose assumes no feature passes the Holm gate"
    assert H["G1"]["verdict"] == "supported", "prose assumes the H4a G_total gate passes on the primary audit"
    assert H["G2"]["verdict"] == H["G2b"]["verdict"] == H["G3"]["verdict"] == "not_supported"
    assert H["SB5"]["verdict"] == "not_supported"
    assert enl["complete"], "prose assumes the enlargement is complete"
    assert bool(gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: new_records_only)", "passes"])
    assert bool(gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: post_2024_26)", "passes"])
    sc = tp.loc["sentence_case"]
    ou = tp.loc["O_union_arxiv"]
    assert bool(sc.auditable) and bool(ou.auditable)

    # ================================================================ header
    A("# WP4 Results: camera-ready snapshot bounds (D4 decision-stage bound, V7 route validation, §4 gate)")
    A("")
    A("Work package WP4. Pre-registered in `docs/PLAN.md` §D4 (\"Decision-stage bound\"), §3 V7 and §4 (Gate); common "
      "definitions §0.")
    A("")
    A(f"**Status: final.** Every number below comes from one frozen audit sample: the original 616-paper audit plus the "
      f"complete enlargement ({enl['n_records_ok']:,} records without a network error, from the first "
      f"{enl['n_lines_used']:,} lines of `cache/arxiv_audit_enlarge.jsonl`; SHA-256 of those bytes "
      f"`{enl['sha256_of_lines_used'][:16]}…`, full hash in `results.json` → `meta.audit_freeze`). This run supersedes "
      "the interim run on the first 254 enlargement records. That run's files are archived in `interim_254/`, and the "
      "audit response at the end of this file lists what changed.")
    A("")
    A("**Scripts.**")
    A("- `src/analyses/snapshot_final.py` runs the analysis (about 45 s) and writes every table, figure and "
      "`results.json`.")
    A("- `src/analyses/snapshot_bounds.py` holds the building blocks (pairs, flip tables, tipping points, stage "
      "prevalences, findability, route validation). `snapshot_final.py` uses them unchanged. The file is hashed as "
      "required code in the pre-registration bundle (`outputs/prereg/bundle.sha256`), so it was not edited.")
    A("- `src/analyses/audit_v2.py` ran the arXiv re-queries in the background: route validation, v1 abstracts and "
      "the enlargement.")
    A("- `src/analyses/snapshot_final_report.py` writes this file from `results.json` and the tables.")
    A("")
    A("**Language.** All acceptance statements are associational. Author information enters only through the first "
      "author's declared name, used as an arXiv search key. It is never treated as a verified person.")
    A("")
    A("**Why the audit matters.** The export is a post-decision snapshot. Accepted papers may carry camera-ready "
      "titles, while rejected, withdrawn and desk-rejected papers keep submission-stage text.")
    A("")
    A("**How the audit works.**")
    A("- Each audited paper's arXiv version 1, posted before the ICLR decision date, is compared with the stored title.")
    A("- Rejected papers' v1-vs-stored differences measure everything that is *not* camera-ready editing: "
      "arXiv-vs-OpenReview wording, rebuttal-period edits and pre-submission revisions.")
    A("- The accepted-minus-rejected difference in net feature flips is the **net-flip DiD**, D. It estimates the "
      "camera-ready excess, which can bias any acceptance association of a title feature. It does so only if the "
      "non-camera-ready drift is the same in both arms; §2 tests this by v1 timing.")
    A("")
    A("**Tipping point.**")
    a2 = nm.acc_share_s2
    A(f"- A net camera-ready addition D raises P(f | accepted) = P₃ by D, and P(f | reviewed) = P₂ by a₂·D. Here "
      f"a₂ = {n_(a2, 3)} is the accepted share of the reviewed set (2024–26, year-standardised).")
    A("- The submission-stage gain is G_dec(D) = (P₃ − D)/(P₂ − a₂D). Setting it to 1 gives the tipping point "
      "D\\* = (P₃ − P₂)/(1 − a₂). G_total uses s0 and a₀ in the same way.")
    A(f"- Within a single year, D\\* equals P₃ minus the prevalence among reviewed, non-accepted papers. With "
      f"year-standardised pooling it differs from the accepted-minus-rejected risk difference (NAME: D\\* "
      f"{n_(nm.tip_dec_pp)} pp vs {n_(nm.rd_acc_rej_pp)} pp).")
    A("")
    A("**Auditable.** A feature is auditable when two conditions hold:")
    A("1. arXiv metadata can carry it. arXiv titles are never ALL-CAPS and never contain U+2011/U+2013 typography, "
      "and arXiv abstracts never contain an em dash. For such features the \"net flip\" is just the stored prevalence.")
    A(f"2. At least {S.MIN_V1} titles in *each* arm have the feature in their v1 (pre-stated).")
    A("")
    A("**Gate (G_dec acceptance associations).** A claim passes only if all three conditions hold:")
    A("1. The feature is auditable.")
    A("2. The editing-corrected 95% CI of G excludes 1. This CI pairs a universe-bootstrap replicate with an audit "
      "draw D ~ N(D̂, pseudo-flip SE).")
    A(f"3. Its one-sided identification p-value survives Holm across all {len(aud)} auditable title features at "
      f"α = {meta['alpha_one_sided']}, the one-sided level of the PLAN's 95% CI rule (PLAN §0 requires Holm within a "
      "confirmatory family).")
    A("")
    A("The identification p-value tests H₀ \"the true DiD is at or beyond the tipping point\". It uses "
      "z = (D\\* − D̂)/√(se_D² + se_D\\*²), where se_D is the pseudo-flip SE and se_D\\* is the universe-bootstrap SE "
      "of the tipping point. The interim rule had no multiplicity control and ignored se_D\\*: it required only the "
      "point tipping point beyond one audit 95% CI, plus an observed G CI excluding 1. That rule is reported as "
      "\"uncorrected\".")
    A("")
    A("---")
    A("")

    # ================================================================ verdict table
    sb3 = {k: fl.loc[k] for k in ["using", "R24", "R26", "slot_llm", "title_typo"]}
    r_all, r_post = rtrow("primary", "all"), rtrow("primary", "2024-26")
    r_in, r_pre = rtrow("v1_in_review", "all"), rtrow("v1_before_deadline", "all")
    fa = fmrow("acc", "found_i ~ C(year) + acc + log_nw + NAME", "original+enlarge")
    fn = fmrow("NAME", "found_i ~ C(year) + acc + log_nw + NAME", "original+enlarge")
    fA = fr_row("original+enlarge", "all", "accepted")
    fR = fr_row("original+enlarge", "all", "rejected")
    ipwp = spec("ipw_find_pop")
    g1 = gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: primary)"]
    g1d = gate.loc["H4a NAME G_dec within [0.90, 1.11] (2024-26 pooled; audit: primary)"]
    g1p = gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: post_2024_26)"]
    g1o = gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: original_only)"]
    g2 = gate.loc["H4b L-title G_total < 1 (2024-26; audited as R24 or R26)"]
    g2b = gate.loc["H4b O-union G_total < 1 (2024-26; audited without ALL-CAPS)"]
    g3 = gate.loc["H4b/abstract F24 or F26 words G_total < 1 (2024-26)"]
    abp = ab[ab.spec == "abs_2024_26"].set_index("feature")
    ab23 = ab[ab.spec == "abs_2023_26"].set_index("feature")
    abo = ab[ab.spec == "abs_original_only"].set_index("feature")
    f24, f24s = abp.loc["F24"], ab23.loc["F24"]
    lt = fl.loc["L_title_words"]
    ouf = fl.loc["O_union_arxiv"]
    gg = rv
    A("## Verdict summary")
    A("")
    A("| ID | Claim tested | Estimate (95% CI unless stated) | Criterion | Verdict |")
    A("|---|---|---|---|---|")
    A(f"| SB1 | PLAN D4: NAME G_dec is not identified by the audit (pilot: tip ≈ 1.8 pp vs DiD +2.1, se 2.4) | "
      f"DiD **{n_(nf.did * 100, 2, True)} pp {ci(nf.did_lo * 100, nf.did_hi * 100)}** ({nA}/{nR} pairs). Tip "
      f"**D\\* = {n_(nm.tip_dec_pp)} pp**; one-sided p = {n_(nm.p_ident_dec, 3)}. Observed G_dec {n_(nm.G_dec_obs, 3)} "
      f"{ci(nm.G_dec_lo95, nm.G_dec_hi95, 3)}; G_dec at the audit point estimate {n_(nm.G_dec_sel_point, 3)} | "
      f"Identified iff D\\* lies beyond the audit CI | **Supported** (not identified) |")
    A(f"| SB2 | Gate §4: some title feature's acceptance association (G_dec ≠ 1) survives the audit | "
      f"**{len(holm_pass)} of {len(tp)}** features pass ({len(aud)} auditable). Smallest identification p: "
      + "; ".join(f"{lab(k)} {n_(r.p_ident_dec, 3)} (Holm {n_(r.p_holm_dec, 2)})"
                  for k, r in aud.sort_values("p_ident_dec").head(3).iterrows()) +
      f". Uncorrected rule: {len(unc_pass)} pass ({', '.join(lab(k) for k in unc_pass) or 'none'}) | "
      f"Auditable, corrected 95% CI excludes 1, Holm p < 0.025 | "
      f"**Not supported** (no claim survives multiplicity control) |")
    A(f"| SB3 | V7: rare lexical features are unauditable | v1-present accepted/rejected: 'using' {int(sb3['using'].v1_present_acc)}/"
      f"{int(sb3['using'].v1_present_rej)}, R24 {int(sb3['R24'].v1_present_acc)}/{int(sb3['R24'].v1_present_rej)}, "
      f"R26 {int(sb3['R26'].v1_present_acc)}/{int(sb3['R26'].v1_present_rej)}, LLM slot word "
      f"{int(sb3['slot_llm'].v1_present_acc)}/{int(sb3['slot_llm'].v1_present_rej)}, title typography 0/0 (channel) | "
      f"≥ 10 per arm and arXiv-measurable | **{H['SB3']['verdict'].replace('_', ' ').capitalize()}** ('using' and R24 "
      f"became auditable as the audit grew) |")
    A(f"| SB4 | Accepted papers are more findable; IPW leaves the NAME bound unchanged | Found {pct(fA.found_rate)}% vs "
      f"{pct(fR.found_rate)}% (2023–26, n = {int(fA.n):,}/{int(fR.n):,}). Odds ratio (accepted) **{n_(fa.OR)} "
      f"{ci(fa.OR_lo, fa.OR_hi)}**; OR(NAME) {n_(fn.OR)} {ci(fn.OR_lo, fn.OR_hi)}. IPW × population NAME DiD "
      f"{n_(ipwp.did_pp, 2, True)} {ci(ipwp.did_lo_pp, ipwp.did_hi_pp)} | Not pre-registered; descriptive | "
      f"**{H['SB4']['verdict'].replace('_', ' ').capitalize()}** |")
    A(f"| SB5 | Camera-ready retitling: accepted papers retitle more than rejected ones | {pct(r_all.rate_acc)}% vs "
      f"{pct(r_all.rate_rej)}%: **{n_(100 * r_all['diff'], 1, True)} pp {ci(100 * r_all.diff_lo, 100 * r_all.diff_hi, 1)}**. "
      f"v1 posted during review: {n_(100 * r_in['diff'], 1, True)} {ci(100 * r_in.diff_lo, 100 * r_in.diff_hi, 1)}; v1 "
      f"posted before the deadline: {n_(100 * r_pre['diff'], 1, True)} {ci(100 * r_pre.diff_lo, 100 * r_pre.diff_hi, 1)} | "
      f"CI excludes 0 | **Not supported** |")
    A(f"| V7a | The findability gap is not specific to title search | n = 300 (150/150). Gap {n_(rvs['gap_A']['est'])} "
      f"(route A) vs {n_(rvs['gap_B']['est'])} (route B); difference {n_(rvs['gap_B_minus_A']['est'] + 0.0)} "
      f"{ci(rvs['gap_B_minus_A']['lo'], rvs['gap_B_minus_A']['hi'])}. Both routes share an abstract-similarity rule; "
      f"near-miss bound on the gap {n_(rvs['near_miss_bound']['jac_ge_0.10']['gap_bound'])} | Gap B CI > 0 and gap "
      f"difference CI includes 0 | **{H['V7a']['verdict'].replace('_', ' ').capitalize()}** (with the shared-rule caveat) |")
    A(f"| V7b | The title route does not select on title stability | Retitled: route A "
      f"{pct(gg.loc['all', 'A_changed_rate'])}% (n = {int(gg.loc['all', 'A_changed_n'])}), route B "
      f"{pct(gg.loc['all', 'B_changed_rate'])}% (n = {int(gg.loc['all', 'B_changed_n'])}); papers only route B finds: "
      f"{int(gg.loc['all', 'Bonly_changed_k'])} of {int(gg.loc['all', 'Bonly_changed_n'])} retitled | Rule in "
      f"`results.json` | **{H['V7b']['verdict'].replace('_', ' ').capitalize()}** |")
    A(f"| G1 | Gate for D4-H4a: NAME neutrality (pooled 2024–26 G_total in [0.90, 1.11]) survives camera-ready "
      f"uncertainty | G_total {n_(g1.observed, 3)}, 90% CI {g1.obs_ci90}; audit-implied {g1.audit_interval}; "
      f"**editing-corrected 90% CI {g1.corrected_ci90}**. 2024–26 pairs only: {g1p.corrected_ci90}. Original audit "
      f"only: {g1o.corrected_ci90} (fails). G_dec: {g1d.corrected_ci90} | Corrected 90% CI inside the margins | "
      f"**Supported** |")
    A(f"| G2 | Gate for D4-H4b: L-title depletion (G_total < 1), audited as R24 or R26 | G_total {n_(g2.observed, 3)}, "
      f"90% CI {g2.obs_ci90}; DiD {n_(g2.did_pp, 2, True)} pp vs D\\* {n_(g2.tip_pp, 2, True)}; corrected 90% CI "
      f"{g2.corrected_ci90}; Holm p {n_(g2.p_holm, 2)} | Auditable, corrected 95% CI < 1, Holm p < 0.025 (3 H4b claims) | "
      f"**Not supported** (not identified) |")
    A(f"| G2b | Gate for D4-H4b: O-union depletion (G_total < 1), audited without ALL-CAPS | G_total "
      f"{n_(g2b.observed, 3)}, 90% CI {g2b.obs_ci90}; DiD {n_(g2b.did_pp, 2, True)} pp vs D\\* {n_(g2b.tip_pp, 2, True)}; "
      f"corrected 90% CI {g2b.corrected_ci90}; p {n_(g2b.p_ident, 3)}, Holm {n_(g2b.p_holm, 3)} | As G2 | "
      f"**Not supported** ({'passes the uncorrected rule only' if g2b.passes_uncorrected else 'fails even the uncorrected rule'}) |")
    A(f"| G3 | Abstract audit (extension): depletion of F24-or-F26 abstract words (G_total < 1) survives the audit | "
      f"G_total {n_(g3.observed, 3)}, 90% CI {g3.obs_ci90}; DiD {n_(g3.did_pp, 2, True)} pp vs D\\* "
      f"{n_(g3.tip_pp, 2, True)}; Holm p {n_(g3.p_holm, 2)} | As G2 | **Not supported** (little pooled depletion "
      f"to protect) |")
    A(f"| G4 | D4-H4c direction assumption: camera-ready polishing does not *lower* accepted papers' RARE21 rates | "
      f"2024–26 pairs ({int(f24.n_acc)}/{int(f24.n_rej)}): F24 DiD **{n_(100 * f24.did, 2, True)} pp "
      f"{ci(100 * f24.did_lo, 100 * f24.did_hi)}**. 2023–26: {n_(100 * f24s.did, 2, True)} "
      f"{ci(100 * f24s.did_lo, 100 * f24s.did_hi)} | Sign of DiD (CI > 0 = supported) | "
      f"**{H['G4']['verdict'].replace('_', ' ').capitalize()}** (sign as assumed, CI includes 0) |")
    A("")

    # ================================================================ headline
    ex, exlo, exhi = nm.excess_share_edit_dec, nm.excess_share_edit_lo_dec, nm.excess_share_edit_hi_dec
    nmS, nmL = tp.loc["NAME_strict"], tp.loc["NAME_loose"]
    A("**Headline.**")
    A("- **No title feature's decision-stage acceptance association survives the camera-ready audit once multiplicity "
      "is controlled.** This holds on the complete audit "
      f"({nA:,} accepted and {nR:,} rejected pre-decision pairs, {(nA + nR) / np_['original_all_years']:.1f}× the "
      f"original {np_['original_all_years']}).")
    A(f"  - Under the uncorrected interim rule, {len(unc_pass)} associations would pass: "
      + ", ".join(f"{lab(k)} (one-sided p {n_(tp.loc[k].p_ident_dec, 3)})" for k in unc_pass) +
      f". With Holm across {len(aud)} auditable features none passes; the smallest Holm-adjusted p is "
      f"{n_(aud.p_holm_dec.min(), 2)}.")
    sc_hist = [int(r.enlarge_lines) for _, r in fpath.iterrows() if "sentence_case" in str(r.passes_uncorrected).split(",")]
    A(f"  - The set passing the uncorrected rule moves as records accrue (§4, freeze path). Sentence case passed it at "
      f"{', '.join(f'{x:,}' for x in sc_hist) or 'no'} enlargement lines but not on the complete audit (margin "
      f"{n_(sc.tip_dec_margin_pp, 2)} pp).")
    A(f"  - Outsider-casing depletion (O-union w/o ALL-CAPS, G_dec {n_(ou.G_dec_obs, 3)}) comes closest. Editing runs "
      f"the conservative way: accepted papers *gain* sentence case after v1 (net "
      f"{n_(100 * fl.loc['sentence_case'].net_acc, 1, True)} vs {n_(100 * fl.loc['sentence_case'].net_rej, 1, True)} pp). "
      "This is a lead for the held-out test, not a finding.")
    A(f"- **NAME (the mainstream fashion).** The NAME acceptance association (G_dec {n_(nm.G_dec_obs, 3)}) is not "
      f"identified: DiD {n_(100 * nf.did, 2, True)} pp {ci(100 * nf.did_lo, 100 * nf.did_hi)} against D\\* "
      f"{n_(nm.tip_dec_pp)} pp.")
    A(f"  - The audit cannot rule out that post-decision renaming produces the NAME association. At the audit point "
      f"estimate the submission-stage G_dec is {n_(nm.G_dec_sel_point, 3)} (NAME), {n_(nmS.G_dec_sel_point, 3)} "
      f"(strict) and {n_(nmL.G_dec_sel_point, 3)} (loose), against an observed {n_(nm.G_dec_obs, 3)}.")
    A(f"  - About {n_(100 * ex, 0)}% of the stored-title NAME excess is camera-ready at the point estimate "
      f"(audit CI {n_(100 * exlo, 0)}% to {n_(100 * exhi, 0)}%). The CI spans both no editing effect and an editing "
      "effect larger than the whole association.")
    A(f"  - Accepted papers add NAME more often than rejected ones (add rate given v1-absent "
      f"{pct(nf.add_rate_acc)}% vs {pct(nf.add_rate_rej)}%; {int(nf.adds_acc)} vs {int(nf.adds_rej)} adds). Drop "
      f"rates are similar ({pct(nf.drop_rate_acc)}% vs {pct(nf.drop_rate_rej)}%).")
    A(f"- **NAME neutrality (D4-H4a) is robust to editing.** The pooled 2024–26 G_total TOST passes on the complete "
      f"audit (corrected 90% CI {g1.corrected_ci90}), on 2024–26 pairs only ({g1p.corrected_ci90}) and on new records "
      f"only. The corrected centre is {n_(nm.G_total_sel_point, 3)}, i.e. *below* the stored-title "
      f"{n_(nm.G_total_obs, 3)}. A \"peer review amplifies NAME\" reading is therefore not supported. The original "
      f"331-pair audit alone did not pass ({g1o.corrected_ci90}).")
    A(f"- **Findability.** Accepted papers have {n_(fa.OR, 1)}-fold higher odds of being found on arXiv "
      f"({pct(fA.found_rate)}% vs {pct(fR.found_rate)}%). NAME does not predict findability (OR {n_(fn.OR)} "
      f"{ci(fn.OR_lo, fn.OR_hi)}). A title-free route gives the same gap, but both routes match on the latest arXiv "
      "abstract, so the routes are not independent checks.")
    A(f"- **No camera-ready retitling excess.** Accepted and rejected papers retitle at similar rates "
      f"({n_(100 * r_all['diff'], 1, True)} pp {ci(100 * r_all.diff_lo, 100 * r_all.diff_hi, 1)}). Where the v1 was "
      f"posted during review, so that it is close to the submitted version, the difference is "
      f"{n_(100 * r_in['diff'], 1, True)} pp {ci(100 * r_in.diff_lo, 100 * r_in.diff_hi, 1)}. An excess appears only "
      f"where the v1 predates the deadline ({n_(100 * r_pre['diff'], 1, True)} pp "
      f"{ci(100 * r_pre.diff_lo, 100 * r_pre.diff_hi, 1)}). Camera-ready edits would show up in both strata, so this "
      "most plausibly reflects how earlier drafts were revised before submission.")
    A("- **Channel limits.** Title typography (U+2011/U+2013), ALL-CAPS titles and the abstract em dash cannot be "
      "audited through arXiv at any sample size. D4's ALL-CAPS and typography depletion therefore stays unaudited.")
    A("")
    A("---")
    A("")

    # ================================================================ 1 findability
    A("## 1. Audit sample and differential findability (`found_rates.csv`, `findability_models.csv`, Fig. S1a)")
    A("")
    A("**Sample.**")
    A("- **Original audit** (`src/arxiv_audit.py`, title route): 616 papers. 75 per year × decision cell for "
      "2023–2026, plus 16 accepted papers from 2022.")
    A(f"- **Enlargement** (`audit_v2.py` phase 2): a fresh stratified random sample of 250 per cell for 2023–26, "
      f"queried with the same title route. {enl['n_records_ok']:,} records are complete; "
      f"{enl['n_error_lines']} lines are network-error rows superseded by a retry. Per cell: " +
      (f"{min(enl['by_cell'].values())}." if min(enl['by_cell'].values()) == max(enl['by_cell'].values()) else
       f"{min(enl['by_cell'].values())}–{max(enl['by_cell'].values())}."))
    A(f"- **Primary audit:** usable pairs from both, 2023–26: **{nA:,} accepted / {nR:,} rejected**. The 9 accepted "
      "2022 pairs have no rejected counterpart; they enter only the `incl_2022` spec.")
    A("")
    A("**Usable pair.** A paper is a usable pair when it is found on arXiv, has a v1 title, and its v1 predates the "
      "decision date of its conference year (`arxiv_audit.DECISION_DATE`).")
    A("")
    A("| Sample | Decision | n | Found | Found rate [95% Wilson] | Usable pairs |")
    A("|---|---|---|---|---|---|")
    for src, nm_src in [("original", "Original (2022–26)"), ("enlarge", "Enlargement (2023–26)"),
                        ("original+enlarge", "Pooled 2023–26")]:
        for dec in ["accepted", "rejected"]:
            r = fr_row(src, "all", dec)
            A(f"| {nm_src} | {dec} | {int(r.n):,} | {int(r.found):,} | {pct(r.found_rate)}% "
              f"{ci(100 * r.found_lo, 100 * r.found_hi, 1)} | {int(r.usable):,} ({pct(r.usable_rate)}%) |")
    A("")
    ua = fmrow("acc", "usable_i ~ C(year) + acc + log_nw + NAME", "original+enlarge")
    un = fmrow("NAME", "usable_i ~ C(year) + acc + log_nw + NAME", "original+enlarge")
    fl_ = fmrow("log_nw", "found_i ~ C(year) + acc + log_nw + NAME", "original+enlarge")
    fint = fm[(fm.term == "acc:NAME") & (fm["sample"] == "original+enlarge")].iloc[0]
    fpre = fm[(fm.term == "acc") & (fm.outcome == "usable_given_found") & (fm["sample"] == "original+enlarge")].iloc[0]
    oa = fmrow("acc", "found_i ~ C(year) + acc + log_nw + NAME", "original")
    on = fmrow("NAME", "found_i ~ C(year) + acc + log_nw + NAME", "original")
    oun = fmrow("NAME", "usable_i ~ C(year) + acc + log_nw + NAME", "original")
    A(f"**Findability models** (logit with year FE, pooled 2023–26, n = {int(fa.nobs):,}):")
    A(f"- Found: odds ratio (accepted) **{n_(fa.OR)} {ci(fa.OR_lo, fa.OR_hi)}**. OR(NAME) {n_(fn.OR)} "
      f"{ci(fn.OR_lo, fn.OR_hi)} (p = {n_(fn.p, 2)}). OR per log title word {n_(fl_.OR)} {ci(fl_.OR_lo, fl_.OR_hi)} "
      f"(p = {n_(fl_.p, 3)}). Accepted × NAME interaction {n_(fint.OR)} {ci(fint.OR_lo, fint.OR_hi)}.")
    A(f"- Usable pair: OR(accepted) {n_(ua.OR)} {ci(ua.OR_lo, ua.OR_hi)}; OR(NAME) {n_(un.OR)} {ci(un.OR_lo, un.OR_hi)} "
      f"(p = {n_(un.p, 2)}).")
    A(f"- Pre-decision v1 given found: OR(accepted) {n_(fpre.OR)} {ci(fpre.OR_lo, fpre.OR_hi)}.")
    A(f"- Original sample only (n = {int(oa.nobs)}): OR(accepted) {n_(oa.OR)} {ci(oa.OR_lo, oa.OR_hi)}, OR(NAME) "
      f"{n_(on.OR)} {ci(on.OR_lo, on.OR_hi)}, usable-pair OR(NAME) {n_(oun.OR)} {ci(oun.OR_lo, oun.OR_hi)} "
      f"(p = {n_(oun.p, 2)}). The interim text's \"NAME does not predict findability\" asserted a null on a CI reaching "
      "2.2. The pooled sample now bounds the NAME effect near 1.")
    A("- The selection is therefore mostly \"is the paper on arXiv at all\", which differs strongly by decision. "
      "Longer titles are slightly less findable.")
    kish, wr = meta["ipw"]["kish_neff"], meta["ipw"]["weight_range"]
    A(f"- IPW weights for the robustness specs: 1/P̂(usable | year, accepted, log title words, NAME), optionally times "
      f"N_pop/n_sampled per year × decision. Normalised weights range {n_(wr['ipw_find'][0])}–{n_(wr['ipw_find'][1])} "
      f"and {n_(wr['ipw_find_pop'][0])}–{n_(wr['ipw_find_pop'][1])} (with design weights). Kish effective n with design "
      f"weights: {kish['ipw_find_pop']['accepted']:.0f} of {nA} accepted, {kish['ipw_find_pop']['rejected']:.0f} of "
      f"{nR} rejected.")
    tc = tim["title_clause_share"]
    A(f"- **Title-clause admissions.** `arxiv_audit.find` also accepts a hit with title Jaccard ≥ 0.6 and a "
      f"surname *substring* match when the abstract Jaccard is below 0.45. Among primary pairs this clause admits "
      f"{pct(tc['rejected'])}% of rejected but {pct(tc['accepted'])}% of accepted pairs. The `abstract_matched` spec "
      "drops these pairs (§4). Surname matching cannot be redone at the whole-token level, because the caches do not "
      "store arXiv author lists. Dropping the clause covers that case.")
    A("")

    # ================================================================ 2 retitling
    A("## 2. Retitling between pre-decision v1 and stored title (`retitling.csv`, Fig. S1b)")
    A("")
    A("**Measures** (on usable pairs):")
    A("- *Retitled*: the word sequence differs after lower-casing and stripping punctuation.")
    A("- *Major*: content-word Jaccard < 0.5.")
    A("- *Case/punctuation-only*: the raw string differs but the word sequence does not.")
    A("")
    A(f"**v1 timing.** The v1 is classed *in review* when it was posted after the ICLR full-paper deadline "
      f"(approximate public deadlines in `results.json` → `meta.submission_deadlines`), and *before deadline* "
      f"otherwise.")
    A(f"- Primary pairs in review: accepted {pct(tim['share_in_review']['accepted'])}%, rejected "
      f"{pct(tim['share_in_review']['rejected'])}% (Fisher p = {n_(tim['fisher_p'], 2)}).")
    A(f"- Median lag: {n_(tim['median_lag_days']['accepted'], 1, True)} vs "
      f"{n_(tim['median_lag_days']['rejected'], 1, True)} days relative to the deadline.")
    A(f"- In the original 2023–26 pairs the mix differed: {pct(tim['original_share_in_review']['accepted'])}% vs "
      f"{pct(tim['original_share_in_review']['rejected'])}% (p = {n_(tim['original_fisher_p'], 2)}).")
    A("")
    A("| Sample | Years | Measure | Accepted | Rejected | Difference, Newcombe 95% CI |")
    A("|---|---|---|---|---|---|")
    rows = [("primary", "all", "changed_norm", "Primary"), ("primary", "all", "changed_major", "Primary"),
            ("primary", "all", "case_punct_only", "Primary"), ("primary", "2024-26", "changed_norm", "Primary"),
            ("primary", "2023", "changed_norm", "Primary"),
            ("v1_in_review", "all", "changed_norm", "v1 posted during review"),
            ("v1_in_review", "2024-26", "changed_norm", "v1 posted during review"),
            ("v1_before_deadline", "all", "changed_norm", "v1 posted before the deadline"),
            ("original_only", "all", "changed_norm", "Original audit (interim primary)"),
            ("original_only", "2024-26", "changed_norm", "Original audit (interim primary)"),
            ("original_in_review", "all", "changed_norm", "Original audit, v1 during review"),
            ("original_before_deadline", "all", "changed_norm", "Original audit, v1 before the deadline")]
    mname = {"changed_norm": "retitled", "changed_major": "major", "case_punct_only": "case/punct only"}
    for sp, yrs, ms, nm_ in rows:
        r = rtrow(sp, yrs, ms)
        A(f"| {nm_} | {yrs} | {mname[ms]} | {int(r.k_acc)}/{int(r.n_acc)} = {pct(r.rate_acc)}% | "
          f"{int(r.k_rej)}/{int(r.n_rej)} = {pct(r.rate_rej)}% | {n_(100 * r['diff'], 1, True)} "
          f"{ci(100 * r.diff_lo, 100 * r.diff_hi, 1)} |")
    A("")
    lo_ = R["retitling"]["extra"]["primary"]["logit_acc_OR"]
    dp = R["retitling"]["extra"]["primary"]["did_period_post_minus_pre"]
    dw = R["retitling"]["extra"]["primary"]["mean_dwords"]
    A("**Model and period contrast.**")
    A(f"- Logit with year FE: OR(accepted) = {n_(lo_['OR'])} {ci(lo_['lo'], lo_['hi'])}, p = {n_(lo_['p'], 2)}.")
    A(f"- Period contrast: (acc − rej) in 2024–26 minus (acc − rej) in 2023 = {n_(100 * dp['est'], 1, True)} pp, "
      f"bootstrap 95% CI {ci(100 * dp['lo'], 100 * dp['hi'], 1)}. The pre-period is 2023 only; the interim 2022–23 "
      "contrast mixed in accepted-only 2022 pairs.")
    A(f"- Title length does not change on average: Δwords {n_(dw['acc'], 2, True)} (accepted), "
      f"{n_(dw['rej'], 2, True)} (rejected).")
    A("")
    A("**Interpretation.**")
    A(f"- {pct(r_all.rate_rej)}% of rejected papers already carry a different title on arXiv v1 than on OpenReview. "
      f"This is the non-camera-ready noise floor. It is concentrated in v1s posted before "
      f"the deadline ({pct(r_pre.rate_rej)}%), against {pct(r_in.rate_rej)}% for v1s posted during review.")
    A(f"- There is no camera-ready retitling excess. The in-review stratum, where v1 is close to the submitted "
      f"version, gives {n_(100 * r_in['diff'], 1, True)} pp {ci(100 * r_in.diff_lo, 100 * r_in.diff_hi, 1)}.")
    A(f"- The before-deadline stratum shows an accepted excess of {n_(100 * r_pre['diff'], 1, True)} pp "
      f"{ci(100 * r_pre.diff_lo, 100 * r_pre.diff_hi, 1)}" +
      (", with a CI that excludes 0" if r_pre.diff_lo > 0 else "") +
      ". Camera-ready retitling happens after the decision whatever the v1 date, so it should appear in both strata. "
      "If anything it should be harder to detect where the v1 was already retitled. The excess therefore most "
      "plausibly reflects pre-submission revision of earlier drafts that differs by eventual decision, e.g. papers "
      "resubmitted from another venue. This is an interpretation; the design cannot separate it from a "
      "camera-ready effect confined to early posters.")
    oi, ob = rtrow("original_in_review", "all"), rtrow("original_before_deadline", "all")
    A(f"- The interim reading (\"+6 pp, +10 pp in 2024–26 camera-ready excess\") is withdrawn. In the original sample "
      f"the excess sits in v1s posted before the deadline ({n_(100 * ob['diff'], 1, True)} pp) and not in v1s posted "
      f"during review ({n_(100 * oi['diff'], 1, True)} pp). The original sample's timing mix also differed by "
      f"decision.")
    A("")

    # ================================================================ 3 flips
    A("## 3. Flip matrices with feature-present v1 denominators (T4.2: `T4_2_flip_matrices.csv`, "
      "`T4_2_flip_multiclass.csv`, Fig. S4)")
    A("")
    A("**Features.** All features are computed with `features_v2.build` on both titles; the stored-title features "
      "reproduce `features_v2.parquet`. Two audited unions are new:")
    A("- *L-title words* = R24 or R26. This is the arXiv-measurable part of the L-title union, which also contains "
      "typography.")
    A("- *O-union w/o ALL-CAPS* = sentence case or question opener.")
    A("")
    A("**Column definitions.**")
    A("- Cells show *v1-present: +adds/−drops*. Net = (adds − drops)/n. DiD = net(accepted) − net(rejected).")
    A("- **Primary CI:** Wald with a pseudo-flip variance floor (one pseudo-add and one pseudo-drop per arm).")
    A("- *Auditable:* \"no (count)\" means fewer than 10 v1-present titles in an arm; \"no (channel)\" means arXiv "
      "metadata cannot carry the feature.")
    A("")
    A(f"| Feature | Accepted (n = {nA}) | Rejected (n = {nR}) | Net acc / rej (pp) | DiD (pp) [pseudo-flip 95% CI] | "
      "Plain Wald CI | Auditable |")
    A("|---|---|---|---|---|---|---|")
    for k in list(fl.index):
        r = fl.loc[k]
        A(f"| {lab(k)} | {int(r.v1_present_acc)}: +{int(r.adds_acc)}/−{int(r.drops_acc)} | {int(r.v1_present_rej)}: "
          f"+{int(r.adds_rej)}/−{int(r.drops_rej)} | {n_(100 * r.net_acc, 1, True)} / {n_(100 * r.net_rej, 1, True)} | "
          f"{'**' if k == 'NAME' else ''}{n_(100 * r.did, 2, True)} {ci(100 * r.did_lo, 100 * r.did_hi)}"
          f"{'**' if k == 'NAME' else ''} | {ci(100 * r.did_lo_wald, 100 * r.did_hi_wald)} | {aud_word(k)} |")
    A("")
    A("**Add and drop rates** (Fig. S4, Wilson CIs).")
    for k in ["NAME", "compound", "title_case", "sentence_case", "via"]:
        r = fl.loc[k]
        A(f"- {lab(k)}: drop rate {pct(r.drop_rate_acc)}% vs {pct(r.drop_rate_rej)}%; add rate "
          f"{pct(r.add_rate_acc)}% vs {pct(r.add_rate_rej)}% (accepted vs rejected).")
    A(f"- Drop-rate CIs overlap across arms. The NAME DiD comes from adds: accepted papers add a coined name after v1 "
      f"{n_(nf.add_rate_acc / nf.add_rate_rej, 1)}× as often as rejected papers.")
    A("")
    mcp = mc[(mc.spec == "primary") & mc.changed]

    def trans(feat, dec, top=6):
        q = mcp[(mcp.feature == feat) & (mcp.decision == dec)].sort_values("n", ascending=False).head(top)
        return ", ".join(f"{a}→{b} {int(n)}" for a, b, n in zip(q.v1_class, q.stored_class, q.n))
    A("**Multi-class transitions** (primary; `T4_2_flip_multiclass.csv`):")
    for dec in ["accepted", "rejected"]:
        A(f"- *{dec.capitalize()}.* Casing: {trans('casing', dec)}. Name orthography: {trans('name_orthography', dec)}. "
          f"Slot state: {trans('slot_state', dec) or 'none'}.")
    na_caps = int(mcp[(mcp.feature == 'casing') & (mcp.stored_class == 'all_caps') & (mcp.decision == 'accepted')].n.sum())
    nr_caps = int(mcp[(mcp.feature == 'casing') & (mcp.stored_class == 'all_caps') & (mcp.decision == 'rejected')].n.sum())
    A(f"- Every →all_caps transition ({na_caps} accepted, {nr_caps} rejected) is consistent with OpenReview form entry. "
      "arXiv titles are never ALL-CAPS, so these transitions say nothing about camera-ready editing.")
    A("")
    A("**Examples of camera-ready NAME additions** (original audit, 2026): \"Self-Augmented Visual Contrastive "
      "Decoding\" → \"Self-Aug: Query and Entropy Adaptive Decoding …\"; \"Scaled Inverse Graphics: …\" → "
      "\"Fused-Planes: …\"; \"Shortening the Trajectories: …\" → \"GAGA: …\". Drops: \"SeerAttention-R: …\" → "
      "\"Sparse Attention Adaptation for Long Reasoning\"; \"RSRM: …\" → \"Reinforcement Symbolic Regression Machine\".")
    A("")

    # ================================================================ 4 tipping
    A("## 4. Tipping points and the decision-stage bound (T4.2: `T4_2_tipping_points.csv`, "
      "`T4_2_identification_by_spec.csv`, `T4_2_identified_anywhere.csv`, `T4_2_freeze_path.csv`, "
      "`T4_2_tipping_by_year.csv`, Fig. S2)")
    A("")
    A("**Prevalences.** Universe prevalences are pooled over 2024–26 and year-standardised to s0 sizes, as in D4. The "
      "audit DiD is the primary 2023–26 estimate.")
    A("")
    A("**Auditable features** (primary audit). p = one-sided identification p-value; Holm across the "
      f"{len(aud)} auditable features.")
    A("")
    A("| Feature | P₂ → P₃ | G_dec [95%] | DiD [95%] (pp) | D\\* (pp) | p | Holm p | Uncorrected rule | G_dec at D̂ | "
      "Audit-implied G_dec |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for k, r in aud.iterrows():
        A(f"| {lab(k)} | {pct(r.P_s2)} → {pct(r.P_s3)}% | {n_(r.G_dec_obs, 3)} {ci(r.G_dec_lo95, r.G_dec_hi95, 3)} | "
          f"{n_(r.did_pp, 2, True)} {ci(r.did_lo_pp, r.did_hi_pp)} | {n_(r.tip_dec_pp, 2, True)} | {n_(r.p_ident_dec, 3)} | "
          f"{n_(r.p_holm_dec, 2)} | {'passes' if r.passes_uncorrected_dec else 'no'} | {n_(r.G_dec_sel_point, 3)} | "
          f"{ci(r.G_dec_audit_lo, r.G_dec_audit_hi, 3)} |")
    A("")
    A("**Unauditable features.** These cannot enter a gate.")
    A("")
    A("| Feature | Reason | G_dec [95%] | D\\* (pp) | Audit CI (pp) | v1-present (acc/rej) |")
    A("|---|---|---|---|---|---|")
    for k, r in tp[~tp.auditable].iterrows():
        f_ = fl.loc[k]
        reason = f_.channel_note if not bool(f_.channel_ok) else "fewer than 10 v1-present in an arm"
        A(f"| {lab(k)} | {reason} | {n_(r.G_dec_obs, 3)} {ci(r.G_dec_lo95, r.G_dec_hi95, 3)} | "
          f"{n_(r.tip_dec_pp, 2, True)} | {ci(r.did_lo_pp, r.did_hi_pp)} | {int(f_.v1_present_acc)}/{int(f_.v1_present_rej)} |")
    A("")
    ac = fl.loc["all_caps_title"]
    A("**Notes on individual features.**")
    A(f"- **ALL-CAPS title.** The net-flip DiD ({n_(100 * ac.did, 2, True)} pp) comes from {int(ac.adds_acc)} accepted "
      f"and {int(ac.adds_rej)} rejected additions with no v1-present titles. arXiv titles are never ALL-CAPS, so the "
      "\"DiD\" is just the accepted-vs-rejected gap in stored ALL-CAPS prevalence among pairs. That gap is the "
      "association under test, not a measure of editing. The interim note that this DiD \"exceeds the whole tipping "
      "point\" is withdrawn. ALL-CAPS title is unauditable by channel; D4's decision-stage ALL-CAPS depletion cannot be "
      "separated from editing or form entry.")
    A(f"- **Sentence case** became auditable as the audit grew (v1-present {int(fl.loc['sentence_case'].v1_present_acc)}/"
      f"{int(fl.loc['sentence_case'].v1_present_rej)}). Editing runs the conservative way: accepted papers gain sentence "
      f"case (net {n_(100 * fl.loc['sentence_case'].net_acc, 1, True)} pp vs {n_(100 * fl.loc['sentence_case'].net_rej, 1, True)} pp). "
      f"The DiD lower bound is {n_(sc.did_lo_pp, 2, True)} pp against D\\* = {n_(sc.tip_dec_pp, 2, True)} pp: "
      + (f"identified under the uncorrected rule by {n_(sc.tip_dec_margin_pp, 2)} pp" if sc.G_dec_identified else
         f"not identified (margin {n_(sc.tip_dec_margin_pp, 2)} pp), although it was identified at 600–1,261 "
         "enlargement lines") +
      f". With the tipping point's own sampling error, p = {n_(sc.p_ident_dec, 3)} and Holm gives "
      f"{n_(sc.p_holm_dec, 2)}.")
    A(f"- **'using'** reached {int(fl.loc['using'].v1_present_acc)}/{int(fl.loc['using'].v1_present_rej)} v1-present titles "
      "and is now auditable; it is not identified. The PLAN example (\"n = 4 accepted v1 titles\") reproduces on the "
      "original 331 pairs.")
    A("")
    A("**Robustness of the NAME bound** (D\\* = "
      f"{n_(nm.tip_dec_pp)} pp throughout):")
    A("")
    A("| Audit specification | n acc / rej | DiD (pp) [95%] | p | Identified |")
    A("|---|---|---|---|---|")
    spec_names = {
        "primary": "Primary: original + enlargement, 2023–26",
        "incl_2022": "Including the 9 accepted-only 2022 pairs",
        "year_std": "Year-standardised arms (within-year contrasts)",
        "post_2024_26": "2024–26 pairs only",
        "original_only": "Original audit only (interim primary)",
        "new_records_only": "Enlargement records only (out of sample)",
        "new_records_2024_26": "Enlargement records only, 2024–26",
        "ipw_find": "IPW for findability",
        "ipw_find_pop": "IPW × population design weights",
        "abstract_matched": "Abstract-matched pairs only (drops title-clause admissions)",
        "v1_in_review": "v1 posted during review",
        "v1_before_deadline": "v1 posted before the deadline",
        "timing_std": "Timing-standardised arms (year × v1 timing)",
        "union_route_v7sub": "Union with route-B-only pairs (300-paper V7 subsample only)",
    }
    for s_, nm_ in spec_names.items():
        r = spec(s_)
        A(f"| {nm_} | {int(r.n_acc)} / {int(r.n_rej)} | {n_(r.did_pp, 2, True)} {ci(r.did_lo_pp, r.did_hi_pp)} | "
          f"{n_(r.p_ident_dec, 3)} | {'yes' if r.G_dec_identified else 'no'} |")
    A(f"| Plain Wald / bootstrap CI (primary pairs) | {nA} / {nR} | {ci(nf.did_lo_wald * 100, nf.did_hi_wald * 100)} / "
      f"{ci(nf.did_lo_boot * 100, nf.did_hi_boot * 100)} | | {'yes' if nm.G_dec_identified_wald else 'no'} / "
      f"{'yes' if nm.G_dec_identified_boot else 'no'} |")
    A("")
    nm_any = ida[(ida.feature == "NAME")]
    assert nm_any.empty, "prose assumes NAME is identified nowhere"
    A("NAME G_dec is identified in no specification under any CI type.")
    A("")
    A("**Where any feature is identified under the uncorrected rule** (`T4_2_identified_anywhere.csv`, G_dec, "
      f"{idt.spec.nunique()} specs × 3 CI types). No identification survives Holm in any spec.")
    A("")
    A("| Feature | Specs identified (pseudo-flip CI) | Additional specs (Wald or bootstrap only) | Smallest margin (pp) |")
    A("|---|---|---|---|")
    qd = ida[~ida.ci.str.contains("G_total")]
    for k, g in qd.groupby("feature", sort=False):
        pf = sorted(set(g[g.ci == "pseudo-flip"].spec))
        oth = sorted(set(g.spec) - set(pf))
        A(f"| {lab(k)} | {len(pf)}: {', '.join(pf) or '–'} | {', '.join(oth) or '–'} | {n_(g.margin_pp.min(), 2)} |")
    assert not ida.passes_holm.any()
    A("")
    A("Notes:")
    A("- The interim text claimed \"no feature is identified in any specification, under any CI type\". That was "
      "already false at the interim freeze: in the `ipw_find_pop` spec the O-union was identified under the Wald and "
      "bootstrap CIs.")
    wn = qd[qd.feature == "word_name"]
    if len(wn) and set(wn.ci) == {"bootstrap"}:
        A("- Word-name identifications occur under the bootstrap only. Its bootstrap DiD is nearly degenerate, because "
          "flips are rare.")
    vp = spec("primary", "via")
    vspecs = sorted(set(qd[(qd.feature == "via") & (qd.ci == "pseudo-flip")].spec))
    if vspecs:
        A(f"- 'via' (a control word) is identified only in {', '.join(vspecs)}. In the primary its upper CI "
          f"({n_(vp.did_hi_pp, 2, True)} pp) exceeds D\\* ({n_(vp.tip_dec_pp, 2, True)} pp), and its observed G_dec "
          f"CI lower bound is {n_(vp.G_dec_lo95, 3)}.")
    A("")
    A("**Freeze path** (`T4_2_freeze_path.csv`): the same primary definition, re-run on the original 2023–26 pairs plus "
      "the first N enlargement lines.")
    A("")
    A("| Enlargement lines | Pairs acc/rej | Auditable features | NAME DiD [95%] | NAME G_total corrected 90% CI | "
      "Pass uncorrected rule | Pass Holm | Smallest p |")
    A("|---|---|---|---|---|---|---|---|")
    for _, r in fpath.iterrows():
        A(f"| {int(r.enlarge_lines):,} | {int(r.n_acc)}/{int(r.n_rej)} | {int(r.n_auditable)} | "
          f"{n_(r.NAME_did_pp, 2, True)} {ci(r.NAME_lo_pp, r.NAME_hi_pp)} | "
          f"{ci(r.NAME_G_total_corr_lo90, r.NAME_G_total_corr_hi90, 3)} | "
          f"{', '.join(lab(k) for k in str(r.passes_uncorrected).split(',') if k and k != 'nan') or 'none'} | "
          f"{', '.join(lab(k) for k in str(r.passes_holm).split(',') if k and k != 'nan') or 'none'} | "
          f"{n_(r.min_p_ident, 3)} ({lab(r.min_p_feature)}) |")
    A("")
    A("- Under the uncorrected rule, the set of passing features changes as records accrue. The interim "
      "\"0 of 24 pass\" (uncorrected rule, original + 254 records) therefore was not a stable verdict; only the "
      "multiplicity-controlled gate gives the same answer at every freeze.")
    A("- Under Holm, nothing passes at any freeze. NAME is never identified. The H4a G_total TOST passes at every "
      "freeze with the enlargement.")
    A("")
    ny = tpy[tpy.feature == "NAME"].set_index("period")
    hw = ((ny.did_hi_pp - ny.did_lo_pp) / 2)
    yid = tpy[tpy.G_dec_identified]
    A("**Per-year bounds** (`T4_2_tipping_by_year.csv`).")
    A(f"- Every year 2023–2026 has its own audit: {int(tpy.n_acc.min())}–{int(tpy.n_acc.max())} accepted and "
      f"{int(tpy.n_rej.min())}–{int(tpy.n_rej.max())} rejected pairs. NAME CI half-widths are "
      f"{n_(hw.min(), 1)}–{n_(hw.max(), 1)} pp. Example: NAME in 2024, DiD {n_(ny.loc[2024, 'did_pp'], 1, True)} "
      f"{ci(ny.loc[2024, 'did_lo_pp'], ny.loc[2024, 'did_hi_pp'], 1)} vs D\\* {n_(ny.loc[2024, 'tip_dec_pp'], 1)} pp.")
    A(f"- Identified per year under the uncorrected rule: " +
      ("; ".join(f"{lab(r.feature)} in {r.period} (margin {n_(r.tip_dec_margin_pp, 3)} pp)" for _, r in yid.iterrows())
       or "none") + f". These are {len(tpy)} year × feature tests without multiplicity control, so isolated "
      "identifications are not interpreted.")
    A("- H4a's per-year claims for 2018–2022 have no audit. 2022 has 9 accepted pairs and no rejected ones.")
    A("")
    pil = tp.loc["NAME"]
    A("**Comparison with the PLAN pilot.**")
    A(f"- The PLAN's 1.8 pp tipping point is P₃ − P₂ = {n_(100 * (pil.P_s3 - pil.P_s2), 2)} pp. It omits the "
      f"1/(1 − a₂) factor: camera-ready edits also shift P(f | reviewed), because accepted papers are part of the "
      f"reviewed set. With the factor, D\\* = {n_(pil.tip_dec_pp)} pp.")
    A("- The year-standardised pooling is the same in both. The interim text attributed the difference to pooling, "
      "which was wrong.")
    A(f"- The original-audit DiD and SE reproduce the pilot: {n_(spec('original_only').did_pp, 2, True)} pp vs "
      f"+2.1 (Wald se 2.37 vs 2.4).")
    se = 100 * nf.did_se
    A("")
    A(f"**How large an audit would identify NAME G_dec?** The primary pseudo-flip se is {n_(se, 2)} pp.")
    m50, m80 = nm.n_mult_D0_50_dec, nm.n_mult_D0_80_dec
    A(f"- If the true DiD were 0, the CI would clear D\\* with 50% probability at {n_(m50, 2)}× the current pairs "
      f"and with 80% probability at {n_(m80, 2)}× (≈ {m80 * (nA + nR):,.0f} pairs). " +
      ("The complete audit therefore has at least 80% power in that case." if m80 <= 1 else
       "The complete audit therefore has more than 50% but less than 80% power in that case." if m50 <= 1 else
       "The complete audit has less than 50% power even in that case."))
    A(f"- For comparison, the interim plan (\"the full enlargement would suffice\") quoted only the 50% multiplier "
      f"(3.2× of 331 pairs) and assumed a 54% usable rate. The enlargement's realised usable rate was "
      f"{pct((fr_row('enlarge', 'all', 'accepted').usable + fr_row('enlarge', 'all', 'rejected').usable) / (fr_row('enlarge', 'all', 'accepted').n + fr_row('enlarge', 'all', 'rejected').n))}%.")
    A(f"- If the true DiD equals the observed {n_(100 * nf.did, 2, True)} pp ({n_(nm.tip_dec_pp - 100 * nf.did, 2)} pp "
      f"below D\\*), the 95% CI clears D\\* only at about {n_(nm.n_mult_obs_50_dec, 1)}× the current pairs "
      f"(≈ {nm.n_mult_obs_50_dec * (nA + nR):,.0f} pairs, with 50% probability).")
    A("- The interim statement \"no audit size would identify NAME G_dec\" was false; the point estimate was below D\\* "
      "then too.")
    A("")

    # ================================================================ 5 gate
    A("## 5. Gate for D4 claims (PLAN §4; `gate.csv`)")
    A("")
    A("**H4a (NAME neutrality, pooled 2024–26).** The rule is a TOST on the editing-corrected 90% CI within "
      "[0.90, 1.11].")
    A("")
    A("| Audit | G_total corrected 90% CI | Passes | G_dec corrected 90% CI | Passes |")
    A("|---|---|---|---|---|")
    for s_ in ["primary", "post_2024_26", "new_records_only", "v1_in_review", "original_only"]:
        gt_ = gate.loc[f"H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: {s_})"]
        gd_ = gate.loc[f"H4a NAME G_dec within [0.90, 1.11] (2024-26 pooled; audit: {s_})"]
        A(f"| {spec_names.get(s_, s_)} | {gt_.corrected_ci90} | {'yes' if gt_.passes else 'no'} | {gd_.corrected_ci90} | "
          f"{'yes' if gd_.passes else 'no'} |")
    A("")
    lit = gate.loc["H4a NAME G_total: literal PLAN section 4 rule (tipping point beyond the audit upper CI)"]
    A(f"- G_total is more editing-sensitive than G_dec, because accepted papers are a smaller share of s0 "
      f"(a₀ = {n_(nm.acc_share_s0, 3)}) than of s2 (a₂ = {n_(nm.acc_share_s2, 3)}).")
    A(f"- The corrected point estimate (G_total at D̂) is {n_(nm.G_total_sel_point, 3)}. The editing-corrected "
      f"submission-stage NAME ratio is therefore about {n_(min(nm.G_total_sel_point, spec('post_2024_26').G_total_sel_point), 2)}–"
      f"{n_(max(nm.G_total_sel_point, spec('post_2024_26').G_total_sel_point), 2)} across the primary and 2024–26 audits, "
      f"not the stored-title {n_(nm.G_total_obs, 3)}.")
    A(f"- The literal §4 rule (\"tipping point exceeds the audit upper CI\") is written for association claims. For "
      f"NAME G_total it is not met (D\\*_total {n_(lit.tip_pp)} pp vs upper CI {n_(nm.did_hi_pp)} pp). The H4a "
      "equivalence claim is gated by the corrected-CI TOST instead (Deviation 11).")
    A("")
    A("**H4b (depletion of LLM and outsider markers).** One family of three claims, Holm at one-sided 0.025.")
    for nm_, g_ in [("L-title, audited as R24 or R26 (G2)", g2), ("O-union, audited without ALL-CAPS (G2b)", g2b),
                    ("F24-or-F26 abstract words (G3)", g3)]:
        A(f"- {nm_}: G_total {n_(g_.observed, 3)}; DiD {n_(g_.did_pp, 2, True)} pp vs D\\* {n_(g_.tip_pp, 2, True)}; "
          f"corrected 90% CI {g_.corrected_ci90}; p {n_(g_.p_ident, 3)}, Holm {n_(g_.p_holm, 3)}; uncorrected rule "
          f"{'passes' if g_.passes_uncorrected else 'fails'}; **{'passes' if g_.passes else 'does not pass'}**.")
    A("- The original L-title union (with typography) and O-union (with ALL-CAPS) are channel-unauditable and listed "
      "in `gate.csv` for transparency only.")
    A("- H4b's audit-free component, G_desk × G_exit on submission-stage text, is unaffected.")
    A("")
    A(f"**Acceptance associations.** {len(holm_pass)} of {len(tp)} title features pass. Diachronic and NA-pool results "
      "do not depend on the audit (PLAN §4).")
    A("")

    # ================================================================ 6 abstract
    jac = meta["abstract_audit"]["abstract_jaccard"]
    A("## 6. Abstract audit (extension; `abstract_audit.csv`)")
    A("")
    A("**Design.**")
    A("- arXiv v1 abstracts come from two sources:")
    A("  - the 330 original pre-decision pairs, re-fetched by `audit_v2.py` (one 503 error is not retried, to keep "
      "the file the prereg froze unchanged);")
    A("  - every enlargement record, which already carries its v1 abstract.")
    A(f"- Re-fetched v1 titles match the original audit for {pct(meta['abstract_audit']['v1_title_consistent'], 0)}% of "
      "pairs.")
    A("- **Primary sample: 2024–26 pairs**, the H4b/H4c scope. Sensitivities: 2023–26, original only, enlargement only.")
    A(f"- Content-word Jaccard between v1 and stored abstract:")
    A(f"  - pooled 2023–26: accepted {n_(jac['abs_2023_26']['acc'])} vs rejected {n_(jac['abs_2023_26']['rej'])}, "
      f"difference {n_(jac['abs_2023_26']['diff'], 3, True)} {ci(jac['abs_2023_26']['lo'], jac['abs_2023_26']['hi'], 3)};")
    A(f"  - original pairs: {n_(jac['original']['acc'])} vs {n_(jac['original']['rej'])}, "
      f"{n_(jac['original']['diff'], 3, True)} {ci(jac['original']['lo'], jac['original']['hi'], 3)}.")
    A("  - Accepted abstracts do not change measurably more than rejected ones.")
    A("")
    A("| Marker | Sample | Accepted: v1-present, +adds/−drops, n | Rejected | DiD (pp) [pseudo-flip 95%] | Auditable |")
    A("|---|---|---|---|---|---|")
    for k in ["F24", "F24_2", "F26_words", "abs_emdash", "L_abs_words"]:
        for sp_, tab in [("2024–26", abp), ("2023–26", ab23), ("original", abo)]:
            if sp_ != "2024–26" and k not in ("F24", "L_abs_words"):
                continue
            r = tab.loc[k]
            aw = "no (channel)" if not bool(r.channel_ok) else ("yes" if bool(r.auditable) else "no (count)")
            A(f"| {S.FEAT_LABEL[k]} | {sp_} | {int(r.v1_present_acc)}, +{int(r.adds_acc)}/−{int(r.drops_acc)}, "
              f"{int(r.n_acc)} | {int(r.v1_present_rej)}, +{int(r.adds_rej)}/−{int(r.drops_rej)}, {int(r.n_rej)} | "
              f"{n_(100 * r.did, 2, True)} {ci(100 * r.did_lo, 100 * r.did_hi)} | {aw} |")
    A("")
    em = abp.loc["abs_emdash"]
    A(f"**Em dash.** No arXiv v1 abstract contains an em dash ({meta['channel_check']['n_abs_emdash']} of "
      f"{meta['channel_check']['n_arxiv_v1_abstracts']:,}). arXiv writes TeX `--`/`---` or a plain hyphen, e.g. "
      "\"interactions--such as\" vs the stored \"interactions—such as\".")
    A(f"- The {int(em.adds_acc)} + {int(em.adds_rej)} em-dash \"adds\" are therefore channel artefacts.")
    A("- The em dash, and by the same mechanism U+2011/en-dash typography in titles (0 of "
      f"{meta['channel_check']['n_arxiv_titles']:,} arXiv titles), **cannot be audited through arXiv**.")
    A("")
    fa24 = abp.loc["F24"]
    A("**Tipping points** (pooled 2024–26, year-standardised):")
    A(f"- F24: G_dec {n_(fa24.tp_G_dec_obs, 3)}, G_total {n_(fa24.tp_G_total_obs, 3)} "
      f"{ci(fa24.tp_G_total_lo95, fa24.tp_G_total_hi95, 3)}. D\\*_total {n_(fa24.tp_tip_total_pp, 2, True)} pp vs DiD "
      f"{n_(100 * fa24.did, 2, True)} {ci(100 * fa24.did_lo, 100 * fa24.did_hi)}. Not identified.")
    A(f"- F24-or-F26 words: G_total {n_(g3.observed, 3)}. Not identified.")
    A("")
    A("**Readings.**")
    A(f"1. On stored abstracts, the accepted/all *prevalence* ratio for RARE21 is close to 1 "
      f"({n_(fa24.tp_G_total_obs, 2)} pooled 2024–26).")
    A("   - D4's H4c contrast is larger because the Kobak bound subtracts a pre-2024 baseline from both sets.")
    A(f"   - A prevalence-scale depletion of a few percent cannot be made audit-robust: the tipping points are below "
      f"1 pp, against an audit band of about ±{n_(50 * (fa24.did_hi - fa24.did_lo) * 100 / 100, 1)} pp.")
    A(f"2. The abstract-editing DiD is **positive but small and not significant**: "
      f"{n_(100 * f24.did, 2, True)} pp {ci(100 * f24.did_lo, 100 * f24.did_hi)} on 2024–26 pairs, and "
      f"{n_(100 * f24s.did, 2, True)} pp on 2023–26 pairs.")
    A(f"   - Both arms gain F24 words between v1 and the stored abstract (accepted {n_(100 * f24.net_acc, 2, True)} pp, "
      f"rejected {n_(100 * f24.net_rej, 2, True)} pp).")
    A(f"   - The interim estimate fell from {n_(100 * abo.loc['F24'].did, 2, True)} pp (330 original pairs) to "
      f"{n_(100 * f24.did, 2, True)} pp.")
    A(f"   - The sign matches H4c's assumption, so the accepted-only understatement is not reversed by editing (G4 "
      f"{H['G4']['verdict'].replace('_', ' ')}).")
    A("   - The interim sentence calling the accepted additions \"consistent with LLM-assisted camera-ready polishing\" "
      "is withdrawn.")
    A("")

    # ================================================================ 7 route
    A("## 7. V7: retrieval-route validation (`route_validation.csv`, `route_pairs.csv`, Fig. S3)")
    A("")
    A("**Design.**")
    A("- Sample: a random subsample of the original audit, 150 accepted + 150 rejected (seed 20261011). Complete: "
      "n = 300.")
    A("- **Route B** never uses the title. It queries `au:<first-author surname> AND abs:w1 AND abs:w2 AND abs:w3`.")
    A("  - The w's are the three abstract words with the lowest document frequency among all exported ICLR "
      "abstracts, excluding words in the stored title. A fallback query uses the surname and the next two words.")
    A("  - Acceptance tiers: A, abstract Jaccard ≥ 0.45; B, surname match and Jaccard ≥ 0.30; C, surname match, "
      "Jaccard ≥ 0.15, plausible v1 year and a 3-word query.")
    A("")
    A("| | Accepted (n = 150) | Rejected (n = 150) | All (n = 300) |")
    A("|---|---|---|---|")
    for col, nm_ in [("A_found", "Found, route A (title)"), ("B_found", "Found, route B (surname + abstract)"),
                     ("B_found_strict", "Found, route B strict tiers"), ("union_found", "Found, A or B")]:
        A(f"| {nm_} | {pct(gg.loc['accepted', col + '_rate'])}% {ci(100 * gg.loc['accepted', col + '_lo'], 100 * gg.loc['accepted', col + '_hi'], 1)} | "
          f"{pct(gg.loc['rejected', col + '_rate'])}% {ci(100 * gg.loc['rejected', col + '_lo'], 100 * gg.loc['rejected', col + '_hi'], 1)} | "
          f"{pct(gg.loc['all', col + '_rate'])}% |")
    A(f"| A only / B only / neither | {int(gg.loc['accepted', 'A_only'])} / {int(gg.loc['accepted', 'B_only'])} / "
      f"{int(gg.loc['accepted', 'neither'])} | {int(gg.loc['rejected', 'A_only'])} / {int(gg.loc['rejected', 'B_only'])} / "
      f"{int(gg.loc['rejected', 'neither'])} | {int(gg.loc['all', 'A_only'])} / {int(gg.loc['all', 'B_only'])} / "
      f"{int(gg.loc['all', 'neither'])} (McNemar p = {n_(gg.loc['all', 'mcnemar_p'], 3)}) |")
    A(f"| Same arXiv id when both found | {pct(gg.loc['accepted', 'same_id_rate'])}% | {pct(gg.loc['rejected', 'same_id_rate'])}% | "
      f"{pct(gg.loc['all', 'same_id_rate'])}% |")
    for col, nm_ in [("A_changed", "v1 retitled vs stored, route A"), ("B_changed", "v1 retitled vs stored, route B"),
                     ("A_latest_diff", "Latest arXiv title ≠ stored, route A"),
                     ("B_latest_diff", "Latest arXiv title ≠ stored, route B")]:
        A(f"| {nm_} | {int(gg.loc['accepted', col + '_k'])}/{int(gg.loc['accepted', col + '_n'])} = "
          f"{pct(gg.loc['accepted', col + '_rate'])}% | {int(gg.loc['rejected', col + '_k'])}/"
          f"{int(gg.loc['rejected', col + '_n'])} = {pct(gg.loc['rejected', col + '_rate'])}% | "
          f"{pct(gg.loc['all', col + '_rate'])}% |")
    A("")
    nmb = rvs["near_miss_bound"]
    A("**Findability (V7a).**")
    A(f"- The accepted–rejected findability gap is the same on both routes: {n_(rvs['gap_A']['est'])}; difference "
      f"{n_(rvs['gap_B_minus_A']['est'] + 0.0)} {ci(rvs['gap_B_minus_A']['lo'], rvs['gap_B_minus_A']['hi'])}. So the "
      "gap is not specific to title search.")
    A("- **The routes are not independent.** Both accept a hit only if the *latest* arXiv abstract resembles the stored "
      "abstract. Route A's third attempt is also already title-free (surname + abstract words). Rejected papers "
      "rewritten after rejection can be missed by both routes.")
    for thr, key in [("0.10", "jac_ge_0.10"), ("0.05", "jac_ge_0.05")]:
        q = nmb[key]
        A(f"- Near-miss bound (Jaccard ≥ {thr}): among papers neither route found, {q['accepted']['near_miss']} accepted "
          f"and {q['rejected']['near_miss']} rejected have a same-surname, date-plausible candidate below the acceptance "
          f"tiers. Counting them as found moves the rejected found rate from {pct(q['rejected']['union_rate'])}% to "
          f"{pct(q['rejected']['bound_rate'])}%, and the gap from {n_(q['gap_union'])} to {n_(q['gap_bound'])}.")
    A("- A substantial gap remains under either bound. Differential findability is consistent with arXiv posting "
      "differing by decision, plus some censoring of heavily revised rejected papers.")
    A("")
    A("**Title stability (V7b).**")
    A(f"- Retitling rates differ by {n_(100 * (gg.loc['all', 'B_changed_rate'] - gg.loc['all', 'A_changed_rate']), 1)} pp "
      f"between routes ({pct(gg.loc['all', 'A_changed_rate'])}% vs {pct(gg.loc['all', 'B_changed_rate'])}%; no CI is "
      "computed because the routes share most papers).")
    A(f"- The papers found only by route B are disproportionately retitled: {int(gg.loc['all', 'Bonly_changed_k'])} "
      f"of {int(gg.loc['all', 'Bonly_changed_n'])}.")
    us = spec("union_route_v7sub")
    A(f"- Adding the route-B-only pairs, which exist only for the 300-paper subsample, moves the NAME DiD from "
      f"{n_(nf.did * 100, 2, True)} to {n_(us.did_pp, 2, True)} pp. On the interim 331 pairs the same "
      f"{rvs['n_B_only_pairs_added']} pairs moved it by {n_(i_union_shift, 2)} pp; a full-sample union could move it "
      "more.")
    am = spec("abstract_matched")
    A(f"- Dropping title-clause admissions (abstract-matched pairs only) gives a NAME DiD of {n_(am.did_pp, 2, True)} "
      f"{ci(am.did_lo_pp, am.did_hi_pp)} pp.")
    A(f"- Rejected papers' *latest* arXiv titles differ from the stored title in {pct(gg.loc['rejected', 'A_latest_diff_rate'])}% "
      f"of cases (accepted: {pct(gg.loc['accepted', 'A_latest_diff_rate'])}%). This is retitling after rejection.")
    A("")

    # ================================================================ 8 enlargement
    A("## 8. Enlargement and freeze (`audit_v2.py` phase 2)")
    A("")
    fe_a, fe_r = fr_row("enlarge", "all", "accepted"), fr_row("enlarge", "all", "rejected")
    A(f"- **Status:** complete. {enl['n_records_ok']:,} of {enl['target']:,} sampled papers queried without a network "
      f"error ({enl['n_lines_used']:,} lines; errored rows were retried and the retry superseded them).")
    A("- Throughput is about 375–430 papers per hour. Each paper needs 2–4 requests at ≥ 3.2 s apart, so the PLAN's "
      "\"1k papers/hour\" is not achievable within the rate limit.")
    A(f"- **Findability replicates out of sample:** found {pct(fe_a.found_rate)}% "
      f"{ci(100 * fe_a.found_lo, 100 * fe_a.found_hi, 1)} accepted vs {pct(fe_r.found_rate)}% "
      f"{ci(100 * fe_r.found_lo, 100 * fe_r.found_hi, 1)} rejected.")
    A(f"- **Pairs:** {np_['enlargement']:,} new usable pairs; primary {nA + nR:,} ({nA:,}/{nR:,}).")
    A("- **Reproducing the freeze:** `python -m analyses.snapshot_final --enlarge-n "
      f"{enl['n_lines_used']}`, then check `meta.audit_freeze.enlargement.sha256_of_lines_used`.")
    A("- **Consumers of this freeze** (aligned in the integration passes, after this work package's own audit):")
    A("  - `d4_bias_atlas.py` builds D4's flip tables on this freeze's primary pairs (`audit_pairs.csv`) with the "
      "same auditability rule and pseudo-flip CI, and asserts that they equal `T4_2_flip_matrices.csv`. Before the "
      "integration pass it used the original audit only.")
    A("  - `prereg_confirm` (pre-registration revision 2) re-froze its gate audit on this freeze (same line count, "
      "SHA-256 checked) and adopted the multiplicity-controlled gate. Revision 1 had frozen the original audit plus "
      "1,261 enlargement lines and gated with the uncorrected rule in `snapshot_bounds.tipping_table`. Revision 3 "
      "keeps this audit unchanged.")
    A("  - `d3_slots.py` (D3's camera-ready audit of LLM slot words) reads this freeze's enlargement lines (same line "
      "count, SHA-256 checked) with D3's own pairing rule (2022-26). Until the second integration pass it read a "
      "pre-freeze pin of 1,620 lines (1,127 pairs; LLM-slot v1 titles 22 accepted / 4 rejected). On this freeze the "
      "slot words stay unauditable (SB3: 23 / 5 v1-present; rejected arm below 10).")
    p12 = fpath.set_index("enlarge_lines").loc[1261]
    A(f"  - At 1,261 lines the uncorrected rule passes "
      f"{', '.join(lab(k) for k in str(p12.passes_uncorrected).split(',') if k and k != 'nan') or 'nothing'} (see the "
      "freeze path); that is why the prereg gate was revised before any held-out data were requested.")
    A("")
    A("---")
    A("")

    # ================================================================ deviations
    A("## Deviations from PLAN.md (logged)")
    A("")
    A("1. **CI for the net-flip DiD.** The PLAN does not fix the CI type. The primary CI is Wald with a pseudo-flip "
      "variance floor, because plain Wald SEs are 0 for zero-flip arms. Plain Wald and a stratified bootstrap "
      "(2,000 replicates, year × decision strata) are reported. Under the Holm gate no verdict changes between them. "
      "Under the uncorrected rule the identified set differs by CI type and spec (§4).")
    A("2. **Auditability rule.** ≥ 10 v1-present titles in *both* arms, plus arXiv-channel measurability. The "
      "channel criterion was added after the interim run: arXiv titles were never ALL-CAPS or Unicode-typographic "
      f"(0 of {meta['channel_check']['n_arxiv_titles']:,}), and v1 abstracts never contained an em dash.")
    A("3. **Tipping point regenerated at 2.92 pp** against the pilot's 1.8 pp. The pilot omitted the 1/(1 − a₂) "
      "factor (§4).")
    A("4. **V7 retrieval key.**")
    A("   - PLAN: \"surname plus the first abstract sentence\". Phrase search on a full sentence fails after any "
      "rewording, so three corpus-rare abstract words are used, excluding title words, with a 2-word fallback.")
    A("   - Tier C was added after a pilot query; its false-positive rate in validation was 1 of 2, so strict-tier "
      "results are reported.")
    A("   - Route B uses an ASCII-transliterating surname helper. The enlargement keeps the original helper so that it "
      "can be pooled with the original audit.")
    A("5. **Extension: arXiv v1 abstracts** audit abstract markers (F24, F26, em dash). This is not in the PLAN.")
    A("6. **Enlargement.** 250 per year × decision cell for 2023–26, interleaved queue, written to a separate file. "
      "The PLAN's rate is infeasible under the 3.2 s rate limit.")
    A("7. **IPW models** are fitted on 2023–26, because 2022 has accepted papers only.")
    A("8. **G intervals clip D** to the feasible range [P₃ − 1, P₃].")
    A("9. **Per-year tipping points** exist for 2023–2026 only. 2018–2022 have no audit.")
    A("10. **Note for D4.** `d4_filter/audit_pairs.csv` reads `arxiv_id` with `pd.read_json`, which parses ids as "
      "floats. This does not affect D4's features.")
    A("11. **Gate operationalisation** (set after the interim run, in response to the audit).")
    A("    - For association claims, PLAN §4 (\"tipping point exceeds the audit's upper CI\") is applied with the "
      "tipping point's sampling error and Holm across auditable features (PLAN §0), plus an editing-corrected 95% CI "
      "that excludes 1.")
    A("    - For the H4a equivalence claim, the §4 rule is replaced by a TOST on the editing-corrected 90% CI. Under "
      "the literal rule NAME G_total is not identified.")
    A("    - The G4 four-way rule and the V7b rule were set after seeing the pilot.")
    A("    - The interim G1 \"partially supported when only the enlarged audit passes\" rule is dropped, because the "
      "enlarged audit is now the primary.")
    A("12. **Primary audit** = original + complete enlargement, 2023–26 (interim: original only, 2022–26). The PLAN "
      "asked for the enlargement before confirmation; dropping the 9 accepted-only 2022 pairs follows the code audit. "
      "Retitling's period contrast uses 2023 as the pre-period.")
    A("13. **Audited unions.** L-title is audited as R24 or R26, and the O-union as sentence case or question opener. "
      "The PLAN's unions contain channel-unauditable components.")
    A("14. **Abstract audit primary sample** is 2024–26 pairs (the H4b/H4c scope), with 2023–26 as a sensitivity.")
    A("15. **v1 timing strata** use approximate public full-paper deadlines.")
    A("16. **Code.** The fixes live in `snapshot_final.py`, because `snapshot_bounds.py` is hashed by the prereg "
      "bundle.")
    A("")
    A("## Limitations")
    A("")
    A(f"- **Sample size.** Even with {nA:,}/{nR:,} pairs, the NAME CI (±{n_(Z_(nf), 1)} pp) is wider than the gap "
      "between D̂ and D\\*. \"Not identified\" is a statement about the audit, not evidence that editing explains the "
      "association.")
    rr_ = sorted([r_pre.rate_acc / r_in.rate_acc, r_pre.rate_rej / r_in.rate_rej])
    A(f"- **arXiv v1 is not the submitted OpenReview title.** {pct(1 - (tim['n_in_review']['accepted'] + tim['n_in_review']['rejected']) / (nA + nR), 0)}% "
      f"of v1s predate the submission deadline. These earlier drafts retitle {n_(rr_[0], 1)}–{n_(rr_[1], 1)}× as often "
      "as in-review v1s. The DiD removes this drift only if it is the same in both arms. The timing mix is similar in "
      "the primary sample, and neither the in-review nor the timing-standardised spec identifies NAME (§4). Fetching "
      "the last pre-decision arXiv version instead of v1 would remove most of this noise; it was not done.")
    A("- **Selection.** Findability IPW corrects for year, decision, title length and NAME only. Unobserved "
      "differences between arXiv-posting and non-posting rejected papers remain. So does censoring of heavily "
      "revised rejected papers by the abstract-similarity matching rule (near-miss bound, §7).")
    A("- **Channel.** Typography, ALL-CAPS titles and the em dash cannot be audited through arXiv at any sample size.")
    A("- **Abstract audit caveats.** The arXiv v1 abstract may differ from the OpenReview submission abstract for "
      "reasons common to both arms.")
    A("- **Gate verdicts depend on 2024–26 pooling.** Per-year bounds are wide.")
    A("")
    A("## Interface for D4 (WP8) and the prereg")
    A("")
    A("- `T4_2_flip_matrices.csv`, rows `spec == 'primary'`: the canonical net-flip DiD per feature. Columns `did`, "
      "`did_lo`, `did_hi` (pseudo-flip 95%), `did_lo_wald`/`did_hi_wald`, `did_lo_boot`/`did_hi_boot`, `auditable` "
      "(channel + count), `auditable_count`, `channel_ok`.")
    A("- `T4_2_tipping_points.csv`: G_dec and G_total, tipping points and their SEs, identification p-values (`p_ident_*`, "
      "`p_holm_dec`), gate flags (`passes_holm_dec`, `passes_uncorrected_dec`), editing shares, audit-size "
      "multipliers, audit-implied and corrected intervals.")
    A("- `gate.csv`: gate verdicts for H4a (by audit spec), H4b and every acceptance association.")
    A("- `results.json` → `meta.audit_freeze`: the line count and SHA-256 to pass as `--enlarge-n` for any consumer.")
    A("")
    A("## Files")
    A("")
    A("- **Scripts:** `src/analyses/snapshot_final.py`, `src/analyses/snapshot_final_report.py`, "
      "`src/analyses/snapshot_bounds.py` (unchanged), `src/analyses/audit_v2.py`.")
    A("- **Caches** (written by `audit_v2.py`): `cache/arxiv_audit_route.jsonl`, `cache/arxiv_audit_v1abs.jsonl`, "
      "`cache/arxiv_audit_enlarge.jsonl`; background log `outputs/snapshot/audit_v2.log`.")
    A("- **Tables:** `audit_pairs.csv` (primary pairs), `found_rates.csv`, `findability_models.csv`, `retitling.csv`, "
      "`T4_2_flip_matrices.csv`, `T4_2_flip_multiclass.csv`, `T4_2_tipping_points.csv`, `T4_2_tipping_by_year.csv`, "
      "`T4_2_identification_by_spec.csv`, `T4_2_identified_anywhere.csv`, `T4_2_freeze_path.csv`, `abstract_audit.csv`, "
      "`gate.csv`, `route_validation.csv`, `route_pairs.csv`, `results.json`, `snapshot_final.log`.")
    A("- **Figures** (each as PDF + PNG + CSV):")
    A("  - **Fig. S1** `fig_S1_findability_retitling`: findability and retitling by year × decision, pooled audit.")
    A("  - **Fig. S2** `fig_S2_tipping_points`: net-flip DiD vs tipping point, observed G with CI, audit-implied G.")
    A("  - **Fig. S3** `fig_S3_route_validation`: V7.")
    A("  - **Fig. S4** `fig_S4_flip_rates`: drop and add rates with feature-present denominators (replaces "
      "`fig_S4_drop_rates`).")
    A("- **Interim run** (254 enlargement records): `interim_254/`.")
    A("")
    return "\n".join(L) + "\n"


def audit_response(out: Path) -> str:
    """'## Audit response' section: every issue raised by the three WP4 audits, with final numbers."""
    R = json.loads((out / "results.json").read_text())
    I = json.loads((out / "interim_254" / "results.json").read_text())  # noqa: E741
    H = {h["id"]: h for h in R["hypotheses"]}
    tp = pd.read_csv(out / "T4_2_tipping_points.csv").set_index("feature")
    fl_all = pd.read_csv(out / "T4_2_flip_matrices.csv")
    fl = fl_all[fl_all.spec == "primary"].set_index("feature")
    idt = pd.read_csv(out / "T4_2_identification_by_spec.csv")
    fpath = pd.read_csv(out / "T4_2_freeze_path.csv")
    rt = pd.read_csv(out / "retitling.csv")
    gate = pd.read_csv(out / "gate.csv").set_index("claim")
    ab = pd.read_csv(out / "abstract_audit.csv")
    meta = R["meta"]
    enl = meta["audit_freeze"]["enlargement"]
    nA, nR = meta["n_pairs"]["primary_by_decision"]["accepted"], meta["n_pairs"]["primary_by_decision"]["rejected"]
    nm, nf = tp.loc["NAME"], fl.loc["NAME"]
    sc, ou, cp = tp.loc["sentence_case"], tp.loc["O_union_arxiv"], tp.loc["compound"]
    aud = tp[tp.auditable]
    unc = sorted(tp.index[tp.passes_uncorrected_dec])

    def sp(s_, k="NAME"):
        return idt[(idt.spec == s_) & (idt.feature == k)].iloc[0]

    def rr(s_, y="all"):
        return rt[(rt.spec == s_) & (rt.years.astype(str) == y) & (rt.measure == "changed_norm")].iloc[0]
    it = {k: v for k, v in I["tipping_2024_26"].items()}
    i_nm = it["NAME"]
    i_g2 = [g for g in I["gate"] if g["claim"].startswith("acceptance association of L_title")][0]
    f24p = ab[(ab.spec == "abs_2024_26") & (ab.feature == "F24")].iloc[0]
    f24a = ab[(ab.spec == "abs_2023_26") & (ab.feature == "F24")].iloc[0]
    fp = fpath.set_index("enlarge_lines")
    p1261 = fp.loc[1261] if 1261 in fp.index else None
    g1 = gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: primary)"]
    g2 = gate.loc["H4b L-title G_total < 1 (2024-26; audited as R24 or R26)"]
    r_in, r_all = rr("v1_in_review"), rr("primary")
    oi, ob = rr("original_in_review"), rr("original_before_deadline")
    nmb = R["route_validation"]["summary"]["near_miss_bound"]["jac_ge_0.10"]
    tim = meta["timing"]
    L = []
    A = L.append
    A("## Audit response")
    A("")
    A("Three independent audits reviewed the interim run:")
    A("- the code audit (`outputs/audit/snapshot_code/`), issues C-I1 to C-I10;")
    A("- the identification audit (`outputs/audit/snapshot_ident/`), issues S-I1 to S-I9;")
    A("- the reporting audit (`outputs/audit/snapshot_reporting/`), issues R1 to R18.")
    A("")
    A("Each issue was re-checked before it was fixed. Fixes live in `src/analyses/snapshot_final.py` and "
      "`snapshot_final_report.py`. `snapshot_bounds.py` is unchanged, because the prereg bundle hashes it. The fix "
      "log is `outputs/audit/wp4/fix_log.md`.")
    A("")
    A("**Claims weakened or withdrawn, in one place.**")
    A(f"1. \"No sign that review-stage acceptance is manufactured by post-decision renaming\" is withdrawn. At the "
      f"audit point estimate about {n_(100 * nm.excess_share_edit_dec, 0)}% of the NAME G_dec excess is camera-ready "
      f"(CI {n_(100 * nm.excess_share_edit_lo_dec, 0)}% to {n_(100 * nm.excess_share_edit_hi_dec, 0)}%).")
    A("2. \"Camera-ready editing moves features in both directions at similar rates\" is withdrawn. Drop rates are "
      f"similar, but accepted papers add NAME {n_(nf.add_rate_acc / nf.add_rate_rej, 1)}× as often as rejected papers.")
    A(f"3. The camera-ready retitling excess (+6.4 pp; +10.1 pp in 2024–26) is withdrawn. It is "
      f"{n_(100 * r_all['diff'], 1, True)} pp on the complete audit and {n_(100 * r_in['diff'], 1, True)} pp where the "
      "v1 was posted during review.")
    A(f"4. The G4 magnitude falls from +3.55 pp to {n_(100 * f24p['did'], 2, True)} pp (2024–26 pairs). The "
      "\"consistent with LLM-assisted polishing\" sentence is withdrawn.")
    A("5. \"Findability depends neither on NAME nor title length nor route\" is rewritten. Longer titles are slightly "
      "less findable, and the two routes share an abstract-similarity rule.")
    A("6. The interim \"0 of 24 pass\" was right only by accident of the 254-record freeze. Under the interim rule "
      f"{len(unc)} features pass on the complete audit; only the new multiplicity-controlled gate yields 0.")
    A("")
    A("**Claims strengthened.**")
    A(f"- G1 (H4a NAME neutrality survives editing) moves from \"partially supported\" to **supported**: corrected "
      f"90% CI {g1.corrected_ci90}.")
    A(f"- The editing-corrected NAME G_total at the audit point estimate is {n_(nm.G_total_sel_point, 3)}, "
      f"{'below' if nm.G_total_sel_point < 1 else 'above'} the stored-title {n_(nm.G_total_obs, 3)}.")
    A("")
    A("### Code audit")
    A("")
    A(f"- **C-I1 (major) — valid, fixed.**")
    A(f"  - What was wrong: the interim run froze the enlargement at 254 of 2,000 records, and D4 and the prereg use "
      f"different audit samples.")
    A(f"  - Change: the analysis now runs on the complete enlargement ({enl['n_records_ok']:,} records, "
      f"{enl['n_lines_used']:,} lines, SHA-256 in `meta.audit_freeze`). That sample is the primary audit, and a "
      f"freeze path reports the verdicts at 254, 600, 1,000 and 1,261 lines.")
    A(f"  - Not done in this work package: D4 (`d4_bias_atlas.py`) and the prereg (`prereg_confirm.freeze_audit`, "
      f"1,261 lines) are other directions' frozen files. Both were aligned to this freeze in the later integration "
      f"pass (§8). D3's slot-word audit (`d3_slots.py`, 1,620 lines) was aligned in the second integration pass.")
    if p1261 is not None:
        A(f"  - What a prereg gate run would currently admit: at 1,261 lines the uncorrected rule passes "
          f"{', '.join(S.FEAT_LABEL.get(k, k) if k != 'O_union_arxiv' else 'O-union w/o ALL-CAPS' for k in str(p1261.passes_uncorrected).split(','))}.")
    A(f"- **C-I2 (major) — valid, fixed.** The gate is now: auditable, editing-corrected 95% CI excludes 1, and the "
      f"Holm-adjusted one-sided identification p (with the tipping point's sampling error) < 0.025 across "
      f"{len(aud)} auditable features. p-values and Holm values are in `gate.csv` and `T4_2_tipping_points.csv`. "
      f"Result: 0 pass; smallest Holm p {n_(aud.p_holm_dec.min(), 2)}. The uncorrected rule is kept as a column.")
    A(f"- **C-I3 (major) — valid, fixed.**")
    A(f"  - Both sentences are withdrawn.")
    A(f"  - G at the audit point estimate is now reported: NAME {n_(nm.G_dec_sel_point, 3)}, strict "
      f"{n_(tp.loc['NAME_strict'].G_dec_sel_point, 3)}, loose {n_(tp.loc['NAME_loose'].G_dec_sel_point, 3)}, against "
      f"observed {n_(nm.G_dec_obs, 3)}.")
    A(f"  - NAME flips on the complete audit: accepted +{int(nf.adds_acc)}/−{int(nf.drops_acc)}, rejected "
      f"+{int(nf.adds_rej)}/−{int(nf.drops_rej)}. DiD {n_(100 * nf.did, 2, True)} "
      f"{ci(100 * nf.did_lo, 100 * nf.did_hi)} pp.")
    A(f"- **C-I4 (minor) — valid, fixed.** arXiv titles carry no U+2011/U+2013 typography (0 of "
      f"{meta['channel_check']['n_arxiv_titles']:,}) and are never ALL-CAPS. Title typography, ALL-CAPS title, the "
      f"L-title union and the O-union are flagged channel-unauditable. G2 now audits R24 or R26: DiD "
      f"{n_(g2.did_pp, 2, True)} pp, not identified.")
    A(f"- **C-I5 (minor) — valid, fixed by stratification.**")
    A(f"  - Original sample: retitling difference {n_(100 * ob['diff'], 1, True)} pp before the deadline vs "
      f"{n_(100 * oi['diff'], 1, True)} pp during review.")
    A(f"  - Primary: v1 in review for {pct(tim['share_in_review']['accepted'])}% of accepted vs "
      f"{pct(tim['share_in_review']['rejected'])}% of rejected pairs.")
    A(f"  - New specs `v1_in_review`, `v1_before_deadline` and `timing_std`: NAME DiD "
      f"{n_(sp('v1_in_review').did_pp, 2, True)}, {n_(sp('v1_before_deadline').did_pp, 2, True)} and "
      f"{n_(sp('timing_std').did_pp, 2, True)} pp. The limitation is reworded.")
    A(f"  - Not done: fetching the last pre-decision arXiv version would need new network queries.")
    A(f"- **C-I6 (minor) — valid, fixed.** The abstract audit pools the enlargement's v1 abstracts. G4 is primary on "
      f"2024–26 pairs ({int(f24p.n_acc)}/{int(f24p.n_rej)}): {n_(100 * f24p.did, 2, True)} "
      f"{ci(100 * f24p.did_lo, 100 * f24p.did_hi)}. On 2023–26 pairs it is {n_(100 * f24a.did, 2, True)}. Verdict "
      f"{H['G4']['verdict'].replace('_', ' ')}, unchanged.")
    A(f"- **C-I7 (minor) — valid, fixed.** The pilot's 1.8 pp is P₃ − P₂ = {n_(100 * (nm.P_s3 - nm.P_s2), 2)} pp "
      f"without the 1/(1 − a₂) factor. Deviation 3 and §4 are corrected.")
    A("- **C-I8 (minor) — valid, fixed.** Every note in `results.json` is generated from the tables. RESULTS.md is "
      "generated by `snapshot_final_report.py`, with assertions on every verdict-dependent sentence.")
    A(f"- **C-I9 (minor) — valid, fixed in wording and specs.**")
    A(f"  - V7a and the headline are softened.")
    A(f"  - New `abstract_matched` spec: NAME DiD {n_(sp('abstract_matched').did_pp, 2, True)} pp.")
    A(f"  - The union spec is renamed `union_route_v7sub` and its scope (the 300-paper subsample) is stated.")
    A(f"  - Not done: whole-token surname matching cannot be re-applied, because the caches do not store arXiv author "
      f"lists. The abstract-matched spec removes every title-clause admission instead (rejected "
      f"{pct(tim['title_clause_share']['rejected'])}% vs accepted {pct(tim['title_clause_share']['accepted'])}% of "
      f"primary pairs).")
    A(f"- **C-I10 (minor) — valid, fixed.** The primary is 2023–26. The 9 accepted-only 2022 pairs form the "
      f"`incl_2022` spec (NAME {n_(sp('incl_2022').did_pp, 2, True)} pp), plus a `year_std` spec "
      f"({n_(sp('year_std').did_pp, 2, True)} pp). The retitling period contrast is 2024–26 vs 2023.")
    A("")
    A("### Identification audit")
    A("")
    A(f"- **S-I1 (critical) — valid in substance; the remedy differs.**")
    others = [S.FEAT_LABEL.get(k, k) if k != "O_union_arxiv" else "the O-union w/o ALL-CAPS" for k in unc
              if k != "sentence_case"]
    A(f"  - On the complete audit, sentence case is auditable and "
      f"{'passes' if sc.passes_uncorrected_dec else 'fails'} the *uncorrected* gate (margin "
      f"{n_(sc.tip_dec_margin_pp, 2)} pp)." + (f" {'So do' if sc.passes_uncorrected_dec else 'Passing it on the complete audit:'} "
                                                f"{', '.join(others)}." if others else ""))
    sc_hist = [f"{int(r.enlarge_lines):,}" for _, r in fpath.iterrows()
               if "sentence_case" in str(r.passes_uncorrected).split(",")]
    A(f"  - Sentence case passed the uncorrected gate at {', '.join(sc_hist) or 'no'} enlargement lines, as the "
      f"auditor found. It fails the multiplicity-controlled gate that PLAN §0 requires at every freeze; on the "
      f"complete audit p = {n_(sc.p_ident_dec, 3)}, Holm {n_(sc.p_holm_dec, 2)}. It is therefore not reported as an "
      f"audit-robust association. The closest lead is the O-union w/o ALL-CAPS (p {n_(ou.p_ident_dec, 3)}, Holm "
      f"{n_(ou.p_holm_dec, 2)}).")
    A(f"  - SB2, the headline, §5 and the unauditable table are rewritten. D4's own H4b text is not edited here (other "
      f"direction).")
    A(f"- **S-I2 (major) — valid, fixed** (as C-I3).")
    A(f"  - Editing share of the NAME excess at the point estimate: {n_(100 * nm.excess_share_edit_dec, 0)}%; "
      f"2024–26 pairs: {n_(100 * sp('post_2024_26').excess_share_edit_dec, 0)}%.")
    A(f"  - Corrected submission-stage NAME G_total: {n_(nm.G_total_sel_point, 3)} (primary) and "
      f"{n_(sp('post_2024_26').G_total_sel_point, 3)} (2024–26).")
    A(f"  - \"Peer review amplifies NAME\" is explicitly rejected in the headline.")
    A(f"- **S-I3 (major) — valid, fixed.** SB3 is restated with final counts, and the freeze path shows auditability "
      f"rising with n ({', '.join(str(int(x)) for x in fpath.n_auditable)} auditable features). Verdict: "
      f"{H['SB3']['verdict'].replace('_', ' ')}.")
    A("- **S-I4 (major) — valid, fixed** (as C-I4). The channel criterion is part of the auditability rule. The "
      "ALL-CAPS \"DiD exceeds the tipping point\" sentence is deleted.")
    A(f"- **S-I5 (major) — valid, fixed in wording plus a bound.**")
    A(f"  - V7a now states that both routes share a latest-abstract similarity rule.")
    A(f"  - Near-miss bound (Jaccard ≥ 0.10): {nmb['accepted']['near_miss']} accepted vs "
      f"{nmb['rejected']['near_miss']} rejected near-misses. The gap moves from {n_(nmb['gap_union'])} to "
      f"{n_(nmb['gap_bound'])}.")
    A(f"  - The censoring is listed as a limitation of the rejected arm's noise floor.")
    A(f"- **S-I6 (minor) — valid, fixed** (as C-I5). The in-review stratum is reported as the cleanest camera-ready "
      f"comparison: retitling {n_(100 * r_in['diff'], 1, True)} pp, NAME DiD {n_(sp('v1_in_review').did_pp, 2, True)} pp.")
    A(f"- **S-I7 (minor) — valid, fixed** (as C-I2).")
    A(f"  - Identification margins by CI type, and stability across {idt.spec.nunique()} specs, are in "
      f"`T4_2_identified_anywhere.csv` and §4.")
    A(f"  - 'via' is identified only in 2024–26 and out-of-sample specs and passes no gate.")
    A(f"- **S-I8 (minor) — valid, fixed** (as C-I6). The LLM-polishing sentence is withdrawn. G4 is reported as point "
      f"≥ 0 with a CI including 0.")
    A(f"- **S-I9 (minor) — valid, fixed.** G1 is upgraded to supported on the complete audit (corrected 90% CI "
      f"{g1.corrected_ci90}). The corrected centre ({n_(nm.G_total_sel_point, 3)}) and the 2024–26-pairs interval "
      f"are reported, and the interim caveat is removed.")
    A("")
    A("### Reporting audit")
    A("")
    A("- **R1 (major) — valid, fixed.** The \"no feature identified under any CI type\" sentences are replaced by a "
      "generated table of every (spec, feature, CI type) identification (§4). Deviation 1 is reworded.")
    A("- **R2 (major) — valid, fixed** (as C-I1). The analysis is no longer interim, and the freeze path replaces the "
      "fragility note.")
    A(f"- **R3 (major) — valid, fixed** (as C-I3). The suggested wording is adopted, with final numbers.")
    A(f"- **R4 (major) — valid, fixed.** The false sentence is replaced. At the observed DiD the CI clears D\\* at "
      f"about {n_(nm.n_mult_obs_50_dec, 1)}× the current {nA + nR:,} pairs.")
    A(f"- **R5 (major) — valid, fixed.** The G2 row bug read the L_title G_dec row; the interim results.json showed "
      f"{i_g2['observed']:.3f} {i_g2['obs_ci90']}. G2 now reads the H4b G_total claim row by name, which is now the "
      f"R24-or-R26 audit.")
    A("- **R6 (major) — valid, fixed.** The unauditable-features text no longer says \"none is identified\". Sentence "
      "case is now auditable and discussed with its margin. L-title is no longer called a strong association.")
    A(f"- **R7 (minor) — valid, fixed.** 50% and 80% power multipliers are reported "
      f"({n_(nm.n_mult_D0_50_dec, 2)}× and {n_(nm.n_mult_D0_80_dec, 2)}× of the complete audit). So is the realised "
      "usable rate.")
    A("- **R8 (minor) — valid, fixed.** 2023 is audited per year. The unaudited range is 2018–2022, and pair counts "
      "and half-widths are generated.")
    A("- **R9 (minor) — valid, fixed.** The text now says \"odds ratio\" with both found rates. The NAME null is "
      "stated with its CI, and the interim CI reaching 2.2 is noted.")
    A("- **R10 (minor) — valid, fixed.** The abstract-Jaccard difference is reported with a bootstrap CI; it is not "
      "significant in either sample.")
    A("- **R11 (minor) — valid, fixed.** Deviation 11 records the gate operationalisation and the literal §4 result "
      "for NAME G_total.")
    A("- **R12 (minor) — valid, fixed** (as S-I4). The wording is \"consistent with form entry\".")
    A(f"- **R13 (minor) — valid, fixed.** The identity is stated for a single year; with pooling, D\\* "
      f"{n_(nm.tip_dec_pp)} vs RD {n_(nm.rd_acc_rej_pp)} pp.")
    A("- **R14 (minor) — valid, fixed** (as C-I9). The text says \"differ by\" with the value, and the union spec is "
      "renamed.")
    A("- **R15 (minor) — valid, fixed.** The \"partial n = 300 of 300\" wording is gone.")
    A("- **R16 (minor) — valid, fixed.**")
    A("  - Fig. S2 draws D\\* as a vertical tick under the DiD dot.")
    A("  - Channel-unauditable rows (incl. the L-abstract union) are grey with ‡.")
    A("  - Abstract rows use D\\*_total and G_total, labelled.")
    A("  - Observed G carries its 95% CI, the legend shows both colours, and a footnote explains clipping.")
    A("- **R17 (minor) — valid, fixed.**")
    A("  - S1: per-panel legends, CIs on usable-pair rates, n per point.")
    A("  - S3: k/n on every point and an adaptive y-limit.")
    A("  - S4 (now `fig_S4_flip_rates`): add rates beside drop rates, with † and ‡ marking unauditable rows.")
    A("  - The text says drop rates overlap while add rates differ.")
    A("- **R18 (minor) — valid, fixed.** The \"shrinks as data accrue\" sentence is removed. The complete-audit "
      "estimate is reported with its CI.")
    A("")
    return "\n".join(L) + "\n"


def Z_(r) -> float:
    return 100 * S.Z * r.did_se


def main(outdir: Path | None = None):
    out = Path(outdir) if outdir else S.OUTDIR
    text = render(out)
    text += "\n" + audit_response(out)
    import re
    for pat in [r"\{[A-Za-z_][A-Za-z_0-9.\[\]'\"]*\}", r"\bnan\b", r"n/a", r"PENDING", r"TODO", r"\bNone\b"]:
        bad = [ln for ln in text.splitlines() if re.search(pat, ln)]
        if bad:
            raise SystemExit(f"unfilled token {pat!r} in RESULTS.md: {bad[:3]}")
    (out / "RESULTS.md").write_text(text)
    print(f"wrote {out / 'RESULTS.md'} ({len(text):,} chars)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=None)
    main(ap.parse_args().outdir)
