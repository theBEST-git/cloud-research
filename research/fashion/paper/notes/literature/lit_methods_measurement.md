# Literature notes: measuring topics over time, hindsight, and transparent observational designs

Area brief: methods literature on (a) topic and trend measurement over time and its pitfalls, and (b) credible confirmatory analysis of observational data. BibTeX: `lit_methods_measurement.bib` (same folder).

**How this was checked.** Every entry under "Verified works" had its authors, title, year and venue (plus volume, issue and pages where they apply) confirmed in at least one search result from a publisher, ACL Anthology, DBLP, PMC, RePEc/IDEAS, NBER, Crossref or the journal's own site. Where a detail could not be confirmed, the entry says so and the BibTeX leaves it out. The descriptions report what the search results showed (abstracts and record excerpts). Where I add standard background knowledge about a well-known paper that the results did not show, I mark it "[background]".

**First names in BibTeX.** For a few entries (Held; Sjögårde & Didegah; Gläser, Glänzel & Scharnhorst; Singh et al.), the search results confirmed surnames and initials but not full first names. The first names in the .bib are from background knowledge, so check them against the publisher before camera-ready.

**Search budget.** The shared web-search budget for this run ran out after 33 searches by this agent (the budget is shared with other agents in the run). So a few candidates (Fischhoff 1975, Kerr 1998, Agrawal et al. 2018 and others) could not be checked and are listed under "Unverified candidates". A follow-up message can resume the search.

**Our project numbers used below**, each with its source:
- 8 emerging topics on the 2017-20 map versus 29 on the all-years map: `research/fashion/presentation/script.md`, line 102.
- Of the papers behind the all-years map, 69% are from 2024-2026: `presentation/script.md`, lines 96-97.
- On the same papers, the "topics age" conclusion flips between the two maps: `presentation/script.md`, lines 103-104.
- Held-out confirmation rows for H1d, H2b′, H2c′ and H3a, including "hindsight passes / fails": `research/fashion/RESULTS.md`, lines 745-748.
- Kwtiming A1, a one-sided p of 0.031 on held-out data: `RESULTS.md`, line 756.

---

## Verified works

### A. Topic models and representations used to measure topics over time

**1. Griffiths, T. L., & Steyvers, M. (2004). Finding scientific topics. *PNAS*, 101(Suppl. 1), 5228-5235. doi:10.1073/pnas.0307752101.** BibTeX key `griffiths2004finding`.
- What it did: applied an LDA topic model, fitted by Gibbs sampling, to PNAS abstracts from 1991 to 2001, using Bayesian model selection to choose the number of topics (seen in the PMC record and summaries).
- [background] It also reported "hot" and "cold" topics by regressing topic shares on year. Those topics were found with one model fitted to the whole decade at once.
- Relevance to us: this is the canonical precedent for reading trends off a single topic model fitted retrospectively on all years. That is exactly the "all-years map" design we show manufactures waves (8 vs 29 emerging topics). It frames our hindsight finding as a critique of a standard, widely copied practice. It is not closest prior work on the outcome side.

