# Closest prior work: verification and novelty wording

Built 2026-11-03 for the ICLR 2017-2026 paper ("Anchored, not herded").

**Scope.** This file resolves:
- landscape.md §3.3, all ten rows;
- the "Open checks" items 3, 4, 5, 6 and 8;
- the named checks in the task;
- 14 fresh searches for (a) author herding at ML/NLP venues and (b) newcomer status or trend timing versus acceptance.

No data file, outcome column or analysis script was opened. Our own numbers are quoted only from `dossier_core.md` (DC) and
`landscape.md`, with line pointers.

## 0. How this was verified (read first)

**Tools.**
- WebFetch could not reach arxiv.org, aclanthology.org, api.openalex.org, api.semanticscholar.org or bytez.com. The
  hosts did not resolve in this session's network allowlist.
- So every check below rests on **WebSearch result pages**: titles, URLs, and snippets or summaries of abstract pages,
  publisher records, PMC, IDEAS/RePEc, ACM DL, OUP and university pages.
- No full text was read.
- To verify the arXiv-only 2026 items properly, arxiv.org must be allowed in the session's network settings.

**Status labels.**

| Label | Meaning |
|---|---|
| **V** | Verified. Authors, title, year and venue were seen in a publisher, index or repository record, consistent across two or more results. |
| **V-arXiv** | Verified as an arXiv preprint. The title, id and author list were seen in arXiv listing metadata via search, but the abstract page was not opened. |
| **P** | Partly verified. One element (author order, issue number or page range) is unresolved. The unresolved element is named. |
| **U** | Unverified. Do not cite. |

**Numbers from other papers.**
- Numbers quoted from these papers come from abstracts or snippets seen in search results.
- Treat them as *reported by the search result*. Re-check them against the PDF before quoting any of them in the paper.
- The safe default is to describe these works qualitatively and not quote their numbers.

---

## 1. Summary table

