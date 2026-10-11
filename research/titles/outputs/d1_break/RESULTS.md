# D1 Results: The 2024 naming break — content, people, or tool?

Work package WP5. Pre-registered in `docs/PLAN.md` §D1; common definitions §0. All numbers below were regenerated in the harmonised pipeline (`src/analyses/d1_its.py`, `d1_content_cf.py`, `d1_decompose.py`, `d1_summary.py`). Machine-readable estimates for every hypothesis and robustness check are in `results.json`. Every statement about acceptance or topic is associational. Author-side quantities use declared profile keys, not persons.

**Population.** Universe U: 43,482 submissions, 2017–2026 (34 placeholder rows dropped).
**Outcome.** NAME (primary) = `name_primary`, a coined lead before a colon or spaced dash.
- NAME share: 20.3% (2023) → 26.6 / 33.1 / 40.5% (2024 / 25 / 26).
- The 2023→2026 rise is ΔNAME = 20.2 pp.

## Verdict summary

| Hypothesis | Pre-registered prediction | Estimate (95% CI) | Falsification rule | Verdict | Holm-adj. p |
|---|---|---|---|---|---|
| H1a dated break | Slope change OR > 1 on U. Holds in NA and non-LLM. sup-LR picks 2024/25. Placebos 2020–22 null. | OR 1.098 [1.044, 1.154]/yr. NA 1.128 [1.061, 1.199]. Non-LLM 1.116 [1.055, 1.180]. Placebos 0.85–0.93, all CIs include 1. Level+slope sup-LR picks **2023**; kink-only scan picks 2024. | NA CI includes 1, or a placebo ≥ actual | **Partially supported** (not falsified) | 0.0006 |
| H1b content minority | Masked content share in [0.20, 0.50] for every masked representation; none ≥ 0.60 | Fixed window: R1 0.43 [0.39, 0.48], R3 **0.51** [0.46, 0.56], R5 0.42 [0.38, 0.47]. Rolling: R1 **0.62** [0.58, 0.67], R3 0.60 [0.55, 0.65], R5 **0.61** [0.57, 0.66] | Any masked share ≥ 0.60 | **Falsified** (rolling design) | 0.81 |
| H1c drift acceleration | mean u(2024–26) − mean u(2019–23) > 0; ratio ≥ 1.5 | u: 1.38 → 2.55 pp/yr. Diff +1.17 pp, paper bootstrap [0.38, 1.97]; refit bootstrap (B = 300) [0.24, 2.00]. Ratio 1.85 [1.13, 3.04]. | Ratio < 1.2, or the diff CI includes 0 | **Supported**, fragile (see text) | 0.007 |
| H1d composition minority | DFL composition share ≤ 0.30 | 0.246 [0.209, 0.286]. Shapley people 0.094 [0.083, 0.107]. | Share ≥ 0.50 | **Supported** | 0.002 |
| H1e tool bounded | F=0 rise ≥ 85% of total; δ ≤ +5 pp; tool share at A_max < 0.25 | F=0 rise / all 0.98 [0.96, 1.00]. δ = +1.6 pp [0.0, 3.2]. Tool share at A = 0.39: 3.1% [0.0, 6.2]. | F=0 < 70%, or tool share at 0.39 ≥ 0.5 | **Supported** | 0.002 |

**How the Holm p-values were computed** (family H1a–H1e):
- H1a: one-sided Wald test of the slope change.
- H1b: intersection–union test of bootstrap P(share ≥ 0.60), taking the maximum over the masked representations and both designs.
- H1c: bootstrap P(diff ≤ 0), taking the larger of the conditional and refit bootstraps.
- H1d: bootstrap P(share ≥ 0.50).
- H1e: intersection–union of two tests. One is bootstrap P(F=0 ratio ≤ 0.70). The other is the one-sided Wald P(tool share at A = 0.39 ≥ 0.5).
- Bootstrap p-values use the (k+1)/(B+1) floor.

**Headline.**
- The 2024 naming turn is a modest acceleration of a trend that was already running.
  - The slope change is +3.0 pp/yr (LPM) on a pre-trend of OR 1.12/yr.
  - It is clearly visible only once 2026 is included.