**2. Blei, D. M., & Lafferty, J. D. (2006). Dynamic topic models. *Proceedings of the 23rd International Conference on Machine Learning (ICML '06)*, ACM ICPS vol. 148, 113-120. doi:10.1145/1143844.1143859.** BibTeX key `blei2006dynamic`.
- Verified via Crossref, MLAnthology and DBLP-derived BibTeX.
- [background] The topic-word distributions are allowed to drift between time slices through a state-space model, and the model was demonstrated on the archive of *Science*.
- Relevance to us: this is the standard "dynamic" alternative to a static map. Note, however, that a DTM is still fitted with all slices at once. Smoothing borrows information from later slices, so it does not by itself remove look-ahead. Cite it as the modelling tradition our early-map and year-balanced checks speak to. Our point is about which years the fit sees, not about whether topics may drift.

**3. Wang, X., & McCallum, A. (2006). Topics over time: A non-Markov continuous-time model of topical trends. *Proceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '06)*, 424-433. doi:10.1145/1150402.1150450.** BibTeX key `wang2006topics`.
- Verified via DBLP and ACM.
- [background] Each topic gets a continuous distribution over timestamps (a Beta distribution), and time stamps are generated jointly with words, so time shapes the topics themselves.
- Relevance to us: this is a second classic way to put time into topic discovery. Here, too, time information from the whole corpus shapes the topics. It supports our claim that the trend measured depends on modelling choices made with knowledge of the full period. It frames our finding; it is not closest prior work.

**4. Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF procedure. arXiv:2203.05794.** BibTeX key `grootendorst2022bertopic`.
- What it did: BERTopic embeds documents with pretrained transformers, clusters the embeddings, and labels clusters with a class-based TF-IDF (seen in the arXiv abstract).
- [background] It also offers a "topics over time" mode in which topics are fitted once on all documents and their representations are then computed per time bin.
- Relevance to us: our topic layer has the same embed-then-cluster architecture (SPECTER2 embeddings, k=100 clusters). This makes BERTopic-style pipelines the most directly exposed to our hindsight result. A global clustering fitted on a corpus where 69% of papers are from 2024-2026 builds categories around recent work. Methodologically, this is closest prior work for our measurement pipeline (a preprint, not peer-reviewed).

**5. Cohan, A., Feldman, S., Beltagy, I., Downey, D., & Weld, D. (2020). SPECTER: Document-level representation learning using citation-informed transformers. *Proceedings of the 58th Annual Meeting of the ACL*, 2270-2282. doi:10.18653/v1/2020.acl-main.207.** BibTeX key `cohan2020specter`.
- What it did: pretrained a SciBERT-based transformer on citation relations to produce document embeddings for scientific papers, and introduced the SCIDOCS benchmark (seen on ACL Anthology and arXiv).
- Relevance to us: this is the embedding family behind our topics. It also means our "topic" is a citation-informed semantic neighbourhood rather than a citation-network cluster, which bridges NLP topic modelling and scientometric clustering. It is a measurement citation, not a finding-level one.

**6. Singh, A., D'Arcy, M., Cohan, A., Downey, D., & Feldman, S. (2023). SciRepEval: A multi-format benchmark for scientific document representations. *Proceedings of EMNLP 2023*, 5548-5566. doi:10.18653/v1/2023.emnlp-main.338.**
- Verified: ACL Anthology record with pages 5548-5566, Singapore. The author list matched the queried names on the Anthology entry.
- BibTeX key `singh2023scirepeval`.
- [background] It is a benchmark of many scientific-document tasks, and it introduced SPECTER2 with format-specific adapters.
- Relevance to us: this is the source for SPECTER2, the encoder we use. Cite it in Data/Methods.

**7. Hall, D., Jurafsky, D., & Manning, C. D. (2008). Studying the history of ideas using topic models. *Proceedings of EMNLP 2008*, 363-371. ACL Anthology D08-1038.** BibTeX key `hall2008studying`.
- What it did: fitted LDA to the ACL Anthology (1978-2006) and tracked each topic's strength over time to describe the rise and fall of ideas in computational linguistics (seen on ACL Anthology and in summaries).
- Relevance to us: this is the closest prior work in the *ACL tradition*. It is a "history of a field from its papers" study using one retrospectively fitted model. Our paper can position itself as revisiting this genre for ICLR, with two changes: rejected and withdrawn submissions are included, and we show that the fitting window changes the history (the topics-age reversal on the same papers). This supports framing our contribution as "how to write a field's history without hindsight".

### B. Emerging topics and science mapping in scientometrics

**8. Small, H., Boyack, K. W., & Klavans, R. (2014). Identifying emerging topics in science and technology. *Research Policy*, 43(8), 1450-1467. doi:10.1016/j.respol.2014.02.005.** BibTeX key `small2014identifying`.
- What it did: proposed a method to nominate emerging topics from a large citation model of Scopus (1996-2010; others cite it as over 17M articles). The abstract notes that few studies actually nominate emerging topics for decision makers (seen on RePEc/IDEAS and in citing papers).
- Relevance to us: this is the canonical scientometric operationalisation of "emerging topic" (novelty plus growth). Our 8-versus-29 result shows that counts of emerging topics depend strongly on the classification's fitting window. That is a validity threat to this whole line of work whenever the clusters are built from data after the period studied. It frames our hindsight finding and is closest prior work on emergence measurement.

**9. Rotolo, D., Hicks, D., & Martin, B. R. (2015). What is an emerging technology? *Research Policy*, 44(10), 1827-1843. doi:10.1016/j.respol.2015.06.006.** BibTeX key `rotolo2015what`.
- What it did: defined emerging technologies by five attributes (radical novelty, relatively fast growth, coherence, prominent impact, and uncertainty and ambiguity), and reviewed scientometric ways to detect them: indicators, citation analysis, co-word analysis and overlay mapping (seen in the arXiv and Sussex records).
- Relevance to us: two of the attributes matter directly. "Coherence" and "prominent impact" can only be judged after the fact. That is the conceptual root of hindsight: a topic looks emergent once we know it cohered. Our design separates what was knowable at time t (early map, dated snapshots) from what is visible only later. It frames our central measurement story.

**10. Waltman, L., & van Eck, N. J. (2012). A new methodology for constructing a publication-level classification system of science. *JASIST*, 63(12), 2378-2392. doi:10.1002/asi.22748.** BibTeX key `waltman2012new`.
- What it did: clustered about ten million Web of Science publications (2001-2010) into a three-level hierarchy using direct citation relations, in three steps: relatedness, clustering and labelling. It argues for publication-level over journal-level classification (seen on RePEc and arXiv).
- Relevance to us: this is the template for the "one classification over a whole decade" design that dominates bibliometric topic studies. Our hindsight checks are a direct test of what such a fixed, full-period classification does to the history it describes. It frames the finding; it does not itself discuss look-ahead in the abstract we saw.

**11. Klavans, R., & Boyack, K. W. (2014). Creation of a highly detailed, dynamic, global model and map of science. *JASIST*, 65(4), 670-685.** BibTeX key `klavans2014creation`.
- Verified via DBLP (authors Klavans and Boyack, 65(4): 670-685) and a Scinapse record (online November 2013). The DOI could not be confirmed and is omitted.
- What it did: built an article-level co-citation model covering 16 years and nearly 20 million articles, framed as support for research *planning* rather than evaluation. "Dynamic" means the model is updated as new years arrive.
- Relevance to us: this is the scientometric precedent for building topic structure year by year rather than once. Our "early map" (2017-2020 only) is a cheap version of that dynamic logic. Cite it to show that the field knew dynamic models were preferable for planning. Our contribution is to *quantify* what is lost when one does not use them.

**12. Leydesdorff, L. (2002). Dynamic and evolutionary updates of classificatory schemes in scientific journal structures. *JASIST*, 53(12), 987-994. doi:10.1002/asi.10144.** BibTeX key `leydesdorff2002dynamic`.
- What it did: argued that a classification of journals, as a reflexive reconstruction, "is in need of an update when new information becomes available in a next year". It proposed factor-analytic updates from journal-journal citation matrices, from an evolutionary perspective (seen on the UvA and Utah BibTeX records).
- A 2016 citing paper (arXiv 1604.02716) says the approach "inverts the arrow of time and can signal, from a perspective of hindsight, when new developments have become important".
- Note: one RePEc author page lists a co-author, but the bibliographic records list Leydesdorff alone.
- Relevance to us: this is the closest found statement in scientometrics that classifications are time-indexed reconstructions and that later data change how earlier structure looks. It is the best citation for "the hindsight issue was recognised conceptually but not quantified for emergence counts". It supports our hindsight finding.

**13. Chavalarias, D., & Cointet, J.-P. (2013). Phylomemetic patterns in science evolution: The rise and fall of scientific fields. *PLOS ONE*, 8(2), e54847. doi:10.1371/journal.pone.0054847.** BibTeX key `chavalarias2013phylomemetic`.
- What it did: reconstructed fields per time period from key-phrase co-occurrence, then matched fields across periods into lineages ("phylomemies"). It reports a life cycle (emergence, gaining cohesion, branching or merging, decline), with density correlating with a field's age and short-term survival. Case studies were embryology and networks in biology (seen on PMC and RePEc).
- Relevance to us: this is a period-by-period design, the alternative to a single global map. Its life-cycle language (emergence, maturation, decline) is the scientometric counterpart of our "maturity" and "wave" vocabulary. It frames our PH6 finding: a keyword's acceptance gap falls after its share peaks, which is a life-cycle pattern measured on the reward side.

**14. Gläser, J., Glänzel, W., & Scharnhorst, A. (2017). Same data—different results? Towards a comparative approach to the identification of thematic structures in science. *Scientometrics*, 111(2), 981-998. doi:10.1007/s11192-017-2295-0.** BibTeX key `glaser2017same`.
- Verified via OpenAlex. DBLP shows a conflicting author line for this title, which looks like a catalogue error, so the authorship relies on OpenAlex and citing records.
- This paper introduces a special issue in which several teams clustered the same dataset and compared the topics they got. The companion "Comparison of topic extraction approaches and their results" (Velden et al.) is in the same issue. I saw only the metadata, not the abstract.
- Relevance to us: the headline is that the same data give different thematic structures under different methods. That is the robustness precedent for our multi-map design (k75, k100, k150, year-balanced, early map). We add the *temporal* axis, showing that the fitting window alone changes conclusions. It frames our hindsight finding.

**15. Held, M., Laudel, G., & Gläser, J. (2021). Challenges to the validity of topic reconstruction. *Scientometrics*, 126(5), 4511-4536. doi:10.1007/s11192-021-03920-3.** BibTeX key `held2021challenges`.
- What it did: built ground-truth topics in atomic, molecular and optical physics and found that none of four combinations of data model and algorithm reconstructed them consistently, at any resolution. It argues that the concept "topic" is left undefined in this literature (seen on Springer and TU Berlin).
- Relevance to us: this is strong support for treating any topic map as a construct with validity limits. It justifies our choice to make every registered claim survive several maps. It also lets us say that the hindsight problem is an additional, *temporal* validity threat, not covered by ground-truth comparisons on a fixed period. It supports our measurement-caution framing.

**16. Klavans, R., Boyack, K. W., & Murdick, D. A. (2020). A novel approach to predicting exceptional growth in research. *PLOS ONE*, 15(9), e0239177. doi:10.1371/journal.pone.0239177.** BibTeX key `klavans2020novel`.
- What it did: using clusters from a global model of science, it applied probit models on *lagged* indicators to forecast which research communities would show exceptional growth over the next three years. Validated on hundreds of thousands of forecasts, it exceeded the IARPA FUSE benchmarks in six of nine fields (seen on PMC, arXiv and DOAJ).
- Relevance to us: this is the forecasting counterpart to emergence detection. Its use of lagged indicators is the right instinct against look-ahead. However, its clusters still come from a global model, so the cluster boundaries themselves may embed later information. That is exactly the leak our early-map check isolates. It is closest prior work for our PH6 "forecast / keyword timing" analyses.

**17. Sjögårde, P., & Didegah, F. (2022). The association between topic growth and citation impact of research publications. *Scientometrics*, 127(4), 1903-1921. doi:10.1007/s11192-022-04293-x.** BibTeX key `sjogarde2022association`.
- What it did: built topics by community detection in a citation network and used two-part regressions across eight broad disciplines to relate topic growth to citation counts. It controls for journal impact, number of references and number of authors (seen on RePEc and arXiv; I did not see the findings).
- Relevance to us: this is the nearest scientometric analogue of our reward-side question ("does being in a growing or hot topic pay?"). There, the reward is citations; for us, it is peer-review acceptance, including rejected and withdrawn papers. Its topics are also built from a full-period classification, so our hindsight critique applies to it. It is closest prior work for our crowding / maturity-acceptance analyses (our H3a is inconclusive: `RESULTS.md`, line 748).

### C. Look-ahead bias, temporal leakage and temporal drift

**18. Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining: Formulation, detection, and avoidance. *ACM TKDD*, 6(4), Article 15, 1-21. doi:10.1145/2382577.2382579.** BibTeX key `kaufman2012leakage`.
- Verified via DBLP and ACM. The TKDD version has four authors; a three-author version appeared at KDD 2011 (pp. 556-563).
- What it did: defined leakage as introducing information about the target that should not legitimately be available. It proposed a "learn-predict separation" plus time-aware data management to avoid it, and detection methods for when one does not control data collection.
- Relevance to us: this gives the formal vocabulary for our hindsight problem. A topic map fitted on 2024-2026 papers and then used to describe 2018 is a learn-predict separation violation in descriptive analysis. It supports reframing hindsight as *temporal leakage in measurement*.

**19. Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9), 100804. doi:10.1016/j.patter.2023.100804.** BibTeX key `kapoor2023leakage`.
- What it did: from earlier reviews, it found leakage affecting at least 294 papers across 17 disciplines. It gave a taxonomy of eight leakage types (including temporal leakage) and proposed "model info sheets". In a civil-war prediction case study, the apparent advantage of complex ML over logistic regression disappeared once leakage was corrected (seen on PMC).
- Relevance to us: this is the most-cited recent statement that leakage silently inflates ML-based scientific claims. Our result extends the concern from *prediction* to *measurement*. Unsupervised topic maps used for descriptive history can leak the future, too. It supports our central hindsight framing and is closest prior work on the leakage side.