| # | Item | Status | BibTeX key | Closest to | Effect on our novelty claim |
|---|---|---|---|---|---|
| 1 | Wang, Peng, Zhang & Zhang, "What have we learned from OpenReview?" (arXiv 2103.05885; APWeb-WAIM 2021; *World Wide Web* 2023) | V (journal issue number P) | `wang2023what`, `wang2021what` | G1, F9 | Topic-cluster acceptance differences at ICLR (2017-2020) are **already documented**. Do not claim to be first to show topic differences in acceptance. |
| 2 | Bao & Li, "Persistence Paradox in Dynamic Science" (arXiv 2506.22729, 2025) | V-arXiv | `bao2025persistence` | G2, G3, F7 | They measure **closeness to one's own prior ML papers with SPECTER2** across the deep-learning shift. Outcome is productivity and impact, not acceptance. Narrows G3's "measure" novelty; G3's "gate" novelty stands. |
| 3 | Jung, Pyeon, Heo & Ahn, "What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review" (arXiv 2509.25701; EMNLP 2026 entry seen) | P (author order between arXiv and Anthology unresolved) | `jung2025what` | G1, G6 | The complete ICLR 2017-2025 corpus is already used. Their "earlier submission" is timing within a review cycle, not timing within a research wave. Name it to pre-empt confusion. |
| 4 | Xu et al., "Reviewer Scores Are Not Comparable Across Research Areas in ML Peer Review" (arXiv 2607.27209, 2026) | P (order of the two middle authors conflicts) | `xu2026reviewer` | F9 (premia), G1 | Topic predicts ICLR acceptance at equal scores, 2021-2026. This is a **rival account of topic edges** and prior art for "topics differ at the gate". Our addition is that the edges **regress out of sample**. |
| 5 | Ibrahim, Rahwan & Zaki, "Bias at the Borderline: Who Gets the Benefit of the Doubt in Peer Review?" (arXiv 2607.26280, 2026) | V-arXiv | `ibrahim2026bias` | G7, F7 (insider) | They report a **pre-registered out-of-sample test on the ICLR 2026 cohort**, so G7 must not say "first registered held-out design at an ML venue". Their prestige effect operates through arXiv identifiability, which is a rival reading of the insider premium. |
| 6 | Biliotti, Verginer & Riccaboni, "Breaking New Ground, Reinforcing Old Gaps: Gender Disparities in Access to Emerging Research Frontiers" (arXiv 2404.04707; EUI MWP WP 2026/01) | V-arXiv (year/version P) | `biliotti2024breaking` | G2, F7 | Uses the same topic-specific newcomer definition (no prior COVID-19 papers). Senior field expertise offsets the newcomer disadvantage, a producer-side analogue of the insider premium. Cite as precedent; it does not narrow G2. |
| 7 | Stelmakh, Rastogi, Shah, Singh & Daumé III, "A large scale randomized controlled trial on herding in peer-review discussions" (*PLOS ONE* 2023) | V | `stelmakh2023large` | Conversation 1, F5 | No herding among **reviewers** (ICML 2020 RCT). Sharpens our line: herding is now tested and not found among reviewers (them) or entrants (us). |
| 8 | Vicinanza, Goldberg & Srivastava, *PNAS Nexus* 2023 | V | `vicinanza2023deep` | Conversation 3 | "Prescient ideas from the periphery". The domains are law, politics and business, not science. Context only. |
| 9 | Hill, Yin, Stein, Wang, Wang & Jones, "The pivot penalty in research", *Nature* 2025 | V | `hill2025pivot` | G3, F7 | **Yes: larger pivots have lower publication success.** Preprints from 2015-2018 are published within five years less often, with a monotonic decline and the highest-pivot bin 35% lower. G3 must not claim "first at the publication or acceptance stage". |
| 10 | Boudreau, Guinan, Lakhani & Riedl, *Management Science* 2016 | V | `boudreau2016looking` | G3, Conv. 2 | Direction: **closer is harsher.** Evaluators score proposals closer to their *own* expertise lower, and also score highly novel proposals lower. Their distance is evaluator-to-proposal, not author-to-own-record. |
| 11 | Lipton & Steinhardt, "Troubling Trends in Machine Learning Scholarship" | V | `lipton2019troubling` (Queue), `lipton2018troubling` (arXiv) | Conv. 5 | Bibliographic only (see §3). |
| 12 | Li, Esposito, Groth, Sitruk, Szatmari & Wijnberg, "Evaluation of unsupervised static topic models' emergence detection ability", *PeerJ Computer Science* 2025 | V | `li2025evaluation` | G4 | Evaluates static models' emergence detection. G4's specific claim (same papers, only the fitting window varies) stands, with the wording in §4. |
| 13 | Fischhoff 1975; Kerr 1998 | V | `fischhoff1975hindsight`, `kerr1998harking` | Vocabulary | Safe to cite. |
| 14 | Fresh: Huang, "Catalyst Papers in AI Research: A Landscape on ICLR from 2017 to 2025" (arXiv 2607.05401, 2026) | V-arXiv | `huang2026catalyst` | G2, G6 | Topic *initiators* and bridges at ICLR precede topic growth. They study who starts topics, not entrants' contribution type or acceptance by entry status. |
| 15 | Fresh: Khanbayov & Kurban, "Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evidence and an Early-Warning Signature for Emerging Topics" (arXiv 2606.12828, 2026) | V-arXiv | `khanbayov2026topical` | G4 | A prospective, temporally split emergence predictor on five AI venues. It is close to the "without hindsight" spirit, but does not compare hindsight against no-hindsight maps. Must be cited in G4. |
| 16 | Fresh: Jurgens, "The Future of NLP may not be at NLP Conferences: Scholarly Migration Patterns in Natural Language Processing" (arXiv 2607.02416, 2026) | V-arXiv | `jurgens2026future` | G2 context | Movement of NLP authors to ML venues, with new researchers debuting at ML venues. Context for "newcomers" at ICLR. |
| 17 | Fresh: Kargaran, Nikeghbal, Yang & Ousidhoum, "Insights from the ICLR Peer Review and Rebuttal Process" (arXiv 2511.15462, 2025) | V-arXiv | `kargaran2025insights` | Conv. 6 | Co-reviewer influence on score changes at ICLR 2024-2025. This is reviewer-side conformity in the rebuttal phase, a nuance next to Stelmakh 2023. |
| 18 | Fresh: Schäfermeier, Stumme & Hanika, "Topic space trajectories: A case study on machine learning literature", *Scientometrics* 2021 | V | `schafermeier2021topic` | Conv. 4 | ML topic-trajectory history fitted on published papers. Adds to the "computational histories" list. |
| — | "Who Pays for Open Review? Visible Author Reputation and Its Effect on Ratings" (arXiv 2609.11983) | U (authors not seen) | none | F7 rival | Reputation proxies raise ratings, more steeply under open review (ICLR 2026). Do not cite until the authors are verified. |
| — | Mishkin et al. 2020; "Corporate Disruption..." arXiv 1612.04108 | not searched | none | — | Not needed for the recommended story. |

---

## 2. Item-by-item findings

### 2.1 "What have we learned from OpenReview?" (arXiv 2103.05885)

**Real.** Gang Wang, Qi Peng, Yanfeng Zhang and Mingyang Zhang (Northeastern University, China).

**Versions.**

| Version | Details |
|---|---|
| arXiv | 2103.05885, cs.DL. v1 10 Mar 2021; v4 6 Apr 2021. |
| Conference | APWeb-WAIM 2021 (Springer LNCS), DOI 10.1007/978-3-030-85896-4_6. The LNCS volume and pages were not confirmed. |
| Journal | *World Wide Web* 26: 683-708 (2023; online Nov 2022), DOI 10.1007/s11280-022-01109-z. The Springer page places it in the APWeb-WAIM 2021 topical collection. The issue is given as 2 by one source and 3 by another, so it is omitted. |

**What it measured, as reported by search snippets.**
- **Data:**
  - arXiv/conference version: ICLR 2017-2020, 5,527 submissions and 16,853 reviews.
  - journal version: 11,915 submissions and 41,276 reviews.
  - plus Google Scholar citations and arXiv versions.
- **Findings reported:**
  - arXived submissions had a higher acceptance rate (49.39% vs 32.68%), and earlier arXiv posting went with higher acceptance;
  - topic clusters differ in acceptance, from "Black-Box Adversarial Attacks" 53.33% to "Few-Shot Learning" 10.53%;
  - lower-confidence reviewers give higher scores;
  - confidence, novelty and experimental results dominate review scores.
