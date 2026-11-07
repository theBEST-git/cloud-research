# Literature notes: closest prior work and the gap

Area brief: find the closest prior work to our specific combination (who drives topic waves at a top ML venue, what they write, and how peer review treats entry position, distance and timing, across the foundation-model transition, with all submissions incl. rejected/withdrawn, hindsight-free topics, registered tests and held-out replication), and state precisely what is new.

## Process note (read first)

- **Search budget.** The workflow-wide WebSearch budget (200 calls per turn, shared by all agents) ran out after my first 10 searches. Per the tool's instruction I did not work around it. arxiv.org and alphaxiv.org fail DNS in this session (WebFetch), so arXiv abstract pages could not be read; arxiv.org has to be allowed in the session's network settings to fetch them.
- **Consequence.** Section A lists the 8 works I verified myself from search results. Section B cross-references closest-prior works that **sibling agents in this workflow verified** from search results (their notes and BibTeX are in the same folder; file and line given). I did not re-verify those myself; their summaries below are taken from the sibling notes, not from my own reading. Section C lists candidates I saw only partially or could not search (do not cite as verified).
- **Our numbers** come from `/tmp/claude-0/-home-user-cloud-research/8f8bbb72-8d64-5b3e-bbfb-b57542d228a7/scratchpad/paper_ws/dossier_core.md` (abbreviated `DC:line`).

### Labels for our findings (with sources)

- **F-DATA**: 43,480 discovery submissions with usable abstracts, incl. rejected and withdrawn (DC:65-66); 11,099 held-out papers from a released former test split (DC:72).
- **F-WAVES**: topic maps fitted with hindsight manufacture waves: 8 emerging topics on the 2017-20 map vs 29 on the all-years map; share of 2024-26 papers in emerging topics 22% (no hindsight) to 41% (pooled) (DC:174-187).
- **F-FMARCH**: FM share of papers 0.3% (2017) to 54.4% (2026); new-architecture share 24.5% to 7.5% (DC:163-164). H1d: topics whose previous-year papers built more on FMs have fewer new-architecture papers, -7.98 pp for 0 to 100% prior FM share (DC:271); held-out -11.0 pp [-18.1, -3.9], one-sided p 0.0013 (DC:364).
- **F-NEWMETHOD**: newcomer papers are more often method papers (+3.71 pp [+2.61, +4.80]) and less often dataset/benchmark/evaluation papers (-1.70 pp [-2.46, -0.93]); registered herding prediction was the opposite; held-out +3.60 and -2.10, both supported (DC:296-297, 365-366). Newcomer share 72.9% (DC:151).
- **F-NEWGAP** (exploratory): newcomer papers accepted -10.2 pp less within topic x year (DC:343); most of the gap is about who writes the papers (about -3 within authors) (DC:396).
- **F-FARJUMP**: far jumps from a team's own past work go with lower acceptance, discovery -5.44 pp, held-out -6.09 pp [-9.32, -2.86], one-sided p 0.0025 (DC:370).
- **F-INSIDER**: one topic insider vs none, discovery +3.42 pp, held-out +3.88 pp [+0.28, +7.47], one-sided p 0.017 (DC:374).
- **F-YOUNGKW**: emerging vs mainstream keywords +2.67 pp discovery, held-out +3.25 [-0.18, +6.69], one-sided p 0.031 (weak) (DC:375).
- **F-PEAK**: a keyword's acceptance gap falls after its share peaks; held-out D -5.2 pp [-11.1, +0.7], one-sided p 0.043, 17 waves (weak) (DC:378, 399).
- **F-FL**: federated learning, keyword 475 papers -11.3 pp (p 0.005, q 0.19); share peaked 3.2% (2023) then 1.1% (2026); held-out not confirmed (DC:397).
- **F-CROWD**, **F-BRAND**: crowding/acceptance inconclusive; branded titles no premium (task brief).

---

## A. VERIFIED BY ME (from search results I saw)

