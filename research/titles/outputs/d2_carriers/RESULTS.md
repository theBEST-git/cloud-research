# D2. Who carries the fashion: communal vs generational change

*WP6. Scripts: `src/analyses/d2_panel.py`, `d2_shiftshare.py`, `d2_markers.py`, `d2_support.py`, `d2_collect.py`. Machine-readable estimates: `results.json`. All numbers below were regenerated in the harmonised pipeline (key-cluster bootstrap, 1,000 replicates, fixed seeds).*

Language follows the README boundaries throughout. A declared profile key is an exact-ID key, not a verified person. "First" and "last list position" are partition labels only and say nothing about seniority or supervision. Every association is descriptive; no influence claim is made.

## Summary

The 2022–23 → 2025–26 rise in NAME titles happened inside the same declared profile keys. At the last list position, keys present in both windows (stayers) moved from 18.8% to 37.1% NAME. The population moved from 19.4% to 37.8%. The within-stayer share is therefore ρ = 0.995 [0.943, 1.050].

Pooled over list positions, ρ = 0.816 [0.777, 0.857]. At the first list position, ρ = 0.525 [0.414, 0.633]. Entrant keys at first position title with NAME 10.6 pp more often than stayer keys there.

Across 85 pre-registered markers, within-stayer change tracks population change (slope 0.92, r = 0.992). Style markers carry a generational increment of 0.17; topic markers carry none (−0.05).

The communal pattern also holds in the pre-LLM email-key era: 2018 → 2020, ρ = 1.20 [0.71, 1.77].

The two supporting tests agree:
- **S2.1:** retitled resubmissions do not add NAME on net (0.000, se 0.025), against an implied drift of +7.2 pp.
- **S2.2:** past-collaborator exposure is no larger than future-collaborator exposure, which fits homophily rather than tie contagion.

The one shortfall is H2c(i). Within stayer keys, with key FE and topic100 FE, the E→L change on papers with no new co-authors is 34% of the raw population change. The prediction was ≥ 50%. Part of the stayers' rise therefore travels with new co-authors.

| Hypothesis | Pre-registered prediction | Estimate (95% CI) | Falsified? | Verdict | one-sided p (Holm) |
|---|---|---|---|---|---|
| H2a communal dominance | ρ_last ≥ 0.70, ρ_any ≥ 0.60 | ρ_last 0.995 [0.943, 1.050]; ρ_any 0.816 [0.777, 0.857] | no (upper CI ≫ 0.5) | **supported** | 0.001 (0.004) |
| H2b first-position increment | ρ_first ≤ ρ_last − 0.2; entrants > stayers at first position in L | ρ_first − ρ_last = −0.470 [−0.602, −0.359]; entrant − stayer = +0.106 [0.085, 0.126] | no | **supported** | 0.001 (0.004) |
| H2c not driven by entrant co-authors | (i) change at share_new = 0 ≥ 0.5 × population change; (ii) all-prior teams ≥ 0.5 × population rise | (i) +6.15 pp [4.54, 7.76] = 0.34 [0.25, 0.43] × 18.3 pp; (ii) 0.66 [0.47, 0.81] | no (CI of (i) excludes 0) | **partially supported** ((i) not met, (ii) met) | 4e-14 (2e-13) |
| H2d style vs topic | slope ≈ 1 (≥ 0.7); G_style > G_topic | slope 0.923 [0.901, 0.946]; G_style 0.166 [0.133, 0.200] vs G_topic −0.047 [−0.068, −0.025]; difference 0.213 [0.176, 0.251] | no | **supported** | 0.001 (0.004) |
| H2e pre-LLM (email keys, 2018→2020) | NAME and colon ρ ≥ 0.5 | NAME 1.20 [0.71, 1.77]; compound 1.13 [0.08, 2.66] | no (both > 0.3) | **supported** (compound imprecise) | 0.001 (0.004) |

The p-values are one-sided against each hypothesis's falsification boundary:
- H2a: ρ_last ≤ 0.5.
- H2b: difference ≥ 0.
- H2c: change ≤ 0.
- H2d: G_style − G_topic ≤ 0.
- H2e: ρ ≤ 0.3.

Bootstrap p-values have a floor of 1/1001. Holm is applied over H2a–H2e.

## 1. Design

