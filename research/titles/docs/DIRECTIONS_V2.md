# Directions v2: candidate research questions (for PI review)

Generated 2026-10-13 by an ideation workflow: 5 brainstormers (fashion theory, peer review, NLP language, author strategy, data opportunity) -> 30 raw ideas -> 12 merged candidates -> feasibility check on the real data (measures and counts only; outcome associations were not computed) -> 3 judges (meaningfulness, novelty vs literature, credibility). Scores are 1-10.

| ID | Candidate | Meaning | Novelty | Credibility | Mean |
|---|---|---|---|---|---|
| Q3 | B. Is review behind the curve? Pioneers vs dead ends | 8 | 6 | 7 | 7 |
| Q1 | A. Does a title name buy uptake? (title vs abstract-only name) | 6 | 7 | 5 | 6 |
| Q7 | Twin discoveries: is the idea judged, or are concurrent twins rationed? | 7 | 7 | 4 | 6 |
| Q4 | C. Riding the wave vs arriving late (and compensatory branding) | 5 | 6 | 6 | 5.67 |
| Q5 | Does a name still mean 'new'? Signal dilution of novelty claims | 6 | 6 | 5 | 5.67 |
| Q2 | A2. Stamp or spread: does rejection stop a named method from diffusing? | 7 | 5 | 4 | 5.33 |
| Q8 | Learning from review luck: superstitious style updating and conformity after rejection | 4 | 7 | 4 | 5 |
| Q9 | Amplifier or brake: does review feed research fashions? | 5 | 4 | 6 | 5 |
| Q10 | Is review worse at judging benchmarks than methods? | 5 | 6 | 4 | 5 |
| Q11 | Newcomers: style setters or content setters? | 5 | 5 | 4 | 4.67 |
| Q12 | Ossification: can a new name still break through? | 4 | 5 | 3 | 4 |
| Q6 | Does ML self-correct? Critique titles and the fashions they target | 4 | 4 | 3 | 3.67 |

## Q3. B. Is review behind the curve? Pioneers vs dead ends

- **Question.** Among equally novel submissions, were the papers whose neighbourhood the field later filled (pioneers) accepted, rejected or withdrawn at different rates from novel papers nobody followed (dead ends)?
- **Stake.** Bias against novelty (Boudreau et al. 2016; Wang et al. 2017) only costs the field if review turns away the novelty the field later follows. Citation studies conflate novelty (distance from the past) with prescience (closeness to the future); this design separates them, and it tests the belief that review cannot forecast impact.
- **Role of titles.** Title-term early adoption (first uses of title n-grams or keywords that later boom, such as 'in-context' or 'test-time') and forward similarity of the title embedding measure whether the label is ahead. The name-masked abstract measures whether the content is ahead. A secondary question is whether pioneers brand.
- **Design.** Papers from 2018-24 with a t+1..t+2 window; 2025 on t+1 as a sensitivity check. Novelty: distance to the 20 nearest t-2..t-1 papers. Prescience: the growth-normalised share of later vs earlier submissions within the paper's radius, on name-masked bge abstracts, excluding shared author keys, linked resubmissions and near-duplicates; also computed at region level (leave-one-out); z-scored within year x topic100. Estimands: (1) the slope of P(ACC) on prescience within novelty quartiles, i.e. whether review separates pioneers from dead ends; (2) a multinomial ACC/REJ/WD/DR model on the novelty x prescience 2x2; (3) the rejected or withdrawn share of the top-5% prescient papers vs base rates. Visibility checks: REJ vs WD, t+1 vs t+2, prescience from later REJ/WD papers only, last-author key x year FE (2022+), and pioneers of keywords that took off vs fizzled.
- **Headline if yes.** Review is blind at the frontier: among the most novel submissions, those the field later followed were accepted no more often than dead ends, despite acceptance's visibility boost, and 1 in N pioneers of later fashions was turned away.
- **Headline if no.** Review sees the future: among equally novel papers, those the field later followed were accepted X pp more often than dead ends, so the novelty penalty falls mostly on dead ends.
- **Contribution to CS.** The first citation-free test of reviewer foresight on a complete ML submission pool. It separates novelty from prescience, bounds visibility feedback with uncertified contrasts, and leaves reusable growth-normalised prescience metrics.
- **Reader benefit.** PCs and ACs learn whether frontier work needs a different track, such as high-variance acceptance slots. Authors of unconventional work learn whether a rejection signals a dead end or noise.
- **Closest prior work.** Kelly, Papanikolaou, Seru & Taddy 2021; Boudreau et al. 2016; Wang, Veugelers & Stephan 2017; Teplitskiy et al. 2022; Huang 2026; Xu et al. 2026; project pilot C22.
- **Main threats.** Pilot C22 already found that, on average, accepted abstracts are more forward-similar (OR 1.32) and less backward-similar (0.80), so the unconditional 'behind the curve' claim likely fails; the stake rests on the comparison conditional on novelty. Acceptance attracts followers, which biases toward 'review sees the future', so a null among novel papers is conservative. Field growth inflates forward similarity. Embeddings capture topic rather than idea (ARI 0.42; replicate with MiniLM). Prescience overlaps with hot-topic membership.
- **Feasibility (7/10).** I built the exposures for every focal paper from 2018 to 2025. The script is at /tmp/claude-0/-home-user-cloud-research/ac787a97-846c-54b7-93f0-8bd8a69ad531/scratchpad/feas/q3_measures.py and runs in about 55 s.

**Main sample: focal years 2018-2024, t+1..t+2 window, N=18,733**
- Pools: ACC 5,820, REJ 9,177, WD 3,572, DR 93, OTHER 71.
- By year: 2018 769, 2019 1,248, 2020 2,070, 2021 2,360, 2022 2,649, 2023 3,872, 2024 5,765.
- Sensitivity sample, 2025 with t+1 only: 8,953 (ACC 2,904, REJ 3,674, WD 2,322, DR 53).

**Pool sizes (backward / forward)**
- 2018: 384 / 3,318
- 2021: 3,318 / 6,521
- 2024: 6,521 / 24,365
- 2025: 9,637 / 15,412

**2x2 cells (main sample)**
- Top novelty quartile: 4,683 papers. A median split on prescience within that quartile gives about 2,340 per cell.
- Because the two exposures are correlated, a global median split gives an unbalanced top quartile: 3,354 high-prescience vs 1,329 low.
- Top 5% prescient papers: 956 in total, 375 of them in the top novelty quartile.
- 19.9% of the top novelty quartile have a 'NAME: subtitle' title.

**Exclusions**
- Forward pairs dropped as near-duplicates (abstract cos > .95): 3 to 267 per year.
- Forward pairs dropped as linked resubmissions: 5 to 253 per year.
- Self-following is large. Share of focal papers with at least one shared-author-key paper in the forward window: 2018 70%, 2019 67%, 2021 79%, 2023 88%, 2024 91%, 2025 86%.

**Title-term early adoption (secondary channel)**
- Terms that boom (≤15 uses in year t, ≥40 uses and a 5x share increase by t+2): 1 term in 2018, 1 in 2019, 3 in 2020, 3 in 2021, 13 in 2022, 27 in 2023, 35 in 2024.
- That is only about 310 early-adopter uses over 2018-24. They are dominated by the LLM wave ('large language', 'in-context', 'agents', 'preference', 'diffusion models') and by style words such as 'enhancing'.
- This channel is too thin and too confounded to carry the study. Keep it as a descriptive add-on.
- **Feasibility issues.** None of these is fatal, but four are serious.

1. **Reverse causation cannot be identified, only bounded.** Acceptance gives a paper visibility, and visible papers get followed. A positive prescience slope is therefore ambiguous. Only the "blind at the frontier" null or negative result can be read cleanly, and the headline must say this.
2. **The exposures are partly mechanically linked.** Prescience correlates with novelty (r = 0.27), and the radius artifacts showed up in the spot checks (about 1-2 of 7 pioneers). Conditioning on novelty quartiles alone is insufficient.
3. **Top-novelty "dead ends" often look like outsider, off-scope or dated-niche submissions** (face detection, sentiment analysis, CNN pooling). The novelty-penalty interpretation can be confounded by poor fit with the venue.
4. **Measure plumbing needs work before the study runs:**
   - Self-follow exclusion fails across the 2020/21 author-key break (0.6% key overlap). It needs a name-based fallback.
   - topic100 is fitted on future years, so it cannot serve as the conditioning set. Backward-only clusters are needed.
   - 55% of the variance in prescience is topic-level, so the study must report both components: picking the booming topic, and being first within a topic.

The title channel (early adoption of booming terms) is too thin to be a primary measure. Titles can enter via title-embedding forward similarity and as a secondary question on whether pioneers brand.
- **Identification plan.** **Design**
- Units: focal papers 2018-24 with a t+1..t+2 window; 2025 with t+1 only as a sensitivity check.
- Exposures:
  - Novelty: backward 20-NN distance.
  - Prescience: growth-normalised forward density inside the paper's backward radius, computed on name-masked bge.
  - Exclusions: shared authors (keys plus name strings), linked resubmissions, near-duplicates.
  - Replications: MiniLM, and a fixed-k combined-pool variant.
  - Region-level leave-one-out version: growth of the paper's backward 20-NN neighbourhood, excluding the paper itself.
- Estimand 1: an LPM or logit of ACC on prescience z, interacted with novelty deciles. Fixed effects are year × backward-only cluster, with controls for team size, author experience (2022+), name_primary and abstract length. The key contrast is the prescience slope in the top novelty quartile (or decile).
- Estimand 2: a multinomial ACC/REJ/WD/DR model on the novelty × prescience 2x2.
- Estimand 3: decision shares of the top-5% prescient papers against year-weighted base rates.
- Report both components: the across-topic one ("picked the booming topic") and the within-cluster one ("first within a topic"), since they answer different questions.

**Confounders and how to handle them**
1. **Reverse causation.** Acceptance makes a paper visible and attracts followers, which inflates "review sees the future". It cannot be removed without citations; it can only be bounded:
   - prescience computed from later REJ/WD/DR papers only;
   - t+1 against t+2 (the visibility effect should grow);
   - REJ against WD, a contrast between two public, uncertified pools;
   - a null among novel papers is conservative, so frame the study around the asymmetric "blind at the frontier" claim.
2. **Mechanical novelty-prescience link.** Sparse regions have large radii and the field diffuses into them. Handle it with flexible novelty conditioning, the fixed-k variant, and a radius cap or a fixed-radius sensitivity check.
3. **Novelty measures off-centredness.** High novelty partly marks outsider or off-scope submissions. Control for author experience and outsider status, for primary_area (2024+), and for backward-cluster FE. Add the last-author key × year FE (2022+) as a robustness check.
4. **Prestige and big labs.** They drive both acceptance and following. Use the within-last-author FE (2022+) and the team-size and prior-acceptance controls.
5. **Self-following.** Shared-author papers are 70-91% present in the forward window. Excluding them is mandatory, and the 2020/21 key break needs the name-based fallback.
6. **topic100 is future-fitted.** Use backward-only clusters instead.
7. **Field growth and composition.** Use the growth normalisation and within-year z, and add a check without 2026 for the 2024 focal year.
- **Judge, meaning (8).** Both outcomes would change minds: 'blind at the frontier' (novel work the field later followed was accepted no more often than dead ends) or 'the novelty penalty falls on dead ends'. It is the only design that separates novelty from prescience on a complete pool, and the visibility bias pushes toward 'sees the future', so a null is conservative and credible.
- **Judge, novelty (6).** The core claim is largely pre-empted: Huang (2026, arXiv:2607.05401) already shows on ICLR 2017-25 that review scores are orthogonal to later disruptiveness and that accepted and rejected papers do not differ on it, and Arts, Melluso & Veugelers (2024/25) and Kelly et al. (2021) already supply text-based novelty and uptake measures; what survives as new is the conditional pioneer-vs-dead-end test (does review separate novel work the field later follows from novel work it ignores?) with withdrawals included and no citations, a sharper test of bias against novelty than Wang et al. (2017) or Boudreau et al. (2016).
- **Judge, credibility (7).** The measures are already built for 18.7k papers (2018-24 with a full t+2 window), and power is adequate (about 2 pp per SD); reverse causation from acceptance visibility can only be bounded, but it biases toward 'review sees the future', so a 'blind at the frontier' null is conservative; the remaining fixes (name-based self-exclusion, backward-only clusters, flexible novelty conditioning) are plumbing, not identification failures.

## Q1. A. Does a title name buy uptake? (title vs abstract-only name)