**20. Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2017). The probability of backtest overfitting. *Journal of Computational Finance*, 20(4). doi:10.21314/jcf.2016.322.** BibTeX key `bailey2017probability`.
- Verified on Risk.net, RePEc and eScholarship. Pages could not be confirmed and are omitted. SSRN lists it as forthcoming in 2015.
- What it did: proposed combinatorially symmetric cross-validation (CSCV) to estimate the probability that a backtested strategy is overfit. It argues that standard hold-out safeguards are unreliable for investment backtests.
- Relevance to us: this is the finance anchor for "backtests built with later knowledge mislead". The finance literature has names for look-ahead bias and backtest overfitting. Scientometric topic-trend work has no such norms. I found no canonical peer-reviewed article defining "look-ahead bias" itself (only practitioner glossaries and preprints), so cite Bailey et al. as the closest peer-reviewed anchor.

**21. Lazaridou, A., Kuncoro, A., et al. (2021). Mind the gap: Assessing temporal generalization in neural language models. *Advances in Neural Information Processing Systems 34 (NeurIPS 2021)*.** BibTeX key `lazaridou2021mind`.
- Verified on the NeurIPS virtual site and MLAnthology. Pages were not confirmed, and the BibTeX lists the first two of 14 authors plus "others".
- What it did: Transformer-XL models evaluated on text from after their training period get steadily worse with temporal distance. Larger models are not immune, and continual updating mitigates the decline.
- Relevance to us: within ACL/ML, this is the standard citation that representations are time-indexed. It gives an ACL-friendly bridge to our claim that a topic map is a model of *when it was fitted*. It frames the finding; it is not closest prior work.

