# D4. The gatekeeper: stage-wise filter gains and the bias of published-only title studies

WP8 results for PLAN.md §D4, revised after three independent audits (code, identification, reporting). The issue-by-issue response is in the last section, **Audit response**. The fix log is `outputs/audit/d4/fix_log.md`.

Code is in `research/titles/src/analyses/`:
- `d4_stage_gains.py`: H4a, H4b, T4.1, F4.1, S4.1.
- `d4_bias_atlas.py`: H4c, H4e, T4.2, F4.2, F4.3.
- `d4_exit_composition.py`: H4d, F4.4, and the exploratory analyses.
- `d4_collect.py`: builds `results.json`, the T4.1/T4.2 markdown tables and the summary table below. It computes the verdicts from the stored estimates (rules in its docstring).

All outputs are in `outputs/d4_filter/`. Acceptance associations are associational and subject to the camera-ready caveat. "Last list position" is a partition label, and a declared profile key is not a verified person.

## Summary

The verdicts are computed by `d4_collect.py`. Multiplicity follows PLAN §0:
- **Holm** over the D4 confirmatory family {H4a, H4b, H4c, H4d}. Each hypothesis enters with one intersection-union p-value.
- **BH** over T4.1 and the atlas.

| Rank | Hypothesis | p (raw) | Holm threshold | Holm-adjusted p | Rejected at 0.05 |
|---|---|---|---|---|---|
| 1 | H4d (cross > 0 and difference > 0) | 1.3e-5 | 0.0125 | 5.0e-5 | yes |
| 2 | H4a (TOST; 0 of 2,000 replicates beyond a margin, floored at 1/2,000) | 0.0005 | 0.0167 | 0.0015 | yes |
| 3 | H4b (L-union total, L-union desk·exit, O-union total) | 0.0295 | 0.025 | 0.059 | **no** |
| 4 | H4c (ratio ≤ 0.85 in each of 2024–26) | 0.209 | 0.05 | 0.209 | **no** |

<!-- AUTO:SUMMARY START -->
| Hypothesis | Pre-registered test | Result (2024–26 pooled unless stated) | Verdict |
|---|---|---|---|
| H4a: neutral filter for NAME | Yearly NAME G_total in [0.95, 1.10]; pooled TOST in [0.90, 1.11]; equal 2024 break across ACC/REJ/WD | Pooled G_total 1.021 [0.997, 1.044], 90% CI [1.001, 1.041] (TOST p < 0.0005). All 9 yearly point estimates in band; 95% CIs inside it only for 2024, 2025, 2026. Break ORs 1.053 / 1.119 / 1.107, Wald p = 0.51; year-level ACC-REJ difference [-0.109, 0.074], ACC-WD [-0.290, 0.252]. Audit-implied selection-only G_total [0.867, 1.081] (WP4) | **Supported** for the observed published-vs-submitted NAME share (Holm p 0.002). Review-stage neutrality is not identified (the selection-only interval crosses 0.90). Pool equality is not rejected, but equivalence is not shown. |
| H4b: depletion of L and O markers | G_total < 1 for the L-union and O-union; G_desk·G_exit < 1 for the L-union | L-union total 0.975 [0.951, 1.001], one-sided p 0.0295. L-union desk·exit 0.981 [0.972, 0.992] (camera-ready-free 0.976 [0.961, 0.991]). L-union without R24: total 0.998 [0.972, 1.027]. R24 post/pre total 0.990 [0.788, 1.288]. O-union total 0.807 [0.749, 0.870]; decision stage 0.812; camera-ready-free pre-decision 1.035 [1.000, 1.072] | **Partially supported** (Holm p 0.059). The L-union total is not significant after Holm. The identified pre-decision L depletion is R24 title words, which were depleted before 2024; the other L markers are neutral. O: the published record under-represents O titles, but selection is not identified (decision stage). The identified O depletion is ALL-CAPS at exit. |
| H4c: published-only Kobak bound understates | Accepted/all bound ratio ≤ 0.85 in each of 2024–26; falsified if ≥ 0.9 in both 2024 and 2025 | 0.800 [0.658, 0.918] / 0.714 [0.504, 0.891] / 0.502 [-0.081, 0.932]. P(ratio ≥ 0.85) 0.209 / 0.078 / 0.079. Post hoc pre-ChatGPT baseline: 0.9005 / 0.9011 / 0.995 | **Partially supported** (Holm p 0.209). Direction (ratio < 1) is supported. The ≥ 15% size holds for point estimates only. The falsification condition is met under the post hoc baseline. |
| H4d: withdrawal excess of NAME papers | Cross-section > 0, within last-position key ≤ 0, and the two differ | 4.06 pp (se 0.96) vs -0.70 pp (se 1.08); difference 4.77 (se 0.75). With topic100 FE: cross 0.84 [-1.05, 2.74], within -1.74. Single-paper keys 6.91 (topic FE 5.60) | **Partially supported** (Holm p < 0.0005). The pre-registered contrast holds. Most of the excess is topic composition, and 'between keys' is not established as the mechanism. |
| H4e: published-only atlas | M statistics within ±10%; deviations concentrate in O and L | M 9/11 within ±10% on the effect scale (accepted-only 9/10); outside: ITS slope change 0.50, colon-premium trend 0.89. L 7/9; O 1/4 | **Partially supported** (descriptive). Prevalence levels are reproduced; the 2024 break is halved. |
| Decision-stage gate | A gain enters the headline only if its tipping point exceeds the audit CI | NAME G_dec tipping point 2.92 pp; audit DiD 2.09 pp [D4 -2.57, 6.74; WP4 -3.16, 7.33] | **No title-feature decision gain is identified** |
<!-- AUTO:SUMMARY END -->

**What the direction supports after the audit.**
- **NAME share.** A published-only study reproduces the all-submission NAME share (TOST passes). Whether review itself selects on NAME is not identified.
- **No LLM-specific depletion.** There is no evidence that peer review selects against LLM-styled titles or abstracts as such:
  - The small L-union depletion does not survive Holm.
  - What is identified comes from R24 title words ("Enhancing X via Y"), which were depleted by the same amount in 2018–23.
  - F24 and the abstract style density show a new pre-decision depletion of about 3–4%. The F24 part is new only relative to a baseline that includes 2023.
- **O markers.** The published record under-represents outsider (O) titles, but whether that is selection or camera-ready recasing is not identified.
- **H4d.** The withdrawal excess of NAME papers is mostly topic composition.

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

**Post-decision withdrawals.**
- The primary s2 follows `_core.pool_flags`, as PLAN §0 and the frozen CT6 do: only the 349 `wd_post` rows of 2026 stay in s2.
- A consistent definition keeps more rows in s2:
  - any withdrawn row that carries an accept/reject decision: 66 / 107 / 355 in 2024 / 2025 / 2026;
  - plus 2025–26 withdrawals timestamped on or after the decision date, which gives 299 in 2025 and 403 in 2026. 2024 timestamps are all post-decision (a bulk update) and cannot be used.
- The consistent variant is reported for the exit, decision and pre-decision gains. G_total = P(s3)/P(s0) does not involve s2, so it is identical under any s2 definition. The earlier "robustness" line for G_total under this variant was tautological and has been removed.

