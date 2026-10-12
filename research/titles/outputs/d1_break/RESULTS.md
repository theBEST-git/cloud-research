# D1 Results: The naming acceleration (pre-registered as "the 2024 naming break"): content, composition, or tool?

Work package WP5. Pre-registered in `docs/PLAN.md` §D1; common definitions §0. **Audit revision**: three independent audits (code, identification, reporting) found a calibration bug in the content models, paper-level inference where the treatment varies only across years, an uncorrected tool bound and several reporting problems. All numbers below were regenerated after the fixes (`src/analyses/d1_its.py`, `d1_content_cf.py`, `d1_decompose.py`, `d1_summary.py`). The issue-by-issue response is in the last section, "Audit response"; the run log is `outputs/audit/d1/fix_log.md`. Machine-readable estimates are in `results.json`. **Integration pass (after all directions were audited):** the D3 positive control for H1e is now reported (§5); no D1 estimate changed. Every statement about acceptance or topic is associational. Author-side quantities use declared profile keys, not persons.

**Population.** Universe U: 43,482 submissions, 2017–2026. 34 placeholder rows were dropped: 1 / 5 / 7 / 1 / 4 / 0 / 0 / 1 / 7 / 8 in 2017 … 2026.
**Outcome.** NAME (primary) = `name_primary`, a coined lead before a colon or spaced dash.
- NAME share: 20.3% (2023) → 26.6 / 33.1 / 40.5% (2024 / 25 / 26).
- The 2023→2026 rise is ΔNAME = 20.2 pp.

## Verdict summary

| Hypothesis | Pre-registered prediction | Estimate (95% CI) | Falsification rule | Verdict | Holm-adj. p¹ |
|---|---|---|---|---|---|
| H1a dated break | Slope-change OR > 1 on U; holds in NA and non-LLM; sup-LR picks 2024/25; placebos 2020–22 null | Paper level: OR 1.098 [1.044, 1.154]/yr. **Year level (primary): OR 1.096 [0.990, 1.214], p = 0.035.** NA pool, year level: 1.121 [1.019, 1.232]. Non-LLM, year level: 1.108 [0.986, 1.245]. Excluding 2026: 1.046 [0.807, 1.355] (year level), 1.052 [0.964, 1.147] (paper level). Placebos 0.85–0.93, all CIs include 1. Level+slope sup-LR picks **2023**; the kink-only scan (post hoc) picks 2024. Randomization p over break years = 0.143 (minimum attainable 1/7). | NA CI includes 1, or a placebo ≥ actual | **Partially supported** (not falsified). Acceleration on the probability scale is clear; a *dated 2024* break is not identified, and on U the year-level CI includes 1. | 0.071 (paper-level Wald: 0.0006; randomization p: 0.29) |
| H1b content minority | Masked content share in [0.20, 0.50] for every masked representation; none ≥ 0.60 | Fixed window: R1 0.389 [0.349, 0.434], R3 0.492 [0.444, 0.544], R5 0.381 [0.341, 0.425]. Rolling: R1 0.574 [0.531, 0.621] (refit [0.505, 0.636]), R3 0.577 [0.534, 0.627], R5 0.565 [0.522, 0.613]. Sensitivities: training-year FE 0.37–0.55; intercept+slope recalibration 0.45–0.65. | Any masked share ≥ 0.60 | **Partially supported: not falsified, but the prediction fails.** No pre-registered masked share reaches 0.60, but the rolling shares exceed 0.50, 0.60 lies inside every rolling CI, and slope recalibration puts R1/R5 rolling at 0.65/0.64. "Content is a minority" is not established. | 0.18 |
| H1c drift acceleration | mean u(2024–26) − mean u(2019–23) > 0; ratio ≥ 1.5 | u: 1.51 → 2.87 pp/yr. Diff +1.35 pp. Paper bootstrap: conditional [0.56, 2.15], refit [0.47, 2.23]. **Year level (primary, two-stage): [0.03, 2.71], p = 0.022**; ratio 1.89 [1.02, 3.55], P(ratio < 1.5) = 0.23. Permutation p = 0.14. Year-level CI includes 0 in the NA pool (+1.14 [−0.10, 2.39]), non-LLM subset (+0.55 [−0.90, 1.99]), R3 (+1.29 [−0.03, 2.61]), strict NAME and excluding 2026 (+1.15 [−0.63, 2.96]). | Ratio < 1.2, or the diff CI includes 0 | **Not established at the year level.** The point estimate is positive under every content specification. The R1 year-level CI barely excludes 0, the test fails Holm, and the falsification rule is met in the camera-ready-free pool and in the non-LLM subset. | 0.067 (paper-level: 0.007) |
| H1d composition minority | DFL composition share ≤ 0.30 | Fixed 2-year new-key lookback: 2024 0.287 [0.202, 0.410], 2025 **0.316** [0.259, 0.386], 2026 0.261 [0.223, 0.301]. Shapley composition share 0.088 [0.077, 0.101] (refit [0.039, 0.154]). | Share ≥ 0.50 | **Partially supported.** The prediction holds for 2024 and 2026 but not for 2025, and is far from the 0.50 falsification line in every year. | 0.008 |
| H1e tool bounded | F=0 rise ≥ 85% of total; δ ≤ +5 pp; tool share at A_max < 0.25 | F=0 rise / all 0.98 [0.96, 1.00]. δ = +1.6 pp [0.0, 3.2]. Tool share at A = 0.39, corrected for fingerprint misclassification and year-matched: **7.1% [1.4, 12.9]** (uncorrected pre-registered formula 3.1% [0.0, 6.2]). Sensitivities up to 16% [6, 27] (F_any DiD) and 19–33% (title typography, upper CI 0.41–0.55). | F=0 < 70%, or tool share at 0.39 ≥ 0.5 | **Supported as pre-registered (abstract fingerprint), but not robust as a bound, and not validated by a positive control on its own fingerprint.** D3's slot uplift with D1's fingerprint F_d1 is OR 1.29 [0.92, 1.81] (not significant); with D3's broader F_any it is 1.42 [1.14, 1.79]. | 0.002 |

¹ Holm over H1a–H1e, using the year-level tests for H1a and H1c (`results.json → holm`). The p-values test the **falsification boundary**, not the prediction:
- H1b tests share ≥ 0.60, though the prediction is ≤ 0.50.
- H1d tests share ≥ 0.50, though the prediction is ≤ 0.30. The prediction-level tail probabilities are P(DFL share ≥ 0.30) = 0.41 / 0.71 / 0.03 for 2024 / 25 / 26.
- H1e tests F0 ratio ≤ 0.70 and corrected tool share ≥ 0.5; the predictions are ≥ 0.85 and < 0.25.
- H1c tests diff ≤ 0. At the prediction level, P(ratio < 1.5) = 0.23 under the two-stage inference and 0.13 under the conditional bootstrap.

Holm under alternative p choices:
- **Paper-level family** (cluster-Wald for H1a, paper bootstrap for H1c, as in the first version): H1a 0.0006, H1c 0.007, H1d 0.006, H1e 0.002, H1b 0.18.
- **H1a randomization p** (0.143): H1a 0.29, H1b 0.29.

**How the p-values were computed:**
- H1a: one-sided t(6) test of the slope change in a REML random-effects meta-regression on the covariate-adjusted logit year effects. It allows a year-shock variance τ².
- H1b: intersection–union of bootstrap P(share ≥ 0.60), taking the maximum over the masked representations, both designs and the refit bootstrap.
- H1c: two-stage P(diff ≤ 0), combining refit paper-bootstrap draws (B = 300) with simulated year shocks (τ from H1a).
- H1d: intersection–union over 2024–26 of bootstrap P(DFL share ≥ 0.50).
- H1e: intersection–union of bootstrap P(F0 ratio ≤ 0.70) and the one-sided Wald P(corrected tool share at A = 0.39 ≥ 0.5).
- Bootstrap p-values use the (k+1)/(B+1) floor.

**Headline.**
- **What changed.** The NAME logit trend became convex. It accelerated from about 2022–24, and the acceleration is most visible in 2026.
  - On the probability scale the slope change is +3.0 pp/yr [2.1, 3.8] on an LPM pre-trend of +1.35 pp/yr. At the year level it is +2.8 pp/yr [1.3, 4.4]; in the NA pool, +3.3 pp/yr [1.7, 5.0].
  - On the log-odds scale the change is smaller: OR 1.098 on a pre-trend OR of 1.125. With year-level inference it is marginal on U (p = 0.035; Holm 0.07) and null without 2026.
  - A dated 2024 break fits no better than a 2023 break or a smooth convex trend.
