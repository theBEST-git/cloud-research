# Pre-registration: held-out confirmation of the ICLR title study (WP9)

- **Date:** 2026-10-11
- **Plan:** `docs/PLAN.md` section 4 (sha256 `680eb53564005fd8...`)
- **Bundle hash:** `f69fdb468702fe11e336b81476869531a71acb1d4f922b8bd1d479934bbac628` (SHA-256 of `outputs/prereg/bundle.sha256`)
- **Status:** frozen before any request for held-out data. The held-out (confirmation) split has not been seen; only discovery rows (`discovery_allowed = 1`) were used.
- **Code:** `src/analyses/prereg_confirm.py` (CT1–CT12 as pure functions, discovery dry run, bundle). The repository is not committed by this work package (no git commands are run here); the code is frozen by content hash instead, as for `features.py` in WP1.

## 1. Held-out data handling

1. The held-out submissions and author tables are read with the README convention (`keep_default_na=False`, `na_values=['\N']`).
2. `prepare_frame` applies the discovery universe rules (placeholder titles, abstracts under 20 words, empty titles), builds pools and stages with `_core.pool_flags`, harmonises areas, and computes all title and abstract features with the frozen `features_v2.build` and `lexicons.json`.
3. Topics: each held-out abstract is embedded with all-MiniLM-L6-v2 (L2-normalised) and assigned to the nearest frozen discovery centroid (k = 100). The centroids reproduce 100.00% of the discovery labels. `llm_topic` = LLM regex OR membership in one of the 20 frozen discovery LLM clusters.
4. Author history (CT3, CT12) is built on the union of discovery and held-out declared profile keys.
   Expected held-out sizes (PLAN): about a quarter of discovery per year, e.g. 2023 ≈ 970, 2024 ≈ 1,440, 2025 ≈ 2,240, 2026 ≈ 3,850 papers.
5. `run_heldout` verifies every hash in `bundle.sha256`, writes a guard file and refuses a second run. Each test runs once.
6. Pipeline check on 2994 raw discovery rows run through `prepare_frame`: 0 mismatches over 55 columns against the discovery frame. The universe filter on all raw rows gives 43,482 (expected 43,482). Re-embedding 120 abstracts: median cosine 1.0000 to the cached embeddings, topic agreement 100.0%.

## 2. Frozen bundle

`outputs/prereg/bundle.sha256` lists every file in `sha256sum` format, with paths relative to `research/titles`. It has three groups:

- **Code:** all of `src/analyses/*.py` and `*.json`, plus `src/{common,features,arxiv_audit,author_features,build_cache}.py`.
- **Frozen parameters (`outputs/prereg/frozen/`):**
  - `lexicons.json`, `d4_lexicon.json`, `slot_inventory.json` (V2-frozen slots) and `slot_variants_dropped.json`.
  - `fingerprints.json` (RARE21, F26 words, typography, R24/R26).
  - `centroids_minilm_k100.npy`, `llm_clusters.json` and `area_crosswalk.csv`.
  - `r1_rolling_<year>.npz`: rolling R1 vocabularies, idf, five fold models and calibration-year OOF scores.
  - `dfl_cells.csv` (DFL cell model), `audit_flips.csv`, `audit_did_boot.npz` and `audit_state.json`.
  - `params.json` and `rules.json` (the machine-readable rules of section 4).
- **Inputs (reference):** the discovery data files, `universe.parquet`, `features_v2.parquet`, the D1 R1 text cache and `PLAN.md`.

The R1 models were refitted here, because D1 saved scores only. Each refit uses D1's CV-chosen C and D1's folds. Test-row fold scores match D1's stored scores:
- Windows 2019–23: within 1.4e-06 logit units.
- Windows 2024–26: within 6.6e-03 logit units, which is within the lbfgs stopping tolerance.
- The per-year unexplained increments u_y equal D1's to about 1e-5. The CT2 dry-run point estimate (+1.353 pp) equals D1's current `results.json` (+1.353 pp).

Two consistency checks also pass:
- The D2 key panel rebuilt from the raw author table matches D2's `panel_rows.parquet` (rows and keys).
- Every other dry-run estimate reproduces the corresponding work package (`dryrun.json`, `wp_reference`).

