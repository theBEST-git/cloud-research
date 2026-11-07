# Story P2 (rival to Candidate 1): "A Package, Not a Herd"

Built 2026-11-03 by the story designer for the rival line. This file designs the paper. It is not the paper.

**What was read.**
- In full: `dossier_core.md`, `dossier_posthoc.md`, `landscape.md`, `verify_prior.md`, `theory_anchors.md`,
  `lit_fashion_waves.md`, and the current Part 1 draft.
- In part: `lit_ml_metaresearch.md` (sections A-C) and `lit_closest_prior.md` (A5-D).
- `analysis_novelty.md` **does not exist**: the subagent was refused permission to write it. The novelty numbers below
  were read from `paper_ws/output/novelty_newcomer.json` and `.csv` instead.
- Read for this story only, all committed and outcome-free:
  - `research/fashion/output/posthoc/ph5_fmwave/free_entry.csv` and `free_fm_share.csv`;
  - `research/fashion/output/posthoc/ph5_position/free_herding.csv` and `free_twin_share.csv` (header only);
  - `research/fashion/output/posthoc/ph5_kwtiming/free_profile_states.csv`;
  - `research/topics/output/hindsight_check.json` (map summaries only);
  - column headers of `paper_contributions.csv.gz` and `topic_year_maturity.csv.gz`.

**What was not read or run.** No outcome or decision column. None of `posthoc.py`, `run_frozen.py`,
`run_confirmation.py` or `outcomes.py`. No author of the corpus is named here. The draft's author line is not copied.

**Pointers.**

| Pointer | Points to |
|---|---|
| `DC:n` | dossier_core.md, line n |
| `DP:n` | dossier_posthoc.md, line n |
| `LS:n` | landscape.md, line n |
| `VP:n` | verify_prior.md, line n |
| `TA:n` | theory_anchors.md, line n |
| `NOV` | paper_ws/output/novelty_newcomer.json |
| `FE` | ph5_fmwave/free_entry.csv |
| `FH` | ph5_position/free_herding.csv |
| `FPS` | ph5_kwtiming/free_profile_states.csv |
| `HC` | topics/output/hindsight_check.json |

Tiers follow DC:25-31 and DP:12-19.

**Values first read for this story.** Values marked **[read here]** come from the committed outcome-free files above
and are not yet in a dossier. They should be added to a dossier before the writers quote them.

---

## Bottom line

> **What converged in the foundation-model (FM) shift was the package that papers build on, not a herd of people.**

The paper makes three moves, all expansions of one claim:
1. It locates the convergence in the substrate, using a paper-level label that needs no topic map. Two results carry
   this:
   - FM adoption displaces new architectures within topics (tier A).
   - The fashion-like *topic* signals are the ones that depend on how the map is drawn (tier E).
2. It shows that the people did not converge as herding predicts:
   - Entrants reverse our registered herding prediction (A).
   - Their content sits farther from earlier ICLR work (E, new).
   - The package travels with an ICLR record, not with the least-informed entrants (E).
3. It asks whether review amplifies the convergence by paying for popularity. It shows no detectable premium for
   following the crowd (C/B). It finds a premium for records (B) and a package premium that does not fade as adoption
   rises (D).

Candidate 1's gate results all keep a place, as the third move. What changes is the centre of gravity:
- **Candidate 1** puts tier-B "anchoring" in the title, and its field-level Act 1 is the part its own frame cannot
  interpret (TA:83-84, TA:600).
- **P2** puts the two tier-A results and the outcome-free population facts at the centre. It builds on the gaps that
  survived the verification of prior work (G2, G5, and G4 narrowed), not on the gap that was narrowed twice (G3).

---

## 1. Title and thesis

**Title (recommended).** *A Package, Not a Herd: What Converged in Machine Learning's Foundation-Model Shift*

**Alternatives:**
- *Homogenised, Not Herded: Tools, Entrants and Review in Machine Learning's Foundation-Model Shift.* This engages
  Bommasani et al.'s term directly.
- *Waves Without Herds: Where Machine Learning Converged during the Foundation-Model Shift, ICLR 2017-2026.* This is
  the landscape's option (LS:839).

**Thesis (one sentence, the story line).**
> At ICLR, the foundation-model shift made machine learning converge on the package that papers build on, not on a
> herd of researchers:
> - within topics, FM adoption goes with fewer papers proposing new architectures (registered, replicated);
> - topic entrants bring method proposals and content farther from earlier ICLR work;
> - entrants take up the package later than researchers who already have an ICLR record;
> - review shows no detectable premium for following the crowd.

**Short form**, for the last line of the introduction: "The field converged in its tools, not in its people."

**Fixed terms.** Define them once and never vary them.

| Term | Definition | Source |
|---|---|---|
| **Package** (synonym: substrate) | What a paper builds on. Measured per paper by the codebook FM label: the paper "uses or adapts a large pre-trained model (LLM, CLIP, pre-trained diffusion)". It is an LLM label, not a human label. | DC:138, DC:52 |
| **Contribution** | What a paper offers: the codebook's primary class (method, including new architecture as `primary_type == model`; theory; empirical; dataset/benchmark; evaluation; other). A contribution type is not a measure of novelty. | DC:129, DC:313-314 |
| **Newcomer paper** | No author has an earlier ICLR submission in the paper's topic, with any outcome. | DC:53, DC:144 |
| **First-time team** | No author has any earlier ICLR submission, in any topic, with any outcome. | TA:684-685 (PRE:1281) |
| **Herding (imitation)** | Conformity whose reference point is what others are doing now. | TA:48-52 |
| **Homogenisation** | Used only in Bommasani et al.'s sense: convergence in the substrate. Not "people think alike". | FW:264-270 |
| **Content distance** | 1 − mean cosine to the 10 nearest earlier-year ICLR papers (SPECTER2, centred), as a percentile within topic × year. Call it **content distance from earlier ICLR work**, never "novelty" or "originality". | NOV; DP:255 |

---

## 2. Conversations, gap, novelty wording, meaning beyond ICLR, and why this line beats Candidate 1

### 2.1 The conversations P2 contributes to

**Host conversation: how ML and NLP read their own FM shift** (landscape Conversation 5).

The essays and studies:
- FMs' effectiveness across tasks "incentivizes homogenization" (`bommasani2021opportunities`, FW:264-270).
- The hardware lottery (`hooker2021hardware`).
- Convergence on general, compute-scaled methods as the efficient "bitter lesson" (`sutton2019bitter`).
- Thematic narrowing on topic models fitted over the full period (`klinger2020narrowing`).
- The compute divide (`ahmed2020dedemocratization`).
- Explore/exploit cycles from interviews (`gururaja2023build`).
- "History repeats" (`saphra2024first`).
- Half of 2023 LLM first authors were new to LLM work (`movva2024topics`, CP:64-69).
- Persistence across the earlier deep-learning shift (`bao2025persistence`, VP:106-136).

The open question is whether the convergence is a herd or a substrate:
- **Herd:** people converge on fashionable topics, and entrants pile in.
- **Substrate:** the tools converge while the contributions on top of them stay varied.

Most of this literature is essays, interviews or descriptive trends (FW:308; CP:137). P2 answers the question with
registered and held-out evidence.

**Theory conversation: bandwagons, packages and herds** (Conversation 1). Two traditions explain how a field comes to
look alike:
- **Imitation.** Covers:
  - cascades (`bikhchandani1992theory`, `banerjee1992simple`);
  - mimetic isomorphism under uncertainty (`dimaggio1983iron`);
  - frequency imitation (`haunschild1997modes`);
  - reputational herding (`scharfstein1990herd`, TA:291-302).
- **A shared package.** Covers:
  - Fujimura's "standardized package" that makes problems do-able for many labs (`fujimura1988molecular`). Its content
    was seen only in secondary descriptions, so cite it for the general argument (FW:107-113).
  - Lock-in under increasing returns (`arthur1989competing`, TA:191-208).

Who adopts a package first is the province of absorptive capacity (`cohen1990absorptive`, TA:138-153). The
literature rarely separates these traditions. The fashion-waves synthesis itself lists "bandwagons without herders" as
an open framing (FW:312). P2 separates them inside one complete submission population.

**Method conversation: computational histories of a field** (Conversation 4).
- Field histories fit one topic model on all years and read it forward (`hall2008studying`, `anderson2012towards`,
  `prabhakaran2016predicting`, `pramanick2023diachronic`, `schafermeier2021topic`).
- Static models can miss small emerging topics (`li2025evaluation`).
- Early-warning signatures have been tested prospectively (`khanbayov2026topical`).

P2 adds one point. The most fashion-like signals are the ones most sensitive to the fitting window, while the
convergence signal (a paper-level substrate label) needs no map and survives the hindsight variants. Measurement is
therefore part of the thesis, not a preamble.

**Secondary conversations:**
- **Entrants** (Conversation 3): `movva2024topics`, `biliotti2024breaking` (the same newcomer-to-topic definition),
  `jurgens2026future` (context), `koch2021reduced` (benchmarks are an insider activity).
- **Review at ML venues** (Conversation 6): `wang2023what`, `xu2026reviewer`, `ibrahim2026bias`, `jung2025what`,
  `stelmakh2023large`, `hill2025pivot`.
