# D4. The gatekeeper: stage-wise filter gains and the bias of published-only title studies

WP8 results for PLAN.md §D4. Code is in `research/titles/src/analyses/`:
- `d4_stage_gains.py`: H4a, H4b, T4.1, F4.1, S4.1.
- `d4_bias_atlas.py`: H4c, H4e, T4.2, F4.2, F4.3.
- `d4_exit_composition.py`: H4d, F4.4, and the exploratory analyses.
- `d4_collect.py`: builds `results.json` and the T4.1/T4.2 markdown tables.

All outputs are in `outputs/d4_filter/`. All acceptance associations are associational and subject to the camera-ready caveat. "Last list position" is a partition label, and a declared profile key is not a verified person.

## Summary

| Hypothesis | Pre-registered test | Result (2024–26 pooled unless stated) | Verdict |
|---|---|---|---|
| H4a: neutral filter for NAME | Yearly NAME G_total in [0.95, 1.10]; pooled TOST in [0.90, 1.11]; equal 2024 break across ACC/REJ/WD | All 9 yearly gains in band (0.976–1.050). G_total 1.021, 90% CI [1.001, 1.041]. Break ORs 1.053 / 1.119 / 1.107, Wald p = 0.51 | **Supported**. Pool equality is not rejected, but equivalence within ±0.1 is not shown. |
| H4b: depletion of L and O markers | G_total < 1 for the L-union and O-union; G_desk·G_exit < 1 for the L-union | L-union 0.975 [0.951, 1.001] (one-sided p = 0.030). O-union 0.807 [0.749, 0.870]. L-union desk·exit 0.982 [0.972, 0.992] | **Supported** (small for L, large for O) |
| H4c: published-only Kobak bound understates | Accepted/all bound ratio ≤ 0.85 in each of 2024–26; falsified if ≥ 0.9 in both 2024 and 2025 | 0.800 / 0.714 / 0.502. Post hoc pre-ChatGPT baseline: 0.900 / 0.901 / 0.995 | **Partially supported** (fragile to the baseline) |
| H4d: withdrawal excess of named papers lies between authors | Cross-section > 0, within last-position key ≤ 0, and the two differ | +4.06 pp (se 0.96) vs −0.70 pp (se 1.08); difference 4.77 pp (se 0.75) | **Supported** |
| H4e: published-only atlas | M metrics within ±10%; deviations concentrate in O and L | M 11/11 within ±10% (median \|log ratio\| 0.018); O 1/4 (0.160); L 7/9 (0.037) | **Supported** (descriptive) |
| Decision-stage gate | A gain enters the headline only if its tipping point exceeds the audit CI | NAME G_dec tipping point 2.92 pp, against an audit DiD of +2.09 pp [−2.57, 6.74] | **No title-feature decision gain is identified** |

## Data and stage frame

The stage frame covers 2018–2026 U. It drops the 71 rows of 2018 that have an unknown decision (OTHER), leaving 43,027 papers.

| Stage | 2024–26 | 2018–23 |
|---|---|---|
| s0 | 30,130 | 12,897 |
| s1 | 29,303 | 12,841 |
| s2 | 21,977 | 10,562 |
| s3 | 8,857 | 4,042 |

Per year, 2024 / 2025 / 2026:

| Stage | 2024 | 2025 | 2026 |
|---|---|---|---|
| s0 | 5,765 | 8,953 | 15,412 |
| s1 | 5,728 | 8,900 | 14,675 |
| s2 | 4,435 | 6,578 | 10,964 |
| s3 | 1,778 | 2,904 | 4,175 |

The desk stage removes 737 papers in 2026 but only 37 and 53 in 2024 and 2025.

**Gains.** Gains are prevalence ratios: P(f | passed stage) / P(f | entered stage).
- For the continuous style density they are ratios of means.
- The CIs come from a paper bootstrap stratified by year, with 2,000 replicates.
- **Pooling.** Pooled gains are year-standardised: each year's stage prevalence is weighted by that year's share of s0. This was fixed before any estimate was seen. Raw pooling is reported as robustness.

**Feature sets.**
- **M:** NAME, compound, phrase colon, mixed-case name, Title Case.
- **O:** ALL-CAPS title, sentence case, question opener.
- **L:**
  - title typography on the raw title;
  - R24 and R26 in the title;
  - F24 (≥ 1 RARE21 word in the abstract) and F26;
  - em dash in the abstract;
  - a year-specific LLM-style density, from 123 / 150 / 223 excess style words in 2024 / 2025 / 2026.
