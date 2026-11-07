# Dossier: registered and descriptive core (authoritative fact sheet)

Built 2026-11-03 from committed files only (read-only). Every number below was read from the file named in its
"Source" cell, or (marked **[derived]**) computed here from a committed, outcome-free file or from a committed result
file (e.g. a CI = coef ± 1.96 SE from a results CSV). No acceptance/decision column was read; no outcome script was run.

Abbreviations for sources:
- **RES** = `research/fashion/RESULTS.md`
- **PRE** = `research/fashion/PREREGISTRATION.md`
- **TOP** = `research/topics/README.md`
- **QA** = `research/fashion/presentation/qa.md`
- **SL** = `research/fashion/presentation/shortlist.md`
- **ROOT** = `README.md` (repo root)
- **RQ1J** = `research/fashion/output/rq1_summary.json`; **RQ1C** = `research/fashion/output/rq1_results.csv`
- **FR2 / FR3 / FRX** = `research/fashion/output/frozen_run/rq2_results.csv`, `rq3_results.csv`, `exploratory_estimates.csv`
- **CONF** = `research/fashion/output_pooled/confirmation_run/summary.json`
- **HC** = `research/topics/output/hindsight_check.json`
- **FC** = `research/fashion/output/ph5_forecast/summary.json` (+ `b4_conditional.csv`)
- **LAB** = `research/topics/output/paper_contributions.csv.gz` (outcome-free labels)

## 0. Evidence tiers and mandatory wording

### Tier legend (use exactly these in the paper's evidence column)

| Tier | Meaning |
|---|---|
| **A** | Registered before the discovery run (or registered for held-out before any held-out data) **and** supported on the held-out split |
| **B** | Post hoc in discovery (declared before run), then a held-out test registered/declared before the held-out run, and that test supported |
| **C** | Registered (discovery and/or held-out) but inconclusive, not supported, or not replicated |
| **D** | Discovery-only exploratory (planned E-analyses) or post hoc; no held-out support |
| **E** | Descriptive / outcome-free (no acceptance outcome); measurement or method facts |