**Panel.**
- Main panel: `native_id_kind == 'profile'` keys on U papers, 2021–26, one row per (key, paper). That is 198,640 rows and 89,115 keys (`panel_rows.parquet`, `panel_summary.csv`).
- Email-era panel (H2e): email keys, 2017–20. That is 17,572 rows and 11,507 keys.
- Coverage of the last list position by a profile key is 89.9% of papers in 2021, 95.2% in 2022, 96.4% in 2023 and ≥ 99.4% from 2024. A paper whose last (first) declared position is not a profile key drops out of that partition.
- No key exceeds 40 papers in a year (V6). The maximum is 40, in 2026.

**Windows and groups.** E = 2022–23 and L = 2025–26. Group status is fixed at the key level from presence in any role:

| Group | Definition | Keys |
|---|---|---|
| Stayers (S) | ≥ 1 paper in E and ≥ 1 in L | 8,710 |
| Exiters (X) | in E, not in L | 8,404 |
| Entrants (N) | in L, not in E, never seen in 2021 or 2024 | 56,217 |
| Returners (R) | in L, not in E, but seen in 2021 or 2024 | 6,949 |

**Partitions.**
- Last list position.
- First list position.
- Any role, with rows weighted 1/#panel keys so that each paper sums to 1.
- Paper-level team types, all-prior / mixed / all-new, under three definitions: rolling (key seen in any earlier panel year), fixed (seen in 2021–22, papers from 2023 on) and lag-1 (seen in the previous year).

**Statistics.** Both statistics are in `T2_1_decomposition.csv`.

- **The within-stayer share.** This is the statistic used in H2a, H2b and H2d (where it is "within/pop"):

  ρ = (P_SL − P_SE) / (P_L − P_E)

  - ρ = 1 under purely communal change: stayers change as much as the population.
  - ρ = 0 under purely generational change: stayers keep their E style.
- **The exact Kitagawa identity of the plan:**

  Δ = s̄(P_SL − P_SE) + (1 − s̄)(P_OL − P_XE) + (s_L − s_E)(P̄_S − P̄_O)

  - Its first term equals s̄·ρ·Δ.
  - Under purely communal change its share therefore equals the stayer weight s̄, not 1 (deviation D2-1).
- **Bounds on the communal share of the E population's change.**
  - (a) Exiters frozen at their E level: s_E·ρ.
  - (b) Exiters moved to the entrants' L level.
- **IPW for staying.** A key-level logit of staying on E-period covariates: log #papers, prior acceptances, NAME share, mean log authors, llm_topic share, first and last position shares, and modal topic50.
  - Discrimination is modest: AUC 0.67, effective sample 8,043 of 8,710 stayers.
  - The weights reproduce the E-population covariate means (`ipw_balance.csv`).
- **CIs.** Key-cluster bootstrap with 1,000 replicates. The same key draws are used for every specification, so the differences between partitions are joint.

## 2. Results

### 2.1 H2a: communal change dominates at the last list position (T2.1, F2.2, F2.3)

**Table T2.1 (main rows, NAME primary, paper-weighted).** Full table: `T2_1_decomposition.csv`.

| Partition | P_E → P_L | Stayers P_SE → P_SL | Exiters P_XE | Entrants P_NL | s_E / s_L | ρ | Kitagawa within / replacement / shift | Bounds (a, b) | ρ IPW |
|---|---|---|---|---|---|---|---|---|---|
| Last | .194 → .378 | .188 → .371 | .212 | .384 | .756 / .472 | **0.995** [0.943, 1.050] | 0.61 / 0.36 / 0.03 | 0.75, 0.98 | 0.977 [0.921, 1.035] |
| Any role | .195 → .378 | .191 → .340 | .202 | .397 | .604 / .252 | **0.816** [0.777, 0.857] | 0.35 / 0.59 / 0.06 | 0.49, 0.92 | 0.801 [0.759, 0.844] |
| First | .194 → .378 | .194 → .290 | .195 | .395 | .526 / .108 | **0.525** [0.414, 0.633] | 0.17 / 0.72 / 0.11 | 0.28, 0.79 | 0.523 [0.405, 0.633] |

At the last list position, stayer keys reproduce the whole population rise (Figure F2.3, left). In L, the three groups title at almost the same rate:

| Group (last position, L) | NAME share |
|---|---|
| Stayers | .371 |
| Entrants | .384 |
| Returners | .382 |

