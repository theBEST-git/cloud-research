# Literature notes: computational histories and meta-research of NLP and ML

Area brief: studies of research trends, communities, peer review and writing in NLP/ML venues. Prepared for the ICLR 2017-2026 "riding the wave" paper (ACL ARR long paper).

Verification rule used: a work is listed as VERIFIED only when authors, title, year and venue (pages, volume/issue or article number where applicable) were confirmed in at least one search result I saw (ACL Anthology, PMLR, publisher/DOI pages, PMC, IDEAS/RePEc, arXiv listing). For arXiv-only works, "venue" = arXiv preprint with its identifier. Summaries are based only on what the search results showed (abstracts, anthology pages, repository and press summaries); I did not read full texts. Where a detail could not be confirmed it is flagged inline. Bib keys follow the sibling files' convention (first author + year + first content word of the title, leading article dropped).

Our own numbers quoted below come from `/tmp/claude-0/-home-user-cloud-research/8f8bbb72-8d64-5b3e-bbfb-b57542d228a7/scratchpad/paper_ws/dossier_core.md` (line numbers given) or from the project context in the task brief.

Labels for our findings used in the "Relevance" lines:
- **F-WAVES**: hindsight-fitted topic maps manufacture waves: 8 emerging topics on the 2017-20 map vs 29 on the all-years map (dossier_core.md:184); share of 2024-26 papers in emerging topics bracketed between 22% and 41% depending on the map (dossier_core.md:187).
- **F-FMARCH**: where more of a topic's previous-year papers built on foundation models, fewer of its papers propose new architectures (H1d: -7.98 pp for 0 -> 100% prior FM share, discovery; held-out -11.0 pp, one-sided p 0.0013; dossier_core.md:271). New-architecture share fell from 24.5% to 7.5% across years (dossier_core.md:164,169).
- **F-NEWMETHOD**: newcomer papers are more often method papers and less often benchmark/dataset papers, opposite to the registered herding prediction; replicated (task brief; sibling notes lit_outsiders.md).
- **F-CROWD**: crowding (topic maturity) and acceptance inconclusive/underpowered (H3a; dossier_core.md:324).
- **F-BRAND**: branded "NAME: subtitle" titles rose from 9% to 41% (dossier_core.md:165, flagged there as "not re-verified") but carry no acceptance premium (task brief).
- **F-FARJUMP / F-INSIDER**: far jumps from a team's own past work go with lower acceptance; one topic insider in the team goes with higher acceptance; both replicated (task brief).
- **F-YOUNGKW**: young rising keywords modestly favoured (replicated, weak; dossier_core.md:375).
- **F-PEAK**: a keyword's acceptance gap falls after its share peaks (PH6, held-out D -5.2 pp, one-sided p 0.043, 17 waves; dossier_core.md:378,399).
- **F-FL**: federated learning is the starkest discovery case; held-out not confirmed (dossier_core.md:399).
- **F-DATA**: our corpus design itself: dated snapshots of official OpenReview records including rejected and withdrawn papers, 2017-2026, pre-registered tests, a held-out replication split.

---

## VERIFIED WORKS

### A. Computational histories of NLP (topic models, epochs, paradigm shifts)

**1. Hall, D., Jurafsky, D., & Manning, C. D. (2008). Studying the history of ideas using topic models. In *Proceedings of the 2008 Conference on Empirical Methods in Natural Language Processing* (EMNLP), pp. 363-371, Honolulu, Hawaii. ACL Anthology D08-1038.**
Key: `hall2008studying`
- What it did: Applied unsupervised (LDA) topic modelling to the ACL Anthology to trace trends in computational linguistics from 1978 to 2006. Reported the rise of probabilistic methods from 1988, a steady increase in applications, and a sharp decline of semantics/understanding research 1978-2001 (possibly rising again after 2001). Introduced "topic entropy" as a measure of the diversity of ideas and used it to compare conferences.
- Verified via: ACL Anthology D08-1038 page and BibTeX (pp. 363-371, eds. Lapata & Ng).
- Relevance to us: The founding move of the "computational history" genre, and the exact procedure our **F-WAVES** result calls into question: a single topic model fitted on the whole period and then read forwards in time. Our finding that all-years maps yield 29 emerging topics vs 8 on an early-only map is a direct methodological critique of this design (hindsight leakage in topic definitions). Canonical anchor; not closest prior on outcomes.