- The unions use the binary markers only.

## H4a. The filter is neutral for the mainstream naming fashion

**Total gain (F4.1, S4.1).**
- **Pooled.** Accepted papers carry NAME titles at almost exactly the rate of all submissions. The pooled 2024–26 G_total is 1.021 (95% CI 0.997–1.044).
- **TOST.** The 90% CI of 1.001–1.041 lies inside the [0.90, 1.11] equivalence margins, so the TOST passes.
- **By year.** Every yearly NAME G_total lies inside the pre-registered [0.95, 1.10] band:

| Year | G_total | 95% CI |
|---|---|---|
| 2018 | 0.976 | 0.68–1.30 |
| 2019 | 1.034 | 0.84–1.23 |
| 2020 | 1.050 | 0.89–1.21 |
| 2021 | 1.039 | 0.89–1.20 |
| 2022 | 1.003 | 0.89–1.12 |
| 2023 | 1.016 | 0.93–1.11 |
| 2024 | 1.029 | 0.97–1.10 |
| 2025 | 1.041 | 1.00–1.09 |
| 2026 | 1.009 | 0.98–1.04 |

- **Robustness.** The result holds under:
  - raw pooling: 1.012, 90% CI 0.993–1.032;
  - dropping the 349 post-decision withdrawals: 1.024, 90% CI 1.004–1.044;
  - keeping every withdrawal that carries a "rejected" decision in s2: 1.021;
  - excluding 2026: 1.037, 90% CI 1.008–1.068;
  - the strict and loose NAME definitions: 1.023 and 1.022.
- **Earlier years.** In 2018–23 the gain was 1.022 (0.966–1.079).

**The stages pull in opposite directions** (F4.1).
- **Desk and exit.** Both deplete NAME slightly:
  - desk 0.998 (0.995–1.000);
  - exit 0.974 (0.965–0.983);
  - desk·exit 0.972 (0.963–0.981).
- **Camera-ready check.** The exit result also holds in the camera-ready-free variant that removes accepted papers from every stage set: 0.946 (0.932–0.961).
- **Decision.** The decision stage enriches NAME: 1.050 (1.028–1.072).
- **Adjusted models (T4.1).** The continuation-ratio logits agree: the desk OR is 0.818 (0.683–0.979), the exit OR 0.961 (0.897–1.030) and the decision OR 1.053 (0.981–1.130). The adjusted total gain is 1.008.
- **The decision gain is not identified against camera-ready retitling.** Its tipping point is 2.92 pp, which lies inside the audit's net-flip DiD of +2.09 pp (95% CI −2.57 to 6.74; T4.2).
  - At the audit's point estimate, the selection-only NAME G_total would be 0.979.
  - The audit CI implies an interval of 0.88–1.07, which is wider than the equivalence margins.
  - Equivalence therefore holds for what a published-only study observes. Whether review itself selects NAME titles is not identified.

**The 2024 break by pool** (`its_pools.csv`). This uses the D1 ITS logit, 2018–26, with topic100 FE.

| Pool | Slope-change OR | 95% CI |
|---|---|---|
| ACC | 1.053 | 0.977–1.134 |
| REJ | 1.119 | 1.037–1.206 |
| WD | 1.107 | 0.992–1.235 |

- **Equality test.** The Wald test does not reject equality: χ²(2) = 1.35, p = 0.51. The joint covariance comes from topic-clustered influence functions, and its diagonal reproduces the model SEs to the third decimal.
- **±0.1 criterion.** The largest point difference is 0.061 on the log-OR scale (ACC − REJ), which meets the |Δ log OR| < 0.1 point criterion. No pairwise difference is TOST-equivalent at ±0.1, because the pairwise 90% CIs span −0.17 to +0.12.
- **Pilot.** The pilot's 1.14–1.16 is not reproduced for ACC, but it is approached for REJ and WD. D1 reports the same ACC estimate (1.042 for 2017–26).
- **Variants.** Equality is also not rejected:
  - without controls or topic FE: p = 0.82;
  - for ACC vs REJ over 2017–26: p = 0.22;
  - with the compound outcome (ORs 1.23 / 1.22 / 1.27): p = 0.77.

**Verdict: supported.** Neither falsification condition holds:
- the 90% CI of G_total is inside [0.90, 1.11];
- the pool breaks do not differ at p < .05.