**Gains.** Gains are prevalence ratios: P(f | passed stage) / P(f | entered stage).
- For the continuous style density they are ratios of means.
- CIs come from a paper bootstrap stratified by year, with 2,000 replicates. The one-sided p for G < 1 is the share of replicates with G ≥ 1.
- **Pooling.** Pooled gains are year-standardised: each year's stage prevalence is weighted by that year's share of s0. Raw pooling is reported as robustness. The choice was made when the script was written. It was not separately timestamped before the first estimates, and the prereg bundle that freezes it post-dates these results.

**What each stage contrast measures.** s1 and s2 still contain the accepted papers, whose stored titles and abstracts are camera-ready.
- The desk and exit gains therefore compare the submission-stage text of exiting papers with survivor sets that mix in camera-ready text. They are not pure selection.
- The **camera-ready-free** (CRF) variants remove accepted papers from every stage set (`*_crf` in `gains.csv`). These are the contrasts that need no audit.
- Rejected titles may also have been revised during the rebuttal. Of 125 rejected audit pairs, 23.2% have stored titles that differ from the pre-decision arXiv v1, and 4 of 8 rejected sentence-case v1 titles were recased.
- OpenReview revision history is not in the data (`metadata_provenance` has only creation and last-modification times), so REJ-vs-WD contrasts may mix selection with rebuttal-period editing.

**Feature sets.**
- **M:** NAME, compound, phrase colon, mixed-case name, Title Case.
- **O:** ALL-CAPS title (whole-title casing), sentence case, question opener.
- **L:**
  - title typography on the raw title;
  - R24 and R26 in the title;
  - F24 (≥ 1 RARE21 word in the abstract);
  - F26, now **abstract-only**: F26 words, or U+2011 or en-dash compounds in the abstract. The features_v2 `f26` also fires on title typography; 104 of 3,253 2024–26 F26 papers qualified through the title only.
  - the abstract em dash;
  - a year-specific LLM-style density, from 123 / 150 / 223 excess style words in 2024 / 2025 / 2026.
- The L-union is any binary L marker. It is unchanged by the F26 fix, because F26's title part is a subset of title typography.
- New secondary union: **L-union without R24**.

## H4a. The published record carries NAME titles at the all-submission rate

**Total gain (F4.1, S4.1).**
- **Pooled.** The pooled 2024–26 NAME G_total is 1.021 (95% CI 0.997–1.044).
- **TOST.** The 90% CI of 1.001–1.041 lies inside [0.90, 1.11]. The TOST bootstrap p is < 0.0005: none of 2,000 replicates is beyond a margin. The Holm-adjusted p is 0.0015.
- **By year.** All nine yearly *point estimates* lie inside the pre-registered [0.95, 1.10] band. The 95% CIs lie inside the band only for 2024–26. Before 2024 they extend beyond it on both sides (e.g. 2018: 0.68–1.30), so the pre-2024 "in band" result carries little information.

| Year | G_total | 95% CI | s0 / s3 |
|---|---|---|---|
| 2018 | 0.976 | 0.68–1.30 | 698 / 263 |
| 2019 | 1.034 | 0.84–1.23 | 1,248 / 412 |
| 2020 | 1.050 | 0.89–1.21 | 2,070 / 558 |
| 2021 | 1.039 | 0.89–1.20 | 2,360 / 678 |
| 2022 | 1.003 | 0.89–1.12 | 2,649 / 875 |
| 2023 | 1.016 | 0.93–1.11 | 3,872 / 1,256 |
| 2024 | 1.029 | 0.97–1.10 | 5,765 / 1,778 |
| 2025 | 1.041 | 1.00–1.09 | 8,953 / 2,904 |
| 2026 | 1.009 | 0.98–1.04 | 15,412 / 4,175 |

**Robustness.** TOST holds under:
- raw pooling: 1.012, 90% CI 0.993–1.032;
- dropping the 349 `wd_post` rows: 1.024, 90% CI 1.004–1.044;
- excluding 2026: 1.037, 90% CI 1.008–1.068;
- strict and loose NAME: 1.023 and 1.022.

Earlier periods:
- 2018–23: 1.022 (0.966–1.079);
- 2018–23 without 2019 (PLAN §0 variant): 1.021 (0.962–1.082);
- 2018–22: 1.026 (0.954–1.095).

**Heterogeneity** (`outputs/audit/d4/v03_name_heterogeneity.txt`). The neutral total is not an average of large offsetting subgroups:
- non-LLM topics: 1.00 (0.96–1.03);
- LLM topics: 1.03 (1.00–1.06);
- across the 20 harmonised areas with ≥ 300 papers, point estimates range from 0.38 to 1.48 (interquartile range 0.91–1.05). The extremes are small cells.

**Stages.**
- **Pre-decision stages deplete NAME slightly:**
  - desk 0.998 (0.995–1.000);
  - exit 0.974 (0.965–0.983);
  - desk·exit 0.972 (0.963–0.981).
- **Camera-ready-free:** exit 0.950 (0.936–0.964); desk·exit 0.946 (0.932–0.961).
- **Decision stage:** 1.050 (1.028–1.072).
- **Consistent post-decision-withdrawal definition:** exit 0.975, decision 1.050, desk·exit 0.972.

**Adjusted models (T4.1) do not agree at the stage level.** With year × area FE, log authors, llm_topic and topic100 FE:

| Stage | Raw gain | Adjusted gain (95% CI) |
|---|---|---|
| Exit | 0.972 | 0.993 (0.981–1.005) |
| Decision | 1.046 | 1.019 (0.993–1.044) |

- Both adjusted stage gains are indistinguishable from 1. The opposite-direction stage pattern is therefore largely topic, area and team composition. Only the total is stable: adjusted 1.008 (approximate 95% CI 0.980–1.037).
- The adjusted desk OR is 0.818 (0.683–0.979, p = 0.028). It does not survive BH across the 83 T4.1 tests (q = 0.065).

**The decision stage is not identified against camera-ready retitling** (T4.2).
- **Tipping point.** The NAME G_dec tipping point is 2.92 pp. It lies inside the audit's net-flip DiD of +2.09 pp, whose 95% interval is −2.57 to 6.74 in D4's normal-theory copy and −3.16 to 7.33 in WP4's canonical pseudo-flip interval.
- **Selection-only G_total.** At the audit point it is 0.979. The audit-implied interval is 0.88–1.07 (D4) or 0.87–1.08 (WP4), which crosses the 0.90 margin.
- **WP4's editing-corrected 90% CI** is [0.885, 1.069], which fails the TOST margins. With WP4's partial audit enlargement (interim) it is [0.921, 1.066].

**The 2024 break by pool** (`its_pools.csv`, `its_pools_yearlevel.csv`). The model is the D1 ITS logit, 2018–26, with topic100 FE. The year-level CIs come from OLS on the 9 annual logit prevalences with t(5).

| Pool | Paper-level slope-change OR | 95% CI | p | Year-level OR [95% CI] |
|---|---|---|---|---|
| ACC | 1.053 | 0.977–1.134 | 0.18 | 1.154 [0.928, 1.434] |
| REJ | 1.119 | 1.037–1.206 | 0.004 | 1.174 [0.992, 1.390] |
| WD | 1.107 | 0.992–1.235 | 0.07 | 1.176 [0.935, 1.479] |

- **Equality test.** The paper-level Wald test does not reject equality: χ²(2) = 1.35, p = 0.51. The largest point difference is 0.061 on the log-OR scale (ACC − REJ).
- **Paper-level equivalence.** No pair is equivalent at ±0.1. The 90% CIs are:
  - ACC − REJ: −0.148 to 0.027;
  - ACC − WD: −0.170 to 0.069;
  - REJ − WD: −0.101 to 0.122.