The entrant − stayer gap is +1.4 pp [−0.4, +2.9].

Exiters were not laggards in E. Their NAME share was .212 against .188 for stayers, a gap of +2.4 pp [−0.0, +5.1]. This reproduces the pilot's .214 vs .189.

Under author weighting (each key-period mean counts once), ρ_last = 0.897 [0.818, 0.980] and ρ_any = 0.699 [0.660, 0.736]. Both still meet the thresholds.

The literal Kitagawa within term is 0.61 [0.58, 0.65] of Δ at the last position and 0.35 [0.33, 0.37] for any role. These values mostly reflect the stayer weights s̄ = 0.61 and 0.43, not a generational residual (see D2-1). The bounds say that even if exiters would not have changed at all, stayers account for ≥ 0.75 of the last-position rise (bound a).

The pilot numbers reproduce:

| Partition | ρ here | Pilot |
|---|---|---|
| Last | 0.995 | ≈ 1.00 |
| Any role | 0.816 | 0.83 |
| First | 0.525 | 0.58 |

**Team types (F2.2, `team_type_shiftshare.csv`).** The within-team-type share of the rise is:

| Definition | Within team type | Within team type × size bin |
|---|---|---|
| Rolling | 0.995 [0.984, 1.007] | 0.893 [0.870, 0.915] |
| Fixed 2021–22 base (E = 2023) | 0.933 [0.908, 0.957] | 0.790 [0.746, 0.833] |
| Lag-1 | 0.984 [0.975, 0.993] | 0.878 [0.855, 0.899] |

Pilot: 0.99, 0.94, and 0.77–0.87 within type × size. Shifts in the mix of all-new, mixed and all-prior teams explain almost none of the rise. Adding team-size cells leaves 79–89% within cells.

### 2.2 H2b: a generational increment at the first list position

The first-position ρ is 0.47 lower than the last-position ρ: difference −0.470 [−0.602, −0.359]. The difference holds in every variant:

| Variant | ρ_first − ρ_last |
|---|---|
| Author-weighted | −0.353 [−0.507, −0.220] |
| NA pool | −0.426 [−0.587, −0.267] |
| Excluding 2026 | −0.474 [−0.670, −0.276] |
| L = 2026 only | −0.447 [−0.601, −0.310] |
| Partition-specific stayers | −0.374 [−0.551, −0.217] |
| Top-1% trim | −0.368 [−0.515, −0.236] |
| topic100-adjusted outcome | −0.558 [−0.782, −0.374] |
| Alias collapse | −0.243 [−0.344, −0.133] |

At the first position in L, entrant keys title with NAME at .395 against .290 for stayer keys, a gap of +10.6 pp [8.5, 12.6]. In E the two groups were identical (exiters .195, stayers .194).

Stayer keys make up only 10.8% of first-position rows in L. The first-position population rise is therefore carried largely by entrant keys, who title more fashionably than stayers in that position.

Figure F2.3 (middle) shows the stayer series bending away from the population after 2023. Under the alias collapse, which is an upper bound on stayer status (§2.6), ρ_first rises to 0.775 [0.686, 0.869]. The first position is the partition most sensitive to how keys are linked.

### 2.3 H2c: entrant co-authors carry part, but not most, of the stayers' change (T2.2)

**Part (i).** The model runs on stayer keys' author-paper rows, 2022–26 (61,610 rows, 8,710 keys):

`NAME ~ year dummies + share_new_coauthors + post × share_new_coauthors + log authors + llm_topic | key + topic100`

Here share_new_coauthors is the share of the other panel keys on the paper that are new in that year (rolling).

| Quantity | Estimate |
|---|---|
| E→L change at share_new = 0: mean(2025, 2026) − mean(2022, 2023) year effects | +6.15 pp [4.54, 7.76] |
| Ratio to the raw any-role population change (18.3 pp) | 0.34 [0.25, 0.43] |
| post × share_new_coauthors | +7.9 pp (se 1.2) |

The ratio is below the predicted 0.5 but above the falsification line: the CI excludes 0 and the point estimate is above 0.3×. Papers on which a stayer key is joined only by new co-authors rose about 8 pp more after 2024 than papers whose co-authors were all seen before.

Variants of part (i):