The claim is "peer review leaves the observed NAME share unchanged". It is not "peer review does not select on NAME", because the decision stage is unidentified.

## H4b. LLM and outsider markers are depleted, mostly mildly

**L-union.**
- **Total gain.** The pooled 2024–26 L-union G_total is 0.975 (95% CI 0.951–1.001; 90% CI 0.954–0.997). The one-sided bootstrap p for G ≥ 1 is 0.030.
- **Pre-decision stages.** Desk·exit, which compares submission-stage text, is 0.982 (0.972–0.992, p < 0.001). The camera-ready-free variant gives 0.976 (0.961–0.991).
- **By year:**

| Year | G_total | 95% CI | Desk·exit | 95% CI |
|---|---|---|---|---|
| 2024 | 0.977 | 0.912–1.041 | 0.992 | 0.970–1.016 |
| 2025 | 0.955 | 0.904–1.006 | 0.969 | 0.948–0.990 |
| 2026 | 0.983 | 0.952–1.016 | 0.984 | 0.971–0.996 |

- **Robustness.** The depletion holds under:
  - raw pooling: 0.961 (0.937–0.987);
  - dropping wd_post: 0.977;
  - excluding 2026: 0.964 (0.926–1.002).

**The depletion is driven by a few markers** (F4.1).
- **Title R24 words:** total 0.807 (0.740–0.874), coming from both exit (0.901) and decision (0.896).
- **Abstract style density:** total 0.965 (0.955–0.975); exit 0.975.
- **F24:** total 0.963 (0.919–1.011); exit 0.970 (0.953–0.988).
- **Markers that are not depleted:**
  - title typography: 0.936 (0.730–1.149);
  - F26: 1.023;
  - the abstract em dash: 0.979 (0.915–1.049);
  - R26, which is enriched: 1.060 (0.967–1.157).
- **Title vs abstract.** As a union, the title markers are depleted (0.915, 0.863–0.970). The abstract markers are near-neutral (0.993, 0.964–1.024).
- **Typography pilot.** The pilot's 2026 LLM-typography gain of 0.79 is not reproduced. With the corrected raw-title measure (v2 `title_typo`) the 2026 G_total is 0.914 (0.699–1.138).

**The depletion is a reversal.** In 2018–23 the same L markers were enriched among accepted papers: L-union G_total 1.154 (1.070–1.236).
- **Logits (T4.1).** In the 2018–23 logits the L-union *raised* the odds of passing:
  - exit OR 1.229 (1.075–1.404);
  - decision OR 1.238 (1.071–1.430).
- **2024–26.** It lowers them:
  - desk OR 0.833 (0.730–0.950);
  - exit OR 0.933 (0.882–0.987);
  - decision OR 0.955 (0.901–1.013, n.s.).
- **Relative to the pre-LLM years,** the post-2024 gains are lower (post/pre ratio):
  - total: 0.845 (0.783–0.915);
  - pre-decision: 0.951 (0.927–0.977).
- **NAME** shows no such shift: post/pre ratio of the total gain 0.999 (0.944–1.062).

**O-union.**
- **Total gain.** The O-union G_total is 0.807 (0.749–0.870).
- **ALL-CAPS titles** have a total gain of 0.361 (0.260–0.470), which reproduces the pilot's 0.37.
- **By stage.** Almost all of the O depletion sits at the decision stage: O-union G_dec 0.812, against desk·exit 0.994 (0.969–1.019). ALL-CAPS is also depleted at exit (0.839, 0.775–0.904; T4.1 exit OR 0.598). Sentence case is *enriched* at exit (1.043) and depleted at decision (0.868).
- **Camera-ready caveat.** The decision-stage part is exactly what camera-ready reformatting could produce. ALL-CAPS and sentence case are unauditable here: 0 and 7 accepted v1 titles in the audit.

**Verdict: supported.** The falsification condition (L-union G_total ≥ 1) does not hold. The two-sided 95% CI of the total L gain touches 1.001, and the depletion is a few percent.

## Continuation-ratio models (T4.1)

`T4_1_continuation_ratio.{csv,md}`. Each feature is entered alone, with these controls:
- year × area FE in 2024–26, or year FE in 2018–23;
- log authors, llm_topic and topic100 FE;
- SEs clustered by topic100.

For each feature, the adjusted gain is G_adj = RR_att / (s·RR_att + 1 − s). The product of the stage G_adj values (2024–26) gives the adjusted total gain:

| Feature | Adjusted total gain |
|---|---|
| NAME | 1.008 |
| Compound | 1.008 |
| Mixed-case name | 1.044 |
| Title Case | 1.016 |
| ALL-CAPS | 0.387 |
| O-union | 0.828 |
| R24 | 0.832 |
| F24 | 0.948 |
| L-union | 0.967 |

Adjustment barely moves the descriptive gains. Topic, team size and area composition do not explain the depletion pattern.

Notable stage effects in 2024–26:
- **Desk stage:**
  - question openers are desk-rejected more often: OR 0.522 (0.349–0.783) for passing;
  - so are F26 (OR 0.709) and abstract em dashes (OR 0.760);
  - style density: OR 0.820 per SD.
- **Decision stage:** Title Case has an OR of 1.435 (1.289–1.598), and ALL-CAPS an OR of 0.324 (0.221–0.475).

## Decision-stage bound (T4.2)

D4 computed its own copy of the snapshot module from `cache/arxiv_audit.jsonl`. WP4's `outputs/snapshot/T4_2_tipping_points.csv` appeared later and agrees exactly for NAME: P_s0 0.3563, P_s2 0.3462, P_s3 0.3636, DiD +2.085 pp, tipping points 2.916 / 1.036 pp. Its primary DiD interval is wider (−3.16 to 7.33 pp).

**The pairs.**
- There are 331 pre-decision arXiv v1 pairs: 206 accepted, 125 rejected.
- Titles changed in 29.6% of accepted pairs and 23.2% of rejected ones (normalised words).
- **NAME flips:** 7 adds and 6 drops among accepted papers, against 1 add and 3 drops among rejected ones.

**The NAME net-flip DiD.** It is +2.09 pp:

| Variant | DiD (pp) | 95% CI |
|---|---|---|
| Primary (normal-theory) | +2.09 (se 2.37) | −2.57 to 6.74 |
| Bootstrap | | −2.63 to 7.08 |
| Audit years 2024–26 only | +3.01 | |
| Population-weighted 2023–26 | +2.07 | |

**Tipping points.** Accepted papers are part of s2 and s0, so the tipping points are D\* = (P3 − P2)/(1 − a2) for G_dec and (P3 − P0)/(1 − a0) for G_total.
- **NAME:** 2.92 pp for G_dec and 1.04 pp for G_total. The plan's 1.8 pp figure omitted the 1 − a2 = 0.60 factor.
- **G_dec interval** implied by the audit CI: 0.93–1.09.
- **No auditable feature is identified** (NAME, compound, phrase colon, mixed-case name, Title Case, O-union, L-title, the NAME variants, ALL-CAPS name, LLM abbreviation-only). Every tipping point lies inside the audit CI.
- **Unauditable features** (fewer than 10 accepted v1 titles): ALL-CAPS title, sentence case, question opener, title typography, R24, R26 and snowclones.
- **Abstract markers** (F24, F26, em dash, density) cannot be audited at all, because no v1 abstracts are cached. WP4's abstract audit file has 0 records.

**Consequence for the headline.** No acceptance-margin claim about title features passes the gate. The desk and exit gains, and every diachronic claim, are unaffected.

## H4c. Published-only Kobak bounds understate LLM use, but the size depends on the baseline

The bound uses the share of abstracts with at least one RARE21 word (F24). The bound is p_Y − q_Y, with the conservative baseline q_Y = max(linear 2021–23 trend extrapolated to Y, max(p2022, p2023)). It is computed separately within each set (F4.3, `kobak_bounds.csv`).

| Year | All submissions (pp) | Accepted (pp) | NA pool (pp) | Accepted/all |
|---|---|---|---|---|
| 2024 | 16.0 [14.9, 17.1] | 12.8 [10.3, 15.1] | 17.2 [15.9, 18.6] | 0.800 [0.658, 0.918] |
| 2025 | 12.2 [11.1, 13.1] | 8.7 [5.8, 11.1] | 13.2 [12.1, 14.3] | 0.714 [0.504, 0.891] |
| 2026 | 6.0 [4.8, 6.7] | 3.0 [−0.5, 5.9] | 6.5 [5.7, 7.3] | 0.502 [−0.081, 0.932] |

This reproduces the pilot: 12.8 / 8.7 / 3.0 accepted vs 15.8 / 12.0 / 5.8 all. All three ratios are ≤ 0.85, and the falsification condition (≥ 0.9 in both 2024 and 2025) does not hold.

