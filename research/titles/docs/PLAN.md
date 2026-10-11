# Working title: **"Branded by People, Polished by Machines: The 2024 Naming Turn in ICLR Titles, Who Carried It, and What Peer Review Did to It"**

## 1. Thesis of the study section

Between 2023 and 2026 the share of ICLR submissions titled "NAME: subtitle" doubled (20.3% → 40.5%), with a dated slope break at 2024 (pilot ITS slope-change OR 1.28/yr; placebo breaks in 2021 and 2022 null). We observe the whole submission pool: accepted, rejected, withdrawn and desk-rejected papers. With it we argue that the naming turn is a **human research fashion that the LLM era sped up but did not create**:

- **Content explains only a minority.** A counterfactual built from name-masked abstracts accounts for about 30–45% of the rise.
- **Unexplained drift accelerated.** Drift that content cannot explain was already running at about 1.7 pp/yr before 2024. It rose to about 3.9 pp/yr after.
- **Detectable LLM drafting adds little.** Its contribution is small and bounded from above.
- **The same people changed.** The rise happened mostly within incumbent authors (communal change), not through cohort replacement (generational change). A generational increment shows up only at the first-author level.
- **LLMs left a lexical signature, not a structural one.** In title slots where meaning is held fixed, LLM-favoured verbs jump at 2024 (pooled OR ≈ 2.7) while control pairs stay flat. Their register turns over in step with the model generation whose markers appear in the same paper's abstract.
- **Peer review neither creates nor amplifies the naming fashion.** The accepted/all NAME ratio is about 1.00–1.05 every year. Review does deplete LLM and outsider markers, so studies of published papers alone are nearly unbiased for mainstream title fashion but understate how many submitters used LLMs.

Abstracts play three roles: the content counterfactual (D1), the topic contrast to style (D2), and the LLM-vintage channel (D3, D4). Every headline claim is diachronic, uses submission-stage text, or is bounded by the arXiv camera-ready audit.

---

## 0. Common definitions (apply to all directions unless overridden)

**Universe U.** All 43,516 discovery rows, minus placeholder titles and abstracts, minus the one empty title.
- Placeholders follow `features.is_placeholder`: title in {NA, N/A, withdraw(n), title, placeholder, …} or abstract under 20 words.
- Report the count dropped per year.
- NFKC-normalise titles. Exclude ratio colons. Handle LaTeX through `features.strip_math`.

**Pools.**
- **ACC/REJ (acceptance population):** README filter (`ordinary_submission`, `outcome_eligible==1`, decision ∈ {accepted, rejected}). The 27 inconsistent rows drop out automatically.
- **WD (withdrawn):** `administrative_status=='withdrawn'`. There are none in 2017. 2018–23 withdrawals carry decision "unknown". The 349 post-decision withdrawals in 2026 (decision "rejected") are flagged `wd_post`.
- **DR (desk-rejected):** `administrative_status=='desk_rejected'`.
- **NA (camera-ready-free):** REJ ∪ WD ∪ DR. Its title and abstract are submission-stage.

**Years and periods.**
- Pre = 2017–2023 (2018–2023 wherever withdrawals are needed). Post = 2024–2026.
- 2026 is always also reported separately as a separate cohort (new desk regime, 15.4k submissions).
- 2019 is run with and without, because of the outcome correction.
- "Excluding 2026" variants use 2024–25 only.

**Title features.**
- Use `features.py` version-locked at a commit hash, extended in `features_v2.py`.
- **NAME (primary):** `name_colon`, i.e. a coined lead before a colon or spaced dash.
- **NAME alternatives:** strict = single-token lead; loose = any lead ≤ 2 tokens that is not a function or genre word; compound = any colon or dash.
- **Orthography:** all_caps, mixed_case, word, paren_acronym.
- **Casing class.**

**Topic.**
- topic50 and topic100: KMeans on MiniLM abstract embeddings (`cache/topics.parquet`).
- Replication: topic50 and topic100 refit on bge-small (512-token) abstract embeddings.
- **LLM topic:** `llm_topic` regex, OR membership in a topic100 cluster where more than 50% of papers match the regex.
- **Non-LLM subset:** neither condition holds.

**Area.**
- `primary_area` exists for 2024+ only.
- A crosswalk harmonises 2024 labels with the 2025–26 labels. Year×area FE are used in 2024+ models only.