- **Year-level differences.** These are the small-T inference the break actually rests on:
  - ACC − REJ: −0.017, 95% CI −0.109 to 0.074, 90% CI −0.089 to 0.054;
  - ACC − WD: 95% CI −0.290 to 0.252;
  - REJ − WD: 95% CI −0.275 to 0.273.
- **Reading.** There is no evidence of a difference. ACC − REJ is equivalent within ±0.1 only under year-level inference. The WD comparisons are uninformative. CT11 should be read as an equivalence test that is likely underpowered.
- **Variants.** Equality is also not rejected without controls (p = 0.82), for ACC vs REJ over 2017–26 (p = 0.22), or with the compound outcome (p = 0.77).

**Verdict: supported** (Holm p = 0.0015) **for the observed published-vs-submitted NAME share.**
- The claim is "a published-only study observes the all-submission NAME share". It is not "peer review does not select on NAME".
- Neither "review neither creates nor amplifies the fashion" nor "neutral filter" is identified: the decision stage fails the gate, and the selection-only interval crosses 0.90.

## H4b. A small L depletion that is not LLM-specific, and an O shortfall that is not identified as selection

**L-union: the pre-registered tests.**
- **Total.** The pooled 2024–26 L-union G_total is 0.975 (95% CI 0.951–1.001; 90% CI 0.954–0.997), one-sided p = 0.030.
  - Topic- and key-cluster bootstraps give p = 0.025–0.027 (`outputs/audit/d4_ident/chk1`, `d4_code/chk10`).
  - At H4b's Holm step (threshold 0.025; p must be below it) **this is not significant** under any of them.
- **Desk·exit.** 0.981 (0.972–0.992), p < 0.0005; camera-ready-free 0.976 (0.961–0.991). This sub-test passes at the Holm step.
- **Consistent post-decision withdrawals.** Desk·exit 0.985; camera-ready-free 0.981. The depletion shrinks by about 15–20%.
- **By year** (s0 / s3 n in the last column):

| Year | G_total | 95% CI | Desk·exit | 95% CI | n s0 / s3 |
|---|---|---|---|---|---|
| 2024 | 0.977 | 0.912–1.041 | 0.992 | 0.970–1.016 | 5,765 / 1,778 |
| 2025 | 0.955 | 0.904–1.006 | 0.969 | 0.948–0.990 | 8,953 / 2,904 |
| 2026 | 0.983 | 0.952–1.016 | 0.984 | 0.971–0.996 | 15,412 / 4,175 |

- **Robustness:**
  - raw pooling: 0.961 (0.937–0.987);
  - dropping `wd_post`: 0.977 (0.951–1.001);
  - excluding 2026: 0.964 (0.926–1.002).

**The depletion is R24, and R24 was depleted before 2024** (F4.1, `gains.csv`).

*R24 title words* ("enhanc\*", "leverag\*" and similar):

| | Total | Exit | Decision | CRF desk·exit |
|---|---|---|---|---|
| 2024–26 | 0.807 (0.740–0.874) | 0.901 (0.871–0.930) | 0.896 | 0.892 (0.850–0.937) |
| 2018–23 | 0.815 (0.631–1.009) | | | 0.916 |

- Post/pre ratio of total gains: 0.990 (0.788–1.288).
- T4.1 exit OR: 0.723 (0.542–0.965) in 2018–23 vs 0.740 (0.655–0.836) in 2024–26.
- Under the consistent post-decision definition, R24 exit is 0.920 (2025 alone: 0.891 → 0.933).

*L-union without R24* is neutral in 2024–26:
- total 0.998 (0.972–1.027);
- desk·exit 0.994 (0.983–1.005);
- camera-ready-free 0.990 (0.974–1.007).

*Markers with an identified 2024–26 pre-decision depletion:*
- **Abstract style density.** Total 0.965 (0.955–0.975); exit 0.975 (0.971–0.979); camera-ready-free desk·exit 0.963 (0.957–0.970).
  - Re-selecting the excess words inside every bootstrap replicate widens the total CI to 0.956–0.980 (camera-ready-free 0.957–0.971). The re-selected lists have median sizes 115 / 145 / 200 and Jaccard overlap 0.71–0.78 with the full-sample lists.
  - T4.1 exit OR per SD: 0.854 (0.829–0.880), against 0.990 (0.942–1.040) in 2018–23.
- **F24.** Total 0.963 (0.919–1.011); exit 0.970 (0.953–0.988); camera-ready-free desk·exit 0.965 (0.939–0.993).
  - This is new relative to 2018–23 (1.057; post/pre 0.914, 0.849–0.988).
  - It is not new relative to 2018–22 (0.990; post/pre 0.975, 0.893–1.071).

*Markers that are not depleted:*
- title typography: 0.936 (0.730–1.149);
- F26 (abstract): 1.027 (0.978–1.080);
- abstract em dash: 0.979 (0.915–1.049);
- R26: 1.060 (0.967–1.157).

*As unions:*
- title markers 0.915 (0.863–0.970): the R24 genre;
- abstract markers 0.993 (0.964–1.023).

*Typography pilot.* The pilot's 2026 typography gain of 0.79 is not reproduced. The v2 raw-title measure gives 0.914 (0.699–1.138).

**Post vs pre: the non-R24 markers lost a pre-2024 advantage.** The LLM-specific estimand is the post/pre ratio of gains, a difference-in-differences of log gains.

L-union post/pre ratios:

| Stage | vs 2018–23 | vs 2018–22 |
|---|---|---|
| Total | 0.845 (0.783–0.915) | 0.846 (0.772–0.936) |
| Desk·exit | 0.951 (0.927–0.977) | 0.961 (0.935–0.991) |
| Camera-ready-free desk·exit | 0.952 (0.913–0.998) | 0.969 (0.925–1.020) |
| Decision | 0.889 (0.827–0.959) | 0.880 (0.806–0.968) |

- **Without R24** the contrast is larger: 2018–23 total 1.226 and camera-ready-free 1.050, so the post/pre ratios are 0.814 (0.752–0.886) and 0.943 (0.902–0.990).
- **What the contrast shows.** It runs from mild pre-2024 enrichment to neutral, not to depletion.
- **The decision-stage part** (0.889) compares camera-ready accepted text with submission-stage text and is not identified. In 2018–23, too, most of the enrichment sat at the decision stage: 1.118 against desk·exit 1.032.
- **The identified (camera-ready-free) part** is 0.952 against 2018–23. Against 2018–22 it is 0.969, whose CI includes 1. ICLR 2023 accepted abstracts are post-ChatGPT camera-ready text, so 2018–23 is "pre-2024", not "pre-LLM", for accepted-text statistics.
- **NAME** shows no shift: post/pre total 0.999 (0.944–1.062).

**O markers: the published record under-represents them, but selection is not identified.**
- **O-union total.** 0.807 (0.749–0.870). It sits entirely at the decision stage:
  - decision 0.812 (0.757–0.871);
  - desk·exit 0.994 (0.969–1.019).
- **The identified camera-ready-free pre-decision stages enrich O:** 1.035 (1.000–1.072). This is driven by sentence case: camera-ready-free 1.093 (1.046–1.142), decision 0.868 (0.791–0.940).
- **Recasing is a live alternative.** The decision-stage pattern is the same in 2018–23:
  - Title Case decision OR 1.435 (2024–26) and 1.355 (2018–23);
  - ALL-CAPS 0.324 and 0.309.
  - Camera-ready recasing would produce exactly this, and the audit cannot bound it: 0 accepted v1 titles are ALL-CAPS and 7 are sentence case.