| Specification | Change at share_new = 0 | Ratio to population change |
|---|---|---|
| Lag-1 definition of a new co-author | 6.9 pp | 0.38 |
| Without topic100 FE | 8.5 pp | 0.47 [0.38, 0.56] |
| Rows weighted 1/#stayer keys on the paper | 6.0 pp | 0.33 |
| NA-pool papers only | 5.8 pp | 0.32 |

Part of the shortfall comes from the comparison being unlike for like. The model nets out topic100 composition, while the benchmark does not. Net of topic100 composition, the population rise is 10.7 pp, and the same change of 6.15 pp is 0.58 of it. This comparison is descriptive, not the pre-registered one.

**Part (ii).** Papers whose panel keys all appeared in an earlier year (rolling all-prior teams; 8.7% of E papers and 10.5% of L papers) went from .141 to .262. That is +12.1 pp [8.8, 14.8], or 0.66 [0.47, 0.81] of the population rise. In the pilot window 2023 → 2026 the figures are .169 → .290, +12.0 pp against +20.2 pp, a ratio of 0.60 [0.51, 0.76], which reproduces the pilot exactly.

### 2.4 H2d: style vs topic channel (F2.1)

**Markers.** Fixed before outcomes were examined:
- 52 of the 61 frozen style markers. The rest fall below 0.1% prevalence: elevat* and 8 snowclones.
- 33 topic markers: the 32 MiniLM topic100 clusters whose share changed by ≥ 1 pp, plus llm_topic.

**Fit.** In the any-role partition, within-stayer change regressed on population change across all 85 markers gives slope 0.923 [0.901, 0.946], intercept −0.001 and r = 0.992.

**Generational increment by channel.** G = 1 − b, where b is the through-origin slope within the channel.

| Channel | G (any-role partition) |
|---|---|
| Style | 0.166 [0.133, 0.200] |
| Topic | −0.047 [−0.068, −0.025] |
| Difference | 0.213 [0.176, 0.251] |

The aggregate-ratio version agrees: 0.162 vs −0.053.

Topic markers sit on or above the 45° line: stayer keys moved into growing topics, LLM topic above all, at least as fast as the population (LLM topic +36.7 pp within stayers against +35.1 pp overall). Style markers sit slightly below it, most visibly the NAME family. The slope below 1 comes from the NAME family: without those nine markers the overall slope is 1.037 [1.015, 1.057]. Even so, the style generational increment remains 0.133 [0.079, 0.194].

By partition:

| Partition | Slope | G_style | G_topic |
|---|---|---|---|
| Last | 1.026 | 0.014 [−0.034, 0.059] | −0.084 |
| First | 0.756 | 0.402 [0.309, 0.494] | 0.029 |

So the style increment, too, sits at the first list position.

### 2.5 H2e: the same mode before LLMs

**Main estimate.** With email keys, E = 2018 and L = 2020 (621 stayer keys in any role):
- **Stayers:** NAME went from .072 to .139.
- **Population:** NAME went from .101 to .157.
- **Within-stayer share:** ρ_any = 1.20 [0.71, 1.77].

**Compound titles (colon).** The population change is only +3.6 pp, so the ratio is imprecise: 1.13 [0.08, 2.66].

**Two-year windows (2017–18 → 2019–20).** Both outcomes clear the 0.5 threshold:

| Outcome | ρ |
|---|---|
| NAME | 1.08 [0.73, 1.49] |
| Compound | 1.12 [0.57, 1.75] |

**Uninformative partitions.** The last- and first-position estimates are too small to inform (`h2e_email.csv`):

| Partition | ρ (NAME) |
|---|---|
| Last | 0.69 [−0.21, 1.44] |
| First | 0.85 [−0.19, 2.05] |

**Selection caveat.** In this era exiters titled with NAME more than stayers in 2018 (+4.2 pp [1.7, 6.6]). The stayers who keep an unchanged email are therefore a selected group. A ρ above 1 partly reflects stayers catching up from a lower base.

### 2.6 Robustness of ρ (NAME primary; `T2_1_decomposition.csv`, `removal_extrapolation.csv`)