**Where the gap comes from.** The understatement comes mainly from the baseline years, not from the LLM era.
- **2024–26 prevalence is close.** In 2024, accepted abstracts carry a RARE21 word at nearly the all-submission rate: 17.8% vs 19.1%. In 2026 the two are equal: 9.3% vs 9.2%.
- **The accepted baseline is higher and rising.** In 2021–23, accepted abstracts went 2.95 → 3.54 → 4.30%, while all submissions went 3.35 → 2.49 → 3.12%.
- **Why that matters.** ICLR 2023 camera-ready abstracts were finalised after ChatGPT's release on 30 Nov 2022. The pre-registered direction argument (camera-ready polishing can only raise accepted rates, so the understatement is conservative) does not cover the baseline years. There, polishing raises the accepted baseline and *lowers* the accepted bound.
- **Post hoc sensitivity.** With the baseline max(p2021, p2022), the F24 ratios are 0.900 [0.766, 1.014], 0.901 [0.758, 1.017] and 0.995. That is exactly on the falsification boundary.
- **Other variants:**
  - the no-trend max(2022, 2023) baseline gives 0.84 / 0.82 / 0.83;
  - the ≥ 2-word variant (F24_2) is less baseline-sensitive: 0.78 / 0.83 / 0.80 under the primary baseline, and 0.79 / 0.86 / 0.93 under max(2021, 2022);
  - the abstract L-union gives 0.84 / 0.82 / 0.91.

**Verdict: partially supported.** The pre-registered criterion is met and the direction is robust: accepted-only bounds are lower in every specification. The ≥ 15% size is not robust to excluding the post-ChatGPT 2023 camera-ready baseline. 2026 is uninformative, because the accepted bound's CI includes 0.

## H4d. The withdrawal excess of named papers is between authors

**Design** (F4.4, `exit_composition.csv`).
- **Population and outcome.** The population is REJ ∪ WD, 2024–26. The outcome is "withdrawn", with the 2026 post-decision withdrawals counted as withdrawn.
- **Models.** These are LPMs with year FE, log authors and llm_topic.
- **Sample.** Both models use the same sample: 13,185 papers, 3,571 last-position profile keys with ≥ 2 papers, of which 1,957 vary in NAME.

**Results.**
- **Cross-section.** Named papers are more often withdrawn than rejected: +4.06 pp (se 0.96; 95% CI 2.17–5.95). On the full sample (n = 20,419) it is +5.12 pp (se 0.91). The pilot's +3.6 pp (se 0.55) used a different population that included desk rejections.
- **Within key.** Within last-position key the coefficient is −0.70 pp (se 1.08; 95% CI −2.83 to +1.42). The pilot had −1.4 pp.
- **Difference.** The two differ by 4.77 pp (se 0.75, from the joint key-clustered influence-function covariance; one-sided p < 0.001). The key-cluster bootstrap with 500 replicates gives 3.21–6.24 pp.

**Robustness** (cross-section / within / difference):

| Variant | Cross (pp) | Within (pp) | Difference (pp) |
|---|---|---|---|
| wd_post counted as rejected | +3.53 | −1.10 | 4.64 |
| Desk rejections included | +3.72 | −0.88 | 4.60 |
| The pilot's "last profile key" definition | +4.06 | −0.72 | 4.79 |
| topic100 FE added | +0.84 | −1.74 | 2.59 (se 0.71) |

The topic100 row shows that topic composition carries much of the cross-sectional excess.

**Before 2024.** In 2018–23 the within estimate is +4.20 pp (se 2.78), against a cross-section of +7.77. The between-author pattern is a 2024–26 result.

**Other features.**
- **Mixed-case name and compound** show the same between-author pattern:
  - mixed-case name: +4.30 → −0.17;
  - compound: +4.04 → +0.43.
- **F24 and the L-union** show it too:
  - F24: +2.08 → −0.94;
  - L-union: +1.58 → −0.15 (difference 1.72, se 0.66).
- **O markers** have negative cross-sectional coefficients that move toward 0 within key: O-union −3.16 → +0.33.
- **R24 and R26** stay positive within key: +3.90 and +6.52 pp.

**Verdict: supported.**
- The within estimate is below the cross-section, so the falsification condition does not hold.
- The within point estimate is ≤ 0, but its CI does not exclude a small positive effect up to +1.4 pp.