### A1. Bharadhwaj, Turpin, Garg & Anderson (2020) [CLOSEST PRIOR: same venue, acceptance correlates]
Bharadhwaj, H., Turpin, D., Garg, A., & Anderson, A. (2020). De-anonymization of authors through arXiv submissions during double-blind review. arXiv preprint arXiv:2007.00177.
Key: `bharadhwaj2020deanonymization`
- What it did: Observational study of ICLR 2019 and 2020 submissions from OpenReview (n = 5,050). Compared papers posted to arXiv before review with papers that were not, measuring author reputation by Google Scholar citations. Reported a statistically significant positive association between author reputation and acceptance for arXiv-posted papers, and that less confident reviewers gave higher scores to papers by well-known authors. A later critique (Rastogi et al., A2) notes the confounder that famous authors may selectively post higher-quality papers.
- Verified via: search result listing arXiv 2007.00177, author names, date (1 July 2020) and abstract content. No peer-reviewed venue seen; cite as arXiv.
- Relevance to us: Closest prior on **ICLR acceptance correlates** using OpenReview data incl. rejected papers. It studies *who the authors are* (prestige, de-anonymisation) in two years; we study *where the paper sits relative to a topic and its own team's past* (newcomer/insider, far jump, keyword timing) over ten years. It is also the main confounder warning for **F-INSIDER** and **F-NEWGAP**: insider status may proxy for reputation, and arXiv posting is a channel through which reputation can reach reviewers.

### A2. Rastogi, Stelmakh, Shen, Meila, Echenique, Chawla & Shah (2022, arXiv; v4 2025)
Rastogi, Stelmakh, Shen, Meila, Echenique, Chawla, & Shah (2022). To ArXiv or not to ArXiv: A study quantifying pros and cons of posting preprints online. arXiv preprint arXiv:2203.17259.
Key: `rastogi2022arxiv`
- Note: surnames, title, arXiv id and date (31 March 2022; v4 30 Dec 2025) seen in a search result; first names were **not** shown in the result, so they are left out here and in the BibTeX. Add them before camera-ready.
- What it did: Surveyed reviewers at two double-blind CS conferences (ICML 2021, EC 2021). More than a third of reviewers self-reported searching online for a paper they were assigned; preprints from higher-ranked institutions drew slightly more attention (correlation 0.06 ICML, 0.05 EC); preprint/social-media bans may have limited effect on anonymity.
- Relevance to us: Frames the anonymity limits of the gate we study. It supports reading **F-INSIDER** and **F-NEWGAP** as possibly partly status-mediated, not purely content-mediated. Not closest prior on topic dynamics.

### A3. Manzoor & Shah (2021)
Manzoor, E., & Shah, N. B. (2021). Uncovering latent biases in text: Method and application to peer review. *Proceedings of the AAAI Conference on Artificial Intelligence*, 35(6), 4767-4775.
Key: `manzoor2021uncovering`
- What it did: Nonparametric method to measure bias in text caused by visibility of author identity, identified via a policy change. Applied to ICLR review text around ICLR's 2018 switch from single- to double-blind review: significant bias in review text for 2017-2018, mirroring the ratings bias; no significant bias for year pairs that were both double-blind.
- Verified via: AAAI OJS article page 16608, mlanthology entry, arXiv 2010.15300 listing (in search results).
- Relevance to us: Another ICLR/OpenReview study of the gate, focused on identity visibility. Confirms that ICLR's double-blind period (2018 onwards) is the relevant regime for our acceptance analyses; not about topics or entry. Frames, not closest.

### A4. Stelmakh, Shah, Singh & Daume III (2021)
Stelmakh, I., Shah, N. B., Singh, A., & Daume III, H. (2021). Prior and prejudice: The novice reviewers' bias against resubmissions in conference peer review. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), Article 75.
Key: `stelmakh2021prior`
- What it did: Randomised experiment with novice reviewers (described by aihub as part of the ICML 2020 experiments): the treatment group was told before reading that a paper was a resubmission. Treated reviewers rated papers lower, with quality underrated most among the criteria; authors caution generalising beyond novice reviewers.
- Verified via: DBLP listing (PACM HCI 5(CSCW1), article 75, 2021), arXiv 2011.14646, NSF PAR record. Effect sizes not seen.
- Relevance to us: Frames the resubmission control in our acceptance models and the general point that reviewers' judgements respond to signals about a paper's history, not only its content. Analogous mechanism for **F-FARJUMP** (a paper's relation to its authors' record is visible to reviewers). Not closest.