| Variant | Last | Any role | First |
|---|---|---|---|
| Main (paper-weighted) | 0.995 [0.943, 1.050] | 0.816 [0.777, 0.857] | 0.525 [0.414, 0.633] |
| Author-weighted | 0.897 [0.818, 0.980] | 0.699 [0.660, 0.736] | 0.545 [0.430, 0.656] |
| IPW for staying | 0.977 [0.921, 1.035] | 0.801 [0.759, 0.844] | 0.523 [0.405, 0.633] |
| NA-pool outcomes (camera-ready-free) | 0.990 [0.929, 1.058] | 0.840 [0.792, 0.892] | 0.564 [0.427, 0.713] |
| Non-LLM papers | 1.012 [0.926, 1.095] | 0.793 [0.729, 0.852] | 0.459 [0.281, 0.635] |
| Excluding 2026 (E 2021–22, L 2024–25) | 1.003 [0.918, 1.095] | 0.812 [0.752, 0.880] | 0.529 [0.348, 0.703] |
| L = 2025 only | 1.095 [1.000, 1.185] | 0.885 [0.818, 0.952] | 0.641 [0.451, 0.825] |
| L = 2026 only | 0.959 [0.902, 1.022] | 0.824 [0.781, 0.870] | 0.512 [0.369, 0.640] |
| 2023 → 2026 (pilot window) | 0.963 [0.895, 1.032] | 0.822 [0.769, 0.879] | 0.460 [0.280, 0.611] |
| Trim top 1% keys (> 16 papers; 844 keys) | 0.875 [0.795, 0.960] | 0.727 [0.681, 0.776] | 0.507 [0.392, 0.621] |
| topic100-adjusted outcome | 0.956 [0.874, 1.041] | 0.744 [0.681, 0.808] | 0.398 [0.201, 0.565] |
| Team-size-bin-adjusted outcome | 0.942 [0.881, 1.004] | 0.788 [0.741, 0.834] | 0.465 [0.330, 0.587] |
| Partition-specific stayers | 0.954 [0.878, 1.033] | 0.816 [0.777, 0.857] | 0.580 [0.421, 0.720] |
| Alias collapse (~First_Last1/2 merged) | 1.018 [0.970, 1.064] | 0.899 [0.865, 0.932] | 0.775 [0.686, 0.869] |
| Returners excluded from L | 0.999 | 0.804 | 0.511 |
| Held-out removal (20% × 200), extrapolated to full coverage | 0.996 | 0.818 | 0.528 |
| NAME strict | 0.992 [0.940, 1.048] | 0.812 [0.772, 0.854] | 0.510 [0.397, 0.618] |
| NAME loose | 0.998 [0.944, 1.054] | 0.828 [0.786, 0.869] | 0.568 [0.453, 0.677] |
| Compound (any colon or dash) | 0.963 [0.918, 1.007] | 0.851 [0.820, 0.886] | 0.688 [0.596, 0.779] |

Notes on the variants:
- **Held-out removal.** Dropping a further 10%, 20% or 30% of papers changes ρ by less than 0.01 on average; simulation SDs are 0.016, 0.014 and 0.034 for last, any and first at 20%. Extrapolated to full coverage, the bias from the held-out 20% split is negligible.
- **Prolific keys.** Trimming the 1% most prolific keys lowers ρ_last to 0.875, so those keys changed slightly more than average. The H2a thresholds still hold.
- **Topic composition.** Net of topic100 composition, the population rise is 10.7 pp rather than 18.3 pp. The communal pattern holds within topic: last 0.96, any 0.74.

### 2.7 Supporting tests (T2.3; exploratory)

#### S2.1 Within-paper retitling (`s2_1_resubmission.csv`)

**Pairs.**
- **Matching rule:** a shared declared key, a gap of 1–2 years, bge cosine ≥ 0.95 or MiniLM ≥ 0.85, a non-accepted source, and greedy one-to-one matching.
- **Count:** this yields 297 pairs with destination year ≥ 2024, exactly the pilot's count.
- **Purity:** the purity estimate is 0.87, from matches per source paper of 0.26% for accepted sources against 1.96% for non-accepted ones. Under a strict rule (bge ≥ 0.97 or MiniLM ≥ 0.90) it is 0.98.
- **Identical titles:** only 1.3% of pairs have identical titles. This is consistent with the export keeping one submission per paper family, so the pairs that survive are selected on retitling.

**Result.**
- **Mean ΔNAME:** within these pairs it is 0.000 (se 0.025), with 28 adds and 28 drops.
- **Implied drift:** the population drift implied by the pairs' years is +7.2 pp.
- **Difference:** −7.2 pp (se 2.5, p = 0.005), with an MDE of 7.1 pp.
- **Other rules and outcomes:**