- Detectable LLM drafting and team composition each account for a small part of the rise. Name-masked content accounts for 42–62%, depending on the design and representation.
- The pre-registered claim that content explains a minority does **not** survive the rolling design.
- The content-unexplained drift did accelerate (1.4 → 2.6 pp/yr), but the evidence for this is weaker than the pre-registered bootstrap CI suggests.

---

## 1. H1a: a dated slope break (T1.1, `T1_1_its.csv`; supplementary `fig_its_scan`)

**Model.** Segmented logit
`NAME ~ (t−2023) + post + post·(t−2023) + log authors + llm_topic + topic100 FE`,
with SEs clustered by topic100.

**Primary result (U, n = 43,482).**

| Term | Estimate |
|---|---|
| Pre-trend | OR 1.125/yr |
| Level shift at 2024 | OR 0.975 |
| Slope change | **OR 1.098 [1.044, 1.154]/yr** (one-sided p = 1.3e-4) |
| Slope change, LPM version | +2.97 pp/yr [2.13, 3.81] |

**T1.1 (selected rows).** Slope-change OR per year, with 95% CI.

| Specification | NAME primary | strict | loose | compound |
|---|---|---|---|---|
| U, topic100 FE | 1.098 [1.044, 1.154] | 1.098 [1.043, 1.155] | 1.112 [1.060, 1.166] | 1.231 [1.176, 1.289] |
| NA pool | 1.128 [1.061, 1.199] | 1.130 [1.060, 1.204] | 1.132 [1.068, 1.200] | 1.241 [1.177, 1.309] |
| non-LLM subset | 1.116 [1.055, 1.180] | 1.118 [1.054, 1.186] | 1.138 [1.079, 1.199] | 1.233 [1.170, 1.299] |
| NA × non-LLM | 1.145 [1.065, 1.230] | | | |
| U, bge topic100 FE | 1.088 [1.035, 1.144] | | | |
| U, controls, no topic FE | 1.138 [1.075, 1.205] | | | |
| U, no controls | 1.188 [1.115, 1.266] | | | |
| 2018+ | 1.107 [1.055, 1.161] | | | |
| without 2019 | 1.095 [1.041, 1.151] | | | |
| **excluding 2026** (2017–25) | **1.052 [0.964, 1.147]** | | | |
| ACC / REJ / WD pools | 1.042 [0.964, 1.127] / 1.115 [1.031, 1.206] / 1.107 [0.992, 1.235] | | | |

**Pilot discrepancy.** The pilot's "slope change OR 1.28/yr" was estimated for **colon titles** (`has_colon`, close to our *compound*), 2018–26, with an LLM-topic control and no topic FE. It was not estimated for NAME.
- Our compound estimate with topic100 FE is 1.231.
- For NAME the slope change is about one third as large on the log-odds scale (1.098).
- The foundation note's 1.10 [1.04, 1.15] is reproduced exactly.

**Year-dummy variant.** Deviations from the extrapolated 2017–23 logit trend, on U:

| Year | Deviation (pp) | OR |
|---|---|---|
| 2024 | +1.5 [−0.7, +3.8] | 1.09 [0.96, 1.24] |
| 2025 | +2.7 [−0.5, +5.9] | 1.15 [0.98, 1.35] |
| 2026 | **+5.5 [+1.5, +9.5]** | 1.30 [1.08, 1.56] |

- The NA pool and the non-LLM subset show the same pattern (`its_year_deviation.csv`).
- The rise in 2024–25 is largely what a logit-linear pre-trend already implies. The excess is concentrated in 2026, the year of the new desk regime and the reported separate cohort.