- **Confirmatory meta-research** (Conversation 7): `nosek2018preregistration`, `kerr1998harking`,
  `fischhoff1975hindsight`.

### 2.2 Closest prior work (verified) and what P2 adds

| Work | What it did | What P2 adds | Wording constraint |
|---|---|---|---|
| `bommasani2021opportunities` | Essay. Defines FMs; argues that their effectiveness incentivises homogenisation (FW:264-270). | A topic-level test of displacement, registered in advance and replicated on held-out papers. Evidence that homogenisation sits in the substrate, not the people. | Do not claim to "confirm Bommasani"; say "consistent with homogenisation in their sense". |
| `gururaja2023build`; `saphra2024first` | Interviews plus ACL Anthology analysis of explore/exploit cycles; a position paper on history repeating (MM:39; CP:71). | A quantitative, registered instance of the exploit-phase displacement. Who carries it. | — |
| `klinger2020narrowing` | Thematic diversity of arXiv AI stagnates; topic models fitted on the full period (MM:83). | Diversity measures peak in each map's own fitting years (DC:189-192). We make no content-diversity claim. | Do not say "AI did not narrow". |
| `movva2024topics` | Half of 2023 LLM first authors were new to LLM work; arXiv; descriptive (CP:64-69). | What entrants write, how far their content is from earlier work, and how they relate to the package. | Our 72.9% newcomer share is "consistent in spirit" (DC:151). |
| `bao2025persistence` | SPECTER2 similarity to a researcher's own prior ICML/NeurIPS papers across the deep-learning shift. Persistence goes with lower impact. Describes deep learning displacing statistical learning (VP:113-128). | Registered, held-out, topic-level displacement in the FM shift (G5 holds, VP:435). Entrants' contribution types (G2 holds, VP:432). | The closeness measure is not new. The tension (persistence penalised in impact; continuity rewarded at the gate) belongs in the Discussion (VP:134-136). |
| `huang2026catalyst` | Topic initiators at ICLR 2017-2025 precede topic growth (VP:57). | Entrants' contribution type and package adoption, not who starts topics. | Cite as a neighbour (VP:432). |
| `prabhakaran2016predicting`; `pramanick2023diachronic` | Rhetorical roles predict topic rise and fall. Methods drive and datasets follow. Published papers; topics fitted on the full period. | Contribution type split by entry status; substrate measured per paper. | — |
| `li2025evaluation`; `khanbayov2026topical` | Static models' emergence detection; a prospective emergence predictor on five AI venues (VP:55, 58). | The hindsight effect quantified on the same papers with the same model, varying only the fitting window: 29 vs 8. | Keep "maps also differ in fitting corpus" (DC:229). |
| `fujimura1988molecular` | Ethnography of a package bandwagon in cancer research (FW:107-113). | A population-level, registered test in a field whose package is unusually well defined. | Content is secondary only; cite for the general argument. |
| `stelmakh2023large` | ICML 2020 RCT: no herding detected among reviewers (VP:250-270). | The matching question for authors. Entrants do not write the follow-on work that herding predicts. | Say "no herding detected", not "reviewers are independent" (VP:269-270). |
| `wang2023what`; `xu2026reviewer` | Topic-level acceptance differences at ICLR; at equal scores, topic predicts acceptance (VP:44, 47). | Only that topic edges regress out of sample (b 0.60 on held-out papers). | Never claim the first topic-acceptance result (VP:104). |
| `hill2025pivot` | Larger pivots are less often published: preprints from 2015-2018, highest-pivot bin about 35% lower (VP:288-316). | The decision itself, on every submission, at an ML venue, under double-blind review, held out. | Never "first pivot penalty at the gate". |
| `ibrahim2026bias` | ICLR 2019-2025 plus a pre-registered 2026 cohort; prestige at the borderline, concentrated where arXiv identifies authors (VP:188-218). | — | No "first confirmatory design" (G7 is dropped). A rival reading of the record premium. |
| `jung2025what` | Process factors on ICLR 2017-2025, 28,358 submissions (VP:138-163). | — | Their "earlier submission" is not timing within a wave. |

### 2.3 The gap, and the exact novelty wording

**Gap paragraph** (for the Background section; every claim is traceable to 2.2):

> Accounts of machine learning's foundation-model shift describe a field whose new models incentivise
> homogenisation (Bommasani et al., 2021), whose topics narrow (Klinger et al., 2020), whose direction follows its
> hardware (Hooker, 2021) or the most general, compute-scaled methods (Sutton, 2019), and whose researchers describe
> an exploit phase (Gururaja et al., 2023). Many authors of large-language-model papers are new to the area (Movva et
> al., 2024), and across the earlier deep-learning shift researchers who stayed close to their own past work gained
> less later impact (Bao and Li, 2025). These accounts rest on essays, interviews, descriptive trends or topic maps
> fitted with hindsight, and they do not separate convergence in what papers build on from convergence in who enters
> a topic and what they bring.

**Novelty sentence** (exact wording; keep the qualifier):

> To our knowledge, among the works we checked, no study tests at the level of topics, with registered hypotheses
> replicated on held-out papers, whether adoption of a foundation-model package goes with the displacement of other
> work, and asks in the same complete submission population whether topic entrants carry that convergence or the
> field's divergence.

**Supporting sentence:**

> Fourteen searches for studies of author herding at ML or NLP venues found none that uses submission data; the
> nearest test, a randomised trial at ICML, detected no herding among reviewers (Stelmakh et al., 2023).

- Source: VP:413-423.
- Write the paper's version as "among the works we checked".

### 2.4 Required narrowings

Each must appear in the text exactly as below.

1. **Topic differences in acceptance are documented** (Wang 2023; Xu 2026). We claim only that topic edges regress
   out of sample (b 0.60 [0.32, 0.88] held-out, B; DC:376).
2. **Hill et al. (2025) report lower publication success for larger pivots.** For far jumps, say "we observe the
   decision itself, on every submission to an ML venue, under double-blind review, with held-out replication".
3. **Bao and Li (2025) already measure persistence** as SPECTER2 similarity to one's own prior ML papers, and
   persistence went with lower impact. In P2:
   - The far-jump measure is a secondary, B-tier gate result.
   - The tension goes in the Discussion.
   - Whether our far-jump cosine is SPECTER2 is still unconfirmed (VP:496-498). Do not write "as we do" until it is
     checked.
4. **Ibrahim et al. (2026) pre-registered an out-of-sample ICLR test.** Make no "first confirmatory design" claim.
   Their prestige-via-arXiv result is a rival reading of the record premium in §6.
5. **Stelmakh et al. (2023):** "no herding detected" among reviewers. Pair it with our entrants.
6. **Boudreau et al. (2016):** their distance runs from evaluator to proposal. Do not equate it with far jumps.
7. **For hindsight**, cite Li et al. (2025) and Khanbayov and Kurban (2026). Claim only: "same papers, same model,
   only the fitting window differs: 29 vs 8".

### 2.5 Why it matters beyond ICLR

1. **Every field now taking up FMs faces the same question.** Does a tool shift make the *people* and their
   *contributions* alike, or only the substrate?
   - P2's measures transfer to any venue with complete submission records:
     - a paper-level substrate label from a fixed codebook;
     - lagged topic adoption;
     - entry status from author identifiers;
     - content distance;
     - a registered held-out split.
   - The ICLR answer is homogenisation of the substrate with no detected herding among entrants. It is a baseline
     other fields can be tested against. The paper must not claim it generalises (DC:56).
2. **Theories of scientific bandwagons gain a quantitative case.**
   - Fujimura's package bandwagon was ethnographic and predicted that a package makes problems do-able for many
     newcomers.
   - ICLR's package spreads first through people who already have an ICLR record, the absorptive-capacity pattern
     (`cohen1990absorptive`).
   - That qualifies the "package invites outsiders" reading and separates the package from an imitation herd.
3. **The hindsight result applies to every topic-model history.** That is the ACL genre itself: Hall et al., Anderson
   et al., Prabhakaran et al., Pramanick et al., Klinger et al. The robust signal is measured per paper, not on a map.
4. **Debates on whether a paradigm shift closes a field** (Movva 2024; Jurgens 2026; Bao and Li 2025) get a precise
   answer for one venue:
   - entrants are not reduced to follow-on work;
   - record-holders adopt the package first;
   - review goes with records (B).

   No advice follows from this, and none is given.

### 2.6 Why P2 is more meaningful than Candidate 1 ("Anchored, not herded")

**1. Its thesis rests on the strongest tiers.**

| | Candidate 1 | P2 |
|---|---|---|
| Positive half carried by | Tier B only: far jump, within-author closeness, one insider (DC:370, 372, 374) | Tier A (H1d; H2b′/H2c′) and tier E population facts |
| Status of that evidence | Post hoc in discovery. The secondary held-out tests are one-sided and unadjusted. The insider test's Holm 0.019 holds within its family only, about 0.17 across modules (DP:54-55). Teams H1 is underpowered at its discovery effect (MDE80 ≈ 4.5 vs +3.42; DC:374, 380). | Registered or outcome-free |
| If a reviewer discounts all post hoc results | The thesis is gone, because "Anchored" is the title | One section loses force; the thesis stands |