## H4e. A published-only study gets the mainstream fashion right and the LLM and outsider picture wrong

**Design.** There are 24 pre-registered statistics (F4.2, `atlas.csv`). Each is computed on s0 through s3 for 2024–26 unless stated, and the gap log(T_s3/T_s0) is split into desk, exit and decision parts.

**M statistics: 11/11 point estimates within ±10%.**

| Statistic | All | Accepted | Ratio (95% CI) |
|---|---|---|---|
| NAME | 35.6% | 36.4% | 1.021 (0.998–1.045) |
| Compound | | | 1.018 |
| Phrase colon | | | 1.012 |
| Mixed-case name | | | 1.059 (1.029–1.091) |
| Title Case | | | 1.018 |
| Snowclone share | 1.08% | 0.98% | 0.908 (0.747–1.068) |
| LLM abbreviation-only share among LM-naming titles | 49.2% | 49.3% | 1.002 |
| ITS slope-change OR, 2018–26 | 1.107 | 1.053 | 0.951 (0.889–1.017) |
| Colon premium, 2024–26 (decided-only vs all) | OR 1.018 | OR 1.053 | 1.034 (1.009–1.060) |
| Opener entropy (NAME-collapsed, rarefied) | 6.893 bits | 6.789 bits | 0.985 (0.974–0.996; random-selection p = 0.014) |
| Lexical-turnover JSD | 0.2363 | 0.2342 | 0.991 (0.977–1.006) |

- **Colon premium trend.** The trend, −0.035 vs −0.031 log-OR per year, does not differ (difference 0.004, −0.003 to 0.011).
- **Peak years of the top-30 fashions.** Accepted-only peaks agree with all-submission peaks for 67% of words. Random subsets of the same size agree for 65% (95% band 47–83%), and the mean shift is 0.63 vs 0.61 years.
- **90% CIs.** Two M statistics have 90% CIs that cross the margin: the snowclone share and the ITS ratio.

**O statistics: 1/4 within ±10%.** The median |log ratio| is 0.160.
- ALL-CAPS: 0.361
- O-union: 0.807
- Question opener: 0.899
- Sentence case: 0.905

**L statistics: 7/9 within ±10%.** The median |log ratio| is 0.037. The outliers are R24 prevalence (0.807) and the Kobak bound (0.717).

**Deviations concentrate in O and L, as predicted.**

**Selection vs editing.**
- **What is exact.** The desk and exit parts are exact selection on submission-stage text. In panel b they are small for M statistics; the NAME exit part is −0.026 on the log scale.
- **Where editing is separable.** It can be split off only for the auditable title features, and there the 331-pair audit does not bound it. For example, NAME editing is +0.042 on the log scale (interval −0.047 to +0.148). For the O-union the audit interval is unbounded.
- **What a published-only study can rely on.** It reproduces the M prevalences and their trends within a few percent. Any acceptance-margin decomposition of those small gaps is unidentified with the current audit.

## Exploratory (not confirmatory)

**Exit timing, 2025–26** (`exit_timing.csv`, `exit_calendar.csv`).

*Calendar check.*
- **Review release.** Withdrawal dates (modification_ms) spike on 2024-11-15 (240) and 2025-11-12 (463). The review releases were around 12 November.
- **Decisions.** They also spike on decision days: 2025-01-23 (54) and 2026-01-26 (108).
- **Baseline.** The median day has 2–3 withdrawals.

*Findings.*
- **NAME in the first week after reviews.** Papers withdrawn in that week carry NAME titles more often than rejected or accepted papers:

| Year | Week-1 withdrawals | Rejected | Accepted |
|---|---|---|---|
| 2025 | 0.417 [0.384, 0.451] | 0.299 [0.285, 0.314] | 0.345 |
| 2026 | 0.457 [0.432, 0.483] | 0.379 [0.367, 0.391] | 0.408 |

  This reproduces the C3 pilot (.42/.46 vs .30/.38).
- **Post-decision withdrawals in 2026** are the most NAME-heavy and L-heavy group: NAME 0.489 [0.440, 0.538], L-union 0.434 [0.387, 0.483].

**Early vs late 2026 desk rejections: not testable.** All 737 desk-rejection timestamps in 2026 fall on or after the decision date; 712 are on 2026-02-12. They record a bulk post-decision update, not the desk-rejection date. In 2025, 94% of the 53 desk rejections have pre-decision timestamps, which is too few to split.