### D. Credible confirmatory analysis of observational and secondary data

**22. Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *PNAS*, 115(11), 2600-2606. doi:10.1073/pnas.1708274114.** BibTeX key `nosek2018preregistration`.
- What it did: argued that committing to questions and an analysis plan before seeing outcomes separates prediction from postdiction. It notes that preregistration services exist in all disciplines (seen on PMC).
- Relevance to us: this justifies our registered hypotheses, frozen single run and the clear split between registered and post hoc (PH1-PH6) results. It also supports the honesty of reporting that newcomer papers are *more* often method papers, opposite to the registered herding prediction. A prediction that failed and then held on held-out papers counts as evidence because it was registered.

**23. Van den Akker, O. R., Weston, S., Campbell, L., et al. (2021). Preregistration of secondary data analysis: A template and tutorial. *Meta-Psychology*, 5. doi:10.15626/MP.2020.2625.** BibTeX key `vandenakker2021preregistration`.
- Verified on the Meta-Psychology journal pages and the Tilburg repository; there are 14 authors, and the BibTeX lists the first three plus "others".
- What it did: provided a 25-question template for preregistering analyses of *existing* data. It stresses that prior knowledge of the data can bias hypotheses, and a worked example suggests the template limits researcher degrees of freedom.
- Relevance to us: this is the closest methodological precedent for our setting. We preregistered on OpenReview records that already existed, sealed the outcome columns, and kept a released test split for one-shot confirmation. Cite it to argue that registering secondary data is legitimate and to describe our sealing as a stronger version of its "prior knowledge" safeguard.