- **ALL-CAPS titles.**
  - Total 0.361 (0.260–0.470) pooled; 0.438 (0.268–0.626) in 2026.
  - The **only identified O depletion** is ALL-CAPS at exit: camera-ready-free desk·exit 0.901 (0.817–0.984); T4.1 exit OR 0.598 (0.464–0.771), q < 0.001.
  - It is not new: 2018–23 camera-ready-free 0.948; post/pre 0.951 (0.847–1.064).
- **Pilot comparison.** The pilot's 0.37 described whole-title ALL-CAPS ("ALL-CAPS titles ... accepted at 16.5% vs 40.5%", LITERATURE_BRIEF §3.5), so the casing class is the right comparison. The earlier deviation note claiming the pilot used NAME-lead orthography is withdrawn. The NAME-lead variant (`allcaps_name`) gives 0.922 (0.874–0.972).

**CT6 cannot identify LLM-specific selection.** An L-union G < 1 on held-out data would mostly re-detect the pre-existing R24 genre penalty. A secondary contrast would be needed: the L-union without R24, or the post/pre ratio.

**Verdict: partially supported** (Holm p = 0.059).
- The falsification condition (L-union G_total ≥ 1) is not met at the point estimate. But the total depletion is not significant after Holm.
- The significant pre-decision L depletion is carried by R24, whose depletion pre-dates 2024. The other L markers are neutral in 2024–26 after losing a mild pre-2024 advantage.
- Only F24 and the abstract style density show a new identified depletion, of 3–4%.
- For O, the published record under-represents O titles (descriptive, H4e), but selection is identified only for ALL-CAPS at exit.

## Continuation-ratio models (T4.1)

`T4_1_continuation_ratio.{csv,md}`. Each feature is entered alone, with these controls:
- year × area FE in 2024–26, or year FE in 2018–23;
- log authors, llm_topic and topic100 FE;
- SEs clustered by topic100.

BH q-values cover all 83 tests. Only effects with q < 0.05 are called notable.

**Notable 2024–26 effects (q < 0.05).**
- **Desk** (OR for passing):
  - question opener 0.522 (q = 0.011);
  - F26 (abstract) 0.710 (q = 0.001);
  - abstract em dash 0.760 (q = 0.039);
  - style density 0.820 per SD (q < 0.001);
  - L-union 0.833 (q = 0.027).
- **Exit:**
  - ALL-CAPS 0.598 (q < 0.001);
  - R24 0.740 (q < 0.001);
  - F26 1.156 (q = 0.010);
  - style density 0.854 (q < 0.001);
  - L-union 0.933 (q = 0.045).
- **Decision:**
  - Title Case 1.435;
  - ALL-CAPS 0.324;
  - O-union 0.737;
  - mixed-case name 1.114 (q = 0.023);
  - R24 0.837 (q = 0.015);
  - style density 0.939 (q = 0.013);
  - sentence case 0.833 (q = 0.043).
  - Decision-stage ORs carry the camera-ready caveat.
- **Not notable after BH:** NAME desk (q = 0.065) and F24 exit (q = 0.052).

**Adjusted total gains** (product of stage G_adj; approximate 95% CI treating stage estimates as independent, since the continuation-ratio likelihood factorises over stages):

| Feature | Adjusted total gain | 95% CI (approx.) | Raw total (product of raw stage gains) |
|---|---|---|---|
| NAME | 1.008 | 0.980–1.037 | 1.012 |
| Compound | 1.008 | 0.988–1.028 | 1.009 |
| Mixed-case name | 1.044 | 1.008–1.081 | 1.049 |
| Title Case | 1.016 | 1.011–1.020 | 1.016 |
| ALL-CAPS | 0.387 | 0.282–0.532 | 0.359 |
| O-union | 0.828 | 0.770–0.889 | 0.822 |
| R24 | 0.832 | 0.770–0.899 | 0.815 |
| F24 | 0.948 | 0.900–0.998 | 0.982 |
| L-union | 0.967 | 0.943–0.992 | 0.961 |
| Title typography | 0.994 | 0.797–1.239 | 0.871 |

- **Totals.** Adjustment barely moves the total gains of the listed features, except title typography (0.87 → 0.99, with a very wide CI).
- **Stage gains.** It does move them. NAME exit goes from 0.972 to 0.993 and NAME decision from 1.046 to 1.019, and the opposite-direction NAME stage pattern disappears.

## Decision-stage bound (T4.2)

D4 computed its own copy of the snapshot module from `cache/arxiv_audit.jsonl`. WP4's canonical outputs (`outputs/snapshot/T4_2_tipping_points.csv`, 17:11 UTC) agree on every point estimate. The NAME values are:
- P_s0 0.3563, P_s2 0.3462, P_s3 0.3636;
- DiD +2.085 pp;
- tipping points 2.916 / 1.036 pp.

WP4's primary (pseudo-flip) DiD interval is wider than D4's normal-theory one, so T4.2 reports both, and the gate statements use WP4's:

| | DiD 95% (pp) | Implied G_dec | Implied G_total |
|---|---|---|---|
| D4 copy | −2.57 to 6.74 | 0.928–1.092 | 0.880–1.070 |
| WP4 canonical | −3.16 to 7.33 | 0.917–1.101 | 0.867–1.081 |

**The pairs.**
- There are 331 pre-decision arXiv v1 pairs: 206 accepted, 125 rejected.
- Titles changed in 29.6% of accepted pairs and 23.2% of rejected ones (normalised words).
- **NAME flips:** 7 adds and 6 drops among accepted papers, against 1 add and 3 drops among rejected ones.

**The NAME net-flip DiD.**

| Variant | DiD (pp) | 95% CI |
|---|---|---|
| D4 normal-theory | +2.09 (se 2.37) | −2.57 to 6.74 |
| D4 bootstrap | | −2.63 to 7.08 |
| Audit years 2024–26 only | +3.01 | |
| Population-weighted 2023–26 | +2.07 | |

**Tipping points.** Accepted papers are part of s2 and s0, so D\* = (P3 − P2)/(1 − a2) for G_dec and (P3 − P0)/(1 − a0) for G_total.
- **NAME:** 2.92 pp (G_dec) and 1.04 pp (G_total). The plan's 1.8 pp omitted the 1 − a2 = 0.60 factor.
- **No auditable title feature is identified.** Every tipping point lies inside the audit CI.
- **Unauditable title features** (fewer than 10 accepted v1 titles): ALL-CAPS title, sentence case, question opener, title typography, R24, R26 and snowclones.

**Abstract markers** (WP4 abstract audit, `outputs/snapshot/abstract_audit.csv`, 330 v1 abstracts: 206 accepted, 124 rejected).
- **F24 is auditable.** Accepted papers gain RARE21 words between v1 and the stored abstract: 20 v1-present, +8/−4, 9.7% → 11.7%. Rejected papers lose them: 13 v1-present, +1/−3, 10.5% → 8.9%.
- **The editing DiD** is +3.55 pp (−1.62 to 8.73). It points the way H4c's direction argument assumes, but its CI includes 0.
- **F24 gains are not identified.** The tipping points are −0.23 pp (G_dec) and −0.67 pp (G_total), and the audit-implied G_total is 0.36–1.05.
- **Not auditable:**
  - the em dash, because arXiv writes TeX dashes;
  - F26 words and RARE21 ≥ 2, which have fewer than 10 v1-present accepted abstracts.