- **What content explains.** Of the +4.7 pp/yr acceleration in annual NAME gains (2.1 → 6.7 pp/yr), about 70% (+3.3 pp/yr) is predicted by name-masked abstract content (R1, rolling). About 30% (+1.35 pp/yr) is unexplained.
  - Content accounts for about 0.37–0.65 of the 2023→26 rise, depending on design and calibration.
  - The pre-registered falsification line (0.60) is not crossed after the calibration fix. But the "content is a minority" prediction is not met either.
  - Most of the content signal is the shift toward LLM-era topics, so "content" and the LLM topic/tool channel are not separated.
- **Unexplained drift.** It rose (1.5 → 2.9 pp/yr). This acceleration is not established once year-to-year shocks are allowed for. It is absent from the camera-ready-free pool and the non-LLM subset at the year level.
- **Composition** (team size × new keys × llm_topic) accounts for about a quarter of the rise by DFL (0.26–0.32 across 2024–26). Its Shapley share once content is included is about 0.09.
- **Detectable LLM drafting** accounts for 7% [1, 13] at A = 0.39 after correcting for fingerprint misclassification.
  - This is a model-conditional estimate, not an upper bound.
  - Title-level and selection-corrected markers give 16–33%.
  - "Not the main driver" holds for the pre-registered fingerprint. "Small and bounded from above" is not established.
  - The D3 positive control does not validate this estimate: with D1's own fingerprint F_d1, D3's meaning-fixed slot uplift is OR 1.29 [0.92, 1.81], not significant (§5).

---

## 1. H1a: slope change (T1.1, `T1_1_its.csv`, `its_year_level.csv`; supplementary `fig_its_scan`)

**Model.** Segmented logit
`NAME ~ (t−2023) + post + post·(t−2023) + log authors + llm_topic + topic100 FE`.

**Inference.** The slope change varies only across 10 annual cohorts.
- **Primary (audit fix):** REML random-effects meta-regression of the segmented trend on the covariate-adjusted logit year effects, using their full sampling covariance plus a year-shock variance τ². Inference uses t with 6 df.
- **Secondary:**
  - the topic100-clustered paper-level Wald test of the first version;
  - a quasi-binomial year-level dispersion correction.

**Primary result (U, n = 43,482).**

| Term | Paper level (topic100-clustered) | Year level, random effects (t, 6 df) |
|---|---|---|
| Pre-trend | OR 1.125/yr; LPM +1.35 pp/yr | OR 1.112/yr |
| Level shift at 2024 | OR 0.975 | |
| **Slope change, logit** | OR 1.098 [1.044, 1.154]; one-sided p = 1.3e-4 | **OR 1.096 [0.990, 1.214]; p = 0.035**; τ = 0.044 (logit) |
| Slope change, LPM | +2.97 pp/yr [2.13, 3.81] | +2.82 pp/yr [1.26, 4.38]; p = 0.002 |
| Quasi-binomial (φ = 1.86 on 6 df) | | OR CI [1.008, 1.195]; p = 0.018 |

**Year-level inference by population** (random effects, t):

| Population | Slope-change OR [95% CI] | p (one-sided) | LPM pp/yr [95% CI] |
|---|---|---|---|
| U | 1.096 [0.990, 1.214] | 0.035 | +2.82 [1.26, 4.38] |
| NA pool (camera-ready-free) | 1.121 [1.019, 1.232] | 0.013 | +3.34 [1.71, 4.97] |
| non-LLM subset | 1.108 [0.986, 1.245] | 0.038 | +2.93 [1.18, 4.68] |
| U excluding 2026 (5 df) | 1.046 [0.807, 1.355] | 0.34 | +1.93 [−1.31, 5.17] |

**T1.1 (selected rows; paper-level, topic100-clustered).** Slope-change OR per year, with 95% CI.

| Specification | n | NAME primary | strict | loose | compound |
|---|---|---|---|---|---|
| U, topic100 FE | 43,482 | 1.098 [1.044, 1.154] | 1.098 [1.043, 1.155] | 1.112 [1.060, 1.166] | 1.231 [1.176, 1.289] |
| NA pool | 30,322 | 1.128 [1.061, 1.199] | 1.130 [1.060, 1.204] | 1.132 [1.068, 1.200] | 1.241 [1.177, 1.309] |
| non-LLM subset | 30,269 | 1.116 [1.055, 1.180] | 1.118 [1.054, 1.186] | 1.138 [1.079, 1.199] | 1.233 [1.170, 1.299] |
| NA × non-LLM | 21,199 | 1.145 [1.065, 1.230] | | | |
| U, bge topic100 FE | 43,482 | 1.088 [1.035, 1.144] | | | |
| U, controls, no topic FE | 43,482 | 1.138 [1.075, 1.205] | | | |
| U, no controls | 43,482 | 1.188 [1.115, 1.266] | | | |
| 2018+ | 43,098 | 1.107 [1.055, 1.161] | | | |
| without 2019 | 42,234 | 1.095 [1.041, 1.151] | | | |
| **excluding 2026** (2017–25) | 28,070 | **1.052 [0.964, 1.147]**; LPM +2.0 pp/yr [0.4, 3.7] | | | |
| ACC pool (2017–26) | 13,048 | 1.042 [0.964, 1.127] | | | |
| REJ pool (2017–26) | 19,485 | 1.115 [1.031, 1.206] | | | |
| WD pool (2018–26) | 9,954 | 1.107 [0.992, 1.235] | | | |

The pool rows use D1's window (accepted and rejected 2017–26; withdrawn 2018–26, as there are no 2017 withdrawals in the frame). D4's H4a refits the three pools on 2018–26 (ACC 1.053, REJ 1.119, WD 1.107; Table 1, Fig. 5).

(The pool label is written `NApool` in the CSV files so that default CSV readers do not turn it into a missing value.)

**Pilot discrepancy.** The pilot's "slope change OR 1.28/yr" was estimated for **colon titles** (`has_colon`, close to our *compound*), 2018–26, with an LLM-topic control and no topic FE. It was not estimated for NAME.
- Our compound estimate with topic100 FE is 1.231.
- For NAME the log-odds slope change is about two fifths of the pilot's: log 1.098 / log 1.28 = 0.38.

**Year-dummy variant.** Deviations from the extrapolated 2017–23 logit trend, on U (paper level):

| Year | Deviation (pp) | OR |
|---|---|---|
| 2024 | +1.5 [−0.7, +3.8] | 1.09 [0.96, 1.24] |
| 2025 | +2.7 [−0.5, +5.9] | 1.15 [0.98, 1.35] |
| 2026 | **+5.5 [+1.5, +9.5]** | 1.30 [1.08, 1.56] |

- The NA pool and the non-LLM subset show the same pattern (`its_year_deviation.csv`).
- The rise in 2024–25 is largely what a logit-linear pre-trend already implies. The excess is concentrated in 2026, the year of the new desk regime and the reported separate cohort.

**Break dating, and break vs smooth acceleration.**
- **Placebo breaks** (pre-2024 data, 2017–23): OR 0.854 [0.685, 1.064] at 2020, 0.910 [0.787, 1.051] at 2021, and 0.925 [0.781, 1.096] at 2022. All are null and all are below the 2024 estimate. NA and non-LLM give the same picture.
- **Randomization over break years** 2019–2025: 2024 has the largest slope-change z (3.66; 2025: 2.87; 2023: 2.12). The randomization p is 1/7 = 0.143, the smallest attainable with 7 candidates, so this test can never reject at 0.05.
- **sup-LR scan** 2020–2025 (segmented level+slope model vs the linear-trend model; LR values; `fig_its_scan` panel b):

  | Break year | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|
  | LR, level+slope (pre-registered) | 2.7 | 18.0 | 11.6 | **18.4** | 16.4 | 15.4 |
  | LR, kink only (post hoc) | 0.0 | 0.4 | 5.9 | 10.0 | **16.1** | 14.8 |

  - The pre-registered scan selects **2023**. 2021 gets a high LR because of a level dip (NAME 15.7% → 15.0% in 2021).
- **Smooth vs dated break** (GLS on the adjusted logit year effects; generalised residual Q, lower is better; `results.json → H1a.year_level_all`):

  | Model (parameters) | Q, U (τ from REML) | Q, U (τ = 0) | Q, NA pool (τ from REML) |
  |---|---|---|---|
  | linear (2) | 12.5 | 28.8 | 14.4 |
  | quadratic (3) | 8.9 | 14.1 | 5.9 |
  | kink at 2024 (3) | 6.5 | 10.8 | 4.5 |
  | segmented at 2023 (4) | **6.0** | **10.3** | **4.3** |
  | segmented at 2024 (4) | 6.5 | 10.6 | 4.5 |
  | quadratic + post·t (4); z of post·t | 5.4; z = 1.87 | 10.1; z = 1.98 | 4.5; z = 1.17 |

  - Acceleration relative to a linear logit trend is clear in both pools.
  - A 2023 break, a 2024 break, a 2024 kink and a convex (quadratic) trend fit about equally well.
  - The 2024 slope term adds little once curvature is allowed.