**2. Anderson, A., McFarland, D. A., & Jurafsky, D. (2012). Towards a computational history of the ACL: 1980-2008. In *Proceedings of the ACL-2012 Special Workshop on Rediscovering 50 Years of Discoveries*, pp. 13-21, Jeju Island, Korea. ACL Anthology W12-3202.**
Key: `anderson2012towards`
- What it did: People-centred history of the ACL using the ACL Anthology Network corpus (around 13,000 papers by about 11,000 authors). Used topic models to classify papers and traced how individual authors move across topics; partitioned the history into "epochs" of topical cohesion and asked which topics and turning points shaped the field.
- Verified via: ACL Anthology W12-3202 (author order on Anthology: Anderson, Jurafsky, McFarland; the brief's order "Anderson, McFarland and Jurafsky" differs; cite per Anthology).
- Relevance to us: Closest canonical precedent for linking topic dynamics to *people* flows (who enters a topic, who migrates). Frames **F-NEWMETHOD**, **F-FARJUMP** and **F-INSIDER**: we measure author movement into topics at the paper level and tie it to contribution type and to acceptance, which Anderson et al. do not observe (they see only published papers, no rejected ones). Same hindsight caveat as Hall et al. for epoch detection (**F-WAVES**).

**3. Gururaja, S., Bertsch, A., Na, C., Widder, D. G., & Strubell, E. (2023). To build our future, we must know our past: Contextualizing paradigm shifts in natural language processing. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (EMNLP), pp. 13310-13325, Singapore. doi:10.18653/v1/2023.emnlp-main.822.**
Key: `gururaja2023build`
- What it did: 26 long-form interviews with NLP researchers combined with quantitative analysis of citations, authorship and language in the ACL Anthology. Identified recurring cycles of methodological change (described by interviewees as explore/exploit phases) and newer shifts in benchmark culture and software infrastructure.
- Verified via: ACL Anthology 2023.emnlp-main.822; arXiv 2310.07715.
- Relevance to us: Closest prior work for the *narrative* of the paper: the field experiences waves (paradigm shifts) and researchers describe exploit phases of herding. Our **F-FMARCH** (FM adoption -> fewer new-architecture papers) is a quantitative, pre-registered, held-out-replicated instance of the "exploit" phase they describe qualitatively; their benchmark-culture observation frames our **F-NEWMETHOD** result (newcomers do *not* go to benchmarks). Our **F-WAVES** adds a caution: some perceived shifts are artefacts of retrospective topic maps.

**4. Pramanick, A., Hou, Y., Mohammad, S. M., & Gurevych, I. (2023). A diachronic analysis of paradigm shifts in NLP research: When, how, and why? In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (EMNLP), pp. 2312-2326, Singapore. doi:10.18653/v1/2023.emnlp-main.142.**
Key: `pramanick2023diachronic`
- What it did: Used a causal discovery algorithm on the ACL Anthology corpus to study how research topics evolve, decomposing research into tasks, methods, datasets and metrics. Abstract: tasks and methods are the primary drivers of research in NLP, datasets follow, and metrics have minimal impact.
- Verified via: ACL Anthology 2023.emnlp-main.142 (four authors; arXiv v1 omitted Mohammad, later versions include him).
- Relevance to us: Closest prior on the *contribution-type* dimension: they decompose research into methods vs datasets vs metrics, as our LLM codebook does (method, benchmark/dataset, evaluation, ...). Their "methods drive, datasets follow" framing is consistent with **F-NEWMETHOD** (newcomers enter with methods) and with **F-FMARCH** (a method-level shift, FMs, reshapes what kinds of method papers appear). Unlike us, they model published papers only and have no peer-review outcome.

**5. Mohammad, S. M. (2020). Examining citations of natural language processing literature. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (ACL), pp. 5199-5209. doi:10.18653/v1/2020.acl-main.464.**
Key: `mohammad2020examining`
- What it did: Aligned ACL Anthology metadata with Google Scholar citation counts for tens of thousands of NLP papers. Found long papers get almost three times as many citations as short papers; some areas (e.g., sentiment classification, anaphora resolution, entity recognition) have the highest median citations; citations are highly skewed towards a few papers.
- Verified via: ACL Anthology 2020.acl-main.464; arXiv 2005.00912.
- Relevance to us: Representative of the "who/what gets attention" strand in NLP meta-research, measured by citations of published work. We measure the earlier gate (acceptance at submission, including rejected/withdrawn papers), which citation studies cannot see. Frames **F-YOUNGKW** and **F-PEAK** (topic-level rewards), but at the review stage.

**6. Mohammad, S. M. (2020). NLP Scholar: A dataset for examining the state of NLP research. In *Proceedings of the Twelfth Language Resources and Evaluation Conference* (LREC), pp. 868-877, Marseille, France. ACL Anthology 2020.lrec-1.109.**
Key: `mohammad2020nlp`
- What it did: Released the NLP Scholar dataset aligning ACL Anthology papers with Google Scholar metadata, enabling analyses of the state of NLP research (an ACL 2020 demo exists alongside). [Only metadata and page range seen; content described from the title and anthology entry.]
- Verified via: ACL Anthology 2020.lrec-1.109 and its BibTeX (pp. 868-877).
- Relevance to us: Infrastructure precedent; contrasts with **F-DATA** (our corpus has submissions incl. rejected/withdrawn and dated snapshots, rather than published papers).

**7. Wahle, J. P., Ruas, T., Abdalla, M., Gipp, B., & Mohammad, S. M. (2023). We are who we cite: Bridges of influence between natural language processing and other academic fields. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing* (EMNLP), pp. 12896-12913, Singapore. doi:10.18653/v1/2023.emnlp-main.797.**
Key: `wahle2023we`
- What it did: Analysed about 77k NLP papers, about 3.1m citations from NLP to other papers and about 1.8m citations into NLP, to measure how NLP's cross-field influence has changed.
- Verified via: ACL Anthology 2023.emnlp-main.797; arXiv 2310.14870.
- Relevance to us: Frames the "insularity vs. outside ideas" axis at field level. Our **F-FARJUMP** (far jumps from a team's own past work penalised) and **F-INSIDER** (an insider helps) give the paper-level, review-stage counterpart: distance from established local knowledge is costly at the gate.

### B. Concentration, industry and the narrowing of ML/AI research

**8. Ahmed, N., & Wahed, M. (2020). The de-democratization of AI: Deep learning and the compute divide in artificial intelligence research. arXiv preprint arXiv:2010.15581.**
Key: `ahmed2020dedemocratization`
- What it did: About 171k papers from 57 prestigious CS conferences (a news write-up says 60), with a difference-in-differences/synthetic-control design around the deep-learning shift. Firms and elite universities expanded their presence after deep learning took off, crowding out mid-tier (QS 201-300) and lower-tier (QS 301-500) universities; text analysis suggests access to compute drives the divergence.
- Verified via: arXiv 2010.15581 listing (submitted 22 Oct 2020); AI Index 2021 cites it. No journal version confirmed.
- Relevance to us: Frames **F-FMARCH** as part of a compute-driven shift: as FMs spread, fewer groups propose new architectures (which need compute), and work moves to building on FMs. Also frames **F-NEWMETHOD**: entry costs differ by contribution type.

**9. Ahmed, N., Wahed, M., & Thompson, N. C. (2023). The growing influence of industry in AI research. *Science*, 379(6635), 884-886. doi:10.1126/science.ade2420.**
Key: `ahmed2023growing`
- What it did: Policy Forum arguing industry increasingly controls the three inputs of modern AI (compute, large datasets, skilled researchers), visible in publications, leading models and benchmarks. Coverage reports industry involvement in the leading benchmark model rose from 62% (2017) to 91% (2020), and AI PhDs going to industry rose from about 21% (2004) to almost 70% (2020).
- Verified via: MIT FutureTech publication page and search results (vol. 379, issue 6635, pp. 884-886, DOI).
- Relevance to us: Macro context for **F-FMARCH**: foundation models concentrate architecture innovation; the rest of the field adapts. Supports a framing in which "riding the wave" (building on FMs) is the rational response for most teams.

**10. Klinger, J., Mateos-Garcia, J., & Stathoulopoulos, K. (2020). A narrowing of AI research? arXiv preprint arXiv:2009.10385.**
Key: `klinger2020narrowing`
- What it did: Hierarchical topic modelling of about 110,000 AI papers on arXiv. Found that thematic diversity of AI research has stagnated in recent years and that AI research involving private-sector organisations is less diverse than academic research.
- Verified via: arXiv listing 2009.10385 (v1 Sept 2020, v4 Jan 2022). Searches found no journal version; cited as arXiv preprint in later work.
- Relevance to us: The closest prior claim about field-level *narrowing* measured with topic models. Our **F-WAVES** warns that diversity/emergence measures depend on whether topics are fitted with hindsight; our **F-FMARCH** is consistent with a narrowing of architecture work. Our data add the review-stage side: does the gate reward the narrowing (**F-YOUNGKW**, **F-PEAK** say: novelty in young keywords is modestly favoured, and the premium fades after a keyword peaks).

**11. Abdalla, M., Wahle, J. P., Ruas, T., Névéol, A., Ducel, F., Mohammad, S. M., & Fort, K. (2023). The elephant in the room: Analyzing the presence of Big Tech in natural language processing research. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 13141-13160, Toronto. doi:10.18653/v1/2023.acl-long.734.**
Key: `abdalla2023elephant`
- What it did: 78,187 NLP publications and 701 author CVs. Industry presence among NLP authors was steady before a steep increase over the past five years (180% growth 2017-2022).
- Verified via: ACL Anthology 2023.acl-long.734; DBLP.
- Relevance to us: Same context as items 8-10 for NLP specifically; supports the backdrop of **F-FMARCH**.

**12. Birhane, A., Kalluri, P., Card, D., Agnew, W., Dotan, R., & Bao, M. (2022). The values encoded in machine learning research. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency* (FAccT '22), Seoul, 12 pages. doi:10.1145/3531146.3533083.**
Key: `birhane2022values`
- What it did: Annotated 100 highly cited ICML and NeurIPS papers (over 3,500 annotated sentences). Only 15% justify the work by a societal need and about 1% discuss negative impacts; the most frequent values are performance, generalization, quantitative evidence, efficiency, building on past work and novelty; growing ties to tech companies and elite universities. (Number of values: 67 in arXiv v1 vs 59 in the FAccT version.)
- Verified via: FAccT 2022 PDF (ACM reference format, 12 pages, DOI); arXiv 2106.15590. Proceedings page range not seen.
- Relevance to us: Names "novelty" and "building on past work" as co-equal community values; our results show how the review gate trades them off: **F-FARJUMP** (too far from own past work is penalised), **F-INSIDER** (local knowledge helps), **F-YOUNGKW** (young topics modestly favoured). Frames the tension the paper's story can be built on.

**13. Koch, B., Denton, E., Hanna, A., & Foster, J. G. (2021). Reduced, reused and recycled: The life of a dataset in machine learning research. In *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks 1* (NeurIPS Datasets and Benchmarks 2021). arXiv:2112.01716.**
Key: `koch2021reduced`
- What it did: Using Papers with Code (2015-2020 per the NeurIPS abstract; a Google listing says 2014-2021), found benchmark usage is increasingly concentrated on fewer datasets within task communities, substantial adoption of datasets from other tasks, and field-wide concentration on datasets introduced by a small number of elite institutions.
- Verified via: NeurIPS Datasets & Benchmarks proceedings page; arXiv 2112.01716. No page numbers (track proceedings without pagination).
- Relevance to us: Directly frames **F-NEWMETHOD**: if benchmark creation is concentrated among established/elite actors, newcomers being *less* likely to write benchmark papers is expected, which explains why the registered "herding into benchmarks" prediction was reversed.

**14. Lipton, Z. C., & Steinhardt, J. (2018). Troubling trends in machine learning scholarship. arXiv preprint arXiv:1807.03341 (ICML 2018 Machine Learning Debates workshop); also published in ACM Queue (Research for Practice).**
Key: `lipton2018troubling`
- What it did: Position paper identifying four patterns in ML papers: failing to separate explanation from speculation, failing to identify sources of empirical gains (e.g., architecture changes whose gains come from tuning), "mathiness", and misuse of language (suggestive terms of art, overloaded terms). Attributes them to rapid community growth, a thin reviewer pool, and misaligned incentives.
- Verified via: arXiv 1807.03341; ACM Queue page queue.acm.org/detail.cfm?id=3328534 (authors and title confirmed; Queue volume/issue/year NOT confirmed in results, so the Queue version is not cited with volume).
- Relevance to us: Frames **F-BRAND** (branded "NAME: subtitle" titles as a form of language/marketing) and the incentive story behind wave-riding. Our null premium for branded titles is evidence that, at ICLR's gate, this form of salesmanship is not rewarded.

### C. Peer review at ML/NLP venues

**15. Tran, D., et al. (2020). An open review of OpenReview: A critical analysis of the machine learning conference review process. arXiv preprint arXiv:2010.05137.**
Key: `tran2020open`
- What it did: ICLR submissions 2017-2020 from OpenReview. Measured randomness in review scores and decisions and whether scores track later impact; reported institutional bias in decisions even after controlling for paper quality, and a gender gap (lower scores, acceptance rates and citations for female authors). Press summary: papers on arXiv before review fared better, especially from CMU, MIT, Cornell.
- Verified via: arXiv 2010.05137 listing (first author David Tran plus six co-authors; full author list NOT confirmed in results, hence "et al."). Companion workshop paper arXiv 2011.12919 (NeurIPS 2020 Broader Impacts workshop).
- Relevance to us: **Closest prior work on data**: same venue and source (ICLR on OpenReview), but 2017-2020 and focused on author-identity bias. We extend to 2017-2026 with dated snapshots including withdrawn papers (**F-DATA**) and ask about topic/position effects rather than identity. Their institutional-bias result is a confounder we must address for **F-INSIDER** (insider status may proxy for prestige).

**16. Sun, M., Barry Danfa, J., & Teplitskiy, M. (2022). Does double-blind peer review reduce bias? Evidence from a top computer science conference. *Journal of the Association for Information Science and Technology*, 73(6), 811-819.**
Key: `sun2022does`
- What it did: Exploited ICLR's switch from single- to double-blind review in 2018 (review files of 5,027 papers). Scores for the most prestigious authors dropped after the switch, a modest reduction in prestige bias; the 2020 rating-scale change (10-point to 4-point) was about four times as effective. Papers rejected under single-blind were cited more than those rejected under double-blind.
- Verified via: IDEAS/RePEc (v73 i6 p811-819); arXiv 2101.02701.
- Relevance to us: Closest prior using ICLR's OpenReview record for a quasi-experiment on review outcomes. Shows ICLR rules changed across our window (blinding 2018, scale 2020), which our year fixed effects and topic x year comparisons must absorb. Frames **F-INSIDER** (status/familiarity effects persist despite blinding).

**17. Zhang, J., Zhang, H., Deng, Z., & Roth, D. (2022). Investigating fairness disparities in peer review: A language model enhanced approach. arXiv preprint arXiv:2211.06398.**
Key: `zhang2022investigating`
- What it did: Built an ICLR peer-review database (cogcomp.github.io/iclr_database) and analysed fairness disparities across author groups, finding disparities that vary by group and that textual features are essential for reducing bias in predictive models; provides baselines for review generation and scoring. (Exact year span not confirmed in results.)
- Verified via: arXiv 2211.06398 listing (7 Nov 2022, cs.CY).
- Relevance to us: Close prior on ICLR data infrastructure and on controlling for paper content when estimating group effects; parallels our use of SPECTER2 embeddings and LLM-coded contribution types as content controls.

**18. Cortes, C., & Lawrence, N. D. (2021). Inconsistency in conference peer review: Revisiting the 2014 NeurIPS experiment. arXiv preprint arXiv:2109.09774.**
Key: `cortes2021inconsistency`
- What it did: Revisited the 2014 NeurIPS experiment in which 10% of papers were reviewed by two independent committees. Estimated that about 50% of the variation in reviewer quality scores is subjective; for 680 rejected papers, quality scores correlated with later citations, but for accepted papers there was no correlation between scores and citations.
- Verified via: arXiv 2109.09774 (submitted 20 Sep 2021, cs.DL).
- Relevance to us: Establishes that acceptance is noisy, so effects of a few percentage points (**F-INSIDER**, **F-FARJUMP**, **F-YOUNGKW**, **F-PEAK**) are systematic shifts in a noisy lottery; it also explains our low power for **F-CROWD**. Supports our design choice of pre-registration plus held-out replication.

**19. Beygelzimer, A., Dauphin, Y. N., Liang, P., & Wortman Vaughan, J. (2023). Has the machine learning review process become more arbitrary as the field has grown? The NeurIPS 2021 consistency experiment. arXiv preprint arXiv:2306.03262.**
Key: `beygelzimer2023has`
- What it did: About 10% of NeurIPS 2021 submissions (882 duplicated papers) were reviewed by two independent committees. About half of papers accepted by one committee were rejected by the other (50.6% vs 49.5% in 2014); committees disagreed on 23% of accept/reject recommendations; increasing selectivity would increase arbitrariness.
- Verified via: arXiv 2306.03262 (5 Jun 2023); NeurIPS blog.
- Relevance to us: Same role as item 18; also bears on **F-CROWD**: growth of the field did not make review much more arbitrary, so crowding effects on acceptance should be expected to be small, consistent with our inconclusive result.

**20. Shah, N. B. (2022). Challenges, experiments, and computational solutions in peer review. *Communications of the ACM*, 65(6). doi:10.1145/3528086.**
Key: `shah2022challenges`
- What it did: Survey of problems in peer review (e.g., miscalibration, bias, strategic behaviour, subjectivity), experiments that help understand them, and computational solutions, with an extended version hosted by the author. [Page numbers within the issue not confirmed.]
- Verified via: NSF PAR record and CACM author page (vol. 65, no. 6, June 2022, DOI).
- Relevance to us: Standard survey to cite for peer-review background; positions our study as an observational, pre-registered study of what the gate rewards rather than a review-mechanism design.

**21. Kang, D., Ammar, W., Dalvi, B., van Zuylen, M., Kohlmeier, S., Hovy, E., & Schwartz, R. (2018). A dataset of peer reviews (PeerRead): Collection, insights and NLP applications. In *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)*, pp. 1647-1661, New Orleans. doi:10.18653/v1/N18-1149.**
Key: `kang2018dataset`
- What it did: 14.7K paper drafts with accept/reject decisions from ACL, NIPS and ICLR, plus 10.7K reviews for a subset (ICLR 2017: 427 papers, 1,304 reviews). Simple models predict acceptance with up to 21% error reduction over the majority baseline and predict aspect scores (originality, impact) above a mean baseline.
- Verified via: ACL Anthology N18-1149 (Anthology BibTeX lists "Dalvi"; the PDF gives "Bhavana Dalvi Mishra").
- Relevance to us: Origin of ICLR-on-OpenReview as an NLP research object; shows acceptance is partly predictable from text. Our study is not an acceptance-prediction task: we test pre-registered hypotheses about position in the topic landscape (**F-FARJUMP**, **F-INSIDER**, **F-YOUNGKW**).

**22. Zhang, D., Bao, Z., et al. (2025). Re2: A consistency-ensured dataset for full-stage peer review and multi-turn rebuttal discussions. arXiv preprint arXiv:2505.07920.**
Key: `zhang2025re2`
- What it did: Re2-Review: 19,926 initial submissions and 70,668 reviews from OpenReview across 24 conferences and 21 workshops (2017-2025); Re2-Rebuttal: 14,830 submissions with 53,818 rebuttal/discussion turns. Emphasises using initial (not revised) submissions to avoid inconsistency; aimed at training LLM reviewing assistants.
- Verified via: arXiv 2505.07920 (v1 12 May 2025; v2 March 2026). Seven authors; only the first two names seen, hence "et al.".
- Relevance to us: Closest recent data work emphasising the *version* problem; supports our **F-DATA** choice of dated snapshots of official records (state as of submission), and shows that existing OpenReview datasets mostly serve review-generation, not meta-research.

**23. Yang, J., Wei, Q., & Pei, J. (2025). Paper Copilot: Tracking the evolution of peer review in AI conferences. arXiv preprint arXiv:2510.13201.**
Key: `yang2025paper`
- What it did: System and open dataset archiving peer reviews across CS venues from official sites, OpenReview and opt-in forms into standardised, versioned, timestamped records; includes temporal snapshots of ICLR 2024/2025 reviews and a large-scale multi-year analysis of ICLR reviews. Notes that top AI/ML venues now exceed 10,000 submissions a year. An ICLR 2026 poster page lists the paper.
- Verified via: arXiv 2510.13201 (v1 15 Oct 2025, v2 9 Feb 2026); ICLR 2026 virtual poster page (so the ICLR 2026 venue is likely, but the arXiv record is cited here).
- Relevance to us: Closest concurrent infrastructure (timestamped ICLR snapshots). Distinguish: they track review evolution; we use snapshots to fix the information set at submission time and test pre-registered hypotheses about topic waves, with held-out replication.

**24. Latona, G. R., Horta Ribeiro, M., Davidson, T. R., Veselovsky, V., & West, R. (2024). The AI review lottery: Widespread AI-assisted peer reviews boost paper scores and acceptance rates. arXiv preprint arXiv:2405.02150.**
Key: `latona2024ai`
- What it did: All ICLR 2024 submissions and reviews; GPTZero estimates at least 15.8% of reviews were AI-assisted; in 53.4% of review pairs with different scores the AI-assisted one was higher; borderline papers with an AI-assisted review were 4.9 pp more likely to be accepted.
- Verified via: arXiv 2405.02150 (3 May 2024); Princeton/EPFL repositories report later publication in *Proceedings of the ACM on Human-Computer Interaction* 9(7), 2025 (article number not seen).
- Relevance to us: A late-window change in the ICLR review process (2024 on) that could interact with any year-specific acceptance effect, e.g., **F-PEAK** and **F-FL** (several keyword peaks fall in the LLM era). A robustness/limitations citation.

**25. Liang, W., Izzo, Z., Zhang, Y., Lepp, H., Cao, H., Zhao, X., Chen, L., Ye, H., Liu, S., Huang, Z., McFarland, D. A., & Zou, J. Y. (2024). Monitoring AI-modified content at scale: A case study on the impact of ChatGPT on AI conference peer reviews. In *Proceedings of the 41st International Conference on Machine Learning* (ICML), PMLR 235, pp. 29575-29620.**
Key: `liang2024monitoring`
- What it did: Corpus-level estimator of LLM-modified text applied to reviews at ICLR 2024, NeurIPS 2023, CoRL 2023 and EMNLP 2023: between 6.5% and 16.9% of review text could have been substantially modified by LLMs (10.6% for ICLR 2024 in v1). Higher in low-confidence, near-deadline reviews and among reviewers less likely to respond to rebuttals.
- Verified via: PMLR v235 page (liang24b).
- Relevance to us: Same role as item 24 (review-process change late in our window).

### D. Writing and titles: LLM-era language and title strategy

**26. Liang, W., Zhang, Y., Wu, Z., Lepp, H., et al. (2024). Mapping the increasing use of LLMs in scientific papers. In *First Conference on Language Modeling* (COLM 2024). arXiv:2404.01268.**
Key: `liang2024mapping`
- What it did: 950,965 papers (Jan 2020-Feb 2024) from arXiv, bioRxiv and Nature portfolio journals; population-level estimate of LLM-modified text. Largest and fastest growth in computer science (up to 17.5%); least in mathematics and Nature portfolio (up to 6.3%). Higher LLM modification is associated with authors who post preprints more, with papers in more crowded research areas, and with shorter papers. Expanded version in *Nature Human Behaviour* (2025).
- Verified via: OpenReview COLM 2024 PDF; arXiv 2404.01268 (submitted 1 Apr 2024). Full author list beyond the first four and James Zou not confirmed, hence "et al.".
- Relevance to us: Its link between *crowded areas* and LLM-assisted writing is a direct bridge to **F-CROWD** (crowded topics as a distinct writing/competition environment). Also a confound for any text-based measure in 2023-2026 (our SPECTER2 topic assignment and LLM coding of contribution type operate on LLM-era text), and context for **F-BRAND** (title style drift).

**27. Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances*, 11(27), eadt3813. doi:10.1126/sciadv.adt3813. (Preprint: "Delving into ChatGPT usage in academic writing through excess vocabulary", arXiv:2406.07016, 2024.)**
Key: `kobak2025delving`
- What it did: Excess-word analysis of PubMed abstracts (frequency gap and ratio measures, e.g., "delves", "showcasing", "underscores"). Lower bound of 13.5% of 2024 abstracts processed with LLMs (published version; preprint versions said at least 10%, up to 30% in some subcorpora); the shift exceeds the effect of COVID-19 on vocabulary.
- Verified via: PMC article, arXiv 2406.07016 listing, authors' GitHub README (vol. 11, no. 27, eadt3813, 2 July 2025). The brief's "Kobak et al. 2024" refers to the preprint title.
- Relevance to us: Methodological kin to our **F-YOUNGKW**/**F-PEAK** keyword-wave analyses (vocabulary excess over a counterfactual baseline). Also a caution that title/keyword trends after 2023 partly reflect LLM writing, not topic choice.

**28. Letchford, A., Moat, H. S., & Preis, T. (2015). The advantage of short paper titles. *Royal Society Open Science*, 2(8), 150266.**
Key: `letchford2015advantage`
- What it did: 140,000 papers from Scopus (the 20,000 most-cited per year, 2007-2013). Shorter titles associated with more citations per paper; with journal controls the link held for 2007-2010 but not 2011-2013.
- Verified via: DOAJ record; Warwick WRAP repository; Royal Society news release.
- Relevance to us: Canonical "title form affects attention" study. Contrasts with **F-BRAND**: at the ICLR review gate, branded titles bring no acceptance premium. Note mixed evidence (they mention an opposite 2009 result).

**29. Heard, Cull, & White (2023). If this title is funny, will you cite me? Citation impacts of humour and other features of article titles in ecology and evolution. *FACETS*, 8. doi:10.1139/facets-2022-0079.**
Key: `heard2023if`
- What it did: 2,439 papers (2000-2001) from nine ecology and evolution journals, humour scored on a 0-6 scale by volunteers. Raw: funnier titles had fewer citations, but authors give humorous titles to papers they judge less important; after correcting via self-citation, funny titles were linked to higher citations (roughly double). Title length had no effect.
- Verified via: DOAJ record; FACETS DOI page; bioRxiv preprint 2022. Surnames and venue/volume confirmed; first names/initials not seen in results (fill in from the DOI page before final bib); article page range not seen.
- Relevance to us: Shows the selection confound behind title-style effects (authors choose catchy titles for certain papers). Our **F-BRAND** null should be read with this confound in mind: branding is a choice correlated with paper type (method papers name their methods).

**30. Barnett, A., & Doubleday, Z. (2020). Meta-Research: The growth of acronyms in the scientific literature. *eLife*, 9, e60080.**
Key: `barnett2020growth`
- What it did: 24,873,372 titles and 18,249,091 abstracts since 1950. Acronym use in titles more than trebled and in abstracts rose about 10-fold; of over a million unique acronyms only about 0.2% are used regularly and 79% appear fewer than 10 times.
- Verified via: eLife article page 60080; PMC7556863.
- Relevance to us: Long-run backdrop for **F-BRAND** (the "NAME: subtitle" convention is an ML-specific, very fast version of a general trend toward coined names; 9% to 41% at ICLR, dossier_core.md:165, flagged "not re-verified").

### E. Community surveys (peripheral)

**31. Michael, J., Holtzman, A., Parrish, A., et al. (incl. Bowman, S. R.) (2023). What do NLP researchers believe? Results of the NLP community metasurvey. In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pp. 16334-16368, Toronto. doi:10.18653/v1/2023.acl-long.903.**
Key: `michael2023what`
- What it did: Survey of NLP researchers' beliefs about contested questions in the field. [Only metadata seen; content not summarised from results.]
- Verified via: ACL Anthology 2023.acl-long.903 BibTeX.
- Relevance to us: Peripheral; could be cited for community self-perception about scale and benchmarks if needed. Low priority.

---

## UNVERIFIED / PARTIALLY VERIFIED CANDIDATES (do not cite as verified)

- **"Bias at the Borderline: Who Gets the Benefit of the Doubt in Peer Review?"** arXiv:2607.26280 (2026). One search result attributed it to Ibrahim, Rahwan and Zaki; first names not seen and author list not confirmed from the arXiv page itself. Content seen: borderline ICLR submissions from 2019 on; at equal reviewer scores, papers with no top-25-institution author accepted 0.5-1.6 pp less often; penalty concentrated where a pre-decision arXiv preprint revealed authors (-3.4 vs -0.2 pp). **Potentially closest prior on ICLR acceptance at the borderline**; relevant to **F-INSIDER** (status vs topic familiarity). Verify authors before citing.
- **Lipton & Steinhardt in ACM Queue**: volume/issue/year (believed 2019, vol. 17) not confirmed; cite the arXiv version (item 14) unless confirmed.
- **Latona et al. in PACM HCI 9(7), 2025**: journal publication reported by repository pages but article number/pages not seen; cite arXiv version (item 24).
- **Liang et al. 2025, "Quantifying large language model usage in scientific papers", *Nature Human Behaviour*, doi:10.1038/s41562-025-02273-8**: seen only as a mention in search results; volume/pages not confirmed.
- **Tran et al. 2020 full author list**: only the first author and "six co-authors" seen.
- **Zhang et al. 2025 (Re2) full author list**: only the first two authors seen.

---

## Synthesis

### (a) What this literature already knows
1. **Fields move in waves that can be read from text.** Topic models on the ACL Anthology show the rise of statistical methods, decline of semantics, distinct epochs and people-flows across topics (Hall et al. 2008; Anderson et al. 2012); recent work finds cyclical explore/exploit paradigm shifts (Gururaja et al. 2023) and that methods and tasks drive change while datasets follow (Pramanick et al. 2023).
2. **ML/AI research has concentrated and possibly narrowed.** Compute and industry concentrate production (Ahmed & Wahed 2020; Ahmed et al. 2023; Abdalla et al. 2023), topical diversity has stagnated (Klinger et al. 2020), benchmark use concentrates on few datasets from elite institutions (Koch et al. 2021), and the field's stated values centre on performance, novelty and building on past work (Birhane et al. 2022).
3. **ML peer review is noisy and partly biased.** Two independent committees disagree on about half of accepted papers (Cortes & Lawrence 2021; Beygelzimer et al. 2023); ICLR data show institutional and prestige effects and responses to blinding and scale changes (Tran et al. 2020; Sun et al. 2022; Zhang et al. 2022); acceptance is partly predictable from text (Kang et al. 2018); since 2023 LLMs enter both reviews (Liang et al. 2024 ICML; Latona et al. 2024) and papers (Liang et al. 2024 COLM; Kobak et al. 2025).
4. **Title form is associated with attention, but with selection confounds.** Short titles and humour relate to citations (Letchford et al. 2015; Heard et al. 2023), and coined acronyms have exploded (Barnett & Doubleday 2020). Lipton & Steinhardt (2018) argue ML language and incentive problems arise from rapid growth.
5. **OpenReview data infrastructure exists and is growing** (PeerRead; ICLR database; Re2; Paper Copilot), mostly aimed at review generation or bias audits, with growing attention to versioning and timestamps.

### (b) What it does not know that our data can speak to
1. **Whether computational histories' waves are real or artefacts of hindsight.** Every topic-model history above fits topics on the whole period and reads them forward. None tests how many "emerging" topics survive when topics are defined only from early data. Our **F-WAVES** (8 vs 29 emerging topics) quantifies this hindsight inflation directly.
2. **What the gate rewards, not only what gets published or cited.** Histories and citation studies see only published papers; peer-review studies focus on author identity (gender, institution, prestige) or review consistency. None asks how a paper's *position in the moving topic landscape* (young vs. peaked keyword, crowded vs. sparse topic, near vs. far from its team's own past, with or without a topic insider) relates to acceptance, with rejected and withdrawn papers included and the information set fixed at submission time.
3. **How paradigm shifts change the mix of contribution types.** Paradigm-shift work is qualitative (Gururaja et al.) or published-only causal discovery (Pramanick et al.). No study tests, pre-registered and on held-out data, whether foundation-model adoption in a topic is followed by fewer new-architecture papers (**F-FMARCH**), or who (newcomers vs. insiders) supplies methods vs. benchmarks (**F-NEWMETHOD**).
4. **Whether being early on a wave pays, and when the premium fades.** The literature asserts herding/narrowing but does not measure the review-stage premium of riding a rising keyword and its decline after the peak (**F-YOUNGKW**, **F-PEAK**), nor whether branding a method (a common wave-riding marketing move) helps (**F-BRAND**).
5. **Confirmatory standards.** Almost all meta-research of NLP/ML is exploratory on one corpus. Our pre-registration, single frozen run and held-out replication (11,099 papers) are rare in this genre, and the pattern of what replicates (FM/architecture, newcomer method shift, far-jump penalty, insider premium) vs. what does not (federated learning, crowding) is itself informative.

### (c) Candidate framings our findings could contribute to
1. **"Reading the field's waves without hindsight" (methods + substance).** Main story: computational histories of NLP/ML (Hall et al.; Anderson et al.; Klinger et al.; Pramanick et al.) narrate waves using maps fitted after the fact. We rebuild ICLR 2017-2026 from dated snapshots with all submissions and show (i) hindsight maps manufacture waves (**F-WAVES**), and then (ii) using prospective measures, what wave-riding actually looks like at the review gate: the FM wave displaces new architectures (**F-FMARCH**); newcomers ride in with methods, not benchmarks (**F-NEWMETHOD**); the gate rewards proximity (**F-INSIDER**, penalises **F-FARJUMP**), modestly rewards early arrival on young keywords (**F-YOUNGKW**), and the premium fades after the peak (**F-PEAK**), while branding (**F-BRAND**) and crowding (**F-CROWD**) do not matter detectably. This positions the paper as both a critique of the genre's method and a confirmatory update of its claims.
2. **"The gate, not the archive": a review-stage history of a field.** Position against citation/publication-based histories (Mohammad 2020; Wahle et al. 2023) and identity-focused ICLR review studies (Tran et al. 2020; Sun et al. 2022; Zhang et al. 2022): we provide the first history of a field told through what its gatekeepers accept as topics rise and fall, including rejected/withdrawn work. Findings arranged as: what enters (contribution mix shifts), who enters (newcomers' methods), and what passes (proximity, timing).
3. **"Exploit phases are local, not global" (paradigm shifts at micro level).** Build on Gururaja et al.'s explore/exploit cycles and the narrowing/concentration literature (Klinger; Koch; Ahmed et al.): FM adoption narrows architecture work topic-by-topic (**F-FMARCH**), but entrants still bring methods (**F-NEWMETHOD**), and the gate rewards local knowledge (**F-INSIDER**) over far exploration (**F-FARJUMP**). This gives a mechanism-level account of how a field narrows: not by herding newcomers into benchmarks, but by a review gate that favours near moves.
4. **"Confirmatory meta-research for NLP/ML."** A methodological framing: the genre's headline claims should be pre-registered and replicated; we show which wave stories survive (FM/architecture; newcomer methods; proximity effects) and which do not (federated learning as the poster-child wave, **F-FL**; crowding). Fits ACL's growing interest in reproducibility of meta-scientific claims and the noisy-review backdrop (Cortes & Lawrence; Beygelzimer et al.).
5. **Writing/branding side note.** Relate **F-BRAND** to Letchford et al., Heard et al., Barnett & Doubleday and Lipton & Steinhardt: the "NAME: subtitle" boom is a marketing response to a crowded field, but it buys no acceptance at the gate; post-2023 text-based measures must also reckon with LLM-assisted writing (Liang et al. 2024; Kobak et al. 2025).

Suggested closest prior work to name in the paper: Tran et al. 2020 (same venue/data source), Sun et al. 2022 (ICLR OpenReview quasi-experiment), Gururaja et al. 2023 and Pramanick et al. 2023 (paradigm shifts in NLP), Hall et al. 2008 and Klinger et al. 2020 (topic-model histories whose design our hindsight result challenges), Koch et al. 2021 (benchmark concentration; explains the reversed newcomer prediction), Paper Copilot 2025 and Re2 2025 (concurrent timestamped OpenReview infrastructure).