Note on H2b/H2c: the registered discovery prediction was *wrong-signed* (verdict "significant in the opposite
direction"); the reversed hypotheses H2b′/H2c′ were registered after discovery, before any held-out data, and were
supported held-out. Label as **A (reversed registered prediction)** — always say the original registered herding
prediction failed.

### Wording rules (verbatim-safe)

| Rule | Exact source wording / requirement | Source |
|---|---|---|
| Associations only | "All results are associations within topic and year. None is a causal effect of choosing a topic, a team or a contribution type." | RES, preamble (lines 70–71) |
| Held-out status | "a pre-registered out-of-sample replication, not a certified untouched independent holdout. It is a split-sample replication within the same ICLR years." | RES, update box (lines 4–6); "Held-out replication → Design → Data status" |
| Held-out spoken form | "the released former confirmation split, which we had never analysed: a pre-registered out-of-sample replication, not a certified untouched holdout." | QA, "Three habits" |
| Held-out guards against | analyst overfitting to discovery papers, **not** year- or reviewer-specific patterns (splits share conference-years, topic-year cells, reviewer pools, authors; features built jointly) | RES, Limitations; Design |
| Underpowered nulls | Non-supported test with estimate below MDE80 = "uninformative", "not evidence of no association" / not "no effect" | RES, "MDE80 and reading rules"; QA "Three habits" |
| Supported held-out sizes | "The replication supports the direction, not the size." Held-out estimates larger than discovery's "do not show that the effect is as large or larger" | RES, Interpretation |
| Never "causes" | Say "goes with" / "is associated with" | QA, "Three habits" |
| Pooled re-run | "It confirms nothing" (≈80% of each pooled sample is discovery papers; pooling changes discovery features) | RES, "Pooled re-run (exploratory)" |
| Unregistered held-out rows | two-sided, unadjusted, "not interpreted as findings"; do not quote discovery null readings of E2/P2 without held-out and pooled rows | RES, "Unregistered rows" |
| Secondary PH5 tests | one-sided 0.05, unadjusted; "6 secondary tests, so one false positive would not be surprising" | RES, update box |
| Labels | reference labels are **LLM** labels, not human; agreement "shows consistency between LLM labellings more than human-level validity" | RES, Data → Contribution labels |
| Newcomer | "no author with an earlier ICLR submission in that topic" (any outcome; exact author IDs) — not "no author published" | RES, Constructed variables; PRE post-run record (audit C) |
| P1b (novelty floor) | "did not replicate"; "should not be presented as replicated"; field-novelty tail remains discovery-only | RES, Interpretation |
| FL | "not confirmed"; acceptance gap "stands as discovery evidence only"; do not say "scam" | RES Interpretation; QA §4 |
| One venue | results are for ICLR only; held-out tests replication on unseen ICLR papers, not generalisation to other venues | RES, Limitations |

## 1. Data provenance and corpus

| Item | Claim | Number | Tier | Source |
|---|---|---|---|---|
| Corpus origin | Provenance-preserving ICLR corpus built from **our own dated acquisitions of official OpenReview records** | 55,938 reconciled submission instances | E | RES, Data → "Data sources"; QA §1 |
| Fields used | titles, abstracts, author-declared keywords, primary areas, author lists, decisions — all from the selected official submission metadata; keyword preprocessing our own | keyword cleaning: 40,930 canonical expressions | E | RES Data sources; QA §1 |
| Discovery export | discovery submissions / author-list positions, 2017–2026 | 43,516 submissions; 219,719 declared author-list positions (not distinct people) | E | ROOT, intro |
| Discovery analysis corpus | submissions with a usable abstract (≥30 words) | **43,480** (36 lack usable abstract: 34 placeholders, 2 genuine but malformed) | E | RES Data; TOP "How it was built" step 1 |
| Includes | rejected and withdrawn submissions (avoids survivorship bias) | — | E | QA §1 "Why ICLR?" |
| Papers by era (discovery) | 2017–20 / 2021–23 / 2024–26 | 4,472 / 8,881 / 30,127 (2024–26 = 69%) | E | HC `papers_by_era`; TOP Hindsight check ("69% of papers are from 2024–2026") |
| Papers per year (discovery, labelled) | 2017 → 2026 | 384, 770, 1,248, 2,070, 2,360, 2,649, 3,872, 5,765, 8,951, 15,411 | E | LAB **[derived]** (row counts by year) |
| Re² (Zhang et al., 2025, arXiv:2505.07920; `Daoze/ReviewRebuttal`) | Audited; first considered as main dataset; **not pooled**. Main-conference ICLR coverage ends 2023 and omits 2019; conversations contain training-format placeholders; rebuttal train/test partitions share 475 paper IDs → motivated own collection | — | E | RES Data sources; QA §1 |
| Louis archive (`MlouisBE/iclr-rebuttal-analysis`) | separate archive layer for source comparison and identity reconciliation; added no submissions; no Louis text fallback in clean corpus; **not pooled** | — | E | RES Data sources; QA §1 |
| Paper Copilot (Yang, Wei & Pei, 2025, arXiv:2510.13201) | metadata comparisons; lineage of reconstructed 2024–25 score pairs (reach us via Louis archive); study uses **no review scores**; **not pooled** | — | E | RES Data sources; QA §1 |
| Held-out release | released former-confirmation split; source policy does **not** certify untouched independent holdout (`independent_confirmation_available: false`; `holdout_retired: true`) | 11,113 released; **11,099** with abstract; released 2026-10-18 | E | ROOT; PRE 2026-10-18 §A; RES Design |
| Held-out by year | 2017 → 2026 | 105, 212, 309, 500, 603, 704, 995, 1,445, 2,284, 3,942 | E | CONF `papers.by_year` |
| Held-out decided | decided / decided in 2018–26 (acceptance-test population) | 8,284 / 8,185 | E | SL "After the held-out run"; QA Numbers |
| Held-out source exclusions | source excluded 1,309 pending family/link cases; assignment mechanism undocumented | 1,309 | E | QA §5 |
| Pooled corpus | discovery ∪ held-out (exploratory only) | 54,579 | E | RES Data; PRE 2026-10-18 §A |
| Held-out text | post-decision abstracts; no link-removed (cleantext) check | — | — | RES Design → Labels; Limitations |
| Text caveat (discovery) | text is the September 2026 snapshot, may differ from submitted version; accepted abstracts more often camera-ready (2023–26: 17.6% accepted vs 0.5% rejected carry a code link) | 17.6% vs 0.5% | E | TOP Limitations; SL "Robustness to camera-ready text" |

## 2. Measurement: topics, labels, newcomer definition

### 2a. Topic layer

| Item | Claim | Number | Tier | Source |
|---|---|---|---|---|
| Embedding | `title [SEP] abstract` with SPECTER2 (`allenai/specter2_base` + proximity adapter) | — | E | TOP "How it was built" |
| Clustering | unit-length PCA(128) (93% variance), spherical k-means k = 100 (best of 3 seeds × 20 inits); broad 20 (Ward); fine 198 | — | E | TOP "How it was built" |
| Outcome-blind | no acceptance/decision/review field read in topic layer (checked by `validate_outputs.py`) | — | E | TOP intro |
| Topic sizes | middle topics 127–1,121 papers; 91 topics (94% of papers) have ≥30 papers in ≥3 years | — | E | TOP "Which level to use" |
| Agreement with ICLR primary areas (NMI, 2024–26) | SPECTER2 middle vs TF-IDF/LSA word-count baseline | 0.302 vs 0.272 | E | TOP Quality evidence table |
| Stability | middle ARI across seeds 0.66 (0.63–0.69); median middle Jaccard 0.66; 26 middle topics < 0.5 | — | E | TOP Quality evidence |
| Synonym overlap (middle) | SPECTER2 vs word counts | 0.67 vs 0.46 | E | TOP table |
| Blind name check | correct fine topic 61% (chance 10%); correct middle topic 80% | — | E | TOP Quality evidence |
| Coherence | mixed: 3/100 middle, 9/198 fine | — | E | TOP Quality evidence |
| Keyword typing | 912 keywords (≥20 papers), 2 annotators, κ 0.93 (96.6% agreement), 31 adjudicated; same model → consistency not validity | — | E | TOP "How it was built", Quality evidence |
| Annotators | Claude agents (October 2026) | — | — | TOP "How it was built" |

### 2b. k-sensitivity (topic quality; TOP "Sensitivity to k")

| k | Papers in trackable topics | NMI w/ primary areas | ARI | Synonym overlap | Keyword coherence | NMI with k=100 |
|---|---|---|---|---|---|---|
| 50 | 100% | 0.294 | 0.77 | 0.77 | 0.26 | 0.72 |
| 75 | 97% | 0.302 | 0.74 | 0.72 | 0.27 | 0.80 |
| **100** | **94%** | **0.302** | **0.68** | **0.67** | **0.29** | 1 |
| 150 | 76% | 0.301 | 0.62 | 0.67 | 0.31 | 0.78 |
| 200 | 53% | 0.302 | 0.57 | 0.64 | 0.33 | 0.75 |

- k = 100 "a design choice, not tuned"; chosen before sweep. Adjacent solutions nest only partly (76–82% of a finer
  topic's papers in one coarser topic). Tier E. Source: TOP "Sensitivity to k".
- Across k (pooled maps), 28–33% of topics are emerging, holding 40–44% of 2024–26 papers — **but TOP says "Do not
  report them as findings"** because they depend on the fitting years. Source: TOP "Sensitivity to k".

### 2c. k-sensitivity of registered tests (counted variants; discovery)

| Test | k = 75 | k = 100 (main) | k = 150 | Source |
|---|---|---|---|---|
| H1d, pp for 0 → 100% FM | −8.70 (p 0.001) | −7.98 [−12.14, −3.82] | −7.47 (p 0.0009) | RQ1C (k75, main, k150 rows); QA §1 table (−8.7/−8.0/−7.5) |
| H2b, pp | +3.06 [+1.87, +4.25] | +3.71 [+2.61, +4.80] | +3.87 [+2.74, +4.99] | FR2 |
| H2c, pp | −1.51 [−2.25, −0.76] | −1.70 [−2.46, −0.93] | −1.81 [−2.47, −1.14] | FR2 |
| H3a, pp per log unit | −1.54 [−3.53, +0.45] | −1.68 [−3.68, +0.32] | −1.33 [−3.14, +0.48] | FR3 |
| H2a, pp | −1.39 [−4.29, +1.51] | −0.73 [−2.68, +1.22] | +0.37 [−1.19, +1.94] (only sign change) | FR2; QA §1 |

Tier E (robustness fact). QA: "Same sign and similar size at every k; H3a is inconclusive at every k."

### 2d. Contribution labels

| Item | Claim | Number | Tier | Source |
|---|---|---|---|---|
| Codebook | one primary contribution type per paper; fixed LLM codebook prompt v1 (sha256 `aaa1478f…`); classes method (incl. `model` = new architecture), theory, empirical, dataset_benchmark, evaluation, other | — | E | RES Data; PRE "Data and units" |
| Labeller | Claude Haiku subagents, prompt v1 unchanged, batches of 100 (logged deviation from planned external run) | — | E | PRE Deviations 2026-10-15 |
| Quality gate | registered: ≥93% agreement with pilot 300 and second-pass κ ≥ 0.80; achieved 97.7% and κ 0.93 | — | E | PRE Data and units; Deviations |
| Reference set | 2,300 papers labelled by **LLM annotators** (not humans): main-class agreement 95.8% overall (pilot 300: 97.7%; training 200 double-labelled: 95.5%; training 1,800 single: 95.6%) | — | E | RES Data → Contribution labels |
| Blind second pass (discovery) | 2,174 papers: κ 0.93 overall; method κ 0.933 (agreement 97.5%); measurement κ 0.949 (99.3%) | — | E | RES Data; RES RQ2 header (D11) |
| Error rates vs LLM reference (random stratum) | FP / FN: method 0.084 / 0.011; measurement 0.005 / 0.070 | — | E | RES Data |
| Held-out second pass | 555 papers: main class 96.9% (κ 0.931); method 98.0% (0.949); measurement 99.1% (0.923); FM 98.2% (0.960) | — | E | RES Design → Labels; PRE §B |
| Human check | presenter "hand-checked a small random sample"; larger human validation is future work | — | — | QA §1 |
| "Measurement" | primary class dataset_benchmark or evaluation | base 7.7% (RQ2 pop.) | E | PRE Variables; RES RQ2 |
| "FM" | paper uses or adapts a large pre-trained model (LLM, CLIP, pre-trained diffusion), same codebook | — | E | QA §1 |

### 2e. Newcomer / incumbent definition and the 2021 author-ID switch

| Item | Claim | Number | Tier | Source |
|---|---|---|---|---|
| Definition | *incumbent* paper: ≥1 author ID (exact `declared_id_key`) has an earlier discovery submission (any outcome) in the same topic; *newcomer* paper: none has. Strictly before year t; history from 2017; recomputed per map; names not matched | — | E | RES Constructed variables; PRE D1–D2 |
| ID switch | 2017–2020 author IDs are 98–99.6% email-based; 2021 85% profile-based; 2025–26 100% profile-based; email and profile IDs not linked | — | E | PRE pre-run log (facts checked) |
| Consequence | pre-2021 history hidden in all later years → some true incumbents counted as newcomers; registration D2 treats as **bias towards zero** | k100 incumbency 18% (2020) → 0.5% (2021) → 18% (2022) → 33% (2026) | E | RES Constructed variables |
| Second gap | earlier work sitting in held-out split invisible in discovery histories (also bias to zero) | — | E | PRE D2; RES Limitations |
| R2 variant | drops only 2021–22; H2b +3.72 [+2.61, +4.83], H2c −1.74 [−2.53, −0.95] (n 37,312) — same results; does not remove 2023–26 undercount | — | E | FR2 `id_consistent_years`; RES Limitations |
| ICLR-only | experience at other venues not captured; a senior person from another field counts as newcomer | — | — | RES Limitations; QA §1 |
| Discovery vs held-out measure | discovery H2b/H2c used discovery-only histories (incumbency 26.5%); held-out uses pooled histories (held-out incumbency 30.9%); under pooled histories 1,515 discovery papers would switch newcomer → incumbent; pooled discovery incumbency 30.0% (+3.5 pp) | — | E | RES Design → Features (D14); Pooled re-run caveats |
| Newcomer share | RQ2 population | **72.9%** newcomer (incumbent 27.0%) | E | RES RQ2 base rates; FR2 `regressor_mean` 0.7295 |
| Newcomer share held-out | H2b′/H2c′ sample | 68.3% | E | RES Held-out → H2b′ and H2c′ |
| Other variables | `maturity` = log(1 + papers in topic before t) (mean 4.8 ≈ 120 prior papers in RQ3); `fm_adoption` = share of topic's t−1 papers FM (mean prior adoption 29%); `hot` = prior growth (share t−1 / share t−2, +0.5) in top 20% that year (20 topics/yr; 33 in 2019, 19 in 2022) | — | E | PRE Variables; RES RQ3 model; PRE post-run record (audit C); RES Constructed variables |
| Probable earlier versions (R1/S4) | 170 flagged (167 at centred SPECTER2 cosine ≥ τ = 0.90; 3 identical titles); τ calibrated by blind judges (yes-rates 10/48/90/100% across four bins) | — | E | RES Constructed variables |
| Buzzword measure | failed blind validation: flagged uses peripheral 42% (95% CI 33–52%) vs 15% for matched non-flagged; gate needed ≥50% → H2d/H3c dropped before any estimate | — | C (dropped) | RES Constructed variables; RES Summary |

## 3. Descriptive trends and hindsight / topic-map results (outcome-free)

### 3a. Field-level shares (LAB, all 43,480 discovery papers; outcome-free)

| Claim | 2017 | 2026 | Tier | Source |
|---|---|---|---|---|
| Share building on an FM | 0.3% | 54.4% (→ "54%") | E | LAB **[derived]** by year; slides.tex lines 61–62; paper draft line 28 |
| Share proposing a new architecture (`primary_type == model`) | 24.5% (→ "24%") | 7.5% (→ "8%") | E | LAB **[derived]**; slides.tex; `make_figures.py fm_trend` |
| Share with branded "NAME: subtitle" title | 9% | 41% | E (from earlier title analysis; not re-verified here) | `presentation/slides.tex` line 63; QA Numbers |
| Method share (primary class) | 76.8% | 73.4% | E | LAB **[derived]** |
| Measurement share (dataset/benchmark + evaluation) | 2.6% | 11.1% | E | LAB **[derived]** |
| FM share by year | 0.3, 0.0, 0.5, 3.3, 4.2, 5.4, 10.6, 26.7, 42.3, 54.4% (2017→2026) | | E | LAB **[derived]** |
| New-architecture share by year | 24.5, 16.8, 15.0, 13.7, 10.6, 11.3, 9.9, 9.2, 8.5, 7.5% | | E | LAB **[derived]** |
| Overall class mix | method 75.1%, empirical 6.9%, theory 6.9%, dataset/benchmark 5.2%, other 3.5%, evaluation 2.4% | | E | LAB **[derived]** |

### 3b. Hindsight check (k = 100 maps differing only in fitting years)

| Map | Topics defined from | ARI with published | Emerging topics (share of 2024–26 papers in them) | Declining topics | Fit 2017 vs 2026 | Source |
|---|---|---|---|---|---|---|
| pooled (published) | all papers | 1 | **29** (40.9%) | 13 | 0.62 vs 0.65 | TOP Hindsight table; HC |
| seed refit | all papers | 0.69 | 28 (41%) | 15 | 0.62 vs 0.65 | TOP; HC |
| balanced | all years, equal weight | 0.48 | 16 (42.2%) | 26 | 0.69 vs 0.61 | TOP; HC |
| early | 2017–2020 only (no hindsight) | 0.34 | **8** (22.3%) | 17 | 0.69 vs 0.53 | TOP; HC |
| middle-era | middle-era papers (exact years not stated in HC) | 0.40 | 10 (20.9%) | 17 | 0.63 vs 0.58 | HC (not in TOP table) |
| late | 2024–2026 only (full hindsight) | 0.55 | 28 (31%) | 6 | 0.56 vs 0.66 | TOP; HC |

- Emerging rule: 2024–26 share ≥ 3× 2017–20 share; declining ≤ 1/3×. Source: HC `ratio_rule`.
- **Claim (headline, Tier E): hindsight-fitted topic maps manufacture waves — 8 emerging topics on the 2017–20 map vs
  29 on the all-years map; the published map's emerging count (29) equals the late-only map's (28), and it shows half
  as many declining topics as a year-balanced map (13 vs 26).** Source: TOP "Hindsight check"; QA Numbers; slides.tex.
- Emergence "bracketed, not pinned down": share of 2024–26 papers in emerging topics 22% (no hindsight) to 41%
  (pooled). Source: TOP Hindsight check.
- Diversity (effective topics / k by year) peaks in each map's own fitting years. Pooled: 0.443 (2017) → 0.91 (2025),
  0.84 (2026). Early: 0.738 (2017), peak 0.908 (2020), 0.681 (2026). Late: 0.448 (2017) → 0.937 (2025). Balanced:
  peak 0.867 (2021). Source: HC `effective_topics_over_k_by_year`. TOP: "The pooled map's 'diversity rises to 2025' is
  therefore not a finding."
- Consequence registered: time-trend results must hold under the balanced map and the early map on 2021–2026; this
  check was seen before registration and is "the reason for the mandatory hindsight variants". Source: TOP; PRE
  "What had been seen before registration".

### 3c. Lifecycle flip (same papers, same model, different map; RQ1 H1a/H1b)

| Hypothesis (prediction) | All-years k100 (main) | Year-balanced | Early map, all papers | Early map, 2021–26 papers (prospective) | Source |
|---|---|---|---|---|---|
| H1a method ~ maturity (−), pp per log unit | −0.14 [−1.78, +1.49], p 0.86 | −0.08 [−1.98, +1.83] | −2.30 [−4.47, −0.13], p 0.041 | **−3.48 [−6.21, −0.76], p 0.014** (n 39,008) | RQ1C; CIs **[derived]** ±1.96 SE |
| H1b measurement ~ maturity (+) | +0.50 [−0.76, +1.75], p 0.44 | +0.66 [−1.13, +2.45] | +2.16 [+0.35, +3.98], p 0.021 | **+3.96 [+1.35, +6.57], p 0.0037** | RQ1C; **[derived]** CIs |
| H1c empirical ~ maturity (+) | −0.31 [−1.29, +0.67] | −0.75 | −1.06 (wrong sign) | −1.03 [−2.51, +0.46] (wrong sign) | RQ1C |

- **Claim (Tier E/exploratory): whether topics "age" from new methods towards benchmarks depends on the map — the
  all-years map says no, the 2017–20 map says yes.** Early-map rows are counted robustness variants of registered
  H1a/H1b, but reading them as a lifecycle is exploratory and unadjusted ("method −3.5 pp, measurement +4.0 pp per log
  unit (exploratory, unadjusted)"). Only H1a/H1b are named (H1c has the wrong sign there; audit C2). Source: RES RQ1
  "Maturity (H1a–c)"; PRE post-run record (audit C2); slides.tex "Consequence"; script.md slide 8.
- QA framing: "We don't claim either. By our pre-registered rule it is 'not supported', because the main map shows
  nothing. The lesson is that the answer depends on the map." (QA §2)

### 3d. Forecastability of topic growth (PH5 forecast; post hoc, outcome-free, declared 2026-10-17)

| Metric (B4, out-of-time, test origins 2021–24, 2-year growth) | k100 (hindsight) map | Early (2017–20) map | Source |
|---|---|---|---|
| R² of **size** predictor | **0.281** [0.217, 0.335] | **−0.033** [−0.082, −0.002] | FC `headline.b4` |
| Spearman, size | 0.595 [0.51, 0.672] | −0.043 [−0.151, 0.063] | FC |
| Precision@top quintile, size | 0.563 | 0.25 | FC |
| Spearman, momentum | 0.377 | 0.198 [0.103, 0.278] | FC |
| Precision@top quintile, momentum | 0.42 | 0.395 (30/76; chance 20%) | FC; SL finding 4 |
| R², momentum | 0.056 | 0.032 | FC |
| Topic-years | 446 | 522 | FC `sizes.b4_topic_years` |
| P(top-fifth growth) by size tercile small/mid/large (in-sample) | 40 / 21 / 2% | 22 / 20 / 20% | SL finding 4; `b4_conditional.csv` |
| Without LLM/VLM areas, R² size | 0.30 | −0.09 | SL finding 4 |

- **Claim (Tier E): small size "predicts" 2-year topic growth out of time only on the hindsight map (R² 0.28 vs
  −0.03).** Caveats: early map cannot represent topics born after 2020; maps differ in fitting corpus and eligibility
  timing, so the gap "cannot be attributed to hindsight alone"; no paired test. Real forecasting is weak: momentum
  precision only 16/56 (29%) for origins 2021–23. Interval method in FC not inspected here (report as stored). Source:
  SL finding 4; QA Numbers.

## 4. Protocol, decision rule and calibration facts

| Item | Fact | Source |
|---|---|---|
| Registration | 2026-10-13, by commit; before any full-corpus label existed (only 2,300 validation papers had labels; no RQ analysis on them) | PRE header; RES Protocol |
| Disclosure | earlier exploratory work on keyword popularity vs acceptance and title style vs acceptance in the same corpus came before registration and is disclosed | PRE "What had been seen"; QA §3 |
| Decision rule ("supported") | predicted sign; Holm-adjusted p < 0.05 within family; ≥75% of counted variants with predicted sign; both hindsight variants (year-balanced map; early map on 2021–26) with predicted sign | RES Protocol; PRE "Decision rule" |
| Other verdicts | "significant in the opposite direction" (Holm p < 0.05, wrong sign); "equivalent to null" (90% CI inside SESOI); "inconclusive"; *fragile* if a supplementary variant is significant against prediction | RES Protocol |
| Holm families (discovery) | {H1a–e}, {H2a–c}, {H3a–b}, two-sided α 0.05 | PRE Decision rule; D10 |
| SESOIs | H2a ±2 pp; H2b ±2; H2c ±1; H3a/H3b ±1 pp per log unit | PRE D12 |
| Counted variants | RQ2: k75, k150, balanced, early, early_prospective, stable_papers, coherent_topics, certain_labels, without 2026, R2 (10); RQ1 the 9 without R2; RQ3 the 9 + logit + R1 (11) | PRE D9; QA §3 |
| Models | LPMs; topic and year FE (topic × year cells for H2b/H2c); SE clustered by k100 topic (100 clusters) | RES RQ1–RQ3 headers |
| Outcome blindness | only `outcomes.py` reads outcome/review columns (lint-enforced); real mode refuses unless caller is `run_frozen.py`, FREEZE.json hashes match (68 files), clean tree, no debugger | RES Protocol |
| Single run | `run_frozen.py` attempt 1, 19:03:11–19:03:29 UTC (18 s), commit e08ece3; outputs committed unchanged (604f41c) before interpretation | PRE post-run record; RES Protocol |
| Reviews | 9 adversarial review rounds (A, B, B2–B8); two blinding incidents disclosed (E7 seen by a reviewer; analyst once read value sets of outcome columns) | RES Protocol → Reviews |
| Dry-runs | two runs × 12,400 simulated jobs | RES Protocol; PRE dry-run v2/v3 |
| **Size failure (the "12.6%")** | under the RQ2 null whose structure follows the early map (cuts across k100 topics), the main test rejected **12.6% (H2b) / 10.0% (H2c)** at nominal 5% (all other sizes 3.8–7.2%) | PRE dry-run v2 results; RES Protocol → Remedy; QA §3 |
| Remedy | wild cluster restricted bootstrap (Rademacher by k100 topic, null imposed, 9,999 draws) — did **not** fix it: 12.4% / 9.6%; reported, not hidden | PRE dry-run v3; RES Remedy |
| S11 two-way clustering | size 4.4–7.6% in every null; 7.6%/7.0% in the cross-map null | PRE dry-run v3 |
| Family-wise error under cross-map null | some RQ2 hypothesis supported 6.4% (2.0% under k100 null); some directional claim 11.2% (4.6%); per-hypothesis false support ≤3.2% | PRE dry-run v3; RES RQ2 "How much to trust" |
| Stress factors | t inflation 1.3078 (H2b), 1.2198 (H2c) — single-scenario bracket, not a correction | PRE dry-run v3 |
| Discovery MDE80 (frozen) | H2a 3.6 pp; H2b 1.7; H2c 1.1; H3a 4.1 pp per log unit (2.8 low-variance); H3b 2.4 (2.1) | PRE dry-run v3 |
| H3a power | 54% detection at 3 × SESOI (high variance), 88% low | PRE; RES RQ3 |
| Held-out families | {H1d}, {H2b′, H2c′}, {H3a}, {H4-FL}, PH5 primary {E1, P1b}; six PH5 secondary each one-sided 0.05 unadjusted | RES Design; PRE 2026-10-18 §C–D |
| Held-out one-sided rule | p1 = p/2 if predicted sign else 1 − p/2 (p = two-sided p of discovery method); exception premia b (intersection-union) | RES Design |
| Held-out freeze/run | `FREEZE_CONFIRMATION.json`; `run_confirmation.py` once, attempt 1, 2026-10-18 16:39–16:42 UTC | RES Held-out replication |
| Held-out MDE80 (registered) | H1d 12.0 pp; H2b′ 2.8; H2c′ 2.4; H3a 4.8 per log unit; H4-FL 14.5; PH5 E1 4.9; P1b 5.4 | RES "MDE80 and reading rules"; PRE §C |
| Held-out simulated null sizes | one-sided: H1d 4.5%, H2b′ 2.0%, H2c′ 2.5%, H3a 5.0%, H4-FL 4.0% | PRE 2026-10-18 §C |
| Frozen topic maps for held-out | nine alternative maps' exact KMeans centres re-derived; all 9 gates reproduce discovery labels exactly; held-out topic distribution differs from discovery by no more than sampling noise; stable share 0.792 both splits | RES Design → Topic maps |
| Keyword map for held-out | lookup learned on discovery only: 45,778 forms (5,738 non-identity); recall/precision 98.6%/99.96% (759 vocab), 99.0%/99.98% (68 PH4 kw), 97.2%/100% ('federated learning') | RES Design → Keyword map |

## 5. RQ1 (registered; discovery 2018–2026, n 43,096; H1d/H1e n 42,990; 100 topics)

| ID | One-line claim | Discovery estimate [95% CI], units | Holm p | Variants same sign | Held-out | Tier | Source |
|---|---|---|---|---|---|---|---|
| H1a | Method share does not detectably move with topic maturity | −0.14 pp per log unit [−1.78, +1.49] | 1.0 | 78% (7/9) | not tested | C (not supported) | RES Summary; RQ1J |
| H1b | Measurement share does not detectably rise with maturity | +0.50 [−0.76, +1.75] | 1.0 | 89% | not tested | C | RES Summary; RQ1J |
| H1c | Empirical share does not rise with maturity | −0.31 [−1.29, +0.67] | 1.0 | 0%; hindsight fails | not tested | C | RES Summary; RQ1J |
| **H1d** | **Where more of a topic's previous-year papers built on FMs, fewer of its papers propose new architectures** | **−7.98 pp for 0 → 100% prior FM share [−12.14, −3.82]**; p 0.00029 | **0.0014** | 100% (9/9); variants −6.3 to −14.2 | **−11.0 [−18.1, −3.9], n 10,978; one-sided p 0.0013 (Holm 0.0013), two-sided 0.0027; 9/9 variants (−5.4 to −15.2), hindsight passes; MDE80 12.0 (underpowered at discovery size)** | **A** | RES Summary, RQ1, Held-out table; RQ1J; CONF |
| H1e | No shift towards empirical/evaluation with FM adoption | −0.63 [−3.64, +2.38] | 1.0 | 44% | not tested | C | RES Summary; RQ1J |

- H1d base: new-architecture (`model`) outcome mean 9.24% (RQ1C `outcome_mean`; RES "against a mean of 9.2%").
  Mean prior FM adoption 29% (PRE post-run record, audit C). Reading: "topics at 50 percent adoption have about a
  third fewer new-architecture papers than topics at 10 percent" (script.md slide 10; QA Numbers) — **[derived]**
  0.4 × 8.0 = 3.2 pp on a ≈9% base.
- H1d held-out weakest variant: prospective early map −5.4 pp, two-sided p 0.24 (one-sided 0.12). Source: RES
  Held-out → H1d.
- H1d pooled (exploratory): −8.9 [−13.1, −4.7], Holm 3 × 10⁻⁴. Source: RES Pooled table.
- Equivalence reading for H1a–c ("intervals exclude effects larger than about 1–2 pp per log unit") is **post hoc**.
  Source: RES RQ1.
- Caveats (QA §4): year FE remove field-wide trends; reverse causality possible (lagged adoption helps timing only);
  "adapter on an LLM" is labelled method, not new architecture.
- Pooled RQ1 rows (exploratory): H1a −0.59, H1b +0.81, H1c −0.24, H1e −0.6; all not supported. RES Pooled table.

## 6. RQ2 (registered; discovery 2019–2026; models LPM, SE by k100 topic)

Population: papers with ≥1 author ID, 2019–2026: **42,325** (42,315 after dropping singleton topic-year cells for
H2b/H2c; 776 cells). Base rates: incumbent 27.0%, hot 26.1%, method 75.0%, measurement 7.7%, newcomer 72.9%.
Source: RES Data, RQ2; FR2.

| ID | One-line claim | Discovery estimate [95% CI] | p / Holm | Variants | Held-out (registered) | Tier | Source |
|---|---|---|---|---|---|---|---|
| H2a | No reliable difference in incumbent share between hot and other topics | −0.73 pp [−2.68, +1.22]; 90% CI [−2.37, +0.90] | p 0.46; Holm 0.46 | 8/10 predicted sign; hindsight fails (balanced +1.05); k150 +0.37; early −1.62 (p 0.03), early-prospective −1.55 (p 0.045) | not registered; reported row −2.55 [−5.59, +0.49], p 0.099 | C (inconclusive; TOST p 0.10; MDE80 3.6) | RES H2a; FR2; RES Unregistered rows |
| **H2b → H2b′** | **Newcomer papers are *more* often method papers (registered herding prediction was the opposite)** | **+3.71 pp [+2.61, +4.80]**, t = 6.7, on 75% base | bootstrap p < 1/9,999; Holm < 0.001; CR1 p 1.1 × 10⁻⁹ | all 10 positive, +2.16 to +3.87, all p < 0.05; hindsight variants +3.10 (balanced) / +2.16 (early 2021–26) | **H2b′: +3.60 [+1.48, +5.71], n 10,718; one-sided p 0.0007, Holm 0.0010; two-sided 0.0014; 10/10, hindsight passes, S11 agrees; MDE80 2.8** | **A** (reversed prediction) | RES H2b/H2c; FR2; RES Held-out table; CONF |
| **H2c → H2c′** | **Newcomer papers are *less* often dataset/benchmark/evaluation papers** | **−1.70 pp [−2.46, −0.93]**, t = −4.4, on 7.7% base (≈ a fifth fewer) | bootstrap p < 1/9,999; Holm < 0.001; CR1 p 2.7 × 10⁻⁵ | all 10 negative, −1.81 to −0.86; hindsight −1.41 / −0.86 | **H2c′: −2.10 [−3.35, −0.85], n 10,718; one-sided p 0.0005, Holm 0.0010; two-sided 0.0010; 10/10, S11 agrees; MDE80 2.4 (underpowered at discovery size → direction only)** | **A** (reversed prediction) | same |

Robustness and qualifiers for H2b/H2c (all from RES "H2b and H2c" and FR2):
- S11 two-way: +3.71 (Holm p 4 × 10⁻⁸) / −1.70 (2 × 10⁻⁴). Stress sensitivity Holm p 4 × 10⁻⁶ / 1 × 10⁻³.
- S1 log team size: H2b +3.92 [+2.69, +5.16] unchanged; **H2c shrinks to −0.54 [−1.11, +0.04], p 0.07** — "much of the
  measurement gap is accounted for by team size"; read as partly small all-new teams vs larger mixed teams.
- S5 fine topics +3.57 / −1.62; S3 two-year window (2023–26) +3.20 / −1.77; S4 excluding own earlier versions
  +3.77 / −1.69; S8 misclassification correction +4.09 / −1.84 (can only enlarge; assumes non-differential error).
- By era (E4, exploratory): H2b +5.5 (2019–20, p 0.009), +3.4 (2021–23, p 0.008), +3.6 (2024–26); H2c −0.5 (n.s.),
  −0.5 (n.s.), **−2.0 (2024–26, p < 0.001)** — H2c concentrated in 2024–26.
- Newcomer × hot (E5): −0.4 / −0.6 pp, both n.s. (no detectable difference in hot topics).
- Held-out S1: H2c′ shrinks to −0.98 (two-sided p 0.10); H2b′ stays +3.64. Held-out base rates: method 75.0%,
  measurement 7.9%, newcomer 68.3%. Held-out stress Holm p1 0.0075 both. Not fragile.
- Pooled: H2b +3.46 [+2.38, +4.54]; H2c −1.65 [−2.36, −0.94] (exploratory).
- Trust caveat: p-values approximate under cross-k100 structure (simulated size 10–12%); t = 6.7 and −4.4 are large
  relative to the 1.31/1.22 inflation.
- QA framing (§4): "consistent with outsider innovation, not with herding"; "'New method' is a contribution *type*,
  not a measure of quality or novelty."

## 7. RQ3 (registered; acceptance; discovery 2018–2026)

Population: ordinary submissions with final accept/reject, **32,190 papers, 40.1% accepted**; filter leaves out 9,986
withdrawn submissions. Maturity mean 4.8 (≈120 prior papers); one log unit ≈ 2.7× as many prior papers. Model: LPM,
topic + year FE, class dummies (ref. method), FM dummy, SE by topic. Source: RES RQ3; FR3.

| ID | One-line claim | Discovery [95% CI] | p / Holm | Variants | Held-out | Tier | Source |
|---|---|---|---|---|---|---|---|
| H3a | Crowding (topic maturity) and acceptance: inconclusive, underpowered | −1.68 pp per log unit [−3.68, +0.32] | p 0.099; Holm 0.20 | all 11 counted negative (linear −2.53 to −1.31; logit AME −1.64); hindsight negative | **−1.51 [−5.20, +2.19], n 8,185; one-sided p 0.21; two-sided 0.42; 9/11 variants; hindsight fails; MDE80 4.8 → uninformative; TOST p 0.61; acceptance 39.4%** | C | RES H3a; FR3; RES Held-out table; CONF |
| H3b | Whether method papers fare worse in mature topics cannot be told | −0.36 [−1.51, +0.79]; 90% CI [−1.33, +0.60] | p 0.53; Holm 0.53 | 10/11 negative (early +0.13) | not registered; row +1.34 [−1.26, +3.93], p 0.31 | C (TOST p 0.14; MDE80 2.4) | RES H3b; FR3; RES Unregistered rows |

H3a details: supplementary S1 −2.04 (p 0.04); S5 −2.42 (p 0.005); S9 withdrawals-after-review as rejections −2.12
(p 0.02; +9,631 papers); S10 newcomer control −2.99 (p 0.003); S11 −1.68 (p 0.07) — unadjusted, outside the verdict,
"neither of these is confirmatory evidence". By era (E4): −0.3, −6.5, −2.9 (all n.s.). Pre-declared reading: "uninformative
about effects below about 4 pp per log unit. It is not evidence of no effect." Pooled −1.72 [−3.44, −0.01], p 0.049,
Holm 0.098, still inconclusive; pooled H3b −0.03 labelled "equivalent to null" (descriptive). Held-out S9 −1.97
(two-sided p 0.19). QA safe line: "All we can say is that there is no detectable *premium*." Source: RES H3a; Pooled;
QA §4.

E9 (equivalence, exploratory): none equivalent — TOST p H2a 0.10, H3a 0.75, H3b 0.14. Every 90% CI reaches beyond the
SESOI. Source: RES Exploratory table; RES Summary.

## 8. Planned exploratory analyses E1–E10 (discovery; labelled, unadjusted p) — Tier D

| ID | One-line claim | Estimate [95% CI] | p | N | Pooled (expl.) | Source |
|---|---|---|---|---|---|---|
| E1 | FM papers accepted more often, within topic × year, class controls | +4.62 pp [+2.79, +6.44]; +4.06 without class controls | 2.2 × 10⁻⁶ | 32,159 | +5.61 [+3.93, +7.29] | RES Exploratory; FRX; RES Pooled |
| E2 | Newcomer papers accepted less often, within topic × year, class + FM controls — "largest association in the study" | **−10.2 pp [−11.8, −8.7]**; −10.5 [−12.0, −8.9] in ID-consistent years | 3.9 × 10⁻²³ | 31,534 (27,490) | −10.2 [−11.6, −8.9] | RES; FRX |
| E3 | Withdrawal after review rises with maturity; before review does not | +1.62 pp per log unit [+0.42, +2.81]; before review −0.07 (n.s.) | 0.009 | 42,214 | — | RES; FRX |
| E4 | H2b, H2c, H3a, H3b by era | see §6, §7 | | 3,314 / 8,875 / 30,126 (RQ2 eras) | — | RES; FRX |
| E5 | Newcomer × hot (method, measurement, acceptance) | −0.4, −0.6, +0.2 pp | all n.s. | 42,315 / 31,534 | — | RES; FRX |
| E6 | Dose-response plots after removing FE (H1d, H2a, H3a) | Figure F4 | — | — | — | RES |
| E7 | Buzzword decomposition | reported, **not interpreted** (failed measure; seen early by a reviewer) | — | — | — | RES |
| E8 | New-architecture papers accepted relatively more often where prior FM adoption is high ("against the tide"; scarcity hypothesis, not a test) | +8.3 pp for 0 → 100% FM [+1.3, +15.4] | 0.02 | 32,101 | +9.4 [+2.3, +16.4], p 0.010 | RES; FRX |
| E9 | Equivalence tests | none equivalent (see §7) | — | — | — | RES |
| E10 | Acceptance by class vs method, within topic × year | theory +8.9 [+6.5, +11.3]; dataset/benchmark +3.9 [+1.1, +6.7]; empirical −2.7 [−5.2, −0.3]; evaluation −1.9 (n.s.); other −8.0 | theory 6 × 10⁻¹¹ | 32,159 | — | RES; FRX |

E2 caveat: "Experience, team size, reviewer familiarity and resubmission are all candidate explanations; this analysis
cannot separate them." (RES). Within the same authors the gap is ≈ −3 pp (PH3; see §10). E8 was not among the
registered held-out tests, stays exploratory (QA §4 "Against the tide").

## 9. Held-out replication: every registered test (2026-10-18) — one table

Held-out n: H1d 10,978; RQ2 10,718; acceptance tests 8,185 (2018–26 decided). Discovery estimates two-sided.
Source: RES "Results for every registered test"; CONF.

| Test (family) | Prediction | Discovery (95% CI) | Held-out [95% CI]; N | One-sided p (Holm) | Two-sided p | Verdict | MDE80 | Tier |
|---|---|---|---|---|---|---|---|---|
| H1d (RQ1) | − | −8.0 (−12.1, −3.8); Holm 0.001 | −11.0 [−18.1, −3.9]; 10,978 | 0.0013 (0.0013) | 0.0027 | supported; 9/9; hindsight passes | 12.0 | A |
| H2b′ (RQ2) | + | +3.71 (+2.61, +4.80) | +3.60 [+1.48, +5.71]; 10,718 | 0.0007 (0.0010) | 0.0014 | supported; 10/10; S11 agrees | 2.8 | A |
| H2c′ (RQ2) | − | −1.70 (−2.46, −0.93) | −2.10 [−3.35, −0.85]; 10,718 | 0.0005 (0.0010) | 0.0010 | supported; 10/10; S11 agrees | 2.4 | A |
| H3a (RQ3) | − | −1.68 (−3.68, +0.32); Holm 0.20 | −1.51 [−5.20, +2.19]; 8,185 | 0.21 (0.21) | 0.42 | inconclusive; uninformative | 4.8 | C |
| H4-FL level | − | −11.3 (−17.9, −4.8); p 0.005, q 0.19 | −4.9 [−15.4, +5.7]; 134 FL papers, 6 years ≥10 | 0.14 (0.14) | 0.29 | not supported; uninformative (MDE80 > discovery gap) | 14.5 | C (discovery gap: D) |
| H4-FL trend (sec.) | − | −3.0 (−6.4, +0.5); p 0.08 | +3.2 [−3.3, +9.6] pp/yr | 0.88 | 0.24 | not supported (opposite sign) | not computed | C |
| PH5 E1 (primary) | − far jump | −5.44 (−7.10, −3.78); Holm 1.3 × 10⁻⁸ | −6.09 [−9.32, −2.86]; 5,344 | 0.0025 (0.0050) | 0.0050 | supported | 4.9 | B |
| PH5 P1b (primary) | − least-novel fifth | −3.27 (−4.93, −1.60); Holm 0.0014 | −0.13 [−3.50, +3.25]; 8,010 | 0.47 (0.47) | 0.94 | not supported; uninformative (power 0.47) | 5.4 | C (discovery: D) |
| PH5 E4 (sec.) | + within-author per +0.1 cos | +0.55 (+0.21, +0.90); Holm 0.006 | +1.06 [+0.23, +1.89]; 4,311 | 0.006 | 0.012 | supported | — | B |
| PH5 P7 (sec.) | + within-author novelty | +0.39 (+0.09, +0.69); Holm 0.105 | +0.34 [−0.47, +1.16]; 4,810 | 0.22 | 0.43 | not supported | derived ≈1.0–1.1 | C |
| Teams H1 (sec.) | + one topic insider vs none | +3.42 (+1.18, +5.66); Holm 0.019 | +3.88 [+0.28, +7.47]; 6,243 | 0.017 | 0.035 | supported | derived ≈4.5 | B |
| Kwtiming A1 (sec.) | + Emerging − Mainstream keywords | +2.67 (+0.76, +4.58); Holm 0.020 | +3.25 [−0.18, +6.69]; 5,741 | 0.031; null-frame 0.020 | 0.063 | supported (weak; 95% CI includes 0) | derived ≈4.3 | B (weak) |
| Premia b (sec.) | 0 < b < 1 | 0.38 (0.18, 0.58) | 0.60 [0.32, 0.88]; 75 units | 0.003 (IUT) | — (b=0: 6.5 × 10⁻⁵) | supported | — | B |
| Premia EB D0 (sec.) | > 0 | none (new test) | 1.71 [0.42, 3.01] × 10⁻³ | 0.005 | 0.010 | supported | — | B (no discovery counterpart) |
| PH6 waves D (declared 2026-10-28) | < 0 | −5.7 (−8.5, −2.9) (not a test) | −5.2 [−11.1, +0.7]; 17 waves | 0.043 | — | supported, only just; below MDE80 | 7.4 | B (weak) |

Underpowered-at-discovery-effect supported tests (direction, not size): H1d (12.0 vs −8.0), H2c′ (2.4 vs −1.70), teams
H1 (≈4.5 vs +3.42), A1 (≈4.3 vs +2.67). Source: RES Interpretation; Limitations.

Unregistered held-out rows (two-sided, not interpreted; RES "Not registered"): H2a −2.55 (p 0.099); H3b +1.34 (0.31);
FL recent level −3.6; FL adjusted −3.4; E2 near +2.34 (0.17); E3 −3.09; P1a +2.54; P2 twin +3.69 [+0.90, +6.48]
(p 0.010); P3 +4.84; P4 +1.47; P5 −9.75 (0.030); P6 +10.74 (0.030); teams H2 +4.47; premia b k100 0.51; keywords 0.16
[−0.34, 0.66]; areas 0.71; premia D descriptive 0.37 × 10⁻³.

## 10. Post hoc analyses (PH1–PH6) — summary for orientation (Tier D unless stated)

All declared in PRE before they were run; associations within topic and year.

| ID | Claim | Key numbers | Tier | Source |
|---|---|---|---|---|
| PH1 | Among newcomer papers, theory, large teams and FM go with higher acceptance; newcomer gap present in every subgroup | population 31,549 decided 2019–26; 22,603 newcomer papers accepted 37.2% vs incumbent 47.3%; theory +10.2 [+7.2, +13.2]; FM +4.1 [+2.0, +6.2]; team 1–2 −8.5, 7+ +11.1 vs 3–4; newcomers in mature topics −2.8 pp/log unit (Holm 0.02); gap −5.1 (theory) to −14.6 (dataset/benchmark); negative in all 20 areas (−3.8 to −20.8), none survives Holm | D | RES PH1 |
| PH2 | Steep team-size gradient in acceptance | 1–2 authors 28.7%, 3–4 37.6%, 5–6 41.6%, 7+ 49.0%; +8.8 pp per doubling [+8.0, +9.7] (+7.8 with newcomer control); positive in every area; benchmark 21% (1–2) vs 52% (7+) | D | RES PH2 |
| PH3 | Most of the newcomer gap is about who writes the papers | 160,222 paper-author rows; 15,579 authors with both types; newcomer paper −5.4 → −3.1 [−4.5, −1.6] with author FE; author new to topic −1.4 [−2.7, −0.0]; −10.2 → ≈ −6.7 with team size + experience → ≈ −3 within authors | D | RES PH3 |
| PH4 | No area survives multiple testing; areas differ descriptively by about ±10 pp; FL low under both definitions | 68 keywords, 100 topics; FL keyword 475 papers −11.3 [−17.9, −4.8] (p 0.005, q 0.19); FL topic m029 485 papers −13.5 [−21.1, −5.9] (q 0.17); FL share peaked 3.2% (2023) → 1.1% (2026); FL authors with earlier acceptance 4% (2021) → ≈60%; adjusted level −10.5 | D (held-out not confirmed → C) | RES PH4 |
| PH5 | Own-record far jump; field novelty; teams; keyword timing; premia; forecast | see §9; discovery far-jump n 20,430 (2023–26, ≥1 experienced author); adjusted acceptance by closeness fifth 39.7/41.8/44.4/47.2/46.9%; −5.0 with newcomer control; cleantext checks hold | B/C/D per §9 | SL finding 1; QA Numbers; RES Held-out |
| PH6 | A keyword's acceptance gap falls after its share peaks | 17 waves; held-out D −5.2 [−11.1, +0.7], one-sided p 0.043, MDE80 7.4; without six viewed-first keywords −1.7 (p 0.33); without FL −6.2 (p 0.033); discovery −5.7 (not a test); FL itself +3.5 after vs before held-out (discovery −5.9); gap highest well before the peak (+9 to +30 pp 2–5 years before, few papers), ≈0 at peak, −2 to −5 pp 3–5 years after | B (weak) | RES PH6; PRE 2026-10-28 |

## 11. Base rates and sample sizes per analysis (quick reference)

| Quantity | Value | Source |
|---|---|---|
| Discovery papers (topics) | 43,480 | RES Data |
| RQ1 sample | 43,096 (2018–26); H1d/H1e 42,990; early-prospective 39,008 | RQ1C |
| RQ2 sample | 42,325 (H2a); 42,315 (H2b/H2c); 776 topic-year cells | FR2 |
| RQ3 sample | 32,190; acceptance 40.1% | RES RQ3; FR3 |
| E1/E10 sample | 32,159 | FRX |
| E2 / PH1 sample | 31,534 (E2 model) / 31,549 (PH1 population) | FRX; RES PH1 |
| Withdrawn left out of RQ3 | 9,986 | RES Limitations; PRE pre-run log |
| Method base | 75.0% (RQ2); 75.1% all papers; 75.0% held-out | RES RQ2; LAB **[derived]**; RES held-out |
| Measurement base | 7.7% (RQ2); 7.6% RQ1 mean; 7.9% held-out | RES; RQ1C; RES held-out |
| Newcomer share | 72.9% (RQ2); 68.3% held-out | RES; RES held-out |
| Incumbent / hot | 27.0% / 26.1% | RES RQ2 |
| New-architecture base | 9.2% (RQ1 sample) | RQ1C; RES RQ1 |
| Newcomer vs incumbent acceptance (raw) | 37.2% vs 47.3% | RES PH1 |
| Held-out acceptance | 39.4% (H3a sample) | RES Held-out → H3a |
| Pooled | 54,579; ≈80% discovery per sample | RES Pooled |

## 12. Items the paper must NOT claim (from the sources)

- That H1a–c / lifecycles are "found" or "absent": the answer depends on the map (TOP; QA §2).
- That pooled-map diversity rising to 2025, or 28–33% emerging topics, are findings (TOP).
- That P1b (novelty floor) or the FL acceptance gap replicated (RES Interpretation).
- That crowding has "no effect" (H3a uninformative below ≈4–5 pp) (RES; QA).
- Causal or advisory language ("choose", "should") for any acceptance association (RES; SL).
- Effect-size comparisons across modules, or held-out sizes as "larger effects" (RES Interpretation; SL "Do not put").
- That reference labels are human labels (PRE audit C).
- Any held-out result as "independent confirmation" (PRE 2026-10-18 §A).