**Controls.**
- log(#authors) (`declared_name_count`).
- `llm_topic`.
- Author experience (2022+ only): `max_prior_subs`, `max_prior_accs`, `share_new_authors`, `last_prior_accs`.
- Title length is **not** a control in trend models, because it is a co-moving outcome (bad control). Length-bin FE are a robustness check only.

**Estimation conventions.**
- Binary outcomes: logit (ORs) for trend and association models; LPM for decompositions and high-dimensional FE.
- SEs clustered by topic100 for paper-level models, by author key for author-panel models, and by word or slot for word panels.
- With only 10 years, break inference also uses randomization over placebo break years.
- FE LPMs use in-house alternating-projection demeaning in `_core.py`. pyfixest and linearmodels are not installed; try `pip install pyfixest` first and keep the in-house version as fallback.

**Multiple testing.**
- Holm within each direction's confirmatory family.
- BH (q = 0.05) across the exploratory atlas and the marker lists.

**Language rules (README boundaries).**
- Profile IDs are "declared profile keys", not persons.
- No influence or supervisor claims.
- Author order is used only as a partition label ("first/last list position"), never as seniority.
- Topic, acceptance and outcome claims are associational.

---

## 2. Locked directions

### D1. The 2024 naming break: content, people, or tool? *(C1 core + people channel from C2/teamsize check + C7-H1 as positive control link)*

**Research question.** The 2024 slope break in NAME titles could come from what papers are about (content and LLM topic), from who writes them (team and newcomer composition), or from LLM drafting (tool). Or it could be a change in how given content is titled (fashion). How much does each account for, and did the content-unexplained drift accelerate at 2024?

**Hypotheses**

- **H1a (dated break).**
  - In a segmented logit on U, the 2024 slope change is OR > 1 (pilot 1.28/yr).
  - The break holds in the NA pool and in the non-LLM subset (pilot NA share 0.20 → 0.41; non-LLM 0.200 → 0.371).
  - A sup-LR scan over candidate breaks 2020–2025 selects 2024 or 2025. Placebo breaks at 2020, 2021 and 2022 are null.
- **H1b (content is a minority).** Content's share of the 2023→2026 rise lies in [0.20, 0.50] for every name-masked representation, and none exceeds 0.60. Pilot: fixed-window masked TF-IDF 29%; rolling 42%; unmasked bge 45%, which is an upper bound because names leak.
- **H1c (primary estimand: acceleration of unexplained drift).**
  - Define the one-step-ahead unexplained increment u_y = obs_y − p̂_y. Here p̂_y comes from a content model trained on y−3..y−1, with its intercept recalibrated so that cross-fitted predictions match obs_{y−1}.
  - Prediction: mean(u_2024–26) − mean(u_2019–23) > 0 and the ratio is ≥ 1.5.
  - Pilot: 1.7 → 3.9 pp/yr, ratio 2.3. Content steps are +1.5, +3.6 and +3.3 pp in 2024–26 against ≈ 0 to +0.9 pp before.
- **H1d (people/composition is a minority).** DFL reweighting of 2024–26 to the 2023 composition explains ≤ 30% of the rise. The reweighting uses team-size bins (1–2, 3, 4, 5, 6–7, 8+) × share-new-author bins (0, (0, .5], (.5, 1)) × llm_topic. Pilot: team size alone 18%; size × LLM topic 26%.
- **H1e (tool, bounded).**
  - (i) Among papers without an LLM fingerprint (F = 0), the 2023→2026 NAME rise is ≥ 85% of the full-population rise.
  - (ii) The fingerprint uplift δ on NAME is small: LPM within topic100 × year, 2024–26, δ ≤ +5 pp (pilot colon adjOR 1.24).
  - (iii) The implied maximum tool share is δ × A_max / ΔNAME < 0.25. A_max is an upper prevalence of LLM drafting; the sensitivity range is 0.24–1.0, with 0.39 from the held-out greedy abstract bound for 2026.

**Operationalisation**

- **Population:** U, 2017–2026. Restricted variants: NA pool, non-LLM subset, 2018+ (to drop the tiny 2017 cell).
- **Outcome:** NAME (primary); strict, loose and compound as alternatives.
- **ITS model:**
  `logit P(NAME_i) = α + β(t−2023) + γ·post + δ·post·(t−2023) + λ·log authors + κ·llm_topic + topic100 FE`.
  - Variant with year dummies: deviations from the extrapolated 2017–23 linear trend.
  - Randomization p for δ comes from refitting with the break at each year from 2019 to 2025.
- **Content counterfactual representations** (L2 logit; C chosen by 5-fold CV inside the training window):
  - **R1 (primary):** name-masked abstract TF-IDF on 1–2-grams.
    - Masking removes the title's lead string and keeps only originally lowercase tokens, which drops coined names and acronyms.
    - Parameters: min_df 5, max_df 0.5, 50k features, sublinear tf.
  - **R2 (lower):** keyword TF-IDF on `normalized_keywords_json`.
  - **R3:** bge-small embeddings of name-masked abstracts. Re-embed 2018–26 abstracts with the lead name and every CamelCase or ALLCAPS token (≥ 3 characters) replaced by "[NAME]". This takes about 1.5 CPU-hours in the background.
  - **R4 (upper, leaky):** bge-small embeddings of unmasked abstracts.
  - **R5 (genre-stripped):** R1 minus a frozen list of rhetorical-move n-grams ("we introduce", "we propose", "framework", "novel", "we present", "this paper"). This separates abstract-genre fashion from content.
  - **R6 (coarse):** topic100 one-hot plus llm_topic.
- **Designs:**
  - **Fixed window:** train on 2021–23, predict 2024–26.
  - **Rolling one-step-ahead (primary for H1c):** train on y−3..y−1 for y = 2019..2026, with intercept recalibration to y−1 on cross-fitted scores.
- **People:** DFL reweighting as defined in H1d. Shapley decomposition over the orderings (content → people) and (people → content), with ΔNAME split into content, composition and residual.
- **Tool:**
  - Fingerprint F = F24 ∪ F26 ∪ title typography (definitions in D3).
  - Compute the NAME trend for F = 0 against all papers.
  - Estimate δ by LPM `NAME ~ F + log authors + topic100×year FE` on 2024–26.
  - Draw a sensitivity curve of maximum tool share against A_max.
- **Positive control link:** D3's slot result (OR ≈ 2.7–4) shows that the toolkit detects LLM influence where it exists. This is reported beside H1e.

**Identification and robustness**
- Placebo training window: train on 2018–20 and predict 2021–23. This shows that pre-2024 unexplained drift exists, which is why H1c is a difference in unexplained drift.
- **New-topic placebo** (answers the extrapolation critique):
  - Calibration-in-the-large for papers in topic100 clusters whose share grew at least 3× relative to the training window, e.g. diffusion in 2022–23.
  - Pass if |obs − pred| in fast-growing clusters ≤ |obs − pred| elsewhere + 2 pp.
- Replications: NA pool; non-LLM subset; MiniLM vs bge topics; all four NAME definitions; with and without 2019; excluding 2026; year×area FE for 2024+.
- **Bracket reporting:** all R1–R6 content shares are reported. Claims use only the name-masked range. Framing is "accelerated at 2024", never "caused by ChatGPT".
- Multiple testing: Holm over H1a–H1e.

**Expected figures and tables**
- **F1.1:** observed NAME share 2017–26 against counterfactual ribbons (R1–R6 envelope). Inset: NA pool.
- **F1.2:** annual steps split into content and unexplained parts, 2019–2026, with the pre and post means marked.
- **F1.3:** 2023→2026 decomposition bars for content, team/newcomer composition, the detectable-tool bound, and residual fashion.
- **T1.1:** ITS coefficients across pools, subsets and definitions.
- **T1.2:** representation bracket with out-of-sample AUC and calibration slope.
- **T1.3:** tool-bound sensitivity table.

**Falsification**
- H1a fails if the NA-pool slope-change CI includes 1, or if any placebo break is at least as large.
- H1b fails if any name-masked representation explains ≥ 60%.
- H1c fails if the ratio is < 1.2 or the CI of the difference includes 0.
- H1d fails if composition explains ≥ 50%.
- H1e fails if the F = 0 rise is < 70% of the total, or the maximum tool share at A_max = 0.39 is ≥ 0.5.

---

### D2. Who carries the fashion: communal vs generational change *(C2 core + C4-H1 and C15 future-tie placebo as supporting tests)*

**Research question.** Is the post-2023 change in title style produced by the same declared profile keys changing their titles (communal change; Labov, Ryder) or by entrants replacing exiters (generational change; the Planck principle per Azoulay et al. 2019, and Danescu-Niculescu-Mizil et al. 2013)? Does the channel differ between style and topic, and between list positions?

**Hypotheses**

- **H2a (communal dominance at last position).** In a Kitagawa decomposition of the early-to-late change, the within-stayer share is ≥ 0.70 for the last-position partition and ≥ 0.60 for the any-role partition. Early is E = 2022–23 and late is L = 2025–26. Pilot: last ≈ 1.00 (18.9 → 37.1 vs 19.5 → 37.8); any-role 0.83.
- **H2b (generational increment at first position).**
  - The first-position within-stayer share is lower than the last-position share by ≥ 0.2 (pilot 0.58 vs 1.00).
  - Entrant first authors' late NAME share exceeds that of stayer first authors.
- **H2c (not driven by entrant co-authors).**
  - Model, on stayers' author-paper rows: `NAME ~ key FE + year FE + post×share_new_coauthors + log authors + llm_topic + topic100 FE`.
  - The implied post change at share_new_coauthors = 0 is ≥ 0.5 × the population change.
  - Teams in which every key appeared in an earlier year (rolling definition) rise by ≥ 0.5 × the population rise (pilot +12.1 vs +20.2 pp = 0.60).
- **H2d (style vs topic channel).**
  - Across markers m, regress within-stayer change on population change. Expect slope ≈ 1 (pilot 0.97, r = .985 over 175 words).
  - Style markers: ≥ 40 pre-registered title forms and words (NAME, compound, Title Case, register verbs, via, top snowclones, mixed-case and ALL-CAPS names).
  - Topic markers: abstract topic100 clusters with |Δshare| ≥ 1 pp, plus llm_topic.
  - The generational increment share (1 − within/pop) is larger for style than for topic.
- **H2e (pre-LLM replication).** For 2018→2020, using email keys, the colon and NAME rise is ≥ 50% within stayers. Communal change is then the general mode, not an LLM-era artefact.

**Supporting tests (exploratory, reported as robustness paragraphs)**
- **S2.1 Within-paper retitling (C4-H1).**
  - Pairs: resubmissions detected by a shared key plus abstract cosine, with the union rule bge ≥ 0.95 or MiniLM ≥ 0.85.
  - Expect mean ΔNAME ≈ 0 for destination years ≥ 2024 (pilot 0.000, se 0.025, 28 adds and 28 drops, n = 297), against an implied drift of +7 pp.
  - Stated as "even among retitled papers, NAME is not added on net". Transition rates are not reported as behaviour, because the pairs are selected on retitling.
- **S2.2 Future-tie placebo (C15).**
  - Clean sample excluding the exposing collaborators. Expect past-collaborator exposure (pilot .045, se .028) to be no larger than future-collaborator exposure (pilot .118, se .026).
  - Topic-content exposure serves as a positive control. The MDE is reported.
  - Framed only as falsifying a tie-contagion account. No influence claims.

**Operationalisation**
- **Panel:** `native_id_kind=='profile'` keys, 2021–26; author-paper rows.
- **Partitions:**
  - last list position;
  - first list position;
  - any role, with rows weighted 1/#keys so each paper sums to 1;
  - paper-level team types: all-prior, mixed, all-new, under both a rolling definition (seen in any earlier year) and a fixed base window (seen in 2021–22).
- **Groups:**
  - stayers: ≥ 1 paper in E and ≥ 1 in L;
  - exiters: E only;
  - entrants: L only and never seen before;
  - returners: seen in 2021 or 2024 only; kept separate.
- **Decomposition.** Let s be the stayer weight, S stayers, X exiters, N entrants, bars the E/L average, and O "others" (exiters in E, entrants in L). Then
  Δ = s̄·(P_SL − P_SE) [within-stayer] + (1 − s̄)·(P_NL − P_XE) [replacement] + (s_L − s_E)·(P̄_S − P̄_O) [weight shift].
  Paper- and author-weighted versions are both reported, with bootstrap CIs clustered by key (1,000 reps).
- **Markers for H2d:** frozen list in `lexicons.json`. Topic markers use the abstract-based topic100 clusters.

**Identification and robustness**
- **Exiter–stayer comparability:** NAME in 2022–23 (pilot last-position .214 vs .189).
- **IPW for staying:** logit on E-period covariates (number of papers, prior acceptances, topic, team size, own NAME use).
- **Bounds:** (a) exiters frozen at their E level; (b) exiters given the entrants' L level.
- **Censoring:** fixed-window vs rolling definitions; a fixed 1-year lookback.
- **Held-out-removal simulation:** drop a further 20% of discovery papers at random, 200 times, recompute the within share, and extrapolate the 80%→100% coverage bias. This addresses false entrants whose earlier papers sit in the held-out split.
- **Alias sensitivity:** collapse profile IDs differing only by trailing digits (`~First_Last1/2`) as an upper bound on stayer status.
- **Further robustness:**
  - outcomes measured on NA-pool papers only (camera-ready-free);
  - excluding 2026 (E = 2021–22, L = 2024–25);
  - trimming the top 1% most prolific keys;
  - topic100 FE and team-size-bin variants;
  - team-type × size cells (pilot within-cell share 0.77–0.87).
- **Language:** no person-level or seniority language.

**Expected figures and tables**
- **F2.1:** 45-degree scatter of within-stayer change against population change per marker, coloured style vs topic.
- **F2.2:** decomposition bars by partition (last, any, first, team type) with IPW and the two bounds.
- **F2.3:** NAME level by year for stayers, entrants and exiters, per partition.
- **T2.1:** decomposition table.
- **T2.2:** author-FE models (H2c).
- **T2.3:** supporting tests S2.1 and S2.2 with MDEs.

**Falsification**
- H2a fails if the upper CI of the last-position within share is < 0.5.
- H2b fails if the first- and last-position shares do not differ (CI of the difference includes 0) and the first-position share is ≥ 0.8.
- H2c fails if the change at share_new = 0 has a CI that includes 0 and a point estimate < 0.3 × the population change.
- H2d fails if the slope is < 0.7 or topic markers show a significantly larger generational increment than style markers.
- H2e fails if the pre-LLM within share is < 0.3.

---

### D3. The machine register: meaning-fixed slots, vintage turnover and a bounded second-hand diffusion test *(C7 H1, H3, H4-light; local generation and positive-unlabelled estimation dropped)*

**Research question.** Detectors fail on 10-word titles, and the naming fashion predates ChatGPT. Where meaning is held fixed, did LLM-favoured wording break at 2024? Did that register turn over with model generations, and does it line up with the LLM generation visible in the same paper's abstract? Does the tool leave a lexical signature rather than a structural one?

**Frozen inventories** (`lexicons.json`, hashed)

- **LLM slots** (title-opening gerund, after an optional "NAME:"):
  - **S-improve:** {Enhancing, Boosting, Advancing, Elevating, Empowering} vs {Improving}.
  - **S-reveal:** {Unveiling, Uncovering, Unraveling, Demystifying, Decoding} vs {Understanding, Analyzing/Analysing, Investigating, Characterizing, Explaining}.
  - **S-exploit:** {Leveraging, Harnessing, Unleashing, Unlocking} vs {Exploiting, Utilizing, Enabling}.
  - **S-study-adj:** {comprehensive} vs {systematic, extensive, large-scale} before {study, benchmark, evaluation, analysis, survey, investigation, review, assessment}.
  - Senses excluded after validation V2, e.g. "Boosting" as the boosting algorithm, and LM "Decoding".
- **Control pairs** (no 2024 LLM preference expected): Towards/Toward; novel/new; via/using.
  - via/using is a control for the 2024 break only. It drifts up gradually from 2018 and accelerates in 2026 (0.78 → 0.90).
- **Register families:**
  - R24 = {enhanc*, leverag*, unveil*, unleash*, harness*, empower*, elevat*, boost*}.
  - R26 = {unified, unifying, beyond, bridging}.
- **Fingerprints:**
  - F24 = abstract has ≥ 1 RARE21 word (fixed 2024-generation list; the ≥ 2 variant is used for D1).
  - F26 = abstract has ≥ 1 of {principled, reframe*, genuine*, brittle, auditable, sharply, high-stakes}, or U+2011 / en-dash letter compounds in title or abstract.
  - F = F24 ∪ F26 ∪ title typography.

**Hypotheses**

- **H3a (slot break).**
  - Pooled slot logit: post-2024 OR ≥ 2 (pilot 2.69 [1.80, 4.01], n = 2,362; improve slot alone ≈ 4.3).
  - Control pairs: post OR within [0.67, 1.5] (pilot 0.87 [0.64, 1.17]).
  - The slot-minus-control difference in log OR is > 0.
- **H3b (register turnover).**
  - From 2025 to 2026, R24 per-1k title rate falls within area in ≥ 10 of 16 large areas (pilot enhanc* 36.7 → 25.6 per 1k; down in 12 of 16).
  - R26 rises in ≥ 12 of 16 (pilot unified 11.2 → 23.1; up in 16 of 16).
- **H3c (vintage alignment across channels).**
  - In 2025–26, with year, topic100, log authors, llm_topic and log title length as controls: OR(F24 → R24 in title) > OR(F26 → R24 in title).
  - Pilot: 1.29 [1.09, 1.53] vs 0.83 [0.66, 1.05].
  - The mirror contrast for R26 is exploratory; the pilot is weak (F26 1.23 vs F24 1.17).
- **H3d (lexical, not structural, signature).**
  - In 2024–26 within topic100 × year: OR(F → LLM slot variant | slot filled) ≥ 1.5 × OR(F → NAME).
  - Pilot: slot share fingerprinted vs not, 0.78 vs 0.57 in 2024 (OR ≈ 2.7), against NAME/colon adjOR ≈ 1.24.
- **H3e (exploratory, bounded: second-hand diffusion).**
  - F = 0 papers also break: improve slot .31 → .57 in 2024.
  - Compute U* = (p_F0,post − p_pre)/(p_F1,post − p_pre). This is the share of undetected LLM users among F = 0 papers needed to explain their break (pilot 2024 ≈ 0.55).
  - "Second-hand diffusion" is claimed only if U* > 0.8 in a pooled-slot analysis. Otherwise it is reported as unresolved.
  - Gap closure in 2026 is not interpreted, because fingerprint recall decays (RARE21 19.2% → 9.1%).

**Models**
- Slot logit, 2018+:
  `y_i ~ slot FE + slot×(t−2023) + post + llm_topic (+ topic100 FE as robustness)`, with SEs clustered by topic100. LPM is used where cells are sparse.
- Stacked slot + control model with a `post × LLM-slot` interaction (the confirmatory parameter).
- Register: per-area Poisson on counts with a log(#titles) offset, 2023–26, with area FE.
- Vintage: logit as specified in H3c.
- Signature: two LPMs on the same papers; compare the ratio via a seemingly-unrelated bootstrap.

**Identification and robustness**
- NA-pool replication; non-LLM subset.
- Exclude titles whose own abstract contains the same verb, so the test isolates title-specific choice.
- Leave-one-variant-out within each slot.
- Opener-position variants: title start vs post-colon.
- Excluding 2026.
- Camera-ready: audit word-level flips for opener verbs among pre-decision arXiv v1 pairs.
- 2024-only analysis, the cleanest year.
- BH correction over per-slot estimates.

**Expected figures and tables**
- **F3.1:** LLM-variant share by year per slot, with the control pairs in grey.
- **F3.2:** area × year heat map of R24 vs R26 rates, 2023–26.
- **F3.3:** forest plot of vintage alignment (F24/F26 × R24/R26).
- **F3.4:** lexical vs structural signature: OR_slot vs OR_NAME.
- **T3.1:** slot model table.

**Falsification**
- H3a fails if the pooled OR CI includes 1 or the controls break comparably.
- H3b fails if fewer than 9 of 16 areas move in the predicted direction.
- H3c fails if the OR ratio is ≤ 1.
- H3d fails if OR_slot ≤ OR_NAME.

---

### D4. The gatekeeper: stage-wise filter gains and the bias of published-only title studies *(C6 core + C3-H1 exit composition + C5 audit as the decision-stage bound)*

**Research question.** Treat ICLR as a sequence of stages: desk screen, then author exit (withdrawal), then decision. What does each stage do to fashionable, outsider and LLM-styled title and abstract features? How wrong would a study of accepted papers alone be?

**Stages** (2018–2026; the desk stage is substantive only in 2025–26, where 2026 has 737 desk rejections)
- s0 = U.
- s1 = not desk-rejected.
- s2 = s1 and not withdrawn before decision. `wd_post` rows stay in s2 as rejected; dropping them is a sensitivity check.
- s3 = accepted.

**Gains**
- G_desk = P(f|s1)/P(f|s0); G_exit = P(f|s2)/P(f|s1); G_dec = P(f|s3)/P(f|s2); G_total = P(f|s3)/P(f|s0).
- CIs: paper bootstrap stratified by year, 2,000 reps.
- Adjusted gains: continuation-ratio logits for passing each stage, with year FE (year × area for 2024+), log authors, llm_topic and topic100.

**Feature sets**
- **Mainstream M:** NAME, compound, phrase-colon, mixed-case name, Title Case.
- **Outsider O:** ALL-CAPS title, sentence case, question opener.
- **LLM L:** title typography, R24, R26, abstract F24, F26, em-dash, and year-specific LLM-style density.

**Hypotheses**

- **H4a (neutral filter for the mainstream fashion).**
  - NAME G_total lies in [0.95, 1.10] in every year 2018–26 (pilot 1.01–1.04 for 2024–26).
  - Pooled 2024–26 passes TOST equivalence within [0.90, 1.11].
  - The 2024 slope-change OR is equal across the ACC, REJ and WD pools: Wald equality test, |Δlog OR| < 0.1 (pilot 1.14–1.16).
- **H4b (depletion of LLM and outsider markers).**
  - Pooled 2024–26 G_total < 1 for the L-union and O-union. Pilot: LLM typography 0.79 in 2026; ALL-CAPS 0.37.
  - G_desk × G_exit < 1 for the L-union. These stages use submission-stage text, so the result needs no audit.
- **H4c (published-only bias in LLM-usage estimates).**
  - A Kobak-style lower bound on LLM-styled abstracts, computed on accepted papers, understates the all-submission bound by ≥ 15% relative in each of 2024–26.
  - Pilot RARE21: 12.8/8.7/3.0 pp (accepted) vs 15.8/12.0/5.8 pp (all).
  - Direction argument: camera-ready polishing could only raise accepted papers' marker rates, so the understatement is conservative. This assumption is stated.
- **H4d (exit composition; C3).**
  - Within NA, for withdrawn vs rejected, the NAME coefficient is > 0 in the cross-section (pilot +3.6 pp, se 0.55).
  - It is ≤ 0 within last-author FE (pilot −1.4 pp, se 0.75), and the two differ.
  - The withdrawal excess of named papers is therefore between authors.
- **H4e (published-only atlas, descriptive).**
  - Pre-registered list of about 20 fashion statistics:
    - yearly prevalence of the M features;
    - the ITS slope change;
    - LLM abbreviation-only share;
    - snowclone share;
    - name-collapsed opener entropy (rarefied to equal n);
    - lexical-turnover JSD;
    - peak years of the top-30 title fashions;
    - colon-premium trend.
  - Accepted-only estimates fall within ±10% relative of all-submission estimates for M metrics. Deviations concentrate in O and L.
  - Each gap is split into a selection part (exact for the desk and exit stages) and an editing part, bounded by the audit.

**Decision-stage bound (snapshot module)**
- Per feature, the audit gives net flips (adds − drops) among accepted vs rejected pre-decision arXiv v1 pairs.
- Report the G_dec interval implied by the CI of the net-flip DiD.
- Report the tipping point: the net-flip DiD that would bring G_dec to 1. For NAME it is about 1.8 pp, against a current +2.1 (se 2.4). G_dec for NAME is therefore reported as not identified until the audit is enlarged.
- No acceptance claim enters the headline unless its tipping point exceeds the upper CI of the audit.

**Exploratory (not confirmatory)**
- Early vs late 2026 desk rejections. Uses `modification_ms`, validated against the review calendar.
- Exit timing in 2025–26.
- Location-scale and high-variance-bet models are dropped.

**Expected figures and tables**
- **F4.1:** stage-gain ladder per feature (forest plot: desk, exit, decision, total).
- **F4.2:** published-only bias atlas (forest of accepted/all ratios), with bars splitting selection from editing.
- **F4.3:** Kobak bounds by year, accepted vs all.
- **F4.4:** arrows from cross-sectional to within-author coefficients for withdrawal (H4d).
- **T4.1:** continuation-ratio models.
- **T4.2:** audit flip matrices and tipping points.

**Falsification**
- H4a fails if the pooled NAME G_total 90% CI falls outside [0.90, 1.11], or the pool-specific break ORs differ at p < .05.
- H4b fails if the L-union G_total ≥ 1.
- H4c fails if the accepted-only bound is ≥ 0.9 × the all-submission bound in 2024 and 2025.
- H4d fails if the within-author coefficient is ≥ the cross-sectional coefficient.

---

## 3. Measurement validation plan

**V1. NAME, compound, orthography and casing detectors.**
- Sample 1,200 titles, stratified by year block (2017–19, 2020–22, 2023, 2024, 2025, 2026) × detector output (positive/negative) × orthography. Add 200 hard cases: two-token leads, LaTeX, dash compounds and genre leads.
- Two independent LLM annotation passes (Claude subagents) with different codebooks and prompts. Both are blind to year, outcome and detector output, and items are randomly ordered.
- Labels:
  - compound (y/n);
  - lead type: coined artefact name / descriptive phrase / genre label;
  - orthography;
  - casing class.
- Metrics: Cohen's κ (target ≥ 0.80). The PI adjudicates disagreements. 150 manual spot checks of agreed items estimate the consensus error.
- Outputs:
  - precision and recall per year block;
  - Rogan–Gladen-corrected yearly prevalence;
  - ITS rerun with year-specific misclassification.
- Pass criteria: the corrected slope-change OR is within 10% of the uncorrected one, and precision drifts by less than 5 pp across eras.

**V2. Slots.**
- 400 slot-filled titles, stratified by slot × variant × era.
- Annotators judge (a) whether the word is in the slot sense, and (b) whether swapping in the neutral variant preserves meaning.
- Variants with precision below 0.85 are dropped before the slot inventory is frozen.

**V3. Fingerprints and register.**
- Specificity: false-positive rates measured in 2021–22.
- Manual check of 100 U+2011 and en-dash hits to rule out LaTeX or PDF conversion artefacts.
- An LLM rates 300 abstracts (stratified by F status, 2024–26) for "LLM-polished" likelihood. The correlation is reported as weak convergent validity, not as ground truth.
- Recall is declared unknown, so all tool estimates are bounds.

**V4. Name-masking leakage.**
- The lead string must survive masking in 0% of NAME-paper abstracts.
- Report the masked-vs-unmasked AUC gap.
- Inspect the top-200 R1 features for name fragments.

**V5. Topics.**
- LLM labels for the 100 clusters, from the 20 most central abstracts each; 10 clusters checked manually.
- MiniLM vs bge clustering stability (ARI).
- Agreement between the LLM-cluster flag and the regex `llm_topic`.

**V6. Author keys and team types.**
- Distribution of papers per key. Flag keys with more than 40 papers in a year.
- Alias sensitivity (trailing digits).
- Contrast the email-key and profile-key eras.

**V7. Camera-ready audit validity.**
- Re-query a random validation subsample (150 accepted, 150 rejected) by first-author surname plus the first abstract sentence, not by title.
- Compare found rates and title stability by retrieval route.
- Report flip matrices with feature-present v1 denominators. For example, "using" appears in only n = 4 accepted v1 titles, so rare lexical features are declared unauditable.
- Enlarge the audit in the background to about 2,000 papers (about 1k papers/hour) before confirmation.

---

## 4. Confirmatory tests for the held-out ~20% split

**Procedure**
- Freeze the following, then hash the bundle (SHA-256), commit it and record the hash in `outputs/prereg/` **before** requesting held-out data:
  - code commit;
  - `lexicons.json`;
  - discovery-derived parameters: KMeans centroids (MiniLM, k = 100), R1 vectoriser and classifiers, DFL propensity models, fingerprint lists.
- Held-out handling:
  - Held-out papers get topics from the nearest discovery centroid.
  - Author history is computed on the union of discovery and held-out keys.
  - Each test runs once.
- Inference: tests are one-sided in the predicted direction. The family-wise α = 0.05 uses Holm over the 6 primary tests. Secondary tests use BH (q = 0.05).
- Verdicts:
  - **Confirmed:** adjusted p < .05 and the point estimate beyond the stated minimal effect.
  - **Contradicted:** the CI excludes the predicted region on the opposite side.
  - **Not confirmed:** otherwise.
- Expected held-out sizes are about a quarter of discovery per year: 2023 ≈ 970, 2024 ≈ 1,440, 2025 ≈ 2,240, 2026 ≈ 3,850.

**Primary tests**

1. **CT1 (D1 break).**
   - Test: ITS logit on held-out U (same specification as D1); test δ > 0.
   - Confirm if: Holm p < .05 and OR ≥ 1.10.
   - Expected z: ≈ 6.
2. **CT2 (D1 acceleration).**
   - Test: apply the frozen rolling R1 models to held-out year y, recalibrated to discovery obs_{y−1}, to get u_y. Test mean(u_2024–26) − mean(u_2019–23) > 0 with a paper bootstrap (stratified by year).
   - Confirm if: lower 95% bound > 0, ratio ≥ 1.5, and the upper 95% bound of content's share of the 2024–26 steps is < 0.60.
3. **CT3 (D2 communal).**
   - Test: last-position stayers are keys with an E-period paper (union) and a held-out L-period paper. The within-stayer share uses held-out L outcomes, with a key-cluster bootstrap.
   - Confirm if: lower 95% bound > 0.5.
4. **CT4 (D3 slots).**
   - Test: stacked slot + control logit on held-out data; test the `post × LLM-slot` interaction > 0.
   - Confirm if: Holm p < .05 and OR ratio ≥ 1.5.
   - Approximate power: 0.75 (discovery log-OR se 0.20 → held-out ≈ 0.41).
5. **CT5 (D4 neutrality).**
   - Test: held-out pooled 2024–26 NAME G_total, TOST.
   - Confirm if: the 90% CI lies inside [0.90, 1.11].
6. **CT6 (D4 depletion).**
   - Test: held-out pooled 2024–26 G_total and G_desk × G_exit for the L-union.
   - Confirm if: both are < 1 at one-sided p < .05 (Holm).

**Secondary tests**
- **CT7 (D3 vintage):** OR(F24 → R24)/OR(F26 → R24) > 1. Power ≈ 0.45; a null reads as "not confirmed", not "refuted".
- **CT8 (D3 turnover):** in held-out 2026 vs held-out 2025, R24 down and R26 up (two one-sided tests).
- **CT9 (D1 tool):** F = 0 rise / total rise, lower bound > 0.70.
- **CT10 (D4 Kobak):** accepted-only / all-submission bound < 0.90 in pooled 2024–26.
- **CT11 (D4 invariance):** pool-specific break log-ORs equivalent within ±0.1.
- **CT12 (D2 role gradient):** first-position minus last-position within share < 0.

**Gate.** No acceptance-margin result is called confirmed unless the audit tipping point exceeds the audit's upper CI. Diachronic and NA-pool tests do not depend on the audit.

---

## 5. Work packages

All code goes in `research/titles/src/analyses/`; all outputs in `research/titles/outputs/<folder>/`. Analyses are read-only on `data/` and `cache/`.

| WP | Files | Inputs → Outputs | Depends on | Parallel group |
|---|---|---|---|---|
| WP0 core | `_core.py` (universe and pools, crosswalk, controls, FE demeaning, cluster SEs, bootstraps, centroid assignment, plotting style) | data + cache → `outputs/core/universe.parquet`, `area_crosswalk.csv` | none | A |
| WP1 features v2 | `features_v2.py`, `lexicons.json` (NAME variants, slots, R24/R26, F24/F26, masks, control pairs, marker lists for D2) | universe → `outputs/features/features_v2.parquet`, `lexicon_hash.txt` | WP0 | A |
| WP2 topics/encoders | `topics_bge.py` (k50/k100 on bge; LLM-cluster flag), `embed_masked.py` (bge on name-masked abstracts, 2018–26, background) | cache → `outputs/topics/{topics_bge.parquet, emb_masked_bge.npy, centroids.npz}` | WP0 | A |
| WP3 validation | `annotate_sample.py` (stratified samples, codebooks), `validate_measures.py` (κ, precision/recall, Rogan–Gladen, V2–V6) | features, topics → `outputs/validation/` | WP1, WP2 | B |
| WP4 audit | `audit_v2.py` (route-randomised re-query, enlargement, background), `snapshot_bounds.py` (flip matrices, IPW, tipping points) | `cache/arxiv_audit.jsonl` → `outputs/snapshot/` | WP1 | A (network, background) |
| WP5 D1 | `d1_its.py`, `d1_content_cf.py` (R1–R6, fixed and rolling, new-topic placebo), `d1_decompose.py` (DFL, Shapley, tool bound) | WP1, WP2 → `outputs/d1_break/` | WP1, WP2 (R3 waits for `embed_masked`) | C |
| WP6 D2 | `d2_panel.py` (key-year panel, partitions, team types), `d2_shiftshare.py` (decomposition, IPW, bounds, removal simulation), `d2_markers.py` (H2d scatter), `d2_support.py` (S2.1 resubmissions, S2.2 future-tie) | universe, authors, features, topics → `outputs/d2_carriers/` | WP1, WP2 | C |
| WP7 D3 | `d3_slots.py`, `d3_register.py`, `d3_vintage.py`, `d3_signature_bound.py` | features, topics → `outputs/d3_register/` | WP1, WP3 (slot sense filter) | C |
| WP8 D4 | `d4_stage_gains.py`, `d4_bias_atlas.py`, `d4_exit_composition.py` | features, topics, snapshot → `outputs/d4_filter/` | WP1, WP2; decision-stage parts on WP4 | C |
| WP9 pre-registration | `prereg_confirm.py` (CT1–CT12 as pure functions; discovery dry run; freezes the bundle and hash) | all frozen parameters → `outputs/prereg/{prereg.md, bundle.sha256, dryrun.json}` | WP5–WP8 | D |
| WP10 figures | `figures.py` (F1.x–F4.x, T-tables) | all outputs → `outputs/figures/`, `outputs/tables/` | WP5–WP8 | D |

- **Critical path:** WP0 → WP1 → WP5–WP8 → WP9.
- Start WP2 `embed_masked` and the WP4 audit enlargement in the background immediately.
- WP5–WP8 are independent of each other and can run in parallel.

---

## 6. Directions considered but not locked (for future work)

- **C3 (selection paradox, high-variance bet):** the exit-composition part is absorbed into D4-H4d. The acceptance part sits inside the camera-ready flip band, and the location-scale model is identified only through functional form.
- **C4 (named at birth):** kept as supporting test S2.1. The pairs are selected on retitling because the export drops linked families, so a full analysis needs family data from the data owners.
- **C5 (snapshot gauntlet):** adopted as shared infrastructure (WP4 and the §4 gate), not as a finding.
- **C7-H4 and local-model generation:** positive-unlabelled class-prior estimation on 10-word strings is fragile, and CPU-only generation with small models does not resemble the tools authors actually use.
- **C8 (born branded, Zipf abbreviation):** the strongest NLP alternate. Its cohort effect rests on a few LLM/RL families and the within-concept effect is weak before 2024; this is a standalone short paper.
- **C9 (dilution and backgrounding):** dilution is near-obvious in a field that grew 40×. Backgrounding effects are small with T = 10. Usable as a framing paragraph.
- **C10 (constructionalization):** heuristic skeletons, few snowclones (79 "all you need"), and its fossilization result overlaps C11.
- **C11 (diversity illusion):** largely restates the NAME share. It needs to overturn a specific published homogenization claim and fits a methods box.
- **C12 (title informativeness):** the measures disagree in sign, effects are about 0.01–0.02 cosine, and small seq2seq probes partly measure their own limits.
- **C13 (namespace crowding):** an engaging ecology note, but the collision null depends on the character LM, and reuse is not influence.
- **C14 (exemplar cascades):** few lineages, confounded with topic booms, and the Berger–Le Mens coupling was already null.
- **C15 (contagion vs homophily):** kept only as placebo S2.2. Influence claims need verified person histories.
- **C16 (payoff-biased learning):** the camera-ready-free signal is null and the pilots disagree in sign.
- **C17 (trickle-down vs across):** status is internal to ICLR and confounded with resources, and the style sample is small.
- **C18 (crowding and distinctiveness):** density is confounded with genre and formulaic writing, and H4 fails the withdrawn-vs-rejected check.
- **C19 (momentum premium):** a clean deflationary null once team size and topic × year FE are added. Belongs in a robustness appendix.
- **C20 ("using" shibboleth):** the strongest single association, but the audit cannot bound it (n = 4 accepted v1 titles with "using"), it may proxy paper type, and it needs ethical framing.
- **C21 (claim strength across channels):** low power, out-of-domain NLI and certainty models, and too much annotation for the budget.
- **C22 (prescience of rejected papers):** reverse causation cannot be removed without citations, and titles are the weaker channel.

---

**Pilot checks run for this plan:**
- **Rolling content counterfactual:** unexplained drift 1.7 → 3.9 pp/yr; content share of the 2024–26 steps 0.42.
- **Pooled slots vs controls:** OR 2.69 [1.80, 4.01] vs 0.87 [0.64, 1.17].
- **Vintage alignment:** F24 → R24 OR 1.29 vs F26 → R24 OR 0.83.
- **Team-type definitions:** within-type share 0.94 (fixed window) and 0.99 (rolling); 0.77–0.87 within type × size; rolling all-prior teams .169 → .290.

Scripts are in /tmp/claude-0/-home-user-cloud-research/ac787a97-846c-54b7-93f0-8bd8a69ad531/scratchpad/design/pi/:
- rolling_cf.py
- rolling_cf2.py
- slot_power.py
- vintage_check.py
- team_defs.py