**2. Its novelty sits on the gaps that survived verification.** The check of prior work (VP:429-437) found:

| Gap | Status | Carries |
|---|---|---|
| G2: what entrants bring | Holds | P2 |
| G5: registered held-out FM displacement | Holds | P2 |
| G4: hindsight | Narrowed only to the fitting-window wording | P2 |
| G3: pivot and chaperone at the decision | Narrowed twice: Hill 2025 (publication) and Bao & Li 2025 (measure) | Much of Candidate 1's novelty |

Candidate 1's insider premium also faces a published rival mechanism: visible prestige at the borderline (Ibrahim
2026; VP:209-218).

**3. Its frame discriminates where its evidence is strongest.**
- The theory file concedes that the imitation-vs-continuity frame is "weakest at the field level", where "H1d fits a
  package bandwagon, lock-in and efficient choice alike" (TA:83-84, TA:600). Candidate 1 therefore spends its
  strongest result in an act its own frame cannot read.
- P2's distinction between substrate and people uses H1d as what it is, the location of the convergence. It then
  moves the discrimination to entry, where the herding account makes sharp, registered predictions:
  - entrants imitate most (DiMaggio & Powell; cascades);
  - duplication per pair rises;
  - the least-informed adopt the trend fastest.
- The data contradict each prediction, on A and E evidence.

**4. It speaks to the larger and livelier conversation for an ACL audience.**
- "Is the FM era homogenising research?" is the field's own question (Bommasani, Hooker, Klinger, Gururaja, Saphra,
  Movva).
- "Homogenisation of the substrate without detected herding of the people" is a claim every reader of those papers
  can use.
- Candidate 1's payoff ("conformity at the gate is continuity") speaks mainly to the science-of-science literature on
  evaluation.

**5. It uses the new content-distance result as a pillar, not a footnote.** That result answers the strongest
objection to H2b′, that a method paper is a type, not novelty (DC:313-314). It does so with a content measure for all
42,325 RQ2 papers, holding:
- within topic × year;
- within method papers;
- in both eras.

Under Candidate 1 it would be peripheral.

**6. Measurement becomes part of the argument.** The strongest convergence signal needs no map. The fashion-like
signals depend on the fitting window. The finding "measurement locates the convergence" is substantive.

**7. It avoids two wording hazards that Candidate 1 must manage:**
- the "anchoring" collision with the cognitive-bias term, which the herding-in-science literature itself uses (TA:499-512);
- an advice reading ("stay close to your record", "add an insider"), which DC:427 and DP:298 forbid.

**Where Candidate 1 is stronger.** Say this openly to the supervisor.
1. It integrates the gate results more tightly. In P2 the gate is the third act, framed by one question but less
   central.
2. Its imitation-vs-continuity split is a sharper conceptual contribution for science of science
   (`weisberg2009epistemic`).
3. P2's people layer leans on several tier-E rows. H1d is underpowered at the discovery effect on held-out papers
   (MDE80 12.0 vs −8.0), so it confirms direction, not size.
4. "Package versus herd" is not discriminated by H1d alone.

**Synthesis.** P2 keeps every Candidate 1 result (§6). A reviewer who prefers Candidate 1's concept still finds it in
§6 and the Discussion. A reviewer who distrusts post hoc results still finds an intact thesis.

---

## 3. Abstract (180 words; counted with `wc -w`)

> Machine learning is often said to herd onto whatever is popular. We ask what converged during the foundation-model
> (FM) shift, using 43,480 ICLR submissions from 2017 to 2026, rejected and withdrawn papers included, with registered
> hypotheses run once and replicated on 11,099 held-out papers. The share of submissions building on an FM rose from
> 0.3% to 54.4%, and within topics, prior FM adoption goes with fewer papers proposing new architectures (registered,
> replicated). Topic-level fashions are partly a measurement artefact: on the same papers, a topic map fitted with
> hindsight finds 29 emerging topics, a map fitted on 2017-2020 only 8. The people did not converge as herding
> predicts. Papers by newcomers to a topic are more often method papers and less often benchmark papers, the reverse
> of our registered prediction; the reversal replicated. Descriptively, their content lies farther from earlier ICLR
> work, and teams new to ICLR write FM papers less often while FMs spread through a topic. Review shows no detectable
> premium for following the crowd. What converged is the package papers build on, not a herd of researchers.

**Sources for each number:**
- 43,480 and 11,099: DC:65, 72.
- 0.3% → 54.4%: DC:163.
- H1d: A, DC:271, 364.
- 29 vs 8: E, DC:176-179.
- H2b′/H2c′: A (reversed), DC:296-297, 365-366.
- Content distance: E, NOV `main_pct`.
- First-time FM gap: E, DP:360-362.
- "No detectable premium": H3a C (DC:367), branding D\* (DP:133), premia B (DC:376).

**Wording notes:**
- "Topic-level fashions are partly a measurement artefact" is deliberately "partly", because the maps also differ in
  corpus (DC:229).
- "Descriptively" marks the two tier-E clauses.

---

## 4. Three contribution statements

Each contribution is to a conversation, and each expands the one thesis.

**C1. To ML's debate about homogenisation in the FM era: where the convergence lies.**
> To our knowledge, among the works we checked, we give the first topic-level test of foundation-model displacement
> registered in advance and replicated on held-out papers. We show that the convergence lies in the substrate, not in
> the people. Within topics, prior FM adoption goes with fewer new-architecture papers (−11.0 pp held-out, tier A),
> while topic entrants keep bringing method proposals (tier A, the reverse of our registered prediction) and content
> farther from earlier ICLR work (+5.9 percentile points, tier E).

**C2. To theories of bandwagons and herding: package and herd separated in one population.**
> In one complete submission population, the spread of a shared package and an imitation herd come apart:
> - The package travels with an ICLR record. Teams new to ICLR write FM papers 4.6-14.7 pp less often in topics at
>   5-50% adoption, while topic newcomers who already have an ICLR record do not differ detectably from incumbents.
> - Near-duplication per pair of papers falls as volume grows.
> - Review shows no detectable premium for following the crowd. Topic acceptance edges regress, and acceptance goes
>   with a team's record.
>
> Tiers: E, E, C/B, B.

**C3. To computational histories of a field: measurement locates the convergence.**
> The most fashion-like signals are the least robust to measurement, and the convergence signal is the most robust:
> - On the same papers with the same model, varying only the fitting window moves the count of emerging topics from
>   29 to 8 and reverses a life-cycle conclusion.
> - A paper-level substrate label needs no topic map, and its registered displacement test passes both hindsight
>   variants.
>
> Tiers: E; A.

**The design statement** (registered, single frozen run, every held-out test reported, tiers) goes in the Data
section. It is not a contribution, because Ibrahim et al. (2026) narrow G7.

---

## 5. The argument, section by section

### 5.0 Word budget

The target is about 3,800 words of body text.

| § | Section | Words |
|---|---|---|
| 1 | Introduction | 600 |
| 2 | Background: two accounts of a converging field | 380 |
| 3 | Data, measures and evidence tiers | 400 |
| 4 | What converged: not the topics, the package | 800 (4.1: 330; 4.2: 470) |
| 5 | Who carries the package, and who carries divergence | 680 |
| 6 | What review pays for during a package shift | 520 |
| 7 | Discussion | 330 |
| 8 | Conclusion | 100 |
| | **Total** | **3,810** |

Limitations, captions, tables and the appendix are outside the count.

### §1 Introduction (≈600)

**Role.** State the puzzle (convergence is visible, and the herd reading is common), give the two accounts and the
predictions that tell them apart, announce the registered failure, and state the thesis and contributions.

**Paragraph by paragraph:**

1. **Hook.** Field-level convergence: these numbers set the scale.

   | Item | Value | Tier | Source |
   |---|---|---|---|
   | Submissions, 2017 → 2026 | 384 → 15,411 (×40.1) | E | DP:70-71 |
   | Share building on an FM | 0.3% → 54.4% | E | DC:163 |
   | Share proposing a new architecture | 24.5% → 7.5% | E | DC:164 |
   | Frequent keywords that rose and fell (Figure 1) | 17 of 68 | E | DP:81 |

2. **Two readings.**
   - **The herd reading:**
     - ML's self-critique: growth and thin reviewing (`lipton2019troubling`), homogenisation
       (`bommasani2021opportunities`), narrowing (`klinger2020narrowing`);
     - fashion theory: `abrahamson1991managerial`, `bikhchandani1992theory`.
   - **The package reading:** `fujimura1988molecular`, `arthur1989competing`, `sutton2019bitter`.
   - Both predict convergence. They disagree about **where** it lives.
3. **What tells them apart.** Entry, duplication per pair, who adopts the package first, and what review pays for.
   - We registered the herding prediction for entrants (H2b/H2c) on 2026-10-13, before any full-corpus label existed
     (DC:237).
   - It came out significant in the opposite direction, and the reversal held on held-out papers (A; DC:33-36, 296-297).