**Consequence for the headline.** No acceptance-margin claim about title or abstract features passes the gate. The camera-ready-free desk and exit contrasts, and the diachronic claims, do not depend on the audit.

## H4c. Published-only Kobak bounds understate the excess of LLM-style abstract vocabulary; the size depends on the baseline

The bound uses the share of abstracts with at least one RARE21 word (F24). It is p_Y − q_Y, with the conservative baseline q_Y = max(linear 2021–23 trend extrapolated to Y, max(p2022, p2023)). It is computed separately within each set (F4.3, `kobak_bounds.csv`). Percentile CIs are shown; basic-bootstrap intervals follow below. n = papers in the set that year.

| Year | All (pp), n | Accepted (pp), n | NA pool (pp), n | Accepted/all |
|---|---|---|---|---|
| 2024 | 16.0 [14.9, 17.1], 5,765 | 12.8 [10.3, 15.1], 1,778 | 17.2 [15.9, 18.6], 3,987 | 0.800 [0.658, 0.918] |
| 2025 | 12.2 [11.1, 13.1], 8,953 | 8.7 [5.8, 11.1], 2,904 | 13.2 [12.1, 14.3], 6,049 | 0.714 [0.504, 0.891] |
| 2026 | 6.0 [4.8, 6.7], 15,412 | 3.0 [−0.5, 5.9], 4,175 | 6.5 [5.7, 7.3], 11,237 | 0.502 [−0.081, 0.932] |

**Pilot comparison.** D4 reproduces the pilot's *accepted* bounds (12.8 / 8.7 / 3.0). The all-submission bounds are about 0.2 pp higher than the pilot's: 16.0 / 12.2 / 6.0 against 15.8 / 12.0 / 5.8.

**Inference.**
- **Point criterion.** All three ratios are ≤ 0.85. But P(ratio ≥ 0.85) is 0.209 / 0.078 / 0.079, so the ≥ 15% understatement is **not established in any year**. The intersection-union p is 0.209 (Holm 0.209).
- **Falsification boundary.** P(ratio ≥ 0.9) is 0.0495 / 0.018 / 0.042. The 2024 upper CI of 0.918 is close to 0.9.
- **Direction** (ratio < 1). P(ratio ≥ 1) is 0.001 / < 0.0005 / 0.0075.
- **Bias of the percentile intervals.** The baseline is a max() of noisy prevalences, which is biased upward, so the bound is biased downward and the percentile intervals sit asymmetrically around the point. Basic-bootstrap intervals for the ratios are [0.682, 0.943], [0.537, 0.924] and **[0.071, 1.084] for 2026, which includes 1**. Coverage of these intervals is uncertain.

**Where the gap comes from.** Mainly the baseline years, not the LLM era.
- **2024–26 prevalence is close.** In 2024, accepted abstracts carry a RARE21 word at nearly the all-submission rate: 17.8% vs 19.1%. In 2026 they are equal: 9.3% vs 9.1%.
- **The accepted baseline is higher and rising.** In 2021–23, accepted abstracts went 2.95 → 3.54 → 4.30% (n 678 / 875 / 1,256), while all submissions went 3.35 → 2.49 → 3.12%.
- **ICLR 2023 accepted abstracts post-date ChatGPT** (30 Nov 2022). The WP4 abstract audit shows accepted papers gaining RARE21 words through camera-ready editing (+3.55 pp DiD, CI includes 0).
  - In 2024–26 that editing raises accepted rates, so the understatement is conservative, as the plan argued.
  - In the 2023 baseline it raises the accepted baseline, which *lowers* the accepted bound.
  - The pre-registered direction argument therefore does not cover the baseline years.
- **Post hoc pre-ChatGPT baseline**, max(p2021, p2022): the ratios are 0.9005 [0.766, 1.014], 0.9011 [0.758, 1.017] and 0.995 [0.718, 1.219]. Both 2024 and 2025 are ≥ 0.90, so **the pre-registered falsification condition is met under this baseline**, and every CI includes 1.
- **Other variants:**
  - no-trend max(2022, 2023) baseline: 0.84 / 0.82 / 0.83;
  - ≥ 2-word variant (F24_2): 0.78 / 0.83 / 0.80 under the primary baseline, 0.79 / 0.86 / 0.93 under max(2021, 2022);
  - abstract L-union: 0.84 / 0.82 / 0.91.

**Verdict: partially supported** (Holm p = 0.209).
- The pre-registered rule passes on point estimates under the primary baseline, and the direction (ratio < 1) is significant in each year.
- The ≥ 15% magnitude is not established in any year.
- Under the post hoc pre-ChatGPT baseline the falsification condition is met, and the point estimates are < 1 but all CIs include 1.
- 2026 is uninformative: the accepted bound's CI includes 0, and the basic-bootstrap ratio interval includes 1.

## H4d. The withdrawal excess of named papers is mostly topic composition

**Design** (F4.4, `exit_composition.csv`).
- **Population and outcome.** REJ ∪ WD, 2024–26. The outcome is "withdrawn", with the 2026 post-decision withdrawals counted as withdrawn.
- **Models.** LPMs with year FE, log authors and llm_topic. SEs clustered by last-position profile key.
- **Sample.** Both models use the same sample: 13,185 papers in 3,571 last-position profile keys with ≥ 2 papers, of which 1,957 vary in NAME.
- **Co-primary specification.** After the identification audit, the topic100-FE contrast is reported as co-primary.

| Specification | Cross-section (pp) | Within key (pp) | Difference (pp) |
|---|---|---|---|
| **Pre-registered** (year FE) | +4.06 (se 0.96; 2.17 to 5.95) | −0.70 (se 1.08; −2.83 to 1.42) | 4.77 (se 0.75; key bootstrap 3.21–6.24) |
| **Topic100 FE in both** | +0.84 (se 0.97; −1.05 to 2.74) | −1.74 (se 1.10; −3.89 to 0.41) | 2.58 (se 0.71) |
| Key × year FE (same cycle) | +3.17 | −1.60 | 4.76 |
| Key × year + topic100 FE | −0.20 | −2.65 (−5.20 to −0.11) | 2.46 |

**Who carries the excess.**
- **Full population** (n = 20,419): +5.12 (se 0.91), or +2.58 (se 0.82) with topic100 FE.
- **Single-paper keys** (n = 7,234), which the within design excludes by construction: +6.91 (se 1.36), or +5.60 (se 1.33) with topic FE.
- **Repeat keys.** Once topic is held fixed, nothing remains among keys with ≥ 2 papers (+0.84, n.s.).
- **Measurement error** does not explain the within-key null. The identification audit (`d4_ident/chk3`) finds that 63% of NAME variance is within key; with detector accuracy 0.985 this implies attenuation of only about 0.90.

**Robustness** (pre-registered specification; cross / within / difference, pp):

| Variant | Cross | Within | Difference |
|---|---|---|---|
| Post-decision withdrawals (consistent definition: 66 / 299 / 403 in 2024 / 25 / 26) counted as rejected | +3.38 | −1.47 | 4.86 |
| Post-decision withdrawals dropped | +3.58 | −1.15 | 4.72 |
| Desk rejections included | +3.72 | −0.88 | 4.60 |
| The pilot's "last profile key" definition | +4.06 | −0.72 | 4.79 |

**Before 2024.** In 2018–23 the within estimate is +4.20 pp (se 2.78), against a cross-section of +7.77 (se 2.39).

