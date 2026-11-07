# Literature notes: outsiders, newcomers and who brings new ideas

Area brief: who innovates (outsiders, newcomers, field switchers, marginal or underrepresented scientists) and how their innovations are received. Prepared for the ICLR 2017-2026 "riding the wave" paper.

Verification rule used: a work is listed as VERIFIED only when authors, title, year and venue (with volume/issue/pages, or article number, where applicable) were confirmed in at least one search result I saw (publisher, PubMed/PMC, IDEAS/RePEc, DOI resolver, university repository, NBER). Summaries are based only on what the search results showed (mostly abstracts and press/repository summaries; I did not read full texts). Where a detail was not confirmed, it is flagged.

Our own numbers quoted below come from the scratchpad dossier `/tmp/claude-0/-home-user-cloud-research/8f8bbb72-8d64-5b3e-bbfb-b57542d228a7/scratchpad/paper_ws/dossier_core.md` (line numbers given) or from the project context in the task brief.

Our findings this area speaks to (short labels used in "Relevance" lines):
- **F-NEWMETHOD**: newcomer papers (no author with an earlier ICLR submission in that topic) are more often method papers (+3.71 pp discovery; +3.60 pp held-out; dossier_core.md:296) and less often benchmark/dataset/evaluation papers (-1.70 pp; held-out -2.10 pp; dossier_core.md:297). This reversed the registered herding prediction.
- **F-NEWGAP**: newcomer papers are accepted less often within topic x year (-10.2 pp, planned exploratory E2; dossier_core.md:343); raw 37.2% vs 47.3% (dossier_core.md:417); most of the gap is about who writes newcomer papers, with author fixed effects shrinking it to about -3 pp and "author new to topic" to -1.4 pp (PH3; dossier_core.md:396).
- **F-INSIDER**: one topic insider in the team (vs none) goes with higher acceptance (+3.42 pp discovery, +3.88 pp held-out; dossier_core.md:374).
- **F-FARJUMP**: far jumps from a team's own past work go with lower acceptance (-5.44 pp discovery, -6.09 pp held-out; dossier_core.md:370).
- **F-WAVES / F-CROWD / F-YOUNGKW / F-PEAK**: hindsight maps manufacture waves; crowding inconclusive; young rising keywords modestly favoured; a keyword's acceptance gap falls after its share peaks (from task brief).

---

## VERIFIED WORKS

### A. Outsiders and marginal actors as sources of novelty

**1. Jeppesen, L. B., & Lakhani, K. R. (2010). Marginality and problem-solving effectiveness in broadcast search. *Organization Science*, 21(5), 1016-1033. doi:10.1287/orsc.1090.0491.**
Key: `jeppesen2010marginality`
- What it did: 166 science challenges broadcast on an open innovation platform (InnoCentive) to over 12,000 scientists. The probability of a winning solution rose with the distance between the solver's field of technical expertise and the problem's field ("technical marginality"); female solvers, outsiders to the scientific establishment ("social marginality"), did significantly better than men.
- Verified via: IDEAS/RePEc (v21 i5 p1016-1033), INFORMS DOI page, Harvard DASH.
- Relevance to us: Canonical evidence that outsiders produce the solution-type contributions. Frames **F-NEWMETHOD**: topic newcomers at ICLR disproportionately submit *method* papers (proposed solutions), not benchmarks. Contrast: in broadcast search a neutral seeker judges solutions on merit; at ICLR peers judge, and newcomers are accepted less (**F-NEWGAP**). Not closest prior (different setting), but the anchor citation for "outsiders solve".

