# Dossier: post hoc and descriptive findings (authoritative fact sheet)

Built 2026-11-03 from committed, already-published aggregates only. No outcome column, decision column, author name,
author ID or email was read. Paths below are relative to `/home/user/cloud-research/research/fashion/` unless they
start with `/`. "RESULTS L123" means `RESULTS.md` line 123; "SL L19" means `presentation/shortlist.md` line 19.

Units: pp = percentage points of acceptance probability (or of a share, where stated). All estimates are
associations within the stated fixed effects (mostly topic x year), never causal effects of an author's choice.

## 0. Tier key and the quoting rules that apply everywhere

| Tier | Meaning | What the paper may say |
|---|---|---|
| A | registered (pre-registration or held-out registration) and replicated on held-out papers | "replicated"; direction, not size |
| B | post hoc in discovery, then a held-out test registered before the run, supported | "post hoc, supported on held-out papers"; secondary tests are one-sided, unadjusted |
| C | registered test inconclusive or not replicated | "not confirmed" / "uninformative" (if below MDE80) |
| D | discovery-only (post hoc or exploratory; pooled re-run confirms nothing) | "discovery, post hoc, unconfirmed" |
| E | descriptive, outcome-free (no acceptance data) | plain description |
| E* / D* | earlier exploratory title analysis (Notion page, no code). E* = outcome-free share (re-verified here, Sec. 2); D* = acceptance ratio (not re-run) | quote D* only as "earlier exploratory" |

Global caveats (quote once, in Methods/Limitations):
- Held-out = 11,099 released former-holdout papers (8,284 decided; 8,185 in 2018-26). It is a pre-registered
  split-sample replication within the same ICLR years, not a certified independent holdout; splits share
  conference-years, reviewer pools and authors (RESULTS L3-9, L631-641; SL L9-15).
- Held-out text measures use post-decision abstracts with no link-removal (cleantext) check (RESULTS L683-684).
- Supported held-out tests that were underpowered at the discovery effect (H1d, H2c', teams H1, A1) confirm
  direction, not size; held-out estimates larger than discovery's must not be read as larger effects (RESULTS
  L842-848).
- PH5 secondary held-out tests: six, each one-sided at 0.05, unadjusted; "one false positive would not be
  surprising" (RESULTS L21-22, L834-835).
- Pooled re-run (54,579 papers) confirms nothing: ~80% of each pooled sample is discovery papers, and pooling changes
  discovery features (RESULTS L58-62, L898-906).
- Unregistered held-out rows (17 rows, RESULTS L800-821) are two-sided, unadjusted, "reported, not interpreted".

Named quoting rules (must travel with the finding):
- **P2 twins rule.** Do not quote the discovery "concurrent twin shows no detectable gap" reading without the held-out
  and pooled rows: discovery +0.68 pp (CI -0.84, +2.20; Holm 1.0), held-out +3.69 [+0.90, +6.48] (p 0.010,
  unregistered), pooled +1.86 (+0.47, +3.24; p 0.009, Holm 0.063). The held-out estimate "does not fit the no
  detectable gap reading" (RESULTS L877-881, L936; SL L26, L41-43).
- **E2 rule (same logic).** Discovery "staying close shows no detectable gain" (+1.75, Holm 0.148) must come with
  held-out +2.34 [-1.01, +5.70] (p 0.17) and pooled +2.10 (Holm 0.036) (RESULTS L882-883, L934).
- **P1b not replicated.** The field-novelty ("least-novel fifth") tail is discovery-only; held-out -0.13 pp, power
  0.47, below MDE80 5.4 pp, uninformative. Do not present the "two tails" summary or the novelty floor as a finding
  (RESULTS L35-42, L849-865; SL L21).
- **FL not confirmed.** Federated learning's low acceptance is discovery-only; the registered held-out level test is
  not supported and uninformative (MDE80 14.5 pp > discovery gap); the trend has the opposite sign (RESULTS L51-56,
  L866-872; SL L31).
- **A1 CI includes 0.** Held-out kwtiming A1 is "supported" one-sided (p 0.031; null-frame 0.020) but its two-sided
  95% CI is [-0.18, +6.69] (RESULTS L25-26, L741, L840; SL L30).
- **PH6 leans on six inspected keywords.** Without the six keywords viewed before declaration, the held-out estimate
  is -1.7 pp (p 0.33) (RESULTS L983-987).
- **Premia keyword units not persistent.** The registered premia b uses early-map topic units; keyword units give
  held-out b 0.16 [-0.34, 0.66] (unregistered) (RESULTS L819; SL L23).
- **Within-family Holm only.** Shortlist strength labels such as Holm 0.019 (teams H1) or 0.020 (A1) hold within the
  module family only; across modules teams H1 would be ~0.17 (Bonferroni) and A1 ~0.18 (SL L177, L213).
- **Do-not-quote list** (SL L227-239): teams H5 hot-topic reversal; position most-novel-with-twin cell; P6 and advice
  built on it; fmwave spline hump, C1 framing, B1/B2; pivot "sweet spot" (cos 0.535) and hot/not-hot curves;
  premia asymmetry, named low-topic lists, flow slope, surge term; "saturation" readings of raw lift; kwtiming
  off-trend +2.0 pp; E4/P7 as standalone; P7 as Holm-significant; 2019-20 replications; cross-module effect-size
  comparisons; mechanical results (past acceptance predicts acceptance, n_exp gradient, raw twin share without
  per-pair normalisation); uncommitted verifier numbers.

---

## 1. Vivid descriptive facts for the introduction (tier E)