- These figures are from the arXiv version's snippets. The journal version's figures were not seen.

**Closeness.**
- **G1 and F9.** This is the earliest study we found that ties ICLR topic (cluster) to acceptance.
- It is descriptive: one cross-section of topics, no time dynamics, no entry status, no out-of-sample test.
- It does not touch G2-G5.

**Wording.**
- Background: "Earlier OpenReview studies documented that acceptance rates at ICLR differ across topic clusters
  and that arXiv-posted submissions are accepted more often (Wang et al., 2023)."
- In §6 (F9): "Topic-level acceptance differences at ICLR are known (Wang et al., 2023; Xu et al., 2026); our test
  asks whether a topic's edge in one period persists in the next, and finds that it shrinks (0 < b < 1) on held-out
  papers."
- **Do not write:** "we are the first to relate topic popularity to acceptance at ICLR".

### 2.2 "Persistence Paradox in Dynamic Science" (arXiv 2506.22729)

**Real.** Honglin Bao and Kai Li.
- cs.DL. v1 28 Jun 2025; v2 1 Jul 2025.
- The HTML version carries the subtitle "Evidence from the Deep Learning Revolution". One search summary said "by Honglin Bao" alone, but the arXiv listing snippet gives both authors.
- No peer-reviewed venue was found.

**What it measured, as reported in search snippets.**
- **Cohort:** 5,359 scientists with at least one ICML or NeurIPS paper in 2003-2012, followed over 20 years around the 2012 AlexNet shift.
- **Persistence measure:** for each scientist and year, bootstrapped **SPECTER2** similarity of titles and abstracts to all of their prior ICML/NeurIPS papers.
- **Findings:**
  - persistence goes with productivity but lower citation impact after the shift; adaptivity goes with impact;
  - at field level, moderate persistence dominates output;
  - leading venues increasingly prioritised deep learning, displacing traditional statistical learning;
  - ICLR, NeurIPS and ICML converged in topic emphasis.
- **Caveat:** a third-party review flags survivorship, since the sample is post-2013 survivors.