**Break dating.**
- **Placebo breaks** (pre-2024 data, 2017–23): OR 0.854 [0.685, 1.064] at 2020, 0.910 [0.787, 1.051] at 2021, and 0.925 [0.781, 1.096] at 2022. All are null and all are below the 2024 estimate. NA and non-LLM give the same picture.
- **Randomization over break years** 2019–2025 (full data): 2024 has the largest slope-change z (3.66; 2025: 2.87; 2023: 2.12). The randomization p is 1/7 = 0.143, the smallest value attainable with 7 candidate years.
- **sup-LR scan** 2020–2025 (segmented level+slope model vs the linear-trend model; LR values):

  | Break year | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
  |---|---|---|---|---|---|---|
  | LR | 2.7 | 18.0 | 11.6 | **18.4** | 16.4 | 15.4 |

  - The level+slope scan selects **2023**, not 2024/2025. 2021 gets a high LR because of a level dip (NAME 15.7% → 15.0% in 2021).
  - A kink-only (continuous) scan, added as robustness, selects **2024**: LR 16.1, against 14.8 for 2025 and 10.0 for 2023.

**Verdict H1a: partially supported, not falsified.**
- Met:
  - The NA-pool CI excludes 1.
  - No placebo is as large as the 2024 estimate.
  - The break holds in the non-LLM subset and under all four NAME definitions.
- Not met: the pre-registered sup-LR scan picks 2023.
- The logit break also loses significance without 2026 (OR 1.052 [0.964, 1.147]); the LPM version stays positive (+2.0 pp/yr [0.4, 3.7]).
- The appropriate wording is "the trend steepened from about 2023–24, most visibly in 2026", not a sharp 2024 discontinuity.

## 2. H1b: how much of the rise does content explain? (F1.1, T1.2)

**Method.**
- Each representation is fitted as an L2 logit, with C chosen by 5-fold CV (log loss) inside each training window.
- Intercepts are recalibrated so that cross-fitted (out-of-fold) predictions for the last training year match its observed share.
- Content share:
  - fixed window = (p̂_2026 − obs_2023)/(obs_2026 − obs_2023);
  - rolling = Σ content steps 2024–26 / Σ observed steps 2024–26.
- CIs come from a conditional paper bootstrap, stratified by year, with 2,000 replicates. Models are held fixed; the recalibration and all means are recomputed.

**T1.2 (`T1_2_representations.csv`).** Content share of the 2023→2026 rise, with mean out-of-sample AUC and calibration slope.

| Rep. | Role | Fixed 2021–23 → 2026: share [95% CI] | AUC | Cal. slope | Rolling 2024–26: share [95% CI] | AUC |
|---|---|---|---|---|---|---|
| R1 masked TF-IDF (primary) | masked | **0.429** [0.387, 0.478] | 0.741 | 1.24 | **0.620** [0.575, 0.671] | 0.710 |
| R3 bge, masked abstract | masked | **0.509** [0.460, 0.562] | 0.744 | 1.03 | **0.595** [0.551, 0.646] | 0.714 |
| R5 R1 minus rhetorical moves | masked | 0.420 [0.378, 0.468] | 0.740 | 1.24 | 0.611 [0.566, 0.662] | 0.709 |
| R2 keywords | lower | −0.033 [−0.046, −0.020] | 0.570 | 0.58 | 0.123 [0.103, 0.144] | 0.584 |
| R6 topic100 + llm_topic | coarse | 0.178 [0.156, 0.201] | 0.640 | 1.10 | 0.336 [0.306, 0.368] | 0.622 |
| R6b bge topic100 | coarse | 0.186 [0.165, 0.211] | 0.644 | 1.10 | 0.344 [0.314, 0.378] | 0.623 |
| R4 bge, unmasked (leaky) | upper | 0.571 [0.520, 0.628] | 0.759 | 1.06 | 0.661 [0.613, 0.716] | 0.734 |
| R1u unmasked TF-IDF (V4) | diagnostic | 0.400 [0.358, 0.445] | 0.745 | | 0.595 | 0.713 |
| R1n R1 minus naming tokens | diagnostic | 0.429 | 0.740 | | 0.617 | 0.708 |
| R1 at pilot C = 0.5 | sensitivity | 0.252 [0.227, 0.277] | 0.747 | | 0.476 | 0.715 |

**Per-year fixed-window shares for R1.**