### A5. Prabhakaran, Hamilton, McFarland & Jurafsky (2016) [CLOSEST PRIOR: topic life cycle x contribution framing]
Prabhakaran, V., Hamilton, W. L., McFarland, D., & Jurafsky, D. (2016). Predicting the rise and fall of scientific topics from trends in their rhetorical framing. In *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 1170-1180, Berlin. doi:10.18653/v1/P16-1111.
Key: `prabhakaran2016predicting`
- What it did: Combined topic models with a classifier of rhetorical function in abstracts (e.g., a topic used as method, goal or result) and showed that the rhetorical roles a topic plays help predict whether it will grow or decline. (A third-party summary reported about 72% accuracy predicting growth/decline from a topic's first five years; I did not verify that figure.)
- Verified via: ACL Anthology P16-1111 page and BibTeX (pp. 1170-1180, DOI).
- Relevance to us: **Closest prior for linking a topic's life cycle to the *kind* of contribution papers make**, which is our contribution-type layer (method vs benchmark/evaluation). Differences: published papers only, topics fitted over the full period (the hindsight practice **F-WAVES** questions), no peer-review outcome, no author-level entry. Our **F-NEWMETHOD** and **F-FMARCH** move the question from "which framing predicts topic growth" to "who brings which kind of contribution into a topic, and what the gate does with it".

### A6. Movva, Balachandar, Peng, Agostini, Garg & Pierson (2024) [CLOSEST PRIOR: who drives an ML trend]
Movva, R., Balachandar, S., Peng, K., Agostini, G., Garg, N., & Pierson, E. (2024). Topics, authors, and institutions in large language model research: Trends from 17K arXiv papers. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pp. 1223-1243, Mexico City. ACL Anthology 2024.naacl-long.67.
Key: `movva2024topics`
- What it did: 16,979 LLM-related arXiv papers, 2023 vs 2018-2022. Half of first authors in 2023 were new to LLM work, entering from non-NLP fields of CS; about 20x growth of LLM submissions to arXiv Computers and Society; industry's publication share fell in 2023; industry-academic collaborations focus on industry's topics.
- Verified via: ACL Anthology 2024.naacl-long.67 (pages 1223-1243), arXiv 2307.10700.
- Relevance to us: **Closest prior on "newcomers drive the FM wave"** in ML/NLP. It shows entry is large but is descriptive, on arXiv (no review outcome, no rejected papers), one wave, and does not ask what entrants write or how they are judged. Our **F-NEWMETHOD** (entrants bring methods, not benchmarks), **F-NEWGAP**/**F-INSIDER**/**F-FARJUMP** (the gate discounts entrants unless they bring an insider or stay near their record) are exactly the two steps it leaves open. Our newcomer share (72.9%, DC:151) is consistent in spirit with their "half of first authors new".

### A7. Saphra, Fleisig, Cho & Lopez (2024)
Saphra, N., Fleisig, E., Cho, K., & Lopez, A. (2024). First tragedy, then parse: History repeats itself in the new era of large language models. In *Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)*, pp. 2310-2326, Mexico City. doi:10.18653/v1/2024.naacl-long.128.
Key: `saphra2024first`
- What it did: Position/history paper. Uses the first era of large models in NLP (statistical machine translation from about 2005) to draw lessons for the current LLM era; argues that disparities in scale are transient and that some research problems are evergreen.
- Verified via: ACL Anthology 2024.naacl-long.128, Edinburgh research portal, arXiv 2311.05020.
- Relevance to us: Frames **F-FMARCH** as one more instance of a recurring scale-driven displacement, and offers the "history repeats" reading of waves (rise, crowding, fade) that **F-PEAK** and **F-FL** quantify at the review stage. Qualitative; no data on submissions or acceptance.