## 3. Inference, multiplicity and verdicts

- All tests are one-sided in the predicted direction.
- **Primary family (CT1–CT6):** Holm, family-wise α = 0.05.
- **Secondary family (CT7–CT12):** Benjamini–Hochberg, q = 0.05.
- Bootstrap p-values use the +1 correction, (1 + #null)/(B + 1). Paper bootstraps use B = 2,000, stratified by year; the key-cluster bootstrap uses B = 1,000. All seeds are fixed in `params.json`.
- **Confirmed:** adjusted p < .05, the point estimate beyond the stated minimal effect, the test's CI rule met and, for acceptance-margin tests, the audit gate passed.
- **Contradicted:** the CI excludes the predicted region on the opposite side (test-specific rule).
- **Not confirmed:** otherwise; when only the gate fails the result is reported as 'not confirmed (gate)'.

## 4. Tests

### CT1: D1 break (H1a) (primary)

- **Data:** held-out U, 2017-2026.
- **Statistic:** Segmented logit NAME ~ (t-2023) + post + post x (t-2023) + log(#authors) + llm_topic + topic100 FE, SEs clustered by topic100 (d1_its.its_fit). Parameter: slope change delta = post x (t-2023), reported as OR per year.
- **p-value:** one-sided Wald z of delta <= 0.
- **Confirm if:** Holm-adjusted p < .05 and OR >= 1.10.
- **Contradicted if:** upper 95% CI bound of the OR < 1.
- **Gate:** none (diachronic).
- **Discovery dry run:** 1.098, 95% CI [1.044, 1.154]; one-sided p = 0.0001282.
- **Projected held-out power (approximate):** P(confirm) at alpha 0.0083 0.29; P(confirm) at alpha 0.0500 0.48; z_heldout_projected 1.83.

### CT2: D1 acceleration of unexplained drift (H1c) (primary)

- **Data:** held-out U, 2019-2026.
- **Statistic:** Each held-out year y is scored by the frozen rolling R1 models (trained on discovery y-3..y-1; five fold models; prediction = mean_k expit(s_k + c_y)); the frozen shift c_y makes the discovery cross-fitted predictions of y-1 match discovery obs_{y-1}. u_y = obs_y - p_hat_y. D = mean(u_2024-26) - mean(u_2019-23); ratio = mean(u_post)/mean(u_pre); content share of the 2024-26 steps = sum(p_hat_y - obs^disc_{y-1}) / sum(obs_y - obs^disc_{y-1}).
- **p-value:** bootstrap (B = 2,000): held-out papers resampled within year, discovery calibration-year papers resampled independently and c_y re-solved; p = (1 + #{D_b <= 0})/(B + 1).
- **Confirm if:** Holm-adjusted p < .05, lower 95% bound of D > 0, ratio >= 1.5, and upper 95% bound of the content share < 0.60.
- **Contradicted if:** upper 95% bound of D < 0.
- **Gate:** none (diachronic).
- **Discovery dry run:** 1.353, 95% CI [0.020, 2.701]; one-sided p = 0.02499.
- **Projected held-out power (approximate):** z_heldout_projected 1.00; alpha_0.0083 0.08; alpha_0.05 0.26; P_share_upper95_below_0p60 0.05.

### CT3: D2 communal change at the last list position (H2a) (primary)

- **Data:** declared profile keys, panel 2021-26; E = 2022-23 papers of discovery ∪ held-out; L = 2025-26 held-out papers.
- **Statistic:** Stayers: keys with >= 1 E paper and >= 1 held-out L paper (any list position). rho_last = (P_SL - P_SE)/(P_L - P_E) on last-list-position rows (weight 1 per row); P_E over all E rows, P_L over all held-out L rows.
- **p-value:** key-cluster bootstrap (B = 1,000, multinomial key counts, seed 20260); p = (1 + #{rho_b <= 0.5})/(B + 1).
- **Confirm if:** Holm-adjusted p < .05 and lower 95% bound > 0.5.
- **Contradicted if:** upper 95% bound < 0.5.
- **Gate:** none (diachronic within-key change).
- **Discovery dry run:** 0.995, 95% CI [0.943, 1.050]; one-sided p = 0.000999.
- **Projected held-out power (approximate):** z_heldout_projected 9.11; alpha_0.0083 1.00; alpha_0.05 1.00.

### CT4: D3 meaning-fixed slot break (H3a) (primary)

- **Data:** held-out titles 2018-2026 that fill an LLM slot (frozen V2 inventory, PLAN opener rule) or a control pair.
- **Statistic:** Stacked logit y ~ C(slot) + C(slot):(t-2023) + post + post x LLM-slot + llm_topic, SEs clustered by topic100 (d3_slots.STACKED). Parameter: post x LLM-slot, as OR.
- **p-value:** one-sided Wald z of the interaction <= 0.
- **Confirm if:** Holm-adjusted p < .05 and OR >= 1.5.
- **Contradicted if:** upper 95% CI bound of the OR < 1.
- **Gate:** none (diachronic).
- **Discovery dry run:** 2.551, 95% CI [1.530, 4.255]; one-sided p = 0.0001654.
- **Projected held-out power (approximate):** P(confirm) at alpha 0.0083 0.27; P(confirm) at alpha 0.0500 0.56; z_heldout_projected 1.79.

### CT5: D4 neutral filter for NAME (H4a) (primary)

- **Data:** held-out 2018-2026 without OTHER rows; stages s0-s3.
- **Statistic:** Pooled 2024-26 NAME G_total = P(NAME | accepted)/P(NAME | U), year-standardised (weights = the year's s0 size).
- **p-value:** paper bootstrap stratified by year (B = 2,000); TOST p = max{(1 + #{G_b <= 0.90})/(B + 1), (1 + #{G_b >= 1.11})/(B + 1)}.
- **Confirm if:** Holm-adjusted p < .05, 90% percentile CI inside [0.90, 1.11], and the gate.
- **Contradicted if:** 90% CI entirely outside [0.90, 1.11].
- **Gate:** acceptance-margin: the editing-corrected 90% CI (held-out bootstrap paired with draws of the audit net-flip DiD, WP4 G1 construction, frozen title audit) must lie inside [0.90, 1.11].
- **Discovery dry run:** 1.021, 90% CI [1.001, 1.041]; one-sided p = 0.0004998.
- **Projected held-out power (approximate):** P(90% CI inside margin), approx 0.98; heldout_se_projected 0.02.

### CT6: D4 depletion of LLM markers (H4b) (primary)

- **Data:** as CT5.
- **Statistic:** L-union (title typography, R24, R26, F24, F26, abstract em dash): pooled 2024-26 G_total and G_desk x G_exit = P(f | s2)/P(f | s0).
- **p-value:** bootstrap as CT5; p = max of (1 + #{G_b >= 1})/(B + 1) over the two gains.
- **Confirm if:** Holm-adjusted p < .05 (both gains < 1) and the gate for G_total.
- **Contradicted if:** lower 95% bound of either gain > 1.
- **Gate:** acceptance-margin (G_total): L-union must be auditable with the tipping point beyond the audit CI. It is not auditable (abstract em dash and title typography: 0 v1-present pairs in both arms), so CT6 cannot reach 'confirmed'; G_desk x G_exit is reported as the audit-free component.
- **Discovery dry run:** G_total 0.975; G_desk_x_exit 0.981, 95% CI G_total [0.951, 1.001]; G_desk_x_exit [0.972, 0.992]; one-sided p = 0.02999.
- **Projected held-out power (approximate):** z_heldout_projected G_total 0.98; G_desk_x_exit 1.83; alpha_0.0083 0.02; alpha_0.05 0.15.

### CT7: D3 vintage alignment (H3c) (secondary)

- **Data:** held-out U, 2025-2026.
- **Statistic:** Logit R24-in-title ~ F24 + F26 + C(year) + C(topic100) + log(#authors) + llm_topic + log(title words); topic100 cells without outcome variation dropped; SEs clustered by topic100. Statistic: OR(F24)/OR(F26).
- **p-value:** one-sided Wald z of log ratio <= 0.
- **Confirm if:** BH-adjusted p < .05 and ratio > 1.
- **Contradicted if:** upper 95% CI bound < 1.
- **Gate:** none (submission-population association, not acceptance).
- **Discovery dry run:** 1.461, 95% CI [1.168, 1.828]; one-sided p = 0.0004546.
- **Projected held-out power (approximate):** z_heldout_projected 1.66; alpha_0.0083 0.23; alpha_0.05 0.51.

### CT8: D3 register turnover (H3b) (secondary)

- **Data:** held-out 2025 and 2026 titles in the 16 frozen large areas.
- **Statistic:** Quasi-Poisson counts of titles with R24 (and R26) by area x year, area FE, log(#titles) offset, Pearson dispersion: RR 2026/2025 for R24 and for R26.
- **p-value:** two one-sided Wald tests on log RR (R24 down, R26 up); p = max of the two (intersection-union).
- **Confirm if:** BH-adjusted p < .05, RR_R24 < 1 and RR_R26 > 1.
- **Contradicted if:** R24 lower 95% bound > 1 or R26 upper 95% bound < 1.
- **Gate:** none (diachronic).
- **Discovery dry run:** RR_R24 0.744; RR_R26 1.944, 95% CI RR_R24 [0.642, 0.862]; RR_R26 [1.672, 2.261]; one-sided p = 4.309e-05.
- **Projected held-out power (approximate):** z_heldout_projected R24 1.96; R26 4.32; alpha_0.0083 0.32; alpha_0.05 0.62.

### CT9: D1 tool bound (H1e(i)) (secondary)

- **Data:** held-out U, 2023 and 2026.
- **Statistic:** F = f24_2 OR f26 OR title_typo. ratio = (NAME_2026 - NAME_2023 among F = 0) / (NAME_2026 - NAME_2023 among all).
- **p-value:** bootstrap within year (B = 2,000); p = (1 + #{ratio_b <= 0.70})/(B + 1).
- **Confirm if:** BH-adjusted p < .05 and lower 95% bound > 0.70.
- **Contradicted if:** upper 95% bound < 0.70.
- **Gate:** none (diachronic).
- **Discovery dry run:** 0.982, 95% CI [0.961, 1.004]; one-sided p = 0.0004998.
- **Projected held-out power (approximate):** z_heldout_projected 12.84; alpha_0.0083 1.00; alpha_0.05 1.00.

### CT10: D4 published-only understatement of LLM use (H4c) (secondary)

- **Data:** held-out 2021-2026 without OTHER rows.
- **Statistic:** Kobak-style bound per year Y in 2024-26 = P(F24 | set, Y) - baseline, baseline = max(linear 2021-23 trend extrapolated to Y, max(P_2022, P_2023)), set in {accepted, all}; pooled = mean over the three years; ratio = accepted/all. The held-out split supplies its own baseline years.
- **p-value:** paper bootstrap stratified by year (B = 2,000); p = (1 + #{ratio_b >= 0.90})/(B + 1).
- **Confirm if:** BH-adjusted p < .05, ratio < 0.90, and the gate.
- **Contradicted if:** lower 95% bound > 0.90.
- **Gate:** acceptance-margin: tipping point D* = (b_acc - 0.9 b_all)/(1 - 0.9 a0) (net camera-ready change of the accepted F24 prevalence that would lift the ratio to 0.90); passes if the F24 abstract audit is auditable and its net-flip DiD lower 95% bound > D*.
- **Discovery dry run:** 0.717, 95% CI [0.495, 0.888]; one-sided p = 0.01799.
- **Projected held-out power (approximate):** z_heldout_projected 0.89; alpha_0.0083 0.07; alpha_0.05 0.23.

### CT11: D4 pool invariance of the break (H4a(iii)) (secondary)

- **Data:** held-out 2018-2026, ACC, REJ and WD pools.
- **Statistic:** CT1 logit fitted separately per pool; joint cluster-robust covariance from influence functions summed by topic100 (d4_stage_gains.its_pools). Statistic: the three pairwise differences in slope-change log OR.
- **p-value:** TOST at +/-0.1 per pair (normal); p = max over the three pairs.
- **Confirm if:** BH-adjusted p < .05, every pairwise 90% CI inside (-0.1, 0.1), and the gate.
- **Contradicted if:** any pairwise 90% CI entirely outside [-0.1, 0.1].
- **Gate:** acceptance-margin for the ACC pairs: widen their 90% CIs by b_max = (D_hi - D_lo)/(2 p (1 - p)) from the frozen NAME title audit and the held-out ACC NAME share p (2024-26); widened CIs must stay inside (-0.1, 0.1). The REJ-WD pair is audit-free.
- **Discovery dry run:** ACC-REJ -0.061; ACC-WD -0.050; REJ-WD 0.010, 90% CI ACC-REJ [-0.148, 0.027]; ACC-WD [-0.170, 0.069]; REJ-WD [-0.101, 0.122]; one-sided p = 0.2469.
- **Projected held-out power (approximate):** P(pair equivalent), approx, per pair [0.00, 0.00, 0.00]; heldout_se_projected [0.11, 0.15, 0.14].

### CT12: D2 role gradient (H2b) (secondary)

- **Data:** as CT3.
- **Statistic:** rho_first - rho_last (first-list-position minus last-list-position within-stayer share), same stayers and windows as CT3.
- **p-value:** joint key-cluster bootstrap (the CT3 draws); p = (1 + #{diff_b >= 0})/(B + 1).
- **Confirm if:** BH-adjusted p < .05 and upper 95% bound < 0.
- **Contradicted if:** lower 95% bound > 0.
- **Gate:** none (diachronic within-key change).
- **Discovery dry run:** -0.470, 95% CI [-0.602, -0.359]; one-sided p = 0.000999.
- **Projected held-out power (approximate):** z_heldout_projected 3.68; alpha_0.0083 0.90; alpha_0.05 0.98.

## 5. Audit gate

The PLAN gate says that no acceptance-margin result is called confirmed unless the audit tipping point exceeds the audit's CI. Diachronic and camera-ready-free tests (CT1–CT4, CT7–CT9, CT12) are not gated. The gated tests, with their operational rules fixed now:

- **CT5:** acceptance-margin: the editing-corrected 90% CI (held-out bootstrap paired with draws of the audit net-flip DiD, WP4 G1 construction, frozen title audit) must lie inside [0.90, 1.11].
- **CT6:** acceptance-margin (G_total): L-union must be auditable with the tipping point beyond the audit CI. It is not auditable (abstract em dash and title typography: 0 v1-present pairs in both arms), so CT6 cannot reach 'confirmed'; G_desk x G_exit is reported as the audit-free component.
- **CT10:** acceptance-margin: tipping point D* = (b_acc - 0.9 b_all)/(1 - 0.9 a0) (net camera-ready change of the accepted F24 prevalence that would lift the ratio to 0.90); passes if the F24 abstract audit is auditable and its net-flip DiD lower 95% bound > D*.
- **CT11:** acceptance-margin for the ACC pairs: widen their 90% CIs by b_max = (D_hi - D_lo)/(2 p (1 - p)) from the frozen NAME title audit and the held-out ACC NAME share p (2024-26); widened CIs must stay inside (-0.1, 0.1). The REJ-WD pair is audit-free.

**Audit state frozen in the bundle.**
- Original audit: 331 usable pairs.
- Enlargement: 1261 records, of which 634 are usable pairs. The pooled title audit therefore has 965 pairs.
- arXiv v1 abstracts: 330 pairs.

**Refreeze rule.** The background enlargement (WP4) samples discovery papers only, so it carries no held-out information. Before held-out data are requested, `python -m analyses.prereg_confirm audit_refreeze` may be run once. It recomputes the same flip tables, with the same code, on all enlargement records present at that moment, writes them to `frozen/audit_refreeze/` and appends their hashes to `audit_refreeze.sha256`. If that directory exists, the held-out gate uses it. Otherwise the gate uses the bundle-time audit. Both versions are reported.

## 6. Discovery dry run

Each test applied to the discovery split. The verdicts are **as if** discovery were the held-out data; they show which decision rules the discovery estimates already meet. Adjusted p-values use the same families.

| Test | Estimate | CI | p (one-sided) | p adjusted | Gate | Verdict as if | Reasons |
|---|---|---|---|---|---|---|---|
| CT1 | 1.098 | [1.044, 1.154] (95%) | 0.0001282 | 0.0007695 | n/a | not confirmed | point estimate not beyond the minimal effect |
| CT2 | 1.353 | [0.020, 2.701] (95%) | 0.02499 | 0.04998 | n/a | not confirmed | CI rule not met |
| CT3 | 0.995 | [0.943, 1.050] (95%) | 0.000999 | 0.002997 | n/a | confirmed | - |
| CT4 | 2.551 | [1.530, 4.255] (95%) | 0.0001654 | 0.000827 | n/a | confirmed | - |
| CT5 | 1.021 | [1.001, 1.041] (90%) | 0.0004998 | 0.001999 | pass | confirmed | - |
| CT6 | G_total 0.975; G_desk_x_exit 0.981 | G_total [0.951, 1.001]; G_desk_x_exit [0.972, 0.992] (95%) | 0.02999 | 0.04998 | fail | not confirmed | audit gate not passed |
| CT7 | 1.461 | [1.168, 1.828] (95%) | 0.0004546 | 0.0009995 | n/a | confirmed | - |
| CT8 | RR_R24 0.744; RR_R26 1.944 | RR_R24 [0.642, 0.862]; RR_R26 [1.672, 2.261] (95%) | 4.309e-05 | 0.0002585 | n/a | confirmed | - |
| CT9 | 0.982 | [0.961, 1.004] (95%) | 0.0004998 | 0.0009995 | n/a | confirmed | - |
| CT10 | 0.717 | [0.495, 0.888] (95%) | 0.01799 | 0.02159 | pass | confirmed | - |
| CT11 | ACC-REJ -0.061; ACC-WD -0.050; REJ-WD 0.010 | ACC-REJ [-0.148, 0.027]; ACC-WD [-0.170, 0.069]; REJ-WD [-0.101, 0.122] (90%) | 0.2469 | 0.2469 | fail | not confirmed | adjusted p >= .05; point estimate not beyond the minimal effect; CI rule not met; audit gate not passed |
| CT12 | -0.470 | [-0.602, -0.359] (95%) | 0.000999 | 0.001499 | n/a | confirmed | - |

**What the dry run implies for the held-out run.** These points were fixed before held-out access and are not grounds for changing any rule:

- CT1: the discovery OR (1.098) is below the pre-registered minimal effect of 1.10. Even with the discovery value as the true effect, the projected held-out z is about 1.8, not the ≈ 6 stated in the PLAN (that figure came from the pilot's 1.28, which was for compound titles). CT1 will most likely end as 'not confirmed'.
- CT2: in discovery, the upper bound of the content share is 0.657 (point 0.574), so the '< 0.60' condition already fails. The acceleration itself is +1.35 pp/yr [0.02, 2.70], ratio 1.89. This CI is wider than D1's conditional CI [0.56, 2.15] because the held-out design resamples the discovery calibration years and the test years independently. In the held-out data they really are independent, so obs_{y-1} no longer telescopes out of the year-to-year steps. Projected held-out z ≈ 1.0, so CT2 is underpowered.
- CT6: the L-union is unauditable, so CT6 cannot be 'confirmed' under the gate. The audit-free G_desk x G_exit = 0.981 (one-sided p 0.0005) will be reported as such.
- CT11: no discovery pair is equivalent within ±0.1 (90% CIs ACC-REJ [-0.148, 0.027]; ACC-WD [-0.170, 0.069]; REJ-WD [-0.101, 0.122]). The held-out CIs are about twice as wide, so CT11 is expected to be 'not confirmed'. Its ACC-pair gate also fails in discovery (b_max = 0.107).
- CT5: discovery G_total 1.021, 90% CI [1.001, 1.041]. The editing-corrected 90% CI [0.944, 1.036] passes the gate.
- CT10: discovery ratio 0.717 [0.495, 0.888]. Tipping point -2.86 pp against an audit lower bound of -1.62 pp: the gate passes. The held-out split's own 2021–23 baseline years are small, so the CI will be wide.
- Approximate projected probability of meeting the statistical rule at α = .05 (unadjusted) is below 0.5 for: CT1 (0.48), CT2 (0.26), CT6 (0.15), CT10 (0.23), CT11 (0.00). For these tests, a 'not confirmed' held-out result is weak evidence against the discovery finding.

## 7. Clarifications and deviations from PLAN section 4

1. Code commit: no git commands are run in this work package, so the code is frozen by content hashes (bundle.sha256) rather than by a commit id. The commit itself is left to the orchestrator.
2. R1 vectoriser and classifiers: D1 saved scores, not models. The rolling R1 models were refitted with D1's CV-chosen C and D1's StratifiedKFold folds (seed 0). Their test-row fold scores reproduce D1's stored scores (see params.json, `max_abs_diff_test_scores_vs_d1`).
3. CT2 inference: the PLAN asks for a paper bootstrap stratified by year. Held-out papers are resampled within year. Because the recalibration targets discovery obs_{y-1}, the discovery calibration-year papers are also resampled, independently, and the shift is re-solved each replicate. The content-share condition uses the share of the summed 2024–26 steps, as in D1.
4. CT3/CT12: stayer status uses any-role presence (D2-2). The E side uses the discovery ∪ held-out union (PLAN: 'an E-period paper (union)'); P_E and P_SE are computed over union E rows. L outcomes are held-out only. rho uses the pilot/D2 definition (P_SL − P_SE)/(P_L − P_E) (D2-1).
5. CT5/CT6 pooling: 2024–26 is year-standardised to s0 sizes (D4). G_desk × G_exit uses the PLAN stages (accepted papers are inside s0–s2). The camera-ready-free variant (accepted papers removed) is reported as a pre-specified robustness check.
6. Gate operationalisation (fixed now): CT5 uses the editing-corrected TOST (the WP4 G1 construction). CT6's G_total gate cannot pass, because the L-union is unauditable. CT10 uses an explicit tipping point for the 0.90 ratio against the F24 abstract audit. CT11 widens the ACC-pair CIs by the largest slope bias that editing within the NAME audit CI could create. The gate audit is the pooled original + enlargement audit (the larger audit), with the refreeze rule of section 5.
7. CT8 statistic: the PLAN says 'R24 down and R26 up (two one-sided tests)'. Here this is the within-area quasi-Poisson rate ratio 2026/2025 (D3 H3b model, area FE and offset) on the 16 frozen large areas, with an intersection-union p. Area sign counts are descriptive only, because the held-out areas are about a quarter of discovery size.
8. CT9 estimand: 2023→2026, with F = f24_2 ∪ f26 ∪ title_typo, the D1 primary fingerprint.
9. CT10: the Kobak bound uses F24 (any RARE21 word) with the conservative baseline. 'Pooled 2024–26' is the mean of the three yearly bounds (D4). The held-out split supplies its own 2021–23 baseline.
10. CT11: 'equivalent within ±0.1' means that all three pairwise 90% CIs lie inside (−0.1, 0.1). The CT11 p-value is the largest pairwise TOST p.
11. Expected z: the PLAN's 'expected z ≈ 6' for CT1 came from the pilot's 1.28/yr, which was for compound titles. The dry run gives the discovery-based projection.
12. The DFL cell model is frozen, as the PLAN requires, but no CT uses it, because there is no confirmatory test of H1d.
13. Fixed seeds reproduce the work packages' bootstrap draws wherever the inputs coincide: D4 stage gains, the D4 Kobak bound, the D2 key bootstrap and D1's f0_rise.

## 8. Running the confirmation

```bash
cd research/titles/src
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.prereg_confirm verify
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.prereg_confirm heldout <heldout_submissions.csv.gz> <heldout_submission_authors.csv.gz>
```

The run writes `outputs/prereg/heldout.json`, with the same fields as `dryrun.json`.

The guard file `heldout_started.json` logs every attempt. A run that crashes before writing `heldout.json` is a technical failure, not a result; it may be restarted with `--force`, and the restart is logged. Once `heldout.json` exists, the run cannot be repeated.