| Year | Share |
|---|---|
| 2024 | 0.40 [0.30, 0.55] |
| 2025 | 0.45 [0.38, 0.52] |
| 2026 | 0.43 [0.39, 0.48] |

**Verdict H1b: falsified, by the pre-registered rule** ("fails if any name-masked representation explains ≥ 60%").
- In the fixed-window design R1 and R5 land inside the predicted band [0.20, 0.50] (0.43, 0.42). R3 lands just above it (0.51 [0.46, 0.56]).
- In the rolling design R1, R5 and R3 explain 0.62, 0.61 and 0.60. The R1 and R5 point estimates exceed 0.60; all three CIs straddle it.
- The pilot's 29% (fixed) and 42% (rolling) are reproduced only at the pilot's hand-set C = 0.5 (0.25 and 0.48). With the pre-registered CV choice of C (C = 2 for most windows), content explains more.
- The out-of-sample calibration slopes are above 1 (1.1–1.4). Content scores therefore discriminate *more* strongly in later years than in training, which argues against over-fitting as the explanation.
- The honest range for name-masked content is about **0.42–0.62 of the 2023→26 rise**. The fixed window is at the low end and the rolling one-step design at the high end.
- R3 (masked bge) gives 0.51 in the fixed window, already above the band, and 0.60 in the rolling design. Its fixed-window share by year is 0.51 / 0.60 / 0.51 for 2024–26.
- R3 is also better calibrated out of sample than the TF-IDF models (calibration slope 1.03 fixed, 0.94 rolling), so its larger share is not an artefact of mis-calibration.
- The non-masked bracket runs from 0.12–0.34 (keywords, coarse topics) to 0.57–0.66 (leaky unmasked bge).

**Figure F1.1** (`fig_F1_1_counterfactual.{pdf,png}`). Observed NAME share against content counterfactuals:
- the fixed window (train 2021–23, anchored at 2023);
- the placebo window (train 2018–20, anchored at 2020);
- the full R1–R6 envelope (light) and the name-masked envelope (dark).
- Inset: NA pool, R1.

## 3. H1c: did content-unexplained drift accelerate? (F1.2)

**Method.**
- Rolling one-step-ahead R1: train on y−3..y−1, recalibrate to obs_{y−1} on cross-fitted scores, then u_y = obs_y − p̂_y.

**Annual decomposition** (pp; R1; `cf_rolling_steps.csv`, `fig_F1_2_steps`):

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|
| Observed step | +3.1 | +2.6 | −0.7 | +3.3 | +2.0 | +6.3 | +6.5 | +7.3 |
| Content step | −0.3 | +0.9 | +0.5 | +0.8 | +1.5 | +2.5 | +5.7 | +4.3 |
| Unexplained u | +3.4 | +1.6 | −1.1 | +2.5 | +0.5 | +3.8 | +0.9 | +3.0 |

**Result.** mean u = 1.38 pp/yr (2019–23) → 2.55 pp/yr (2024–26).

| Statistic | Estimate | 95% CI |
|---|---|---|
| Difference, conditional paper bootstrap | +1.17 pp | [0.38, 1.97] |
| Difference, refit paper bootstrap | +1.17 pp | [0.24, 2.00] (ratio [1.13, 3.04]) |
| Ratio (conditional bootstrap) | 1.85 | [1.22, 3.14] |

- The refit bootstrap (B = 300) re-estimates every rolling model on resampled papers within year, at the chosen C.
- Content steps jumped from ≈ 0.7 pp/yr before to 4.2 pp/yr after.
- The pilot was 1.7 → 3.9 pp/yr (ratio 2.3).

**Verdict H1c: supported by the pre-registered criteria** (ratio ≥ 1.5 and the paper-bootstrap CI excludes 0). It is fragile in four ways, which a reader should weigh:
1. **Year-level uncertainty.** The paper bootstrap holds each year's shocks fixed.
   - Treating the eight u_y as draws, an exact permutation test of pre/post labels (56 arrangements) gives one-sided p = 0.18. Welch t = 0.99, p = 0.18.
   - u is noisy from year to year: SD 1.8 pp before, 1.5 pp after, and 2025 itself is only +0.9.