**24. Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing transparency through a multiverse analysis. *Perspectives on Psychological Science*, 11(5), 702-712. doi:10.1177/1745691616658637.** BibTeX key `steegen2016increasing`.
- What it did: proposed running the analysis over all reasonable data-processing choices (the "multiverse") instead of one. Its fertility-religiosity example shows how arbitrary choices change conclusions (seen in the PDF record and CRAN).
- Relevance to us: our variant grid (k75, k100, k150, year-balanced map, early map, other specification variants; "9/9" and "10/10 variants" in `RESULTS.md`, lines 745-747) is a small multiverse. The hindsight result can be presented as a *temporal multiverse*: the fitting window is a processing choice that the usual multiverse does not list. This supports our design and suggests a framing.

**25. Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2020). Specification curve analysis. *Nature Human Behaviour*, 4(11), 1208-1214. doi:10.1038/s41562-020-0912-z.** BibTeX key `simonsohn2020specification`.
- What it did: proposed estimating all reasonable specifications, with an inferential test across them. Applied to three published findings, it sorted them into robust, weak and not holding (seen on Springer). A publisher correction exists (doi:10.1038/s41562-020-00974-w).
- Relevance to us: this gives the vocabulary for reporting "x/y variants agree" and for discussing which results are fragile (the inconclusive crowding and acceptance results). It supports our robustness reporting.