| Fact | Value | Source |
|---|---|---|
| Discovery corpus | 43,480 papers, 2017-2026, usable abstract | RESULTS L116 |
| Submissions per year, analytical corpus | 2017 384; 2018 770; 2019 1,248; 2020 2,070; 2021 2,360; 2022 2,649; 2023 3,872; 2024 5,765; 2025 8,951; 2026 15,411 (sum 43,480) | `output/posthoc/ph5_premia/summary.json`, `free_summary.submissions_by_year` |
| Growth 2017 -> 2026 | x40.1 (15,411 / 384) | derived from the row above |
| Share of corpus from 2024-2026 | 69.3% (30,127 / 43,480); 2026 alone 35.4% | derived from the row above; the "69%" claim is confirmed |
| Same, recomputed from the raw file | rows by year 385; 774; 1,255; 2,071; 2,364; 2,649; 3,872; 5,766; 8,960; 15,420 (43,516 rows; 43,515 with abstract); 2024-26 share 69.3% (30,146 / 43,516) | own count of `/home/user/cloud-research/data/submissions.csv.gz` (year only; script `paper_ws/scripts/title_share.py`). The file holds 43,516 discovery rows; the 36-row gap to 43,480 is the corpus's "usable abstract" filter. Quote the corpus row above in the paper. |
| Held-out papers per year | 105 (2017) rising to 3,942 (2026); 11,099 in all | RESULTS L632-633 |
| Pooled | 54,579 papers | RESULTS L128 |
| FM-building papers as share of submissions | 2019 0.4% (5/1,231); 2020 2.9%; 2021 4.2%; 2022 5.4%; 2023 10.6%; 2024 26.7%; 2025 42.3%; 2026 54.4% (8,376/15,411) | derived by summing bins in `output/posthoc/ph5_fmwave/free_fm_share.csv` (papers with a prior-year adoption value; LLM label on partly camera-ready abstracts) |
| In topics with >= 50% prior FM adoption | FM share 87.8% of 7,516 papers in 2026 | same file, row 2026 >=50% |
| Papers with an independent same-year "twin" (cos >= 0.70) | 19.5% (2019) -> 48.8% (2026) | `output/posthoc/ph5_position/summary.json`, `free_summary.any_twin_by_year` |
| Twins per paper per 1,000 submissions | 0.32 (2019) -> 0.19 (2026), i.e. per-pair rate fell ~40% | derived: `ph5_position/free_twin_share.csv` (all, 2019: 0.4006 twins/paper over 1,248; 2026: 2.9356 over 15,411); SL L129 |
| Keyword shares (pooled corpus) | "large language models" 0.26% (2022) -> 16.7% (2026); "generative adversarial networks" 8.1% (2018) -> 0.09% (2026); "graph neural networks" peak 4.3% (2022) -> 1.8% (2026); "federated learning" 3.2% (2023) -> 1.1%; "vision transformer" 1.4% (2022) -> 0.4% | `output_pooled/posthoc/ph5_waves/wave_table.csv`; RESULTS L968-970 |
| Keywords that rose and fell | 17 of PH4's 68 frequent keywords (peak 2019-2024, at most half the peak before and in 2026) | RESULTS L968-970; `ph5_waves/summary.json` settings.waves |
| Emerging topics, hindsight vs prospective map | 29 (all-years map) vs 8 (2017-20 map) | `/home/user/cloud-research/research/topics/output/hindsight_check.json` (emerging_topics 29; cited in the paper draft L56/L134; registered-dossier item, cross-reference only) |
| Code links in abstracts, 2023-26 | 17.6% of accepted vs 0.5% of rejected (difference 17.2 pp) | SL L72, L223; `ph5_fmwave/summary.json` P0_code_links.difference_2023_2026 = 0.1715 |
| Acceptance base rate | 40.1% of 32,190 decided 2018-26 papers | RESULTS L146, L316 |
| Newcomer paper share | 72.9% (RQ2 population) | RESULTS L250 |

---

## 2. Title style: "NAME: subtitle" (earlier exploratory, Notion page; share re-verified here)

### 2a. Re-verification of the outcome-free share (tier E*)

Script `paper_ws/scripts/title_share.py` (Python venv, `pandas.read_csv(..., keep_default_na=False,
na_values=['\N'])`, columns read: submission_id, year, title, abstract; no outcome column). Results saved in
`paper_ws/title_share.json`. Population: 43,515 rows with a non-empty title (discovery split).

Definitions (prefix = text before the first colon; subtitle must be non-empty):
- **D1 broad:** prefix has 1-3 whitespace tokens.
- **D2 name-like:** D1, every prefix token starts with an uppercase letter or digit, and the first token is not a
  generic lead word (Towards, Beyond, Rethinking, Revisiting, Learning, Understanding, Unveiling, Enhancing, On, How,
  What, Position, ... ; full list in the script).
- **D3 coined single token:** one token with >= 2 capitals, or a digit plus a capital (BERT, LoRA, GraphSAGE,
  Llama-2).
- **D4 one name-like token:** D2 restricted to exactly one token (e.g. "PRISM:", "GenFlow:", "Mixup:").

| Year | n | any colon | D1 broad | D2 name-like | D4 one token | D3 coined |
|---|---|---|---|---|---|---|
| 2017 | 384 | 19.0% | 14.3% | 10.9% | 7.6% | 6.5% |
| 2018 | 774 | 22.4% | 16.8% | 13.8% | 8.8% | 7.9% |
| 2019 | 1,255 | 25.6% | 19.8% | 17.6% | 11.8% | 10.7% |
| 2020 | 2,071 | 26.4% | 21.4% | 18.8% | 14.6% | 13.8% |
| 2021 | 2,364 | 27.8% | 21.1% | 18.7% | 14.1% | 13.2% |
| 2022 | 2,649 | 31.4% | 24.6% | 21.9% | 17.3% | 16.0% |
| 2023 | 3,872 | 32.4% | 25.9% | 23.2% | 19.0% | 17.6% |
| 2024 | 5,766 | 40.8% | 32.9% | 30.2% | 25.3% | 23.9% |
| 2025 | 8,960 | 49.5% | 40.7% | 37.6% | 31.2% | 29.3% |
| 2026 | 15,420 | 59.7% | 48.8% | 44.6% | 38.8% | 37.0% |