- **Question.** When a paper coins a method name, do other teams use that name more in later ICLR submissions if it sits in the title rather than only in the abstract, at equal uptake of the underlying content?
- **Stake.** Is naming cheap talk or a working attention strategy (Abrahamson's rhetoric of fashion, Merton on eponymy)? We showed names buy nothing at review (OR 1.00), so this asks whether they buy anything with readers, which is where branding is supposed to pay.
- **Role of titles.** Treatment: the coined name is the 'NAME:' title lead (name_primary, lead_raw), compared with a fresh coinage left in the abstract. The name string is also the tracer searched for in later titles and abstracts.
- **Design.** Sample: first-attested coinages from 2018-24, i.e. no earlier ICLR use, after a dictionary and generic-acronym filter, with 300-400 matches hand-checked. That gives about 3.4k title leads, 5-10k abstract-only coinages, and about 1.6k papers that coin both. Outcome: t+1..t+2 submissions mentioning the exact token, per 1,000 later submissions, excluding any paper sharing a declared author key and any later re-coining; modelled with NB/Poisson plus an any-uptake LPM. Primary model is a within-paper Poisson with paper FE (title token vs the same paper's abstract-only token). The between-paper model adds topic100 x year FE, name-masked forward content similarity, team size, author history and orthography, with Oster bounds. Moderators: cohort NAME share (Red Queen), newcomer teams, method vs benchmark.
- **Headline if yes.** Other teams pick up a name in the title X times more often than the same paper's abstract-only name. Branding fails with reviewers but works with readers.
- **Headline if no.** Names travel only as far as their ideas: title placement adds no uptake, so the naming boom is cheap talk with reviewers and readers alike.
- **Contribution to CS.** A label-uptake measure that needs no citations, excludes self-mentions and covers every submission. A within-paper design that removes the paper-quality confound behind title-citation studies.
- **Reader benefit.** Authors learn whether a title name buys adoption, given that it buys no acceptance. Meta-scientists get a reusable uptake metric for OpenReview venues that lack citation data.
- **Closest prior work.** Peng, Qiu, Fosse & Uzzi 2024 (PNAS); Kuhn, Perc & Helbing 2014; Barnett & Doubleday 2020; Sato et al. 2022 (twin papers); Heard et al. 2023; Kelly et al. 2021; project pilot C13.
- **Main threats.** Authors put their main contribution in the title; the within-paper design and the content-uptake control address this only partly. The outcome is sparse: pre-checks give 8-21% external uptake depending on filters, so these must be harmonised first. Homonyms and generic acronyms. Benchmarks are mentioned when used. Abstract-only, ICLR-only mentions undercount uptake. 2025-26 coinages are right-censored.
- **Feasibility (5/10).** All counts are on the discovery split. Coinages are first-attested in 2018-24 (no earlier ICLR title or abstract use).
- Title-lead coinages (name_primary, single-token lead): 3,457. Of these, 178 (5%) had earlier ICLR use, leaving 3,279. After removing dictionary words, same-year co-use and capitalised plain words: 2,917. Restricting to distinctive names (5 or more characters, mixed case, all caps or containing digits): 2,463.
- Abstract-only coinages, with a strict proposal or naming cue ('we propose/introduce X', 'called/dubbed X', '(X)' after a proposal verb) and not a variant of the title lead: 4,480 first-attested, 4,009 clean, 2,097 distinctive. Of the distinctive ones, 1,950 are in papers with no title name.
- Within-paper set (papers coining both): 502 with loose extraction, 176 with strict extraction (only 17 in 2018-20), 90 distinctive. The candidate's figure of about 1.6k does not hold.
- Recommended symmetric between-paper sample (main-method name defined with a proposal cue in the abstract in both arms, distinctive): T 1,428 vs A 1,406, 2,834 papers in total.
  - By year: 2018 66, 2019 109, 2020 229, 2021 279, 2022 370, 2023 649, 2024 1,132.
  - By pool (T/A): ACC 473/466, REJ 632/655, WD 312/280, DR 5/2.
  - 88.5% of observations fall in year x topic100 cells that contain both arms (311 of 493 cells).
- Outcome, pooled across arms and not split by treatment. Definition: a later submission at t+1..t+2 mentions the exact token in its title or abstract; authors sharing a key or a normalised declared name are excluded, and re-coinings are excluded.
  - Symmetric sample: any-uptake 4.6%, 130 events, 250 mentions. Overdispersed (var/mean 5.7); the top 10 names account for 36% of mentions.
  - Broader distinctive sample (4,560 names): 4.0%, 179 events.
  - Loose versions give 9.6-13.8%, but most of those matches are homonyms (see validity notes).
- Arm differences in the exposure-side measures (not outcomes):
  - Mixed-case: T 68% vs A 38%. Median length: 7 vs 5 characters.
  - Benchmark or dataset share: 14% vs 9.7%.
  - T names that also appear in the abstract: 81%. T names with a proposal cue: 58% (A: 72%).
- Covariates: the masked abstract embedding is available for 100% of the sample. exp_valid (author history) covers 73-75%.
- Author-key break: keys are email-based through 2020 and profile-based from 2021. Only 0.9% of 2020 keys reappear later, so key-only self-exclusion fails for 2019-20 coinages. Declared names are 99.7-100% present and fix this.
- **Feasibility issues.** The proposed primary design is not feasible.
- (a) Only 176 papers (strict extraction) or 90 (distinctive names) coin both a title name and a separate abstract-only name, not about 1.6k.
- (b) In those papers the abstract-only names are sub-modules, objectives, new datasets or variants of the title name. They are a different kind of entity, so the within-paper contrast does not remove the importance/quality confound it was meant to remove.
The fallback between-paper design is buildable and measures are valid after cleaning, but it has three weaknesses:
- It brings back the core selection confound (authors title-brand what they expect to spread), with no instrument.
- The cleaned outcome is sparse: 4-5% any-uptake, about 130-180 events.
- Measurement error differs sharply by arm unless names are restricted to distinctive ones and hand-validated per arm. Abstract-only names are mostly short ALL-CAPS initialisms; homonym precision was about 8% for abstract-arm matches vs about 83% for title-arm matches before cleaning, and about 58% vs about 100% after.
Self-exclusion must use declared names as well as keys, because of the 2020/2021 switch from email to profile keys.
The study can only deliver a bounded conditional association. It is credible mainly if the result is null or very large (RR above about 1.7).
- **Identification plan.** Drop the within-paper Poisson as the primary model: there are too few papers (90-176), and the second name is a different kind of entity.
Primary design: a between-paper comparison on the symmetric sample.
- Unit: a distinctive main-method name, first-attested at ICLR in 2018-24 and defined with a proposal cue in its own abstract.
- Treatment: the name is the 'NAME:' title lead, versus a name left only in the abstract of a paper with no title name. Both arms carry the name in the abstract, so the contrast is title placement on top of the abstract.
- Outcome: any external mention in t+1..t+2 (LPM and logit), plus mentions per 1,000 later submissions (NB with an exposure offset).
- Controls:
  - year FE; topic50 or llm_topic FE (topic100 x year FE would discard most of the ~130 events);
  - idea uptake: name-masked forward content similarity, i.e. k-NN cosine of the masked bge abstract to t+1..t+2 submissions by other authors;
  - name form: shape, length, digits, pronounceability;
  - a benchmark/dataset flag, used to stratify, since benchmarks spread through use;
  - pool (ACC/REJ/WD) as a stratifier, defensible because a title name has no acceptance effect (OR 1.00);
  - team size and author prior acceptances (2022+ subsample).
- Robustness:
  - Oster delta;
  - rejected and withdrawn papers only, where there is no camera-ready and less visibility;
  - a looser T arm without the proposal-cue requirement, because 42% of T names lack the cue;
  - harmonised t+1-only windows that add the 2025 cohort.
- Placebo: same-year mentions by other authors, which should not depend on title placement after controls.
Main confounders:
- Expected importance: authors put in the title the names they expect to spread. This is only partly absorbed by forward content similarity.
- Lab status and arXiv fame before ICLR. Author history is valid only from 2022; the timing evidence in metadata_provenance could flag arXiv-before-deadline papers.
- Brandability of the name itself.
- Differential homonym precision between arms.
The result should be reported as a bounded conditional association, not a causal title effect.
- **Judge, meaning (6).** It is the natural sequel to the null result at review (names buy nothing from reviewers, so do they buy readers?), and authors would act on the answer. But a 'yes' is confounded by authors putting in the title the names they expect to spread, so only a null or a very large effect would move beliefs.
- **Judge, novelty (7).** No one has measured whether a coined name spreads more when it sits in the title than in the abstract, using exact-name uptake that excludes the authors' own mentions, on a complete pool that includes rejected and withdrawn papers; the nearest work counts acronym reuse (Barnett & Doubleday 2020; Mandyam Rangarajan & Krishnan 2026, NeurIPS abstracts, ~89% rarely reused) or links acronym-named trials and promotional language to citations (Stanbrook et al. 2006, NEJM; Peng et al. 2024), but none isolates title placement or the uncertified pool. Points off because 'branding buys attention' has citation-based precedents and the within-paper design that would make it distinctive has collapsed.
- **Judge, credibility (5).** The within-paper design that was meant to remove the quality confound collapses (90-176 papers, and their second names are a different kind of entity); the fallback between-paper comparison has about 130 events, differential homonym precision by arm and no answer to 'authors title-brand what they expect to spread', so it gives only a bounded association that is interpretable if null or RR>1.7.

## Q7. Twin discoveries: is the idea judged, or are concurrent twins rationed?

- **Question.** When independent teams submit near-identical ideas to the same ICLR cycle, are their fates concordant (review judges the idea), independent (execution and noise), or rationed (one in, one out, despite the concurrent-work policy)?
- **Stake.** Reliability experiments hold the paper fixed and cannot separate the idea from its execution. Merton's multiple discoveries, ICLR's rule that concurrent work must not count against novelty, and zero-sum rationing within AC batches make opposite predictions for twins.
- **Role of titles.** Title similarity screens out dual submissions and retitled duplicates. Within discordant pairs, title packaging (NAME, hype, differentiation from the twin's title) is the tiebreak covariate with content held fixed, tested on REJ vs WD, which is free of camera-ready edits.
- **Design.** Twins are same-year mutual nearest neighbours on name-masked abstracts above a threshold set by blind labelling of 200 pairs. Pre-checks give about 4-9k pairs at cosine 0.92 or above and about 1k at 0.94 or above. Pairs share no author key, have title cosine below 0.95, and are not linked resubmissions. Estimand 1: the residual correlation of acceptance and withdrawal by similarity bin, against 0.80-0.85 'cousin' pairs and random pairs from the same topic. Placebo: twins in different primary areas (2024+, separate AC pools) vs the same area. Estimand 2: the same-cycle twin penalty vs matched singletons and vs papers whose twin came in the previous cycle. Estimand 3: a pair-FE conditional logit on discordant pairs, with title features and author history as predictors.
- **Headline if yes.** Same idea, opposite fates: near-identical independent submissions in the same area are rationed, and a same-cycle twin cuts acceptance odds by X% despite the concurrent-work policy.
- **Headline if no.** Review judges the idea: twins share their fate far more often than same-topic pairs (phi about X), and a same-cycle twin costs nothing. (A flat curve would instead mean that the same idea gets a coin-flip decision.)
- **Contribution to CS.** A natural experiment on review reliability that holds the idea fixed without re-reviewing anything. It is also the first test of whether ML venues honour their concurrent-work policy.
- **Reader benefit.** Authors learn how much of their outcome comes from the idea vs execution or luck, and whether being scooped within a cycle costs them. PCs get a cheap, repeatable reliability monitor and evidence on AC batching.
- **Closest prior work.** Cortes & Lawrence 2021; Beygelzimer et al. 2023; Merton 1961; Sato et al. 2022 (Twin Papers); Stelmakh et al. 2021.
- **Main threats.** Affinity matching likely sends twins to shared reviewers or ACs, which inflates concordance (the area placebo checks this). Embedding similarity is not the same idea, so validation is needed. Hidden same-lab pairs, since pre-2022 keys are emails. Twins concentrate in 2025-26 LLM topics. A twin may withdraw after seeing its rival's reviews.
- **Feasibility (5/10).** Masked bge embeddings cover 2018-26 only (43,098 papers; 2017 has none). Same-year mutual nearest-neighbour (MNN) pairs on masked abstracts: 7,019 in total; 3,965 at cosine >=0.90, 1,853 at >=0.92, 461 at >=0.94, 20 at >=0.96. The pre-check figure of '4-9k pairs at 0.92' does not hold once mutuality is required: there are 1.9k.

Filters at >=0.92: 183 pairs share an author key, 262 share a fuzzy author name (initial plus surname, which catches about 40% more than keys alone), 19 have title cosine >=0.95, and 83 include a desk-rejected paper.

CLEAN pairs (no shared key or name, title cosine <0.95), with the count that excludes DR/OTHER in brackets:
- >=0.90: 3,446 [3,306]
- >=0.92: 1,577 [1,509]
- >=0.94: 372 [361]

By year at >=0.92: 2018 5, 2019 18, 2020 38, 2021 32, 2022 44, 2023 61, 2024 172, 2025 363, 2026 844. At >=0.94: 2018-23 25 in total, 2024 25, 2025 80, 2026 242. So 2026 alone is 54-65% of pairs. The LLM-topic share is 58% at 0.92 and 76% at 0.94. 2022+ (exp_valid) makes up 1,417/1,509 and 348/361 pairs.

Area placebo cells (2024+, by area_h): same area 694 vs different area 685 at 0.92; 171 vs 176 at 0.94. The split is roughly 50/50, so the placebo is usable.

Distinctiveness margin (s1-s2 >=0.03) at >=0.90: 300 pairs, 174 of them also at >=0.92.

Previous-cycle twins (nearest neighbour in year-1 with no shared key, not a linked resubmission): 3,471 papers at >=0.92 and 555 at >=0.94, of which 371 are in 2026. Name filtering has not yet been applied to these.

Marginals used only for planning discordance: the 2018+ ACC/REJ/WD shares are 0.306/0.458/0.236. Expected acceptance-discordant pairs under independence: about 42%, i.e. about 150 pairs at 0.94 and about 640 at 0.92.

Median nearest-neighbour cosine drifts upward by year (0.867 in 2018 to 0.901 in 2026), so a fixed threshold over-selects late, dense LLM years.
- **Feasibility issues.** None is strictly fatal, but four are serious:

1. **The twin measure is not ready.** bge-small masked cosine detects shared problems, not identical ideas: precision is about 50% at >=0.94 and about 10% at 0.92-0.94. The '4-9k pairs' pre-check collapses to 361 strict clean pairs, roughly 180 true twins. The study needs labels on about 3.4k candidate pairs, and there is no LLM API key in the environment.
2. **Exposure is measured after the outcome.** The single final metadata snapshot gives accepted papers camera-ready abstracts, so twin detection can depend on the decision. No pre-review text exists at scale; only about 331 arXiv v1 abstracts are available.
3. **The mechanism cannot be identified.** Without reviewer or AC IDs, shared-reviewer agreement and AC rationing push concordance in opposite directions within the same area, and the area placebo only gives their net. A 'rationed' headline therefore cannot be cleanly claimed, and the 'despite the concurrent-work policy' framing outruns the data.
4. **The sample is concentrated.** 2026 plus LLM topics hold about 60-75% of twins, and the title-tiebreak arm (estimand 3) is underpowered.

Of the three estimands, estimand 1 is the most defensible: it reports where twins fall on the T > P > N concordance gradient, as a reliability result in which the idea is held fixed.
- **Identification plan.** 1. Candidates. Take same-year MNN pairs on name-masked bge abstracts. Use year-specific percentile thresholds instead of a fixed cosine, because nearest-neighbour similarity drifts upward. Add a distinctiveness margin (s1-s2) to recover twins in niche topics. Exclude pairs with any shared key or fuzzy name, title cosine >=0.95, linked resubmissions, and DR/OTHER members.

2. Labels. Label all ~3.4k pairs at >=0.90 as T / P / N, using an LLM judge with a human audit of 200 stratified pairs and reporting kappa. The core test is a gradient of fate concordance across T > P > N > random same-year same-topic100 pairs > random same-year pairs. This gradient is more informative than any single threshold.

3. Estimand 1 (concordance). First model each paper's outcome (3-way ACC/REJ/WD, plus binary ACC) on year x area/topic100 FE, author history (2022+), log authors and genre (benchmark vs method vs theory). Then compute the residual pair correlation (phi), or the log odds ratio of the pair's joint outcome, against the product of predicted marginals. Main confounders:
   - (a) topic-level acceptance heterogeneity, handled by residualising and by the same-topic comparator;
   - (b) shared reviewers or ACs through affinity matching, which inflates concordance;
   - (c) AC-batch rationing, which deflates it;
   - (d) hidden same-lab pairs, which inflate it;
   - (e) camera-ready revision, which makes detection depend on the outcome;
   - (f) strategic withdrawal after the rival's public ICLR reviews.
   The 2024+ same-area vs different-area contrast (about 50/50) identifies only the NET of (b) and (c). There are no reviewer or AC IDs, so 'rationing' and 'shared-reviewer agreement' cannot be separated. Different-area twins also differ in genre (D&B vs methods), so match on genre.

4. Estimand 2 (twin penalty). Regress the outcome on 'has a same-cycle T twin' within year x topic100 FE, with flexible controls for local crowding (similarity to the 2nd through 10th neighbours). The comparison is then a paper with an unusually close rival vs one equally embedded in a crowd. Contrast this with having a previous-cycle twin (scooped, not concurrent; about 555-3.5k papers before name filtering).

5. Estimand 3 (tiebreak). Run a pair-FE conditional logit on outcome-discordant T pairs, with NAME, hype words and title distance to the twin as predictors. Run REJ vs WD separately, because that comparison is free of camera-ready titles.

6. Sensitivity checks: exclude 2026; exclude the LLM topic; restrict to the arXiv-dated subset for concurrency.
- **Judge, meaning (7).** Comparing fates along the twin > same-problem > same-topic ladder holds the idea fixed. That extends the famous NeurIPS consistency experiments in a way ML readers care about, and either answer (review judges the idea, or a coin flip for the same idea) informs authors and PCs. It loses points because the rationing mechanism cannot be identified and the twin labels need heavy validation.
- **Judge, novelty (7).** Idea twins are an established tool (Bikard 2020, used for citations and the Matthew effect; Hill & Stein on scooping), and review-consistency experiments hold the paper fixed (NeurIPS 2014 and 2021), but no study holds the idea fixed across independent same-cycle submissions to test review concordance or whether venues honour their concurrent-work policy; that combination is genuinely new.
- **Judge, credibility (4).** bge cosine detects shared problems, not identical ideas (about 50% precision at 0.94 or above, 10% below), so 3.4k pairs need labelling and there is no LLM key; exposure is measured after the outcome (camera-ready abstracts), and without reviewer or AC IDs rationing cannot be separated from shared-reviewer agreement, so the headline outruns the data.

## Q4. C. Riding the wave vs arriving late (and compensatory branding)

- **Question.** Holding topic, year and lab fixed, are papers that enter a research wave late accepted less often than early entrants, and do late followers compensate with more title branding and hype?
- **Stake.** A first-mover or novelty premium (Newman 2009; Xu et al. 2026) vs 'the bandwagon is safe' (Fujimura's doable problems). For rhetoric, Abrahamson & Fairchild (the upswing is the most emotional, so early) vs Simmel's distinctiveness (latecomers must differentiate). This decides whether the naming boom is compensation for crowding or a field-wide shift in style.
- **Role of titles.** Outcomes are title packaging: NAME, orthography, R24/R26 hype words and promotional templates. Title n-grams and keywords give a second lifecycle clock, checked against the masked-abstract clock.
- **Design.** Every 2019-26 paper gets a position with no lookahead in name-masked embedding space: prior neighbourhood volume, field-normalised growth from t-2 to t-1, neighbourhood age, and same-cycle crowding. The ex-post adoption percentile is descriptive only. Identification comes from three sources: topics at different stages in the same year (topic and year FE), the same last-author key with early and late entries (2022+), and the same paper (about 500 resubmissions whose abstract lands in a more crowded t+1 field). Outcomes: multinomial ACC/REJ/WD, and P(NAME, hype) by position. The payoff of compensation is tested only on WD vs REJ, which is free of camera-ready edits.
- **Headline if yes.** Arriving late costs X pp of acceptance, even for the same paper resubmitted into a more crowded field. Latecomers brand Y pp more without closing the gap: in crowded topics a coined name stands in for novelty.
- **Headline if no.** Review is neutral to timing and latecomers do not over-brand: riding the wave neither pays nor costs, and the naming boom is a field-wide style shift, not a response to crowding.
- **Contribution to CS.** Paper-level lifecycle estimates on a complete pool with no lookahead, linking topic timing to both review outcomes and rhetoric. The within-lab and within-paper designs are what topic-level studies such as Xu et al. 2026 lack.
- **Reader benefit.** PhD students and PIs learn what joining a hot topic late costs. Reviewers learn whether heavy branding in crowded topics flags lateness rather than novelty.
- **Closest prior work.** Xu, Dai, Yang & Zhang 2026; Newman 2009; Fujimura 1988; Abrahamson & Fairchild 1999; Berger & Le Mens 2009; Sjögårde & Didegah 2022; project pilots C18 and C19; finding 5.
- **Main threats.** Pilot C18 found that density predicts NAME (+1.4 to +2.4 pp per SD), and pilot C19 found that the momentum acceptance premium vanishes once team size and topic x year FE are added. The new contribution must therefore be the gradient within topic, lab and paper, not the level (which overlaps finding 5). In a 40x field, stage moves with calendar time, so stages must overlap within years. Late entrants are newcomers in smaller teams. Neighbourhoods are only moderately stable. The resubmission design has a minimum detectable effect of about 10 pp.
- **Feasibility (6/10).** Clock universe: 2019-26 papers with name-masked bge embeddings, n=42,329 (ACC 12,636, REJ 18,913, WD 9,897, DR 883). Per year: 2019 1,248; 2020 2,070; 2021 2,360; 2022 2,649; 2023 3,872; 2024 5,765; 2025 8,953; 2026 15,412. The growth measure needs t-2, so it covers 2020+ (41,081).

Exposures (radius cos >= 0.85; random-pair cos has p50 0.70 and p99 0.83):
- The median paper has 7 neighbours in t-1 (p75 21) and 11 in the same cycle.
- Field-normalised prior volume (share of the t-1 field within the radius) has R2 of only 0.013 on year and 0.39 on topic100_bge x year. 78% of its SD is left within topic x year, so stages overlap within years.
- Growth (t-2 to t-1) keeps 85% of its SD within topic x year.
- Stage cells, using within-year medians and no lookahead (non-DR ACC/REJ/WD):
  - early (low prior volume, rising this cycle): 10,658 (3,292 ACC)
  - upswing (high prior, rising): 9,124 (3,070 ACC)
  - late (high prior, flat or declining): 10,553 (3,148 ACC)
  - low/flat: 8,066
  - isolated (no neighbours in t-1 or t): 3,045
- Cell shares are roughly flat across years (early 22-28% every year).

Within-lab design (last-author key, 2022-26, non-DR):
- 35,789 papers across 14,792 keys.
- 5,624 keys have >= 2 papers (26,620 papers).
- 3,447 keys vary in ACC (20,875 papers) and 3,155 vary in NAME.
- Within-author SD of the volume z-score is 0.785 (pooled 0.997).

Within-paper design:
- 669 linked resubmission pairs fall in the clock window (610 one year apart).
- 541 are clean (previous version not accepted, masked cos >= 0.85). Their next pool is REJ 265, ACC 137, WD 132, DR 7.
- Previous-to-next NAME switches: 50 adds and 49 drops.
- SD of the within-pair change in the volume z-score is 0.68.

Outcome prevalence (no association computed):
- NAME: 13.1% (2019) to 40.5% (2026).
- R24 hype words: 0.6% to 6.3% (2025), then 4.8% (2026).
- R26: 1.1% to 4.6%.

Keyword clock: keyword coverage is 84-100% by year. The keyword prior-share clock is available for 40,810 papers.
- **Feasibility issues.** No single issue is fatal, but three things must be fixed or the headline is not credible:
(1) Construct validity of 'early':
   - Without lookahead, the low-prior-volume tail is mostly isolated niche or applied work, not wave pioneers (9 of 10 spot checks fit the expected pattern only when early is defined as low prior plus high same-cycle emergence, with isolated papers split off).
   - 'Arriving early' rests on same-cycle emergence, which is contemporaneous with review.
(2) Novelty overlap:
   - The prior-volume level is about 0.9 correlated with local density, so a 'late = crowded' result just restates C18 and finding 5.
   - Under C19, the level-acceptance link is already null once team size and topic x year FE are added.
   - The new contribution must be the growth/emergence gradient within topic x year and within lab. Its MDE (about 1.5-2 pp per SD) may be too coarse if the true gradient is small.
(3) Mechanical artefacts must be removed before any outcome is examined:
   - Absolute-threshold measures move with pool size (the isolated share falls from 20% to 3%), so they need rarefaction.
   - Own and lab prior versions sit inside every resubmission's radius, so author-overlapping priors must be excluded.
   - Age is left-censored, so drop or bound it.

The headline phrase 'even for the same paper' is supportable only with the fixed-text resubmission design, and that design can detect only effects of about 10 pp or more.
- **Identification plan.** Exposure (no lookahead, rarefied, own-author priors excluded):
- Two dimensions per paper: field-normalised prior volume (share of the t-1 field within radius, z-scored within year) and emergence (same-cycle share over t-1 share).
- Main contrast: late (high prior, flat or declining) vs upswing (high prior, rising) vs early (low prior, rising). Isolated papers are a separate category.
- Report the growth gradient conditional on the level, because the level alone is the C18/finding-5 density.
- The ex-post adoption percentile is descriptive only.

Designs:
1. Cross-topic, same year: multinomial ACC/REJ/WD (or LPMs on ACC and on WD|not ACC), with topic100_bge x year FE, log team size and llm_topic. Add experience controls in 2022+. Cluster SEs by topic.
2. Within-lab: last-author key FE, 2022-26 (3,447 keys with ACC variation), plus year FE and topic FE.
3. Within-paper, text held fixed: take the previous-version abstract embedding and compute its position against the t field and against the t+1 field. The change in position is then pure field movement, not author revision. Regress the next outcome on that change, conditional on the previous decision (541 clean pairs).

Compensation outcomes:
- P(NAME), orthography, R24/R26 and promotional templates as functions of position under the same FE.
- Whether branding pays is tested only on WD vs REJ among not-accepted papers (free of camera-ready edits).

Key confounders and fixes:
(a) Density, genre and formulaic writing: control local kNN density, genre markers and the abstract style density, or residualise the level and identify off growth or emergence.
(b) Team size and status sort into hot topics: C19 showed the momentum premium vanishes under them, so control experience and use the lab FE.
(c) Calendar time: within-year z-scores, rarefaction and year FE. Stages are roughly flat across years, so this is manageable.
(d) Self and lab contamination: exclude author-overlapping priors.
(e) Neighbourhood instability: report thresholds of 0.85 and 0.88, MiniLM vs bge, and the topic-level clock (topic100 share growth).
(f) LLM-era break: run 2019-23 and 2024-26 separately, plus a non-LLM subset.

Pre-specify the definition of the gradient before outcomes are touched.
- **Judge, meaning (5).** The practical stake for students choosing topics is real. But the acceptance gradient is largely anticipated by C19 (a null under controls) and by finding 5, and 'early' is poorly measured, so a reader is unlikely to update much either way.
- **Judge, novelty (6).** Early-vs-late entry and acceptance is partly covered at topic level (Xu et al. 2026; Newman 2009 used citations; Prabhakaran et al. 2016 linked rhetorical framing to topic lifecycle stage), but a paper-level, no-lookahead, within-lab test of whether late entrants compensate with branding (Abrahamson & Fairchild vs Simmel) is untested in the literature; its novelty against our own C18 and finding 5 is weaker.
- **Judge, credibility (6).** A large N with three nested designs (topic x year FE, last-author FE on 3.4k keys, fixed-text resubmissions) and no lookahead makes the design defensible, but 'early' is mostly niche or isolation unless it is redefined via same-cycle emergence, the level measure duplicates density/finding 5, and C19 already showed the acceptance premium dies under controls, so the credible new result is a gradient whose MDE is about 1.5-2 pp per SD.

## Q5. Does a name still mean 'new'? Signal dilution of novelty claims

- **Question.** Do papers that claim novelty, through a coined title name or 'novel', 'the first' or 'new paradigm' in the abstract, have measurably more novel content than comparable papers, and did that signal fade as the claims became common?
- **Stake.** Signalling theory: a separating vs a pooling equilibrium, or Simmel's differentiation without difference. Peng et al. 2024 say promotional language marks innovative work, and hype-inflation studies assume such language loses meaning but never measure it. The answer also supplies a mechanism for our null acceptance payoff.
- **Role of titles.** The NAME title is the main claim tested, with templates as secondary claims. Novelty of the title with the name stripped gives a second, title-level novelty measure.
- **Design.** Novelty with no lookahead: 1 minus the mean cosine of the name-masked bge abstract to its 20 nearest t-2..t-1 papers, plus Uzzi-style keyword-pair atypicality, a MiniLM replication and 300 hand-rated pairs. Arms: title-branded, abstract-only coinage (the comparator matched on genre) and no coinage, plus the abstract claims. Estimand: the standardised novelty gap within year x topic100, with team and author controls, for each claim x year. Dilution: the gap regressed on claim prevalence across claim x year cells with claim FE, so variation across claims, not calendar time, identifies it. F_any is a moderator.
- **Headline if yes.** Claims stopped meaning 'new': in 2018 a coined-name title marked +X SD of measured novelty, at 41% prevalence it marks about zero, and 'novel' follows the same dilution curve.
- **Headline if no.** Claims stay honest: even after a fourfold rise, branded and 'novel' papers remain measurably more novel than comparable papers.
- **Contribution to CS.** Measures the information value of promotional language in ML, and whether it erodes as it spreads, on a complete pool. A quantitative CS test of Peng et al.
- **Reader benefit.** Reviewers and readers learn how much 'NAME:' or 'novel' should weigh when they triage papers. Authors learn whether such claims still set their work apart.
- **Closest prior work.** Peng, Qiu, Fosse & Uzzi 2024; Millar, Batalo & Budgell 2022; Vinkers et al. 2015; Uzzi et al. 2013; Shibayama et al. 2021; Veitch, Sridhar & Blei 2020; Heard et al. 2023.
- **Main threats.** Embedding distance is not novelty of the idea: off-topic or poorly written abstracts look novel. Genre confound, since method papers brand. Prevalence moves with the year. LLM polishing shifts embeddings. Keywords are chosen by authors.
- **Feasibility (6/10).** Novelty is computable for 2019-2026 (masked bge exists for 2018-26 but not 2017, so 2018 has no masked t-2..t-1 reference set). Query n per year: 2019 1,248 ... 2026 15,412 (41,329 papers, 2019-26).
Title NAME (exposure) by year: 2018 77, 2019 164, 2020 325, 2021 355, 2022 486, 2023 786, 2024 1,534, 2025 2,965, 2026 6,236.
Refined arms, all years: title_name 12,962; abstract-only coinage 11,570; no coinage 18,950.
- Abstract-only coinage = a CamelCase/ALLCAPS token whose first corpus appearance is in this year and which follows a propose/introduce/called/dubbed cue.
- By pool: NAME ACC 3,904 / REJ 5,246 / WD 3,448 / DR 354; abstract-only ACC 3,510 / REJ 5,031 / WD 2,774 / DR 224; none ACC 5,634 / REJ 9,208 / WD 3,732 / DR 305.
Abstract claims, refined, n per year 2017 to 2026:
- novel_claim ('novel', excluding domain uses such as novel view/class/task, about 2% of hits): 54, 158, 263, 454, 553, 593, 942, 1,730, 3,089, 4,175. Share 14% -> 34.5% (2025) -> 27%.
- first_claim ('we are the first', 'for the first time', 'the first method/work/...'): 20, 28, 41, 89, 144, 127, 263, 334, 565, 1,160. Share 3-7.5%.
- paradigm/groundbreaking/pioneering/unprecedented: 2-364 per year.
- Templates are tiny: all_you_need 0-24 per year, rethinking 1-141, revisiting 1-64, towards 9-433.
Year x topic100 cells:
- 782 cells in 2019+; 696 contain both NAME and non-NAME papers (98.8% of papers).
- 523 cells have n >= 20 (39,967 papers), but only 19 of them in 2019 and 38 in 2020.
- Local NAME prevalence p10-p90 within year: 2019 0.05-0.23, 2026 0.14-0.59. Residual SD of cell prevalence after year and topic FE is 0.075.
Keywords: 40,917 distinct free-text keywords, only 912 used 20 or more times. Only 38-50% of papers have even one keyword pair seen in an earlier year (2019+).
- **Feasibility issues.** Nothing is strictly fatal, but several design elements fail as proposed:
(1) Construct validity. kNN embedding distance mainly detects off-scope or peripheral papers in its upper tail (application or poorly fitting work, 54% REJ and 29% WD in the top 1%), not new ideas. Without a validation (hand or LLM-rated pairs, which the pipeline does not have) or a forward-uptake variant, a null or negative gap is ambiguous: 'claimers are less peripheral' is not 'claims are dishonest'.
(2) The stored masked embeddings carry a differential [NAME]-token bias of about 0.12 SD against NAME papers. The whole corpus must be re-embedded with deletion (about 1.5-2 h) before any gap is credible.
(3) The raw kNN measure trends mechanically with reference size; fix it with fixed-size references.
(4) Uzzi keyword atypicality is infeasible: 40.9k free-text keywords, only 912 used 20+ times, and under 50% of papers have any previously seen pair. Drop it or replace it with concept clusters.
(5) The proposed claim x year dilution panel with claim FE is underpowered (templates are too sparse) and effectively identified by NAME's calendar trend. Replace it with the topic x year local-prevalence design.
(6) The 2018 baseline in the headline is not estimable (no masked 2017 references, n = 77). Use 2019-20 as the early baseline.
- **Identification plan.** The estimand is descriptive signal value, which is the right one for signalling theory: how much does seeing the claim shift expected novelty? No causal claim is needed.
Primary novelty measure:
- bge abstract with both name and CamelCase tokens deleted (re-embed; do not use the [NAME]-token file).
- kNN k=20 against a fixed-size random reference set (1,100 papers from t-2..t-1, averaged over 20 draws), 2019-2026, z-scored within year.
- Drop withdrawal-note abstracts.
- Add an off-scope guard: winsorise at p1/p99 and report a version excluding papers in the bottom 2% of similarity to their own topic centroid.
Second measure, to separate 'new' from 'off-topic': a Kelly et al. (2021) style novelty-with-uptake score (low backward similarity and high forward similarity at t+1..t+2). This is defined only through 2024, and it overlaps candidate B.
Gaps:
- Arms: title NAME vs abstract-only coinage (the genre-matched comparator, 2019+) vs no coinage; also novel_claim and first_claim.
- Standardised gap within year x topic100_bge.
- Report two versions: (i) the raw within-topic gap, which is what a reader actually learns; (ii) the gap with controls for log_authors, llm_topic, abstract length, masked-token count, F_any, and author experience (exp_valid, 2022+ only).
Dilution:
- Primary design: topic x year cells. Regress the cell gap on local claim prevalence with year FE and topic FE, giving 523 cells with n >= 20 and residual prevalence SD 0.075. Prevalence then varies across topics within a year, not only with calendar time.
- Secondary: the per-year NAME gap trajectory (2019-20 pooled as the early baseline).
- Tertiary: the proposed claim x year panel with claim and year FE. It has only about 4-5 non-trivial claims (NAME, novel, first, abstract coinage, paradigm); templates are too sparse, so this panel is underpowered and identified mostly by NAME's own trend.
Main confounders:
(1) Genre (method vs analysis/benchmark papers): handled by the abstract-coinage comparator and a genre-word control.
(2) Composition drift: NAME spreads into new genres, which is arguably part of 'pooling', so report with and without genre adjustment.
(3) Measurement drift over time: fixed reference size, deletion masking, MiniLM replication.
(4) Off-scope papers inflating the novelty of non-claimers: off-scope guard and forward-similarity variant.
(5) LLM polishing: F_any is uncorrelated with novelty (-0.009), so use it as a moderator only.
- **Judge, meaning (6).** It is a clean signalling test (do claims separate or pool?) that would supply a mechanism for the null acceptance payoff, and 'claims stay honest' would surprise people. But many readers already expect dilution, and because embedding novelty mostly measures peripherality, either answer is open to reinterpretation.
- **Judge, novelty (6).** That promotional or novelty language tracks real novelty already has evidence in grants (Peng et al. 2024), patents (arXiv:2605.04926) and paper introductions (arXiv:2606.13452); the new parts are whether the signal dilutes as claims become common, and using a coined title name as the claim, which no study has measured.
- **Judge, credibility (5).** A descriptive signal-value estimand needs no causal identification and is powered from 2021 on, but the upper tail of kNN 'novelty' is off-scope or peripheral work (top 1% is 83% REJ/WD), the stored masked embeddings carry a 0.12 SD bias against NAME papers (a full re-embed is needed), the 2018 baseline is not estimable, and with no hand or LLM validation a null cannot be read as dishonest signalling.

## Q2. A2. Stamp or spread: does rejection stop a named method from diffusing?

- **Question.** Do coined methods from rejected or withdrawn ICLR submissions get taken up by other teams as often as comparable accepted ones?
- **Stake.** Does a top venue's accept decision still gate which methods spread (certification, a Matthew effect through acceptance)? Or, in an arXiv-first field, do ideas diffuse anyway, so that the decision is only a lagging label?
- **Role of titles.** The 'NAME:' title lead is the tracer. Title-derived lineages (X++, 'Beyond X') are a second channel. The subtitle identifies the name type (method vs benchmark).
- **Design.** Named papers from 2018-24 (t+2 window) and 2025 (t+1), using Q1's uptake outcome without self-mentions. Estimates: rate ratios REJ/ACC and WD/ACC within year x topic100, with masked-abstract PCs, local density, team, author history and name type; plus the share of all external uptake that comes from unaccepted papers. Contrasts that approach certification: REJ vs WD (both uncertified, both public during review), and an event study on rejected named papers later resubmitted and accepted (uptake before vs after acceptance). Forward content uptake serves as a check. Pilot C13, unadjusted: two-year external reuse of 16.1% ACC, 10.3% REJ, 9.4% WD.
- **Headline if yes.** Rejection barely slows ideas: other teams reuse comparable rejected methods at about X% of the accepted rate, and unaccepted papers supply Y% of all later name uptake.
- **Headline if no.** The accept stamp gates diffusion: comparable rejected methods are reused at a fraction of the accepted rate, and uptake jumps once a resubmission is accepted.
- **Contribution to CS.** The first estimate, on a complete pool and without citations, of how much a top ML venue's decision governs which methods spread. Uncertified-vs-uncertified and resubmission contrasts separate selection from certification.
- **Reader benefit.** Authors learn what a rejection costs their method's adoption, and whether withdrawing differs from staying public. PCs learn how much their decisions shape the field's toolset.
- **Closest prior work.** Wang, Veugelers & Stephan 2017; Elazar et al. 2024; Bharadhwaj et al. 2020 (arXiv posting and acceptance); Kuhn, Perc & Helbing 2014; Huang 2026; project pilot C13.
- **Main threats.** The ACC/REJ gap mixes quality selection with certification; only the REJ-vs-WD contrast and the resubmission event study come close to certification. Rejected papers are often published later at NeurIPS/ICML. The event-study sample is small. Mentions are rare and dominated by benchmarks. Homonyms. Shares Q1's pipeline and could run as Q1's second estimand.
- **Feasibility (5/10).** Tracers are single-token 'NAME:' leads (name_primary, lead_raw) that had no earlier ICLR use. Some 8.1% of single-token leads had appeared in ICLR text before and are dropped as not novel. Leads that are 3 characters or fewer and all caps are also dropped as homonym-prone (157). That leaves 5,757 tracers in 2018-25: ACC 1,900, REJ 2,380, WD 1,443, DR 26, OTHER 8.
By year (ACC/REJ/WD):
- 2018: 24/33/5
- 2019: 47/84/13
- 2020: 85/156/44
- 2021: 90/173/48
- 2022: 145/165/115
- 2023: 228/270/176
- 2024: 425/577/319
- 2025: 856/922/723 (t+1 window only)
The 2022-25 subset, where author history is valid (exp_valid), is ACC 1,654, REJ 1,934, WD 1,333. 2025 alone is 44% of tracers.
Name type, inferred from the subtitle: method 5,305, benchmark 576, tool 33. The benchmark share is similar across pools (ACC 10.3%, REJ 9.3%, WD 9.8%).
Outcome, pooled over all pools for power only (not tabulated by pool): any external mention in a later ICLR title or abstract within t+2 (t+1 for 2025). The base rate is 5.6% after the homonym filter (6.1% raw), which gives 321 positive names and 767 mentions. The count is extremely skewed: 0 mentions for 5,500 names, 1 for 269, 2 for 67. The top 1% of names carry 53% of all mentions. Benchmarks are taken up about 1.7x more than methods (10.9% vs 6.5%, pooled).
Event study: of 678 linked resubmissions, 108 have a named REJ/WD original, but only 37 keep the same name. Only 5 are REJ/WD->ACC with the name kept and at least one post-acceptance year. Only 12 are comparable REJ/WD->REJ/WD cases.
arXiv v1 dates from the audit cache cover just 439 tracers (ACC/REJ only, 2022-25).
- **Feasibility issues.** 1. The certification identification promised in the stake is not achievable with these data.
- There are no review scores, so no threshold regression discontinuity.
- The resubmission event study has only 5 named REJ/WD->ACC cases with the name kept and a post window (12 comparison cases).
- REJ vs WD is a quality and author-choice contrast between two uncertified pools, not a certification test.
So the 'stamp gates diffusion' result cannot be separated from quality selection. Only the 'rejection barely slows ideas' direction, a near-null gap, is interpretable, as an upper bound.

2. Diffusion is not ICLR-caused for the names that dominate uptake.
- The top 1% of names carry 53% of mentions.
- Hits are dominated by arXiv/GitHub-first industry artifacts (LoRA, SDXL, Qwen-VL, which was rejected in 2024, MetaGPT, OpenHands, GAIA).
- arXiv timing covers only 439 tracers, so this cannot be stratified at scale.

3. Low power for anything but large gaps.
- 321 positive names in total, and rate ratios of only about 0.65 or below are detectable.
- 44% of tracers are 2025 cohort with only a one-year window.

4. Measure quirks, not fatal:
- Raw matching runs about 25% homonyms. The strict filter cuts this to about 7%, but a hand check of 300 pairs is still needed.
- Exact-token matching misses derivative forms such as X-7B and X++.

Recommendation: do not run this as a standalone study. Fold it into Q1 as a secondary estimand, report the share of all uptake supplied by the non-accepted pool, and frame the result as a bound on certification.
- **Identification plan.** Recommended design: selection on observables, framed as bounding the effect.

Setup:
- Unit: one novel tracer name per paper.
- Outcome: any external uptake in t+1..t+2 (binary, primary). A Poisson count of mentions is secondary, also run with the top 1% of names winsorized or removed.
- Estimands: RR(REJ/ACC), RR(WD/ACC) and RR(WD/REJ).

Controls and fixed effects:
- Year FE.
- topic50, or topic100 by period. Full year x topic100 fixed effects leave about 800 cells for 321 positives, so most cells drop out of a conditional model.
- 10-20 PCs of the masked abstract embedding.
- Local density: count of earlier neighbours in the same year and topic.
- Name type (benchmark/method/tool), orthography and length.
- log team size.
- Author history (max prior subs/accs, share of new authors). These are valid only for 2022+, so the main sample is 2022-25 (n≈4,945) and the 2018-21 years are a sensitivity check.
- review_count, as a crude proxy for engagement.
- Also report the descriptive share of all external uptake that comes from non-accepted papers (fully feasible).

Main confounders:
1. Quality selection. Accepted papers are better, and there are no review scores, so a regression-discontinuity at the acceptance threshold is impossible.
2. Off-ICLR certification. Rejected papers are later published at NeurIPS/ICML/CVPR, which we cannot observe.
3. Diffusion that started before the decision. Industry models and benchmarks spread through arXiv and GitHub before review. arXiv dates exist for only 439 tracers, too few to stratify on.
4. Lab and status effects. Big-lab releases are disproportionately accepted, and author history is only a partial control.
5. Benchmark versus method mix.

The proposed certification contrasts do not hold up:
- REJ vs WD compares two uncertified groups that differ in quality and in author choice. It is a quality gradient, not a certification test.
- The resubmission event study has 5 treated cases and is infeasible.

The design is therefore informative in one direction only:
- If the adjusted REJ/ACC ratio is close to 1, that bounds certification as small. The 'rejection barely slows ideas' headline would be credible, because selection should inflate the gap, not shrink it.
- A large gap cannot be split into quality and certification. The 'stamp gates diffusion' headline is not identifiable.

Recommended framing: 'how much uptake does the ICLR non-accepted pool supply, and an upper bound on the acceptance premium'. Run this as Q1's second estimand on Q1's pipeline, not as a standalone study.
- **Judge, meaning (7).** It has a high stake (does a top venue's accept stamp still gate diffusion in an arXiv-first field?), and the surprising direction is the identifiable one: if rejection barely slows uptake, that is a credible upper bound, because quality selection should widen the gap. The share of all uptake that comes from non-accepted papers also extends finding 4. The 'stamp gates' direction cannot be interpreted.
- **Judge, novelty (5).** That rejected ML papers still diffuse is already documented with citations: rejected ICLR 2017-19 papers that became highly cited (Wang et al. 2021, 'What have we learned from OpenReview'), NeurIPS 2014 rejects (Cortes & Lawrence 2021), and editorial gatekeeping misses (Siler, Lee & Bero 2015); what is new is a citation-free name-uptake share from the withdrawn and rejected pool, a modest descriptive addition, since the certification estimand it promises cannot be identified.
- **Judge, credibility (4).** Certification is not identified (no scores, 5 resubmission event cases, REJ vs WD is a quality gradient), uptake is dominated by arXiv/GitHub-first industry artifacts, and the pilot's raw gap (0.64) sits at the MDE, so only a near-null result is interpretable; it is best kept as Q1's secondary estimand plus a descriptive 'share of uptake from non-accepted papers'.

## Q8. Learning from review luck: superstitious style updating and conformity after rejection

- **Question.** Do authors change how they title (and what they study) according to which of their own papers got accepted, even though title style carries no acceptance payoff?
- **Stake.** Superstitious learning from noisy outcomes (Levitt & March 1988; Denrell & March 2001) vs persistence; payoff-biased vs conformist transmission (Boyd & Richerson). This is also the learning channel assumed by 'peer review breeds conservatism' (Rzhetsky et al. 2015). If authors learn style from review luck, review noise itself drives writing fashion.
- **Role of titles.** Title style is the learned behaviour: NAME, colon, question titles, R24 words, templates, and distance to the centroid of accepted titles. Topic moves in the masked abstract are the benchmark, since there following success could be rational.
- **Design.** Mixed-portfolio design on 2022-26 profile keys: key-years with at least two decided papers in year t, one ACC and one REJ, that differ on a style feature (about 12.8k key-years have both outcomes). Outcome: the share of the key's new t+1 submissions that use the feature, excluding resubmissions and sequels (abstract cosine above 0.8 or a reused name). Estimand: style uptake when the styled paper won minus when it lost, with key x year FE absorbing baseline style and quality, stacked across features, with content switching as the rational benchmark. Secondary: after an all-reject year vs an all-accept year at matched content, do the next titles and topics move toward the accepted mainstream? Estimated as a DiD on the t-1 to t+1 trajectory.
- **Headline if yes.** Authors learn title style from review luck: when their named paper gets in and their unnamed one does not, they brand X pp more next year, even though names do not help acceptance.
- **Headline if no.** Review outcomes do not teach style: title habits are unmoved by which paper got in, so title fashion spreads socially, not by chasing reviewer reward.
- **Contribution to CS.** The first within-author test of whether ML researchers adapt how they write, and what they study, to peer-review outcomes. It shows whether review noise propagates into community norms.
- **Reader benefit.** Authors see whether 'this is what got my paper in' inferences are noise-chasing. PCs learn about a hidden cost of noisy review.
- **Closest prior work.** Denrell & March 2001; Levitt & March 1988; Boyd & Richerson 1985; Hengel 2022; Wang, Jones & Wang 2019; Rzhetsky et al. 2015; project pilot C16 (lose-shift +4.1 pp after withdrawal, weak win-stay, coding not harmonised).
- **Main threats.** Accepted projects spawn sequels that inherit their names. Keys are not persons (24% aliasing). Co-author teams differ between the two papers. Keys with mixed portfolios are prolific, senior authors. Camera-ready edits to accepted titles (the audit found no excess). Low power for rare features. Without review scores, rejection is not as-good-as-random.
- **Feasibility (5/10).** Profile-key author-rows by year: 2021 8.3k, 2022 11.0k, 2023 16.8k, 2024 27.8k, 2025 47.5k, 2026 87.4k. Before 2021 there are almost none, so the window is t = 2021-2025 and t+1 runs to 2026.

Key-years, t = 2021-25: 76,895 in total. 17,961 have at least 2 submissions. 7,489 have both an ACC and a REJ paper (by year: 604 / 695 / 1,106 / 1,855 / 3,229). Counting WD as a loss raises this to 9,787. The candidate's figure of about 12.8k is not reproduced.

Of the 7,489 mixed key-years, 5,514 have at least one new t+1 submission when resubmissions are cut at bge cosine > 0.9 plus name reuse. At the candidate's 0.8 cutoff only 4,303 do.

NAME-discordant mixed key-years with a new t+1 paper (0.9 cutoff): 2,723 differ on any share. 1,141 are clean (all ACC papers named and no REJ paper named, or the reverse): in 640 the named paper won, in 501 it lost. These cover 3,420 new t+1 papers. Portfolios and keys are about 0.89 distinct per key-year, because co-authors share the same paper pair.

Pooled outcome (NAME share of t+1 new papers, not split by treatment): mean 0.40, SD 0.38.

Clean discordant key-years with a next paper, by feature (0.8 cutoff): compound 1,015, gerund opener 929, NAME 880, any template 486, title case 285, R24 words 257, question 145, R26 words 125. The rare features have little power.

Keys that are first or last author on all of their decided t papers: only 171 of the clean NAME cells.

Secondary design: all-ACC key-years with both t-1 and t+1 submissions = 2,670; all-REJ = 2,685, of which about 2,000 have a single paper.
- **Feasibility issues.** None of these is fatal on its own, but together they are serious.
(1) The learner is misidentified. Keys are mostly middle or last-author hubs (first author on 10% of papers), and the ACC and REJ papers have largely different teams (median Jaccard 0.17). 'My named paper won' is diluted, and team continuity (the winning student keeps working with the group and brings their own style) can mimic win-stay without any learning.
(2) Topic following mechanically moves NAME rates, because names cluster by topic. A content-adjusted outcome is required.
(3) Power: the NAME-only MDE is about 5-7 pp against plausible effects of 2-4 pp, so the realistic deliverable is a bounded null.
(4) The premise is weaker than stated. Among decided papers within a key, the named paper won 56% of clean discordant cells, so authors are not obviously 'superstitious' from what they can see.
(5) The candidate's numbers need correcting: there are 7,489 mixed key-years, not 12.8k, and the 0.8 cosine resubmission filter is miscalibrated for bge-small (use 0.9).
(6) Heavy overlap with pilot C16, which was weak and had sign disagreements.
- **Identification plan.** Unit: a key-year t in 2021-25 with at least one ACC and one REJ paper. Treatment for feature f: D = (share of ACC papers with f) - (share of REJ papers with f). The primary sample is the clean +1/-1 cells; a continuous-D sensitivity uses all 2,723 discordant cells.

Outcome: share of the key's new t+1 submissions with f. Exclude resubmissions and sequels: bge cosine > 0.9 to any t paper, or in the resubmission link table, or a fuzzy name match.

Main specification: stack features with key x year FE and feature x year FE. Cluster by paper portfolio, ideally by connected components of shared t papers, because co-author keys are copies of the same experiment.

Key confounders and fixes:
(a) Topic following. If the named paper won in a CV or LLM topic, the author does more CV/LLM work at t+1, and those topics name more by default. Use a content-adjusted outcome: f minus a cross-fitted p(f | name-masked abstract embedding, year, area). Report the rational benchmark alongside: cos(t+1, ACC paper) - cos(t+1, REJ paper).
(b) Team continuity. Acceptance keeps the winning student in the group, and the student carries their own style. Control for each t+1 paper's co-author overlap with the ACC team vs the REJ team, and estimate on t+1 papers that include neither t-paper's first author.
(c) Quality and seniority differences between the two papers. Key x year FE handles key level. Add the named paper's topic, the LLM flag, and the n_keys of each paper.
(d) Who the learner is. Run heterogeneity by key role. First/last-only is too small (171 cells) to be primary.

Placebos:
- A lead test: the t-1 style of the key should not respond to t outcomes.
- REJ vs WD contrast.
- A feature reviewers cannot see but that is written at the same time, e.g. abstract typography (F_any), as a negative control.

Secondary (rejection to conformity): compare all-ACC and all-REJ key-years (about 2.7k each) on the t-1 to t+1 change in distance to the accepted-title centroid and to the topic centroid. Using t-1, not t, as the baseline avoids regression to the mean from the t draw. Trends in quality and seniority are still not identified, so this part is descriptive.

Timing works: ICLR t decisions (January) come before the t+1 deadline (September/October). Outcomes at NeurIPS and ICML in between are unobserved noise.
- **Judge, meaning (4).** Superstitious learning is an elegant theory link, but the learner is misidentified (keys are hubs; the two papers usually have different teams), the premise is weak (the named paper won 56% of the time), and the realistic result is a bounded null that adds little to finding 2.
- **Judge, novelty (7).** Learning from failure has been studied for grant resubmission trajectories (Yin et al. 2019) and career near-misses (Wang, Jones & Wang 2019), but whether authors superstitiously update writing style from noisy review outcomes, given that style has no payoff, appears to be untested anywhere; the novelty is high against the literature, though it overlaps our own pilot C16.
- **Judge, credibility (4).** Keys are mostly middle- or last-author hubs (first author on 10%), the ACC and REJ teams barely overlap (Jaccard 0.17), and team continuity mimics win-stay; topic following moves NAME mechanically, the 'superstitious' premise fails within portfolios (the named paper won 56% of cells), and the MDE of 5-7 pp against plausible effects of 2-4 pp gives at best a bounded null that overlaps C16.

## Q9. Amplifier or brake: does review feed research fashions?

- **Question.** When submissions to a research fashion surge, do ICLR acceptances rise more than proportionally (amplifier), proportionally (mirror) or less (brake), and do authors then move toward the fashions review just favoured?
- **Stake.** One complaint is that ML conferences fuel hype bandwagons; the opposite view is that review is conservative and damps fads. Theories of recognition-driven research cycles (Bramoullé & Saint-Paul 2010) and of informational cascades need a feedback loop from review to submissions that has never been measured on a complete pool.
- **Role of titles.** Fashions are defined from title terms and coined-name lineages (GAN, NeRF, diffusion, in-context, test-time, -R1, -Bench), with masked-abstract clusters as robustness. Comparing membership by title label with membership by abstract only tests whether review rewards the label beyond the content.
- **Design.** Cells are fashion x year, using title terms with at least 30 uses and topic100 masked clusters. The elasticity beta comes from a Poisson model, acc_kt = exp(beta log sub_kt + alpha_k + gamma_t). Split-sample counts avoid division bias. Beta is estimated separately for rising and falling phases, on decided papers and on the full pool. Feedback: the change in log share at t+1 regressed on the acceptance-rate residual at t, with fashion and year FE. Placebo: the residual at t+1 should not predict growth at t.
- **Headline if yes.** ICLR review amplifies fashions: a 10% surge in submissions brings a rise in acceptances of more than 10%, and next year's submissions flow toward the fashions review just favoured.
- **Headline if no.** Review is a mirror, not an engine: acceptances scale proportionally with surges and authors do not chase last year's acceptance rates, so bandwagons are driven by authors.
- **Contribution to CS.** A single, comparable elasticity for whether peer review amplifies research fashions, plus a test of the feedback loop from review to submissions, with withdrawals included.
- **Reader benefit.** PCs learn whether area-based AC allocation passes booms through unfiltered. Authors learn whether jumping into a surging topic raises or lowers their odds.
- **Closest prior work.** Xu et al. 2026; González-Márquez & Kobak 2024; Bramoullé & Saint-Paul 2010; Bikhchandani et al. 1992; Sjögårde & Didegah 2022.
- **Main threats.** Prior evidence points to a mirror: our NAME amplification test was null (editing-corrected 0.991), and pilot C19's momentum premium vanished under controls. Area quotas may force beta to about 1 by design. Boom entrants differ in composition. Few independent fashions and short series. Results are sensitive to how fashions are defined. Camera-ready edits affect cells defined by title terms.
- **Feasibility (6/10).** Universe without OTHER: 43,370 papers. Acceptance rate over all submissions by year: 2017 .43, 2018 .38, 2019 .33, 2020 .27, 2021 .29, 2022 .33, 2023 .32, 2024 .31, 2025 .32, 2026 .27. Over decided papers it is .32-.44.
(1) Title terms: 1,618 terms with at least 30 uses (518 with at least 100). Most are generic words (generation, adaptive, time, can, how), so 'at least 30 uses' does not define a fashion by itself. A curated set of 44 lineage regexes (gan, nas, meta-learning, few-shot, federated, contrastive, self-supervised, gnn, transformer, nerf, diffusion, flow matching, in-context, prompt, cot, lora, rlhf/dpo, test-time, -R1/GRPO, mamba, moe, rag, *Bench, llm-agent, etc.) tags 15,535 papers, 2,432 of them in 2 or more fashions. Coverage rises from 8% of submissions in 2017 to 43% in 2026, because the list was chosen with hindsight.
Fashion x year cells with at least 20 submissions: 140 cells across 38 fashions, 5,112 acceptances, median 19 acceptances per cell. 76 cells are in a rising phase and 63 in a falling phase (by change in log share). Only 21 fashions have any falling cell, and these are concentrated: gan 8, vae 6, adversarial 6, few-shot 5, gnn 5, equivariant 4, contrastive 4, others 1-3. Cells usable for the feedback regression (t up to 2025): 104, of which 50 have t up to 2023.
(2) topic100_bge clusters (masked-abstract centroids are also available): 923 cells, 511 with at least 20 submissions (248 rising, 260 falling). After removing cluster and year means, the SD of log submissions is 0.68 and the SD of the change in log share is 0.50. Feedback cells (t up to 2025): 417, of which 226 have t up to 2023.
(3) Title label vs abstract only: papers whose abstract uses the term but whose title does not, relative to title users: diffusion 0.42, federated 0.16, mamba 0.93, llm 1.13, gan 1.21, test-time 1.28, in-context 1.48, contrastive 1.66, lora 1.90. So the 'label beyond content' contrast has large groups.
Areas (2024+ only): 21 x 3 cells, smallest cell 32.
- **Feasibility issues.** None is strictly fatal, but four issues lower the value:
(1) Novelty overlap with in-house results already peeked. The feedback half is essentially C16 H1, which found success-biased growth post-2023 but a null on the camera-ready-free contrast. The amplification half generalises the NAME accepted/all ratio test (about 1.00, editing-corrected 0.991). So the likely headline, 'mirror', is close to known.
(2) Title-term cells for accepted papers are camera-ready text, which mechanically biases toward amplification. A positive beta on title cells would not be credible unless it replicates on masked-abstract clusters.
(3) Area-level AC calibration from 2024 may force beta toward 1 by design, so a mirror may reflect PC procedure rather than reviewer neutrality.
(4) Falling-phase evidence rests on about 6 old fashions (gan, vae, adversarial, few-shot, gnn, contrastive), mostly before 2024 with small cells. The 'brake on decline' estimate is thin.
Also: the stated placebo is miscoded, and split-sample counts do not address the actual bias, which is membership misclassification.
- **Identification plan.** Main estimand: a cell-level Poisson model (acceptances on log submissions, with fashion and year FE), equivalently a paper-level logit of acceptance on log fashion size with fashion and year FE. Outcome over all submissions as primary (withdrawals in the denominator), over decided papers as secondary. Run it on two fashion definitions that agree with each other: about 40 curated title lineages, and topic100 masked-abstract clusters. Weighted precision-trimmed cells (at least 20 submissions). Estimate rising and falling phases separately.
Key confounders and fixes:
(1) Composition of boom entrants: new and inexperienced authors and teams of different size enter booms, which pushes toward 'brake'. Add paper-level controls (log authors; max prior accepts and share of new authors, valid 2022+ only) and report the adjusted beta. The difference between raw and adjusted beta is itself informative (is it reviewers or entrants?).
(2) Area-level calibration (2024+): add area x year FE to test within area. If beta is about 1 by construction at area level, say so.
(3) Camera-ready contamination of title cells: use abstract-masked clusters as primary for accepted-paper membership. For title cells, use the withdrawn+rejected vs accepted audit (arXiv v1 pairs in outputs/audit) to bound how far term addition after the decision could move beta.
(4) Polysemy: restrict each fashion to years after its onset, or require the term in both title and abstract.
(5) Few independent fashions: cluster SEs by fashion, wild-cluster bootstrap for the curated set (38 clusters), leave-one-fashion-out.
Feedback loop: change in log share from t to t+1 on the acceptance-rate residual at t, with fashion and year FE plus lagged growth. Its problems:
(a) Nickell bias with T of about 8.
(b) A common cause: fashion promise drives both acceptance at t and growth at t+1. This is the reason in-house pilot C16 H1 found b=.076 post-2023 for title forms but a null on the camera-ready-free contrast.
(c) ICLR outcomes cannot be separated from NeurIPS/ICML outcomes in the same months.
(d) The proposed placebo is miscoded: the residual at t+1 vs growth t to t+1 shares the t+1 count. Use the residual at t+2 vs growth t to t+1, or a lead-lag event study.
The binomial noise in the residual attenuates the estimate. Correct it with split-half reliability of the residual: random halves of papers within each cell.
- **Judge, meaning (5).** It addresses the important 'do conferences fuel hype?' debate, but the likely answer ('mirror') is close to what we already know (NAME ratio 1.00, C16/C19), and area-level calibration may force a mirror by design, so a reader learns little either way.
- **Judge, novelty (4).** Topic-level acceptance differences and emerging-topic premia at ICLR are already described (González-Márquez & Kobak 2024; Xu et al. 2026, with topic acceptance spanning 18-46%), and our own NAME amplification test was null; the elasticity framing and feedback loop are new packaging of a largely known 'mirror' answer.
- **Judge, credibility (6).** It is cheap and quick to finish, and a pooled 'mirror' elasticity on masked-abstract clusters is well powered (MDE about 0.07-0.12); however, title-term cells are biased by camera-ready edits, 2024+ area calibration may force beta to 1, the falling-phase estimate rests on about 6 old fashions, and the feedback loop suffers Nickell bias and a common-cause confound, so only the cluster-based mirror headline survives.

## Q10. Is review worse at judging benchmarks than methods?

- **Question.** Is ICLR review less able to pick which benchmarks and datasets the field will adopt than which methods it will adopt?
- **Stake.** A widespread belief holds that ML venues undervalue and misjudge data and benchmark work (Sambasivan et al. 2021; Koch et al. 2021; Fujimura's bandwagons around transportable packages). That belief motivated the NeurIPS Datasets & Benchmarks track and ICLR's datasets & benchmarks area. Here it is tested against revealed adoption rather than opinion.
- **Role of titles.** Contribution type is read from the title (-Bench, Benchmark, Dataset, Arena, Gym, Suite) and validated against primary_area from 2024. The title name is the adoption tracer, since most benchmark titles are NAME titles.
- **Design.** Types are coded from titles and validated on 300 papers: about 1.9k benchmark or dataset papers, mostly from 2024-25. Adoption is measured by external name uptake (Q1's measure) and by growth of the masked forward neighbourhood. Within each type: the adoption ratio of accepted to rejected or withdrawn papers within topic100 x year, and the AUC of acceptance for predicting top-decile adoption. The main estimand is the type x decision interaction. Also: the share of the most-adopted benchmarks vs methods that were rejected or withdrawn. Influence ratios across genres are not estimated.
- **Headline if yes.** Review sorts methods but not benchmarks: rejected benchmarks are adopted about as often as accepted ones, while accepted methods are adopted X times more than rejected ones.
- **Headline if no.** Reviewers judge benchmarks as well as methods: the gradient from acceptance to adoption is the same for both.
- **Contribution to CS.** The first revealed-preference evidence on whether CS peer review misjudges infrastructure contributions, which directly informs the criteria for datasets and benchmarks tracks.
- **Reader benefit.** PCs learn whether benchmarks need separate criteria or reviewers. Benchmark authors learn whether a rejection predicts poor adoption or only reflects reviewer taste.
- **Closest prior work.** Sambasivan et al. 2021; Koch et al. 2021; Dehghani et al. 2021; Raji et al. 2021; Fujimura 1988; Huang 2026.
- **Main threats.** Benchmarks are mentioned when used and methods when compared, so mention rates are comparable only within a type. Power comes mainly from 2024-25, with short windows. Title-based typing misses some benchmarks. The interaction isolates review only if acceptance's visibility effect is the same for both types.
- **Feasibility (4/10).** TITLE-CODED BENCHMARK/DATASET PAPERS (coder B2: -Bench suffix, benchmark(ing), or constructive dataset/corpus/testbed/arena/gym/suite phrasing, with dataset-distillation and "on X datasets" excluded). All years 1,707. By year: 2017-23 together 137 (at most 49 in any one year), 2024 148, 2025 455, 2026 967. The 2026 papers (57% of the total) have no forward window, because 2026 is the last year in the data. So the candidate's "~1.9k, mostly 2024-25" is wrong: only 603 papers can be analysed.
ANALYSABLE 2024-25 BENCHMARKS: 603 (ACC 187, REJ 260, WD 152, DR 4).
WITH A USABLE TITLE-NAME TRACER: 380. A usable tracer is a distinctive single token or capitalised phrase that does not appear in any earlier submission and is unique within its year. Breakdown: 2024 80 (ACC 28, REJ 36, WD 15); 2025 300 (ACC 100, REJ 120, WD 79); in total ACC 128, REJ 156, WD 94.
METHOD COMPARATORS WITH A USABLE TRACER (2024-25): 3,305 (ACC 1,081, REJ 1,281, WD 924, DR 19).
BROADER CODER B3 (B2 plus an abstract "we introduce/release a benchmark/dataset" cue on named or "Evaluating..." titles): 698 tracers (ACC 249, REJ 263, WD 184). Its additions are low precision (see notes).
OUTCOME BASE RATE, POOLED OVER DECISIONS, USED ONLY AS A POWER INPUT. "Any external mention" means a later ICLR title or abstract mentions the name and shares no author ID or author name with the paper.
- Benchmarks: 12.5% in the 2024 cohort (2-year window); 8.7% in the 2025 cohort (1-year window, ICLR 2026 only). That is about 36 benchmark papers with any external mention in total.
- Methods: 6.7% and 3.5%, about 154 papers.
- Mentions are very concentrated. 5 benchmarks account for 71 of the 123 external benchmark mentions (SWE-bench 22, WebArena 20, AndroidWorld 12, OGBench 10, LVBench 7).
- Self-mentions, excluded from the outcome: 3-9% of papers.
PRE-2024: only 60 B2 benchmark papers with tracers (141 with B3), about 12-50 of them accepted, so negligible.
IDENTIFYING VARIATION: 579 of 698 B3 benchmark tracers sit in topic100 x year cells that contain both accepted and non-accepted benchmarks (70 cells); with topic50 the figure is 647.
Pool shares of benchmark tracers versus method tracers are similar (ACC 36% vs 32%, REJ 38% vs 39%, WD 26% vs 28%).
- **Feasibility issues.** Not strictly fatal, but four serious issues stack up.
(1) Power. Only 380-700 benchmark papers have both a forward window and a usable tracer (2024-25). They yield about 36-60 adoption events, dominated by 5 superstars (SWE-bench, WebArena, AndroidWorld, OGBench, LVBench). The interaction MDE is a ratio of ORs of about 2.5-3, so a null is uninformative. 57% of title-coded benchmarks are from 2026 and have no outcome window. The candidate's "~1.9k analysable" figure is wrong.
(2) The interaction cannot isolate reviewer judgement. Rejected ICLR benchmarks have a dedicated fast second venue (NeurIPS Datasets & Benchmarks, decided before the next ICLR deadline), and visibility effects of acceptance likely differ by type. Both push toward the 'review cannot sort benchmarks' headline with no misjudgement at all.
(3) The second proposed measure (masked forward-neighbourhood growth) is invalid for benchmarks. Their later neighbours are rival benchmarks and same-domain methods, not users. Drop it.
(4) The title coder is about 90% precise but only about 63% recall against area_db. Its misses sit in the high-uptake tail: MathVista, UltraFeedback and WildChat are coded as 'methods'. Every adopted tracer must be hand-coded.
Recommendation: do not run this as a standalone headline study. Fold it into Q1/A (branding to uptake) as a pre-registered heterogeneity test (benchmark vs method), plus a descriptive table of the decision status of the most-adopted benchmarks.
Scratch scripts: /tmp/claude-0/-home-user-cloud-research/ac787a97-846c-54b7-93f0-8bd8a69ad531/scratchpad/feas/q10/ (a_types.py, b_types.py, c_tracer.py, d_spot.py, e_more.py, f_b3.py; tracer.parquet holds the tracer table).
- **Identification plan.** Unit: 2024-25 papers with a first-attested, distinctive title-name tracer. The type is title-coded (B2), plus area_db for papers in that area that pass a hand check. Every tracer with at least 1 external mention is hand-coded as benchmark, method or mixed. Mixed papers are kept as a separate third type or dropped.
Outcome: any external later-ICLR mention (binary, the primary outcome, robust to the superstar tail). A secondary outcome is the count (negative binomial or Poisson with cluster-robust SEs), winsorised at p99. Mentions are excluded when the later paper shares an author ID or author name, or re-coins the same name.
Estimand: the ratio of odds ratios (accepted vs not accepted) between types. The model is a logit of uptake on type x pool with topic50 x year FE (topic100 is too sparse for benchmarks: about 8 per cell). Controls:
- tracer distinctiveness: shape, length, mixed/all-caps;
- log_authors, max_prior_accs and first/last-author prior accs (exp_valid holds for 2024-25);
- llm_topic;
- review_count (it is post-treatment, so only as a sensitivity check);
- window: a year dummy plus a year x type interaction, because 2025 has only a 1-year window.
Withdrawn papers are analysed separately from rejected ones, since withdrawals are often a strategic exit to another venue. Descriptive companion: the decision status of the top-k most-adopted benchmarks and methods (k = 10/20). It is reported as a case table, not a test.
MAIN CONFOUNDERS
(1) Post-decision afterlife differs by type. A benchmark rejected at ICLR has a dedicated, quick second venue: the NeurIPS Datasets & Benchmarks track, which decides around September, before the next ICLR deadline. So "rejected at ICLR" benchmarks are often published elsewhere within months. That mechanically flattens the benchmark gradient and produces the 'yes' headline without any reviewer misjudgement.
- Mitigation: none available inside our data. We can only bound it by restricting to mentions in the y+1 submission round, or by flagging resubmissions (cache/resubmissions only covers ICLR to ICLR).
(2) Acceptance causes visibility: the venue stamp and the ICLR proceedings. The interaction isolates review only if this effect is the same for both types, which is unlikely (benchmarks spread via leaderboards and HuggingFace regardless of venue).
(3) Lab prominence and release infrastructure (SWE-bench from Princeton, WebArena from CMU) drive both acceptance and uptake. Author prior-acceptance controls only partly absorb this.
(4) Outcome scales differ by type (mentioned when used vs mentioned when compared). Comparisons must stay within type, so we compare ratios of ORs and never levels.
(5) Type misclassification is concentrated in the tail; hand-coding is required.
(6) Truncation: the 2025 cohort has a single round of later submissions.
CREDIBLE DESIGN
At best a conditional association: a within-type, within-topic-year 'review-adoption gradient' compared across types. It cannot separate reviewer misjudgement from afterlife and visibility channels. The honest framing is 'predictive validity of ICLR decisions for later in-venue uptake, by contribution type'.
- **Judge, meaning (5).** It bears directly on the policy behind Datasets & Benchmarks tracks, so it has a real stake. But with about 36-60 events a null is uninformative, and the fast second venue (NeurIPS D&B) produces a 'yes' even without any reviewer misjudgement.
- **Judge, novelty (6).** The belief that review undervalues benchmarks is widespread (Sambasivan et al. 2021; Koch et al. 2021; NeurIPS track rationale), and I found no revealed-preference test linking decisions to later adoption by contribution type, so the question is novel; it is held at 6 because the comparison is confounded by NeurIPS D&B as a fast second venue, which caps how new the answer can be.
- **Judge, credibility (4).** Only 380-700 benchmarks have both a window and a tracer (about 36-60 events, 5 superstars hold 58% of mentions), so the interaction MDE is a ratio of ORs of about 2.5-3; the NeurIPS D&B afterlife and type-specific visibility mechanically produce the 'yes' headline, and the coder misses the high-uptake tail, so it works only as a heterogeneity cut inside Q1.

## Q11. Newcomers: style setters or content setters?

- **Question.** Do first-time ICLR teams write the content the field later converges on, or do they only set its packaging? And does review discount prescient work when it comes from newcomers?
- **Stake.** The Planck principle and outsider innovation (Azoulay et al. 2019; Shi & Evans 2023) vs incumbent advantage (the Matthew effect). It extends our finding that title style spreads through new people while returning authors keep pace on topics.
- **Role of titles.** Title style leadership, i.e. adopting a marker while it is below 25% of its later prevalence, is the packaging channel. It is measured on the same scale as content prescience.
- **Design.** Cohorts 2022-24 with valid profile keys (about 12k papers); 2025 on a t+1 window. Team status: all-new, mixed or incumbent keys (fixed two-year lookback), and new vs returning last author. Outcomes on a symmetric early-adopter scale: content lead (Q3's prescience, or early use of a concept keyword) vs style lead. Estimand: the newcomer-incumbent gap in content lead vs the gap in style lead within topic100 x year, split by LLM vs non-LLM topics. Then acceptance on prescience x newcomer.
- **Headline if yes.** Newcomers lead ML in substance, not just packaging: first-time teams are X% more likely to write what the field converges on, yet their prescient papers are accepted Y pp less often than incumbents' equally prescient work.
- **Headline if no.** Newcomers bring the packaging, incumbents bring the ideas: first-time teams lead title style but not content.
- **Contribution to CS.** Separates the style and substance channels of research fashion on one scale and tests the Planck and outsider-innovation hypotheses in the fastest-growing CS field without citations. It adds a fairness check of double-blind review for newcomers' foresight.
- **Reader benefit.** Field leaders and PCs learn whether ML's flood of newcomers brings ideas or only branding, and whether review treats newcomers' foresight fairly. Newcomers learn where their comparative advantage lies.
- **Closest prior work.** Azoulay, Fons-Rosen & Graff Zivin 2019; Shi & Evans 2023; Movva et al. 2024; Sun et al. 2022; project finding D2.
- **Main threats.** Keys are not persons (aliasing changes 24% of new-key shares). New to ICLR is not new to ML. Newcomers cluster in hot topics. Only three full cohorts. Depends on Q3's prescience measure.
- **Feasibility (5/10).** TEAM STATUS (profile keys from d2_carriers/panel_rows.parquet, fixed two-year lookback y-1/y-2, any role). all_new / mixed / all_prior: 2022 987 / 1,479 / 183 (n 2,649), 2023 1,004 / 2,478 / 384 (3,872), 2024 1,404 / 3,837 / 524 (5,765), 2025 1,808 / 6,328 / 817 (8,953), 2026 3,085 / 10,953 / 1,373 (no t+1). Last-position key new: 47.6% (2022), 37.2%, 37.4%, 33.7%. The 2022 cohort is NOT usable. Its lookback window runs over 2020-21, and 2020 has zero profile keys (all email) while 2021 has only 65% fully-profiled papers. That is why all_new is 37% in 2022 against 26% in 2023. Cohorts with a valid lookback are 2023-25 (18,590 papers: all_new 4,216, mixed 12,643, all_prior 1,725), not 2022-24 (~12k) as proposed. Pools 2023-25 by team: ACC 839/4,474/625, REJ 2,064/5,218/762, WD 1,263/2,907/327, DR 50/44/11 (all_new/mixed/all_prior). Decided ACC+REJ 2023-25 is about 14.0k, with 2,903 of them all_new. Under trailing-digit aliasing, all_new drops from 25.9% to 21.7% (2023) and from 20.2% to 15.6% (2025). All_new share is 25.7% in non-LLM topics vs 14.8% in LLM topics (2023-25).
LEAD MEASURES AS SPECIFIED (binary, 'below 25% of later prevalence', H=2): too sparse. Style lead: 25 papers (2022, 3 markers: bridg/enhanc/guided), 41 (2023, enhanc/comprehensive), 0 in 2024, 0 in 2025. At a 50% threshold: 44 / 104 / 268 / 203. Content lead (keywords with ≥30 later uses and ≥0.3% later share): 32 / 104 / 78 / 27 papers. At 50%: 94 / 375 / 457 / 162. Crossed with a 20-25% newcomer share, that leaves fewer than about 100 newcomer leaders per channel.
CONTINUOUS SYMMETRIC VERSIONS (built): each paper gets the mean over the items it carries of log(prev_{y+1}/prev_{y-1}). Coverage: style 2,490 / 4,115 / 6,857 papers carry a style marker in 2023/24/25 (64-77%; SD 0.23-0.25); content 2,773 / 4,956 / 7,891 carry a keyword with ≥10 uses in y-1 plus y+1 (72-88%; SD 0.64-0.95). Forward-minus-backward abstract similarity (bge, k=20 nearest neighbours in random 2,000-paper pools for t+1 and t-1, z-scored within year x topic100) is defined for all 2022-25 papers. The raw fb SD is about 0.013-0.018. Topic100 x year cells (2023-25): 299 cells, median 56, min 1.
- **Feasibility issues.** The study is not fatal as a whole, but the design as specified fails on four points and must be changed. (1) The 2022 cohort has an invalid lookback (2020 has no profile keys), so the usable cohorts are 2023-25, not 2022-24. (2) The binary '<25% of later prevalence' early-adopter scale is far too sparse: style 25 / 41 / 0 / 0 papers per year 2022-25, content 32-104. A continuous symmetric growth score or forward-similarity score is required. (3) The style channel in this window is essentially NAME plus LLM-assisted words. The NAME newcomer premium is already estimated in D2, and the remaining markers are tool artifacts, so the 'style vs substance on one scale' contrast mostly re-tests D2 on the style side. (4) Forward similarity is contaminated by same-key follow-ups and resubmissions (about 21% of papers have one in their top-20 t+1 neighbours), and it cannot separate prescience from status-driven imitation (Matthew). Key exclusion is mandatory, and the headline must say 'lead' rather than 'prescience'. 'New to ICLR' cannot be separated from 'new to ML', which limits the Planck and outsider framing. The review-discount half is powered only for large interaction effects.
- **Identification plan.** Units: 2023-25 submissions (2025 on a t+1 window; all cohorts on a fixed t+1 horizon for symmetry). Exposure: team status under the fixed two-year lookback (all_new / mixed / all_prior), plus new vs returning last key. As sensitivities: the alias-collapsed key, and a rolling all-prior-ICLR definition (2021+). Outcomes, on one scale: (a) content lead = z-scored forward-minus-backward abstract (and title) similarity within year x topic100, with all t+1 papers that share a key with the focal paper removed (also resubmission pairs from cache/resubmissions.parquet); (b) content_g = growth of the paper's keywords, after synonym merging; (c) style_g = growth of its title markers, reported with and without NAME and without the LLM-assisted words. The binary 25% early-adopter rule is too sparse and should be dropped or kept only as a descriptive appendix. Estimand: the gap (all_new minus incumbent) in standardized content lead minus the gap in standardized style lead. Estimate it as a stacked paper x channel regression with topic100 x year FE, controls for team size bin, LLM topic and area_h (2024+), and SEs clustered by topic100 and last key. Split by LLM vs non-LLM topics. Review stage: P(accept), with withdrawals counted as not accepted plus a decided-only sensitivity, on content-lead z x newcomer with topic100 x year FE. Present it as a moderation, never as a level gap. Main confounders: (1) 'new to ICLR' is not 'new to ML'; NLP and CV migrants look like newcomers, and no external data exist to fix this, so bound it with the rolling-history definition and a 'last key has ≥1 prior ICLR acceptance' contrast; (2) topic sorting, since newcomers are under-represented in LLM topics, handled by within-cell FE; (3) the Matthew-effect reverse channel, where incumbents' papers are imitated because of status, so forward similarity measures influence and not only prescience; keyword-growth content_g is less exposed to this and serves as a co-primary; (4) self-continuation, removed by key exclusion; (5) key aliasing (about 20% relative shift in all_new share), run on both key and alias; (6) LLM-tool use driving the non-NAME style markers.
- **Judge, meaning (5).** The Planck/outsider framing and the check on double-blind fairness are meaningful. But the style half re-tests D2, and the content 'lead' cannot separate prescience from status-driven imitation, which blunts both headlines.
- **Judge, novelty (5).** Outsider and Planck-principle effects are established (Azoulay et al. 2019; Shi & Evans 2023), and newcomer flows in ML (Movva et al. 2024) and newcomer shares at CS conferences are documented; putting style and substance on one scale is a new twist, but the style half mostly re-tests our own finding D2.
- **Judge, credibility (4).** The 2022 cohort is invalid because of the key break and the binary early-adopter scale is empty (0 style leaders in 2024-25); the style channel is NAME plus LLM words, which re-tests D2, forward similarity cannot separate prescience from Matthew-style imitation, and the main gap is only borderline powered.

## Q12. Ossification: can a new name still break through?

- **Question.** As ICLR grew 40x and 'NAME:' titles rose from 9% to 41%, did a newly coined name's chance of uptake by unrelated authors fall? If so, is the cause field size (attention concentrating on a canon) or name saturation (a branding arms race)?
- **Stake.** Chu & Evans (2021, PNAS) argue that large fields slow canonical progress because attention concentrates on established work. The rival account is a Red Queen, where branding loses value once everyone brands. The answer shows whether ML's growth is ossifying attention.
- **Role of titles.** Units are names coined in titles, with abstract-only names as the comparison. A topic's density of NAME titles is the Red Queen predictor. Later mentions in titles and abstracts measure attention.
- **Design.** Names coined 2018-24, with Q1's sense filter and uptake measure free of self-mentions. A breakthrough is at least k external mentions per 1,000 later submissions, with later pools rarefied to equal size. Canon concentration per year: the share of all name mentions going to names at least 3 years old and to the top 1%, the Gini of mentions, and the median age of mentioned names. Mechanism: breakthrough regressed on log topic x cohort size and that cell's NAME density (about 100 topics x 7 cohorts), with cohort and topic FE.
- **Headline if yes.** A new ML name's chance of catching on fell by X% as ICLR grew, while mentions concentrated on an ageing canon. Field size, not branding saturation, accounts for it.
- **Headline if no.** ML's growth has not ossified attention: new names break through as often in 2024 as in 2018.
- **Contribution to CS.** The first within-field, citation-free test of the large-field ossification hypothesis, separating field size from branding saturation.
- **Reader benefit.** The community learns whether ML's scale is crowding out new ideas, which bears on venue design and the 'too many papers' debate. Authors learn whether coining a name still helps when everyone does.
- **Closest prior work.** Chu & Evans 2021; Barnett & Doubleday 2020; Lorenz-Spreen et al. 2019; Stewart & Eisenstein 2018; Park, Leahey & Funk 2023.
- **Main threats.** Mention norms shift (LLM-era abstracts list more models). Polysemy grows as the namespace fills (collisions rose from 1.1% to 5.7%; 339 title names were re-coined). Size is confounded with topic maturity. Uptake is counted only within ICLR. The 2024 cohort's window ends in the largest pool.
- **Feasibility (3/10).** Reused the Q1 inventory (feas/q1_H.parquet). It holds names that are first attested in ICLR, have a distinctive shape, are not dictionary words and are not used by another paper in the same year. External uptake in years y+1 and y+2 excludes papers that share an author key or a normalised author name.

Names per cohort (title-coined T / abstract-only A):
- 2018: 49/56; 2019: 108/98; 2020: 220/176; 2021: 229/225; 2022: 313/277; 2023: 504/479; 2024: 1040/786.
- Total 4,644 (T 2,463, A 2,097, Tin 84). The T arm covers 2,463 of 3,727 NAME titles from 2018 to 2024.
- By pool, T arm: ACC 772, REJ 1,121, WD 556, DR 7.
- With the proposal-cue filter (symmetric sample): T 1,428, A 1,406. The 2018 cohort then has only 25 T and 41 A names.

Size of the later two-year window per cohort: 3,318 / 4,430 / 5,009 / 6,521 / 9,637 / 14,718 / 24,365. Rarefying every window to the 2018 size keeps 13.6% of the 2024 window. A threshold of 1 mention per 1,000 later papers means 3.3 mentions for the 2018 cohort and 24 for the 2024 cohort.

Pooled outcome prevalence (all cohorts together, never split by cohort):
- At least 1 external mention: 184 names (4.0%). At least 2: 65. At least 3: 30. At least 5: 13. At least 10: 7.
- At least 0.3 mentions per 1,000 later papers: 17 names. At least 1 per 1,000: 5 names.
- Expected names with at least 1 mention after rarefaction: about 68. With at least 2: about 15.

Mechanism cells (topic100 × cohort, 2018-24): 666 cells. 491 contain at least one T name and 464 at least one A name. Median cell size is 20 papers (IQR 7-42). NAME share per cell: median 0.16 (IQR 0.06-0.26).
- **Feasibility issues.** 1. **Too few outcome events.** Only 184 of 4,644 coined names (2018-24) get any external ICLR mention within 2 years. About half of those are polysemy false positives, and rarefaction leaves about 68. Breakthroughs (at least 1 per 1,000 later papers) number about 17. The headline trend can detect only a decline of 60-70% or more, and the size-versus-saturation mechanism is not estimable.
2. **Measurement error moves with the exposure.** Name-shaped tokens per abstract doubled (1.9 → 3.9), polysemy rises with the namespace, and the benchmark share rose from 10% to 15%. All of these move with cohort and field size, so per-paper normalisation is biased. Fixing it means hand-validating every event and adding a mention-density offset.
3. **Field size cannot be separated from cohort.** It is collinear with cohort fixed effects, and within-topic NAME density is about 50% sampling noise.
4. **Canon measures are confounded by truncation.** Age and old-canon share are left-truncated at 2017 (384 papers), so they rise mechanically with calendar year.
5. **Landmark names are absent.** Most were coined at other venues (CLIP, ViT, MMLU), and LoRA is wrongly filtered out by Q1's COMMON list. The "breakthrough" tail is mostly benchmarks.

Q12 is not viable as specified. A reduced version could survive as a robustness or secondary analysis inside Q1 (A): a descriptive cohort trend in hand-validated, density-normalised uptake for method names, T versus A.

Scratch scripts are in /tmp/claude-0/-home-user-cloud-research/ac787a97-846c-54b7-93f0-8bd8a69ad531/scratchpad/feas/q12/.
- **Identification plan.** Field size varies at the cohort level and is perfectly collinear with cohort fixed effects. The proposed regression (breakthrough on log topic×cohort size plus NAME density, with cohort and topic FE) can therefore identify only within-topic deviations.

Within-topic variation is thin:
- The residual SD of log cell size is 0.54 (MiniLM topics) or 0.51 (bge).
- The residual SD of NAME share is 0.11 or 0.12. But the sampling SD of a share in a median 20-paper cell is about 0.08, so roughly half of that NAME-density variation is noise. Reliability is about 0.5, which attenuates the Red Queen coefficient.
- With about 70 rarefied events, most topics have no events and drop out of an FE logit. The size-versus-saturation decomposition is not identified.

Best credible design is descriptive and two-arm:
- **Units:** method names coined in titles (T, with the proposal cue), separated from benchmarks, with abstract-only names (A) as the within-cohort comparison arm.
- **Outcome:** hand-validated external mentions in y+1 to y+2.
- **Model:** Poisson or negative binomial counts with offset log(later pool size × name-shaped tokens per abstract), or double rarefaction to equal pool size and equal mention density.
- **Estimands:**
  - The cohort trend in size-normalised uptake.
  - Whether the trend differs for T versus A. If branding saturation drives the decline, T should fall faster than A; field size should hit both arms.
  - As a secondary check, the trend within quartiles of topic NAME density, measured with large-cell or multi-year smoothing.

Key confounders:
- Mention inflation in LLM-era abstracts.
- Polysemy growth, which grows with the namespace (collisions 1.1% → 5.7%).
- Benchmark composition.
- Left-truncated first attestation for the 2018-19 cohorts (only 384 prior papers).
- The held-out 20% split: the coining paper may be missing.
- Topic maturity, which is confounded with size.
- The 2024 window, which falls in the largest and most LLM-heavy pools.

Drop the canon measures, or limit them to a rarefied fixed-lookback panel for 2023-26.
- **Judge, meaning (4).** Testing Chu & Evans within ML would be high-profile, but with about 68 validated events, measurement error that moves with field size, and a size-vs-saturation split that cannot be identified, only a collapse of 60-70% or more is detectable, so most outcomes would be uninformative.
- **Judge, novelty (5).** A within-field, citation-free test of Chu & Evans (2021) ossification separating field size from name saturation would be new, but the large-field claim itself is established, and the proposed decomposition is unidentified (size is collinear with cohort), so the deliverable novelty is a descriptive trend.
- **Judge, credibility (3).** Uptake events are too few (184 raw, about half polysemy, about 68 after rarefaction, 17 breakthroughs), field size is collinear with cohort FE, within-topic NAME density is about 50% noise, mention density doubled and polysemy grows with the exposure, and canon measures are left-truncated, so only a 60-70% collapse is detectable and the mechanism is not estimable.

## Q6. Does ML self-correct? Critique titles and the fashions they target

- **Question.** Does a critique paper ('Rethinking X', 'Do we really need X?', 'X is not all you need', 'pitfalls of X') slow the growth of the fashion it targets, and does ICLR accept critiques at par?
- **Stake.** Does ML self-correct through refutation (Lipton & Steinhardt 2018; Sculley et al. 2018), or do fashions end only by exhaustion and displacement (the critical downswing in Abrahamson & Fairchild 1999; Kuhn vs Lakatos)? It also tests authors' belief that critiques are hard to publish and get ignored.
- **Role of titles.** Titles define the critique genre and its target, the object noun phrase. Non-adversarial 'Revisiting' and 'Understanding' titles form the placebo genre.
- **Design.** About 500 strict critique titles plus about 330 'Rethinking' titles from 2018-26, with 300 validated. Part 1: multinomial ACC/REJ/WD vs non-critiques within topic100 x year, with WD vs REJ as the primary contrast because of camera-ready edits. Part 2, a stacked event study: the target region is the critique's k nearest prior-cycle neighbours in masked-abstract space plus papers whose titles match the target term. Its share growth over t+1..t+2 is compared with regions matched on pre-trend and size. Placebos are Revisiting papers and false event years. Heterogeneity: accepted vs rejected critiques. Secondary: does critical title share lead topic peaks (out-of-time forecast)?
- **Headline if yes.** Critiques bend the curve: fashions targeted by an ICLR critique grow X% slower over the next two years than matched topics, and more so after accepted critiques.
- **Headline if no.** Fashions roll on: targets grow as fast after a critique as matched topics, so ML fashions end by exhaustion and displacement, not refutation.
- **Contribution to CS.** The first large-scale test of whether ML critique papers change what the field works on, and of how review treats them, on a complete pool. It also yields a title-based indicator of topic peaks.
- **Reader benefit.** Authors learn whether a critique is a publishable and consequential project. The community learns whether its self-correction mechanism works.
- **Closest prior work.** Lipton & Steinhardt 2018; Sculley et al. 2018; Abrahamson & Fairchild 1999; Prabhakaran et al. 2016; Beese et al. 2023; Park, Leahey & Funk 2023.
- **Main threats.** Critiques appear near peaks, so mean reversion needs pre-trend matching and placebos. Few critiques have clean targets, and target extraction is noisy. With 40x growth, most share declines are dilution. Few usable years. Topic partitions are only moderately stable. A pilot (C10) already found a null for Abrahamson's upswing/downswing discourse at the form level.
- **Feasibility (3/10).** These are discovery-split counts from my own regex flags; there is no existing critique feature.

Genre sizes:
- Strict critique titles (do/does X really, really need, not all you need, pitfalls, myth/illusion/mirage, sanity/reality check, critical look/analysis of, overestimate, unnecessary/necessary?, plus skeptical yes/no questions with really/truly/necessary/sufficient/matter): n=194, 0.45% of U.
- 'Rethinking' (tpl_rethinking): n=334.
- Placebo 'Revisiting'/'Understanding': n=497.
- Looser regex variants: 228 to 287. Union of strict critiques and Rethinking: 616.

Strict critiques by year (2017-2026): 1, 1, 4, 8, 9, 8, 17, 21, 51, 74. The pools are ACC 60, REJ 84, WD 46, DR 4. 64% fall in 2025-26.

Rethinking by year (2017-2026): 1, 2, 3, 3, 18, 23, 20, 51, 72, 141. The pools are ACC 98, REJ 141, WD 93, DR 2.

Placebo by year (2019-2024): 226. All years: ACC 159, REJ 229, WD 102.

Precision from my spot checks (genuine critique of a method, practice or evaluation):
- Strict critiques: about 65% (26 of 40 hand-judged).
- Rethinking: about 25% (5 of 20). Most Rethinking titles brand a new method, e.g. 'TokenFormer: Rethinking...' or 'Rethinking Attention with Performers'.

Expected genuine critiques: about 125 strict plus about 85 Rethinking, so about 210 in all years.

Event-study units (Part 2):
- 2-year horizon (critique in 2024 or earlier): about 75 genuine events.
- 1-year horizon (2025 or earlier): about 125.
- Events that also have a frequent, specific target string (10 or more title/abstract hits in t-2..t-1): 34 in 2019-24. By hand, only about 8-10 of these are clean adversarial critiques of an identifiable fashion, e.g. 'Self-Supervision is Not All You Need', 'Is Pre-training Truly Better Than Meta-Learning?', 'Is Deep RL Really Superhuman on Atari?', 'Behind the Myth of Exploration in Policy Gradients'.

Target extraction:
- Regex extracted a target for 62% of the 616 titles (70% of Rethinking, 53% of strict critiques).
- Targets are often generic: 'Attention', 'Labels', 'Scale', 'Solution', 'Neurons' (should be neural collapse). The median target had only 1 prior-2-year string hit.
- **Feasibility issues.** 1. The critique genre is tiny and back-loaded: 194 strict critiques (0.45%), 64% of them in 2025-26, which have no or only partial follow-up years. The roughly 500 strict critiques the design assumes do not exist.

2. 'Rethinking' is mainly a method-branding template, with about 25% adversarial precision, so it cannot double the sample without heavy validation.

3. Only about 8-10 critiques from 2024 or earlier have a clean, identifiable fashion target. Regex targets are generic ('Attention', 'Labels', 'Scale').

4. The target region in embedding space cannot separate adoption of the fashion from debate about it, so the outcome is not a valid measure of 'growth of the fashion'.

5. Critiques select into regions that are already growing (pre-trend 0.34 vs 0.19). Outcome noise is large (SD 0.6-0.76 log), and pre-trend matching explains about 1% of it, so mean reversion and noise swamp any plausible effect. The MDE is about 15-25% with noisy events and about 40-50% with clean ones.

6. This is an ICLR-only window on critiques that often first appear at other venues. Pilot C10 already found a null for upswing/downswing discourse.

Part 1 (are critiques accepted at par?) is answerable but is close to another descriptive acceptance-rate result of the kind the PI called a data summary. Recommendation: drop Part 2, or fold the critique genre into candidate B or C as a heterogeneity cut. Do not run it as a headline study.
- **Identification plan.** Part 1: are critiques accepted at par? This part is credible but modest.
- Data: hand- or LLM-validated critique titles, about 210 genuine, against all other papers.
- Model: conditional logit for ACC vs REJ, and separately WD vs REJ (camera-ready-free), with topic100 x year fixed effects.
- Controls: log_authors, n_words, question-title form; author-history controls in 2022+ (exp_valid).
- Placebo genre: 'Revisiting'/'Understanding' (n=497).
- Confounders:
  - Critiques are mostly empirical or benchmark papers. Add an 'empirical study/benchmark' title or keyword control, and compare with non-critique benchmark papers.
  - Topic: use within-cell FE.
  - Senior authors who can afford critiques: use the 2022+ experience controls.
- No review scores, so no reviewer-level mechanism.

Part 2: does a critique bend the curve? I do not recommend it as specified. The best feasible version:
- A stacked event study on validated critiques from 2019-2025, with a 1-year horizon as primary because 2-year horizons leave only events from 2024 or earlier.
- Treated unit: the K=20 masked-abstract region of the critique in t-1, intersected with target-string hits to drop debate papers where possible.
- Controls: 5 random non-critique seed regions per event, matched on year, region size and pre-trend.
- Outcome: log share growth from t-1 to t+1.
- Placebos: Revisiting seeds and false event years.
- Heterogeneity: ACC vs REJ critiques.
- Main confounders:
  - Mean reversion: critiques select into upswings, and pre-trend has little predictive power.
  - Dilution from 40x field growth: use shares, which still mix with composition shifts.
  - The region measure counts the critique's own debate as growth.
  - ICLR-only diffusion: the most influential critiques often appear at NeurIPS/ICML/arXiv first.
  - Contamination: about 75% of 'Rethinking' titles are method papers.
- A cleaner reframing: drop the causal claim and ask the forecasting question (does a region's critique-title share lead its peak or decline?). Even that has very few peaked topics in 2019-24 and was effectively null in pilot C10.
- **Judge, meaning (4).** Whether ML self-corrects is a first-order question, but with only about 8-10 clean critique events and an outcome that counts debate as growth, neither answer would be credible enough to change beliefs. The part that can be answered (critique acceptance at par) is a data summary.
- **Judge, novelty (4).** Chen, Murray, Liu & Barabási (2024, arXiv:2412.02809) already find that critical letters do not change the citation trajectory of the papers they criticise (cf. Radicchi 2012, 'no bad publicity'), so 'critique does not bend the curve' is largely answered; moving to topic level in ML and asking whether critiques are accepted at par adds only incremental novelty.
- **Judge, credibility (3).** There are only 194 strict critiques (64% in 2025-26) and about 8-10 clean pre-2025 targets, 'Rethinking' is 75% method branding, target regions cannot separate adoption from debate, and critiques select into upswings with noise (SD 0.6-0.76 log) that pre-trend matching cannot absorb; Part 2 is infeasible and Part 1 is another acceptance-rate summary.

## Dropped ideas

- [5] Distinctive or informative? What branding did to titles as summaries: largely answered by pilot C12. NAME titles are already better self-identifiers (retrieval 0.944 vs 0.917), the informativeness measures disagree, judges scored that direction lowest, and it is descriptive, with no practice it would change.
- [6] Converging prose or converging ideas? Homogenization in the LLM era: largely answered by pilot C11, which found that title structure converges while title semantics diverge at fixed abstract similarity. Its structural half re-describes the NAME rise and finding 3, which makes it a data summary with no decision stake.
- Dropped from the Q1 merge: [1]'s Stewart & Eisenstein test (whether spread across topics predicts survival). It is tangential to the naming stake.
- Dropped from the Q10 merge: the cross-genre influence ratio ('benchmarks draw X times the follow-on work of methods') from Bandwagon builders. It is not identified, because benchmarks are mentioned when used and methods when compared. Only the review-calibration contrast within each genre is kept.
- Dropped from the Q7 merge: the twin tiebreak on title features using ACC vs REJ. Title-acceptance associations are not identified after the camera-ready audit (0 of 18 auditable features pass), so only the REJ-vs-WD tiebreak is kept.
- Dropped from the Q4 merge: the compensation payoff on ACC vs REJ, the plain momentum acceptance premium, and the level effect of crowding on branding. The first fails the camera-ready caveat, pilot C19 found the momentum premium null under controls, and the crowding level effect re-describes finding 5 and pilot C18. Only the gradient within topic, lab and paper is kept, with payoffs tested on WD vs REJ.
- Dropped from the Q4 merge: ex-post Rogers bins and the adoption percentile as the primary lifecycle clock, because they use lookahead (kept as descriptive only), and idea 5's Berger & Le Mens test of rise-fall speed, which is tangential.
- Dropped from the Q8 merge: idea 2's population-level test of payoff-biased template copying. Pilot C16 already found the field-level success bias null on WD vs REJ.
- Dropped from the Q3 merge: B+ Prescience's oral/spotlight tier outcome, which has small cells and adds little to the stake.