2. **Pools and subsets.**

   | Variant | Diff | 95% CI | Ratio |
   |---|---|---|---|
   | NA pool | +0.83 pp | [−0.16, +1.85] | 1.49 |
   | non-LLM subset | +0.40 pp | [−0.53, +1.30] | 1.27 |
   | strict NAME | +0.94 pp | [0.13, 1.73] | 1.64 |
   | loose NAME | +1.31 pp | [0.46, 2.16] | 2.17 |
   | compound | +3.72 pp | [2.73, 4.73] | 3.80 |
   | R5 | +1.22 pp | [0.35, 2.03] | 1.88 |
   | R6 | +2.47 pp | [1.66, 3.29] | 2.24 |
   | R4 (leaky) | +0.98 pp | [0.19, 1.82] | 1.76 |
   | without 2019 (pre = 2020–23) | +1.68 pp | [0.74, 2.57] | 2.91 |
   | excluding 2026 (post = 2024–25) | +0.95 pp | [−0.04, +1.99] | 1.69 |
   | R3 masked bge | +1.26 pp | [0.39, 2.06] | 1.86 |

   The acceleration is weakest in the camera-ready-free pool and among non-LLM papers, where its CI includes 0.
3. **New-topic placebo fails** (§5). Content models under-predict NAME in fast-growing clusters. Unexplained drift is therefore partly a property of new topics. Restricting u to papers outside fast-growing clusters still gives 1.21 → 2.22 pp/yr (ratio 1.84; exploratory). Inside fast-growing clusters, u is much larger in both periods: 5.0 → 6.0 pp/yr.
4. **Cumulative 3-year comparison.**
   - Placebo window (train 2018–20, anchored at 2020): unexplained by 2023 = +3.1 pp [1.0, 5.3]; content share of the 2020→23 rise 0.32 [0.20, 0.61].
   - Fixed window (train 2021–23): unexplained by 2026 = +11.5 pp [9.8, 13.2].
   - Pre-2024 unexplained drift exists (the reason H1c is a difference), and the 3-year unexplained drift was about 3.7 times larger after 2023.

## 4. H1d: people and composition (F1.3; `dfl_table.csv`, `shapley_table.csv`)

**Composition change, 2023 → 2026.**

| | 2023 | 2026 |
|---|---|---|
| Mean declared authors | 4.56 | 5.67 |
| Mean share of new keys | 0.59 | 0.53 |
| llm_topic share | 0.11 | 0.48 |

**DFL composition share of the 2023→y rise** (y-year papers reweighted to the 2023 cell distribution; bootstrap 2,000):

| Cells | 2024 | 2025 | 2026 |
|---|---|---|---|
| team size (6 bins) | 0.13 | 0.20 | 0.175 [0.153, 0.199] |
| size × llm_topic | 0.29 | 0.32 | 0.267 [0.232, 0.307] |
| size × newcomer | 0.10 | 0.17 | 0.148 [0.125, 0.174] |
| **size × newcomer × llm_topic (primary)** | 0.25 | 0.30 | **0.246 [0.209, 0.286]** |
| + experience bins (max prior subs) | 0.26 | 0.33 | 0.246 [0.205, 0.291] |
| primary, NA pool | | | 0.221 [0.177, 0.267] |
| non-LLM subset (size × newcomer) | | | 0.087 [0.060, 0.116] |

- The pilot gave 18% (size) and 26% (size × LLM topic); both reproduce (0.175, 0.267).
- Valued at 2023 cell rates (Oaxaca), the composition share is lower: 0.18.
- Most of the "composition" effect is the llm_topic margin, which overlaps content. Team size and newcomer share alone explain 15–18%.

**Shapley over content (R1) and people (cells).** Fixed window with recalibration; 2026 shares.

| Ordering | Content | People |
|---|---|---|
| Content first | 0.429 | then 0.064 |
| People first | then 0.368 | 0.125 |
| **Shapley** | **0.399 [0.362, 0.442]** | **0.094 [0.083, 0.107]** |