### A8. Hoonlor, Szymanski & Zaki (2013)
Hoonlor, A., Szymanski, B. K., & Zaki, M. J. (2013). Trends in computer science research. *Communications of the ACM*, 56(10), 74-83. doi:10.1145/2500892.
Key: `hoonlor2013trends`
- What it did: Keyword trends in ACM Digital Library and IEEE Xplore publications and NSF grants, used to trace (and anticipate) shifts in CS research communities and topics, and how funding relates to these shifts.
- Verified via: CACM author page and Mahidol repository record (vol. 56, no. 10, pp. 74-83, DOI).
- Relevance to us: Canonical precedent for **life cycles of CS research topics** from bibliographic keywords. Published papers only, no review gate, no entrant analysis; keyword trends read with hindsight. Frames **F-WAVES** and our keyword-timing analyses (**F-YOUNGKW**, **F-PEAK**).

---

## B. CLOSEST-PRIOR WORKS VERIFIED BY SIBLING AGENTS (cross-reference; not re-verified by me)

Keys refer to the sibling BibTeX files in the same folder. Summaries condensed from the sibling notes.

| Key (sibling file:line) | What it measured, data | How we differ | Role |
|---|---|---|---|
| `tran2020open` (lit_ml_metaresearch.md:115) | ICLR 2017-2020 OpenReview; randomness of scores/decisions, institutional and gender gaps; arXiv-before-review papers fared better | 10 years incl. withdrawn and FM era; topic position and timing rather than identity; registered + held-out | **Closest prior on data** |
| `zhang2022investigating` (lit_outsiders.md:195) | ICLR (2017 onward) relational database from OpenReview, Scholar, arXiv, CSRankings; disparities by author/institution attributes | no topic incumbency, contribution type or life cycle; no held-out | Closest prior dataset |
| `sun2022does` (lit_ml_metaresearch.md:121) | ICLR single- to double-blind switch (2018), 5,027 papers; prestige bias fell modestly | identity bias vs our topic position/timing | Same gate, different question |
| `anderson2012towards` (lit_ml_metaresearch.md:33) | ACL 1980-2008, about 13,000 papers; topic models + author movement across topics, epochs | published only; hindsight-fitted topics; no gate | **Closest canonical "people flows into topics"** |
| `gururaja2023build` (lit_ml_metaresearch.md:39) | 26 interviews + ACL Anthology citation/authorship analysis; explore/exploit cycles, benchmark culture | qualitative/descriptive; we test the exploit phase (**F-FMARCH**) with registration and held-out | Closest narrative of paradigm shift |
| `pramanick2023diachronic` (lit_ml_metaresearch.md:45) | ACL Anthology; causal discovery over tasks, methods, datasets, metrics; methods and tasks drive, datasets follow | published only; no entrant split; no gate | Closest on contribution-type dimension |
| `klinger2020narrowing` (lit_ml_metaresearch.md:83) | about 110,000 arXiv AI papers; thematic diversity stagnates; industry less diverse | topic diversity from full-period topic models (hindsight, **F-WAVES**) | Closest "narrowing" claim |
| `koch2021reduced` (lit_ml_metaresearch.md:101) | Papers with Code; benchmark use concentrates on few datasets from elite institutions | explains why newcomers do not write benchmarks (**F-NEWMETHOD**) | Mechanism |
| `sekara2018chaperone` (lit_outsiders.md:60) | New PIs in Nature/Science/PNAS often previously coauthors there ("chaperoned") | publication/citation outcome, not acceptance of all submissions; we replicate at topic level on held-out | **Closest prior for F-INSIDER** |
| `hill2025pivot` (lit_outsiders.md:74) | 25.8M papers, 1.7M patents; further pivots, lower citation impact | citations after publication vs acceptance at the gate | **Closest prior for F-FARJUMP** |
| `arts2018paradise` (lit_outsiders.md:66) | Patents; inventors entering new fields: more novel, less valuable; experts mitigate | same mechanism (novelty, value loss, expert mitigation) in patents | Closest mechanism for F-NEWMETHOD + F-NEWGAP + F-INSIDER |
| `packalen2019age` (lit_outsiders.md:54) | Biomedical text; young researchers try newer ideas; young first + experienced last author best | career age vs topic newcomer; citations vs acceptance | Supports F-NEWMETHOD, F-INSIDER |
| `newman2009first` (lit_novelty_reward.md:295) | Price model; first papers in a field get citation advantage | reward for earliness measured at evaluation (F-YOUNGKW, F-PEAK), not citations | **Closest prior for timing** |
| `zeng2019increasing`, `jia2017quantifying` (lit_outsiders.md:80, 86) | Topic switching is rising but mostly local; switching goes with lower citations | we observe switching outcomes at the gate | Frames F-FARJUMP |
| `boudreau2016looking`, `wang2017bias`, `foster2015tradition`, `hofstra2020diversity` (lit_outsiders.md:118, 106, 100, 34) | Evaluators penalise novelty/distance; novel work has delayed recognition; diverse/novel contributors less rewarded | grant/citation settings; we test at ML conference review | Theory of the gate |
| `bommasani2021opportunities`, `hooker2021hardware` (lit_fashion_waves.md:264, 224) | FM paradigm; hardware lottery | essays; no test | Frame F-FMARCH |