| Sample | Mean change | Implied drift |
|---|---|---|
| Strict rule (n = 164) | +1.8 pp (se 2.9) | +6.9 pp |
| Destinations ≤ 2023 (n = 76) | 0.000 (se 0.042) | +2.5 pp |
| Compound outcome | +3.7 pp (se 3.2) | +9.7 pp |

**Statement.** The statement is limited to this: even among retitled papers, NAME is not added on net. Add and drop counts are descriptive only. They are not behavioural transition rates, because the pairs are selected on retitling.

#### S2.2 Future-tie placebo (`s2_2_future_tie.csv`, supplementary `fig_S2_2_future_tie`)

**Sample.** Clean focal papers, T = 2023–25: 6,572 rows, 2,358 keys. Past-collaborator exposure covers a median of 9 collaborators, future-collaborator exposure a median of 4.

**NAME, primary specification (year + topic100 FE).** Past exposure is no larger than future exposure, which fits homophily rather than tie contagion:

| Exposure | Coefficient (se) |
|---|---|
| Past | −0.007 (0.026) |
| Future | +0.067 (0.025) |
| Past − future | −0.075 (0.037) |

The MDE for the past coefficient is 0.073. The pilot specification without topic FE reproduces the pilot exactly: past 0.044 (0.028) vs future 0.117 (0.026). Compound titles behave the same way: past 0.008 vs future 0.029.

**Positive control (llm_topic outcome and exposure).** It is clearly detected in the specification without topic FE: past 0.221 (0.030), future 0.265 (0.029). With topic100 FE it is mostly absorbed (0.022, se 0.016), because llm_topic is partly defined by topic100 clusters.

**Reading.** The result is framed only as failing to support a tie-contagion account. In the full, non-clean sample, past and future exposure are equal (0.056 vs 0.053).

## 3. Deviations from PLAN.md (logged)

- **D2-1 Definition of the within-stayer share.**
  - H2a, H2b and H2d are evaluated on ρ = ΔP_S/Δ. This is how the pilot numbers behind the thresholds were computed (1.00 / 0.83 / 0.58), and it is the "within/pop" of H2d.
  - The literal first-term share of the plan's Kitagawa formula equals s̄·ρ. Under purely communal change it equals the stayer weight s̄, so the 0.70 and 0.60 thresholds cannot be meant for it.
  - All three Kitagawa terms are still reported in T2.1, together with both bounds.
- **D2-2 Stayer status.** Stayer status comes from any-role presence, as in the pilot. Partition-specific stayer status is a robustness check.
- **D2-3 First and last positions.**
  - Both are defined on the full declared list. Rows whose last or first key is not a profile key drop out of that partition.
  - This affects 10% of 2021 papers and 4–5% of 2022–23 papers.
- **D2-4 Returners.** For the exact identity, returners stay in the L "others" group. ρ does not depend on this choice; a variant without returners is reported.
- **D2-5 Fixed-base team type.** This definition uses E = 2023 only, because its 2021–22 base window overlaps E.
- **D2-6 IPW.**
  - Specification: a key-level L2 logit (C = 10), with p clipped to [0.02, 0.98] and weights capped at the 99th percentile.
  - Propensities are held fixed across bootstrap replicates, so the IPW CIs ignore propensity-estimation error.
- **D2-7 H2c model.**
  - The model adds a main effect of share_new_coauthors, which the plan's formula omits.
  - It uses rows from 2022–26, because in 2021 every key is new under the rolling definition.
  - The E→L contrast is mean(2025, 2026) − mean(2022, 2023) year effects. Solo-key papers get share 0.
  - The benchmark is the raw any-role population change, as pre-registered. The topic-adjusted benchmark is descriptive.
- **D2-8 H2d markers and statistic.**
  - Minimum prevalence is 0.1% in E∪L, the rule announced in API.md §4.6. Topic markers are MiniLM topic100 clusters with |Δshare| ≥ 1 pp, plus llm_topic.
  - G = 1 − the through-origin slope per channel; the aggregate-ratio version is also reported.
  - The marker set is held fixed across bootstrap replicates.
- **D2-9 H2e windows.**
  - The windows are single years, E = 2018 and L = 2020, following "2018→2020".
  - Any role is primary, since the plan names no partition. Two-year windows are a robustness check.
  - IPW is not applied in the email era.