**26. Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, 102, 460-465.** BibTeX key `gelman2014statistical`.
- Verified: the authors, title, year and journal appear on the American Scientist site. Volume 102 and pages 460-465 come from a citing article (Fraser & Reid 2016). Issue 6 was not confirmed and is omitted.
- What it did: argued that the "garden of forking paths" creates multiple-comparison problems even without explicit fishing, in a single dataset (as summarised by commentators).
- Relevance to us: this is the reason our many post hoc analyses (PH1-PH6) are reported as exploratory unless declared and tested on held-out papers. It frames the weak results (PH6 p 0.043; kwtiming A1 one-sided p 0.031, `RESULTS.md`, line 756) as needing that caveat.

**27. Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics*, 6(2), 65-70.** BibTeX key `holm1979simple`.
- What it did: a sequentially rejective Bonferroni procedure that controls the family-wise error rate and is uniformly more powerful than Bonferroni (seen on JSTOR, GESIS and Wikipedia).
- Relevance to us: this is the correction used for our registered families ("Holm 0.001", "Holm < 0.001" in `RESULTS.md`, lines 745-748). It is a methods citation.

**28. Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics*, 90(3), 414-427. doi:10.1162/rest.90.3.414.** BibTeX key `cameron2008bootstrap`.
- What it did: showed that cluster-robust tests over-reject with few clusters (about 5-30). It proposed cluster bootstrap-t procedures and found the wild cluster bootstrap works best in practice (seen on NBER and RePEc).
- Relevance to us: this justifies our cluster-robust or two-way clustered inference by topic and year. With only 10 conference years, year is a small-cluster dimension, which is exactly the situation it warns about. It is a methods citation.