**Verdict H1a: partially supported, not falsified.**
- Met:
  - The NA-pool CI excludes 1, at paper level and at year level.
  - No placebo is as large as the 2024 estimate.
  - The pattern holds under all four NAME definitions.
- Not met:
  - The pre-registered sup-LR scan picks 2023.
  - On U the year-level CI includes 1 (p = 0.035; Holm-adjusted 0.071). The non-LLM year-level CI also includes 1.
  - Without 2026 the logit slope change is null at both levels.
- The appropriate wording is "the NAME trend became convex (accelerated) from about 2022–24, most visibly in 2026". The design does not identify a dated 2024 break, and the timing cannot be tied to ChatGPT.

## 2. H1b: how much of the rise does content explain? (F1.1, T1.2)

**Method.**
- Each representation is fitted as an L2 logit, with C chosen by 5-fold CV (log loss) inside each training window.
- Intercepts are recalibrated so that the cross-fitted (out-of-fold) predictions for the last training year match its observed share.
- **Audit fix (D1-C1).** The test rows are now scored by the same five CV fold models whose OOF scores set the intercept: p̂ = mean over folds of expit(s_k + c). The first version added c to a separately fitted full-data model. That model's scores are more dispersed at the same C, so every content step was inflated by a model-mismatch term.
- Content share:
  - fixed window = (p̂_2026 − obs_2023)/(obs_2026 − obs_2023);
  - rolling = Σ content steps 2024–26 / Σ observed steps 2024–26.
- CIs:
  - **conditional:** paper bootstrap stratified by year, 2,000 replicates; models held fixed; recalibration recomputed;
  - **refit:** B = 300 (rolling R1) or B = 200 (fixed R1); every fold model re-estimated on the resampled papers.

**T1.2 (`T1_2_representations.csv`).** Content share of the 2023→2026 rise, with mean out-of-sample AUC and calibration slope.

| Rep. | Role | Fixed 2021–23 → 2026: share [95% CI] | AUC | Cal. slope | Rolling 2024–26: share [95% CI] | AUC | Cal. slope |
|---|---|---|---|---|---|---|---|
| R1 masked TF-IDF (primary) | masked | **0.389** [0.349, 0.434]; refit [0.299, 0.439] | 0.744 | 1.39 | **0.574** [0.531, 0.621]; refit [0.505, 0.636] | 0.712 | 1.41 |
| R3 bge, masked abstract | masked | **0.492** [0.444, 0.544] | 0.745 | 1.07 | **0.577** [0.534, 0.627] | 0.715 | 0.99 |
| R5 R1 minus rhetorical moves | masked | 0.381 [0.341, 0.425] | 0.743 | 1.39 | 0.565 [0.522, 0.613] | 0.711 | 1.41 |
| R1yfe R1 + training-year FE | masked, sensitivity | 0.377 [0.339, 0.420] | 0.744 | 1.41 | 0.544 [0.504, 0.590] | 0.712 | 1.42 |
| R3yfe R3 + training-year FE | masked, sensitivity | 0.479 [0.434, 0.532] | 0.744 | 1.07 | 0.551 [0.509, 0.599] | 0.715 | 0.99 |
| R5yfe R5 + training-year FE | masked, sensitivity | 0.368 [0.331, 0.409] | 0.743 | 1.41 | 0.533 [0.491, 0.576] | 0.711 | 1.41 |
| R2 keywords (papers with keywords) | lower | −0.041 [−0.056, −0.027] | 0.567 | 0.62 | 0.117 [0.095, 0.138] | 0.590 | 1.56 |
| R6 topic100 + llm_topic | coarse | 0.174 [0.153, 0.197] | 0.640 | 1.15 | 0.330 [0.301, 0.361] | 0.622 | 1.11 |
| R6b bge topic100 | coarse | 0.179 [0.158, 0.202] | 0.643 | 1.15 | 0.334 [0.306, 0.368] | 0.623 | 1.42 |
| R4 bge, unmasked (leaky) | upper | 0.551 [0.501, 0.606] | 0.759 | 1.10 | 0.643 [0.597, 0.697] | 0.734 | 1.11 |
| R1u unmasked TF-IDF (V4) | diagnostic | 0.363 [0.324, 0.406] | 0.748 | 1.42 | 0.554 [0.514, 0.601] | 0.714 | 1.43 |
| R1n R1 minus naming tokens | diagnostic | 0.390 [0.350, 0.432] | 0.743 | 1.39 | 0.571 [0.530, 0.618] | 0.710 | 1.39 |
| R1 at pilot C = 0.5 | sensitivity | 0.217 [0.195, 0.240] | 0.746 | 2.60 | 0.424 [0.392, 0.458] | 0.715 | 3.07 |

**Intercept+slope recalibration** (sensitivity, point estimates). Logistic recalibration on the calibration year's OOF scores. The recalibration slope is about 1.2 for R1/R5 and 1.0 for R3. Shares under it:
- R1 fixed 0.462, rolling **0.652**;
- R5 fixed 0.450, rolling **0.641**;
- R3 fixed 0.494, rolling 0.579.

**First-version values** (full-data model with the mismatched intercept): R1 0.430 / 0.620, R3 0.509 / 0.595, R5 0.420 / 0.611 (fixed / rolling).

**Per-year fixed-window shares.**

| Year | R1 | R3 |
|---|---|---|
| 2024 | 0.36 [0.27, 0.50] | 0.50 |
| 2025 | 0.40 [0.35, 0.47] | 0.58 |
| 2026 | 0.39 [0.35, 0.43] | 0.49 |

**Verdict H1b: partially supported. Not falsified, but the prediction fails.** The pre-registered rule is "fails if any name-masked representation explains ≥ 60%".
- After the calibration fix, no pre-registered masked share reaches 0.60 (maximum: R3 rolling 0.577).
- The first version's "falsified" verdict rested on the calibration mismatch (R1 0.620, R5 0.611). It no longer holds.
- The prediction ("[0.20, 0.50] for every masked representation") also fails:
  - the rolling shares (0.57–0.58) exceed 0.50;
  - R3 fixed is at 0.49;
  - 0.60 lies inside every rolling CI (P(share ≥ 0.60): 0.07–0.18).
- The share depends on the specification:
  - Training-year fixed effects, which stop tokens that trend with NAME inside the window from carrying the time trend (D1-C2), lower it to 0.37 (fixed) and 0.53–0.55 (rolling).
  - Intercept+slope recalibration, which the out-of-sample calibration slopes of 1.2–1.4 for R1/R5 favour, raises R1/R5 rolling to 0.64–0.65.
  - Stronger regularisation (C = 0.5) lowers it to 0.22 (fixed) and 0.42 (rolling).
- **Range across reasonable name-masked specifications: about 0.37–0.65.** The fixed window sits at the low end and the rolling one-step design at the high end. Neither "content is a minority" nor "content ≥ 0.60" is robust.
- Calibration slopes above 1 for R1/R5 mean the CV-regularised scores are under-dispersed, not over-fitted. If anything, content shifts are under-predicted at the chosen C. R3, which is well calibrated (slope 0.99–1.07), is insensitive to slope recalibration (0.58).
- What the content signal is: the fixed-window attribution (audit check ID-5) is dominated by LLM-era topic words (reasoning, generation, language, benchmark, evaluation). Announcement and promotional tokens contribute about a fifth. "Content" therefore includes the move to LLM topics, which is also where the tool operates.
- The non-masked bracket runs from −0.04 to 0.33 (keywords and coarse topics, fixed and rolling) to 0.55–0.64 (leaky unmasked bge).
- The pilot's 29% (fixed) and 42% (rolling) are approximately matched only at the pilot's hand-set C = 0.5 (0.22 and 0.42).

**Figure F1.1** (`fig_F1_1_counterfactual.{pdf,png}`). Observed NAME share against:
- the R1 fixed-window counterfactual (train 2021–23);
- the R1 rolling cumulative counterfactual (2023 + cumulative one-step content steps: 22.6 / 27.8 / 31.9% in 2024 / 25 / 26);
- the placebo window (train 2018–20).

Shaded bands are ranges across representations, not confidence intervals. Inset: NA pool, R1.

## 3. H1c: did content-unexplained drift accelerate? (F1.2)

**Method.**
- Rolling one-step-ahead R1: train on y−3..y−1, recalibrate to obs_{y−1} on cross-fitted scores, predict y with the same fold models.
- Then u_y = obs_y − p̂_y = (obs_y − obs_{y−1}) − cs_y, where cs_y is the content step.
- **The statistic telescopes** (audit ID-3):
  diff = (obs_2026 − obs_2023 − Σcs_2024–26)/3 − (obs_2023 − obs_2018 − Σcs_2019–23)/5.
  It is an endpoint contrast. A year-level shock to the 2023 cohort enters with weight −8/15, to 2026 with +1/3 and to 2018 with +1/5.
- The pre-registered paper bootstrap resamples papers within year and holds those shocks fixed.