- **D2-10 S2.1 matching.**
  - The source pool is NA, which adds desk-rejected papers; the pilot used rejected and withdrawn.
  - Pairs follow the pilot's greedy ordering: best bge match first, then the union rule.
  - Two additions: a strict-rule variant, and a same-key other-papers context. For that context, the shared keys' other papers changed by +2.5 pp (se 2.0, n = 217).
- **D2-11 S2.2 specification.**
  - The primary specification adds topic100 FE, following the C15 operationalisation ("cluster and year controls"). The pilot specification is also reported.
  - The positive control is read off the no-topic-FE specification (see §2.7).
- **D2-12 Team-type bootstrap.** The team-type and all-prior bootstraps cluster on the paper's last-position key.
- **D2-13 Removal simulation.** It assumes discovery coverage c0 = 0.8 and adds 10% and 30% removal as a linearity check.
- **D2-14 Extra variants.** Added beyond the plan: L = 2025 and L = 2026 cohorts (PLAN §0), the non-LLM subset, the 2023 → 2026 pilot window, and a team-size-bin-adjusted outcome.

## 4. Limitations

- **Keys are not people.**
  - A person with two profiles creates a false exit plus a false entry.
  - Different people who share a name stay distinct, unless aliases are collapsed.
  - Collapsing trailing-digit aliases is an upper bound on stayer status. It mostly raises ρ_first (0.53 → 0.78), because false stayers created by common names are really entrants.
  - So the first-position result is the most key-sensitive. Even so, its difference from the last position holds under the alias collapse (−0.24 [−0.34, −0.13]).
- **Entrant status is left-censored at 2021.** Returners (6,949 keys) absorb part of this. The held-out 20% split is shown by simulation to matter little, but cross-split histories remain unobserved.
- **Stayers are selected.** IPW balances observables only, with AUC 0.67. The bounds are wide for the any-role and first partitions (0.49–0.92 and 0.28–0.79).
- **Communal does not mean tool-free.** The analysis says *who* changed, not *why*. Communal change is fully compatible with the same keys adopting writing tools after 2023. Topic composition accounts for about 40% of the raw population rise (10.7 pp net of topic100 composition against 18.3 pp); D1 handles content.
- **Camera-ready contamination** affects accepted papers. All main results replicate on NA-pool outcomes.
- **H2e** uses email keys with linkage breaks and a selected, lower-baseline stayer group.
- **S2.1** is selected on retitling and has an MDE of 7.1 pp.
- **S2.2** has modest power (MDE 0.073 per unit of exposure) and can only fail to support tie contagion. It does not establish homophily, and it does not rule out influence.

## 5. Files (`outputs/d2_carriers/`)

**Figures** (PDF, PNG and CSV for each):
- `fig_F2_1_marker_scatter`: F2.1.
- `fig_F2_2_decomposition`: F2.2.
- `fig_F2_3_levels`: F2.3.
- `fig_S2_2_future_tie`: supplementary.

**Tables:**
- T2.1: `T2_1_decomposition.csv`, plus `decomposition_long.csv`.
- T2.2: `T2_2_author_fe.csv`.
- T2.3: `T2_3_support.csv`, with detail in `s2_1_resubmission.csv` and `s2_2_future_tie.csv`.

**Other outputs:**
- Team types: `team_type_shiftshare.csv`, `team_type_rates.csv`.
- Removal simulation: `removal_simulation.csv`, `removal_extrapolation.csv`.
- IPW and H2e: `ipw_balance.csv`, `h2e_email.csv`.
- Markers: `markers_changes.csv`, `markers_selection.csv`.
- Panel: `panel_summary.csv`, `panel_info.json`, `panel_rows.parquet`, `panel_papers.parquet`, `email_rows.parquet`.
- Resubmission pairs: `resub_pairs.parquet`.
- Per-script JSON: `shiftshare_results.json`, `markers_results.json`, `support_results.json`.
- Bootstrap draws: `*_boot_draws.npz`.
- Logs: `d2_*.log`.
- Machine-readable summary of everything above: `results.json`.

**Run order:**

```bash
cd research/titles/src
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_panel
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_shiftshare 1000
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_markers 1000
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_support
/home/user/venv/bin/python -m analyses.d2_collect
```

Total run time is about 3 minutes.