- **Residual (fashion):** 0.507 [0.453, 0.552] of the 2023→26 rise.
- 2024: content 0.37, people 0.10, residual 0.54. 2025: 0.41 / 0.11 / 0.48.

**Verdict H1d: supported.** Composition explains 0.25 [0.21, 0.29] by DFL, and only 0.09 once content is accounted for. Both are below the 0.30 prediction and far from the 0.50 falsification threshold.

## 5. H1e: the tool, bounded (F1.3, T1.3; `tool_delta_models.csv`, `T1_3_tool_bound.csv`)

**Fingerprint.** F (D1 variant) = F24 with ≥ 2 RARE21 words ∪ F26 ∪ title typography.
- Share of papers with F: 2.5% (2023), 7.1% (2024), 5.2% (2025), 19.2% (2026). The 2023 value is the pre-LLM false-positive level.

**(i) NAME rise among F = 0 papers relative to all papers.**

| Population / fingerprint | 2024 | 2025 | 2026 |
|---|---|---|---|
| F (D1 variant) | 1.00 [0.94, 1.06] | 1.00 [0.97, 1.02] | **0.98 [0.96, 1.00]** |
| NA pool | | | 0.98 [0.95, 1.00] |
| broader F_any (F24 ≥ 1 word) | 0.86 [0.73, 0.96] | 0.93 [0.88, 0.97] | 0.95 [0.92, 0.98] |

NAME share 2023 → 2026: 20.3% → 40.1% among F = 0 papers, against 20.6% → 42.0% among F = 1 papers.

**(ii) δ.** LPM `NAME ~ F + log authors | topic100×year`, 2024–26, n = 30,130, clustered by topic100.

| Specification | δ (pp) | 95% CI |
|---|---|---|
| **Primary** | **+1.62** | [+0.02, +3.22] |
| + area×year FE | +1.46 | [−0.08, +2.99] |
| + llm_topic | +1.54 | [−0.05, +3.13] |
| bge topic×year | +1.49 | [−0.21, +3.18] |
| non-LLM subset | −0.18 | [−2.67, +2.31] |
| 2024 only | −0.4 | |
| 2025 only | −0.9 | |
| 2026 only | +2.4 | [0.5, 4.4] |
| F_any | +2.5 | [1.3, 3.8] |

- Logit adjOR: 1.08 [1.00, 1.17]; 1.13 for F_any. The pilot colon adjOR was 1.24.
- δ ≤ +5 pp holds with room to spare. The upper CI is 3.2 pp.

**(iii) Maximum tool share** = δ·A_max/ΔNAME.
- A_max = 0.39 is the PLAN's held-out greedy abstract bound for 2026. It is taken as given and was not re-estimated here.

| A_max | 0.24 | **0.39** | 0.50 | 0.75 | 1.00 |
|---|---|---|---|---|---|
| tool share | 1.9% [0.0, 3.8] | **3.1% [0.0, 6.2]** | 4.0% [0.1, 8.0] | 6.0% [0.1, 12.0] | 8.0% [0.1, 16.0] |

- With every paper treated as LLM-drafted and the upper CI of δ, the tool accounts for at most 16% of the 2023→26 rise.
- The contribution from detectable fingerprints alone (δ × ΔP(F)) is 1.3%.

**Verdict H1e: supported** on all three criteria.

**Positive-control link.** D3's slot result (H3a; WP7, `outputs/d3_register/`) is the demonstration that this toolkit detects LLM influence where it exists. It is computed by WP7 and not reproduced here.
- At the time of writing `outputs/d3_register/` did not yet exist, so no regenerated slot estimate is quoted.
- The PLAN's pilot value is pooled slot OR 2.69 [1.80, 4.01], against 0.87 for the controls. Set against our H1e δ, this would be a lexical-vs-structural contrast: OR ≈ 2.7 for slot wording vs logit adjOR 1.08 for NAME.

## 6. Identification and robustness