**Other features.**
- **Same direction, significant cross-sections:**
  - mixed-case name: +4.30 → −0.17;
  - compound: +4.04 → +0.43.
- **Same direction, but the cross-sectional excess is not significant:**
  - F24: +2.08, CI −0.39 to 4.55 → −0.94;
  - L-union: +1.58, CI −0.25 to 3.41 → −0.15; difference 1.72 (se 0.66).
- **O markers** have negative cross-sectional coefficients that move toward 0 within key: O-union −3.16 → +0.33.
- **R24 and R26** stay positive within key: +3.90 and +6.52 pp.

**Verdict: partially supported** (Holm p < 0.001).
- The pre-registered contrast holds: cross > 0, within ≤ 0 at the point, and the two differ. The within CI reaches +1.42 pp.
- The pre-registered reading, "the excess is therefore between authors", is **not supported as a mechanism**:
  - with topic100 FE, condition 1 (cross > 0) fails (+0.84, p = 0.19);
  - among repeat keys nothing remains once topic is fixed;
  - the residual population excess sits with one-off keys. This is consistent with, but not tested as, a between-key effect.

## H4e. A published-only study reproduces mainstream and most LLM-style prevalences within 10%; it misses ALL-CAPS/outsider titles and R24 words, and it halves the 2024 break

**Design.** The atlas has 26 rows (`atlas.csv`, F4.2):
- 24 statistics with a published/all ratio;
- one colon-premium row that is supplementary;
- the peak-year agreement, which has no ratio.

The O and L prevalence rows go beyond the list in PLAN §D4.
- **Effect scale.** OR-type statistics are compared on the effect scale: the ratio of log-ORs, with a delta-method CI from the joint influence-function covariance. Their earlier OR-ratio comparison was close to vacuous near OR = 1.
- **Colon premium.** No accepted-only version exists. The pre-registered colon-premium *trend* enters the M count as a decided-only (ACC vs REJ) analogue; the level is supplementary.
- **Entropy and JSD intervals** are random-selection null bands, not CIs. They are kept out of the 90%-CI count.
- **BH q-values** over all atlas tests are in `atlas.csv`.

**M statistics: 9/11 within ±10%; 9/10 among those computable on accepted papers.**

| Statistic | All | Accepted | Ratio (95% interval) | Within ±10% |
|---|---|---|---|---|
| NAME | 35.6% | 36.4% | 1.021 (0.998–1.045) | yes |
| Compound | 53.3% | 54.3% | 1.018 (1.002–1.034) | yes |
| Phrase colon | 17.7% | 17.9% | 1.012 (0.973–1.051) | yes |
| Mixed-case name | 23.2% | 24.6% | 1.059 (1.029–1.091) | yes |
| Title Case | 92.9% | 94.5% | 1.018 (1.013–1.022) | yes |
| Snowclone share | 1.08% | 0.98% | 0.908 (0.747–1.068) | yes (knife-edge) |
| LLM abbreviation-only share (among LM-naming titles) | 49.2% | 49.3% | 1.002 (0.961–1.041) | yes |
| ITS slope change, NAME, 2018–26 (log-OR) | 0.102 (OR 1.107) | 0.051 (OR 1.053) | **0.50 (−0.15 to 1.16)** | **no** |
| Colon-premium trend, 2018–26 (log-OR/yr; decided-only) | −0.035 | −0.031 (s2) | **0.89 (0.66–1.12)** | **no** |
| Opener entropy (NAME-collapsed, rarefied) | 6.893 bits | 6.789 bits | 0.985 (null band 0.974–0.996; random-selection p = 0.014) | yes |
| Lexical-turnover JSD | 0.2363 | 0.2342 | 0.991 (null band 0.977–1.006) | yes |
| *Supplementary:* colon premium, 2024–26 (decided-only) | log-OR 0.018 (se 0.031) | 0.052 (s2) | 2.88; difference +0.034 (0.009–0.058) | no |

- **The 2024 break.** A published-only study recovers the NAME prevalence level, but it estimates the 2024 slope break at half the all-submission log-OR.
  - It also does not detect the break: the ACC pool's slope-change OR is 1.053, p = 0.18, against REJ's p = 0.004.
  - The earlier OR-ratio comparison (0.951) hid this.
- **The colon premium.** The all-submission colon premium is itself near 0, so its relative error is ill-conditioned. A decided-only study overstates it by +0.034 log-OR.
- **Peak years of the top-30 fashions.** Accepted-only peaks agree with all-submission peaks for 67% of words. Random subsets of the same size agree for 65% (95% band 47–83%).
- **90% CIs.** Among the M statistics with sampling CIs, 6 of 9 lie inside ±10%: NAME, compound, phrase colon, mixed-case name, Title Case, LLM abbreviation-only. The snowclone share, the ITS ratio and the colon trend do not.
- **Yearly M prevalences.** These are the yearly accepted/all ratios, i.e. the G_total by year in `gains.csv`. NAME is within ±10% in every year 2018–26. The other M features are reported in `results.json` → H4e `M_yearly_total_gain_within_10pct`.

**O statistics: 1/4 within ±10%** (median |log ratio| 0.160):
- ALL-CAPS 0.361 (0.260–0.470);
- O-union 0.807 (0.747–0.867);
- question opener 0.899 (0.776–1.023);
- sentence case 0.905 (0.822–0.986).

Question opener and sentence case sit on the 0.90 knife-edge, as does the M snowclone share (0.908). Their within/outside classification is not meaningful.

**L statistics: 7/9 within ±10%** (median |log ratio| 0.037):
- The outliers are R24 prevalence, 0.807 (0.736–0.876), and the Kobak bound, 0.717 (0.495–0.888). The Kobak bound is fragile to the baseline (H4c).
- The L-union ratio is 0.975 (0.951–1.000).

**Where the gaps arise** (F4.2 panel b).
- **Decomposition.** Each gap log(T_s3/T_s0) is split into desk, exit and decision parts.
- **Desk and exit** compare exiting papers with survivor sets that contain camera-ready text, so they are not exact selection. The camera-ready-free versions are in `atlas.csv`. For NAME, the exit part is −0.026 observed and −0.051 camera-ready-free.
- **The decision part is not separable** into selection and editing for any statistic. For auditable title features, the audit-implied editing interval is shown as a whisker (NAME: −0.047 to +0.148). For the O-union it is unbounded.

**Verdict: partially supported (descriptive).**
- Prevalence-type M statistics are within ±10%, and the deviations concentrate in O and L: median |log ratio| 0.018 (M), 0.160 (O), 0.037 (L).
- The ITS break (effect scale) and the colon-premium trend are not within ±10%.
- "Trends within a few percent" is withdrawn.

## Exploratory (not confirmatory)

**Exit timing, 2025–26** (`exit_timing.csv`, `exit_calendar.csv`).

*Calendar check.*
- **Review release.** Withdrawal dates (`modification_ms`) spike on 2024-11-15 (240) and 2025-11-12 (463). The review releases were around 12 November.
- **Decisions.** They also spike on decision days: 2025-01-23 (54) and 2026-01-26 (108).
- **Baseline.** The median day has 2–3 withdrawals.

*Findings.*
- **NAME in the first week after reviews.** Papers withdrawn in that week carry NAME titles more often than rejected or accepted papers:

| Year | Week-1 withdrawals | Rejected | Accepted |
|---|---|---|---|
| 2025 | 0.417 [0.384, 0.451], n = 832 | 0.299 [0.285, 0.314], n = 3,674 | 0.345, n = 2,904 |
| 2026 | 0.457 [0.432, 0.483], n = 1,444 | 0.379 [0.367, 0.391], n = 6,440 | 0.408, n = 4,175 |

  This reproduces the C3 pilot (.42/.46 vs .30/.38). Topic composition was not adjusted here (see H4d).
- **2026 post-decision withdrawals.** These are timestamp-defined: on or after the decision day, n = 403, including the 349 `wd_post` rows.
  - They are the most NAME-heavy phase: 0.489 [0.440, 0.538].
  - Their L-union share, 0.434 [0.387, 0.483], is second to the small early-withdrawal group: 0.492 [0.368, 0.616], n = 59.

**Early vs late 2026 desk rejections: not testable.** All 737 desk-rejection timestamps in 2026 fall on or after the decision date; 712 are on 2026-02-12. They record a bulk post-decision update, not the desk-rejection date. In 2025, 94% of the 53 desk rejections have pre-decision timestamps, which is too few to split.

## Implications for the study thesis (PLAN §1)

The PLAN §1 bullet "Peer review neither creates nor amplifies the naming fashion … Review does deplete LLM and outsider markers, so studies of published papers alone are nearly unbiased for mainstream title fashion but understate how many submitters used LLMs" is not supported as written. PLAN.md is locked and was not edited here. Suggested replacement:

> The published record carries NAME titles at the all-submission rate (TOST passes); whether review itself selects on NAME is not identified. Desk rejection and withdrawal remove titles of a pre-existing incremental genre (R24 words such as "Enhancing … via …"), as they did before 2024, and, in a new pattern, a few percent of abstracts with LLM-style vocabulary. The decision stage is neutral for LLM markers, and outsider (ALL-CAPS, sentence-case) titles are under-represented among published papers for reasons the audit cannot separate from camera-ready recasing. Published-only Kobak-style bounds understate the all-submission excess of LLM-style vocabulary by 20–50% with the conventional 2021–23 baseline, but by only about 0–10% with a pre-ChatGPT baseline. A published-only study recovers mainstream title prevalences within a few percent but halves the 2024 NAME break.

## Deviations from PLAN.md (all logged in `results.json` → `deviations`)

1. **Pooling.** Pooled gains are year-standardised; raw pooling is robustness. PLAN does not specify the pooling. The choice was not separately timestamped.
2. **Frame.** The 71 OTHER rows of 2018 are dropped.
3. **ALL-CAPS** is the whole-title casing class, which matches the scout record. The earlier claim that the pilot used NAME-lead orthography is withdrawn. `allcaps_name` (0.922) is secondary.
4. **L-union** covers the binary L markers only. Em dash means the abstract em dash.
5. **F26** in the L set is abstract-only. The features_v2 `f26` is kept as the secondary `F26_incl_title`.
6. **Style density** re-implements the scout rule on the frozen scout style pool (`analyses/d4_lexicon.json`). The bootstrap re-selects the words in every replicate. The T4.1 density ORs still condition on the full-sample list.
7. **Tipping point** includes the accepted share of s2: D\* = (P3 − P2)/(1 − a2). This gives NAME 2.9 pp, not the plan's 1.8 pp.
8. **Snapshot module.** D4's copy is computed from `cache/arxiv_audit.jsonl`. WP4's canonical outputs agree on point estimates but have a wider primary interval. Both are reported, and the gate uses WP4's. WP4's abstract audit makes F24 auditable.
9. **Colon premium.** The analogue is decided-only. The pre-registered trend is counted; the level is supplementary.
10. **OR-type atlas statistics** are compared on the effect (log-OR) scale.
11. **Entropy and JSD intervals** are random-selection null bands, not CIs.
12. **H4c baseline.** A post hoc max(2021, 2022) baseline was added. Under it the falsification condition is met.
13. **Post-decision withdrawals.** The primary follows `_core.pool_flags` (2026 `wd_post` only, as PLAN §0 and the frozen CT6). The consistent cross-year definition is reported for exit, decision and pre-decision gains and in H4d.
14. **H4d specification.**
    - Population: REJ ∪ WD, 2024–26.
    - Last position: the maximum list position (the D2 convention).
    - Controls: year FE, log authors, llm_topic.
    - The topic100-FE contrast is co-primary.
15. **Multiplicity.** Holm over {H4a–H4d} with intersection-union p-values. BH over T4.1 and the atlas.
16. **Desk stage.** Desk-stage logits are fitted for 2024–26 only. The 2026 early/late desk-rejection analysis was dropped as not testable.

## Limitations

- **The decision stage is the weak link.** With 331 audit pairs, the NAME DiD has an se of 2.4 pp, and no acceptance gain for any title or abstract feature is identified.
  - The em dash and casing cannot be audited through arXiv.
  - F24 is auditable but not identified.
  - Every "editing" statement about other abstract markers rests on the stated direction assumption, and H4c shows that assumption can fail for baseline years.
- **Desk and exit are not pure selection.** The survivor sets contain camera-ready accepted text, and rejected papers may have revised their titles during the rebuttal (no revision history). The camera-ready-free variants address the first issue only.
- **The desk stage matters in 2026 only.** Desk-rejection reasons are not observed. Selection at ICLR may understate selection at stricter venues; this is untested.
- **The L markers are not LLM use.** Before 2024 the same words were more common among accepted papers than among all submissions, and most of that pre-2024 excess sat at the decision stage. The post-2024 change is relative to that baseline. It is not evidence that reviewers detect LLM use.
- **H4d is within-key, not within-person.** Within-key variation is self-selected: 1,957 keys vary in NAME. Topic composition explains most of the cross-sectional excess.
- **Small T.** The pool-specific break rests on 9 annual cohorts. Year-level intervals are wide, especially for WD.
- **Atlas uncertainty differs by statistic.**
  - Paper bootstrap for the prevalences and the Kobak bound. The Kobak percentile intervals are biased by the max() baseline.
  - Delta-method influence-function covariance for the ITS and the colon premium.
  - A random-selection null band for entropy and JSD.
  - No interval for the peak-year agreement beyond the random null.

## Files

**Scripts:** `src/analyses/d4_stage_gains.py`, `d4_bias_atlas.py`, `d4_exit_composition.py`, `d4_collect.py`, `d4_lexicon.json`. Audit checks are in `outputs/audit/d4/` (fixer) and `outputs/audit/d4_{code,ident,reporting}/` (auditors).

**Figures** (each as PDF, PNG and CSV):
- `fig_F4_1_stage_ladder`: the decision stage is drawn hollow (not identified); off-scale values carry their CIs.
- `fig_F4_2_bias_atlas`: effect-scale OR rows; null bands dashed; every decision part hatched as not separable; a stage palette distinct from the class colours.
- `fig_F4_3_kobak_bounds`: panel a starts at 0; panel b extends below 0; ratio CIs annotated.
- `fig_F4_4_exit_arrows`: adds the topic100-FE NAME row, the full control list and n.
- `fig_S4_1_total_gain_by_year`: log-scale axis label; the band is labelled NAME only.