Reading:
- The Notion figure (9% -> 41%) lies inside the range spanned by reasonable definitions: 2017 6.5-14.3%, 2026
  37.0-48.8%. The rise is 3.4x (D1) to 5.7x (D3); every definition rises monotonically after 2021.
- Sensitivity: the level depends on the definition by about +-4 pp in 2017 and +-6 pp in 2026; the trend
  (roughly a fourfold rise, steepest 2023 -> 2026) does not. 2017 rests on 384 titles (sampling SE ~1.6 pp at 11%).
- Safe wording: "the share of titles that open with a short coined name and a colon rose roughly fourfold, from
  about one in ten (2017) to about four in ten (2026); 7-14% and 37-49% under alternative definitions".
- Not checked: whether accepted papers' titles were edited after the decision (titles are from the selected official
  metadata, partly camera-ready).

### 2b. Other title findings (earlier exploratory; Notion page only; no code in the repository; NOT re-run)

| Claim (as stated on the Notion findings page) | Tier | Caveat |
|---|---|---|
| Accepted papers carry NAME: titles at the submitted rate: ratio 1.02; OR 1.00 ("branded titles, no premium") | D* | uses acceptance; not re-run; earlier exploratory; also in deck (SL L68 "Branded title: ratio 1.02") |
| Returning authors move into new topics as fast as the field but lag on title style, most among first authors (about 40% lag for first authors in its figure; paper draft table "+3% vs +40%") | E* (outcome-free, not re-verified) | figure-read value; definitions of "lag" not documented in code |
| LLM-favoured title verbs (Enhancing, Unveiling, ...) jump after 2023 (OR 2.2) | E* (not re-verified) | odds ratio from the Notion page only |
| Branding rises with or without LLM fingerprints in the abstract | E* (not re-verified) | fingerprint measure not documented in code |

---

## 3. PH1-PH4 (post hoc, declared before they were run; discovery only)

### PH1. What goes with acceptance for newcomer papers? (tier D)
Source: RESULTS L375-414; `output/posthoc/ph1_summary.json`.
- Population: 31,549 decided 2019-26 papers with an author ID; 22,603 newcomer papers accepted 37.2% vs incumbent
  47.3% (ph1_summary.json).
- Background (planned exploratory E2, RESULTS L357, L366-368): newcomer papers accepted -10.2 pp within topic x year
  (pooled -10.2, CI -11.6, -8.9; RESULTS L923). "The largest association in the study."
- Among newcomer papers (A2, vs newcomer method papers): theory +10.2 pp (CI +7.2, +13.2); FM +4.1 (+2.0, +6.2);
  dataset/benchmark +2.4 n.s.; evaluation -0.5 n.s.; empirical -3.1 n.s.; other -9.1.
- Team size strongest (A1, vs 3-4 authors): 1-2 authors -8.5; 5-6 +3.7; 7+ +11.1 pp.
- Topic choice: newcomer papers in more mature topics -2.8 pp per log unit (Holm 0.02); hot topics +1.2 n.s.
- Newcomer gap present in every subgroup (B): -10.2 overall; smallest theory -5.1 and 7+ teams -6.4; largest
  dataset/benchmark -14.6 and most mature topics -11.6.
- Areas (C): within-topic-year gap negative in all 20 coarse areas (-3.8 to -20.8 pp); no area survives Holm.
- Held-out: none (not registered). Pooled: E2 -10.2 (RESULTS L923).
- Caveats: selection (newcomer theory papers may come from established researchers elsewhere; large teams bring
  seniority); "not recommendations about what a newcomer should do" (RESULTS L410-414). Incumbency is undercounted
  after 2020 (email -> profile ID switch; RESULTS L152-155, L554-560).

### PH2. Team size (tier D)
Source: RESULTS L416-454; `output/posthoc/ph2_summary.json`.
- N 32,190 (RQ3 population). Acceptance by band: 1-2 authors 28.7% (4,176 papers); 3-4 37.6% (12,022); 5-6 41.6%
  (8,843); 7+ 49.0% (7,149).
- Within topic x year: +8.8 pp per doubling of team size (CI +8.0, +9.7); +7.8 with newcomer control. Pooled +8.8
  (+8.0, +9.6) (RESULTS L925).
- By class: dataset/benchmark and evaluation +13.5 pp per doubling each (benchmark 1-2 authors 21% vs 7+ 52%);
  method +9.3; empirical +5.5; theory +3.3 n.s. (theory 1-2 authors 42% vs method 1-2 authors 27%). Equal-slope test
  not rejected (calibrated p 0.13); theory vs benchmark CIs do not overlap.
- By area: differ (calibrated p 0.035). Steepest neuroscience/spiking +14.2, diffusion image/video +12.9 (1-2 authors
  25% vs 7+ 59%), VLM reasoning +12.3, vision-language +11.9, LLMs/NLP +11.2; flattest federated learning/privacy +4.0,
  time series +4.3, optimisation/scientific ML/probabilistic inference +5.2. Slope positive in every area.
- Held-out: none. Caveat: team size stands for compute, data, engineering, seniority; "not advice to add authors".

### PH3. Author fixed effects: is the newcomer gap about who the authors are? (tier D)
Source: RESULTS L456-480; `output/posthoc/ph3_estimates.csv`, `ph3_summary.json`.
- 160,222 paper-author rows, 31,549 papers, 81,013 authors; 15,579 authors with both newcomer and incumbent papers.
- Newcomer paper, all author rows, no author FE (M0, with controls): -6.7 pp (CI -8.3, -5.1).
- Same sample (28,370 papers): no author FE -5.4 (-7.1, -3.7) vs author FE -3.1 (-4.5, -1.6).
- Author new to the topic: -3.1 -> -1.4 (-2.7, -0.0; p 0.049) with author FE.
- First-author FE -2.2 (-4.8, +0.3); last-author FE -2.9 (-4.6, -1.1).
- Reading: most of the -10.2 gap is about who writes newcomer papers; the same person entering a new topic is ~1.4 pp
  less likely accepted. ICLR is double-blind; the residual "need not be reviewer bias" (less topic familiarity can
  make the paper weaker). Pooled -3.1 (-4.5, -1.7) (RESULTS L926). Held-out: none.