---

## C. UNVERIFIED OR PARTLY VERIFIED CANDIDATES (do not cite as verified)

Seen in search results but without full bibliographic confirmation (authors or venue missing), or planned but not searched because the budget ran out.

Seen, partly verified:
1. **"What Have We Learned from OpenReview?"** arXiv 2103.05885 (2021). A search summary attributed to it an ICLR 2017-2020 analysis in which arXiv-posted submissions had higher acceptance (49.39% vs 32.68%) and cluster-level popularity treated as area competitiveness. Authors and any journal version not seen. **Potentially closest prior on topic popularity and acceptance at ICLR; verify before citing.**
2. **"Persistence Paradox in Dynamic Science"** arXiv 2506.22729 (2025). Search summary: ML researchers' persistence vs adaptability during the post-2013 deep-learning shift; persistence predicts productivity but lower impact; ICML/NeurIPS topics increasingly aligned with ICLR's. Authors not seen. **Potentially closest prior on incumbents vs adapters in an ML paradigm shift; verify.**
3. **"Reviewer Scores Are Not Comparable Across Research Areas in ML Peer Review"** arXiv 2607.27209 (2026). Search summary: high-acceptance areas have higher acceptance at every score level. Authors not seen.
4. **"Breaking New Ground, Reinforcing Old Gaps: Gender Disparities in Access to Emerging Research Frontiers"** arXiv 2404.04707. Search summary: PubMed-based; defines incumbents as authors who already published in the paper's field and newcomers as those who did not (same operationalisation as ours). Authors not seen.
5. **"Corporate Disruption in the Science of Machine Learning"** arXiv 1612.04108. Title and id only.
6. **Mishkin, Tabb & Matas (2020), "ArXiving Before Submission Helps Everyone"**, arXiv 2010.05365. Surnames, title, id seen; first names not seen; position paper.
7. **"Bias at the Borderline: Who Gets the Benefit of the Doubt in Peer Review?"** arXiv 2607.26280 (2026). Search summary: prestige-related score gap concentrated among papers identifiable (arXiv) at decision time. Authors not confirmed (a sibling note lists a tentative attribution).
8. Blog analyses of ICLR OpenReview (e.g., one reporting that about one in five ICLR submissions has "LLM"/"language model" in the title and these are accepted at the average rate). Not scholarly; do not cite.

Planned but not searched (budget exhausted): Effendy & Yap 2017 (CS trends from Microsoft Academic Graph); Salatino, Osborne & Motta 2018 (AUGUR, forecasting emerging topics); Small, Boyack & Klavans 2014 (emerging topics, Research Policy); Jurgens et al. 2018 (citation frames, TACL); Krenn et al. 2023 (forecasting AI research with link prediction, Nature MI); Frank et al. 2019 (evolution of AI citation graphs); Duede et al. 2024 (AI diffusion across fields); Gao & Wang 2024 (AI in science). All unverified; titles from memory only.

---

## D. Synthesis: what is closest and what is new

### Closest prior work, by strand