4. **Design in one sentence.**
   - 43,480 submissions, including rejected and withdrawn papers (DC:65-66).
   - A single frozen run (DC:246).
   - 11,099 held-out papers (DC:72).
   - Every finding tiered (Table 1).
   - All results are associations (DC:42).
5. **Thesis, then C1-C3** in three short bullets.

**Figure.** Figure 1 (exists) goes here, re-captioned as keyword turnover; see §7 of this file.

### §2 Background: two accounts of a converging field (≈380)

**Role.** Turn the two readings into predictions at each layer, which become Table 1's two prediction columns. Place
the gap.

**Paragraph 1: Imitation (herding).**
- Mechanisms:
  - cascades (`bikhchandani1992theory`; `banerjee1992simple`);
  - mimetic isomorphism under uncertainty (`dimaggio1983iron`; mimetic section seen only secondarily, TA:217-219);
  - frequency imitation (`haunschild1997modes`);
  - reputational herding (`scharfstein1990herd`);
  - "followers" (`weisberg2009epistemic`).
- Predictions:
  - Entrants, with the least information, imitate most. They write follow-on work close to existing work and adopt
    trends fastest.
  - Duplication per pair rises.
  - If imitation is individually rational, review pays for following.

**Paragraph 2: The package.**
- Mechanisms:
  - a standardised package makes problems do-able (`fujimura1988molecular`, general argument only);
  - increasing returns (`arthur1989competing`);
  - homogenisation (`bommasani2021opportunities`);
  - the hardware lottery (`hooker2021hardware`) and efficient choice (`sutton2019bitter`) as rival accounts of *why*.
    P2 does not adjudicate between them.
  - Who adopts first: absorptive capacity (`cohen1990absorptive`). Record-holders take up the package; entrants bring
    their own contributions.
- Honesty sentence: bandwagons can spread among adopters without any reward (`abrahamson1993institutional`, TA:269-287).
  "Package" therefore does not mean "no one imitates".

**Paragraph 3: Histories and the gap.**
- Prior histories: `hall2008studying`, `anderson2012towards`, `prabhakaran2016predicting`, `pramanick2023diachronic`,
  `gururaja2023build`, `saphra2024first`, `movva2024topics`, `bao2025persistence`, `huang2026catalyst`.
- Then the gap paragraph and novelty sentence of 2.3, verbatim.
- One sentence on what is not new (LS:479-489): ICLR OpenReview data, noisy review, FM growth as an idea, and that
  entrants are numerous.

### §3 Data, measures and evidence tiers (≈400)

**Role.** Make the three layers measurable and give the reader the tiers.

**Claims and facts:**

- **Corpus.**
  - 43,480 discovery submissions with a usable abstract, 2017-2026, including rejected and withdrawn papers
    (DC:65-66).
  - Built from our own dated acquisitions of official OpenReview records (DC:62).
  - Held-out set: 11,099 papers, described as "a pre-registered out-of-sample replication, not a certified untouched
    holdout" (DC:43-44, 72).
- **Substrate layer.**
  - The FM label and the new-architecture label (`primary_type == model`) come from a fixed LLM codebook.
  - Blind second pass: κ 0.93 (DC:133). Held-out FM agreement: 98.2% (κ 0.960) (DC:135).
  - These are LLM labels, not human labels (DC:52).
  - The text is partly camera-ready: in 2023-26, code links appear in 17.6% of accepted vs 0.5% of rejected abstracts
    (DC:78).
- **Topics.**
  - SPECTER2 embedding of "title [SEP] abstract"; spherical k-means with k = 100 (DC:86-87).
  - Alternative maps differ only in their fitting years: all-years, year-balanced, 2017-20 ("early"), late-only
    (DC:172-183).
  - Prior FM adoption = the share of a topic's papers in year t−1 that are FM papers (DC:153).
- **People.**
  - Newcomer paper and first-time team, as defined in §1 of this file.
  - The 2021 switch from email-based to profile-based author IDs hides pre-2021 histories. This biases incumbency
    towards zero (DC:145-146).
  - Incumbency counts ICLR submissions only (DC:149).
- **Content distance.**
  - As defined in §1 of this file. It reimplements the position module's measure at K = 10 (NOV).
  - It was added during writing, reads no outcome, is unregistered, and is tier E.
- **Twins.** A same-year submission at cosine ≥ 0.70 (DP:78).
- **Protocol:**
  - registration (DC:237);
  - a single frozen run of 18 s (DC:246);
  - held-out tests registered before the held-out data, one-sided (DC:256-258);
  - tiers A-E (DC:25-31);
  - the simulated size failure: 12.6% / 10.0% for H2b/H2c at nominal 5%, reported, not fixed (DC:249-250);
  - "associations within topic and year" (DC:42);
  - "supports the direction, not the size" (DC:47).

### §4 What converged: not the topics, the package (≈800)

#### §4.1 Fashion signals that depend on the ruler (≈330)

**Role.** Show that the topic-level evidence that most resembles fashion depends on how topics are measured, and that
duplication grows with volume. This clears the ground: the herd reading's most visible evidence is the least robust.

**Claim.** On the same papers, with the same embedding and clustering, the fitting window alone changes how
fashion-like the field looks.

**Findings (all tier E):**

| Finding | Values | Source |
|---|---|---|
| **Emerging topics** | 29 on the all-years map vs 8 on the 2017-20 map. Share of 2024-26 papers in emerging topics: 40.9% vs 22.3%. Late-only map: 28; year-balanced map: 16. | DC:176-179; HC |
| Declining topics | 13 (all-years) vs 26 (year-balanced) | DC:176-178; HC |
| Overall reading | "Bracketed, not pinned down" | DC:187 |
| **Life-cycle conclusion flips** | Method share vs maturity: −0.14 [−1.78, +1.49] on the all-years map vs −3.48 [−6.21, −0.76] on the early map for 2021-26 papers. Measurement share: +0.50 vs +3.96 [+1.35, +6.57]. Tier E (counted variants of C). | DC:201-205 |
| **Hindsight makes growth look predictable** | Size predicts 2-year topic growth out of time: R² 0.281 on the hindsight map vs −0.033 on the early map | DC:217 |
| **Topic diversity** peaks in each map's own fitting years | The pooled map's rise is "not a finding" | DC:189-192 |
| **Twins** | The share of papers with a same-year twin rose from 19.5% (2019) to 48.8% (2026), but twins per paper per 1,000 submissions fell from 0.32 to 0.19 | DP:78-79 |

**Implications of the rows:**
- **Diversity.** P2 makes no claim about content diversity. Say so in one clause.
- **Twins.** The rise is volume, not pile-on. The registered reading rule for twins applies (DP:36-39): do not quote
  any acceptance gap for twins here.

**Prior work and wording:**
- `li2025evaluation`, `khanbayov2026topical`, `hall2008studying`, `klinger2020narrowing`, `dedehayir2016hype` (hype
  shapes do not replicate reliably; FW:197-204).
- Keep "the maps also differ in fitting corpus, so the gap cannot be attributed to hindsight alone" (DC:229).
- The early map cannot represent topics born after 2020.

**Transition.** The substrate label is assigned per paper and needs no map.

#### §4.2 The package (≈470)

**Role.** The core result. The convergence that survives every check sits in the substrate. It is cumulative, it
nears saturation inside adopting topics, and it displaces the craft it replaces.

**Findings:**

| Finding | Values | Tier | Source |
|---|---|---|---|
| FM share by year, 2017 → 2026 | 0.3, 0.0, 0.5, 3.3, 4.2, 5.4, 10.6, 26.7, 42.3, 54.4%: rising every year since 2018. This differs from the 17 of 68 keywords that rose and fell. | E | DC:168; DP:81 |
| FM share in topics with ≥ 50% prior adoption, 2026 | 87.8% of 7,516 papers | E | DP:77; FFS |
| New-architecture share | 24.5% → 7.5% | E | DC:169 |
| **H1d** | **−7.98 pp for 0 → 100% prior FM share [−12.14, −3.82]** in discovery. **−11.0 [−18.1, −3.9] held-out** (n 10,978; one-sided p 0.0013). 9/9 counted variants (−5.4 to −15.2). Both hindsight variants pass. Base rate 9.2%. | A | DC:271, 364, 274 |

**How to read H1d:**
- In plain terms: "a topic at 50% adoption has about a third fewer new-architecture papers than a topic at 10%"
  (DC:276-277).
- Direction, not size: held-out MDE80 is 12.0 against a discovery effect of 8.0 (DC:380).
- The weakest held-out variant is −5.4 (p 0.24) (DC:278).

**Optional supporting row (tier E; check the specification before quoting).**
- In the outcome-free twin model, FM papers are more often twinned: +11.0 pp [+8.0, +13.9] (FH, `fm` row)
  **[read here]**. Papers built on one substrate resemble one another.
- Caveat: shared vocabulary ("large language model") raises SPECTER2 similarity mechanically.
- The model's fixed-effects structure is not documented in the dossiers.

**Limits, stated in this section:**
- **H1e: no detectable shift towards empirical or evaluation papers with adoption.** −0.63 [−3.64, +2.38] (C;
  DC:272). The field-wide rise in measurement papers (2.6% → 11.1%; DC:167) is therefore *not* tied to adoption within
  topics. The package's within-topic signature is displacement of new architectures, nothing more.