### PH4. Areas, incl. federated learning and mechanism probes (tier D; FL held-out test tier C)
Source: RESULTS L482-548, L749-750, L786-798, L927-932, L947-952; `output/posthoc/ph4_keywords.csv`,
`ph4_keywords_cells.csv`, `ph4_mechanisms.csv`, `ph4_summary.json`.
- Units: 68 author keywords (>= 200 submissions each) and 100 k100 topics; N 32,190 decided 2018-26. Estimand:
  unit's acceptance minus all other papers of the same year (level 2018-26, recent 2024-26, trend pp/yr). BH within
  set.
- No keyword or topic flagged (min q: level 0.185, recent 0.367, trend 0.636 for keywords; ph4_summary.json and own
  read of ph4_keywords.csv). Declared tests conservative: permutation rejection 0.5-1.4% at nominal 5%.
- Descriptive spread about +-10 pp. Keywords with >= 5 years (50 of 68): highest pre-training +9.9 (p 0.032),
  imitation learning +8.8, language models +8.0, generative models +6.4; lowest convolutional neural networks -14.2
  (p 0.004), federated learning -11.3, data augmentation -11.0, image classification -10.2, adversarial attack -7.4.
  Diffusion models +8.6 (p 0.02). Topics: neural rendering +13.5, robot learning +11.0, diffusion formulation +10.6;
  clinical ML -14.9, federated learning (m029) -13.5, recommender systems -13.5, graph representation learning -9.8.
- **Federated learning (discovery):** keyword 475 papers, level -11.3 (CI -17.9, -4.8; p 0.005, q 0.19); 2024-26
  -13.5 (p 0.007); trend -3.0 pp/yr (-6.4, +0.5; p 0.08); adjusted level -10.5. Topic m029: 485 papers, -13.5
  (-21.1, -5.9). Below average every year since 2022, about -11 to -15 pp a year since 2023; FL's own acceptance 36%
  (2022) -> 24% (2026). Yearly gaps (ph4_keywords_cells.csv): 2022 -6.9 (44 papers); 2023 -14.6 (96); 2024 -11.2
  (103); 2025 -14.2 (83); 2026 -15.2 (111); 2020 +23.2 on 11 papers (unreliable).
- **PH4b mechanism probes (FL only):**
  1. Composition/influx: not supported. Papers with an author with an earlier accepted ICLR paper 4% (2021) -> ~60%
     (2023-25); keyword newcomers 96% -> 40-58%; team size 4.3-4.9 and method share ~85% stable; composition
     adjustment keeps 76% of the raw trend (ph4_mechanisms.csv: share_of_trend_kept 0.756; adjusted trend -2.2 pp/yr,
     p 0.20).
  2. Field moved on: supported descriptively; FL share of submissions peaked 3.2% in 2023 -> 1.1% in 2026.
  3. Harsher judgement (reviewer scepticism / idea saturation): "consistent with the data, not testable here".
     Decline in every author group: established -1.6 pp/yr, others -3.2, keyword incumbents -1.8, keyword newcomers
     -4.3; none significant; registered reading rule returns "mixed".
- **Held-out H4-FL (registered, tier C):** level -4.9 [-15.4, +5.7], one-sided p 0.14, 134 FL papers, 6 years with
  >= 10; below MDE80 14.5 pp -> uninformative. Trend +3.2 pp/yr [-3.3, +9.6], one-sided p 0.88, opposite sign, no
  MDE. Yearly held-out gaps: 2021 -20.0 (14), 2022 -16.9 (13), 2023 +6.4 (19), 2024 -3.6 (34), 2025 -11.3 (16),
  2026 -0.2 (36). Unregistered: recent level -3.6 [-17.2, +9.9]; adjusted level -3.4. H4-FL's out-of-sample status
  is itself unverified (the earlier keyword grid has unknown provenance).
- **Pooled (exploratory):** FL keyword level -9.9 (q 0.14), topic -12.8 (q 0.037, BH-flagged); trend halves to -1.9
  (keyword, p 0.18) and -1.2 (topic, p 0.34). Four topics BH-flagged in pooled: clinical ML -16.2, FL -12.8, graph
  representation learning -9.7, robot learning +12.1; no keyword.
- Quote: "FL is the starkest discovery case; it was not confirmed on held-out papers (underpowered)". Premia caveat:
  FL was not an extreme in 2018-22 (topic -4.6, keyword -0.6); its gap appeared in 2024-26 (-11.7 / -11.5 pp on 297
  decided papers) (SL L123).

---

## 4. PH5 modules (post hoc in discovery, each family declared before it was run; held-out tests registered 2026-10-18)

### 4.1 Pivot: far jumps from the team's own earlier work (E1 tier B primary; E4 tier B secondary; E2/E3 tier D)
Source: `output/posthoc/ph5_pivot/tests.csv`, `quintiles.csv`, `robustness.csv`, `summary.json`;
`output_pooled/confirmation_run/ph5/tests.csv`; RESULTS L18-23, L751-753, L831-833; SL L19-20, L84-85.
- Measure: F_max = cosine between the abstract and the closest experienced co-author's earlier ICLR submissions
  (histories since 2021). Population: 20,430 decided 2023-26 papers with >= 1 experienced author (acceptance 44.1%).
- **E1 (primary):** P(accept) at F_max p10 minus p50 = **-5.44 pp (CI -7.10, -3.78); Holm 1.3e-8**. Held-out
  **-6.09 [-9.32, -2.86]; 5,344 papers; one-sided p 0.0025, Holm 0.005; MDE80 4.9; power 0.89 at discovery effect;
  supported**. Pooled -5.53 (Holm 1.2e-9).
- Adjusted acceptance by F_max quintile (bottom -> top): 39.7 / 41.8 / 44.4 / 47.2 / 46.9% (quintiles.csv). Bottom
  fifth boundary cos ~0.14.