**Closeness. This is the closest paper on the producer side of an ML paradigm shift.**
- **G3 / F7, measure.** Their persistence measure is essentially our within-author closeness (SPECTER2 similarity to one's own earlier papers). Do not claim the measure as new.
- **G3 / F7, outcome.** Their outcomes are productivity and later citations of *published* papers. Ours is the accept/reject decision on all submissions. G3's "at the gate" claim survives.
- **Direction.** They find persistence penalised in *impact* during a shift. We find continuity goes with *acceptance*. This is a tension worth one sentence in the Discussion, not a contradiction: a different stage, a different shift (2012 versus FMs) and a different period.
- **G2.** They study incumbents' adaptation, not what topic entrants write. G2 stands.
- **G5.** Their "DL displaced statistical learning at the leading venues" is a descriptive displacement claim about the earlier shift. G5's "registered, topic-level, held-out test" stands.

**Wording.**
- "Bao and Li (2025) measure how far ML researchers stayed from their own earlier work across the deep-learning shift,
  using SPECTER2 similarity as we do, and find that persistence went with lower later impact. We ask the complementary
  question at the review gate: on every ICLR submission, closeness to the team's own record goes with acceptance."
- Discussion: "That continuity is rewarded at the gate while, in the previous shift, persistence went with lower later
  impact (Bao and Li, 2025) suggests that the gate and the citation record need not reward the same thing; our data
  cannot test this."

### 2.3 "What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review"

**Real.**
- **arXiv 2509.25701.** Authors as listed: Sangkeun Jung, Goun Pyeon, Inbum Heo, Hyungjin Ahn. Listed under cs.CY. v1 30 Sep 2025; v2 29 Jan 2026.
- **ACL Anthology.** An entry `2026.emnlp-main.1123` with this title appeared in search results, but the page could not be opened.
  - lit_novelty_reward.md records it as "Heo et al.", pp. 25711-25731.
  - The author order in the EMNLP version is **unresolved**, and three searches failed to confirm the EMNLP listing.
- **Recommendation:** cite the arXiv version (`jung2025what`) with the arXiv author order. Switch to the Anthology record only after opening it.

**What it measured.**
- **Data:** ICLR 2017-2025, 28,358 submissions (the complete OpenReview record, by their account).
- **Findings:**
  - the rebuttal stage is the most influential phase; timely, substantive interaction raises acceptance odds;
  - clearer writing, balanced visuals, earlier submission, and resolution of reviewer disagreement correlate with acceptance;
  - "factors beyond scientific novelty" shape outcomes.
- They propose guidelines. The results are associations.

**Closeness.**
- **G1.** The full ICLR submission population is not new as a data source.
- **G6.** "Earlier submission" means timing within a review cycle, not position in a topic's life cycle. A reviewer may conflate it with our "arriving early" (A1, PH6), so name the difference.
- **G2-G5.** No entry status, contribution type or topic dynamics.

**Wording.**
- "Process-level studies of the full ICLR record relate rebuttal engagement, writing and submission timing to
  acceptance (Jung et al., 2025); we study a paper's position in its topic's life and its team's record instead."
- In §6 (A1): "early" means early in a keyword's wave, not early in the submission window.

### 2.4 "Reviewer Scores Are Not Comparable Across Research Areas in ML Peer Review" (arXiv 2607.27209)

**Real.**
- **Authors:** Binyan Xu, Kehuan Zhang, and two middle authors (Xilin Dai, Fan Yang) whose order differs between two search results. The affiliations seen were CUHK and Zhejiang University.
- **BibTeX:** cite as "Xu et al. (2026)"; the BibTeX uses `and others` until the order is checked.

**What it measured.**
- **Data:** ICLR 2021-2026, 50,289 papers, 219 BERTopic topics.
- **Finding:** topic predicts acceptance after controlling for mean score and year. The largest topic-band ratio at the same score is 8×, which the authors call an observed maximum, not typical.
- **Hypotheses examined:** scoring culture, reviewer expertise, subscore reweighting, quality dilution.
- **Mechanism:** topic-specific, only partly overlapping reviewer pools with no equating of score scales.
- **Caveat:** the authors say equal scores need not mean equal latent quality.

**Closeness.**
- **F9 (premia, B).** This is the most direct prior art: persistent topic-level acceptance differences at ICLR over almost our period.
- **Difference from ours.** Our premia test asks whether a topic's edge measured in one window **persists out of sample**, and finds it shrinks (b 0.38 discovery, 0.60 held-out; DC:376), with a positive EB variance D0 (DC:377).
- **Score-scale reading.** Their account (non-comparable score scales) is one mechanism by which edges could exist and partly persist. It does not conflict with regression toward zero.

**Wording.**
- "Topics differ in acceptance at ICLR even at equal reviewer scores (Xu et al., 2026). We find that these edges are
  real but regress: a topic's edge in one period predicts only part of its edge in the next."
- **Do not write** "topic choice is not rewarded". Write "a favoured topic is not a reward that keeps paying in full".

### 2.5 "Bias at the Borderline" (arXiv 2607.26280)

**Real.** Hazem Ibrahim, Talal Rahwan and Yasir Zaki (NYU Abu Dhabi). Submitted 28 Jul 2026. HTML subtitle "Evidence from ICLR".
- One search summary did not confirm the second and third authors. Two others did, including the arXiv listing snippet. Status: V-arXiv.
- A GEM workshop journal-ref seen in one listing belonged to a neighbouring entry, so it is not used.

**What it measured.**
- **Data:** ICLR 2019-2025, 31,711 submissions, 10,416 borderline.
- **Main finding:** at equal reviewer scores, borderline papers with no top-25-institution author are accepted 0.5-1.6 pp less often. The gap arises at the discretionary decision stage.
- **Replication:** it **reappears out of sample in the pre-registered ICLR 2026 cohort**.
- **Identifiability:** the gap is concentrated where a pre-decision arXiv preprint identifies the authors (−3.4 vs −0.2 pp).
- **Outcome test:** a "robust outcome test" across five downstream outcomes, including the "first reject-side outcome test", does not meet its criterion for discrimination.

**Closeness.**
- **G7. Must change.** A pre-registered, out-of-sample ICLR test already exists. Our design is still unusual in combining:
  - sealed outcomes;
  - a single frozen run across many registered hypotheses;
  - a reported size failure;
  - tiered reporting.

  But "first" is out.
- **F7 (insider premium).** This is a rival mechanism. An insider on a team is often an established author whose identity is visible through arXiv. Our insider premium could partly be status visible to the deciders, which fits the open caution in landscape.md about the "insider vs proven-record ambiguity".

**Wording.**
- "Pre-registration of tests on later ICLR cohorts has been used before (Ibrahim et al., 2026); we apply the same logic
  to a science-of-science account, freezing all analyses before a single run and replicating on 11,099 held-out
  papers."
  - The 11,099 figure is from DC:65/72 via landscape G1.
- In §6/Discussion: "Because authors are often identifiable through preprints, and borderline acceptance at ICLR leans
  towards visible prestige (Ibrahim et al., 2026), the insider association may partly reflect visible status rather
  than topic knowledge."

### 2.6 "Breaking New Ground, Reinforcing Old Gaps" (arXiv 2404.04707)

**Real.**
- **Authors:** Carolina Biliotti, Luca Verginer, Massimo Riccaboni.
- **Versions:**
  - arXiv 2404.04707, first posted 2024. An earlier version of this arXiv record was titled "The Uneven Access to COVID-19 Research for Women in Science".
  - Also EUI Max Weber Programme Working Paper 2026/01.
  - The exact version history was not seen.

**What it measured.**
- **Design:**
  - PubMed biomedical papers;
  - COVID-19 as an exogenous shock;
  - name-inferred gender;
  - difference-in-differences.
- **Findings:**
  - COVID-19 papers less often have women as first or last author;
  - the first-author gap is concentrated in **newcomer teams whose lead authors had no prior COVID-19 research**;
  - senior field expertise, and prior collaboration with women newcomers, offset the disadvantage (from the EUI interview).

**Closeness.**
- **Operationalisation.** Same topic-specific incumbent/newcomer split as ours.
- **Outcome and subject.** Authorship position by gender, not contribution type or acceptance.
- **G2.** Not narrowed.
- **Analogy.** Their "expertise on the team offsets newcomer disadvantage" is a useful producer-side analogue of our one-insider association (Teams H1, B; DC:374 per landscape).

**Wording.**
- "Following studies that define newcomers relative to a topic rather than a career (e.g., Biliotti et al., 2024), a
  team is a newcomer to a topic if no author has an earlier ICLR submission in it."

### 2.7 Stelmakh et al., herding in review discussions

**Real.** Ivan Stelmakh, Charvi Rastogi, Nihar B. Shah, Aarti Singh, Hal Daumé III.
- **Journal:** *PLOS ONE* 18(7): e0287443, published 12 Jul 2023, DOI 10.1371/journal.pone.0287443 (PMC10337975).
- **Preprint:** arXiv 2011.15083 (Nov 2020).
- A PMC metadata line naming another person appears to be the academic editor, not an author.

**What it measured.**
- **Design:** RCT inside ICML 2020 review. Borderline papers with reviewer disagreement were randomised to have a positive or a negative reviewer open the discussion.
- **Finding:** no evidence of herding in discussions.
- The sample size seen in one snippet (1,544 papers, 2,797 reviewers) is unverified against the full text, so do not quote it.

**Closeness.**
- **Conversation 1 / F5.** Herding has been tested at an ML venue among **reviewers** and not found.
- We test herding among **authors entering topics**, which is a different population. Together they strengthen "conformity in this field is not well described as herding".

**Wording.**
- "A randomised trial at ICML found no herding among reviewers in discussion (Stelmakh et al., 2023); we ask the
  corresponding question about authors and find that topic entrants do not write the follow-on work herding predicts."
- Kargaran et al. (2025) report that co-reviewers' ratings predict rebuttal-phase score changes at ICLR 2024-2025, so
  write "no herding detected in the RCT", not "reviewers are independent".

### 2.8 Vicinanza, Goldberg & Srivastava 2023

**Real.**
- **Citation:** "A deep-learning model of prescient ideas demonstrates that they emerge from the periphery". *PNAS Nexus* 2(1): pgac275 (Jan 2023).
- **Correction:** PubMed lists a correction notice for Volume 2 Issue 1 of PNAS Nexus (PMID 36744020). Whether it concerns this article was not confirmed.
- **DOI:** not seen. By the OUP pattern it is likely 10.1093/pnasnexus/pgac275, but this is **unverified**, so it is omitted from the BibTeX.

**Measured.**
- **Method:** a BERT-based prescience measure.
- **Domains:** law (state vs federal courts), politics (congressional speeches) and business (firm size).
- **Finding:** prescient ideas come from the periphery.

**Closeness.** Low. It concerns outsiders as sources of new ideas outside science, and supports the "entrants propose" reading (F3) only by analogy.

**Wording.** "Ideas that later prevail often originate at the periphery of a domain (Vicinanza et al., 2023)."

### 2.9 Hill et al. 2025: does it report lower publication success for larger pivots? **Yes.**

**Authors, now verified.** Ryan Hill, Yian Yin, Carolyn Stein, **Xizhao Wang**, Dashun Wang, Benjamin F. Jones.
- The full list appears in the Kellogg/IDEAS/Spotify records.
- **Citation:** *Nature* 642(8069): 999-1006 (online 28 May 2025), DOI 10.1038/s41586-025-09048-1.

**Publication result, from search snippets of the Nature article.**
- **Sample:** preprints from 2015-2018, followed for whether each is published in a journal within five years.
- **Gradient:** publication propensity declines smoothly with pivot size. "Virtually all" of the lowest-pivot working papers are published, against about two-thirds of the highest-pivot ones.
- **Size:** the highest-pivot bin has a 35% lower publication rate (P < 0.001).
- Also reported: lower citation impact, patents from the largest pivots worth 29% less, and a 61% lower top-cited hit rate for COVID-19 pivoters.
- **Mitigator:** a Nature News & Views piece reports a smaller penalty when publishing in a journal the author has used before.
- A snippet said "1.07 million preprints". That count is unverified; do not quote it.

**Closeness.**
- **G3 is narrowed.** The pivot penalty is already shown at the *publication* stage.
- **What remains ours:**
  1. We observe the editorial decision itself on every submission, including withdrawals. Preprint non-publication mixes rejection with authors never submitting.
  2. The decision is made under double-blind review.
  3. It is at a single ML venue during the FM shift.
  4. It is paired with the insider association.
  5. It is replicated on held-out papers.

**Wording.**
- "Hill et al. (2025) show that larger pivots are cited less and are less often published. We observe the decision
  itself: on every ICLR submission, papers far from the team's own record are accepted less often, and the association
  holds on held-out papers."
- **Never write:** "first evidence of a pivot penalty at acceptance". Write "at the review decision of an ML venue,
  observed directly".

### 2.10 Boudreau et al. 2016: direction of the intellectual-distance effect

**Resolved: closer is harsher.**
- Abstract wording (via search): "evaluators systematically give lower scores to research proposals that are closer to their own areas of expertise and to those that are highly novel."
- **Design:** randomised evaluator assignment in a grant process at a leading research university, with 2,130 evaluator-proposal pairs.
- **Reading:** the authors read the result as boundedly rational evaluation of new ideas, not noise or conflicts of interest.
- **Size:** distance variation accounts for about 1.1 points on a 10-point scale.
- **Citation:** *Management Science* 62(10): 2765-2783, DOI 10.1287/mnsc.2015.2285.

So lit_novelty_reward.md (NR:223-225) is correct, and the caution in lit_outsiders.md (OUT:122) can be closed.

**Closeness.**
- Their "intellectual distance" is between the **evaluator and the proposal**. Ours is between the **paper and its own authors' past work**.
- Do not present Boudreau et al. as showing that "distance is penalised" in our sense. They show that *expert* evaluators are harsher, which, if anything, is the opposite intuition to an insider premium.
- The novelty penalty in the right tail is the relevant part for Conversation 2.

**Wording.**
- "In a randomised grant evaluation, reviewers scored proposals closer to their own expertise, and highly novel
  proposals, lower (Boudreau et al., 2016). Our distance is different: it is the distance of a submission from its
  own authors' record."

### 2.11 Lipton & Steinhardt: Queue 2019 vs arXiv 2018

| Version | Details | Use |
|---|---|---|
| **Queue** | Zachary C. Lipton and Jacob Steinhardt, "Troubling Trends in Machine Learning Scholarship: Some ML papers suffer from flaws that could mislead the public and stymie future research." *Queue* 17(1): 45-77, 2019. DOI 10.1145/3317287.3328534. The ACM DL gives a February 2019 issue date; the Queue site gives 24 Apr 2019. **V** | Cite this as the archival version (`lipton2019troubling`). |
| **arXiv** | 1807.03341 (July 2018), presented at the ICML 2018 Machine Learning Debates workshop. **V** | `lipton2018troubling` only if the 2018 date matters. |
| **CACM** | A "Research for Practice" version in *Communications of the ACM*, June 2019 (cacm.acm.org/magazines/2019/6/...). The pages 45-53 given in lit_fashion_waves.md were **not** re-confirmed here. | Do not cite with pages unless re-checked. |

Use one key in the paper, not both.

### 2.12 PeerJ CS 2025: emergence detection by static topic models

**Real.**
- **Authors:** Xue Li, Ciro D. Esposito, Paul Groth, Jonathan Sitruk, Balazs Szatmari, Nachoem Wijnberg.
- **Title:** "Evaluation of unsupervised static topic models' emergence detection ability".
- **Citation:** *PeerJ Computer Science* 11: e2875, published 30 May 2025, DOI 10.7717/peerj-cs.2875.

**What it measured.**
- It compares LDA, BERTopic and CoWords clustering on emergence detection with a new metric.
- LDA has the best F1 (reported 80.6%); CoWords flags emergence earliest.
- According to ME:170, it notes that a global model may overfit dominant trends and miss small emerging topics.

**Closeness.**
- **G4.** It evaluates static models' detection ability. It does not refit the same model on early-only versus all-years windows on the same papers and count how many topics emerge.

**Wording.**
- "Static topic models can miss small emerging topics (Li et al., 2025), and prospective early-warning signatures for AI
  topics have been tested on later years (Khanbayov and Kurban, 2026). We quantify the hindsight effect directly: on
  the same papers with the same model, a map fitted with hindsight finds 29 emerging topics where an early-only map
  finds 8."
  - The 29 vs 8 figure is from DC:176-231 via landscape F2.
- Keep the dossier's caveat that the maps also differ in fitting corpus (DC:229).

### 2.13 Fischhoff 1975; Kerr 1998

| Citation | Status |
|---|---|
| Baruch Fischhoff, "Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty." *Journal of Experimental Psychology: Human Perception and Performance* 1(3): 288-299, 1975. DOI 10.1037/0096-1523.1.3.288. | **V**. One index misdates it as 2006; PubMed and the BMJ reprint give 1975. |
| Norbert L. Kerr, "HARKing: Hypothesizing after the results are known." *Personality and Social Psychology Review* 2(3): 196-217, 1998. DOI 10.1207/s15327957pspr0203_4. | **V** |

---

## 3. Bibliographic gaps (Open check 8)

| Gap | Resolution | Status |
|---|---|---|
| **Crane 1969** end page | **433-441**: the OUP record for *Social Problems* 16(4), Spring 1969, gives pp. 433-441 and DOI 10.2307/799952. One later bibliography gives 433-444; treat that as a variant. Use 433-441 and add the DOI. Existing `crane1969fashion` is correct. | V |
| **Foster et al. 2015** end page | **875-908** confirmed: *ASR* 80(5): 875-908, DOI 10.1177/0003122415601618. Remove the "end page not confirmed" note in lit_fashion_waves.bib. | V |
| **Hill et al. 2025** fourth author | **Xizhao Wang**. Replace "Wang, X." in lit_novelty_reward.bib. | V |
| **Fortunato et al. 2018** authors | All 14 authors confirmed in order: Fortunato, Bergstrom, Börner, Evans, Helbing, Milojević, Petersen, Radicchi, Sinatra, Uzzi, Vespignani, Waltman, Wang, Barabási. *Science* 359(6379): eaao0185, DOI 10.1126/science.aao0185. Search confirmed the surnames and order. The given names of the last four (Alessandro, Ludo, Dashun, Albert-László) are the standard record but were not separately displayed. | V (surnames); given names of the last four: high confidence |
| **Rastogi et al.** first names | Charvi Rastogi, Ivan Stelmakh, Xinwei Shen, Marina Meila, Federico Echenique, Shuchi Chawla, Nihar B. Shah. arXiv 2203.17259 (v1 31 Mar 2022; v4 Dec 2025). No archival venue was seen, so cite it as arXiv. | V-arXiv |
| **Tran et al. 2020** author list | David Tran, Alex Valtchanov, Keshav Ganapathy, Raymond Feng, Eric Slud, Micah Goldblum, Tom Goldstein. arXiv 2010.05137. Also a lightning talk at the NeurIPS 2020 workshop "Navigating the Broader Impacts of AI Research", where the third author appears as "Keshav R Ganapathy". | V-arXiv |

---

## 4. Fresh searches for directly competing studies

| # | Query (abridged) | Mode | Result |
|---|---|---|---|
| 1 | herding/bandwagon researchers ML conference submissions hot topics | extended | Nothing on *author* herding. Found Stelmakh 2023 (reviewers) and Wang 2023 (topic acceptance). |
| 2 | newcomer / first-time submitters acceptance ICLR or NeurIPS | extended | **No study found** breaking out acceptance by first-time or topic-newcomer status at ICLR/NeurIPS. Found Xu 2026, Ibrahim 2026, Huang 2026 and the NeurIPS 2021 consistency experiment (already in lit). |
| 3 | topic popularity / trend timing vs acceptance at ICLR 2025-2026 | extended | Xu 2026 (topic × acceptance at equal score) and Wang 2023. Nothing on timing within a topic's wave. |
| 4 | Catalyst Papers ICLR 2017-2025 | extended | Huang 2026 (new; see table row 14). |
| 5 | Insights from ICLR rebuttal | standard | Kargaran et al. 2025 (new; row 17). |
| 6 | Topic space trajectories (ML literature) | standard | Schäfermeier et al. 2021 (new; row 18). |
| 7 | Topical phase transitions in AI research | standard | Khanbayov & Kurban 2026 (new; row 15). |
| 8 | NLP researchers' bandwagon / trend-following | extended | Jurgens 2026 (migration, new; row 16). Nothing testing bandwagon topic choice. |
| 9 | newcomers vs incumbents entering LLM research and acceptance | extended | Nothing on point. Leads: "Nobel and novice" (journal prominence study; not checked here). |
| 10 | early adopters vs late followers and acceptance at ML conferences | extended | Nothing on point. |
| 11 | herding / herd behaviour in researchers' topic selection in AI | extended | Nothing on point. Only LLM-agent herding and finance. |
| 12 | ICLR acceptance by prior record / topic familiarity | extended | "Who Pays for Open Review?" (arXiv 2609.11983; authors unseen, **U**). Reputation proxies raise ICLR 2026 ratings, more so under open review. Nothing on topic familiarity. |
| 13 | Scholarly migration in NLP (authors) | extended | Confirmed Jurgens 2026. |
| 14 | Bias at the Borderline authors / pre-registration | extended | Confirmed (row 5). |

**Bottom line of the fresh searches.**
- Among the works these searches reached, **none** tests herding or bandwagon behaviour of *authors* at an ML/NLP venue
  with submission data.
- **None** relates topic-newcomer status, or timing within a topic's wave, to acceptance at ICLR or NeurIPS.
- The nearest are:
  - reviewer-side herding (Stelmakh 2023; Kargaran 2025);
  - topic × acceptance (Wang 2023; Xu 2026);
  - prestige × acceptance with pre-registration (Ibrahim 2026);
  - topic initiators and topic growth (Huang 2026);
  - persistence across the deep-learning shift (Bao & Li 2025).
- WebSearch is not exhaustive, and arXiv full-text search was not available. Keep "among the works we checked".

---

## 5. Consequences for gaps G1-G7 and the recommended story

| Gap | Status after verification | Required change |
|---|---|---|
| **G1** producers and gate in one complete population | **Holds, narrowed.** Full ICLR submission records are now standard: Wang 2023 (2017-2020), Jung 2025 (2017-2025, 28,358), Ibrahim 2026 (2019-2025 + 2026), Xu 2026 (2021-2026, 50,289), Huang 2026 (2017-2025). None joins topic-entry status and contribution type (producers) with position effects at the gate. | Say "complete ICLR records are widely used; what is new is asking, in one population, who carries waves into topics and how the gate treats position in a topic's life and in a team's record". |
| **G2** what entrants bring | **Holds.** Bao & Li study incumbents' persistence; Huang studies initiators; Biliotti studies newcomer authorship by gender; Jurgens studies venue migration; Movva counts entrants. None splits contribution type by topic-entry status. | Cite Bao & Li, Huang and Biliotti as neighbours. |
| **G3** pivot / chaperone at the decision | **Narrowed twice.** Hill 2025 shows lower publication success for larger pivots. Bao & Li 2025 use our closeness measure (SPECTER2 to own prior papers) in ML, with an impact outcome. | Claim only: the decision observed directly on all submissions of an ML venue under double-blind review, paired with the insider association, held-out replicated. |
| **G4** hindsight distortion | **Holds, narrowed.** Li 2025 (static-model emergence detection) and Khanbayov & Kurban 2026 (prospective early warning tested on later years). Neither compares hindsight and no-hindsight maps on the same papers. | Cite both. Keep DC:229's caveat that maps also differ in fitting corpus. |
| **G5** registered held-out FM displacement | **Holds.** Bao & Li's "DL displaced statistical learning" is descriptive, about the earlier shift. | Cite as the descriptive analogue for the previous paradigm shift. |
| **G6** reward over a wave's life | **Holds (still weak in our data).** Jung 2025's "earlier submission" is a different notion of time. | Define "early" explicitly. |
| **G7** confirmatory design | **Narrowed.** Ibrahim 2026 pre-registered an out-of-sample ICLR 2026 test. | Drop any "first" claim. Present the design as unusual in its breadth (sealed outcomes, single frozen run, registered held-out tests, reported size failure), not unique. |

**The story line survives.**
- The recommended thesis ("anchored, not herded") does not depend on any claim these works pre-empt.
- Two prior works now *strengthen* the herding side:
  - Stelmakh 2023: no reviewer herding;
  - our registered reversal (H2b′/H2c′, A; DC:364-366): no entrant herding of the predicted kind.
- Two add **rival readings** of the anchoring side:
  - Ibrahim 2026: visible prestige at the borderline;
  - Xu 2026: non-comparable topic score scales.
- One adds a **tension** for the Discussion: Bao & Li 2025, where persistence was penalised in impact during the previous shift.

---

## 6. Recommended novelty wording (drop-in)

**Gap paragraph (Introduction or Background):**

> Studies of ICLR's open records have related acceptance to author prestige and visibility (Tran et al., 2020;
> Ibrahim et al., 2026), to the review process (Jung et al., 2025), and to research area (Wang et al., 2023; Xu et al.,
> 2026). Studies of the producers describe who enters machine-learning topics and how far researchers stay from their
> own past work (Movva et al., 2024; Bao and Li, 2025), and the science of science shows that moving far from one's own
> record costs citations and publication (Hill et al., 2025). To our knowledge, among the works we checked, none asks in
> one complete submission population whether the herding account of a field's waves holds at three points — how the
> waves are measured, what kind of work topic entrants bring, and what the review decision goes with — nor tests these
> predictions with registered hypotheses replicated on held-out papers.