- **H1a-c life cycles** are not supported on the main map (C).
- **Reverse causality is possible.** Lagged adoption fixes the timing only (DC:283-284).
- **"Adapter on an LLM" is labelled method**, not new architecture.
- **H1d cannot by itself separate the three rival readings:**
  - a package bandwagon (Fujimura);
  - lock-in (Arthur; Hooker);
  - efficient choice (Sutton).

  Hence the next section: the entry layer is where herd and package part ways.

**Figure.** Figure 2 goes here.

### §5 Who carries the package, and who carries divergence (≈680)

**Role.** This section does the discriminating. Herding predicts that entrants imitate (follow-on work, content close
to existing work, near-duplicates, the fastest adoption of trends). The package account, through absorptive capacity,
predicts that entrants bring their own contributions and that record-holders adopt the package first.

**Claim.** Entrants carry the divergence and record-holders carry the package, the reverse of what herding predicts.

**Findings, in the order to write them:**

**1. The registered reversal (A).**
- **Method papers:** newcomer papers +3.71 pp [+2.61, +4.80] in discovery; **+3.60 [+1.48, +5.71] held-out**
  (n 10,718; one-sided p 0.0007).
- **Benchmark/dataset/evaluation papers:** −1.70 [−2.46, −0.93]; **−2.10 [−3.35, −0.85] held-out** (one-sided
  p 0.0005).
- Robustness:
  - all 10 counted variants agree;
  - both hindsight variants pass;
  - two-way clustering agrees.
- Sources: DC:296-297, 365-366.
- Say that our registered herding prediction had the opposite sign.

**2. Qualifiers for the reversal:**
- **Size failure.** p-values are approximate under the cross-map structure (simulated size 10-12%), but t = 6.7 and
  −4.4 are large relative to the inflation factors of 1.31 / 1.22 (DC:311-312).
- **The measurement gap is partly team composition.** With log team size, H2c′ shrinks to −0.54 [−1.11, +0.04],
  p 0.07; on held-out papers it is −0.98. H2b′ is unchanged at +3.92 (DC:301, 308).
- **By era (exploratory, D):**
  - Method: +5.5 (2019-20), +3.4 (2021-23), +3.6 (2024-26).
  - Measurement: −2.0 in 2024-26 only (DC:305-306).
  - Entrants kept writing method papers through the FM era.
- **Scale of entry.** Newcomer papers are 72.9% of papers (DC:151), consistent with `movva2024topics`.

**3. Content distance (E, new; NOV).**

| Specification | Gap, newcomer minus incumbent (percentile points) | N |
|---|---|---|
| **Main: within topic × year cells, CR1 errors clustered by topic** | **+5.90 [+4.95, +6.85]** | 42,325 (100 topics) |
| Raw means | 51.4 vs 46.1 | |
| Method papers only | +5.24 [+4.16, +6.31] | 31,764 |
| With team-size, class and FM controls | +5.76 [+4.82, +6.70] | |
| Raw cosine ×100 | +1.35 [+1.16, +1.55], i.e. 0.22 within-cell SD | |
| Era 2019-22 | +4.95 [+2.32, +7.58] | 8,327 |
| Era 2023-26 | +6.01 [+5.03, +6.98] | 33,998 |
| Difference between eras | +1.06 [−1.64, +3.75], p 0.44 | |
| Sensitivities | +5.81 to +6.63 | |
| By year | Positive in 2020 and 2022-2026. 2019: +1.26 (p 0.70). 2021 rests on about 11 incumbent papers. | |

The era rows give the key sentence: "the entrant-incumbent content gap was no smaller in 2023-26, when FM share ran
from 10.6% to 54.4%, than in 2019-22".

**Reading:**
- Two readings are possible:
  - entrants bring content from elsewhere;
  - incumbents continue their own earlier work, which stays in the comparison set (NOV caveat 3).
- **Both contradict the herding prediction** that entrants imitate what already exists.
- Never call it novelty or originality. It is distance in SPECTER2 space, and vocabulary from other fields may
  contribute.

**4. Near-duplicates (E).** Newcomer papers are less often twinned: −3.9 pp [−5.0, −2.7]. First-time teams: −0.3,
n.s. (DP:275; FH).

**5. Who takes up the package (E).**
- First-time teams write 26.3% of RQ2 papers (FH `mean`) **[read here]**.
- Compared with returning topic newcomers, they write FM papers less often:

  | Prior FM adoption of the topic | Gap (pp) | Note |
  |---|---|---|
  | 0-5% | −1.0 | p 0.08 |
  | 5-15% | −4.6 [−6.6, −2.6] | |
  | 15-30% | −9.0 [−13.3, −4.6] | |
  | 30-50% | −14.7 [−19.8, −9.6] | |
  | ≥ 50% | −2.0 | p 0.14 |

  Sources: DP:360-362; FE. 33,993 submissions, 2023-26.
- **Topic newcomers who already have an ICLR record do not differ detectably from incumbents in any bin:** +1.1
  (p 0.06), −0.4 (p 0.73), −2.6 (p 0.11), +2.9 (p 0.31), −1.0 (p 0.10) (FE, "topic newcomer (vs incumbent)" rows)
  **[read here]**.
- **Reading:**
  - The package travels with an ICLR record, not with topic incumbency, and not with the least-informed entrants.
  - That is the pattern absorptive capacity predicts (`cohen1990absorptive`). It is the opposite of what mimetic
    isomorphism predicts for actors facing the most uncertainty (`dimaggio1983iron`, TA:220-228).
  - The gap closes at saturation: the ≥ 50% bin is n.s. Use "less often while the package spreads", not "never".

**6. Trending keywords (E).**
- First-time teams use Emerging (young, rising) keywords less often: 16.7% vs 25.0%; −3.7 [−5.1, −2.3]; q 6e-6.
- They use Cooling keywords +2.4 and Mainstream keywords +2.3 more often.
- There is no team-size control (DP:315-317; FPS).

**7. What stays untested: flocking.**
- H2a: −0.73 [−2.68, +1.22]. It fails the hindsight check (C; DC:295).
- Newcomer × hot topic: −0.4 / −0.6, n.s. (E5; DC:307).
- Scope "not herded" accordingly: entrants do not write the follow-on work, near-duplicates or early package papers
  that herding predicts. Whether they flock to hot topics is untested.
- `borjas2015cognitive` may be cited as context only (TA:474-485).

**Pairing.** "A randomised trial found no herding detected among reviewers at ICML (Stelmakh et al., 2023); among
authors, topic entrants do not write the follow-on work herding predicts."

**Figure.** Figure 4 goes here.

### §6 What review pays for during a package shift (≈520)

**Role.** This is the third expansion. The section answers one question: **does review amplify the convergence by
paying for popularity, or does it treat the package like a tool whose users are judged on competence?** Candidate 1's
results all live here.

**Claim.** We detect no premium for following the crowd. What goes with acceptance is the package, which shows no sign
of a fading fad (D), and a team's record (B). Fashion-like timing appears, weakly, only in keyword waves.

**1. Popularity is not detectably rewarded.**
- **Crowding (H3a):** −1.68 [−3.68, +0.32]; held-out −1.51 [−5.20, +2.19]; MDE80 4.8 (C; DC:324, 367).
  - Say "uninformative; no detectable premium", never "no effect" (DC:332).
- **Branded "NAME: subtitle" titles:**
  - Their share rose from 7-14% (2017) to 37-49% (2026), depending on the definition (E\*, DP:106-125).
  - Accepted papers carry them at the submitted rate: ratio 1.02 (D\*; earlier exploratory, not re-run; DP:133).
- **Topic acceptance edges regress:** b 0.38 [0.18, 0.58] in discovery; **0.60 [0.32, 0.88] held-out** (B; DC:376).
  - The EB-shrunk premia beat zero (D0, B; DC:377) — appendix.
  - Keyword units give no detectable persistence: 0.16 [−0.34, 0.66], unregistered (DP:52-53).
  - Wording: topic differences are documented (Wang 2023; Xu 2026); our addition is the regression out of sample.
- **Unrewarded bandwagons are not ruled out** (`abrahamson1993institutional`). Say so.

**2. The package is judged like a tool, not like a fad (exploratory, D).**
- FM papers are accepted more often: +4.62 [+2.79, +6.44] (DC:342).
- The premium does not detectably change as adoption rises: +0.19 [−0.96, +1.34] pp per logit unit (DP:356). A fad
  premium would be expected to fade as adoption rises, as in the downswing of a management fashion
  (`abrahamson1999management`) or adaptive emulation, where late adopters do not gain (`strang2001search`).
- The displaced craft is not penalised: new-architecture papers are accepted relatively more often where prior FM
  adoption is high, +8.3 [+1.3, +15.4] (D; DC:349).
- Caveat: the FM label is applied to partly camera-ready text (DC:78; DP:362). Power against a planted fade was only
  about 60-70% (shortlist, finding 3).

**3. Fashion-like timing appears, weakly, in keyword waves, not in the package.**
- A1, young rising vs old flat keywords: +2.67 in discovery; held-out +3.25 [−0.18, +6.69], one-sided p 0.031 (B
  weak; the CI includes 0; DC:375).