- Robustness (robustness.csv): newcomer control -5.0; >= 3 prior authors -4.1; no earlier version -5.5; withdrawals
  as rejections (S9) -4.9; early map -5.2; F_last -4.6; F_team -4.7; cleantext -5.39 (Holm 2.0e-8). 2019-20 small
  replication -1.8 n.s. (do not quote).
- **E4 (secondary, within-author slope per +0.1 cos):** +0.55 pp (CI +0.21, +0.90); Holm 0.006; 54,303 author rows,
  19,266 papers. Held-out **+1.06 [+0.23, +1.89]; 4,311 papers; one-sided p 0.006; supported** (no MDE80).
  Pooled +0.78. Cleantext +0.53. Caveat: co-author composition could account for half or more (SL L85).
- E2 (near, p90 - p50): +1.75 (-0.17, +3.66); Holm 0.148 -> E2 quoting rule (held-out +2.34, p 0.17; pooled +2.10,
  Holm 0.036). Tier D.
- E3 (far-jump contrast hot minus other topics): -0.35 (-3.13, +2.42); held-out -3.09 (p 0.35). Tier D (null).
- Correlation of F_max with newcomer flag -0.57 (summary.json correlations), so E1 is partly the newcomer gap; -5.0
  with newcomer control.
- Caveats: far = far from the visible ICLR record since 2021; co-author choice and failure-driven pivots not
  controlled; post-decision abstracts (cleantext check passed in discovery only).

### 4.2 Position: field novelty, novelty floor, twins (P1b tier C; P7 tier C; P1a, P2-P6 tier D; twin shares tier E)
Source: `output/posthoc/ph5_position/tests.csv`, `summary.json`, `free_twin_share.csv`, `free_herding.csv`;
confirmation `ph5/tests.csv`; RESULTS L35-45, L752-754, L811-816, L849-865; SL L21-22, L83, L127-143.
- Novelty = (1 - mean cosine to 10 nearest earlier ICLR papers), as within topic-year percentile. N 31,549 decided
  2019-26 papers (acceptance 40.1%).
- **P1b (least-novel fifth minus middle fifth):** -3.27 pp (CI -4.93, -1.60); Holm 0.0014; negative in 11/11
  variants, Holm-significant in 8 (within class x year -2.0, Holm 0.65; prior-density control -2.4, Holm 0.12; fixed
  reference -2.5, Holm 0.050). Cleantext -3.51. **Held-out -0.13 [-3.50, +3.25]; 8,010 papers; Holm 0.47; not
  supported; uninformative (MDE80 5.4, power 0.47).** Pooled -2.97 driven by discovery papers. Tier C.
- P1a (most-novel fifth minus middle): +0.44 (-1.41, +2.28); held-out +2.54 [-1.40, +6.48] (p 0.20). "Is maximal
  novelty risky? Not at quintile resolution." Tier D.
- Lind-Mehlum inverted-U test p 0.067 (summary.json) - do not quote as a finding.
- **P7 (within-author slope per 10 novelty percentile points, 2023-26):** +0.39 (+0.09, +0.69); Holm 0.105 (not
  significant); cleantext +0.46 (Holm 0.035; "consistent, not upgraded"). Held-out +0.34 [-0.47, +1.16]; 4,810
  papers; one-sided p 0.22; not supported; derived MDE80 ~1.0-1.1 (post hoc). Tier C.
- **P2 (any independent same-year twin, cos >= 0.70):** +0.68 (-0.84, +2.20); Holm 1.0. Held-out (unregistered)
  +3.69 [+0.90, +6.48], p 0.010. Pooled +1.86 (Holm 0.063). Tier D + P2 quoting rule.
- P3 twin x novelty +0.18 (held-out +4.84 n.s.); P4 twin hot minus other -1.49 (-4.51, +1.52) (held-out +1.47 n.s.);
  P5 (Q5-Q3) newcomer minus incumbent +1.32 -> held-out -9.75 (p 0.030) -> pooled +0.4 (sign flips; do not
  interpret); P6 (Q5-Q3) mature minus young +4.69 (Holm 0.24) -> held-out +10.74 (p 0.030) (do-not-quote list).
- Outcome-free twin facts (tier E): any-twin share 19.5% (2019) -> 48.8% (2026); twins per paper per 1,000
  submissions 0.32 -> 0.19 (derived); Spearman(novelty, twins) -0.47 (2019) to -0.71 (2026); 37.7% of 42,326
  papers twinned overall; independent pairs 2018-26: 36,863 at 0.70-0.80 and 1,400 at >= 0.80 (summary.json).
  Newcomer papers less often twinned: -3.9 pp (CI -5.0, -2.7; n 42,325); first-time teams -0.3 n.s.
  (free_herding.csv). Reading in SL: "fits volume better than herding" (SL L142).
- Caveats: twins counted in discovery only (attenuated); identical ideas (cos >= 0.80, 692 decided pairs) only an
  underpowered shared-fate test (p 0.15); abandoned/scooped projects unobserved.

### 4.3 Teams: topic insiders (H1 tier B secondary; rest tier D)
Source: `output/posthoc/ph5_teams/family.csv`, `decomposition.csv`, `robustness.csv`, `summary.json`; confirmation
`ph5/tests.csv`; RESULTS L24, L755, L817; SL L28, L163-181.
- Population: 24,601 decided 2023-26 papers; acceptance 41.1%; papers by number of topic insiders 0: 16,579; 1:
  3,555; 2: 2,053; 3+: 2,414.
- **H1 (one topic insider vs none, at fixed team size and number of experienced authors):** +3.42 pp (CI +1.18,
  +5.66); Holm 0.019 (within family); permutation p 0.005. Held-out **+3.88 [+0.28, +7.47]; 6,243 papers; one-sided
  p 0.017; supported** (derived MDE80 ~4.5, so underpowered -> direction only). Pooled +2.90 (Holm 0.024).
- Robustness: logit consistent; early-map insider +3.0 (p 0.003); without earlier versions +3.4; keyword-based
  insider +0.0 (null); 2019-20 replication +4.3 (-2.9, +11.5) n.s.