**Tables:**
- `summary_table.md` (auto-generated)
- `T4_1_continuation_ratio.{csv,md}` (with BH q) and `T4_1_adjusted_total.csv` (with approximate CIs)
- `T4_2_audit.md` (with WP4 intervals), `T4_2_audit_flips.csv`, `T4_2_decision_bound.csv`
- `gains.csv`, with variants `primary`, `drop_wd_post`, `wd_decided_in_s2`, `wd_postdec_ts`, `density_reselect`, `post_vs_pre` and `post_vs_pre_1822`
- `prevalence_by_stage.csv`
- `its_pools.csv`, `its_pools_yearlevel.csv`
- `kobak_bounds.csv` (with basic-bootstrap intervals and n), `kobak_series.csv`
- `atlas.csv` (with effect-scale, camera-ready-free and BH columns), `atlas_peaks.csv`
- `exit_composition.csv` (with single-paper-key and key × year specifications), `exit_timing.csv`, `exit_calendar.csv`
- `audit_pairs.csv`, `style_density.parquet`, `style_density_words.json`

**Machine-readable:** `results.json` (all hypotheses, the Holm table, verdicts with qualifiers, robustness, exploratory analyses, deviations and code hashes), `stage_gains.json`, `bias_atlas.json`, `exit_composition.json`.

## Audit response

Three audits were run: code (D4-1 to D4-12), identification (I1 to I9) and reporting (R1 to R25). Each issue was re-checked with code before it was changed. Verdicts changed for H4b, H4c, H4d and H4e.

| Issue | Valid? | What changed | Claim weakened |
|---|---|---|---|
| D4-1 / I5 / R4 | Yes | ITS slope change and colon premium compared on the effect scale (ratio of log-ORs, delta-method CI). The pre-registered colon-premium trend replaces the level in the M count; the level is supplementary. | H4e M 11/11 → **9/11** (accepted-only 9/10). The ITS break on accepted papers is half the all-submission value (0.50, −0.15 to 1.16) and not detected in ACC. "Trends within a few percent" withdrawn. |
| D4-2 / R8 | Yes | Holm over {H4a–H4d} with intersection-union p-values in `d4_collect`; Holm table in `results.json`. | H4b Holm p 0.059: the L-union total depletion is **not significant** after Holm. |
| D4-3 / I8 | Yes | "Exact" and "needs no audit" removed. Camera-ready-free contrasts reported alongside desk and exit gains in `gains.csv` and `atlas.csv`; F4.2 relabelled. | The O-union pre-decision gain becomes an enrichment camera-ready-free (1.035). |
| D4-4 | Yes | Reversal stated on pre-decision and camera-ready-free gains only; 2018–22 baseline added (`post_vs_pre_1822`); 2018–23 renamed "pre-2024". | The camera-ready-free L-union post/pre is 0.952 vs 2018–23 but 0.969 (CI includes 1) vs 2018–22. The decision part (0.889) is labelled unidentified. |
| D4-5 / R17 | Yes | Consistent post-decision-withdrawal variants (`wd_decided_in_s2`, `wd_postdec_ts`) reported for exit, decision and pre-decision gains. The tautological G_total line was removed. | L-union desk·exit 0.981 → 0.985; R24 exit 0.901 → 0.920 (depletion about 15–20% smaller). The primary is unchanged (PLAN §0 / CT6 definition). |
| D4-6 | Yes | H4d `wd_post_as_rejected` and new `wd_postdec_dropped` use the consistent definition. | None: difference 4.86 / 4.72 pp. |
| D4-7 / R25 / R16 | Yes | Verdicts are computed from falsification flags, the Holm p and sub-tests; notes and the summary table are templated from the outputs. "Fixed before any estimate" qualified. The 0.946 label is corrected (camera-ready-free desk·exit; exit alone 0.950). | |
| D4-8 | Yes | Entropy and JSD intervals labelled as random-selection null bands, excluded from the 90%-CI count, and drawn dashed in F4.2. | |
| D4-9 / R6 | Yes | BH q in T4.1 (83 tests) and the atlas; only q < 0.05 effects called notable. | NAME desk OR (q = 0.065) and F24 exit (q = 0.052) are no longer notable. |
| D4-10 | Yes | F26 abstract-only in the L set; `f26` kept as `F26_incl_title`. | None: the L-union is unchanged; F26 total 1.023 → 1.027. |
| D4-11 | Yes | Style-density words re-selected in every bootstrap replicate (`density_reselect`). | None: the total CI widens from 0.955–0.975 to 0.956–0.980. |
| D4-12 | Yes | P(ratio ≥ 0.85) and P(ratio ≥ 0.9) reported; H4c in the Holm family. | H4c: ≥ 15% magnitude not established (IUT p 0.209). |
| I1 | Yes | L-union without R24 added; post/pre ratios for every L marker against two baselines; H4b reworded; CT6 caveat added. | H4b "LLM markers are depleted" → depletion is R24-driven and pre-dates 2024; "the depletion is a reversal" withdrawn for the L-union. |
| I2 / R3 | Yes | The O verdict is now descriptive (under-representation); selection is identified only for ALL-CAPS at exit (camera-ready-free 0.901). | "Supported (large) for O" withdrawn. |
| I3 | Yes | Suggested thesis rewrite in "Implications for the study thesis". PLAN.md itself is locked and not edited. | "Review does deplete LLM and outsider markers" not supported. |
| I4 / R5 | Yes | Topic100-FE contrast co-primary; single- vs multi-paper-key split; key × year specifications; "between authors" removed. | H4d → partially supported; the mechanism is mostly topic composition. |
| I6 | Yes | Year-level (t(5)) CIs for pool breaks and differences (`its_pools_yearlevel.csv`). | Pool equality: "no evidence of a difference; equivalence not established (WD uninformative)". |
| I7 | Yes | Thesis wording proposed; topic and area heterogeneity reported. | "Neither creates nor amplifies" not identified. |
| I9 | Partly | No revision history exists to test it; caveat added with the audit evidence (23.2% of rejected stored titles differ from v1; 4 of 8 rejected sentence-case v1 titles recased, not 3 as the auditor reported). | REJ-vs-WD contrasts may mix selection with rebuttal editing. |
| R1 | Yes | WP4 abstract audit cited: F24 auditable, DiD +3.55 pp (−1.62 to 8.73), not identified; em dash unauditable. Limitations updated. | |
| R2 | Yes | The post hoc baseline meets the falsification condition (0.9005 / 0.9011); "direction robust" replaced by "point estimates < 1, post hoc CIs include 1". | H4c stays partially supported, with the qualifier. |
| R7 | Partly | The scout record shows the pilot measured whole-title ALL-CAPS, so the casing class *is* the right comparison. Deviation 3 is wrong and was corrected, rather than the H4b sentence. | |
| R9 | Yes | H4e heading retitled; knife-edge 0.90 cases noted. | |
| R10 / R11 / R12 / R13 / R14 | Yes | Figures redrawn as listed under Files. | |
| R15 / R20 / R21 / R22 / R23 | Yes | 9.1%; pilot reproduces accepted bounds only; "R26 not depleted"; F24 and L-union H4d cross-sections not significant; wording ("pre-2024", "more common among accepted papers", "excess of LLM-style vocabulary", untested venue extrapolation); CIs and n added; 2019 variant reported; atlas counts restated (26 rows, 24 with ratios). | |
| R18 | Yes | Post-decision group defined (n = 403); it is the most NAME-heavy, but its L share is second to early withdrawals. | |
| R19 | Yes | WP4 canonical intervals reported side by side, and used for gate statements. | Deviation 8 rewritten. |
| R24 | Yes | Basic-bootstrap intervals added to `kobak_bounds.csv`; the bias of the max() baseline is noted. | 2026 ratio basic interval [0.071, 1.084] includes 1. |