**Annual decomposition** (pp; R1; `cf_rolling_steps.csv`, `fig_F1_2_steps`):

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| Observed step | +3.1 | +2.6 | −0.7 | +3.3 | +2.0 | +6.3 | +6.5 | +7.3 |
| Content step | −0.2 | +0.7 | +0.3 | +0.6 | +1.3 | +2.3 | +5.2 | +4.1 |
| Unexplained u | +3.4 | +1.8 | −1.0 | +2.7 | +0.6 | +4.0 | +1.3 | +3.3 |

**Decomposition of the acceleration in annual gains.**
- The mean observed step rose from 2.06 to 6.72 pp/yr (+4.66).
- The mean content step rose from 0.54 to 3.85 pp/yr (+3.31, 71%).
- Mean u rose from 1.51 to 2.87 pp/yr (+1.35, 29%).

**Inference for the difference** (+1.35 pp; ratio 1.89):

| Inference | Diff 95% CI (pp) | p (diff ≤ 0) | Ratio 95% CI |
|---|---|---|---|
| Conditional paper bootstrap (models fixed) | [0.56, 2.15] | 0.0015 | [1.29, 3.05] |
| Refit paper bootstrap (B = 300) | [0.47, 2.23] | 0.003 | [1.24, 2.96] |
| **Two-stage: refit + year shocks, τ on the logit scale (primary)** | **[0.03, 2.71]** | **0.022** | [1.02, 3.55] |
| Two-stage, τ on the LPM scale (0.64 pp) | [0.16, 2.54] | 0.013 | |
| Year-label permutation (56 arrangements) / Welch t | | 0.14 / 0.14 | |

- In the two-stage inference, year shocks add an SD of 0.53 pp, against 0.44 pp from refitting. P(ratio < 1.5) = 0.23 and P(ratio < 1.2) = 0.07.
- The permutation test treats the u_y as exchangeable. The telescoping structure makes them negatively autocorrelated, so it is conservative here.
- Two-stage, excluding 2026 (post = 2024–25): +1.15 pp [−0.63, 2.96], p = 0.10.
- Two-stage, without 2019 (pre = 2020–23): +1.81 pp [0.37, 3.27].