- H2 concavity (1 vs 0) - (2+ vs 1): +2.95 (Holm 0.55); held-out +4.47 n.s. Two or more vs one: +0.5 pp (SL L167).
- H3 (1 vs 0) hot minus other: -0.8 (CI -4.9, +3.2). H4 proven outsider minus unproven insider +4.6 (Holm 0.088). H5
  -11.3 (Holm 0.19; do not quote). H6 last- vs first-author insider -2.5 (Holm 0.55). Familiarity without an earlier
  acceptance (767 papers): +0.2 pp (CI -3.8, +4.2) (SL L168).
- Per-head decomposition (decomposition.csv; one specification outside the family): per novice +1.47 pp (CI +0.95,
  +1.99); per crossover +4.77 (+4.23, +5.31); per insider +5.34 (+4.65, +6.04); crossover minus novice +3.30
  (p 2.8e-16); insider minus crossover +0.58 (p 0.16). PH2 gradient on same papers +8.7 per doubling. Tier D.
- Caveats: heavy selection (experienced/insider authors may join better projects); histories since 2021; "not advice
  to recruit names".

### 4.4 Keyword timing states (A1 tier B secondary, weak; A2/A3, B, C tier D; first-time teams tier E)
Source: `output/posthoc/ph5_kwtiming/tests.csv`, `robustness.csv`, `summary.json`, `free_profile_states.csv`;
confirmation `ph5/tests.csv`; RESULTS L25-26, L756; SL L30, L183-217.
- States = keyword age (young/middle/old) x momentum (rising/flat/falling); 759-keyword vocabulary. Population A:
  22,302 papers (40,074 keyword rows), decided 2019-26. Mainstream (old x flat) rate 37.8%.
- **A1 (Emerging = young x rising, minus Mainstream):** +2.67 pp (CI +0.76, +4.58); Holm 0.020 (3-test family);
  null-frame p 0.005; positive in 7/7 variants (censored dropped +4.1; 2-year momentum +3.0; 2022-26 +2.8; early-map
  FE +2.7; no earlier version +2.6; unweighted +2.3; logit). Held-out **+3.25 [-0.18, +6.69]; 5,741 papers;
  one-sided p 0.031; null-frame 0.020; two-sided 0.063; supported (weak: CI includes 0)**; derived MDE80 ~4.3.
  Pooled +3.10 (Holm 0.0015).
- A2 Cooling (old x falling) minus Mainstream +0.13 (Holm 0.90). A3 age gradient +1.74 (Holm 0.077; not supported).
  Old rising +3.9 nominal -> A1 may reflect a low Mainstream baseline as much as keyword age. Within a keyword,
  rising vs flat +0.9 (CI -0.8, +2.7). Omnibus F calibrated p 0.020.
- D_E / D_C profile interactions (teams with no earlier acceptance vs established) +1.1 / -4.0, n.s.; MDE80 5.7-6.2.
  C1 locally early +0.7 n.s. Off-trend +2.0 (p 0.063; do not quote).
- Outcome-free first-time team keyword use (26,640 papers; free_profile_states.csv): Emerging -3.7 pp (raw 16.7% vs
  25.0%; q 6e-6), Cooling +2.4 (q 1e-5), Mainstream +2.3 (q 0.004); young-flat, young-falling n.s. Tier E. Caveats: no
  team-size control; 2021-22 ID switch misclassifies some teams.
- Caveats for A1: age, size and breadth confounded (RL ~18% of Mainstream); labels author-chosen; young cells from
  2020-26; relabelling untested.

### 4.5 Premia: topic acceptance edges and the winner's curse (premia b and EB D0 tier B; keyword lifts tier D/E)
Source: `output/posthoc/ph5_premia/tests.csv`, `summary.json`; `output/ph5_forecast/a1_tests.csv`,
`a1_persistence.csv`; confirmation `ph5/tests.csv`; RESULTS L27-29, L757-758, L818-821; SL L23-25, L103-125.
- Noise-free SD of topic acceptance edges (early map): 6.4 pp (CI 5.0, 7.2; p_perm 0.005); k100 6.1; keywords 4.7;
  areas 4.4. A single year's rate is half noise at ~58 decided papers (n_star 58.5).
- **Premia b (registered unit: early-map topics; 2024-26 edge on 2018-22 edge):** within discovery 0.38 (CI 0.18,
  0.58; Holm 0.001; 82 units). Held-out (held-out 2024-26 on discovery 2018-22) **0.60 [0.32, 0.88]; 75 units;
  intersection-union p 0.003; supported (0 < b < 1)**. Pooled 0.45. Unregistered: k100 0.51 [0.23, 0.79]; keywords
  0.16 [-0.34, 0.66] (no detectable persistence); areas 0.71. Different comparison from within-discovery 0.38.
- Top tenth went +14.3 -> +2.1 pp (early map); top-tenth retention R 0.15 (CI -0.11, 0.42) - do not headline.
- **Premia EB D0 (new held-out test, no discovery counterpart):** EB-shrunk discovery premia predict better than
  zero: D0 1.71 [0.42, 3.01] x 10^-3; MSE 8.76 -> 7.04 x 10^-3; one-sided p 0.005; supported. Descriptive raw-vs-EB D
  0.37 x 10^-3 (p 0.33).
- Keyword winner's curse (outcome-free, forecast module A1; tier D/E): raw-growth top keywords are top again next
  year less often than base (16.0% vs 20.6%; lift -0.045, CI -0.075, -0.017; Holm 0.018; 2,491 keyword-years);
  EB-growth top keywords persist (40.3% vs 22.1%; Holm 0.006) yet gain share less often than others (28.6% vs 36.1%;
  -7.6 pp, CI -12.0, -3.0) (a1_persistence.csv row keyword/eb/h1/all). On topic maps the raw lift is not negative
  (early +0.04, Holm 0.25; k100 +0.11). Raw reversal confined to h = 1 and 10-19-user keywords.