- PH6, a keyword's gap after vs up to its peak: −5.7 in discovery (not a test); held-out −5.2 [−11.1, +0.7], one-sided
  p 0.043; −1.7 (p 0.33) without the six keywords inspected first (B weak; DP:389-397).
- Federated learning, the vivid fad case, is "not confirmed": −11.3 in discovery, −4.9 [−15.4, +5.7] held-out, and
  the trend has the opposite sign (D/C; DC:368-369). One clause here; details in the appendix.
- Define "early" as early in a keyword's wave, not early in the submission window (`jung2025what`).

**4. Records go with acceptance (B).** These are the same records that §5 showed carry the package.

| Result | Discovery | Held-out | Tier | Source |
|---|---|---|---|---|
| Far jump from the team's own ICLR record | −5.44 [−7.10, −3.78] | −6.09 [−9.32, −2.86] | B | DC:370 |
| Within-author closeness, per +0.1 cosine | +0.55 | +1.06 [+0.23, +1.89] | B | DC:372 |
| One topic insider vs none | +3.42 | +3.88 [+0.28, +7.47] | B | DC:374 |
| Newcomer acceptance gap | −10.2 [−11.8, −8.7]; mostly who writes the paper: −3.1 [−4.5, −1.6] within authors, and −1.4 for the same author entering a new topic | — | D | DC:343; DP:178-179 |

**Rival readings.** State them; they cannot be separated here:
- expertise (absorptive capacity);
- evaluator conservatism;
- visible prestige (`ibrahim2026bias`).

**Wording:**
- Hill et al. (2025): "we observe the decision itself".
- Boudreau et al.'s distance is a different construct (VP:330-337).
- No advice.

**One clause on field content distance at the gate.** The least-novel-fifth penalty did not replicate (P1b: −3.27 in
discovery, −0.13 held-out; C; DC:371). So §5's content-distance profile carries no gate claim.

### §7 Discussion (≈330)

**Role.** Return to the three conversations, and state the tension and the limits of the frame.

1. **Homogenisation without herding.** For ML's self-critique, claims of homogenisation need to say which layer they
   measure:
   - **at ICLR, the substrate:** the evidence is A and E;
   - **the people and their contributions:** no evidence of herding of the testable kinds.

   This describes measurement; it is not advice.
2. **Bandwagon theory.** Package and herd come apart.
   - The package spreads first through record-holders, the absorptive-capacity order. That qualifies Fujimura's
     "do-able for many".
   - Imitation among record-holders is not excluded (`abrahamson1993institutional`).
3. **Field histories.**
   - The robust convergence signal is per paper.
   - The fragile one is the topic map.
   - The 29-vs-8 check costs one refit. State this as a measurement fact, not an instruction.
4. **Tension and long-run costs:**
   - Bao and Li (2025) find persistence went with lower *impact* in the previous shift, while continuity goes with
     *acceptance* here (B). The gate and the citation record need not reward the same thing; our data cannot test this
     (VP:134-136).
   - Long-run costs of continuity (`march1991exploration`, `rzhetsky2015choosing`) are untested.

### §8 Conclusion (≈100)

Restate the short form, "converged in its tools, not in its people". Name the three layers with their tiers. End on the
scope: one venue; associations.

### Limitations (outside the word count)

1. **One venue.** The held-out set is a split-sample replication within the same ICLR years: it shares reviewers,
   authors and topic-year cells (DC:43-45, 56).
2. **Associations only.** Reverse causality is possible for H1d.
3. **LLM labels, not human labels.** The FM label is applied to partly camera-ready text, and held-out abstracts are
   post-decision.
4. **Incumbency counts ICLR submissions only.** The 2021 ID switch biases incumbency towards zero.
5. **Content distance** was added during writing and is unregistered. It is not originality, and it may partly
   reflect incumbents' self-continuation.
6. **Untested:** flocking (H2a C). Unrewarded bandwagons are not excluded.
7. **Hindsight maps** also differ in fitting corpus. There is no paired test for R².
8. **Size failure** for the main H2b/H2c test.
9. **Within-family Holm only** for the secondary held-out tests. Supported tests that were underpowered at the
   discovery effect confirm direction, not size.

### Placement map: every major finding has a place