**Specific sentences:**
- **Herding.** "A randomised trial found no herding among reviewers at ICML (Stelmakh et al., 2023); we find that
  topic entrants do not write the follow-on work herding predicts."
- **Pivot.** "Larger pivots are less often published (Hill et al., 2025); we observe the decision itself, on every
  submission, at one ML venue."
- **Closeness measure.** "Our closeness measure follows Bao and Li (2025), who use SPECTER2 similarity to a
  researcher's own earlier papers."
  - This is accurate only if our measure is SPECTER2-based. landscape.md lists SPECTER2 topics; the writers must
    confirm which embedding the within-author closeness uses before writing "as we do".
- **Topic edges.** "Topic-level acceptance differences at ICLR are documented (Wang et al., 2023; Xu et al., 2026);
  we show they regress out of sample."
- **Design.** "Like Ibrahim et al. (2026), we test pre-registered predictions on later ICLR papers."

**Phrases to avoid:**
- "first study of acceptance at ICLR by topic";
- "first evidence of a pivot penalty at the gate";
- "first pre-registered study at an ML venue";
- "first to measure distance from one's own work in ML";
- "reviewers herd" or "reviewers do not herd" (say "no herding detected in an RCT");
- any number from the papers above that is not re-checked against the PDF.

---

## 7. Still open

1. **EMNLP 2026 record of Jung/Heo et al.**: author order and pages. This needs aclanthology.org access.
2. **Xu et al. 2026**: the order of the two middle authors.
3. **Wang et al. 2023 (*WWW*)**: issue number (2 vs 3); LNCS volume and pages of the 2021 conference paper.
4. **Biliotti et al.**: which arXiv version and year to cite. The title changed across versions.
5. **Vicinanza et al.**: the DOI, and whether the PNAS Nexus 2(1) correction concerns this article.
6. **"Who Pays for Open Review?"** (arXiv 2609.11983): the authors. Relevant as a rival to the insider premium.
7. **Our closeness embedding.** Confirm it is SPECTER2 before writing "as we do" (§6).
   - The dossiers name SPECTER2 for the topic embedding (DC:86) and for earlier-version detection (DC:154).
   - The far-jump measure is "cosine between the abstract and the closest experienced co-author's earlier ICLR
     submissions" (DP:231), which does not name the embedding. Check RESULTS.md.
8. **Every quoted number from these papers** must be checked against the full text. Only abstracts and snippets were seen.
