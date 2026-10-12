# Pre-registration: held-out confirmation of the ICLR title study (WP9)

- **Date:** 2026-10-11
- **Plan:** `docs/PLAN.md` section 4 (sha256 `680eb53564005fd8...`)
- **Bundle hash:** `6853685bf21a08cdb40227d7fe5d94285c3ec023a9354ab3971faec75051ecd9` (SHA-256 of `outputs/prereg/bundle.sha256`)
- **Revision 3** (second integration pass, 2026-10-11). Supersedes bundle hash `853827a92e85ad56ee85376e8b90a881c4f4ca1e46a861e80ed21a04e883d922` (revision 2). Why: Cross-direction consistency corrections before any held-out data were requested or seen (no guard file, no heldout.json): (1) reading notes for CT1, CT2, CT4, CT6 and CT12 state what a confirmed statistic would and would not show given the direction audits (CT1 and CT2 use paper-level inference that D1's audit demoted; CT4 leans on via/using and 'enhancing'; CT6 mostly re-detects the pre-2024 R24 penalty; CT12 mixes cohort with tenure); the decision rules are unchanged; (2) required code outside the tests changed: d3_slots.py reads WP4's frozen enlargement sample (2,004 lines, SHA-256 checked) for D3's descriptive slot-word audit instead of a 1,620-line pre-freeze pin and fails loudly without the audit caches; d4_bias_atlas.py makes atlas prevalence ratios reuse the stage-gain bootstrap seed. No CT uses either change. Frozen parameters other than params.json -> revision and rules.json are byte-identical, and the dry run was re-run with every statistic, CI, p-value and gate field unchanged. Details in section 9.
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
- **Gate:** acceptance-margin association (G_total), WP4 Holm gate: L-union must be auditable (count and arXiv channel), its editing-corrected 95% interval below 1 and its identification p must survive Holm at 0.025. It is not auditable (title typography and the abstract em dash cannot be carried by arXiv metadata), so CT6 cannot reach 'confirmed'; G_desk x G_exit is reported as the audit-free component.
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
- **Gate:** acceptance-margin association, WP4 Holm gate: tipping point D* = (b_acc - 0.9 b_all)/(1 - 0.9 a0) (net camera-ready change of the accepted F24 prevalence that would lift the ratio to 0.90); passes if the F24 abstract audit (2024-26 v1-abstract pairs) is auditable, the editing-corrected ratio's upper 95% bound is < 0.90, and the identification p (z = (D_hat - D*)/sqrt(se_D^2 + se_D*^2)) survives Holm at one-sided 0.025 across the run's auditable association claims.
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
- **CT6:** acceptance-margin association (G_total), WP4 Holm gate: L-union must be auditable (count and arXiv channel), its editing-corrected 95% interval below 1 and its identification p must survive Holm at 0.025. It is not auditable (title typography and the abstract em dash cannot be carried by arXiv metadata), so CT6 cannot reach 'confirmed'; G_desk x G_exit is reported as the audit-free component.
- **CT10:** acceptance-margin association, WP4 Holm gate: tipping point D* = (b_acc - 0.9 b_all)/(1 - 0.9 a0) (net camera-ready change of the accepted F24 prevalence that would lift the ratio to 0.90); passes if the F24 abstract audit (2024-26 v1-abstract pairs) is auditable, the editing-corrected ratio's upper 95% bound is < 0.90, and the identification p (z = (D_hat - D*)/sqrt(se_D^2 + se_D*^2)) survives Holm at one-sided 0.025 across the run's auditable association claims.
- **CT11:** acceptance-margin for the ACC pairs: widen their 90% CIs by b_max = (D_hi - D_lo)/(2 p (1 - p)) from the frozen NAME title audit and the held-out ACC NAME share p (2024-26); widened CIs must stay inside (-0.1, 0.1). The REJ-WD pair is audit-free.

**Gate rule (adopted in revision 2; unchanged since).** WP4 multiplicity-controlled gate (revision 2). Association claims (CT6 G_total, CT10): the marker must be auditable (>= 10 v1-present per arm and measurable through arXiv metadata), its editing-corrected 95% interval (bootstrap replicate paired with an audit draw D ~ N(D_hat, se_D)) must lie beyond the claim's boundary, and its one-sided identification p, z = (D_hat - D*)/sqrt(se_D^2 + se_D*^2) with se_D the pseudo-flip SE and se_D* the bootstrap SE of the tipping point, must survive Holm at 0.025 across the run's auditable association claims. Equivalence claims (CT5, CT11): editing-corrected interval rules (CT5 = WP4 G1 TOST; CT11 = ACC-pair CIs widened by the largest editing bias inside the NAME audit CI).

**Audit state frozen in the bundle** (WP4's final audit; `frozen/audit_state.json`).
- Original audit: 331 usable pairs (2022–26; sensitivity spec), 322 of them in 2023–26.
- Enlargement: the complete file, 2004 lines (2000 records without a network error; SHA-256 `dd51d5faaa0a7937...`, identical to WP4's freeze: True), of which 989 are usable pairs.
- Title gate audit (WP4 primary, 2023–26): 1311 pairs ({'accepted': 803, 'rejected': 508}).
- Abstract gate audit (WP4 primary, 2024–26 v1-abstract pairs): 1032 pairs ({'accepted': 628, 'rejected': 404}).
- The frozen flip tables reproduce WP4's canonical `T4_2_flip_matrices.csv` (primary) and `abstract_audit.csv` (abs_2024_26) exactly: max |difference| primary 9.6e-17, abs_2024_26 9.7e-17; auditability identical.

**Refreeze rule: closed.** Revision 1 allowed one `audit_refreeze` before held-out access because the background enlargement was still running. The enlargement is now complete and frozen in the bundle itself, so `audit_refreeze` refuses to run.

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
| CT10 | 0.717 | [0.495, 0.888] (95%) | 0.01799 | 0.02159 | fail | not confirmed | audit gate not passed |
| CT11 | ACC-REJ -0.061; ACC-WD -0.050; REJ-WD 0.010 | ACC-REJ [-0.148, 0.027]; ACC-WD [-0.170, 0.069]; REJ-WD [-0.101, 0.122] (90%) | 0.2469 | 0.2469 | fail | not confirmed | adjusted p >= .05; point estimate not beyond the minimal effect; CI rule not met; audit gate not passed |
| CT12 | -0.470 | [-0.602, -0.359] (95%) | 0.000999 | 0.001499 | n/a | confirmed | - |

**What the dry run implies for the held-out run.** These points were fixed before held-out access and are not grounds for changing any rule:

- CT1: the discovery OR (1.098) is below the pre-registered minimal effect of 1.10. Even with the discovery value as the true effect, the projected held-out z is about 1.8, not the ≈ 6 stated in the PLAN (that figure came from the pilot's 1.28, which was for compound titles). CT1 will most likely end as 'not confirmed'.
- CT2: in discovery, the upper bound of the content share is 0.657 (point 0.574), so the '< 0.60' condition already fails. The acceleration itself is +1.35 pp/yr [0.02, 2.70], ratio 1.89. This CI is wider than D1's conditional CI [0.56, 2.15] because the held-out design resamples the discovery calibration years and the test years independently. In the held-out data they really are independent, so obs_{y-1} no longer telescopes out of the year-to-year steps. Projected held-out z ≈ 1.0, so CT2 is underpowered.
- CT6: the L-union is unauditable (arXiv cannot carry title typography or the em dash), so CT6 cannot be 'confirmed' under the gate. The audit-free G_desk x G_exit = 0.981 (one-sided p 0.0005) will be reported as such.
- CT11: no discovery pair is equivalent within ±0.1 (90% CIs ACC-REJ [-0.148, 0.027]; ACC-WD [-0.170, 0.069]; REJ-WD [-0.101, 0.122]). The held-out CIs are about twice as wide, so CT11 is expected to be 'not confirmed'. Its ACC-pair gate also fails in discovery (b_max = 0.092).
- CT5: discovery G_total 1.021, 90% CI [1.001, 1.041]. The editing-corrected 90% CI [0.949, 1.031] passes the gate.
- CT10: discovery ratio 0.717 [0.495, 0.888]. Tipping point -2.86 pp (se 1.55) against the F24 abstract-audit DiD +0.71 pp [-1.95, 3.36]: identification p 0.0414 (Holm 0.04137, family ['CT10']); editing-corrected upper 95% bound of the ratio 0.918. The gate fails (the revision-1 uncorrected rule would pass). The held-out split's own 2021–23 baseline years are small, so the CI will be wide.
- CT1 (reading): CT1's p-value uses paper-level SEs clustered by topic100 (dry run 1.3e-04). D1's audit showed that these ignore year shocks: the year-level REML p in discovery is 0.035 (Holm 0.071). A confirmed CT1 (which needs OR >= 1.10) should be reported with the year-level test beside it, and on its own it would not establish a dated 2024 break.
- CT2 (reading): the held-out bootstrap resamples papers within year, so it holds year shocks fixed; a confirmed CT2 would not establish year-level acceleration. D1's two-stage year-level CI in discovery is [0.03, 2.71] pp (Holm 0.067); the dry-run CI [0.02, 2.70] is similar in width but contains no year-shock variance.
- CT4 (reading): a confirmation confirms the stacked slot-minus-control statistic on the pre-registered 2024 specification. The control contrast leans on via/using (without it the stacked contrast is 1.41 [0.74, 2.68]); OR >= 2 for the slots rests on the in-sample word 'enhancing' (without it 1.72 [1.04, 2.84]); the pooled controls shift at the other candidate break years (2020, 2021, 2022, 2023, 2025); and the break is not sharply dated against 2023.
- CT6 (reading): an L-union G < 1, including the audit-free G_desk x G_exit, would mainly re-detect the pre-2024 R24 genre penalty (D4: R24 total 0.807 in 2024-26 against 0.815 in 2018-23; L-union without R24 0.998). LLM-specific selection would need the L-union without R24 or the post/pre ratio, which CT6 does not test.
- CT12 (reading): a confirmation confirms the D2-group contrast rho_first - rho_last, which mixes cohort with tenure (D2 stayer keys have >= 3 years of presence): within the same last-position key the entrant-first premium is 4.9 pp [2.2, 7.6], and with a symmetric 2-year lookback prior first keys changed 0.86 [0.72, 1.01] times the first-position population. It is not a role effect: list position is a partition label.
- CT3 (reading): the D2 audit found that a purely generational world with the observed co-authorship gives rho_last of 0.88-0.93, above the 0.5 threshold, so a confirmed CT3 would confirm the statistic, not communal change (H2a is 'not identified' in discovery).
- CT7 (reading): without the lemmas shared by RARE21 and R24 the discovery ratio is 1.32 [1.04, 1.66] with OR(F24) 1.00; the contrast is carried by F26 papers avoiding R24, so a confirmed CT7 would not by itself establish title-abstract vintage alignment.
- CT8 (reading): neutral synonyms (improv*, utili[sz]*, exploit*) fell like R24 in discovery (R24 relative to them 1.08 [0.86, 1.36]) and R26 was chosen after the pilot saw it rise, so a confirmed CT8 would show a 2026 shift in these word families, not a register turnover.
- CT9 (reading): the D3 positive control with this fingerprint is not significant (slot OR 1.29 [0.92, 1.81]) and criterion (i) has little power by construction, so a confirmed CT9 would not bound the tool share.
- Approximate projected probability of meeting the statistical rule at α = .05 (unadjusted) is below 0.5 for: CT1 (0.48), CT2 (0.26), CT6 (0.15), CT10 (0.23), CT11 (0.00). For these tests, a 'not confirmed' held-out result is weak evidence against the discovery finding.

## 7. Clarifications and deviations from PLAN section 4

1. Code commit: no git commands are run in this work package, so the code is frozen by content hashes (bundle.sha256) rather than by a commit id. The commit itself is left to the orchestrator.
2. R1 vectoriser and classifiers: D1 saved scores, not models. The rolling R1 models were refitted with D1's CV-chosen C and D1's StratifiedKFold folds (seed 0). Their test-row fold scores reproduce D1's stored scores (see params.json, `max_abs_diff_test_scores_vs_d1`).
3. CT2 inference: the PLAN asks for a paper bootstrap stratified by year. Held-out papers are resampled within year. Because the recalibration targets discovery obs_{y-1}, the discovery calibration-year papers are also resampled, independently, and the shift is re-solved each replicate. The content-share condition uses the share of the summed 2024–26 steps, as in D1.
4. CT3/CT12: stayer status uses any-role presence (D2-2). The E side uses the discovery ∪ held-out union (PLAN: 'an E-period paper (union)'); P_E and P_SE are computed over union E rows. L outcomes are held-out only. rho uses the pilot/D2 definition (P_SL − P_SE)/(P_L − P_E) (D2-1).
5. CT5/CT6 pooling: 2024–26 is year-standardised to s0 sizes (D4). G_desk × G_exit uses the PLAN stages (accepted papers are inside s0–s2). The camera-ready-free variant (accepted papers removed) is reported as a pre-specified robustness check.
6. Gate operationalisation (revision 2): CT5 uses the editing-corrected TOST (the WP4 G1 construction). CT6's G_total gate cannot pass, because the L-union is unauditable (arXiv channel). CT10 uses an explicit tipping point for the 0.90 ratio against the F24 abstract audit, with WP4's identification p (tipping-point SE included), an editing-corrected interval and Holm at 0.025 across the run's auditable association claims. CT11 widens the ACC-pair CIs by the largest slope bias that editing within the NAME audit CI could create. The gate audit is WP4's frozen complete audit (title: 2023–26 primary pairs; abstracts: 2024–26 pairs). Revision 1 used the original audit + 1,261 enlargement lines and an uncorrected rule.
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

## 9. Revision history

- **Revision 1** (2026-10-11, bundle hash `f69fdb468702fe11e336b81476869531a71acb1d4f922b8bd1d479934bbac628`): gate audit = original audit + first 1,261 enlargement lines (965 pooled title pairs incl. 2022; 330 v1 abstracts of the original pairs); gate = point tipping point beyond the 95% audit CI (uncorrected).
- **Revision 2** (2026-10-11, bundle hash `853827a92e85ad56ee85376e8b90a881c4f4ca1e46a861e80ed21a04e883d922`): Post-audit corrections before any held-out data were requested or seen (no guard file, no heldout.json): (1) the D3 and D4 fixer passes changed required code hashed by revision 1 (d3_register.py, d3_slots.py, d3_vintage.py, d4_bias_atlas.py, d4_stage_gains.py; the frozen test definitions they supply are unchanged); (2) the WP4 enlargement finished (2,004 lines, 2,000 records) and the gate audit is re-frozen on WP4's complete audit; (3) the gate adopts WP4's multiplicity-controlled rule (identification p with the tipping point's sampling error, Holm at 0.025, editing-corrected interval), because the revision-1 uncorrected rule admits acceptance associations that the Holm gate rejects. The R1 models, centroids, lexicons, slot inventory, DFL cells and every test statistic are unchanged (frozen files byte-identical).
- **Revision 3** (this file, bundle hash `6853685bf21a08cdb40227d7fe5d94285c3ec023a9354ab3971faec75051ecd9`): Cross-direction consistency corrections before any held-out data were requested or seen (no guard file, no heldout.json): (1) reading notes for CT1, CT2, CT4, CT6 and CT12 state what a confirmed statistic would and would not show given the direction audits (CT1 and CT2 use paper-level inference that D1's audit demoted; CT4 leans on via/using and 'enhancing'; CT6 mostly re-detects the pre-2024 R24 penalty; CT12 mixes cohort with tenure); the decision rules are unchanged; (2) required code outside the tests changed: d3_slots.py reads WP4's frozen enlargement sample (2,004 lines, SHA-256 checked) for D3's descriptive slot-word audit instead of a 1,620-line pre-freeze pin and fails loudly without the audit caches; d4_bias_atlas.py makes atlas prevalence ratios reuse the stage-gain bootstrap seed. No CT uses either change. Frozen parameters other than params.json -> revision and rules.json are byte-identical, and the dry run was re-run with every statistic, CI, p-value and gate field unchanged.
- What changed in the dry run: revision 2 changed only the gate fields of CT5, CT6, CT10 and CT11 (new audit, new rule); revision 3 changed nothing in `dryrun.json` except the bundle hash (re-run and compared). Every test statistic, p-value and CI of CT1–CT12 is computed by the same frozen functions on the same discovery data. Superseded bundle files are not kept in `outputs/prereg/`; the integration pass's pre-change copies are in `outputs/audit/integration/pre_fix_backup/` (pass1: revision 1; pass2: revision 2).