**New-topic placebo (pre-registered; fails).**
- Rule: calibration-in-the-large for papers in topic100 clusters whose share grew ≥ 3× relative to the training window. Pass if |obs − pred| in fast-growing clusters ≤ |obs − pred| elsewhere + 2 pp.
- Signed residual = obs − pred.

| Window | Fast-growing (n) | Elsewhere | Gap difference [95% CI] |
|---|---|---|---|
| Placebo 2018–20 → 2021–23 | +5.7 pp (1,154) | +1.1 pp | 4.6 pp [2.0, 7.0] |
| Same, bge clusters | +7.6 pp | +1.1 pp | 6.4 pp [3.5, 9.4] |
| Rolling, 2019–23 | +5.4 pp (495) | +0.9 pp | 4.4 pp [0.8, 8.1] |
| Rolling, 2024–26 | +5.8 pp (2,427) | +2.2 pp | 3.6 pp [1.7, 5.4] |
| Fixed 2021–23 → 2024–26 | +14.9 pp (9,219) | +6.0 pp | 8.9 pp [7.7, 10.0] |

- R3 fails in the same way: gap differences of 2.9–7.6 pp, with fast-growing residuals of +5.4 to +10.1 pp.
- **All fail.** Emerging topics adopt NAME titles faster than their (masked) abstract content predicts, in the pre-LLM period too (diffusion-era 2021–23).
- Two readings remain open:
  - naming is a property of new artefact-producing topics that bag-of-words content does not capture, in which case content shares are understated;
  - the fashion spreads fastest in hot topics.
- The fixed-window content share is therefore *not* robust to the extrapolation critique, especially for 2024–26 when about 31% of papers sit in fast-growing clusters.

**V4: name-masking leakage.**
- The R1 lead survives in 22 of 12,962 NAME abstracts (0.17%), against the 0% target. All are project-page URLs with a digit suffix (e.g. `resgrad1.github.io`): R1 keeps letter runs, so "resgrad1" becomes "resgrad". This is too few to move any share.
- Masked-vs-unmasked AUC gap:
  - TF-IDF (R1u − R1): +0.004 fixed, +0.003 rolling.
  - bge (R4 − R3): +0.015 fixed, +0.020 rolling, +0.027 placebo.
  - Unmasked bge leaks somewhat more than unmasked TF-IDF. The R3 → R4 content share rises from 0.51 to 0.57 (fixed) and from 0.60 to 0.66 (rolling).
- Top-200 R1 features (`v4_top200_R1_features.csv`):
  - 2% contain rare tokens (zipf < 2): textbf, textsc, "embeddings", "regularizer". No name fragments.
  - The top features include naming-announcement words: "named" (rank 19), "called" (rank 28), "we introduce", and LaTeX emphasis.
  - Removing 12 such tokens (exploratory R1n) leaves the shares unchanged: fixed 0.429, rolling 0.617.

**Other replications** (all in `results.json`):
- MiniLM vs bge topics: ITS 1.088; R6b ≈ R6; δ 1.49.
- All four NAME definitions: the fixed R1 share is 0.44 for strict and loose and 0.27 for compound.
- NA pool: fixed R1 share 0.36 [0.31, 0.41].
- non-LLM subset: fixed R1 share 0.43 [0.38, 0.50].
- Without 2019 and excluding 2026: for ITS see T1.1; for H1c see §3.

## 7. Deviations from PLAN.md (logged)

1. **Pilot ITS number.** The plan's "pilot 1.28/yr" belongs to colon (compound) titles, not NAME. We report all four definitions; NAME gives 1.098.
2. **sup-LR robustness.** We added a kink-only (no level shift) scan alongside the pre-specified level+slope scan. They select different years (2024 vs 2023), and both are reported.
3. **H1c inference.**
   - The pre-registered paper bootstrap is implemented in two ways: a conditional version (2,000 replicates; models fixed) and a refit version (B = 300; all rolling models refitted).
   - The more conservative CI is used for the verdict.
   - We added an exact year-label permutation test and a Welch t, which capture year-level shocks the paper bootstrap ignores.