- Surges (unexpected topic booms): incumbents -0.6, newcomers +0.7 pp per SD (Holm 0.50). Tier D (null).
- Shrinkage multipliers 0.37 / 0.52 / 0.65 at 75 / 150 / 300 decided papers are derivations (SL L111). EB tie rule
  changed after outcome-free outputs (disclosed).

### 4.6 Forecast: topic growth on hindsight vs prospective maps (tier E)
Source: `output/ph5_forecast/b4_models.csv`, `b4_conditional.csv`, `summary.json`; SL L27, L145-161.
- Out-of-time 2-year topic growth, test origins 2021-24. Size as predictor: k100 (fitted on all years) R^2 0.28,
  Spearman 0.59 (precision top fifth 0.56); early map (2017-20 only) R^2 -0.03, Spearman -0.04 (p 0.39). Without
  LLM/VLM areas R^2 0.30 vs -0.09.
- Momentum on the early map: Spearman 0.20, precision 0.39 (30/76; chance 0.20); 16/56 (29%) for origins 2021-23.
- In-sample P(top-fifth growth) by size tercile small/mid/large: k100 40 / 21 / 2%; early map 22 / 20 / 20%.
- Caveats: early map cannot represent topics born after 2020; maps differ in fitting corpus and eligibility; no paired
  test. Links directly to the "hindsight manufactures waves" thread (emerging topics 29 vs 8).

