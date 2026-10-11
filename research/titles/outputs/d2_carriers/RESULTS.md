# D2. Who carries the fashion: communal vs generational change

*WP6. Scripts: `src/analyses/d2_panel.py`, `d2_shiftshare.py`, `d2_markers.py`, `d2_ident.py`, `d2_support.py`, `d2_collect.py`. Machine-readable estimates: `results.json`. Revised after a three-auditor review (code, identification, reporting); every change is listed in the [Audit response](#audit-response) and in `outputs/audit/d2/fix_log.md`. The summary table is written by `d2_collect.py` from the output files. The other numbers were re-checked against the outputs by `outputs/audit/d2/v02_check_numbers.py`.*

Language follows the README boundaries throughout. A declared profile key is an exact-ID key, not a verified person. "First" and "last list position" are partition labels only and say nothing about seniority or supervision. "Tenure" below means only how long a key has been present in the panel. Every association is descriptive; no influence claim is made.

## Summary

**What holds (descriptive).** Papers that carry a key present in both windows (a stayer key) rose in NAME use as much as the population did. At the last list position, stayer keys' papers moved from 18.8% to 37.1% NAME, against 19.4% to 37.8% for the population. The stayer-to-population change ratio is ρ_last = 0.995 [0.943, 1.050]. Pooled over list positions ρ_any = 0.816 [0.777, 0.857], and at the first position ρ_first = 0.525 [0.414, 0.633]. Two-way (key, paper) CIs are almost the same width. Entrant keys hold most L-period papers, so in the Kitagawa accounting stayers' own change makes up 61% (last), 35% (any role) and 17% (first position) of the population change.

**What D2 cannot identify.** A title is shared by every co-author. In L, 69% of the papers with a stayer key at the last position have an entrant key at the first position. Take a world where only papers led by a newcomer first key changed and every other paper kept its E style. With the observed co-authorship, that purely generational world gives ρ_last 0.88–0.93 and ρ_any 0.78–0.82. Both clear the H2a thresholds. The observed ρ_last exceeds this null by 0.07–0.11. ρ_any does not clearly exceed it: +0.04 (two-way CI −0.01 to 0.09) against the entrant-first null, and −0.01 against the entrant-or-returner-first null. So H2a's prediction is met on ρ, but it does not show that "the same keys changed". The earlier summary sentence "the rise happened inside the same declared profile keys" is withdrawn.

**Where the rise sits.** On papers with no newcomer key, the rise is small. Teams made only of stayer keys rose +1.2 pp, 0.06 [−0.14, 0.28] × the population change. Teams whose keys were all seen in 2021–22 changed −0.07 [−0.42, 0.24] ×. Last-position stayers on L papers without an entrant co-author rose 0.22 [0.07, 0.37] ×, against 1.14 [1.07, 1.20] × on L papers with an entrant first author. Looser and symmetric definitions give larger ratios: 0.70 [0.49, 0.90] × for teams whose keys all appeared in the previous year, and 0.55 [0.42, 0.69] × for papers whose first and last keys are both stayers. The rise is graded by how new the team's keys are. Selection is an unresolved alternative: groups of keys that adopted the style may also be the ones adding new co-author keys, and static teams differ in topic and size. Size-bin and topic100 controls widen these CIs but do not remove the gradient.

**First list position.** Entrant first keys in L use NAME 10.6 pp more often than stayer first keys. Within the same last-position key, with size-bin and topic100 FE, the gap is 4.9 [2.2, 7.6] pp. D2 stayers have at least three years of panel presence, so this contrast mixes cohort with tenure. With a symmetric two-year lookback, a newcomer premium at first position is absent in 2023 and appears from 2024 (change +4.3 [0.3, 8.4] pp). Under that definition, prior first keys changed 0.86 [0.72, 1.01] × as much as the first-position population.

**Style vs topic (H2d).** Within-stayer change tracks topic markers at or above the population rate but style markers more slowly: G_style 0.17 [0.13, 0.20] vs G_topic −0.05 [−0.07, −0.03] in the any-role partition. This contrast is the most informative D2 result. A shared-outcome null predicts the same ratio for every marker, so a difference between channels cannot come from co-authorship composition. The contrast holds with equal marker weights (median per-marker ρ: style 0.84, topic 1.05) and when both llm_topic and the NAME family are dropped (0.19 [0.13, 0.26]). It is concentrated at the first list position: G_style is 0.40 there and 0.01 at the last position. The slope criterion (slope ≥ 0.7) is not diagnostic: a random paper subset gives 1.00 and the generational null gives 0.78.

**Pre-LLM era (H2e).** The result is inconclusive. NAME ρ_any (email keys, 2018 → 2020) is 1.20 [0.71, 1.77], which is 0.51 [0.02, 1.07] above its shared-outcome null. The compound outcome is imprecise. The literal pre-registered Kitagawa share is 0.26, below the 0.3 falsification line, but that statistic cannot exceed the stayer weight s̄ = 0.22 even under purely communal change.

**Supporting tests.**
- **S2.1:** retitled resubmissions do not add NAME on net (0.000, se 0.025). The gap against the raw population drift (−7.2 pp, p = 0.005) shrinks against content-fixed benchmarks: −4.8 pp (p = 0.057) against topic100-adjusted drift and −3.4 pp (p = 0.33) against the same keys' other papers. What the test supports is that NAME is not added within a project.
- **S2.2:** past-collaborator exposure is not larger than future-collaborator exposure. The llm_topic positive control is not detected in the primary specification and shows the same ordering where it is detected. So the test is inconclusive between tie contagion and homophily.

**Overall.** D2 does not support the thesis bullet "the same people changed … mostly within incumbent authors" (PLAN §1). The data fit change carried by new projects and newcomer-containing teams, spreading to incumbents' papers through mixed teams. Who chooses a title on a mixed team is not identified. The style-vs-topic contrast and the first-position newcomer premium are the defensible D2 findings.

<!-- BEGIN AUTO: summary_table (written by d2_collect.py; do not edit by hand) -->
| Hypothesis | Pre-registered prediction | Estimate (95% CI) | Falsified? | Verdict | one-sided p (Holm) |
|---|---|---|---|---|---|
| H2a communal dominance | within-stayer share: last ≥ 0.70, any role ≥ 0.60 | ρ_last 0.995 [0.943, 1.050] (two-way [0.940, 1.050]); ρ_any 0.816 [0.777, 0.857] (two-way [0.768, 0.863]). Literal Kitagawa share 0.61 [0.58, 0.65] / 0.35 [0.33, 0.37]. Shared-outcome null: ρ_last 0.88–0.93, ρ_any 0.78–0.82 | no (upper CI ≫ 0.5) | **not identified**: met on ρ (D2-1) but not on the literal share; a purely generational world also meets it | 0.001 (0.005) |
| H2b first-position increment | ρ_first ≤ ρ_last − 0.2; entrants > stayers at first position in L | ρ_first − ρ_last = −0.470 [−0.602, −0.359] (two-way [−0.582, −0.358]); entrant − stayer 10.6 [8.5, 12.6] pp, within the same last key 4.9 [2.2, 7.6] pp; symmetric-lookback prior-first ratio 0.86 [0.72, 1.01] | no | **supported on the pre-registered groups; magnitude not robust** | 0.001 (0.005) |
| H2c not driven by entrant co-authors | (i) change at share_new = 0 ≥ 0.5 × population; (ii) all-prior teams ≥ 0.5 × population | (i) +6.15 pp [3.45, 8.85] = 0.34 [0.19, 0.48] × 18.3 pp (two-way SE; lag-1 0.38); (ii) rolling 0.66 [0.49, 0.85], lag-1 0.70 [0.49, 0.90], fixed 2021–22 base −0.07 [−0.42, 0.24] (n_L = 211) | no (CI of (i) excludes 0; margin above 0.3× not significant) | **not supported**: (i) contradicted (p = 0.015 against ≥ 0.5); (ii) met on the point estimate under rolling and lag-1 only | 0.312 (0.312) |
| H2d style vs topic | slope ≈ 1 (≥ 0.7); G_style > G_topic | slope 0.923 [0.901, 0.946] (random-subset benchmark 1.00, null 0.78); G_style 0.166 [0.133, 0.200] vs G_topic −0.047 [−0.068, −0.025]; difference 0.213 [0.176, 0.251]; without llm_topic and NAME family 0.19 [0.13, 0.26]; equal-weight median ρ style − topic −0.21 [−0.26, −0.14] | no | **supported (channel contrast); slope criterion not diagnostic** | 0.001 (0.005) |
| H2e pre-LLM (email keys, 2018→2020) | NAME and colon within share ≥ 0.5 | ρ_any NAME 1.20 [0.71, 1.77], compound 1.13 [0.08, 2.66]; author-weighted 0.79 / 0.37; literal Kitagawa share 0.26 [0.15, 0.39] / 0.25 [0.02, 0.57] (s̄ = 0.22); ρ_any − null 0.51 [0.02, 1.07] | yes on the literal share (< 0.3), which cannot exceed s̄ even under purely communal change; no on ρ | **inconclusive** | 0.061 (0.122) |
<!-- END AUTO: summary_table -->

The p-values are one-sided against each hypothesis's falsification boundary:
- H2a: ρ_last ≤ 0.5 (key-cluster bootstrap).
- H2b: ρ_first − ρ_last ≥ 0 (joint bootstrap).
- H2c: change at share_new = 0 ≤ 0.3 × the population change. This uses a t-test with two-way CGM SEs. Before the audit the null was "change ≤ 0".
- H2d: G_style − G_topic ≤ 0.
- H2e: ρ_any ≤ 0.3 for NAME or for compound. This is an intersection-union test: the larger of the two p-values.

Bootstrap p-values have a floor of 1/1001. Holm is applied over H2a–H2e. A small p for H2a says only that ρ_last is above 0.5. It does not test communal against generational change; see "not identified".

## 1. Design

**Panel.**
- Main panel: `native_id_kind == 'profile'` keys on U papers, 2021–26, one row per (key, paper). That is 198,640 rows and 89,115 keys (`panel_rows.parquet`, `panel_summary.csv`).
- Email-era panel (H2e): email keys, 2017–20. That is 17,572 rows and 11,507 keys.
- Profile-key coverage by year:

  | Position | 2021 | 2022 | 2023 | 2024–26 |
  |---|---|---|---|---|
  | Last | 89.9% | 95.2% | 96.4% | ≥ 99.4% |
  | First | 93.3% | 98.3% | 98.8% | — |

  A paper whose last (first) declared position is not a profile key drops out of that partition.
- Papers with any email-keyed list position number 817 (2021), 399 (2022), 497 (2023), 173 (2024) and none after (D2-C12). Such a person is invisible to the profile panel.
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
- Paper-level team types (all-prior / mixed / all-new) under four definitions:
  - rolling: key seen in any earlier panel year;
  - lag-1: seen in the previous year;
  - symmetric two-year lookback: seen in y−1 or y−2, for papers from 2023 on;
  - fixed base: seen in 2021–22, for papers from 2023 on.

**Statistics.**
- **Stayer-to-population change ratio.** This is the statistic used for H2a, H2b and H2e (deviation D2-1), and the "within/pop" of H2d:

  ρ = (P_SL − P_SE) / (P_L − P_E)

  ρ can exceed 1, so it is a ratio, not a share.
- **The plan's Kitagawa identity:**

  Δ = s̄(P_SL − P_SE) + (1 − s̄)(P_OL − P_XE) + (s_L − s_E)(P̄_S − P̄_O)

  Its first-term share equals s̄·ρ, so even under purely communal change it cannot exceed the stayer weight s̄. Both statistics are reported in T2.1.
- **Scenario communal shares of the population change.** These are not bounds on ρ.
  - (a) Exiters frozen at their E level: s_E·ρ.
  - (b) Exiters moved to the entrants' L level.
- **Shared-outcome generational null (audit ID-1).** The indicator outcomes `null_Nfirst`, `null_NRfirst` and `null_anyN` are 0 on all E papers. In L they are 1 only on papers whose first key is an entrant, whose first key is an entrant or returner, or which carry any entrant key. Their ρ is the ratio stayers would show if their own style had stayed fixed and only newcomer-carried papers had changed, given the observed co-authorship. This ratio does not depend on the size of the change. The differences between the observed ρ and the null ρ use the same bootstrap draws.
- **Newcomer-free contrasts (audit ID-2).** The NAME change on papers whose team excludes newcomers, under several definitions, as a ratio to the population change. CIs come from a last-position-key cluster bootstrap. There is also an LPM version with size-bin and topic100 FE, compared with the same-model population change (`T2_4_newcomer_free.csv`).
- **IPW for staying.** A key-level logit of staying on E-period covariates: log #papers, prior acceptances, NAME share, mean log authors, llm_topic share, first and last position shares, and modal topic50. AUC is 0.67, and the effective sample is 8,043 of 8,710 stayers.
- **CIs.**
  - Key-cluster bootstrap with 1,000 replicates, the same key draws for every specification.
  - For the headline statistics: key, paper and row bootstraps (500 replicates each), the Cameron–Gelbach–Miller two-way SE (V_key + V_paper − V_row), and a conservative pigeonhole (key × paper) bootstrap (`T2_1b_twoway_se.csv`).
  - Paper-level contrasts cluster on the last-position key.

## 2. Results

### 2.1 H2a: papers carrying stayer keys rose as much as the population; communal change is not identified (T2.1, T2.4, F2.2, F2.3)

**Table T2.1 (main rows, NAME primary, paper-weighted).** Full table: `T2_1_decomposition.csv`.

| Partition | P_E → P_L | Stayers P_SE → P_SL | Exiters P_XE | Entrants P_NL | s_E / s_L | ρ (key-cluster CI) | ρ two-way CI | Kitagawa within / replacement / shift | Scenario (a), (b) | ρ IPW |
|---|---|---|---|---|---|---|---|---|---|---|
| Last | .194 → .378 | .188 → .371 | .212 | .384 | .756 / .472 | **0.995** [0.943, 1.050] | [0.940, 1.050] | 0.61 / 0.36 / 0.03 | 0.75 [0.71, 0.79], 0.98 | 0.977 [0.921, 1.035] |
| Any role | .195 → .378 | .191 → .340 | .202 | .397 | .604 / .252 | **0.816** [0.777, 0.857] | [0.768, 0.863] | 0.35 / 0.59 / 0.06 | 0.49 [0.47, 0.52], 0.92 | 0.801 [0.759, 0.844] |
| First | .194 → .378 | .194 → .290 | .195 | .395 | .526 / .108 | **0.525** [0.414, 0.633] | [0.419, 0.630] | 0.17 / 0.72 / 0.11 | 0.28 [0.22, 0.33], 0.79 | 0.523 [0.405, 0.633] |

The two-way CGM SEs are 0.028, 0.024 and 0.054 for last, any role and first, against key-cluster SEs of 0.028, 0.021 and 0.056. The conservative pigeonhole bootstrap gives 0.044, 0.034 and 0.091; its CI for ρ_last is [0.909, 1.084].

At the last list position, stayer keys' papers reproduce the whole population rise (Figure F2.3, left). In L, the three groups title at almost the same rate:

| Group (last position, L) | NAME share |
|---|---|
| Stayers | .371 |
| Entrants | .384 |
| Returners | .382 |

The entrant − stayer gap is +1.4 pp [−0.4, +2.9]. Exiters were not laggards in E: .212 against .188 for stayers, a gap of +2.4 pp [−0.0, +5.1]. The pilot had .214 vs .189.

Under author weighting (each key-period mean counts once), ρ_last = 0.897 [0.818, 0.980] and ρ_any = 0.699 [0.660, 0.736].

**The literal pre-registered statistic.** The literal Kitagawa within-stayer share is 0.61 [0.58, 0.65] at the last position and 0.35 [0.33, 0.37] for any role. Both are below the 0.70 / 0.60 thresholds, so on the plan's literal statistic H2a is not met. That statistic is capped at s̄ (0.61 and 0.43) even under purely communal change, which is why the thresholds were evaluated on ρ (deviation D2-1, logged before the audit). The upper CI of the literal share at the last position (0.646) is still above 0.5, so H2a is not falsified on either statistic.

**Scenario values.** If exiters would not have changed at all, stayer keys' change would make up 0.75 [0.71, 0.79] of the E population's last-position change; this is scenario (a). If exiters had moved to the entrants' L level, the share would be 0.98; this is scenario (b).

**The shared-outcome null (audit ID-1).** A title is shared by all co-authors, so a key-level ratio cannot say whose choice changed. Of the 11,503 L papers with a stayer key at the last position, 7,889 (69%) have an entrant first key. The table shows the ρ that a world without any change by non-newcomer-led papers would produce:

| Partition | Observed ρ | Null: only entrant-first papers change | Null: entrant- or returner-first papers | Null: papers with any entrant key | Observed − entrant-first null |
|---|---|---|---|---|---|
| Last | 0.995 | 0.882 | 0.927 | 0.958 | +0.113 [0.060, 0.168]; two-way [0.058, 0.167] |
| Any role | 0.816 | 0.776 | 0.822 | 0.898 | +0.040 [0.000, 0.082]; two-way [−0.007, 0.087] |
| First | 0.525 | 0 | 0 | 0.752 | — |

Against the entrant- or returner-first null, the difference is +0.068 [0.017, 0.122] at the last position and −0.007 [−0.047, 0.033] for any role. The NA pool gives the same picture: last +0.107 [0.044, 0.172] against the entrant-first null; any role +0.013 [−0.038, 0.063] against the entrant- or returner-first null.

So the H2a thresholds are met even with zero communal change, and the prediction is not diagnostic. What ρ adds beyond the null is a modest last-position excess and a first-position ratio of 0.525, well above the 0 the first-author null implies. Pure first-author generational change is therefore rejected. Mixed teams may still carry the change.

**Newcomer-free contrasts (T2.4, F2.2c).** Change from E to L as a ratio to the population change on the same papers (18.3 pp; 17.5 pp for the rows with E = 2023):

| Papers | n_E → n_L | NAME E → L | Ratio (95% CI) | With size-bin + topic100 FE |
|---|---|---|---|---|
| All-stayer teams (every declared position a stayer key) | 1,304 → 532 | .165 → .177 | 0.06 [−0.14, 0.28] | 0.09 [−0.32, 0.50] |
| All keys seen in 2021–22 (fixed base; E = 2023) | 384 → 211 | .169 → .156 | −0.07 [−0.42, 0.24] | −0.12 [−0.85, 0.62] |
| Last = S; L papers with no entrant or returner key | 4,728 → 532 | .188 → .177 | −0.06 [−0.26, 0.14] | 0.04 [−0.34, 0.41] |
| Last = S; L papers with no entrant key | 4,728 → 1,163 | .188 → .229 | 0.22 [0.07, 0.37] | 0.38 [0.10, 0.66] |
| Repeated stayer dyad (co-authored in E and L); L without entrant key | 3,214 → 728 | .205 → .232 | 0.15 [−0.06, 0.34] | 0.34 [−0.02, 0.70] |
| All keys seen in the prior two years (symmetric; E = 2023) | 384 → 2,190 | .169 → .262 | 0.53 [0.29, 0.77] | 0.48 [0.02, 0.94] |
| First and last both stayer keys (distinct) | 2,736 → 1,922 | .189 → .290 | 0.55 [0.42, 0.69] | 0.46 [0.18, 0.75] |
| Last = S and all keys seen the year before (symmetric lag-1) | 362 → 1,063 | .135 → .261 | 0.69 [0.44, 0.92] | 0.74 [0.22, 1.26] |
| All keys seen the year before (lag-1 all-prior) | 441 → 1,580 | .132 → .259 | 0.70 [0.49, 0.90] | 0.89 [0.45, 1.32] |
| *Reference:* last = S, all L papers | 4,728 → 11,503 | .188 → .371 | 1.00 [0.94, 1.06] | 0.91 [0.74, 1.07] |
| *Reference:* last = S; L papers with an entrant first author | 4,728 → 7,889 | .188 → .396 | 1.14 [1.07, 1.20] | 1.12 [0.93, 1.30] |

The ratio rises with how new the team's keys are allowed to be:
- teams whose keys all predate the windows, or are all stayers: about 0;
- teams whose keys all appeared one or two years earlier: 0.5–0.7.

The first four "no entrant" rows compare L papers without entrants against all E papers of the same stayers. That asymmetry favours finding a smaller change. The symmetric rows (lag-1, two-year lookback) give 0.53–0.70.

On NA-pool papers (camera-ready-free) the pattern is the same:
- all-stayer teams: 0.03 [−0.25, 0.30];
- last = S with no entrant key: 0.20 [0.01, 0.39];
- lag-1 all-prior teams: 0.65 [0.35, 0.91].

The newcomer-free teams are a small, selected part of L: 532 of 24,364 L papers are all-stayer teams. They may differ in subfield in ways the topic100 FE miss. They may also be groups of keys that did not adopt the style and therefore did not add new keys. These contrasts locate the rise; they do not identify who chose the titles.

**Team-type composition (F2.2d, `team_type_shiftshare.csv`).** This is an accounting statement only. The share of the paper-level rise that falls within team-type cells is:

| Definition | Within team type | Within team type × size bin |
|---|---|---|
| Rolling | 0.995 [0.984, 1.007] | 0.893 [0.870, 0.915] |
| Fixed 2021–22 base (E = 2023) | 0.933 [0.908, 0.957] | 0.790 [0.746, 0.833] |
| Lag-1 | 0.984 [0.975, 0.993] | 0.878 [0.855, 0.899] |

Pilot: 0.99, 0.94, and 0.77–0.87 within type × size. Shifts in the mix of all-new, mixed and all-prior teams explain little of the rise.

### 2.2 H2b: a first-position contrast that mixes cohort and tenure

The first-position ρ is 0.47 lower than the last-position ρ: difference −0.470 [−0.602, −0.359]. The two-way CGM CI is [−0.582, −0.358] and the conservative pigeonhole CI is [−0.650, −0.269]. The difference excludes 0 in every variant:

| Variant | ρ_first − ρ_last |
|---|---|
| Author-weighted | −0.353 [−0.507, −0.220] |
| NA pool | −0.426 [−0.587, −0.267] |
| Excluding 2026 | −0.474 [−0.670, −0.276] |
| L = 2026 only | −0.447 [−0.601, −0.310] |
| Partition-specific stayers | −0.374 [−0.551, −0.217] |
| Top-1% trim | −0.368 [−0.515, −0.236] |
| topic100-adjusted outcome | −0.558 [−0.782, −0.374] |
| Papers with an email-keyed position dropped | −0.459 [−0.591, −0.347] |
| Restricted alias collapse (≤ 3 keys, ≤ 40 papers per alias-year) | −0.394 [−0.505, −0.276] |

The full trailing-digit alias collapse is an extreme upper bound on stayer status, not a robustness check. It merges up to 45 keys into one alias (5,399 aliases, 16,259 keys) and creates alias-years above the 40-paper cap. Under it, the difference shrinks to −0.243 [−0.344, −0.133], whose CI includes gaps smaller than the predicted 0.2, and ρ_first rises to 0.78 [0.69, 0.87].

**Entrants vs stayers at the first position.** In L, entrant keys at the first position title with NAME at .395 against .290 for stayer keys: +10.6 pp [8.5, 12.6]. In E the two groups were identical (exiters .195, stayers .194). D2 stayers need presence in both 2022–23 and 2025–26, so this contrast compares new keys with keys of at least three years' tenure. Within L papers with distinct first and last keys (`h2b_first_position.csv`):

| Specification | Entrant-first − stayer-first |
|---|---|
| Raw | 10.3 pp [8.3, 12.4] |
| Size-bin + topic100 FE | 7.8 pp |
| Same last-position key (last-key FE) | 6.7 pp |
| Last-key + size-bin + topic100 FE | 4.9 pp [2.2, 7.6] |

**Symmetric two-year lookback** (new = key not seen in y−1 or y−2; `h2b_newcomer_premium_by_year.csv`). The newcomer premium at the first position is:

| Year | Raw | Within last key + size + topic |
|---|---|---|
| 2023 | −0.2 pp | −1.3 pp |
| 2024 | +4.5 pp | +1.5 pp |
| 2025 | +4.2 pp | +1.3 pp |
| 2026 | +3.8 pp | +2.1 pp |

The change in the premium from 2023 to 2025–26 is +4.3 pp [0.3, 8.4] (last-key, year, size and topic FE). Under this definition, prior first keys changed 0.86 [0.72, 1.01] × as much as the first-position population (2023 → 2025–26). The newcomer share at the first position barely moved (.734 → .701).

So a post-2023 newcomer premium at the first position exists, of roughly 2–5 pp within the same last-position key. The D2 magnitude (ρ_first 0.525; difference −0.47) is partly a tenure contrast.

Figure F2.3 (middle) shows the first-position series by group. Returners are now plotted; the "all panel rows" line includes them. The 2024 first-position level of all rows (.266) lies above stayers (.234) and exiters (.228) because returners (2,153 rows at .290) are part of it.

### 2.3 H2c: most of the stayers' rise co-occurs with new co-authors (T2.2, T2.2b)

**Part (i).** The model runs on stayer keys' author-paper rows, 2022–26 (61,610 rows, 8,710 keys):

`NAME ~ year dummies + share_new_coauthors + post × share_new_coauthors + log authors + llm_topic | key + topic100`

Here post = year ≥ 2024. Several stayer keys often share one paper and its outcome, so SEs are now two-way clustered by key and paper (CGM). The key-only SE (0.0082) was about 40% too small.

| Quantity | Estimate |
|---|---|
| E→L change at share_new = 0: mean(2025, 2026) − mean(2022, 2023) year effects | +6.15 pp [3.45, 8.85] (two-way se 1.38) |
| Ratio to the raw any-role population change (18.3 pp) | 0.34 [0.19, 0.48] |
| Same ratio, adding the uncertainty of the population change | [0.19, 0.49] |
| Test of the prediction (H0: ratio ≥ 0.5) | p = 0.015, so the prediction is contradicted |
| Test at the falsification line (H0: ratio ≤ 0.3) | p = 0.31, so the margin above 0.3× is not significant |
| post × share_new_coauthors, rolling definition | +7.9 pp (se 1.9) |
| post × share_new_coauthors, lag-1 definition | +4.4 pp (se 1.9) |

The rolling share_new has a lookback that grows with the year (mean on stayer rows 0.61, 0.53, 0.43, 0.42, 0.40 in 2022–26), against the symmetric lag-1 definition (0.61, 0.61, 0.53, 0.54, 0.51). Part of the rolling interaction is therefore censoring.

Variants of part (i), each with a two-way CI of the ratio (the population change held fixed):

| Specification | Change at share_new = 0 | Ratio [95% CI] |
|---|---|---|
| Primary (rolling) | 6.15 pp | 0.34 [0.19, 0.48] |
| Lag-1 definition of a new co-author | 6.89 pp | 0.38 [0.22, 0.54] |
| Without topic100 FE | 8.53 pp | 0.47 [0.32, 0.61] |
| Lag-1, without topic100 FE | 9.30 pp | 0.51 [0.35, 0.67] |
| Rows weighted 1/#stayer keys on the paper | 5.96 pp | 0.33 [0.20, 0.46] |
| NA-pool papers only | 5.79 pp | 0.32 [0.12, 0.51] |

**Like-for-like caution.** The model nets out topic100 composition, while the benchmark does not. Net of topic100 composition, the population rise is 10.7 pp, and 6.15 pp is 0.58 of it. This comparison is descriptive, not the pre-registered one.

**Part (ii).** All-prior teams (every panel key on the paper seen before) under the plan's censoring alternatives (`T2_2b_allprior.csv`; last-key cluster bootstrap):

| Definition | E → L | All-prior NAME E → L | n_E → n_L | Change | Ratio to population |
|---|---|---|---|---|---|
| Rolling (pre-registered) | 2022–23 → 2025–26 | .141 → .262 | 567 → 2,553 | +12.1 pp [8.9, 15.6] | 0.66 [0.49, 0.85] |
| Lag-1 (symmetric) | 2022–23 → 2025–26 | .132 → .259 | 441 → 1,580 | +12.7 pp [8.8, 16.6] | 0.70 [0.49, 0.90] |
| Symmetric two-year lookback | 2023 → 2025–26 | .169 → .262 | 384 → 2,190 | +9.2 pp [4.9, 13.5] | 0.53 [0.29, 0.77] |
| Rolling, E = 2023 | 2023 → 2025–26 | .169 → .262 | 384 → 2,553 | +9.3 pp [4.9, 13.6] | 0.53 [0.29, 0.76] |
| Fixed 2021–22 base | 2023 → 2025–26 | .169 → .156 | 384 → 211 | −1.3 pp [−7.3, +4.3] | −0.07 [−0.42, 0.24] |
| Rolling, pilot window | 2023 → 2026 | .169 → .290 | 384 → 1,613 | +12.0 pp [7.4, 16.3] | 0.60 [0.37, 0.79] |
| Rolling, NA-pool papers | 2022–23 → 2025–26 | .156 → .259 | 366 → 1,664 | +10.3 pp [5.8, 14.7] | 0.57 [0.33, 0.80] |

Notes on part (ii):
- The pilot-window ratio (0.60) matches the pilot's 0.60 to two decimals; the earlier transcription of its CI as [0.51, 0.76] was wrong.
- In L, the rolling definition counts keys first seen in 2024–25 as prior. Of the 2,553 rolling all-prior L papers, 1,042 (41%) contain a D2 entrant key, and they rose 0.95 [0.72, 1.16] ×. Those containing a returner but no entrant (979) rose 0.62 [0.39, 0.85] ×. Those made only of stayer keys (532) rose 0.19 [−0.05, 0.44] ×.
- (ii) is met on the point estimate under the rolling and lag-1 definitions, with CIs reaching just below 0.5. It fails under the fixed 2021–22 base, where all-prior L teams are few (0.9% of L papers).

**Verdict.** Part (i) is contradicted. Part (ii) depends on the definition. The rise of stayer keys' papers is mostly found on papers with new co-author keys. H2c is not supported. It is not falsified, because the CI of (i) excludes 0.

### 2.4 H2d: style vs topic channel (F2.1)

**Markers.** Fixed before outcomes were examined:
- 52 of the 61 frozen style markers. Nine fall below a 0.1% prevalence minimum chosen here: elevat* and 8 snowclones. API.md §4.6 flags the sub-0.1% snowclones but sets no rule.
- 33 topic markers: the 32 MiniLM topic100 clusters whose share changed by ≥ 1 pp, plus llm_topic.

**Fit.** In the any-role partition, within-stayer change regressed on population change across all 85 markers gives slope 0.923 [0.901, 0.946] and r = 0.992. That is not evidence of communal change:
- A random paper subset with the stayers' E/L weights gives slope 1.00 [0.96, 1.04] and r 0.999 (200 draws), so the observed slope falls below the communal benchmark.
- The shared-outcome generational null gives every marker the same ratio, the null ρ_any of 0.78, so its slope is 0.78.

Both benchmarks exceed the 0.7 falsification line, so the slope criterion cannot discriminate.

**Generational increment by channel.** G = 1 − b, where b is the through-origin slope within the channel (weights ∝ d²):

| Channel | G (any role) | G without llm_topic and the NAME family | Equal-weight median ρ_m |
|---|---|---|---|
| Style | 0.166 [0.133, 0.200] | 0.133 [0.079, 0.194] | 0.84 [0.80, 0.91] |
| Topic | −0.047 [−0.068, −0.025] | −0.060 [−0.083, −0.035] | 1.05 [1.02, 1.09] |
| Difference | 0.213 [0.176, 0.251] | 0.192 [0.134, 0.258] | style − topic −0.21 [−0.26, −0.14] |

The aggregate-ratio version agrees: 0.162 vs −0.053.

**Weights.** The d² weights are concentrated:
- In the topic channel, llm_topic carries 94.5% (d = 35.1 pp).
- In the style channel, compound, NAME loose, NAME, NAME strict and mixed-case NAME carry 30%, 18%, 18%, 17% and 10% (93% together).
- Restricted to markers with |d| ≥ 1 pp, the median ρ is 0.83 (style) and 1.05 (topic).

**Marker counts.**
- 38 of 52 style markers lie on the generational side (|ΔS| < |Δ|). So do 11 of 33 topic markers; the other 22 lie on or above the 45° line.
- Stayer keys' papers moved into LLM topics slightly faster than the population: +36.7 pp against +35.1 pp.
- Topic markers show a small negative increment, which is not "none".

**Why the contrast is informative.** The shared-outcome null predicts one common ratio for all markers. A channel difference therefore cannot come from who co-authors with whom: stayer-carried papers moved into growing topics at or above the population rate but adopted style markers more slowly.

By partition:

| Partition | Slope | G_style | G_topic | Median ρ style / topic |
|---|---|---|---|---|
| Last | 1.026 | 0.014 [−0.034, 0.059] | −0.084 | 0.97 / 1.12 |
| First | 0.756 | 0.402 [0.309, 0.494] | 0.029 | 0.70 / 0.94 |

The style increment sits at the first list position.

### 2.5 H2e: the pre-LLM era is inconclusive

**Main estimate.** With email keys, E = 2018 and L = 2020 (621 stayer keys in any role), NAME moved from .072 to .139 among stayers and from .101 to .157 in the population.

| Statistic (any role) | NAME | Compound (colon) |
|---|---|---|
| ρ, paper-weighted (D2-1; post hoc for H2e) | 1.20 [0.71, 1.77] | 1.13 [0.08, 2.66] |
| ρ, author-weighted | 0.79 [0.38, 1.23] | 0.37 [−0.44, 1.13] |
| Literal Kitagawa within share (pre-registered) | 0.26 [0.15, 0.39] | 0.25 [0.02, 0.57] |
| Shared-outcome null ρ (entrant-first / entrant- or returner-first) | 0.69 / 0.76 | same composition |
| ρ − entrant-first null | +0.51 [0.02, 1.07] | +0.44 [−0.59, 1.96] |

Reading the table:
- The literal statistic is below the 0.3 falsification line for both outcomes. With s̄ = 0.22 it would be too even under purely communal change, unless ρ > 1.38.
- On ρ, NAME exceeds 0.5 and sits just above its shared-outcome null.
- Compound is uninformative: the population change is only +3.6 pp, and the author-weighted point estimate is below 0.5.

**Two-year windows (2017–18 → 2019–20).**

| Outcome | ρ | Author-weighted ρ | Literal share |
|---|---|---|---|
| NAME | 1.08 [0.73, 1.49] | 0.95 [0.62, 1.33] | 0.31 [0.21, 0.43] |
| Compound | 1.12 [0.57, 1.75] | 0.81 [0.26, 1.40] | 0.33 [0.16, 0.52] |

For NAME, ρ − null = +0.36 [0.02, 0.78].

**Uninformative partitions.** The last- and first-position estimates are too small to inform (`h2e_email.csv`):

| Partition | ρ (NAME) |
|---|---|
| Last | 0.68 [−0.21, 1.44] |
| First | 0.85 [−0.19, 2.05] |

The newcomer-free cells are tiny: 62 L papers with a stayer last key and no entrant, and 25 all-stayer L papers.

**Selection caveat.** In this era exiters titled with NAME more than stayers in 2018 (+4.2 pp [1.7, 6.6]). The stayers who keep an unchanged email are a selected, lower-baseline group.

**Verdict:** inconclusive. The pre-LLM data are not inconsistent with stayer keys' papers changing, but they do not establish that communal change was the general mode.

### 2.6 Robustness of ρ (NAME primary; `T2_1_decomposition.csv`, `removal_extrapolation.csv`, `removal_family_sim.csv`)

| Variant | Last | Any role | First |
|---|---|---|---|
| Main (paper-weighted) | 0.995 [0.943, 1.050] | 0.816 [0.777, 0.857] | 0.525 [0.414, 0.633] |
| Main, two-way CGM CI | [0.940, 1.050] | [0.768, 0.863] | [0.419, 0.630] |
| Author-weighted | 0.897 [0.818, 0.980] | 0.699 [0.660, 0.736] | 0.545 [0.430, 0.656] |
| IPW for staying | 0.977 [0.921, 1.035] | 0.801 [0.759, 0.844] | 0.523 [0.405, 0.633] |
| NA-pool outcomes (camera-ready-free) | 0.990 [0.929, 1.058] | 0.840 [0.792, 0.892] | 0.564 [0.427, 0.713] |
| Papers with any email-keyed position dropped | 0.995 [0.944, 1.048] | 0.820 [0.783, 0.858] | 0.536 [0.428, 0.642] |
| Non-LLM papers | 1.012 [0.926, 1.095] | 0.793 [0.729, 0.852] | 0.459 [0.281, 0.635] |
| Excluding 2026 (E 2021–22, L 2024–25) | 1.003 [0.918, 1.095] | 0.812 [0.752, 0.880] | 0.529 [0.348, 0.703] |
| L = 2025 only | 1.095 [1.000, 1.185] | 0.885 [0.818, 0.952] | 0.641 [0.451, 0.825] |
| L = 2026 only | 0.959 [0.902, 1.022] | 0.824 [0.781, 0.870] | 0.512 [0.369, 0.640] |
| 2023 → 2026 (pilot window) | 0.963 [0.895, 1.032] | 0.822 [0.769, 0.879] | 0.460 [0.280, 0.611] |
| Trim top 1% keys (> 16 papers; 844 keys) | 0.875 [0.795, 0.960] | 0.727 [0.681, 0.776] | 0.507 [0.392, 0.621] |
| topic100-adjusted outcome | 0.956 [0.874, 1.041] | 0.744 [0.681, 0.808] | 0.398 [0.201, 0.565] |
| Team-size-bin-adjusted outcome | 0.942 [0.881, 1.004] | 0.788 [0.741, 0.834] | 0.465 [0.330, 0.587] |
| Partition-specific stayers | 0.954 [0.878, 1.033] | 0.816 [0.777, 0.857] | 0.580 [0.421, 0.720] |
| Restricted alias collapse (≤ 3 keys, ≤ 40 papers per alias-year) | 1.006 [0.957, 1.061] | 0.841 [0.801, 0.879] | 0.612 [0.502, 0.713] |
| Full alias collapse (extreme upper bound on stayer status) | 1.018 [0.970, 1.064] | 0.899 [0.865, 0.932] | 0.775 [0.686, 0.869] |
| Returners excluded from L | 0.999 [0.952, 1.051] | 0.804 [0.766, 0.844] | 0.511 [0.400, 0.614] |
| Held-out removal (random, 20% × 200), extrapolated to full coverage | 0.996 (point only) | 0.818 (point only) | 0.528 (point only) |
| Further 20% removed in same-key cross-year pairs (100 sims): mean shift | −0.048 | −0.035 | −0.039 |
| NAME strict | 0.992 [0.940, 1.048] | 0.812 [0.772, 0.854] | 0.510 [0.397, 0.618] |
| NAME loose | 0.998 [0.944, 1.054] | 0.828 [0.786, 0.869] | 0.568 [0.453, 0.677] |
| Compound (any colon or dash) | 0.963 [0.918, 1.007] | 0.851 [0.820, 0.886] | 0.688 [0.596, 0.779] |

Notes on the variants:
- **Held-out removal.**
  - Under random removal of a further 10–30% of papers, ρ moves by less than 0.01 on average. At 20%, simulation SDs are 0.016, 0.014 and 0.034 for last, any role and first.
  - The per-unit extrapolations are unstable across fractions: 0.020 / 0.004 / 0.005 per unit of coverage for last at 10 / 20 / 30%. The extrapolated values are point estimates only.
  - Random paper-level removal does not reproduce the held-out split. The export keeps one submission per family, and the split mechanism is not recorded.
  - When the removed papers are same-key pairs one or two years apart (a resubmission-like stress test), ρ falls by 0.02–0.05: 0.021 / 0.018 / 0.026 if half the removed papers come in pairs, and 0.048 / 0.035 / 0.039 if all do.
  - So if the held-out split is family-structured, the observed ρ may understate full-coverage ρ by a few hundredths. Cross-split bias is not ruled out, but it is small relative to the null benchmarks.
- **Prolific keys.** Removing the 844 most prolific keys (0.95% of keys; > 16 papers) lowers ρ_last by 0.12, to 0.875 [0.795, 0.960], and ρ_any by 0.09, to 0.727 [0.681, 0.776]. A disproportionate part of the stayer-paper rise sits on the papers of the most prolific keys. The H2a thresholds on ρ still hold.
- **Topic composition.** Net of topic100 composition, the population rise is 10.7 pp rather than 18.3 pp. ρ within topic is 0.96 for last and 0.74 for any role.

### 2.7 Supporting tests (T2.3; exploratory)

#### S2.1 Within-paper retitling (`s2_1_resubmission.csv`)

**Pairs.**
- **Matching rule:** a shared declared key, a gap of 1–2 years, bge cosine ≥ 0.95 or MiniLM ≥ 0.85, a non-accepted source, and greedy one-to-one matching.
- **Count:** this yields 297 pairs with destination year ≥ 2024, the same count as the pilot.
- **Purity:** 0.87, from matches per source paper of 0.26% for accepted sources against 1.96% for non-accepted ones. Under a strict rule (bge ≥ 0.97 or MiniLM ≥ 0.90) it is 0.98.
- **Identical titles:** only 1.3% of pairs have identical titles. The export keeps one submission per paper family, so the pairs that survive are selected on retitling.

**Result.** Within these pairs, mean ΔNAME is 0.000 (se 0.025), with 28 adds and 28 drops. The MDE is 7.1 pp. The benchmark matters:

| Benchmark (union rule, destination ≥ 2024) | Benchmark change | Pair change − benchmark |
|---|---|---|
| Raw population drift implied by the pairs' years | +7.2 pp | −7.2 pp (se 2.5, p = 0.005) |
| Topic100-adjusted population drift (content held fixed) | +4.8 pp | −4.8 pp (se 2.5, p = 0.057) |
| Drift within the source paper's topic100 cluster | +3.9 pp | −3.9 pp (se 2.5, p = 0.12) |
| The same shared keys' other papers (n = 217 pairs) | +2.5 pp (se 2.0) | −3.4 pp (se 3.5, p = 0.33) |

**Other rules and outcomes:**

| Sample | Mean change | Implied drift (raw) | Change − raw drift |
|---|---|---|---|
| Strict rule (n = 164) | +1.8 pp (se 2.9) | +6.9 pp | −5.1 pp (se 2.9, p = 0.08) |
| Destinations ≤ 2023 (n = 76) | 0.000 (se 0.042) | +2.5 pp | −2.5 pp (se 4.2) |
| Compound outcome | +3.7 pp (se 3.2) | +9.7 pp | — |

**Statement.** Even among retitled papers, NAME is not added on net. These papers lag the raw population drift, but the lag is not established against content-fixed benchmarks. S2.1 is evidence against NAME being added within an existing project: any adoption runs through new projects. It does not show that the same keys changed. Add and drop counts are descriptive only. They are not behavioural transition rates, because the pairs are selected on retitling.

#### S2.2 Future-tie placebo (`s2_2_future_tie.csv`, supplementary `fig_S2_2_future_tie`)

**Sample.** Clean focal papers, T = 2023–25: 6,572 rows and 2,358 keys. Past-collaborator exposure covers a median of 9 collaborators, future-collaborator exposure a median of 4.

| Specification | Outcome | Past | Future | Past − future (se) | MDE of the difference |
|---|---|---|---|---|---|
| Year + topic100 FE (primary) | NAME | −0.007 (0.026) | +0.067 (0.025) | −0.075 (0.037) | 0.103 |
| Year + topic100 FE (primary) | llm_topic (positive control) | +0.022 (0.016) | +0.069 (0.015) | −0.046 (0.023) | 0.065 |
| Year FE only (pilot) | NAME | +0.044 (0.028) | +0.117 (0.026) | −0.072 (0.039) | 0.109 |
| Year FE only (pilot) | llm_topic (positive control) | +0.221 (0.030) | +0.265 (0.029) | −0.043 (0.046) | 0.130 |

The pilot specification reproduces the pilot to within 0.001 (pilot .045 (.028) vs .118 (.026)). Compound titles behave like NAME: 0.008 vs 0.029 in the primary specification. In the full, non-clean sample, past and future exposure are equal (0.056 vs 0.053).

**Reading.**
- Past-collaborator exposure is not larger than future-collaborator exposure. The upper 95% bound of past − future for NAME is −0.003 in the primary specification.
- The positive control is not detected in the primary specification, because topic100 FE absorb most of llm_topic.
- Where the control is detected (pilot specification), it shows the same past < future ordering.

So this design fails to support tie contagion but cannot separate contagion from homophily. S2.2 is inconclusive; the earlier wording "fits homophily" is withdrawn.

## 3. Deviations from PLAN.md (logged)

- **D2-1 Statistic.**
  - H2a, H2b, H2d and H2e are evaluated on ρ = ΔP_S/Δ. This is how the pilot numbers behind the thresholds were computed (1.00 / 0.83 / 0.58), and it is the "within/pop" of H2d.
  - The literal first-term share of the plan's Kitagawa formula equals s̄·ρ, so it cannot reach the thresholds when s̄ is below them, even under purely communal change.
  - H2e was added to this deviation after the audit; it had been switched without disclosure.
  - On the literal statistic, H2a is not met (0.61 / 0.35) and H2e is below its falsification line (0.26 / 0.25). Both are shown in the summary table.
- **D2-2 Stayer status.** Stayer status comes from any-role presence, as in the pilot. Partition-specific stayer status is a robustness check.
- **D2-3 First and last positions.**
  - Both are defined on the full declared list. Papers whose last or first key is not a profile key drop out of that partition.
  - At the last position this removes 10.1% (2021), 4.8% (2022) and 3.6% (2023) of papers; at the first position 6.7%, 1.7% and 1.2%.
- **D2-4 Returners.** For the exact identity, returners stay in the L "others" group. A variant without returners is reported, now with CIs.
- **D2-5 Fixed-base and two-year-lookback team types.** These definitions use E = 2023 only, because their base window overlaps 2022.
- **D2-6 IPW.**
  - Specification: a key-level L2 logit (C = 10), with p clipped to [0.02, 0.98] and weights capped at the 99th percentile.
  - Propensities are held fixed across bootstrap replicates, so the IPW CIs ignore propensity-estimation error.
- **D2-7 H2c model.**
  - The model adds a main effect of share_new_coauthors, which the plan's formula omits.
  - It uses rows from 2022–26, because in 2021 every key is new under the rolling definition.
  - The E→L contrast is mean(2025, 2026) − mean(2022, 2023) year effects. Solo-key papers get share 0.
  - The benchmark is the raw any-role population change, as pre-registered.
  - SEs are two-way clustered by key and paper (CGM; audit D2-C3). The H2c p-value is now tested at the falsification boundary.
- **D2-8 H2d markers and statistic.**
  - Minimum prevalence is 0.1% in E∪L, a rule chosen here.
  - G = 1 − the through-origin slope per channel. Aggregate-ratio and equal-weight (median ρ_m) versions are also reported.
  - The marker set is held fixed across bootstrap replicates.
- **D2-9 H2e windows.**
  - The windows are single years, E = 2018 and L = 2020, following "2018→2020".
  - Any role is primary, since the plan names no partition. Two-year windows and author weighting are robustness checks.
  - IPW is not applied in the email era.
- **D2-10 S2.1 matching.**
  - The source pool is NA, which adds desk-rejected papers; the pilot used rejected and withdrawn.
  - Pairs follow the pilot's greedy ordering: best bge match first, then the union rule.
  - Added: a strict-rule variant, the same keys' other papers, and topic-adjusted and within-topic drift benchmarks.
- **D2-11 S2.2 specification.**
  - The primary specification adds topic100 FE, following the C15 operationalisation ("cluster and year controls"). The pilot specification is also reported.
  - The verdict now requires the positive control to be detected and to behave differently from NAME.
- **D2-12 Team-type bootstrap.** The team-type, all-prior and newcomer-free bootstraps cluster on the paper's last-position key.
- **D2-13 Removal simulation.** It assumes discovery coverage c0 = 0.8 and random paper-level removal. A family-structured (same-key pair) variant was added after the audit.
- **D2-14 Extra variants.** Added beyond the plan:
  - L = 2025 and L = 2026 cohorts (PLAN §0);
  - the non-LLM subset;
  - the 2023 → 2026 pilot window;
  - a team-size-bin-adjusted outcome.
- **D2-15 Audit additions (not pre-registered).**
  - the shared-outcome null;
  - the newcomer-free contrasts;
  - two-way SEs;
  - the first-position within-last-key and symmetric-lookback analyses;
  - the H2d random-subset benchmark;
  - the restricted alias collapse;
  - the email-position sensitivity;
  - the symmetric two-year team type.

## 4. Limitations

- **Shared outcomes.** Titles belong to papers, not keys. A key-level decomposition measures how papers carrying a key changed, not whose choice changed. The newcomer-free contrasts locate the rise but cannot separate "newcomers carry the style" from selection, for example groups of keys that adopt the style also adding new keys.
- **Keys are not people.**
  - A person with two profiles creates a false exit plus a false entry.
  - A person listed by email in E and by profile in L becomes a false exiter and a false entrant. Papers with email-keyed positions are 13–17% of 2021–23 papers. Dropping them leaves ρ unchanged.
  - Different people who share a name stay distinct unless aliases are collapsed. The restricted collapse raises ρ_first to 0.61; the full collapse is an extreme bound (0.78).
- **Censoring.**
  - Entrant status is left-censored at 2021. Returners (6,949 keys) absorb part of this.
  - The rolling team-type and new-co-author definitions have a lookback that grows over time. The symmetric lag-1 and two-year variants are reported next to them.
  - The held-out 20% split is simulated as random or as same-key pairs. Its true structure is unknown.
- **Stayers are selected.** IPW balances observables only, with AUC 0.67. D2 stayers have at least three years of presence, so stayer/entrant contrasts mix cohort with tenure.
- **Communal does not mean tool-free.** The analysis concerns *who* carries the change, not *why*. Topic composition accounts for about 40% of the raw population rise (10.7 pp net of topic100 composition against 18.3 pp); D1 handles content.
- **Camera-ready contamination** affects accepted papers. The ρ partitions replicate on NA-pool outcomes (0.990 / 0.840 / 0.564), and so do the newcomer-free contrasts. H2c(i) gives 0.32 [0.12, 0.51] and rolling H2c(ii) 0.57 [0.33, 0.80] on NA-pool papers. H2d, H2e and S2.2 were not re-run on NA-pool outcomes.
- **H2e** uses email keys with linkage breaks, a selected lower-baseline stayer group and tiny newcomer-free cells.
- **S2.1** is selected on retitling and has an MDE of 7.1 pp.
- **S2.2** has a positive control that the primary specification does not detect, and an MDE of 0.10 for past − future. It can only fail to support tie contagion. It does not establish homophily, and it does not rule out influence.

## 5. Files (`outputs/d2_carriers/`)

**Figures** (PDF, PNG and CSV for each):
- `fig_F2_1_marker_scatter`: F2.1, any-role partition.
- `fig_F2_2_decomposition`: F2.2, four panels:
  - (a) ρ with key-cluster and two-way CIs, IPW and the shared-outcome nulls;
  - (b) the Kitagawa within share and the scenario values;
  - (c) the newcomer-free contrasts;
  - (d) the team-type composition shift-share.
- `fig_F2_3_levels`: F2.3, with returners plotted.
- `fig_S2_2_future_tie`: supplementary, with a shared x-axis and MDE bands.

**Tables:**
- `T2_0_summary_table.md`: the auto-generated summary table.
- T2.1: `T2_1_decomposition.csv`, `T2_1b_twoway_se.csv`, `decomposition_long.csv`.
- T2.2: `T2_2_author_fe.csv`, `T2_2b_allprior.csv`.
- T2.3: `T2_3_support.csv`, with detail in `s2_1_resubmission.csv` and `s2_2_future_tie.csv`.
- T2.4: `T2_4_newcomer_free.csv`.
- H2b: `h2b_first_position.csv`, `h2b_newcomer_premium_by_year.csv`.

**Other outputs:**
- Team types: `team_type_shiftshare.csv`, `team_type_rates.csv`.
- Removal simulations: `removal_simulation.csv`, `removal_extrapolation.csv`, `removal_family_sim.csv`.
- IPW and H2e: `ipw_balance.csv`, `h2e_email.csv`.
- Markers: `markers_changes.csv`, `markers_selection.csv`, `markers_weight_shares.csv`, `h2d_random_subset.csv`.
- Panel: `panel_summary.csv`, `panel_info.json`, `panel_rows.parquet`, `panel_papers.parquet`, `email_rows.parquet`.
- Resubmission pairs: `resub_pairs.parquet`.
- Per-script JSON: `shiftshare_results.json`, `markers_results.json`, `ident_results.json`, `support_results.json`.
- Bootstrap draws: `*_boot_draws.npz`.
- Logs: `d2_*.log`.
- Machine-readable summary of everything above: `results.json`.

**Run order:**

```bash
cd research/titles/src
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_panel
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_shiftshare 1000
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_markers 1000
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_ident 1000
OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_support
/home/user/venv/bin/python -m analyses.d2_collect
```

Total run time is about 6–7 minutes.

## Audit response

Three audits were run: code (D2-C), identification (ID) and reporting (D2-R). Each issue was re-checked before any change was made. All 44 issues were judged valid, ID-2 in part (see below). Pre-fix copies of the scripts and outputs are in `outputs/audit/d2/pre_fix_backup/`.

### Changed verdicts

| Hypothesis | Before | After |
|---|---|---|
| H2a | supported | **not identified**. The prediction is met on ρ but not on the literal statistic, and is also met by a purely generational shared-outcome null. |
| H2b | supported | **supported on the pre-registered groups; magnitude not robust** (tenure confound). |
| H2c | partially supported | **not supported**. (i) is contradicted; (ii) holds only under the rolling and lag-1 definitions. |
| H2d | supported | **supported (channel contrast); slope criterion not diagnostic**. |
| H2e | supported | **inconclusive**. |
| S2.1 | supported | NAME not added on net; lag behind content-fixed drift not established. |
| S2.2 | supported | **inconclusive**. |

The summary claims "happened inside the same declared profile keys", "the communal pattern also holds in the pre-LLM era", "the two supporting tests agree" and "fits homophily" were withdrawn. The thesis bullet "The same people changed" in PLAN §1 is not supported by D2. It should be reworded in the paper write-up; PLAN.md itself was not edited.

### Code audit (D2-C)

- **D2-C1 (valid).** The H2c(ii) CIs in RESULTS were stale. Corrected values:
  - 0.66 [0.49, 0.85];
  - +12.1 pp [8.9, 15.6];
  - 2023→2026: 0.60 [0.37, 0.79].

  `d2_collect` now writes the summary table into RESULTS.md itself. The claim that the pilot-window CI clears 0.5 is dropped.
- **D2-C2 (valid).** H2c(ii) is now reported under the rolling, lag-1, fixed-base and symmetric two-year definitions, plus E = 2023 and NA-pool variants (`T2_2b_allprior.csv`). The fixed base fails at −0.07 [−0.42, 0.24]. The verdict and summary are weakened accordingly.
- **D2-C3 (valid).**
  - (a) The H2c p-value now tests the falsification boundary (ratio ≤ 0.3): p = 0.31. The test of the prediction gives p = 0.015 against ratio ≥ 0.5.
  - (b) SEs are two-way (key, paper) CGM: 1.38 pp against 0.82 pp key-only. The ratio CI is now [0.19, 0.48]. Holm was re-run.
- **D2-C4 (valid; no verdict change).** Two-way CGM SEs and the conservative pigeonhole bootstrap are reported for the headline ρ and for first − last (`T2_1b_twoway_se.csv`). CGM SEs are within about 15% of the key-cluster SEs. Pigeonhole SEs are about 1.6× larger and are labelled conservative.
- **D2-C5 (valid).** Added:
  - the marker weight shares (llm_topic 94.5%; NAME family 93%);
  - a variant without both llm_topic and the NAME family: difference 0.19 [0.13, 0.26];
  - an equal-weight median-ρ version: style − topic −0.21 [−0.26, −0.14].

  "85-marker result" is no longer used as a claim of breadth. The contrast survives.
- **D2-C6 (valid).** The S2.2 verdict now requires the positive control to be detected in the same specification and to differ from NAME. It is now "inconclusive". The upper bound of past − future is reported.
- **D2-C7 (valid).** The S2.1 contrast is now also made against topic100-adjusted drift (−4.8 pp, p = 0.057), within-topic drift (−3.9 pp, p = 0.12) and same-key other papers (−3.4 pp, p = 0.33). The claim that retitled papers lag the drift is weakened.
- **D2-C8 (valid).** The random-removal assumption is stated. A family-structured same-key pair removal was added: ρ shifts by up to −0.05. "Negligible" is replaced by "small under random and pair-structured removal; not ruled out".
- **D2-C9 (valid).** The literal Kitagawa share is shown in the H2a summary row and verdict (not met: 0.61 / 0.35).
- **D2-C10 (valid).** The lag-1 definition is reported next to the rolling one for H2c(i): ratio 0.38, post × share_new 4.4 pp against 7.9 pp. The mean share_new by year is shown, and the interaction is described as partly censoring.
- **D2-C11 (valid).** The full alias collapse was removed from the H2b variant table and labelled an extreme upper bound. A restricted collapse (≤ 3 keys, ≤ 40 papers per alias-year) was added: first − last −0.39 [−0.51, −0.28].
- **D2-C12 (valid; small effect).** A variant was added that drops papers with any email-keyed position: ρ 0.995 / 0.820 / 0.536. The issue is mentioned in Limitations.
- **D2-C13 (valid).** The H2e verdict now uses both outcomes and an intersection-union p-value. Compound is reported as imprecise. H2e is inconclusive.

### Identification audit (ID)

- **ID-1 (valid; critical).**
  - Re-checked with an independent code path. ρ for indicator outcomes reduces to a composition ratio: 0.882 / 0.776 / 0 (last / any / first) for the entrant-first null.
  - The null benchmarks and observed − null differences are now in T2.1, F2.2a and the summary table.
  - H2a is downgraded to "not identified". The "same declared profile keys" and "the same people changed" wording is withdrawn.
- **ID-2 (valid in substance; one point qualified).** The newcomer-free contrasts are now the main within-incumbent evidence (T2.4, F2.2c). Selection is named as the unresolved alternative.

  The auditor's range "0.03 to 0.4" omits the symmetric definitions: lag-1 all-prior teams give 0.70 [0.49, 0.90], and the symmetric two-year lookback gives 0.53. The stricter "no entrant" rows also compare against all E papers of the same stayers, which is an asymmetric comparison. RESULTS therefore reports a tenure gradient (about 0 to 0.7), not "small or zero" across the board.
- **ID-3 (valid).** The composition of rolling all-prior L teams is now reported: 41% contain an entrant key, 21% are stayer-only, and the stayer-only teams rose 0.19 ×. The H2c verdict is now "not supported", and "part, but not most" is replaced.
- **ID-4 (valid).** Added:
  - the within-last-key gap: 4.9 pp [2.2, 7.6];
  - the symmetric two-year newcomer premium by year, with change +4.3 pp [0.3, 8.4];
  - the symmetric prior-first ratio: 0.86 [0.72, 1.01].

  The tenure confound is flagged and the H2b verdict qualified.
- **ID-5 (valid).** The random-subset benchmark (slope 1.00 [0.96, 1.04]) and the null slope (0.78) are reported. "Slope ≈ 1" is no longer cited as evidence of communal change. The G_style vs G_topic contrast is kept as the informative result.
- **ID-6 (valid in part).**
  - The email-era null is 0.69 (entrant-first) and 0.76 (entrant- or returner-first).
  - Here the observed NAME ρ_any exceeds the entrant-first null by 0.51 [0.02, 1.07], a marginal margin, so "not discriminating at all" is slightly too strong.
  - H2e is downgraded to "inconclusive", and "communal change is then the general mode" is withdrawn.
- **ID-7 (valid).** S2.1 is reworded: there is no within-project NAME adoption, so any change runs through new projects. The "agree" claim was dropped.
- **ID-8 (valid).** S2.2 is reworded: the primary specification does not detect the control, and the detected control shows the same ordering. S2.2 is inconclusive.
- **ID-9 (valid).** Two-way CIs are reported for the headline ρ and first − last. The 1.7× figure is the conservative pigeonhole bootstrap. The CGM two-way SEs are close to the key-cluster SEs. Both are reported.

### Reporting audit (D2-R)

- **D2-R1 (valid).** H2e was added to D2-1. The literal shares (0.26 / 0.25 < 0.3) are in the summary table and §2.5. The verdict notes that the literal statistic is capped at s̄ = 0.22.
- **D2-R2 (valid).** The H2a cell shows both statistics. "The one shortfall is H2c(i)" was removed. ρ is renamed "stayer-to-population change ratio".
- **D2-R3 (valid).** The first summary sentence was replaced, with the Kitagawa shares 61% / 35% / 17%.
- **D2-R4 (valid).** Same fix as D2-C1. The header claim was replaced: the table is now generated by code and the other numbers were checked by a script.
- **D2-R5 (valid).** Same fix as D2-C2.
- **D2-R6 (valid).** (i) is reported as contradicted (p = 0.015). The margin above 0.3× is not significant (p = 0.31). Ratio CIs are given for every variant.
- **D2-R7 (valid).** The same-key benchmark (−3.4 pp, se 3.5) and the strict-rule gap (−5.1 pp, p = 0.08) are now in the summary and §2.7.
- **D2-R8 (valid).** "Fits homophily" was removed. The MDE of past − future (0.10) is reported, and the positive-control ordering is discussed.
- **D2-R9 (valid).** F2.2 was redrawn as four panels:
  - (a) ρ with two-way CIs, IPW CIs and null markers;
  - (b) the Kitagawa share and scenario values, labelled "not bounds on ρ";
  - (c) the newcomer-free contrasts;
  - (d) the composition shift-share, with fixed-base rows marked E = 2023.

  The text now gives scenario (a) as 0.75 [0.71, 0.79].
- **D2-R10 (valid).** Author-weighted email-era rows were added. The verdict now accounts for the compound CI.
- **D2-R11 (valid).** "Holds in every variant" was replaced. The full alias collapse is moved out of the table, and its CI including gaps below 0.2 is stated.
- **D2-R12 (valid).** The NA-pool statement in Limitations now lists what was and was not re-run.
- **D2-R13 (valid).** The trim wording is now quantitative and non-causal.
- **D2-R14 (valid).** The G statements are qualified: partition named, NAME-family dominance stated, "none" replaced by a small negative increment, and "mostly on or above (22 of 33)" used.
- **D2-R15 (valid).** The D2-3 coverage numbers are corrected (10.1 / 4.8 / 3.6% last; 6.7 / 1.7 / 1.2% first).
- **D2-R16 (valid).** "Exactly" is replaced by "to within 0.001" and "to two decimals".
- **D2-R17 (valid).** Same fix as D2-C8. The unstable per-unit extrapolations are stated.
- **D2-R18 (valid).** F2.3 now plots returners and labels "all panel rows". The caption states that the bands are 95% key-cluster bootstrap CIs, and the y-axis starts at 0.
- **D2-R19 (valid).** F2.1 now names the partition, labels the cluster "NAME (3 overlapping variants)", notes that the error bars show the within-stayer change only, and nudges the zoom labels.
- **D2-R20 (valid).** S2.2 now uses a shared x-axis, MDE bands and a caption listing the MDE of past − future.
- **D2-R21 (valid).** Wording replaced:
  - "title more fashionably" was removed;
  - the alias mechanism is stated as consistent with false stayers being entrants;
  - "from 2024 on (post = year ≥ 2024)" replaces "after 2024";
  - the API.md §4.6 attribution is corrected.
- **D2-R22 (valid).** ρ_noR now has CIs. The extrapolated removal rows are marked "point only". Ratio CIs are given for all H2c variants, plus a version that includes the uncertainty of the population change.