1. **ICLR/OpenReview acceptance correlates** (Tran 2020; Bharadhwaj 2020; Manzoor & Shah 2021; Sun 2022; Zhang 2022; partly verified "What Have We Learned from OpenReview?"). Same venue and source, incl. rejected papers. All focus on **author identity** (prestige, institution, gender, anonymity) over short windows ending 2018-2020/early 2020s. None asks how a paper's **position in a topic's life cycle** (newcomer/insider, distance from own record, keyword timing) relates to acceptance, and none spans the FM transition or uses registered held-out tests.
2. **Who drives ML/NLP trends** (Movva 2024; Anderson 2012; partly verified "Persistence Paradox"). Show that entrants are numerous and that people move across topics. Published or arXiv papers only; descriptive; no contribution-type split by entry status and no review outcome.
3. **Topic life cycles in CS/NLP** (Hall 2008; Anderson 2012; Hoonlor 2013; Prabhakaran 2016; Klinger 2020; Pramanick 2023). Topics fitted over the whole period and read forward; published papers only. Prabhakaran 2016 is closest because it links a topic's rise/fall to contribution framing, but does not observe who writes or what the gate does. Among the works checked, none compares maps fitted without and with hindsight.
4. **FM displacing other lines** (Bommasani 2021; Gururaja 2023; Saphra 2024; Klinger 2020; Hooker 2021). Essays, interviews or descriptive trends; no topic-level test that FM adoption is followed by fewer new-architecture papers.
5. **Entry, distance and timing rewards** (Sekara 2018 chaperone; Hill 2025 pivot penalty; Arts & Fleming 2018; Packalen & Bhattacharya 2019; Newman 2009 first-mover; Boudreau 2016). Strong analogues for **F-INSIDER**, **F-FARJUMP**, **F-NEWMETHOD**, **F-YOUNGKW/F-PEAK**, but measured on **citations, publications in journals, patents or grants**, outside ML, and on published outcomes rather than a full submission stream.

### Gap statement (3-5 sentences)

Prior work describes ML's waves either from the outside, by fitting topic models to published papers with hindsight, or from the gate, by testing whether reviewers favour prestigious authors; no study we found joins the two by asking who carries a wave into a topic, what kind of contribution they bring, and how peer review treats them as the wave rises and fades. The science-of-science results that would predict an answer (chaperone effect, pivot penalty, first-mover advantage, bias against novelty) come from citations, journals, patents and grants, not from the complete submission stream of an ML venue, where rejected and withdrawn papers are visible. ML-specific accounts of the foundation-model shift are qualitative or descriptive and do not test, out of sample, whether FM adoption crowds out other contribution types. Our ICLR 2017-2026 corpus, with hindsight-free topic maps, a registered single run and a held-out replication, lets us test these mechanisms at the gate across a full paradigm shift, and shows that the apparent size of the shift itself depends on hindsight.

### Three candidate one-sentence positioning claims (with evidence of novelty)

1. **"Newcomers make the waves, the gate keeps the shoreline": in ML's foundation-model transition, topic entrants bring new methods rather than the easy benchmark contributions that herding predicts, but peer review rewards proximity (an insider on the team, a near rather than far move, an early rather than late keyword), so convergence is enforced at evaluation rather than by imitation among authors.**
   Evidence of novelty: Movva 2024 documents entry but not what entrants write or how they are judged; Sekara 2018, Hill 2025, Arts & Fleming 2018 show proximity rewards in citations/patents, not in conference acceptance of all submissions; herding theory (sibling lit_fashion_waves.md, Bikhchandani 1992; Abrahamson) predicts imitation by entrants, which our registered test rejected in the opposite direction (DC:296-297) and held-out confirmed (DC:365-366). Supported by F-NEWMETHOD, F-NEWGAP, F-INSIDER, F-FARJUMP, F-YOUNGKW, F-PEAK.

2. **"The first submission-level, hindsight-free and held-out-replicated account of a paradigm shift in ML", showing that FM adoption in a topic is followed by fewer new-architecture papers, and that how large the shift looks depends on whether topics are drawn with hindsight (8 vs 29 emerging topics).**
   Evidence of novelty: prior ICLR studies end around 2020 and study identity (Tran 2020; Bharadhwaj 2020; Sun 2022; Zhang 2022); paradigm-shift studies use published ACL papers and full-period topic models (Gururaja 2023; Pramanick 2023; Anderson 2012; Hall 2008); FM-displacement claims are essays (Bommasani 2021; Saphra 2024; Hooker 2021). None of the works checked reports early-only vs all-years topic maps. Supported by F-DATA, F-WAVES, F-FMARCH.