## Deviations from PLAN.md (all logged in `results.json` → `deviations`)

1. **Pooling.** Pooled gains are year-standardised; raw pooling is robustness. PLAN does not specify the pooling.
2. **Frame.** The 71 OTHER rows of 2018 are dropped.
3. **ALL-CAPS** is the title casing class. The scout stage pilot used the NAME-lead orthography; that variant is reported as `allcaps_name` (G_total 0.922).
4. **L-union** covers the binary L markers only. Em dash means the abstract em dash; the title em dash is secondary because it is rare.
5. **Style density** re-implements the scout rule on the frozen scout style pool, copied to `analyses/d4_lexicon.json` (SHA-256 2396cb6e…918).
6. **Tipping point** includes the accepted share of s2: D\* = (P3 − P2)/(1 − a2). This gives NAME 2.9 pp, not the plan's 1.8 pp.
7. **Snapshot module** is computed in D4 from `cache/arxiv_audit.jsonl`, because `outputs/snapshot/` did not exist at run time. It was checked against WP4 afterwards and agrees.
   - Only titles are auditable.
   - "Auditable" means at least 10 accepted v1 titles and 10 accepted stored titles carry the feature.
8. **Colon premium.** The published-only analogue is decided-only (ACC vs REJ). No accepted-only premium exists.
9. **Entropy and JSD intervals** pivot on a random-selection band (1,000 random s0 subsets of accepted size). The paper bootstrap produced intervals that excluded the point estimates, because duplicates bias the unrarefied accepted set differently from the rarefied sets.
10. **H4c baseline.** A post hoc max(2021, 2022) baseline sensitivity was added.
11. **H4d specification.**
    - Population: REJ ∪ WD, 2024–26.
    - Last position: the maximum list position (the D2 convention).
    - Controls: year FE, log authors, llm_topic.
12. **Desk stage.** Desk-stage logits are fitted for 2024–26 only. The 2026 early/late desk-rejection analysis was dropped as not testable.

## Limitations

- **The decision stage is the weak link.** With 331 audit pairs, the NAME DiD has an se of 2.4 pp, and no acceptance gain for a title feature is identified. Abstract markers cannot be audited at all, so every "editing" statement about L markers rests on the stated direction assumption. H4c shows that assumption can fail for baseline years.
- **The desk stage matters in 2026 only.** Desk-rejection reasons are not observed. ICLR's lenient filter makes all selection estimates lower bounds on what a stricter venue would do.
- **The L markers are not LLM use.** Before 2024 the same words marked polished, accepted papers. The post-2024 depletion is a reversal relative to that baseline, not evidence that reviewers detect LLM use.
- **H4d is within-key, not within-person.** Within-key variation is self-selected: 1,957 keys vary in NAME. The within estimate cannot exclude a small positive effect. Adding topic FE halves the cross-section/within contrast.
- **Atlas uncertainty differs by statistic.**
  - Bootstrap for the prevalences and the Kobak bound.
  - Influence-function covariance for the ITS and the colon premium.
  - A random-selection band for entropy and JSD.
  - No interval for the peak-year agreement beyond the random null.

## Files

**Scripts:** `src/analyses/d4_stage_gains.py`, `d4_bias_atlas.py`, `d4_exit_composition.py`, `d4_collect.py`, `d4_lexicon.json`.

**Figures** (each as PDF, PNG and CSV):
- `fig_F4_1_stage_ladder`
- `fig_F4_2_bias_atlas`
- `fig_F4_3_kobak_bounds`
- `fig_F4_4_exit_arrows`
- `fig_S4_1_total_gain_by_year`

**Tables:**
- `T4_1_continuation_ratio.{csv,md}` and `T4_1_adjusted_total.csv`
- `T4_2_audit.md`, `T4_2_audit_flips.csv`, `T4_2_decision_bound.csv`
- `gains.csv`, `prevalence_by_stage.csv`, `its_pools.csv`
- `kobak_bounds.csv`, `kobak_series.csv`
- `atlas.csv`, `atlas_peaks.csv`
- `exit_composition.csv`, `exit_timing.csv`, `exit_calendar.csv`
- `audit_pairs.csv`, `style_density.parquet`, `style_density_words.json`

**Machine-readable:** `results.json` (all hypotheses, robustness, exploratory analyses, deviations and code hashes), `stage_gains.json`, `bias_atlas.json`, `exit_composition.json`.