### 4.7 FM wave (fmwave): FM premium vs adoption; first-time teams (tests tier D, null; first-time FM gap tier E)
Source: `output/posthoc/ph5_fmwave/tests.csv`, `summary.json`, `free_entry.csv`; SL L183-199, L220.
- Population: 24,596 decided 2023-26 papers (9,908 FM papers).
- A1 slope of FM premium per logit unit of prior adoption +0.19 pp (CI -0.96, +1.34; p 0.74): no detectable change.
- A2 FM premium in topics >= 50% adoption +2.5 (CI -1.3, +6.3; Holm 0.38) on k100 vs +6.0 (+3.1, +8.8) on early map.
- B1/B2 (no-acceptance vs established teams) n.s.; C1 framing premium -2.4 (Holm 0.12; flagged "possibly
  contaminated by camera-ready edits"; do not quote).
- Outcome-free (free_entry.csv; 33,993 submissions 2023-26): first-time teams vs returning topic newcomers submit FM
  papers less often by -1.0 (0-5% adoption, p 0.08), -4.6 (5-15%), -9.0 (15-30%), -14.7 (30-50%) (p <= 1e-4), -2.0
  (>= 50%, p 0.14). Caveats: descriptive; FM label is an LLM label on partly camera-ready abstracts; link to acceptance
  not established.
- Related registered/exploratory context (other dossier): H1d replicated; E1 FM papers +4.6 pp; E8 new-architecture
  papers accepted +8.3 pp more in high-FM topics (p 0.02; "scarcity rather than penalty" hypothesis).

### 4.8 Cleantext robustness (tier D robustness check, discovery only)
Source: `output/posthoc/ph5_cleantext/tests.csv`, `summary.json`; SL L72-77.
- URLs and availability sentences removed; text changed for 22.4% of accepted vs 8.5% of rejected decided 2019-26
  papers (5,820 papers); re-embedded; pivot and position families re-run with frozen code.
- E1 -5.44 -> -5.39 (Holm 2.0e-8) holds; E4 +0.55 -> +0.53 (Holm 0.009) holds; P1b -3.27 -> -3.51 (Holm 0.0004)
  holds; P7 +0.39 -> +0.46 (Holm 0.035) "consistent, not upgraded"; P2 +0.68 -> +0.98 (n.s.).
- Not covered: rewritten results/polished wording, FM/contribution labels, topics, titles; no cleantext on held-out
  papers.

---

## 5. PH6: does a keyword's acceptance gap fall after its share peaks? (tier B, weak)
Source: RESULTS L962-993; `output_pooled/posthoc/ph5_waves/tests.csv`, `keywords.csv`, `profile.csv`,
`wave_table.csv`, `summary.json`. Declared in PREREGISTRATION 2026-10-28, run once; post hoc (question came from
viewing discovery per-year gaps of six keywords, disclosed).
- Waves (outcome-free): 17 of 68 keywords (adversarial attack, semi-supervised learning, robustness, representation
  learning, data augmentation, adversarial robustness, graph neural networks, multi-agent RL, optimal transport,
  vision transformer, federated learning, contrastive learning, differential privacy, offline RL, self-supervised
  learning, fairness, explainability). Six inspected first: adversarial attack, adversarial robustness, GNNs, FL,
  contrastive learning, self-supervised learning.
- Estimand D = weighted mean over waves of (gap after peak - gap up to peak); 2,000 within-year permutations.

| Split | Waves | D (pp) | 95% interval | One-sided p | MDE80 | Papers pre / post |
|---|---|---|---|---|---|---|
| Held-out (declared test) | 17 | -5.2 | -11.1 to +0.7 | 0.043 | 7.4 | 454 / 1,022 |
| Held-out, without six inspected | 11 | -1.7 | -9.7 to +6.3 | 0.33 | 10.1 | 222 / 554 |
| Held-out, without FL | 16 | -6.2 | -12.5 to +0.1 | 0.033 | 7.9 | 406 / 936 |
| Discovery (not a test) | 17 | -5.7 | -8.5 to -2.9 | < 0.001 | 3.6 | 1,776 / 3,975 |
| Discovery, without six inspected | 11 | -3.7 | -7.5 to +0.2 | 0.034 | 4.8 | 916 / 2,102 |

(Held-out decided papers 8,185; discovery 32,190. RESULTS L977 prints -11.1; tests.csv gives -11.045 to +0.670.)
- Verdict: supported only just; two-sided interval includes 0; estimate below MDE80 -> direction only.
- Drivers: vision transformer largest drop in both splits (-39.8 discovery / -32.9 held-out, on 27/101 and 3/34
  papers pre/post). FL itself: discovery -5.9, held-out +3.5 (does not decline; consistent with H4-FL trend not
  supported). Contrastive learning held-out -33.9.
- Shape (discovery, descriptive; profile.csv): relative to each wave's level, the gap is +9 to +30 pp at 2-5 years
  before the peak (few papers: 9-300), near 0 around the peak, -2 to -5 pp 3-5 years after. "Early arrivals do best;
  the decline starts before the peak." Held-out profile noisy.
- Fits kwtiming A1 (young rising keywords +2.7 discovery, +3.3 held-out).
- Quote with: "post hoc, declared before its single held-out run; leans on the six keywords inspected first".

---

## 6. Planned exploratory analyses that the post hoc work builds on (tier D)
Source: RESULTS L350-373, L922-924.
- E1 FM papers +4.62 pp within topic x year (p < 0.001); pooled +5.61.
- E2 newcomer papers -10.2 pp (base 40%); -10.5 in ID-consistent years; pooled -10.2.
- E3 withdrawal after review +1.62 pp per log unit of maturity (p 0.009).
- E5 newcomer x hot interactions -0.4 / -0.6 / +0.2 pp, all n.s.
- E8 new-architecture papers x prior FM adoption +8.3 pp (p 0.02); pooled +9.4 (p 0.010).
- E10 acceptance by class vs method: theory +8.9, dataset/benchmark +3.9, empirical -2.7, evaluation -1.9 (n.s.),
  other -8.0.

## 7. Registered results (cross-reference only; full detail in the registered dossier)
Source: RESULTS L11-19, L47-56, L743-758.
- Tier A: H1d -8.0 (-12.1, -3.8) / held-out -11.0 [-18.1, -3.9]; H2b' +3.71 / +3.60 [+1.48, +5.71]; H2c' -1.70 /
  -2.10 [-3.35, -0.85]. H2c shrinks with team size (discovery -0.54, held-out -0.98).
- Tier C: H3a -1.68 (-3.68, +0.32) / -1.51 [-5.20, +2.19], uninformative; H2a -0.73 inconclusive; H3b inconclusive;
  H4-FL not confirmed (Sec. 3, PH4).

## 8. One-line status table (for the paper's findings table)

| Finding | Discovery | Held-out | Tier | Must-carry caveat |
|---|---|---|---|---|
| Far jump from team's own record (E1) | -5.44 (-7.10, -3.78) | -6.09 [-9.32, -2.86] | B (primary) | ICLR record since 2021; co-author choice not controlled |
| Within-author closeness slope (E4) | +0.55 per +0.1 cos | +1.06 [+0.23, +1.89] | B (secondary) | composition may explain half |
| One topic insider vs none (teams H1) | +3.42 (+1.18, +5.66) | +3.88 [+0.28, +7.47] | B (secondary) | underpowered; selection; keyword-insider null |
| Young rising vs old flat keyword (A1) | +2.67 (+0.76, +4.58) | +3.25 [-0.18, +6.69] | B (secondary, weak) | 95% CI includes 0 |
| Topic edges persist but shrink (premia b) | 0.38 (0.18, 0.58) | 0.60 [0.32, 0.88] | B (secondary) | early-map topic units only; keywords 0.16 n.s. |
| EB-shrunk premia beat zero (D0) | none | 1.71e-3 [0.42e-3, 3.01e-3] | B (new test) | no discovery counterpart |
| Gap falls after keyword's share peak (PH6) | -5.7 (-8.5, -2.9) | -5.2 (-11.1, +0.7), p 0.043 | B (weak) | without six inspected: -1.7, p 0.33 |
| Least-novel fifth (P1b) | -3.27 (-4.93, -1.60) | -0.13 [-3.50, +3.25] | C | not replicated; uninformative |
| Within-author novelty slope (P7) | +0.39 (+0.09, +0.69), Holm 0.105 | +0.34 [-0.47, +1.16] | C | not supported |
| Federated learning gap (PH4 / H4-FL) | -11.3 (-17.9, -4.8), q 0.19 | -4.9 [-15.4, +5.7] | D / C | not confirmed; trend opposite sign |
| Newcomer gap within same authors (PH3) | -3.1 (-4.5, -1.6) vs -5.4 without author FE | - | D | need not be reviewer bias |
| Team size gradient (PH2) | +8.8 per doubling (+8.0, +9.7) | - | D | proxies compute/seniority |
| Newcomer correlates (PH1) | theory +10.2; FM +4.1; 7+ authors +11.1 | - | D | selection |
| Concurrent twin (P2) | +0.68 (-0.84, +2.20) | +3.69 [+0.90, +6.48] (unregistered) | D | P2 quoting rule |
| Near closeness (E2) | +1.75, Holm 0.148 | +2.34 (p 0.17, unregistered) | D | E2 quoting rule |
| Keyword winner's curse (raw lift) | 16.0% vs 20.6%; Holm 0.018 | - | D/E | keywords only; h = 1 only |
| Hindsight map forecastability | R^2 0.28 vs -0.03 | - | E | maps differ in corpus |
| Twin share 2019 -> 2026 | 19.5% -> 48.8%; per-pair 0.32 -> 0.19 | - | E | volume, not herding |
| First-time teams fewer FM papers | -4.6 to -14.7 pp (5-50% adoption) | - | E | LLM label; no acceptance link |
| First-time teams fewer Emerging keywords | -3.7 pp (16.7% vs 25.0%) | - | E | no team-size control |
| NAME: subtitle title share | 7-14% (2017) -> 37-49% (2026), definition-dependent | - | E* | re-verified here; Notion said 9% -> 41% |
| NAME: title acceptance ratio | 1.02 (OR 1.00) | - | D* | earlier exploratory; not re-run |
| Returning first authors lag on title style | ~40% lag (figure) vs ~3% topic lag | - | E* | Notion only, not re-verified |
| LLM-favoured title verbs after 2023 | OR 2.2 | - | E* | Notion only, not re-verified |