**Replications.** Conditional CI, and the year-robust CI = conditional SE plus year shocks (normal approximation; each population's own τ):

| Variant | Diff (pp) | Conditional CI | Year-robust CI | Ratio |
|---|---|---|---|---|
| R1 (primary) | +1.35 | [0.56, 2.15] | [0.04, 2.67] | 1.89 |
| R3 masked bge | +1.29 | [0.43, 2.10] | [−0.03, 2.61] | 1.83 |
| R5 | +1.40 | [0.54, 2.21] | [0.08, 2.73] | 1.92 |
| R1yfe / R3yfe / R5yfe | +1.50 / +1.41 / +1.57 | [0.68, 2.28] / [0.59, 2.20] / [0.77, 2.41] | [0.19, 2.82] / [0.09, 2.73] / [0.25, 2.89] | 1.96 / 1.88 / 2.00 |
| R1, intercept+slope recalibration | +0.92 | | | 1.65 |
| **NA pool** | +1.14 | [0.14, 2.15] | **[−0.10, 2.39]** | 1.64 |
| **non-LLM subset** | +0.55 | [−0.38, 1.45] | **[−0.90, 1.99]** | 1.34 |
| strict NAME | +1.14 | [0.34, 1.93] | [−0.15, 2.43] | 1.72 |
| loose NAME | +1.49 | [0.64, 2.35] | [0.11, 2.87] | 2.18 |
| compound | +3.94 | [2.95, 4.94] | [2.32, 5.56] | 3.73 |
| R6 (coarse) | +2.51 | [1.69, 3.33] | [1.18, 3.83] | 2.25 |
| R4 (leaky) | +1.01 | [0.21, 1.86] | [−0.30, 2.33] | 1.73 |
| without 2019 (pre = 2020–23) | +1.81 | [0.89, 2.72] | two-stage [0.37, 3.27] | 2.73 |
| excluding 2026 (post = 2024–25) | +1.15 | [0.15, 2.19] | two-stage [−0.63, 2.96] | 1.76 |

**Other checks.**
- **Not regression to the mean** from a low 2023 cohort: obs_2023 = 20.30%, against a segmented-model fit of 20.36% (audit ID-3).
- **New topics.** Content models under-predict NAME in fast-growing clusters (§6).
  - Restricting u to papers outside fast-growing clusters gives 1.34 → 2.52 pp/yr (ratio 1.88; exploratory).
  - Inside fast-growing clusters, u is much larger in both periods: 5.2 → 6.6 pp/yr.
- **Cumulative 3-year comparison.**
  - Placebo window (train 2018–20, anchored at 2020): unexplained by 2023 = +3.4 pp [1.3, 5.5]; content share of the 2020→23 rise 0.26 [0.16, 0.50].
  - Fixed window (train 2021–23): unexplained by 2026 = +12.3 pp [10.6, 14.0].
  - Pre-2024 unexplained drift exists, which is why H1c is a difference. No CI is computed for the ratio of the two quantities.

**Verdict H1c: not established at the year level.**
- The pre-registered criteria (ratio ≥ 1.5 and a paper-bootstrap CI that excludes 0) are met. Under paper-level inference this would read "supported".
- The paper bootstrap holds year shocks fixed, and the estimand is an endpoint contrast of three annual cohorts.
- With year shocks added:
  - the R1 CI barely excludes 0 ([0.03, 2.71] pp; raw p = 0.022), but the Holm-adjusted p is 0.067;
  - the falsification rule is met in the camera-ready-free NA pool and in the non-LLM subset;
  - the CI also includes 0 for R3, strict NAME and the excluding-2026 contrast.
- The positive sign is robust to every content specification (diff +0.9 to +1.6 pp). Its size and significance are not.

## 4. H1d: composition (declared keys) (F1.3; `dfl_table.csv`, `shapley_table.csv`)

**New-key share (audit fix D1-C6).** The share of a paper's declared profile keys not seen on any submission in the two preceding years.
- The first version counted "no prior submission since the export began". Profile keys only start in 2021, so that lookback grew from 2 years (2023) to 5 years (2026).
- 2021 has no profile-key lookback: its value is missing, and it gets its own cell in the Shapley composition model. 2022's lookback effectively covers 2021 only.
- Keys are declared profile keys, not persons. Aliasing inflates new-key counts.

**Composition change, 2023 → 2026.**

| | 2023 | 2026 |
|---|---|---|
| Mean declared authors | 4.56 | 5.67 |
| Mean new-key share, fixed 2-year lookback | 0.594 | 0.558 |
| Mean new-key share, growing lookback (first version) | 0.594 | 0.525 |
| llm_topic share | 0.106 | 0.482 |

**DFL composition share of the 2023→y rise.** y-year papers are reweighted to the 2023 cell distribution; bootstrap 2,000.

| Cells | 2024 | 2025 | 2026 |
|---|---|---|---|
| team size (6 bins) | 0.134 | 0.198 | 0.175 [0.153, 0.199] |
| size × llm_topic | 0.287 | 0.320 | 0.267 [0.232, 0.307] |
| size × new keys | 0.127 | 0.186 | 0.165 [0.143, 0.191] |
| **size × new keys × llm_topic (primary)** | **0.287 [0.202, 0.410]** | **0.316 [0.259, 0.386]** | **0.261 [0.223, 0.301]** |
| + experience bins (max prior subs) | 0.285 | 0.336 | 0.251 [0.208, 0.297] |
| primary, growing-lookback new keys (first version) | 0.251 | 0.297 | 0.246 [0.209, 0.286] |
| primary, NA pool | 0.239 | 0.333 | 0.236 [0.193, 0.283] |
| non-LLM subset (size × new keys) | 0.046 | 0.129 | 0.105 [0.078, 0.134] |

- The pilot gave 18% (size) and 26% (size × LLM topic); both reproduce (0.175, 0.267).
- Valued at 2023 cell rates (Oaxaca), the primary composition share is lower: 0.220 / 0.211 / 0.189 [0.089, 0.300] for 2024 / 25 / 26.
- Most of the "composition" effect is the llm_topic margin, which overlaps content. Team size and new-key share alone explain 0.13–0.19.

**Shapley over content (R1) and composition (cells).** Fixed window, fold-ensemble prediction; 2026 shares.

| Ordering | Content | Composition |
|---|---|---|
| Content first | 0.389 | then 0.036 |
| Composition first | then 0.287 | 0.139 |
| **Shapley** | **0.338** (conditional [0.305, 0.377]; refit [0.255, 0.394]) | **0.088** (conditional [0.077, 0.101]; refit [0.039, 0.154]) |

- **Residual (unexplained by measured content and composition; it includes new-topic naming that bag-of-words content misses, undetected tool use and unmeasured composition):** 0.574 (conditional [0.525, 0.616]; refit [0.481, 0.669]).
- 2024: content 0.30, composition 0.09, residual 0.60. 2025: 0.34 / 0.10 / 0.56.
- **Why DFL (0.26) and Shapley (0.09) differ.** Most of the gap comes from the estimator, not from "accounting for content".
  - DFL uses the target year's own cell rates.
  - The Shapley composition model values cells at logit rates fitted on 2021–23. With composition entered first it already gives 0.139, and that falls to 0.036 after content.

**Verdict H1d: partially supported.** The prediction is "measured team-size × new-key × llm_topic composition explains ≤ 0.30".
- It holds for 2024 (0.287) and 2026 (0.261).
- It does not hold for 2025 (0.316 [0.259, 0.386]).
- Every year is far from the 0.50 falsification threshold.
- The Shapley composition share is about 0.09 in every year.
- This tests measured, key-based composition only, not "people" in a broader sense.

## 5. H1e: the tool (F1.3, T1.3; `tool_delta_models.csv`, `T1_3_tool_bound.csv`)

**Fingerprint.** F (D1 variant, F_d1) = F24 with ≥ 2 RARE21 words ∪ F26 ∪ title typography. The broader F_any (D3's primary and VALIDATION V3's F) = F24 with ≥ 1 RARE21 word ∪ F26 ∪ title typography; the two differ only in the F24 threshold.
- Share of papers with F: 2.5% (2023), 7.1% (2024), 5.2% (2025), 19.2% (2026). The 2023 value is the pre-ChatGPT false-positive level.

**(i) NAME rise among F = 0 papers relative to all papers.**

| Population / fingerprint | 2024 | 2025 | 2026 |
|---|---|---|---|
| F (D1 variant) | 1.00 [0.94, 1.06] | 1.00 [0.97, 1.02] | **0.98 [0.96, 1.00]** |
| NA pool | 0.99 | 0.99 | 0.98 [0.95, 1.00] |
| broader F_any (F24 ≥ 1 RARE21 word ∪ F26 ∪ title typography) | 0.85 [0.73, 0.96] | 0.93 [0.88, 0.97] | 0.95 [0.92, 0.98] |

- NAME share 2023 → 2026: 20.3% → 40.1% among F = 0 papers, against 20.6% → 42.0% among F = 1 papers.
- **Power.** Criterion (i) has little power by construction. With 19% of 2026 papers flagged, the ratio falls below 0.85 only if F = 1 papers' NAME share exceeds F = 0 papers' by ≥ 18 pp. It falls below 0.70 only for a gap of ≥ 44 pp (the maximum possible is 60 pp). With a recall of about 45% at A = 0.39, undetected drafted papers also sit in F = 0.

**(ii) δ.** LPM `NAME ~ F + log authors | topic100×year`, 2024–26, clustered by topic100.

| Specification | n | δ (pp) | 95% CI |
|---|---|---|---|
| **Primary** | 30,130 | **+1.62** | [+0.02, +3.22] |
| + area×year FE | 30,130 | +1.46 | [−0.08, +2.99] |
| + llm_topic | 30,130 | +1.54 | [−0.05, +3.13] |
| bge topic×year | 30,130 | +1.49 | [−0.21, +3.18] |
| NA pool | 21,273 | +2.02 | [+0.01, +4.03] |
| non-LLM subset | 18,005 | −0.18 | [−2.67, +2.31] |
| excluding 2026 (2024–25) | 14,718 | −0.67 | [−3.57, +2.23] |
| 2024 only | 5,765 | −0.42 | [−4.95, +4.12] |
| 2025 only | 8,953 | −0.88 | [−5.10, +3.34] |
| **2026 only** | 15,412 | **+2.42** | [+0.47, +4.37] |
| component: F24 (≥ 2 words) only | 30,130 | +3.49 | [−0.39, +7.36] |
| component: F26 only | 30,130 | +1.30 | [−0.48, +3.09] |
| component: title typography only (0.7% of papers) | 30,130 | **+10.63** | [+3.74, +17.53] |
| title typography, given an intra-word dash in the title | 17,356 | +6.01 | [−0.99, +13.01] |
| F_any (F24 ≥ 1 word ∪ F26 ∪ title typography) | 30,130 | +2.54 | [+1.27, +3.81] |
| pre-period placebo, 2021–23: F_d1 / F_any | 8,881 | +0.45 / −2.62 | [−3.98, +4.88] / [−5.82, +0.58] |
| **DiD F × post, 2021–26 (selection-corrected): F_d1** | 39,011 | +1.57 | [−2.98, +6.12] |
| **DiD F × post, 2021–26: F_any** | 39,011 | **+5.55** | [+2.00, +9.09] |

- Logit adjOR: 1.08 [1.00, 1.17]; 1.13 [1.07, 1.21] for F_any. The pilot colon adjOR was 1.24.
- The pre-registered criterion δ ≤ +5 pp holds for the pre-registered fingerprint (upper CI 3.2 pp).
- It does not hold for the title-level typography marker. Raw NAME share among typography-marked 2024–26 titles is 51.6% (n = 215), against 35.5% otherwise.
- It also does not hold for the selection-corrected F_any DiD. Pre-ChatGPT authors with "LLM-like" vocabulary name less (−2.6 pp), which biases the cross-sectional δ downward.
- δ is positive only in 2026.

**(iii) Tool share.**
- **As pre-registered:** δ·A/ΔNAME.
- **Audit fix (D1-C5):** this formula treats δ as the NAME uplift τ of drafted papers. With imperfect recall, F = 0 contains undetected drafted papers and F = 1 contains false positives, so δ = τ·(P(L|F=1) − P(L|F=0)) = τ·k.
- **Corrected:** τ = δ/k. Recall is implied by A, the 2026 F share (19.2%) and the 2023 false-positive rate (2.5%), and the corrected share is τ·A/ΔNAME.
- **Year-matched:** the 2026-only δ with the 2026 A. A_max = 0.39 is the PLAN's held-out greedy abstract bound for 2026, taken as given.

| A_max | 0.24 | **0.39** | 0.50 | 0.75 | 1.00 |
|---|---|---|---|---|---|
| implied recall / k | 0.72 / 0.82 | 0.45 / 0.66 | 0.36 / 0.54 | 0.25 / 0.27 | not identified |
| uncorrected, pooled δ (pre-registered formula) | 1.9% [0.0, 3.8] | 3.1% [0.0, 6.2] | 4.0% [0.1, 8.0] | 6.0% [0.1, 12.0] | 8.0% [0.1, 16.0] |
| corrected, pooled δ | 2.4% [0.0, 4.7] | 4.8% [0.1, 9.5] | 7.5% [0.1, 14.8] | 22.4% [0.3, 44.5] | not identified |
| **corrected, 2026 δ (primary)** | 3.5% [0.7, 6.4] | **7.1% [1.4, 12.9]** | 11.1% [2.2, 20.1] | 33.4% [6.5, 60.4] | not identified |

- At A = 1 every paper is drafted and the F contrast cannot identify τ. The uncorrected A = 1 row is not a maximum.
- **Sensitivities at A = 0.39** (corrected, each marker with its own false-positive rate):
  - F_any, 2026: 7.7% [2.1, 13.2];
  - F_d1 DiD: 4.6% [−8.8, 18.0];
  - **F_any DiD: 16.3% [5.9, 26.7]**;
  - title typography: 33.3% [11.7, 54.8];
  - title typography given an intra-word dash: 18.8% [−3.1, 40.7].
- The typography marker flags 1.4% of 2026 titles. It is mechanically tied to hyphenated titles, and coined names are often hyphenated, so the nondifferential-misclassification correction is not valid for it: at A ≥ 0.75 the corrected share exceeds 1. Uncorrected typography shares: 20.6% [7.2, 33.9]; given a dash, 11.6% [−1.9, 25.2].
- The contribution of detectable fingerprints alone (δ × ΔP(F) / ΔNAME) is 1.3%.
- **Assumptions behind every number in (iii):**
  - the linear δ·A model;
  - F depends on NAME only through L (nondifferential misclassification);
  - the same NAME uplift in detected and undetected drafted papers;
  - no spillover to undrafted papers;
  - the 2023 F share is all false positives.

None of these is tested, except the last one in part (integration pass 2, `outputs/audit/integration/check_fpr_baseline.py`):
- D3 and VALIDATION V3 take the false-positive rate from 2021–22 instead (F_any 5.9%). For F_d1 the 2021–22 share is 3.2%, above the 2023 share of 2.5%. With the 2021–22 rate the corrected 2026 tool share at A = 0.39 is **7.4% [1.4, 13.4]** (recall 0.44), against 7.1% [1.4, 12.9] with the 2023 rate.
- ICLR 2023 accepted abstracts are post-ChatGPT camera-ready text (D4, H4c). Their F_d1 share is 3.1% (n = 1,256), against 2.2% for the other 2023 papers. Using only the other 2023 papers as the false-positive baseline gives 7.0% [1.4, 12.7]. The choice of baseline moves the tool share by less than half a point.

**Verdict H1e: supported as pre-registered, for the abstract fingerprint, but not robust as a bound.**
- For the pre-registered fingerprint all three criteria are met after the correction: F0 ratio 0.98 ≥ 0.85; δ = +1.6 ≤ +5 pp; corrected tool share 0.07 < 0.25.
- (i) has little power.
- With other markers the point estimates at A = 0.39 range from 5% to 33%. Upper CIs reach 0.27 (abstract markers) and 0.55 (title typography).
- "The tool is not the main driver" survives as a point-estimate statement for the pre-registered fingerprint. "Small and bounded from above" does not.

**Positive control (D3; integration pass).** The PLAN pre-registers D3's slot result to be reported beside H1e as a positive control. D3 has now been run and audited (`outputs/d3_register/`, H3a and H3d; `results.json → H1e.positive_control_D3`).
- **The title-level design detects an LLM-era lexical shift.** LLM-favoured openers in meaning-fixed slots rose from 2024: pooled post OR 2.18 [1.41, 3.38] (H3a), with control pairs flat at the 2024 break (0.87 [0.64, 1.18]).
- **With D1's own fingerprint the control is not significant.** H3d regresses the LLM slot variant on the abstract fingerprint, 2024–26, within topic100 × year (1,508 slot rows):
  - F_d1 (D1's fingerprint: F24 ≥ 2 words ∪ F26 ∪ title typography; 179 F = 1 rows): OR_slot **1.29 [0.92, 1.81]**, one-sided p = 0.072. Against the population NAME comparator (OR 1.08 [1.01, 1.16]) the ratio is 1.19 [0.84, 1.65].
  - F_any (D3's primary: F24 with ≥ 1 RARE21 word ∪ F26 ∪ title typography, i.e. F_d1 with the F24 threshold lowered from 2 words to 1; 381 F = 1 rows): OR_slot **1.42 [1.14, 1.79]**, against a population NAME OR of 1.14 [1.08, 1.21]; ratio 1.24 [0.99, 1.57]. The contrast with the F_d1 row therefore isolates the F24 threshold.
- **Consequence for H1e.** The pre-registered criteria are met for F_d1, but the fingerprint that drives D1's tool share does not detect the LLM-favoured slot words at conventional significance. The D1 tool estimate (7.1% [1.4, 12.9] at A = 0.39) is therefore **not validated by a positive control on its own fingerprint**. The broader F_any does pass the control, and it gives a larger tool share (7.7% [2.1, 13.2] cross-sectionally, 16.3% [5.9, 26.7] by DiD; §5 (iii)).
- The positive control speaks to the fingerprint's sensitivity for lexical LLM traces in titles. It does not test the linear δ·A model or the misclassification assumptions listed above.

## 6. Identification and robustness

**New-topic placebo (pre-registered; fails).**
- Rule: calibration-in-the-large for papers in topic100 clusters whose share grew ≥ 3× relative to the training window. Pass if |obs − pred| in fast-growing clusters ≤ |obs − pred| elsewhere + 2 pp.
- **Audit fix (D1-C7):** residuals are averaged within each test year. The absolute values are averaged over test years with weights equal to the number of fast-cluster papers, so the "elsewhere" baseline is year-matched. The bootstrap recomputes the recalibration.

| Window (R1) | Fast-growing: pooled signed residual (n) | Elsewhere | Year-avg. \|res\| fast vs elsewhere | Gap difference [95% CI] |
|---|---|---|---|---|
| Placebo 2018–20 → 2021–23 | +6.0 pp (1,154) | +1.3 pp | 6.0 vs 2.4 | 3.6 pp [1.0, 6.2] |
| Same, bge clusters | +7.8 pp (720) | +1.4 pp | 7.8 vs 2.4 | 5.4 pp [2.3, 8.6] |
| Rolling, 2019–23 | +5.6 pp (495) | +1.1 pp | 5.6 vs 1.7 | 3.9 pp [1.4, 7.7] |
| Rolling, 2019–23, bge clusters | +3.8 pp (394) | +1.2 pp | 6.9 vs 2.0 | 4.9 pp [1.7, 9.0] |
| Rolling, 2024–26 | +6.3 pp (2,427) | +2.5 pp | 6.3 vs 2.4 | 3.9 pp [2.0, 5.8] |
| Fixed 2021–23 → 2024–26 | +15.8 pp (9,219) | +6.5 pp | 15.8 vs 7.7 | 8.0 pp [6.8, 9.2] |

- In the bge rolling-pre row the 2023 fast-cluster residual is negative (−7.0 pp). The per-year absolute rule prevents it from cancelling the positive years.
- R3 fails in the same way, with gap differences of 3.1–6.7 pp.
- **All fail.** Emerging topics adopt NAME titles faster than their (masked) abstract content predicts, in the pre-LLM period too (diffusion-era 2021–23).
- Two readings remain open:
  - naming is a property of new artefact-producing topics that bag-of-words content does not capture, in which case content shares are understated;
  - the fashion spreads fastest in hot topics.
- The fixed-window content share is therefore *not* robust to the extrapolation critique, especially for 2024–26, when about 31% of papers sit in fast-growing clusters. This failure qualifies both H1b and H1c.

**V4: name-masking leakage.**
- The R1 lead survives in 22 of 12,928 NAME abstracts of 2018–26 (0.17%), against the 0% target; all 22 are from 2023–26. The same denominator is used in VALIDATION V4 and SUMMARY. (`results.json` → `v4.name_papers` = 12,962 counts 2017–26 on the same universe; the 34 NAME papers of 2017, which have no R3 mask, contain no survivor.)
  - All are project-page URLs with a digit suffix (e.g. `resgrad1.github.io`). R1 keeps letter runs, so "resgrad1" becomes "resgrad".
  - This is too few to move any share.
- Masked-vs-unmasked AUC gap:
  - TF-IDF (R1u − R1): +0.004 fixed, +0.003 rolling, −0.002 placebo.
  - bge (R4 − R3): +0.014 fixed, +0.019 rolling, +0.025 placebo.
  - Unmasked bge leaks somewhat more than unmasked TF-IDF. The R3 → R4 content share rises from 0.49 to 0.55 (fixed) and from 0.58 to 0.64 (rolling).
- Top-200 R1 features (`v4_top200_R1_features.csv`):
  - 2% contain rare tokens (zipf < 2): textbf, textsc, "embeddings", "regularizer". No name fragments.
  - The top features include naming-announcement words: "we introduce" (rank 8), "named" (rank 19), "called" (rank 28), and LaTeX emphasis.
  - Removing 12 such tokens (exploratory R1n) leaves the shares unchanged: fixed 0.390, rolling 0.571.

**Other replications** (all in `results.json`):
- MiniLM vs bge topics: ITS 1.088; R6b ≈ R6; δ 1.49.
- All four NAME definitions: the fixed R1 share is 0.40 for strict and loose and 0.24 for compound.
- NA pool: R1 share fixed 0.32 [0.28, 0.36], rolling 0.57 [0.52, 0.63].
- non-LLM subset: fixed 0.39 [0.35, 0.45]; rolling **0.61** [0.55, 0.68].
- Without 2019 and excluding 2026: for ITS see T1.1; for H1c see §3.

## 7. Deviations from PLAN.md (logged)

1. **Pilot ITS number.** The plan's "pilot 1.28/yr" belongs to colon (compound) titles, not NAME. We report all four definitions; NAME gives 1.098.
2. **sup-LR robustness.** A kink-only (no level shift) scan was added post hoc beside the pre-specified level+slope scan. They select different years (2024 vs 2023), and both are reported.
3. **H1c inference.**
   - The pre-registered paper bootstrap is implemented in two ways: a conditional version (2,000 replicates; models fixed) and a refit version (B = 300).
   - The audit made year-level inference primary: two-stage refit plus year shocks.
   - A permutation test and a Welch t are reported as well.
4. **C grid.**
   - C is chosen by 5-fold CV (log loss), as pre-registered.
   - The keyword (R2) and one-hot (R6) grids were widened after their first fit chose the lowest grid value.
   - The pilot's fixed C = 0.5 is reported as a labelled sensitivity only.
5. **Recalibration in the fixed and placebo windows.** The same cross-fitted intercept recalibration as the rolling design is applied (to obs_2023, or to obs_2020 for the placebo).
6. **R2 keywords.** Each normalised keyword phrase is treated as one token (min_df 5, max_df 0.5). After the audit, R2 uses only papers with keywords.
7. **R5.** The six frozen rhetorical-move n-grams are removed by token-subsequence match.
8. **DFL new-key bins.** The PLAN writes (.5, 1); we use (.5, 1] so that all-new teams are kept. The new-key share uses a fixed 2-year lookback (audit). Keyless rows are dropped.
9. **F for D1.** F = F24(≥ 2 words) ∪ F26 ∪ title typography, following D3's note that "the ≥ 2 variant is used for D1". A_max = 0.39 is taken from the PLAN, not re-estimated.
10. **H1b and H1c scope.** R3 is limited to 2018–26, as embedded. For R3, the 2019 rolling window therefore trains on 2018 only.
11. **Added diagnostics** (exploratory, labelled): R1u, R1n, R1@0.5, an established-topics split of u, and a 3-year cumulative placebo-vs-fixed comparison.
12. **Extra script.** `d1_summary.py` (merging, Holm, figures) was added beside the three scripts the PLAN names.
13. **Audit fixes** (details in "Audit response"):
    - fold-ensemble prediction;
    - training-year-FE and intercept+slope-recalibration sensitivities;
    - year-level inference for H1a/H1c;
    - per-year H1d with fixed lookback;
    - misclassification-corrected, year-matched tool share;
    - year-matched new-topic placebo;
    - refit bootstrap for the fixed-window Shapley models;
    - relabelling ("composition", "unexplained residual").

## 8. Limitations

- **Ten years and few post years.** Break dating and the H1c difference rest on 3 post-2024 years and 5 pre years. Year-level inference is much weaker than paper-level inference for both. The year-shock variance τ is itself estimated from 10 points.
  - A held-out replication that resamples papers within the same calendar years (as CT2 in PLAN §4 is written) cannot test year-level acceleration. It needs year-level variance, as in the two-stage inference used here.
- **Content models are specification-dependent.**
  - Across design, calibration, year effects and C, the masked content share moves from 0.22 to 0.65. Within the CV-chosen-C specifications it moves from 0.37 to 0.65.
  - The new-topic placebo fails, so the extrapolation critique is not answered.
  - Content shares should be read as a range; "minority" cannot be claimed.
  - Content includes the move to LLM topics, so after 2023 it is not separable from the LLM topic/tool channel.
- **Composition variables are noisy.** New-key share uses exact declared-ID keys within the discovery export; key aliasing inflates new-key counts. The llm_topic cell margin overlaps content.
- **Tool share.** It depends on:
  - δ measured among *detectable* users;
  - A_max taken from the PLAN;
  - an untested nondifferential-misclassification model.

  Fingerprint recall is unknown, and δ is not causal. The title-level marker gives larger associations.
- **Camera-ready caveat.** For U, accepted papers' titles and abstracts may be camera-ready versions. The NA-pool replications use submission-stage text only.
  - They agree in direction for H1a (and are stronger at the year level), H1d and H1e.
  - They give a lower fixed and a similar rolling content share for H1b (0.32 / 0.57).
  - The H1c acceleration is weaker there: +1.14 pp, with the year-robust CI including 0.

## 9. Implications for the thesis in PLAN §1

PLAN §1 is the locked pre-registration and is left unchanged here. Text written from it should use the following instead.

| PLAN §1 sentence | Status after D1 | Replacement |
|---|---|---|
| "dated slope break at 2024 (pilot ITS slope-change OR 1.28/yr)" | Not supported as written. 1.28 was for colon titles; the level+slope sup-LR picks 2023; the year-level CI on U includes 1. | "The NAME trend accelerated (became convex) from about 2022–24, most visibly in 2026: slope change +3.0 pp/yr [2.1, 3.8] (paper level), +2.8 [1.3, 4.4] (year level); log-odds OR 1.098 [1.044, 1.154] (paper level), 1.096 [0.990, 1.214] (year level)." |
| "Content explains only a minority … about 30–45%" | Not established | "Name-masked content accounts for about 0.37–0.65 of the 2023→26 rise, depending on design and calibration (pre-registered specification: 0.39 fixed, 0.57 rolling); a minority is not established." |
| "Unexplained drift … 1.7 pp/yr before 2024 … 3.9 pp/yr after" | Point estimate changed; inference weak | "Content-unexplained drift rose from 1.5 to 2.9 pp/yr; the increase is not established once year-level shocks are allowed for and is absent at the year level in the submission-stage pool and the non-LLM subset." |
| "Detectable LLM drafting adds little … bounded from above" | Not established as a bound; not validated by a positive control on D1's fingerprint | "With the pre-registered abstract fingerprint, LLM drafting accounts for about 7% [1, 13] of the rise at A = 0.39 after a misclassification correction; other markers give up to 16–33%; this is not an upper bound, and the fingerprint behind it does not pass D3's slot positive control (OR 1.29 [0.92, 1.81])." |
| "sped up but did not create" | Not tested by D1 | Drop, unless a new analysis supports it. |

## Files

**Scripts** (`src/analyses/`):
- `d1_its.py`
- `d1_content_cf.py` (stages: `fit`, `summarise`, `refit_boot`)
- `d1_decompose.py` (stages: `fit`, `all`, `refit_boot`)
- `d1_summary.py`

**Outputs** (`outputs/d1_break/`):
- `results.json`, `RESULTS.md`.
- Tables:
  - `T1_1_its.csv`, `its_year_level.csv`, `its_year_deviation.csv`, `its_break_scan.csv`, `its_results.json`;
  - `T1_2_representations.csv`, `cf_rolling_steps.csv`, `cf_fixed_paths.csv`, `content_cf.json`;
  - `refit_boot_R1.{csv,json}`, `refit_boot_fixed.{csv,json}`;
  - `dfl_table.csv`, `shapley_table.csv`;
  - `tool_delta_models.csv`, `T1_3_tool_bound.csv`, `decompose.json`.
- V4 feature lists: `v4_top200_R1_features.csv`, `v4_bottom200_R1_features.csv`.
- Figures (each as PDF, PNG and CSV): `fig_F1_1_counterfactual`, `fig_F1_2_steps`, `fig_F1_3_decomposition`, `fig_its_scan`.
  - One colour per quantity: observed = black, content = orange, unexplained/residual = blue, composition = grey, tool = yellow.
- `scores/`: per-paper out-of-sample scores, with fold-model test scores `s0`–`s4`, for every representation, design and window.
- The pool label in the CSV files is `NApool`.

**Audit:**
- Pre-fix copies of the outputs and scripts: `outputs/audit/d1/pre_fix_backup/`.
- Fix log: `outputs/audit/d1/fix_log.md`.

## Audit response

Three audits were received: code (D1-C1…C9), identification (ID-1…6) and reporting (REP-1…17). Each issue was re-checked before it was fixed. "Valid" means the problem was reproduced.

| Issue | Valid? | What changed | Claim weakened / changed |
|---|---|---|---|
| D1-C1 calibration/prediction model mismatch | **Yes.** Reproduced: the full-data model's p̂ exceeded the fold-consistent p̂ by 0.26–0.41 pp in 2024–26 (rolling). The refitted pipeline reproduces the audit check (R1 rolling 0.574). | Test rows are scored by the 5 CV fold models that calibrate the intercept, in `run_fit`, `point_summary`, `boot_runs`, `new_topic_placebo`, `stage_refit_boot` and the P/R1P Shapley fits. All representations were refitted, and every bootstrap and table was regenerated. | **H1b verdict changed from "falsified" to "partially supported (not falsified; prediction fails)".** R1 rolling 0.620 → 0.574, R5 0.611 → 0.565, R3 0.595 → 0.577. Fixed R1 0.430 → 0.389. Shapley content 0.399 → 0.338, residual 0.507 → 0.574. H1c diff 1.17 → 1.35 pp. |
| D1-C2 no training-year term | **Yes, as a sensitivity.** The pre-registered model has no year term, so this is not a bug. | Added R1yfe/R3yfe/R5yfe (unpenalised-in-effect year dummies; test rows scored at y−1) to T1.2 and the H1c replications. | Lower end of the content range: 0.37 (fixed), 0.53–0.55 (rolling). H1c diff 1.41–1.57 pp. |
| D1-C3 H1c resampling unit | **Yes.** | Two-stage year-level inference (refit draws + year shocks via the telescoped endpoint weights) is primary for the verdict and Holm. Permutation and Welch reported. Year-robust CIs for all replications. The confirmatory CT2 (PLAN §4), a within-year paper bootstrap on the same years, has the same problem. The two-stage inference is the recommended replacement; PLAN not edited. | **H1c verdict changed from "supported" to "not established at the year level"** (raw p 0.022; Holm 0.067; NA pool and non-LLM CIs include 0). |
| D1-C4 H1a clustered SE ignores year shocks | **Yes.** | Year-level REML random-effects meta-regression (t, 6 df) is primary; quasi-binomial dispersion reported; Holm uses the year-level p. | H1a Holm p 0.0006 → 0.071; U year-level CI [0.990, 1.214]. Verdict unchanged ("partially supported"); NA pool year level 1.121 [1.019, 1.232]. |
| D1-C5 tool bound ignores misclassification; A = 1 incoherent; pooled δ vs 2026 A | **Yes.** | Corrected share τ·A/ΔNAME with τ = δ/k; year-matched 2026 δ is primary; A = 1 marked "not identified"; the power of criterion (i) is reported. | "Bounded from above" and "≤ 16% even if all drafted" removed. Tool share 3.1% → 7.1% [1.4, 12.9]. Verdict unchanged for the pre-registered fingerprint. |
| D1-C6 growing new-key lookback; 2021 artefact; H1d only for 2026 | **Yes.** | Fixed 2-year lookback; 2021 coded missing (own cell) in the composition model; H1d evaluated for 2024, 2025 and 2026; the growing-lookback version kept as a sensitivity. | **H1d verdict changed from "supported" to "partially supported"** (2025: 0.316 > 0.30). DFL 2026 0.246 → 0.261. |
| D1-C7 pooled-abs new-topic placebo; shift not recomputed | **Yes** (method). The result was unaffected except in the bge rolling-pre row. | Per-year absolute residuals with year-matched weights; the bootstrap recomputes recalibration; signed gaps reported. | None. All windows still fail (gaps 3.6–8.0 pp). |
| D1-C8 keyword missingness regime | **Yes.** | R2 restricted to papers with keywords and relabelled. | R2 fixed −0.033 → −0.041, rolling 0.123 → 0.117 (R2 is a "lower" bracket only). |
| D1-C9 conditional-only CIs | **Yes.** | Refit bootstrap for the fixed-window R1, P and R1P (B = 200; shared weights) and for rolling R1 (B = 300, rerun). Refit CIs reported beside the conditional ones; other CIs labelled conditional. | Shapley composition CI widens from [0.077, 0.101] to [0.039, 0.154]; residual to [0.481, 0.669]. |
| ID-1 year-level H1a inference | **Yes** (same as D1-C4). | As D1-C4. | As D1-C4. |
| ID-2 dated break vs convex trend | **Yes.** | Smooth-vs-break GLS table (linear, quadratic, kink, segmented 2022–25, quadratic + post·t); the 2024-break wording is removed from the title, headline and thesis replacement; panel (b) of `fig_its_scan`. | "Dated 2024 break" replaced by "convex acceleration from about 2022–24, most visible in 2026". |
| ID-3 H1c telescoping and year shocks | **Yes.** Identity verified by construction (u_y = Δobs_y − cs_y). | Telescoped form stated in §3; two-stage inference (logit τ; LPM τ as a check). | As D1-C3. |
| ID-4 tool bound: power, title marker, selection, precision | **Yes.** | Power of (i) reported; title-typography δ (unconditional, conditional on an intra-word dash, 2026) and DiD δ (F_d1, F_any) added; pre-period selection placebo; assumptions listed. | "Small" is not established; the sensitivity range at A = 0.39 is 5–33%. |
| ID-5 time-proxy words and rhetoric in content | **Yes.** | Year-FE sensitivity (as D1-C2). The content signal is described as mostly the LLM-era topic shift; the rhetoric-stripped refit (audit ID-5) is cited; slope-recalibration sensitivity added. | The content share is reported as a range of about 0.37–0.65; the H1b outcome is specification-dependent in both directions. |
| ID-6 residual labelled "fashion"; "people" | **Yes.** | Residual renamed "unexplained (includes new-topic naming, undetected tool use, unmeasured composition)"; "people" renamed "composition (declared keys)" in text, tables and figures. | "Fashion" is no longer asserted by elimination. |
| REP-1 H1c verdict row overstated | **Yes.** | Verdict row lists the year-level, NA-pool, non-LLM and excluding-2026 results; headline rewritten. | As D1-C3. |
| REP-2 H1a Holm p paper-level only | **Yes.** | Holm uses the year-level p; paper-level and randomization-p families reported; excluding-2026 result and the post hoc label of the kink scan added to the verdict row. | H1a Holm 0.071 (paper level 0.0006; randomization 0.29). |
| REP-3 F1.1/F1.3 show only the fixed design | **Yes.** | F1.1 adds the rolling cumulative counterfactual; F1.3 adds a rolling-content marker; captions identify the fixed-window bars as the lower end of the bracket. | — |
| REP-4 positive control asserted though D3 is missing | **Yes.** | Marked PENDING in the fixer pass; the "demonstration" sentence and the 2.7-vs-1.08 contrast deleted. **Integration pass:** D3 is now audited; §5 reports its answer and `d1_summary.positive_control_d3()` writes it to `results.json → H1e.positive_control_D3`. | H1e no longer claims a validated toolkit. With F_d1 the D3 slot uplift is OR 1.29 [0.92, 1.81], so D1's tool estimate is not validated by a positive control on its own fingerprint. |
| REP-5 "at most 16%" and omitted adverse δ rows | **Yes.** | δ table now includes excluding-2026, 2024-only, 2025-only, components, typography, NA pool and DiD rows with n; "with room to spare" removed. | As D1-C5/ID-4. |
| REP-6 headline omits the content share of the acceleration | **Yes.** | Headline gives the decomposition: +4.7 pp/yr acceleration, of which about 71% is content and 29% unexplained. | — |
| REP-7 PLAN §1 thesis numbers contradicted | **Yes.** | §9 lists replacement sentences. PLAN.md itself is the locked pre-registration and was not edited; DIRECTIONS.md and LITERATURE_BRIEF.md (which repeat 1.28/yr) are outside D1 and were not edited. | Thesis claims weakened as listed in §9. |
| REP-8 rounding mismatches | **Yes.** | All numbers were regenerated and re-checked against `results.json` (`outputs/audit/d1/check_results_md.py`). | — |
| REP-9 bracket and calibration-slope wording | **Yes.** | Bracket now −0.04 to 0.33 (non-masked) and 0.55–0.64 (leaky); calibration slopes reported per representation (R1@0.5 2.60/3.07); a slope above 1 is read as under-dispersion; slope-recalibration sensitivity added. | — |
| REP-10 DFL vs Shapley difference misattributed; "people" label | **Yes.** | Explained as an estimator difference (composition-first 0.139 vs content-first 0.036); bars relabelled "composition: size × new keys × llm_topic". | — |
| REP-11 "residual fashion"; placebo failure missing from verdicts | **Yes.** | Relabelled; the new-topic placebo failure is noted under H1b/H1c (§6); the bge rolling-pre row added. | — |
| REP-12 mixed scales; "modest"; "small part" | **Yes.** | Headline gives the LPM and logit pre-trends and slope changes separately; "modest" dropped; composition described as "about a quarter by DFL". | — |
| REP-13 unverifiable "foundation note"; "one third"; "reproduced" | **Yes** (no such note exists in the repository). | Sentence deleted; "two fifths (0.38)"; "approximately matched". | — |
| REP-14 missing n and CIs | **Yes.** | n columns in T1.1 and the δ table; CIs for 2024/2025-only δ, Oaxaca, R1u rolling and refit shares; per-year drop counts under Population; the unbootstrapped "3.7×" ratio removed. | — |
| REP-15 figure styling | **Yes.** | One colour per quantity; F1.2 whisker caption and content means; F1.3 divider and "not additive" note; "not a CI" legend entries in F1.1; `fig_its_scan` on a log axis with an LR panel. | — |
| REP-16 "NA" read as missing | **Yes.** | Pool label written `NApool` in all CSV outputs. | — |
| REP-17 p-values test falsification boundaries; "R3 0.60" | **Yes.** | Footnote with prediction-level tail probabilities; R3 rolling printed as 0.577. | — |
| Integration pass 2 (cross-direction consistency) | **Yes.** | (i) F_any is defined in full wherever it appears (F24 with ≥ 1 RARE21 word ∪ F26 ∪ title typography; F_d1 differs only in the ≥ 2-word threshold); it was labelled "F24 ≥ 1 word" in the H1e(i) table, the δ table and the positive-control paragraph. (ii) §5 (iii) adds the false-positive-baseline sensitivity: 2021–22 rate (3.2%) gives 7.4% [1.4, 13.4]; 2023 non-accepted papers only, 7.0%. (iii) V4 uses the 2018–26 denominator (22 of 12,928) shared with VALIDATION; the 12,962 in `results.json` includes the 34 NAME papers of 2017 (no survivors), not placeholder rows. (iv) The positive-control reading in `results.json` is now generated from the significance flag instead of hard-coded. | None (wording and disclosure). |

**Claims weakened overall:**
- H1a: "dated 2024 break", and paper-level significance.
- H1c: the acceleration verdict, from "supported" to "not established at the year level".
- H1d: from "supported" to "partially supported".
- H1e: the "bounded from above / at most 16%" language and the positive-control claim. After integration with D3, the positive control fails on D1's own fingerprint (OR 1.29 [0.92, 1.81]) and passes only on the broader F_any (1.42 [1.14, 1.79]).
- Residual: no longer called "fashion".

**Claims strengthened or reversed:**
- H1b: the first version's "falsified" came from a calibration bug. It is now "not falsified, but the prediction fails".