4. **C grid.**
   - C is chosen by 5-fold CV (log loss), as pre-registered.
   - The keyword (R2) and one-hot (R6) grids were widened after their first fit chose the lowest grid value. This is a grid-coverage fix, not tuning toward a result.
   - The pilot's fixed C = 0.5 is reported as a labelled sensitivity only.
5. **Recalibration in the fixed and placebo windows.** The PLAN specifies intercept recalibration only for the rolling design. We apply the same cross-fitted recalibration (to obs_2023, or to obs_2020 for the placebo), so that the fixed-window share is anchored at the observed baseline.
6. **R2 keywords.** Each normalised keyword phrase is treated as one token, with min_df 5 and max_df 0.5.
7. **R5.** The six frozen rhetorical-move n-grams are removed by token-subsequence match. "framework" removes the unigram and every bigram containing it.
8. **DFL newcomer bins.** The PLAN writes (.5, 1); we use (.5, 1] so that all-new teams are kept. Four papers with no keys are dropped.
9. **F for D1.** F = F24(≥ 2 words) ∪ F26 ∪ title typography, following D3's note that "the ≥ 2 variant is used for D1". F_any (F24 ≥ 1) is reported as a variant. A_max = 0.39 is taken from the PLAN, not re-estimated.
10. **H1b and H1c scope.** R3 is limited to 2018–26, as embedded. For R3, the 2019 rolling window therefore trains on 2018 only.
11. **Added diagnostics** (exploratory, labelled): R1u (unmasked TF-IDF), R1n (naming tokens removed), an established-topics split of u, and a 3-year cumulative placebo-vs-fixed comparison.
12. **Extra script.** `d1_summary.py` (merging, Holm, figures) was added beside the three scripts the PLAN names.

## 8. Limitations

- **Ten years and few post years.** Break dating and the H1c difference rest on 3 post-2024 years and 5 pre years. Year-level inference (permutation p = 0.18) is much weaker than paper-level inference.
- **Content models are design-dependent.**
  - The content share moves from 0.25 to 0.62 across reasonable choices: design and C.
  - The new-topic placebo fails, so the extrapolation critique is not answered.
  - Content shares should be read as a range, and "minority" cannot be claimed.
- **Composition variables are noisy.** Share-new uses exact declared-ID keys within the discovery export: more history in later years means fewer apparent newcomers, and key aliasing inflates newcomer counts. The llm_topic cell margin overlaps content.
- **Tool bound.** The tool share depends on δ measured among *detectable* users and on A_max taken from the PLAN. Fingerprint recall is unknown and decays in 2026, so δ for undetected users could differ. δ is not causal.
- **Camera-ready caveat.** For U, accepted papers' titles and abstracts may be camera-ready versions. The NA-pool replications use submission-stage text only. They agree in direction for H1a, H1d and H1e and give similar content shares for H1b (fixed 0.36, rolling 0.62). The H1c acceleration is weaker there: ratio 1.49, CI including 0.

## Files

**Scripts** (`src/analyses/`):
- `d1_its.py`
- `d1_content_cf.py` (stages: `fit`, `summarise`, `refit_boot`)
- `d1_decompose.py` (stages: `fit`, `all`)
- `d1_summary.py`

**Outputs** (`outputs/d1_break/`):
- `results.json`, `RESULTS.md`.
- Tables:
  - `T1_1_its.csv`, `its_year_deviation.csv`, `its_break_scan.csv`, `its_results.json`;
  - `T1_2_representations.csv`, `cf_rolling_steps.csv`, `cf_fixed_paths.csv`, `content_cf.json`;
  - `refit_boot_R1.{csv,json}`;
  - `dfl_table.csv`, `shapley_table.csv`;
  - `tool_delta_models.csv`, `T1_3_tool_bound.csv`, `decompose.json`.
- V4 feature lists: `v4_top200_R1_features.csv`, `v4_bottom200_R1_features.csv`.
- Figures (each as PDF, PNG and CSV): `fig_F1_1_counterfactual`, `fig_F1_2_steps`, `fig_F1_3_decomposition`, `fig_its_scan`.
- `scores/`: per-paper out-of-sample scores for every representation, design and window.