**2. Azoulay, P., Fons-Rosen, C., & Graff Zivin, J. S. (2019). Does science advance one funeral at a time? *American Economic Review*, 109(8), 2889-2920.**
Key: `azoulay2019does`
- What it did: 452 eminent life scientists who died prematurely (1975-2003). After a star's death, publications by the star's collaborators drop sharply (about 40% per NBER digest), while non-collaborators enter the field (roughly 8-8.6% more articles; sources differ) and their contributions are disproportionately highly cited. The entrants are outsiders who tackle the field's mainstream questions with ideas from other domains; deliberate gatekeeping by stars (editorships, grant panels) is ruled out as the main mechanism, the authors argue outsiders were reluctant to challenge incumbents.
- Verified via: IDEAS/RePEc listing (AER 109(8) 2889-2920), NBER WP 21788 and NBER digest.
- Relevance to us: The closest canonical study of *incumbents shaping where outsiders can enter*. Frames **F-NEWGAP** and **F-INSIDER** (outsider entry is possible but costly while incumbents hold the field) and **F-PEAK** (once a keyword's share peaks, the incumbent premium may erode, analogous to the post-funeral opening). Frames, not closest prior.

**3. Hofstra, B., Kulkarni, V. V., Munoz-Najar Galvez, S., He, B., Jurafsky, D., & McFarland, D. A. (2020). The diversity-innovation paradox in science. *Proceedings of the National Academy of Sciences*, 117(17), 9284-9291. doi:10.1073/pnas.1915378117.**
Key: `hofstra2020diversity`
- What it did: Near-complete population of about 1.2 million US doctoral recipients 1977-2015 (ProQuest dissertations) linked to publication and career records; text-based novelty measures (new conceptual linkages). Underrepresented groups produce higher rates of scientific novelty, but their novel contributions are discounted (taken up less and yielding less career success), which the authors read as reproduction of stratification.
- Verified via: PMC (PMC7196824), Stanford STS publication page, PubMed record. ("Discounted" is the authors' term in the summaries I saw; the exact uptake measure was not shown.)
- Relevance to us: The single most important framing for our whole area: *those at the margin innovate more, but the system rewards them less.* Our ICLR data show the same structure on a different margin (topic incumbency rather than demographics): newcomers bring methods (**F-NEWMETHOD**) and are accepted less (**F-NEWGAP**). Closest prior *in framing* (a "newcomer-novelty paradox" analogue); uses NLP on text like us.

**4. Painter, D. T., Daniels, B. C., & Laubichler, M. D. (2021). Innovations are disproportionately likely in the periphery of a scientific network. *Theory in Biosciences*, 140(4), 391-399. doi:10.1007/s12064-021-00359-1.**
Key: `painter2021innovations`
- What it did: Automated analysis of a corpus of over 6,000 documents covering all of evolutionary medicine; innovations defined by novelty plus persistence; bibliographic coupling network with core-periphery structure. Innovations are disproportionately located in the network periphery; the authors suggest loose ties to established lines of work help produce lasting novelty.
- Verified via: ASU Elsevier Pure record (vol 140, no 4, pp 391-399), NSF PAR record, DOI. Note: a search query with a wrong author list was corrected by the result (van der Wouden and Youn are co-authors of a different 2020 paper).
- Relevance to us: Direct evidence of "innovation from the periphery" at the field level in a single specialty, using text/citation structure. Supports **F-NEWMETHOD**. It does not study reception by peer review, which our acceptance data can.

**5. Cattani, G., & Ferriani, S. (2008). A core/periphery perspective on individual creative performance: Social networks and cinematic achievements in the Hollywood film industry. *Organization Science*, 19(6), 824-844. doi:10.1287/orsc.1070.0350.**
Key: `cattani2008core`
- What it did: Hollywood core crew members on major-studio films 1992-2003; network coreness vs creative recognition. Individuals at intermediate core/periphery positions perform best (inverse U), and the same benefit appears at team level when a team mixes members from both the core and the periphery.
- Verified via: IDEAS/RePEc (v19 i6 p824-844), INFORMS DOI, City Research Online, Bologna repository.
- Relevance to us: The best theoretical frame for **F-INSIDER**: teams that combine a topic insider with outsiders do better than all-outsider teams. Also consistent with **F-FARJUMP** (too peripheral a move is penalised). Frames; not closest prior.

### B. Newcomers, career age and new ideas

**6. Packalen, M., & Bhattacharya, J. (2019). Age and the trying out of new ideas. *Journal of Human Capital*, 13(2), 341-373. doi:10.1086/703160.**
Key: `packalen2019age`
- What it did: Text-based measure of new ideas in nearly all biomedical articles since 1946. Papers by younger (career-age) researchers are more likely to build on new ideas; the probability peaks within a few years of the first paper. Papers with a young first author and an experienced last author are more likely to try newer ideas than other team configurations.
- Verified via: University of Chicago Press DOI page, NBER WP 20920.
- Relevance to us: Supports **F-NEWMETHOD** (newcomers bring new ideas) and, through the young-plus-experienced team result, **F-INSIDER**. Note our "newcomer" is topic-specific, not career age.

**7. Sekara, V., Deville, P., Ahnert, S. E., Barabasi, A.-L., Sinatra, R., & Lehmann, S. (2018). The chaperone effect in scientific publishing. *Proceedings of the National Academy of Sciences*, 115(50), 12603-12607. doi:10.1073/pnas.1800471115.**
Key: `sekara2018chaperone`
- What it did: Follows how scientists become last (senior) authors in specific journals including Nature, Science and PNAS. Many new PIs in a venue were previously non-PI coauthors there ("chaperoned"); the effect is stronger in medical and biological sciences, and chaperoned papers have higher average impact than papers by new PIs in high-impact venues.
- Verified via: Network Science Institute and CEU publication pages, PNAS issue listing.
- Relevance to us: Closest prior for **F-INSIDER**: entry into a venue (here: a topic at ICLR) is easier with someone already inside. Our result is the topic-level, acceptance-based analogue with held-out replication. Closest prior work for that finding.

**8. Arts, S., & Fleming, L. (2018). Paradise of novelty-or loss of human capital? Exploring new fields and inventive output. *Organization Science*, 29(6), 1074-1092. doi:10.1287/orsc.2018.1216.**
Key: `arts2018paradise`
- What it did: Inventor-firm fixed-effects panel of patents. Inventors exploring new fields produce more novel output (new combinations) but of lower value (citations); the value loss is smaller when the novice works with experts or draws on the new field's scientific literature.
- Verified via: IDEAS/RePEc (v29 i6 p1074-1092), INFORMS supplement page with DOI.
- Relevance to us: Very close mechanism for three findings at once: newcomers produce novelty (**F-NEWMETHOD**), novelty from field entry is valued less (**F-NEWGAP**, **F-FARJUMP**), and collaborating with experts mitigates the loss (**F-INSIDER**). Closest prior work in mechanism (patents, not peer review).

### C. Field switching and topic mobility

**9. Hill, R., Yin, Y., Stein, C., Wang, X., Wang, D., & Jones, B. F. (2025). The pivot penalty in research. *Nature*, 642(8069), 999-1006. doi:10.1038/s41586-025-09048-1.**
Key: `hill2025pivot`
- What it did: About 25.8 million papers (1970-2015) and 1.7 million US patents (1985-2015). The further a researcher moves from their prior work, the lower the impact of the new work ("pivot penalty"); the penalty is pervasive, has grown over five decades, appears at all career stages, and held for researchers who pivoted to COVID-19.
- Verified via: IDEAS/RePEc (Nature v642 i8069), Kellogg research page, Times Higher Education report.
- Relevance to us: Closest prior work for **F-FARJUMP**. They measure citations after publication; we measure the gatekeeping step (acceptance) with a registered held-out test, in one fast-moving venue. Our result is the peer-review counterpart of the pivot penalty.

**10. Zeng, A., Shen, Z., Zhou, J., Fan, Y., Di, Z., Wang, Y., Stanley, H. E., & Havlin, S. (2019). Increasing trend of scientists to switch between topics. *Nature Communications*, 10, 3439. doi:10.1038/s41467-019-11401-8.**
Key: `zeng2019increasing`
- What it did: Topics per scientist identified as communities in each scientist's co-citing network of papers. Scientists work on a narrow range of topics, but switching has become more frequent over time; high switching early in a career goes with lower overall productivity and later with higher productivity, while citations per paper are negatively correlated with switching at all career stages.
- Verified via: PMC (PMC6668429), IDEAS/RePEc, DOAJ.
- Relevance to us: Supports **F-FARJUMP** (switching costs impact) and explains why our corpus has a high newcomer share (72.9% of RQ2 papers are newcomer papers; dossier_core.md:151): topic entry is the norm in a fast-growing field. Frames.

**11. Jia, T., Wang, D., & Szymanski, B. K. (2017). Quantifying patterns of research-interest evolution. *Nature Human Behaviour*, 1(4), 0078. doi:10.1038/s41562-017-0078.**
Key: `jia2017quantifying`
- What it did: About 14,715 physicists' publication records in APS journals over 30 years. Few scientists move far from their original focus; those who move do so gradually; changes in interest follow an exponential distribution, consistent with a random-walk-like model with heterogeneity and recency.
- Verified via: IDEAS/RePEc (v1 i4), Kellogg research page, RPI news.
- Relevance to us: Background for **F-FARJUMP**: far jumps are rare, so their penalty is estimated on a selected minority. Frames.

**12. Leahey, E., Beckman, C. M., & Stanko, T. L. (2017). Prominent but less productive: The impact of interdisciplinarity on scientists' research. *Administrative Science Quarterly*, 62(1), 105-139. doi:10.1177/0001839216665364.**
Key: `leahey2017prominent`
- What it did: Scientists' publication records; interdisciplinary research raises visibility (citations) but lowers productivity, a trade-off.
- Verified via: University of Arizona sociology CV listing (ASQ 62(1) 105-139, DOI), Beckman's site, arXiv preprint. (One blog dates it 2016, the online-first year.)
- Relevance to us: Frames **F-FARJUMP** as a cost of spanning boundaries; note the outcome (citations up) differs from our gatekeeping outcome (acceptance down). Frames.

### D. Novelty, risk and how it is received

**13. Foster, J. G., Rzhetsky, A., & Evans, J. A. (2015). Tradition and innovation in scientists' research strategies. *American Sociological Review*, 80(5), 875-908 (start page verified; end page not seen in a search result). doi:10.1177/0003122415601618.**
Key: `foster2015tradition`
- What it did: Millions of biomedical/chemistry abstracts represented as networks of chemicals and relations; strategies classified as tradition (deepening known links) vs innovation (new chemicals/links). The distribution of strategies is stable; risky innovation is rare; it is more often ignored but more likely to achieve high impact, and the extra reward does not compensate for the extra risk. Framed in Bourdieu's field theory and Kuhn's "essential tension".
- Verified via: Scinapse record, UChicago Knowledge Lab page, ScienceDaily, arXiv 1302.6906.
- Relevance to us: Frames the incentive structure behind **F-NEWMETHOD** and **F-NEWGAP**: incumbents rationally stay with tradition (including benchmarks/evaluations that consolidate a topic), while newcomers take risky method bets. Frames.

**14. Wang, J., Veugelers, R., & Stephan, P. (2017). Bias against novelty in science: A cautionary tale for users of bibliometric indicators. *Research Policy*, 46(8), 1416-1436. doi:10.1016/j.respol.2017.06.006.**
Key: `wang2017bias`
- What it did: Web of Science articles; novelty as new combinations of referenced journals. Novel papers are more likely to be top-cited in the long run but less likely in short windows, and they appear in lower-impact-factor journals than expected.
- Verified via: Lancaster and KU Leuven repositories, NBER WP 22180.
- Relevance to us: Frames **F-NEWGAP** and **F-FARJUMP** as possible short-horizon penalties on novelty; peer review at a conference is an extreme "short window". Frames.

**15. Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). Atypical combinations and scientific impact. *Science*, 342, 468-472.**
Key: `uzzi2013atypical`
- What it did: 17.9 million Web of Science papers. The highest-impact work combines mostly conventional combinations of prior work with a small intrusion of atypical combinations; teams are more likely than solo authors to insert novel combinations into familiar domains (37.7% per the search summary).
- Verified via: Kellogg faculty PDF and research page.
- Relevance to us: Frames **F-INSIDER** and **F-FARJUMP**: conventional grounding (an insider, a nearby topic) plus a little novelty is the rewarded mix. Issue number and DOI not seen in results, so omitted.

**16. Boudreau, K. J., Guinan, E. C., Lakhani, K. R., & Riedl, C. (2016). Looking across and looking beyond the knowledge frontier: Intellectual distance, novelty, and resource allocation in science. *Management Science*, 62(10), 2765-2783. doi:10.1287/mnsc.2015.2285.**
Key: `boudreau2016looking`
- What it did: Field experiment on evaluation of research grant proposals (randomly assigned evaluators at a medical school). Evaluators systematically give lower scores to more novel proposals and to proposals closer to their own expertise (as reported in the paper; the search result confirmed the evaluation-of-frontier-projects framing, keywords novelty and intellectual distance).
- Verified via: IDEAS/RePEc (v62 i10 p2765-2783), INFORMS DOI.
- Relevance to us: Frames **F-NEWGAP** / **F-FARJUMP** as an evaluator-side novelty discount. Caution: the specific direction of the intellectual-distance effect was not shown in the search snippet I saw; cite it for the "evaluators discount novelty" claim only after checking the abstract.

### E. Peer review, status and proximity of evaluators

**17. Merton, R. K. (1968). The Matthew effect in science. *Science*, 159(3810), 56-63. doi:10.1126/science.159.3810.56.**
Key: `merton1968matthew`
- What it did: Theoretical essay: eminent scientists get disproportionate credit for joint or multiple discoveries, and contributions by recognised scientists are more visible than those by less-known authors.
- Verified via: PubMed (5634379).
- Relevance to us: Canonical frame for **F-NEWGAP** and **F-INSIDER** (recognition flows to those already inside). Frames.

**18. Tomkins, A., Zhang, M., & Heavlin, W. D. (2017). Reviewer bias in single- versus double-blind peer review. *Proceedings of the National Academy of Sciences*, 114(48), 12708-12713. doi:10.1073/pnas.1707323114.**
Key: `tomkins2017reviewer`
- What it did: WSDM 2017 submissions, each reviewed by two single-blind and two double-blind PC members. Single-blind reviewers gave a significant advantage to papers by famous authors and from top institutions; a gender effect was not significant. A later critique (arXiv 1912.13188, Stelmakh, Shah and Singh) argues the test can declare bias when none exists.
- Verified via: PMC (PMC5715744), Google Research blog.
- Relevance to us: Frames **F-NEWGAP**: status advantages exist in CS conference review. ICLR is double-blind since 2018, so any insider advantage we see must operate through content, framing, or de-anonymisation (e.g. preprints), not names on the PDF. Frames.

**19. Sun, M., Barry Danfa, J., & Teplitskiy, M. (2022). Does double-blind peer review reduce bias? Evidence from a top computer science conference. *Journal of the Association for Information Science and Technology*, 73(6), 811-819. doi:10.1002/asi.24582.**
Key: `sun2022does`
- What it did: Review files for 5,027 ICLR submissions around ICLR's 2018 switch from single- to double-blind review. Scores for the most prestigious authors fell after the switch; acceptance was not significantly affected; inter-reviewer disagreement rose; papers rejected under single-blind were later cited more than those rejected under double-blind.
- Verified via: IDEAS/RePEc (jinfst v73 i6 p811-819), arXiv 2101.02701.
- Relevance to us: Closest prior work on *our venue* about author status and review. It concerns prestige, not topic incumbency; our **F-NEWGAP** and **F-INSIDER** extend it to topic-level insider/outsider status under double-blind review, with author fixed effects (PH3) separating person from position.

**20. Li, D. (2017). Expertise versus bias in evaluation: Evidence from the NIH. *American Economic Journal: Applied Economics*, 9(2), 60-92. doi:10.1257/app.20150421.**
Key: `li2017expertise`
- What it did: Over 100,000 NIH grant applications. Reviewers are biased in favour of applications in their own area but also better informed about them; overall, expertise outweighs bias, so recusing close reviewers could lower decision quality.
- Verified via: IDEAS/RePEc (aejapp v9 i2 p60-92), Kellogg Insight.
- Relevance to us: Offers the main rival interpretation of **F-INSIDER** and **F-NEWGAP**: an insider advantage may reflect better-informed evaluation (and better-crafted papers), not only favouritism. Frames.

**21. Teplitskiy, M., Acuna, D., Elamrani-Raoult, A., Kording, K., & Evans, J. (2018). The sociology of scientific validity: How professional networks shape judgement in peer review. *Research Policy*, 47(9), 1825-1841.**
Key: `teplitskiy2018sociology`
- What it did: Reviews at a journal (PLOS ONE per the preprint) that accepts all scientifically valid work. Reviewers who had co-authored with a manuscript's author scored it about 0.42 points better than reviewers at co-authorship distance 3+; distance 2 about 0.09 better. Recusing close reviewers does not remove the bias; the authors recommend reviewers from diverse networks.
- Verified via: IDEAS/RePEc (respol v47 i9 p1825-1841), CU Boulder record; effect sizes from arXiv 1802.01270 summary.
- Relevance to us: Mechanism for **F-INSIDER** (proximity to the reviewer pool raises scores). Frames.

### F. Specialty formation and intellectual movements

**22. Crane, D. (1972). *Invisible Colleges: Diffusion of Knowledge in Scientific Communities*. Chicago: University of Chicago Press.**
Key: `crane1972invisible`
- What it did: Book on how informal communication networks among researchers ("invisible colleges") carry the social diffusion of knowledge that fuels the growth of scientific specialties (as described in the search results; the book's growth-curve details were not seen in a search result).
- Verified via: CiNii, Cambridge (Medical History review), KIT catalogue (x, 213 p.), Nature review (1973, vol 241, p 76).
- Relevance to us: Frames the topic life cycle (**F-WAVES**, **F-PEAK**, **F-YOUNGKW**) and **F-INSIDER**: a topic's insider network is an invisible college that newcomers must connect to. Frames.

**23. Mullins, N. C. (1972). The development of a scientific specialty: The phage group and the origins of molecular biology. *Minerva*, 10(1), 51-82. doi:10.1007/BF01881390.**
Key: `mullins1972development`
- What it did: Case study of how the phage group grew from a loose network into a cluster and then an institutionalised specialty (stage model of specialty development). Content details not seen in search results; the stage-model description is from general knowledge of the literature and should be checked against the text.
- Verified via: Springer DOI record, National Academies Biographical Memoirs citation, Hayes 1985 citation (Minerva 10: 51-82). Issue "1" is from the Memoirs listing.
- Relevance to us: Frames topic life cycles (**F-WAVES**, **F-PEAK**): as a specialty consolidates, insiders dominate. Frames.

**24. Ben-David, J., & Collins, R. (1966). Social factors in the origins of a new science: The case of psychology. *American Sociological Review*, 31(4), 451-465.**
Key: `bendavid1966social`
- What it did: Historical-comparative account of the origins of experimental psychology. (Abstract not available in search results; the article is widely associated with "role hybridization", in which mobile scientists from an established field carry its methods into a new area, but this link was NOT confirmed in a search result I saw.)
- Verified via: PubMed (5329541), Makerere library catalogue.
- Relevance to us: Potential frame for **F-NEWMETHOD** (entrants import methods). Cite cautiously until the role-hybridization claim is checked against the text.

**25. Frickel, S., & Gross, N. (2005). A general theory of scientific/intellectual movements. *American Sociological Review*, 70(2), 204-232.**
Key: `frickel2005general`
- What it did: Theory article: defines scientific/intellectual movements (SIMs), borrowing from social movement theory, and offers four propositions on when SIMs emerge, gain prestige and become institutionalised (among them, that SIMs are more likely when high-status actors have grievances against the dominant intellectual agenda, and that success depends on access to resources and micromobilisation contexts; the specific propositions were not shown in the search snippets).
- Verified via: bibbase, Scinapse, Stafforini, Canadian Journal of Sociology review.
- Relevance to us: Frames **F-WAVES** and the foundation-model shift as a movement, and the question of whether movements are carried by outsiders or by status-holding insiders (**F-INSIDER**). Frames.

**26. Gieryn, T. F. (1978). Problem retention and problem change in science. *Sociological Inquiry*, 48(3-4), 96-115.**
Key: `gieryn1978problem`
- What it did: Early study of how scientists choose, retain and change research problems. Content not seen in search results. (Issue numbering "3-4" is from general knowledge and not seen; the search confirmed vol 48 (1978), pp. 96-115.)
- Relevance to us: Classic antecedent for **F-FARJUMP** (problem change). Frames. Cite with vol/pages only.

**27. Chu, J. S. G., & Evans, J. A. (2021). Slowed canonical progress in large fields of science. *Proceedings of the National Academy of Sciences*, 118(41), e2021636118. doi:10.1073/pnas.2021636118.**
Key: `chu2021slowed`
- What it did: 1.8 billion citations to 90 million papers (1960-2014). In fields publishing many papers per year, citations concentrate on already-canonical papers and new papers rarely rise into the canon; the authors argue that fast growth entrenches incumbents.
- Verified via: IDEAS/RePEc, PMC (PMC8522281).
- Relevance to us: Frames **F-CROWD** (crowding inconclusive for acceptance) and **F-PEAK**: in a field growing as fast as ICLR, one would expect entrenchment; our results show where entrants do and do not get through. Frames.

### G. Our venue

**28. Zhang, J., Zhang, H., Deng, Z., & Roth, D. (2022). Investigating fairness disparities in peer review: A language model enhanced approach. arXiv:2211.06398.**
Key: `zhang2022investigating`
- What it did: Builds a relational database of ICLR submissions (2017 onward) from OpenReview, Google Scholar, arXiv and CSRankings, and studies disparities in review outcomes by author and institution attributes, using language-model features of the text.
- Verified as an arXiv preprint (authors, title, year, arXiv id). No peer-reviewed venue seen.
- Relevance to us: Closest prior *dataset* (ICLR OpenReview with rejected papers). It studies fairness by author attributes; it does not study topic incumbency, contribution type or topic life cycles. Our data differ (dated snapshots, withdrawn papers, held-out split).

---

## UNVERIFIED OR PARTLY VERIFIED CANDIDATES (do not cite as verified)

- **Leahey, E. (2007). Not by productivity alone: How visibility and specialization contribute to academic earnings. *American Sociological Review*, 72(4).** Authors, title, year, journal and issue confirmed (University of Arizona expert record), but pages (533-561 from memory) and DOI were NOT confirmed. Relevance: specialization raises productivity and pay, so staying in one's topic is rewarded (frames **F-FARJUMP**, **F-INSIDER**).
- **Vicinanza, P., Goldberg, A., & Srivastava, S. B. (2023). A deep learning model of prescient ideas demonstrates that they emerge from the periphery. *PNAS Nexus*.** Authors, title, journal and year confirmed via Berkeley Haas faculty PDF and newsroom; volume, issue and article number NOT confirmed (searched "pgac275", no match). Content: BERT-based prescience measure on about five million congressional speeches, about 4.2 million court decisions and 108,000 earnings calls; prescient ideas more likely from the periphery (state appellate courts vs Supreme Court; small vs large firms). Strong candidate for the "periphery innovates" frame (not science).
- **Stelmakh, I., Shah, N. B., & Singh, A. (2019/2021). On testing for biases in peer review.** arXiv 1912.13188 seen; final venue (NeurIPS 2019) not confirmed. Critique of Tomkins et al.'s test.
- **Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*.** Not searched; the classic claim that new paradigms come from the young or from those new to the field. Verify before citing.
- **Klinger, Mateos-Garcia & Stathoulopoulos (2020), "A narrowing of AI research?"; Koch, Denton, Hanna & Foster (2021), "Reduced, reused and recycled: The life of a dataset in machine learning research".** Not searched in this area; likely covered by another literature area (ML field dynamics / benchmarks).
- **Study showing innovation from the periphery with recognition flowing to the core.** No single verified study found that tracks an idea originating at the periphery and the *credit* subsequently accruing to core actors. The closest pieces are: Merton 1968 (credit flows to the eminent), Hofstra et al. 2020 (novelty by underrepresented scholars is discounted), Azoulay et al. 2019 (outsiders held back while incumbents are present), Vicinanza et al. 2023 (prescient ideas from periphery; unverified issue). This is a gap our data can partly address (see (b)).

---

## (a) What this literature already knows

1. Outsiders and marginal actors produce disproportionate novelty: technical and social marginality wins broadcast contests (Jeppesen and Lakhani 2010); underrepresented PhDs introduce more novel concepts (Hofstra et al. 2020); innovations sit in the periphery of a field's citation network (Painter et al. 2021); early-career researchers try newer ideas (Packalen and Bhattacharya 2019); inventors entering a new field produce more novel combinations (Arts and Fleming 2018).
2. Novelty from the margin is under-rewarded: Hofstra et al. 2020 (discounting), Wang, Veugelers and Stephan 2017 (short-window citation penalty), Foster, Rzhetsky and Evans 2015 (risk not compensated), Arts and Fleming 2018 (lower value), Merton 1968 (credit flows to the eminent).
3. Moving away from one's own past work costs impact: pivot penalty (Hill et al. 2025), switching and citations (Zeng et al. 2019), rarity and gradualness of moves (Jia, Wang and Szymanski 2017), interdisciplinarity trade-offs (Leahey, Beckman and Stanko 2017).
4. Connection to insiders helps entry: chaperone effect (Sekara et al. 2018), young-plus-experienced teams (Packalen and Bhattacharya 2019), novices with experts lose less value (Arts and Fleming 2018), mixed core/periphery teams perform best (Cattani and Ferriani 2008).
5. Evaluators are not neutral to proximity and status: famous-author advantage in single-blind review (Tomkins et al. 2017), prestige effect at ICLR before double-blind (Sun et al. 2022), co-author proximity bias (Teplitskiy et al. 2018), own-area bias that is partly informational (Li 2017).
6. Incumbents shape when outsiders can enter (Azoulay et al. 2019); large fast-growing fields entrench the canon (Chu and Evans 2021); specialties grow through invisible colleges and stage-wise consolidation (Crane 1972; Mullins 1972).

## (b) What it does not know that our data can speak to

1. **Which kind of contribution newcomers bring.** Prior work measures novelty (new combinations, new concepts) but not the *type* of contribution. Our codebook shows newcomers bring proposals (methods) while incumbents consolidate (benchmarks, datasets, evaluations), replicated on held-out papers. This is a division of labour between entrants and incumbents within a topic, not just "more novelty at the margin".
2. **Reception at the gate, including the rejected.** Nearly all prior reception evidence uses citations of published work (survivor bias) or grant panels. We observe acceptance and rejection, including withdrawn papers, at a double-blind venue, so we can measure the newcomer discount at the gatekeeping step itself.
3. **Topic-level incumbency rather than demographic or career-age marginality.** Hofstra et al. measure demographic marginality; Packalen and Bhattacharya career age. Our newcomer is relative to a topic, so the same person can be insider in one topic and outsider in another; author fixed effects (PH3) show most of the gap is about who writes newcomer papers, with a small within-person cost of entering a new topic.
4. **Team composition as a bridge under double-blind review.** Chaperone and core/periphery-team effects have not been shown for acceptance under double-blind review; our one-insider premium, replicated on held-out papers, is that test.
5. **The pivot penalty at the gate.** Hill et al. show citation penalties; our far-jump result shows the penalty already appears at acceptance, and replicates on held-out papers.
6. **Timing.** The literature rarely conditions reception on where a topic is in its life cycle. Our keyword timing results (young rising keywords modestly favoured; acceptance gap falls after share peaks) and the hindsight-map warning (waves manufactured by hindsight topic maps) speak to *when* outsiders' and insiders' contributions are rewarded, and warn that life-cycle measures need prospective topic maps.
7. **Registered and replicated tests.** Most of this literature is observational without pre-registration or held-out replication; our design gives a credibility upgrade (and a reversed registered prediction).

## (c) Candidate framings our findings could contribute to

1. **"A newcomer-novelty paradox at the gate" (strongest).** Extend Hofstra et al.'s diversity-innovation paradox from demographic margins to topic margins in a fast-moving field: entrants supply the methods (the new ideas), incumbents supply the benchmarks that consolidate a topic, and the gate rewards incumbency and insider ties. All the newcomer, insider and far-jump findings hang from this, and the reversed herding prediction becomes a headline (entrants are not herders; they are proposers).
2. **"Division of labour in topic life cycles."** Newcomers propose, insiders measure and consolidate (Crane, Mullins, Frickel and Gross). Combine with keyword timing (young rising keywords favoured; premium falls after peak) and with the hindsight-map warning to argue that topic life cycles must be measured prospectively, and that who contributes what changes over the cycle.
3. **"Bridging, not jumping."** Read the far-jump penalty and one-insider premium together as the gate-level counterpart of the pivot penalty and the chaperone effect: ideas from outside get through when carried by a team with a foothold, not when the team leaps (Cattani and Ferriani's mixed core/periphery teams; Arts and Fleming's novices-with-experts).
4. **"Status without names."** ICLR is double-blind (Sun et al. 2022), yet topic insiders still fare better. Li (2017) and Teplitskiy et al. (2018) offer the competing explanations (informed evaluation vs proximity bias); PH3 author fixed effects let us say how much is person versus position.
5. Caution for any framing: our newcomer measure is ICLR-only and has a 2021 ID switch that biases incumbency towards zero (dossier_core.md:146, 149), so a senior researcher from another venue counts as a newcomer; the framing should say "new to this topic at this venue", not "junior".