---

## Unverified candidates (do NOT cite as verified)

These are known or likely works whose bibliographic details I could not confirm in this run, because the search budget ran out or the results did not show authorship.

- Fischhoff, B. (1975). Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty. *Journal of Experimental Psychology: Human Perception and Performance*, 1(3), 288-299. This is the canonical source for "hindsight bias" and would anchor the paper's vocabulary. The search was not performed (budget).
- Roese, N. J., & Vohs, K. D. (2012). Hindsight bias. *Perspectives on Psychological Science*. Not searched; a ResearchGate hit titled "Hindsight Bias" appeared, but its authors were unconfirmed.
- Kerr, N. L. (1998). HARKing: Hypothesizing after the results are known. *Personality and Social Psychology Review*, 2(3), 196-217. The search was not performed (budget).
- Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology. *Psychological Science*. Not searched.
- Agrawal, A., Fu, W., & Menzies, T. (2018). What is wrong with topic modeling? (and how to fix it...). *Information and Software Technology*, 98. This is about LDA instability across runs. The search was not performed (budget).
- Boyack, K. W., & Klavans, R. (2010). Co-citation analysis, bibliographic coupling, and direct citation: Which citation approach represents the research front most accurately? *JASIST*, 61(12). Not searched.
- Anderson, A., McFarland, D., & Jurafsky, D. (2012). Towards a computational history of the ACL: 1980-2008. ACL workshop. Not searched; it would complement Hall et al. 2008.
- "Evaluation of unsupervised static topic models' emergence detection ability" (PeerJ Computer Science, 2025; PMC12192802). Seen in results, but its authors and volume were not shown. It notes that a global model "may overfit dominant research trends and fail to recognize smaller, emerging topics", which is very close to our hindsight point. It is worth verifying.
- BERTrend: Neural topic modeling for emerging trends detection (arXiv 2411.05930). Seen in results, authors not shown. It notes that there are no accepted benchmarks or ground truth for weak-signal detection.
- BackTrend: Evaluating scientific weak-signal prediction via backward reconstruction (arXiv 2609.24921, 2026). Seen in results, authors not shown. It says emerging-topic benchmarks mostly test detecting salient trends rather than identifying early ideas that later dominate.

I found **no** peer-reviewed work that directly quantifies how far a classification fitted with later data inflates emerging-topic counts or reverses trend conclusions. The specific search returned nothing on point. Leydesdorff (2002), Klavans & Boyack (2014) and the 2025 PeerJ paper come closest, conceptually or as an aside.

---

## (a) What this literature already knows

1. **Topics over time are routinely measured with one model fitted on the whole period.** Examples are Griffiths & Steyvers 2004, Hall et al. 2008, the "topics over time" use of BERTopic, and Waltman & van Eck 2012. Dynamic variants exist (Blei & Lafferty 2006; Wang & McCallum 2006; Chavalarias & Cointet 2013; Klavans & Boyack 2014), but most of them still use the whole period during fitting.
2. **Topic reconstructions are method-dependent constructs.** The same data give different thematic structures (Gläser et al. 2017), and no method reliably recovers ground-truth topics (Held et al. 2021).
3. **"Emerging" is defined partly by properties visible only later** (coherence, impact; Rotolo et al. 2015). Emergence detection and growth forecasting are active fields (Small et al. 2014; Klavans et al. 2020).
4. **Leakage of unavailable information inflates ML-based claims** (Kaufman et al. 2012; Kapoor & Narayanan 2023). Finance names this look-ahead bias and backtest overfitting (Bailey et al. 2017). Language models are time-indexed and decay out of period (Lazaridou et al. 2021).
5. **Classifications need dynamic updating as data arrive,** and re-fitted classifications re-read the past from hindsight (Leydesdorff 2002). This is stated conceptually.
6. **Credibility tools for observational and secondary data are well developed:**
   - preregistration (Nosek et al. 2018), including for existing data (Van den Akker et al. 2021);
   - multiverse and specification-curve robustness (Steegen et al. 2016; Simonsohn et al. 2020);
   - forking-paths awareness (Gelman & Loken 2014);
   - FWER control (Holm 1979);
   - small-cluster inference (Cameron et al. 2008).