| Finding | Where | Role in P2 | Tier |
|---|---|---|---|
| F1 Field waves and FM displacement | §4.2 (core); §1 hook; Fig 2; Table rows S1-S3 | The location of the convergence | E; H1d A |
| F2 Hindsight measurement | §4.1 (core); Fig 3; rows M1-M3 | The most fashion-like signals are the least robust | E |
| F3 Newcomers bring methods, not benchmarks | §5 (core); Fig 4A; rows P1-P2 | Entrants carry divergence (registered reversal) | A (reversed) |
| F4 First-time teams are not trend-chasers | §5 (core, promoted from Candidate 1's "support"); Fig 4C; rows P5-P6 | The package travels with records | E |
| **N: newcomer content distance (new)** | §5 (core support); Fig 4B; row P3 | Divergence in content, not only type | E (added in writing) |
| F11 Twins as volume | §4.1 (support); §5 (newcomers less twinned); rows M3, P4 | No pile-on per pair | E; P2's acceptance gap D (appendix) |
| F5 Crowding and branding not rewarded | §6.1 (support); rows G1-G2 | Review does not pay for popularity | C; E\*/D\* |
| F9 Topic edges shrink | §6.1 (support); row G3 | Outcome imitation would chase regressing signals | B |
| F10 FM premium; new architectures against the tide | §6.2 (support); row G4 | A package premium that does not fade; no penalty for the displaced craft | D |
| F6 Timing | §6.3 (support, weak); row G5; FL in the appendix | Fashion-like timing only in keyword waves | B weak; FL D/C |
| F7 Anchoring | §6.4 (support); row G6 | Records favoured at the gate, matching §5's adoption order | B |
| F8 Newcomer gap mostly composition | §6.4, one sentence; full detail in the appendix | Who writes, not what | D |
| H2a flocking | §5.7 (limit); row P7 | Scope of "not herded" | C |
| H1e, H1a-c | §4.2 (limit); row S3 | The package's within-topic signature is displacement only | C |

**Relegated to the appendix, with reasons:**

| Item | Tier | Reason |
|---|---|---|
| FL detail (PH4, H4-FL) | D/C | Vivid but not confirmed. A single-case fad narrative is what Strang and Macy warn about. |
| P1a, P1b, P7 (field novelty at the gate) | D/C | Not replicated. Does not bear on substrate vs people. One clause in §6. |
| PH1 newcomer correlates; PH2 team-size gradient | D | Composition detail. PH2 is cited as the H2c′ caveat. |
| E3 withdrawal after review; E10 acceptance by class | D | Gate detail outside the question. E10 shows that the gate does not favour the method type. |
| Insider per-head decomposition; E2 near-closeness; far-jump and insider × hot interactions | D | Quoting rules; null and uninformative interactions (DP:40-41, 291-296, 246) |
| Keyword winner's curse; EB D0 | D/E; B | Supports §6.1 but adds length |
| Full held-out table (DC:364-378); pooled re-run ("confirms nothing") | — | Reference |
| Content-distance sensitivity and by-year table (NOV) | E | Reference |
| Title-style lag of returning first authors; LLM-favoured title verbs | E\*, not re-verified (DP:134-135) | Dropped, not relegated |

---

## 6. Main-text table: Table 1, the scorecard

**Caption.**
> Where did ICLR converge? Predictions of a herding account and a package account, and what we observe. All rows are
> associations within topic and year unless noted. Units are pp of probability or share; content distance is in
> percentile points. Discovery estimates have two-sided 95% intervals; held-out tests are one-sided, so a supported
> test can have an interval that includes 0.
>
> Tiers:
> - **A**: registered and replicated on held-out papers;
> - **B**: post hoc in discovery, declared before a held-out test that supported it;
> - **C**: registered, inconclusive or not supported;
> - **D**: discovery only;
> - **E**: descriptive, no acceptance outcome;
> - **E\*/D\***: earlier exploratory title analysis (E\* re-verified; D\* not re-run).
>
> "Reading": P = fits the package account; ¬H = against the herding account; M = depends on measurement; U =
> untested or uninformative.

**Layout.** `table*`, small font, columns: Contrast | Herding predicts | Package predicts | Discovery | Held-out | Tier |
Reading. Four row blocks, one per layer.

### I. Substrate: what papers build on

| # | Contrast | Herding predicts | Package predicts | Discovery | Held-out | Tier | Reading |
|---|---|---|---|---|---|---|---|
| S1 | FM share of submissions, 2017 → 2026 | a wave that rises and falls, like the 17 of 68 keywords in Fig. 1 | cumulative rise | 0.3% → 54.4%, rising every year since 2018; 87.8% of 2026 papers in topics at ≥ 50% prior adoption | — | E | P |
| S2 | Prior FM adoption (0 → 100%) → new-architecture paper | — | displacement of the replaced craft | −8.0 [−12.1, −3.8] | −11.0 [−18.1, −3.9] | A | P (also fits lock-in or efficient choice) |
| S3 | Prior FM adoption → empirical or evaluation paper | — | a shift to adapting and evaluating | −0.6 [−3.6, +2.4] | not tested | C | U |

### II. Measurement: does the fashion survive the ruler?

| # | Contrast | Herding predicts | Package predicts | Discovery | Held-out | Tier | Reading |
|---|---|---|---|---|---|---|---|
| M1 | Emerging topics, same papers and model: all-years map vs 2017-20 map | many, whatever the map | — | 29 vs 8 (41% vs 22% of 2024-26 papers) | — | E | M |
| M2 | Trend conclusions from maps: maturity → method; maturity → measurement; size → 2-year growth (R²) | — | — | All-years map: −0.1 / +0.5. Early map, 2021-26 papers: −3.5 [−6.2, −0.8] / +4.0 [+1.4, +6.6]. R²: 0.28 (hindsight map) vs −0.03 (early map). | — | E | M |
| M3 | Same-year twins: share of papers; twins per paper per 1,000 submissions, 2019 → 2026 | the per-pair rate rises as people pile on | volume: the share rises, the per-pair rate does not | 19.5% → 48.8%; 0.32 → 0.19 | — | E | ¬H |

### III. People: who carries what

| # | Contrast | Herding predicts | Package predicts | Discovery | Held-out | Tier | Reading |
|---|---|---|---|---|---|---|---|
| P1 | Newcomer paper → method paper | fewer (registered H2b) | more | +3.7 [+2.6, +4.8] | +3.6 [+1.5, +5.7] | A (reversed registered prediction) | ¬H |
| P2 | Newcomer paper → benchmark, dataset or evaluation paper | more (registered H2c) | fewer | −1.7 [−2.5, −0.9] | −2.1 [−3.4, −0.9] | A (reversed) | ¬H (partly team size) |
| P3 | Newcomer paper → content distance from earlier ICLR work | lower | higher | +5.9 [+4.9, +6.8]; method papers only +5.2 [+4.2, +6.3] | — | E | ¬H |
| P4 | Newcomer paper → has a same-year twin | more | — | −3.9 [−5.0, −2.7] | — | E | ¬H |
| P5 | FM paper: first-time team vs returning topic newcomer (topics at 5-15 / 15-30 / 30-50% adoption); topic newcomer with an ICLR record vs incumbent (all bins) | entrants adopt the trend fastest | record-holders adopt first | −4.6 / −9.0 / −14.7 (n.s. at 0-5% and ≥ 50%); −2.6 to +2.9, all n.s. | — | E | P |
| P6 | First-time team → Emerging (young, rising) keyword | more | — | −3.7 (16.7% vs 25.0%) | — | E | ¬H |
| P7 | Hot topic → share of papers with an incumbent author | lower (entrants flock) | — | −0.7 [−2.7, +1.2]; fails the hindsight check | — | C | U |

### IV. Gate: what review pays for

| # | Contrast | Herding predicts | Package predicts | Discovery | Held-out | Tier | Reading |
|---|---|---|---|---|---|---|---|
| G1 | Topic crowding → acceptance (per log unit) | premium, if imitation is rewarded | no premium for popularity | −1.7 [−3.7, +0.3] | −1.5 [−5.2, +2.2] | C | U: no detectable premium |
| G2 | Branded "NAME: subtitle" title: share 2017 → 2026; accepted ÷ all ratio | premium | — | 7-14% → 37-49%; ratio 1.02 | — | E\*/D\* | no detectable premium |
| G3 | Topic acceptance edge, 2018-22 → 2024-26 (slope b) | edges persist (b ≈ 1) | — | 0.38 [0.18, 0.58] | 0.60 [0.32, 0.88] | B | edges regress |
| G4 | FM paper → acceptance; change per logit unit of adoption; new architecture × prior FM adoption | a fad premium fades; the displaced craft is penalised | stable premium | +4.6 [+2.8, +6.4]; +0.2 [−1.0, +1.3]; +8.3 [+1.3, +15.4] | — | D | P (camera-ready caveat) |
| G5 | Young rising vs old flat keyword; keyword gap after vs up to its peak | late riders do as well as early ones | — | +2.7 [+0.8, +4.6]; −5.7 [−8.5, −2.9] (not a test) | +3.3 [−0.2, +6.7]; −5.2 [−11.1, +0.7] (−1.7 without the six inspected keywords) | B (weak) | early arrival weakly favoured, in keyword fashions only |
| G6 | Far jump from own record; within-author closeness (per +0.1 cosine); one topic insider vs none | — | records matter | −5.4 [−7.1, −3.8]; +0.55 [+0.21, +0.90]; +3.4 [+1.2, +5.7] | −6.1 [−9.3, −2.9]; +1.06 [+0.23, +1.89]; +3.9 [+0.3, +7.5] | B | records favoured; mechanism open |

**Row sources.**

| Row | Sources |
|---|---|
| S1 | DC:163, 168; DP:77, 81 |
| S2 | DC:271, 364 |
| S3 | DC:272 |
| M1 | DC:176-179 |
| M2 | DC:201-205, 217 |
| M3 | DP:78-79 |
| P1, P2 | DC:296-297, 365-366; P2 team-size caveat DC:301, 308 |
| P3 | NOV `main_pct`, `method_only_pct` |
| P4 | DP:275 |
| P5 | DP:360-362; FE **[read here]** |
| P6 | DP:315; FPS |
| P7 | DC:295 |
| G1 | DC:324, 367 |
| G2 | DP:106-125, 133 |
| G3 | DC:376 |
| G4 | DC:342, 349; DP:356 |
| G5 | DC:375, 378; DP:389-397 |
| G6 | DC:370, 372, 374 |

**Rules for the table:**
- Do not compare effect sizes across rows (DC:428). Rows differ in module, population, years and unit.
- Keep the empty cells in the prediction columns. They are honest: neither account predicts every row.

**Appendix Table A1.** The full held-out table (DC:364-378), with FL, P1b, P7 and EB D0, plus the D-tier rows
relegated in §5.

---

## 7. Figure plan (at most four)

### Figure 1 (exists): keyword turnover

- **File:** `/home/user/cloud-research/research/fashion/paper/figs/fig1_waves.pdf`.
- **Data:** discovery keyword shares from `make_figures.py`, which is outcome-free.
- **Message in P2:** fashions turn over at the keyword level. GANs, adversarial attacks, meta-learning, GNNs,
  federated learning and self-supervised learning rose and fell, while diffusion models and LLMs rose. This is the
  layer where the field looks most like fashion.
- **New caption:** "Keyword waves at ICLR, 2018-2026 (share of submissions; peak marked). 17 of 68 frequent keywords
  rose and fell (§4.1). Compare the package in Figure 2, which has risen every year since 2018."
- **Placement:** §1.
- No change to the file is needed.

### Figure 2 (new): the package accumulates and displaces

- **Message:** the convergence is in the substrate. It is cumulative and map-free, and inside topics it goes with
  fewer new architectures.
- **Panel (a):** FM share and new-architecture share by year, 2017-2026.
  - Source: `research/topics/output/paper_contributions.csv.gz` (columns `year`, `primary_type`, `foundation_model`;
    outcome-free).
  - The presentation already draws it: `presentation/make_figures.py`, `fm_trend()` → `presentation/figs/fm_trend.pdf`.
  - Optionally add the 2026 FM share by prior-adoption bin (5.6% at 0-5% → 87.8% at ≥ 50%) from
    `output/posthoc/ph5_fmwave/free_fm_share.csv`.
- **Panel (b):** the H1d dose-response: new-architecture share by prior FM adoption with topic and year effects
  removed, annotated with the discovery and held-out slopes.
  - Sources: the committed E6 figure `output/figures/F4_dose_response.pdf` (H1d panel); the estimates in
    `output/rq1_results.csv` and `output_pooled/confirmation_run/summary.json`.
  - Prior adoption can be recomputed outcome-free from `paper_contributions.csv.gz` and
    `topics/output/topic_assignments.csv.gz`.
- **Placement:** §4.2.

### Figure 3 (new, single column): same papers, different rulers

- **Message:** topic-level fashion signals depend on the fitting window; duplication grows with volume, not per pair.
- **Panel (a):** emerging-topic counts for the six maps (all-years 29, seed refit 28, late-only 28, year-balanced 16,
  middle-era 10, early 8), with the share of 2024-26 papers in emerging topics on a second axis or as labels (40.9% …
  22.3%).
  - Source: `research/topics/output/hindsight_check.json`.
  - The presentation already draws `hindsight_emerging.pdf`.
- **Panel (b):** share of papers with a same-year twin (19.5% → 48.8%) and twins per paper per 1,000 submissions
  (0.32 → 0.19), 2019-2026.
  - Source: `output/posthoc/ph5_position/free_twin_share.csv`, using the `all` group: `any_twin`, `twins`, `papers`.
  - The per-1,000 normalisation is derived; the committed `PH5_position_twin_share.pdf` shows the raw share.
- **Placement:** §4.1.

### Figure 4 (new): who carries the package, and who carries divergence

- **Message:** entrants diverge in contribution type and content, and lag on the package; record-holders carry it.
- **Panel (a), registered:** H2b′ (method) and H2c′ (measurement), discovery and held-out estimates with CIs.
  - Sources: `output/frozen_run/rq2_results.csv`; `output_pooled/confirmation_run/summary.json`.
  - The presentation's `newcomers.pdf` already draws a version.
- **Panel (b), outcome-free profile (tier E):** three rows, each labelled with its own N and unit:
  - content distance: +5.90 percentile points, with the two era estimates;
  - has a same-year twin: −3.9 pp;
  - Emerging keyword (first-time teams): −3.7 pp.
  - Sources:
    - `output/posthoc/ph5_position/free_herding.csv`;
    - `output/posthoc/ph5_kwtiming/free_profile_states.csv`;
    - `paper_ws/output/novelty_newcomer.json`, which **is not a committed output**. Commit the script
      (`paper_ws/scripts/novelty_newcomer.py`) and its outputs to the repository, and check them against the position
      module's cached features (NOV caveat 6), before this row is drawn. Otherwise drop the row and keep it in the
      text.
- **Panel (c), tier E:** the FM-paper gap by prior-adoption bin, two series:
  - first-time team vs returning topic newcomer;
  - topic newcomer vs incumbent.
  - Source: `output/posthoc/ph5_fmwave/free_entry.csv`.
  - The committed module figure `output/posthoc/ph5_fmwave/PH5_fmwave_profiles.pdf` is related.
- **Rules:**
  - Panels (a)-(c) use separate axes.
  - Do not put acceptance estimates in this figure.
- **Placement:** §5.

**No gate figure.** The gate is the third act, and Table 1 carries it. If space allows, appendix figures can reuse
`presentation/figs/far_jump.pdf` and `premia_scatter.pdf`.

---

## 8. The weakest points, and how the text handles them

**1. H1d alone cannot tell a package from a herd, or from lock-in or efficient choice.**
- It is an association, with possible reverse causality.
- It confirms direction, not size (MDE80 12.0 vs 8.0).
- The weakest held-out variant is −5.4 (p 0.24).

*Handling:*
- §4.2 says all of this plainly.
- "Package" is used as a description of where the convergence lies, not as a mechanism.
- The discriminating evidence is placed at entry (§5).
- The thesis claims location ("converged in its tools"), not efficiency.

**2. The people layer leans on tier E.** Content distance, FM adoption lag, Emerging keywords and twins are
descriptive. The content-distance analysis was added during writing and has not been verified against the module's
cached features.

*Handling:*
- §5 opens with the tier-A reversal. The E rows follow as a "consistent profile", each tagged E.
- The text says the content-distance comparison is unregistered, outcome-free and added during writing.
- Before submission, commit the script and outputs and run the cross-check against the position module.

**3. Type is not novelty, and SPECTER2 distance is not originality.** Incumbents' self-continuation may drive part of
the gap. Vocabulary from other fields may also contribute.

*Handling:*
- Name the measure "content distance from earlier ICLR work".
- Give both readings. Note that each contradicts the herding prediction that entrants imitate existing work.
- Never write "entrants are more innovative".

**4. Half of herding is untested: flocking.** H2a is C, and newcomer × hot is n.s.

*Handling:*
- Scope every "not herded" sentence: entrants do not write the follow-on work, near-duplicates or early package
  papers that herding predicts.
- State in §5 and in the Limitations that flocking is untested.
- The title's "Not a Herd" is defended as a claim about where the convergence lies, made in the abstract's last
  sentence.

**5. "The package travels with records" is descriptive and partial.**
- There is no team-size control in the keyword profile.
- The ID switch misclassifies some 2021-22 teams.
- The FM label is an LLM label on partly camera-ready text.
- The gap is n.s. at both ends (0-5%; ≥ 50%).
- The "topic newcomer vs incumbent" rows were read from FE for this story and are not yet in a dossier.

*Handling:*
- Report all five bins.
- Write "less often while the package spreads".
- Make no acceptance link.
- Add the FE rows to the dossier before writing.
- Cite absorptive capacity as "the pattern it predicts", not as a test of it.

**6. H2c′ is partly team composition, and concentrated in 2024-26.**

*Handling:*
- Report −0.54 (p 0.07) and the held-out −0.98 next to H2c′ in §5.
- H2b′ carries the reversal (+3.92 with the control).

**7. Some gate rows can be read as "riding pays".** The FM premium (+4.62, D), the held-out twin row (+3.69,
unregistered) and A1.

*Handling:*
- Under P2 these are not anomalies:
  - a non-fading package premium is what the package account expects;
  - A1 rewards being early in a keyword wave, not following.
- The twin row follows the P2 quoting rule (DP:36-39) and stays in the appendix.
- The camera-ready caveat travels with the FM premium.

**8. The hindsight comparison has a corpus confound.**
- The early map cannot see topics born after 2020.
- There is no paired test for R².

*Handling:*
- Use "bracketed, not pinned down" and "cannot be attributed to hindsight alone" (DC:187, 229).
- P2 needs only the weaker claim: topic-level fashion counts are window-dependent, while the substrate signal needs no
  map and H1d passes both hindsight variants.

**9. "Isn't 'FMs are a package' trivially true?"**

*Handling:*
- The non-trivial claims are about the people and the review gate. Our own registered prediction encoded the herd
  reading and failed.
- The package spreads through record-holders, against the "package invites newcomers" reading of Fujimura.
- Entrant divergence did not shrink in the FM era (+4.95 vs +6.01; difference +1.06 [−1.64, +3.75]).
- Topic-level "fashion" is the measurement-fragile signal.

**10. Weisberg's "herding" means risk-avoiding clustering.** A science-of-science reviewer may say continuity *is*
herding.

*Handling:*
- Define herding at first use as imitation of others' current choices (TA:48-52).
- Note the blended usage (`weisberg2013modeling`; TA:367-375).
- Show the continuity results in §6 under their own name, "records".

**11. Generalisation and design limits:**
- one venue;
- a split-sample held-out set;
- LLM labels;
- ICLR-only incumbency with the 2021 ID switch;
- the H2b/H2c size failure (12.6% / 10.0%);
- within-family Holm for the secondary tests.

*Handling:* the Limitations section, in the dossiers' wording. No "first confirmatory design" claim (Ibrahim 2026).

**12. Novelty pressure from close neighbours:**
- Bao and Li (2025): the closeness measure and an earlier-shift displacement description;
- Movva et al. (2024): entrants are numerous;
- Gururaja et al. (2023): the exploit phase;
- Huang (2026): topic initiators at ICLR.

*Handling:*
- The novelty sentence claims only the combination: a registered, held-out, topic-level displacement test plus entry
  evidence in the same complete population, qualified "to our knowledge, among the works we checked".
- Each neighbour is cited for what it did (2.2).

---

## Appendix to this design: wording guardrails specific to P2

**Language:**
- Say "goes with", "is associated with" or "fewer … where adoption is higher". Never "crowds out", "causes",
  "displaces" (as a verb with FM as the subject), "revolution" or "choose".
- "Displacement" is allowed as the name of the H1d pattern, defined as an association.
- No advice to authors, reviewers or venues (DC:427; DP:298).

**Scope:**
- "Not a herd" is always scoped to the herding predictions we could test. Flocking is untested.
- "Homogenisation" only in the substrate sense. Do not claim content homogenisation or diversity trends; they are
  map-dependent.

**Tiers and quoting rules:**
- Held-out results are "a pre-registered out-of-sample replication, not a certified untouched holdout". Supported
  held-out tests confirm direction, not size.
- Underpowered nulls are "uninformative", not "no effect". For crowding, say "no detectable premium".
- Every number carries its tier. E\* and D\* are "earlier exploratory".
- The quoting rules travel with their findings:
  - FL is "not confirmed";
  - A1's interval includes 0;
  - PH6 leans on six inspected keywords;
  - P1b "did not replicate";
  - the P2 twin rule.

**Prior work:**
- No "first" claim without "to our knowledge, among the works we checked".
- Never the first pivot penalty at the gate (Hill 2025).
- Never the first topic-acceptance result (Wang 2023; Xu 2026).
- Never the first registered ICLR test (Ibrahim 2026).
- Cite Fujimura 1988, Kitcher 1990, DiMaggio and Powell 1983 (mimetic section) and Scharfstein and Stein 1990 for
  their general arguments only, because their content is secondary (TA:663-676; FW:107).

## Open checks before the writers start

1. Commit `paper_ws/scripts/novelty_newcomer.py` and `paper_ws/output/novelty_newcomer.{json,csv}`.
   - Cross-check against the position module's cached novelty features (NOV caveat 6).
   - Add the content-distance rows to a dossier.
2. Add the FE "topic newcomer (vs incumbent)" rows and the FH first-time share (26.3%) to `dossier_posthoc.md`.
3. Confirm the fixed effects of the FH twin model before quoting the FM-twin row (+11.0), or drop that row.
4. Confirm whether the far-jump cosine uses SPECTER2 before any "as Bao and Li do" wording (VP:496-498). P2 does not
   need this sentence.
5. Note the shortlist source of the power figure for the FM premium fade (about 60-70%): `presentation/shortlist.md`,
   finding 3. Quote it only with that pointer.