3. **"Moving the science-of-science reward questions (chaperone effect, pivot penalty, first-mover advantage) from citations to the review gate": using every submission to ICLR, including rejected and withdrawn ones, we find that the distance and timing penalties known from citation studies already operate at acceptance, and replicate them on held-out papers.**
   Evidence of novelty: Hill 2025 and Newman 2009 use citations; Sekara 2018 uses journal authorship; Boudreau 2016 uses grant scores; ML review studies (Tran 2020; Bharadhwaj 2020; Manzoor & Shah 2021; Stelmakh 2021) study identity or resubmission signals, not topic distance or timing. Supported by F-FARJUMP, F-INSIDER, F-YOUNGKW, F-PEAK (with weak-evidence caveats for the last two).

Recommendation: claim 1 as the story line (it uses all three levels: field map, who enters and what they write, how the gate judges them), with claim 2 as the measurement contribution and claim 3 as the bridge to science of science. Avoid unqualified "first" wording; say "to our knowledge" and name the closest works.

### Cautions the closest prior work raises for us

- **Prestige confounding** (Bharadhwaj 2020; Tran 2020; Sun 2022; Rastogi 2022): insider and newcomer effects may partly be reputation effects transmitted via arXiv; PH3 (DC:396) shows most of the newcomer gap is about who writes the papers, which supports this caution.
- **Hindsight in topic histories** (Hall 2008; Anderson 2012; Klinger 2020; Hoonlor 2013): our F-WAVES is a methodological contribution to this genre; state it as "in the works we checked", since the search budget prevented an exhaustive check.
- **Paradigm-shift narratives are often retrospective** (Gururaja 2023; Saphra 2024): position F-FMARCH as a tested association, not a causal displacement.

---

## (a) What this literature already knows

- ICLR's open review data allow tests of reviewer bias; author prestige and visibility (via arXiv) go with acceptance, and double-blind review reduced but did not remove this (Bharadhwaj 2020; Manzoor & Shah 2021; Sun 2022; Tran 2020; Rastogi 2022). Reviewers also respond to signals about a paper's history (Stelmakh 2021).
- Large numbers of researchers enter hot ML areas from elsewhere (Movva 2024), and researchers move across topics, mostly locally (Anderson 2012; Zeng 2019; Jia 2017).
- Topic life cycles can be traced from bibliographic text, and the rhetorical role of a topic predicts its rise or fall (Hoonlor 2013; Prabhakaran 2016; Pramanick 2023).
- NLP/ML has undergone recurring scale-driven paradigm shifts; FMs are the latest (Gururaja 2023; Saphra 2024; Bommasani 2021).
- In citations, patents and journals: far pivots are penalised (Hill 2025), entry with an established coauthor helps (Sekara 2018), entrants are more novel but less valued (Arts & Fleming 2018), early papers in a field gain citations (Newman 2009).

## (b) What it does not know that our data can speak to

- Whether the entry, distance and timing rewards seen in citations already operate at the **review gate** of an ML venue, measured on all submissions incl. rejected/withdrawn, and whether they **replicate out of sample** (F-FARJUMP, F-INSIDER held-out supported; F-YOUNGKW, F-PEAK weak).
- **What kind of contribution** entrants to an ML topic bring: methods, not benchmarks, opposite to herding (F-NEWMETHOD).
- Whether FM adoption is followed, **topic by topic**, by fewer new-architecture papers, tested with registration and held-out data (F-FMARCH).
- How much of a measured "wave" is an artefact of **hindsight-fitted topic maps** (F-WAVES).
- How a wave's reward evolves over its own life cycle at the gate (F-PEAK, F-FL as the starkest case).

## (c) Candidate framings our findings could contribute to

1. **Entry and gatekeeping during a paradigm shift** (main story line): newcomers carry new methods into topics; review rewards proximity; waves are made by entrants but shaped by the gate. Contributes to science of science (chaperone, pivot penalty, first-mover) and to ML meta-research (peer review at ICLR).
2. **Measuring paradigm shifts without hindsight**: a methodological contribution to computational histories of NLP/ML, plus a tested FM-architecture displacement.
3. **Herding vs. gatekeeping as the source of conformity in ML research**: herding by authors is not supported; conformity pressure appears at evaluation.