## (b) What it does not know that our data can speak to

1. **How large hindsight distortion is in practice.** No found study holds the papers and the model fixed and varies only the fitting window. Ours does: emerging topics are 8 on the 2017-20 map and 29 on the all-years map, and the "topics age" conclusion reverses on the same papers (`presentation/script.md`, lines 102-104). Neither the leakage literature (prediction-focused) nor the scientometric mapping literature (validity against ground truth on a fixed period) has this temporal, descriptive quantification.
2. **Which substantive conclusions survive a hindsight-free check.** Our registered tests require each result to hold on the early and year-balanced maps; `RESULTS.md` (lines 745-748) marks "hindsight passes" or "hindsight fails" for each.
   - Survive and replicate on held-out papers: foundation-model adoption and fewer new-architecture papers (H1d); newcomers favouring method papers and avoiding benchmark papers (H2b′/H2c′).
   - Hindsight fails: crowding/maturity and acceptance (H3a).

   The literature has no examples of a field-history claim being sorted this way into hindsight-robust and hindsight-fragile.
3. **The reward side of topic dynamics under peer review, including rejected and withdrawn papers.** Topic-growth studies use citations of *published* work (Sjögårde & Didegah 2022). Emergence studies predict *volume* growth (Klavans et al. 2020). Neither observes the gatekeeper's decision on the full submission pool, dated as it was at the time.
4. **Preregistered, held-out confirmation for a science-of-science question in ML.** The preregistration literature gives templates (Van den Akker et al. 2021), but science-of-science and ACL "history of the field" papers rarely apply a frozen single run plus held-out replication. We can show which exploratory patterns survive (several replicated) and which do not (the federated-learning case was not confirmed).

## (c) Candidate framings our findings could contribute to

1. **"Writing a field's history without hindsight" (primary candidate).**
   - Core claim: a topic map is a model of the period it was fitted on. Fitting on the whole corpus leaks the future into the past, a measurement-side analogue of temporal leakage (Kaufman et al. 2012; Kapoor & Narayanan 2023) and look-ahead bias (finance).
   - Evidence: 8 versus 29 emerging topics, and the topics-age reversal.
   - Then the substantive findings become the payoff of a hindsight-free design. Each result is sorted by whether it survives dated measurement, a registered prediction, and held-out replication. FM adoption and fewer architecture papers, newcomers' method/benchmark pattern, insider and far-jump acceptance effects, and the weak keyword-timing effects are each sorted this way.
   - This unifies everything around one methodological-substantive line and positions us against Hall et al. 2008, Griffiths & Steyvers 2004 and BERTopic-style trend studies.
2. **"Temporal multiverse."** Extend multiverse and specification-curve thinking (Steegen et al. 2016; Simonsohn et al. 2020) with the fitting window as a forking path that standard multiverses omit. Report each claim's survival across maps as a credibility grade.
3. **"Waves seen at the time versus waves seen afterwards."** Contrast prospective emergence (what the field could see: early map, dated snapshots, lagged indicators as in Klavans et al. 2020) with retrospective emergence (Rotolo et al.'s coherence and impact). Our PH6 result fits here: the acceptance gap falls after a keyword's share peaks, which is only weakly supported (p 0.043). So does the young-rising-keyword premium, which is weak and replicated. Both show that the reward for riding a wave is small and time-bound when measured without hindsight.
4. **A preregistered and held-out science-of-science template for ACL/ML venues.** This is secondary. It is a methods contribution (sealed outcomes, single frozen run, held-out former test split) applying Van den Akker et al. (2021) to OpenReview data. It is better as a supporting contribution than as the story line.

Recommendation for the story line: framing 1, with framing 2 as its analytical device and framing 3 as the interpretation of the reward-side findings.
