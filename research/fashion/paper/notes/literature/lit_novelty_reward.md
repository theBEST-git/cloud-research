# Literature notes: Novelty, tradition and reward in science

Area brief: science of science on tradition vs innovation, novelty and how it is received, conservatism of evaluation
and peer review, cumulative advantage, timing of entry into a field, crowding and competition.

Verification rule used: a work is listed as VERIFIED only if authors, title, year and venue (with volume/issue/pages
where applicable) were seen in at least one reliable search result (publisher page, PubMed/PMC, IDEAS/RePEc,
NBER, institutional repository, DBLP/ACL Anthology). All searches were run on 2026-11-03 with WebSearch (standard
mode). Summaries below are based only on the abstracts, snippets and summaries seen in those results; effect sizes are
quoted only where a result stated them. Where a detail was not seen (or sources disagreed), it is flagged.

Numbers about OUR study quoted in "Relevance to us" lines come from
`/tmp/claude-0/-home-user-cloud-research/8f8bbb72-8d64-5b3e-bbfb-b57542d228a7/scratchpad/paper_ws/dossier_core.md`
(line numbers given), which itself cites RESULTS.md; otherwise findings are described qualitatively as in the task brief.

Tiering: **[CORE]** = should be cited in the paper's framing/related-work; **[SUPPORT]** = cite if space allows or
in a specific results paragraph. **CLOSEST PRIOR** is marked where relevant.

---

## A. Classic theory: tradition, innovation, reward, priority, fashion

### A1. Kuhn 1962 — The Structure of Scientific Revolutions [CORE]
Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. Chicago: University of Chicago Press. (Issued as
International Encyclopedia of Unified Science, Vol. II, No. 2; xv + 172 pp. per a library record.)
BibTeX key: `kuhn1962structure`
- What it did: Theory of science as long periods of "normal science" (puzzle solving inside a shared paradigm)
  punctuated by revolutions. Verified only bibliographic facts from catalogue/bookseller results (publisher, year,
  series); content summary is the standard one.
- Relevance to us: Frames the foundation-model finding (FM adoption goes with fewer new-architecture papers,
  replicated): once a paradigm (pretrained foundation model) is adopted, work shifts from building new architectures to
  puzzle-solving on top of the paradigm. Also frames the "waves" story: paradigm adoption produces visible surges in
  topics. Use with care: we do not observe revolutions, only the composition of submissions.

### A2. Kuhn 1977 — The Essential Tension [CORE]
Kuhn, T. S. (1977). *The Essential Tension: Selected Studies in Scientific Tradition and Change*. Chicago: University of
Chicago Press. (ISBN 0226458069; 14 essays in historiographic and metahistorical sections; the title essay
"The Essential Tension: Tradition and Innovation in Scientific Research" is chapter 9 per the table of contents seen.)
BibTeX key: `kuhn1977essential`
- What it did: Collection of essays; the title essay argues that productive science requires both convergent
  thinking (deep commitment to a tradition) and divergent thinking (openness to innovation), and that this tension is
  essential rather than a defect.
- Relevance to us: The single most natural umbrella for our story. Our acceptance results look like the essential
  tension operating at the gate of a selective venue: novelty is rewarded when it is anchored in tradition (one topic
  insider on the team goes with higher acceptance; far jumps from a team's own past work go with lower acceptance;
  young rising keywords are modestly favoured, but the premium falls after a keyword's share peaks). The newcomer
  finding (newcomers write more method papers, fewer benchmark papers) shows the divergent side entering through
  outsiders. Foster et al. 2015 explicitly operationalise this essay; we can be the evaluation-side counterpart.

### A3. Merton 1968 — The Matthew Effect in Science [CORE]
Merton, R. K. (1968). The Matthew Effect in Science. *Science*, 159(3810), 56–63. (PMID 5634379; subtitle "The reward
and communication systems of science are considered".)
BibTeX key: `merton1968matthew`
- What it did: Argues eminent scientists receive disproportionate credit for comparable contributions (joint work,
  multiple discoveries), and that the communication system makes work by well-known scientists more visible. Drew on
  Zuckerman's interviews with Nobel laureates (acknowledged in Merton 1988, seen in the same results).
- Relevance to us: Frames the insider and newcomer acceptance gaps. In our data newcomer papers are accepted less
  often within topic x year (−10.2 pp, dossier_core.md L343) and most of that gap is "who writes the papers" (team size,
  experience; PH3, dossier_core.md L396). ICLR review is double-blind, so a pure name-recognition Matthew effect is
  muted; what remains is closer to cumulative advantage in skill/tacit knowledge (Li 2017's "expertise" side) than
  to status bias. Do not overclaim: we cannot separate the two.

### A4. Merton 1957 — Priorities in Scientific Discovery [SUPPORT]
Merton, R. K. (1957). Priorities in Scientific Discovery: A Chapter in the Sociology of Science. *American Sociological
Review*, 22(6), 635–659. (ASA presidential address.)
BibTeX key: `merton1957priorities`
- What it did: Argues that the reward system of science is organised around priority (being first), which explains
  priority disputes and the intensity of competition for recognition; multiple discoveries are common.
- Relevance to us: The theoretical root of "timing of entry" and races. Supports reading PH6 (acceptance gap of a
  keyword is high early and falls after its share peaks) and the young-rising-keyword premium as a priority-style
  reward observed at the evaluation stage: reviewers reward being early on a rising theme, not being on it per se.

### A5. Price 1976 — Cumulative advantage processes [SUPPORT]
Price, D. de S. (1976). A general theory of bibliometric and other cumulative advantage processes. *Journal of the
American Society for Information Science*, 27(5), 292–306. doi:10.1002/asi.4630270505
BibTeX key: `price1976general`
- What it did: Formal model in which success breeds success (Cumulative Advantage Distribution, related to Pólya urn
  schemes); origin of what is now called preferential attachment.
- Relevance to us: Formal backbone for both Newman 2009 (first-mover advantage) and for treating topic insiders as
  holders of accumulated advantage. Cite in one line alongside Merton 1968.

### A6. Crane 1969 — Fashion in Science: Does It Exist? [SUPPORT; check pages]
Crane, D. (1969). Fashion in Science: Does It Exist? *Social Problems*, 16(4), 433–4xx. (Spring 1969 issue confirmed by
a Price letter in an NLM digital repository; volume 16 and start page 433 confirmed; one reference list gives end page
444, the brief gave 441 — **end page not confirmed**, check before camera-ready.)
BibTeX key: `crane1969fashion`
- What it did: Not seen in results (no abstract retrieved). Known as an early sociological treatment of whether
  research topics follow fashion-like dynamics. Bernard Barber (1969, Mens en Maatschappij) wrote a separate paper on
  the functions and dysfunctions of "fashion" in science (seen in results; not verified further).
- Relevance to us: The direct ancestor of our "riding the wave" question. Our finding that hindsight-fitted topic
  maps manufacture waves is a methodological answer to Crane's question: whether fashion "exists" depends on whether
  topics are defined ex ante or ex post. Only cite for the question, not for any specific claim, unless the full text
  is checked.

---

## B. Tradition vs innovation: measurement and payoffs

### B1. Foster, Rzhetsky & Evans 2015 — Tradition and Innovation in Scientists' Research Strategies [CORE; CLOSEST PRIOR for the framing]
Foster, J. G., Rzhetsky, A., & Evans, J. A. (2015). Tradition and Innovation in Scientists' Research Strategies.
*American Sociological Review*, 80(5), 875–908. doi:10.1177/0003122415601618
BibTeX key: `foster2015tradition`
- What it did: Builds networks of chemical entities from abstracts of more than 6.4 million biomedical and chemistry
  publications (1934–2008) and classifies each paper's strategy (deepen known relations vs add new entities/relations;
  consolidate vs bridge clusters). The distribution of strategies is remarkably stable; high-risk innovative strategies
  are rarer, more often ignored, but more likely to bring high impact and awards (137 awards used). Concludes that
  ordinary citation rewards do not compensate scientists for the risk of innovation.
- Relevance to us: The canonical empirical operationalisation of Kuhn's essential tension, but on the
  *producer/strategy* side with *citations and prizes* as reward and on *published* papers only. We observe the *gate*
  (acceptance, including rejected and withdrawn submissions) in a fast-moving field. Their "risky strategies more often
  ignored" maps onto our far-jump penalty (replicated); their "rare innovative strategies" maps onto the newcomer
  method-paper finding. Closest prior for the framing "tradition vs innovation in research strategies and their reward".

### B2. Uzzi, Mukherjee, Stringer & Jones 2013 — Atypical Combinations and Scientific Impact [CORE]
Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). Atypical Combinations and Scientific Impact. *Science*,
342, 468–472.
BibTeX key: `uzzi2013atypical`
- What it did: 17.9 million Web of Science papers; measures conventionality/novelty from pairs of referenced journals.
  Highest-impact science is grounded mostly in highly conventional combinations with an intrusion of unusual ones;
  such papers are about twice as likely to be highly cited. Teams are 37.7% more likely than solo authors to insert
  novel combinations into familiar domains.
- Relevance to us: "Novelty anchored in convention pays" is the citation-side analogue of our acceptance pattern
  (insider + rising topic rewarded; far jumps penalised). The team result echoes our team-composition finding
  (one topic insider vs none). Issue number and DOI were not seen in results and are omitted; volume and pages
  confirmed.

### B3. Wang, Veugelers & Stephan 2017 — Bias against Novelty in Science [CORE]
Wang, J., Veugelers, R., & Stephan, P. (2017). Bias against novelty in science: A cautionary tale for users of
bibliometric indicators. *Research Policy*, 46(8), 1416–1436. doi:10.1016/j.respol.2017.06.006 (NBER WP 22180, 2016.)
BibTeX key: `wang2017bias`
- What it did: Measures novelty as first-time combinations of referenced journals (weighted by distance). Highly novel
  papers are more likely to be top-1% cited in the long run and to inspire highly cited follow-ons, but have higher
  variance, delayed recognition, and are published in journals with lower-than-expected Impact Factor. Warns that
  short-window indicators and mono-disciplinary review are biased against high-risk/high-gain research.
- Relevance to us: Their "lower-than-expected journal" result is a gatekeeping penalty for novelty, which is what our
  far-jump result looks like at a single venue. Our acceptance outcome is a short-window evaluation, so their warning
  (short-term indicators penalise novelty) is the right caveat for interpreting our penalties: lower acceptance is not
  lower long-run value.

### B4. Lee, Walsh & Wang 2015 — Creativity in Scientific Teams [SUPPORT]
Lee, Y.-N., Walsh, J. P., & Wang, J. (2015). Creativity in scientific teams: Unpacking novelty and impact. *Research
Policy*, 44(3), 684–697. doi:10.1016/j.respol.2014.10.007
BibTeX key: `lee2015creativity`
- What it did: Separates novelty from impact; team size has an inverted-U relation with novelty but a monotonically
  increasing relation with high impact; field/task variety has no direct effect on impact net of novelty.
- Relevance to us: Supports reading our steep team-size gradient in acceptance (PH2, dossier_core.md L395) as a
  "reception/impact" effect rather than evidence that large teams are more novel.

### B5. Funk & Owen-Smith 2017 — The CD index [SUPPORT]
Funk, R. J., & Owen-Smith, J. (2017). A Dynamic Network Measure of Technological Change. *Management Science*, 63(3),
791–817. doi:10.1287/mnsc.2015.2366
BibTeX key: `funk2017dynamic`
- What it did: Introduces the CD (consolidation–destabilisation) index, from −1 (consolidating) to 1 (destabilising),
  based on whether a work's descendants also cite its predecessors.
- Relevance to us: Only needed if we discuss the disruption literature (Park 2023, Wu 2019) and contrast citation-
  based measures (needs years of citations) with our ex-ante content measures available at submission.

### B6. Park, Leahey & Funk 2023 — Papers and patents are becoming less disruptive [CORE]
Park, M., Leahey, E., & Funk, R. J. (2023). Papers and patents are becoming less disruptive over time. *Nature*,
613(7942), 138–144. doi:10.1038/s41586-022-05543-x
BibTeX key: `park2023papers`
- What it did: CD index on 45 million papers and 3.9 million patents over six decades; disruptiveness declines; newer
  work is less likely to connect disparate areas. The finding was criticised; the authors' reply (Nature) maintains the
  decline is large and significant (seen via an INSEAD news page, i.e., the authors' side).
- Relevance to us: Macro backdrop for consolidation. Our FM finding (adoption of foundation models goes with fewer
  new-architecture papers) is a concrete, within-field mechanism consistent with consolidation around a dominant
  paradigm; our newcomer finding shows where the remaining method-level novelty comes from.

### B7. Wu, Wang & Evans 2019 — Large teams develop and small teams disrupt [SUPPORT]
Wu, L., Wang, D., & Evans, J. A. (2019). Large teams develop and small teams disrupt science and technology. *Nature*,
566(7744), 378–382. doi:10.1038/s41586-019-0941-9
BibTeX key: `wu2019large`
- What it did: More than 65 million papers, patents and software products (1954–2014). Small teams disrupt, search
  deeper into the past, and are recognised later if at all; large teams develop recent, popular work.
- Relevance to us: Our acceptance rises steeply with team size (PH2, dossier_core.md L395). Read with Wu et al., this
  is consistent with a gate that rewards "development" over "disruption" in the short run; small-team/disruptive work
  pays later if at all, which acceptance cannot see.

### B8. Shi & Evans 2023 — Surprising combinations and scientific outsiders [SUPPORT]
Shi, F., & Evans, J. (2023). Surprising combinations of research contents and contexts are related to impact and emerge
with scientific outsiders from distant disciplines. *Nature Communications*, 14, 1641.
doi:10.1038/s41467-023-36741-4
BibTeX key: `shi2023surprising`
- What it did: Hypergraph model of contents (MeSH/PACS keywords) and contexts over tens of millions of papers and
  patents; surprising content–context combinations predict top-10% citation impact, and such surprises tend to come
  from outsiders from distant fields.
- Relevance to us: Supports the newcomer finding (newcomer papers more often method papers, less often benchmark
  papers; replicated): outsiders bring new methods. Contrast with our far-jump penalty: outsider novelty may pay in
  citations (Shi & Evans) but is taxed at the gate (us, Hill et al. 2025).

### B9. Hofstra et al. 2020 — The diversity–innovation paradox [SUPPORT]
Hofstra, B., Kulkarni, V. V., Munoz-Najar Galvez, S., He, B., Jurafsky, D., & McFarland, D. A. (2020). The
Diversity–Innovation Paradox in Science. *PNAS*, 117(17), 9284–9291. doi:10.1073/pnas.1915378117
BibTeX key: `hofstra2020diversity`
- What it did: About 1.2 million US doctoral theses (1977–2015); novelty measured as new links between concepts.
  Underrepresented students innovate at higher rates, but their novel contributions are discounted and they are less
  likely to obtain academic positions.
- Relevance to us: Frames the newcomer pattern as an instance of a general "innovate more, rewarded less" paradox for
  those outside the established core: newcomers write more method papers yet are accepted less often (dossier_core.md
  L343). Uses NLP concept-linking, so a natural bridge for an ACL audience.

### B10. Packalen & Bhattacharya 2019 — Age and the Trying Out of New Ideas [SUPPORT]
Packalen, M., & Bhattacharya, J. (2019). Age and the Trying Out of New Ideas. *Journal of Human Capital*, 13(2),
341–373. doi:10.1086/703160 (NBER WP 20920, 2015.)
BibTeX key: `packalen2019age`
- What it did: Text-based measure of new ideas over nearly all biomedical articles since 1946; younger researchers are
  more likely to build on new ideas; a young first author with an experienced last author is the configuration most
  likely to try new ideas.
- Relevance to us: Directly parallels two of our findings: newcomers carry new methods (H2b′), and teams with one
  topic insider do better at acceptance (Teams H1, dossier_core.md L374). The "young + experienced" configuration is
  the producer-side analogue of our "newcomer team plus one insider" reward.

---

## C. Conservatism and expertise in evaluation (the gate)

### C1. Boudreau, Guinan, Lakhani & Riedl 2016 — Intellectual distance and novelty in evaluation [CORE; CLOSEST PRIOR for evaluation of novelty]
Boudreau, K. J., Guinan, E. C., Lakhani, K. R., & Riedl, C. (2016). Looking Across and Looking Beyond the Knowledge
Frontier: Intellectual Distance, Novelty, and Resource Allocation in Science. *Management Science*, 62(10), 2765–2783.
doi:10.1287/mnsc.2015.2285
BibTeX key: `boudreau2016looking`
- What it did: Randomised evaluator assignment in a grant competition at a leading research university (2,130
  evaluator–proposal pairs). Evaluators gave systematically lower scores to proposals closer to their own expertise and
  to highly novel proposals; the novelty penalty sits in the right tail (scores rise with novelty at low levels). Authors
  interpret this as boundedly rational evaluation of new ideas, not noise.
- Relevance to us: The inverted-U of novelty reception (rewarded at moderate levels, penalised at the extreme) is the
  pattern our results trace across three distinct dimensions: (i) distance from a team's own past work (far jumps
  penalised; dossier_core.md L398 reports adjusted acceptance by closeness fifth 39.7/41.8/44.4/47.2/46.9%, i.e.
  flattening at the closest end), (ii) topic age (young rising keywords modestly favoured, premium fades after the
  peak), (iii) team composition (one insider helps). Closest prior for "how evaluators receive novelty"; but grants,
  not papers, and one competition.

### C2. Li 2017 — Expertise versus Bias in Evaluation (NIH) [CORE]
Li, D. (2017). Expertise versus Bias in Evaluation: Evidence from the NIH. *American Economic Journal: Applied
Economics*, 9(2), 60–92. doi:10.1257/app.20150421
BibTeX key: `li2017expertise`
- What it did: NIH study-section data; evaluators are both biased in favour of and better informed about projects in
  their own area; the value of expertise generally dominates the cost of bias, so seeking impartial (distant) evaluators
  can lower decision quality.
- Relevance to us: The key lens for our insider finding (one topic insider vs none: higher acceptance, replicated). Is
  the insider premium a bias (in-group favouritism) or information (insiders write papers that meet the topic's
  standards)? ICLR's double-blind review weakens the reviewer-recognises-author channel, which tilts interpretation
  toward the "expertise/tacit knowledge" side; we should say so cautiously.

### C3. Teplitskiy, Acuna, Elamrani-Raoult, Körding & Evans 2018 — Networks and peer review [CORE]
Teplitskiy, M., Acuna, D., Elamrani-Raoult, A., Körding, K., & Evans, J. (2018). The sociology of scientific validity:
How professional networks shape judgement in peer review. *Research Policy*, 47(9), 1825–1841.
BibTeX key: `teplitskiy2018sociology`
- What it did: Studies how reviewers' professional-network ties ("schools of thought") to authors relate to their
  judgements; concludes that bias cannot be removed simply by recusing closely connected reviewers and recommends
  reviewers embedded in diverse networks. (Specific effect sizes not seen in results.)
- Relevance to us: Evaluator–author proximity matters for judgement; supports interpreting our topic-insider premium as
  partly "speaking the school's language". DOI not seen in results (omitted); volume/issue/pages confirmed.

### C4. Teplitskiy, Peng, Blasco & Lakhani 2022 — Is novel research worth doing? [CORE; important counterpoint]
Teplitskiy, M., Peng, H., Blasco, A., & Lakhani, K. R. (2022). Is novel research worth doing? Evidence from peer review
at 49 journals. *PNAS*, 119(47), e2118046119. doi:10.1073/pnas.2118046119
BibTeX key: `teplitskiy2022is`
- What it did: Review files for 20,538 manuscripts (Cell, Cell Reports, 2013–18) and 6,785 manuscripts (47 IOP journals,
  2018). Novelty = unusual combinations of referenced journals. More novel manuscripts were *more* likely to be accepted
  even at equal reviewer enthusiasm; reviewers did not disagree more about novel manuscripts. Suggests peer review is not
  inherently conservative, though novelty may be disfavoured at earlier, more uncertain stages.
- Relevance to us: The strongest counterpoint, and it sharpens our contribution: content novelty (reference
  combinations) is not penalised at journals, but *biographical* novelty (a team moving far from its own past work)
  is penalised at ICLR, and *temporal* novelty (an early theme) is rewarded only until the theme peaks. That is, the
  gate may not dislike new ideas; it dislikes unanchored authors and late arrivals. This reconciles Boudreau/Wang
  (penalty) with Teplitskiy 2022 (no penalty).

### C5. Lane, Teplitskiy, Gray, Ranu, Menietti, Guinan & Lakhani 2022 — Conservatism gets funded? [SUPPORT]
Lane, J. N., Teplitskiy, M., Gray, G., Ranu, H., Menietti, M., Guinan, E. C., & Lakhani, K. R. (2022). Conservatism
Gets Funded? A Field Experiment on the Role of Negative Information in Novel Project Evaluation. *Management Science*,
68(6), 4478–4495. doi:10.1287/mnsc.2021.4107
BibTeX key: `lane2022conservatism`
- What it did: Field experiments with 369 evaluators from seven universities scoring 97 projects (761 proposal–evaluation
  pairs; another summary says 760). Evaluators lower scores more after seeing more critical peer scores than they raise
  them after more favourable ones (negativity bias); information sharing makes allocation more conservative.
- Relevance to us: A mechanism for conservatism in multi-reviewer processes such as ICLR's discussion phase. Supports
  (does not test) why far jumps, which plausibly attract at least one critical reviewer, could be penalised.

### C6. Tomkins, Zhang & Heavlin 2017 — Single- vs double-blind review (WSDM) [SUPPORT]
Tomkins, A., Zhang, M., & Heavlin, W. D. (2017). Reviewer bias in single- versus double-blind peer review. *PNAS*,
114(48), 12708–12713.
BibTeX key: `tomkins2017reviewer`
- What it did: Controlled experiment at WSDM 2017 (15.6% acceptance), each paper scored by two single-blind and two
  double-blind reviewers; single-blind reviewers favoured papers by famous authors and from top institutions. A later
  paper argues the test design can inflate false alarms.
- Relevance to us: The CS-conference evidence that status bias exists when names are visible. Since ICLR is
  double-blind, it helps argue that our insider/newcomer gaps are not only name-based status effects (while arXiv
  pre-posting weakens blinding; say so). DOI not seen in results (omitted); volume/issue/pages confirmed.

---

## D. Cumulative advantage, field size, entry timing, crowding, switching

### D1. Newman 2009 — First-mover advantage in scientific publication [CORE; CLOSEST PRIOR for timing]
Newman, M. E. J. (2009). The first-mover advantage in scientific publication. *EPL (Europhysics Letters)*, 86(6), 68001.
doi:10.1209/0295-5075/86/68001 (arXiv:0809.0522.)
BibTeX key: `newman2009first`
- What it did: Within Price's preferential-attachment model, computes the expected citation advantage of the first
  papers in a new field and finds a substantial first-mover effect in several fields, often matching theory; some areas
  show none, possibly because they are not self-contained fields.
- Relevance to us: Closest prior for "timing of entry and reward". Our young-rising-keyword premium and PH6 (a keyword's
  acceptance gap is highest well before its peak, near zero at the peak, negative after; dossier_core.md L399) are a
  first-mover advantage measured at *evaluation* rather than in citations — it cannot be produced by preferential
  attachment of citations, so it is evidence that the reward for earliness is partly built into judgement. Newman's
  caveat (no effect where "fields" are not self-contained) mirrors our hindsight-map warning: whether a wave/first-mover
  effect appears depends on how topics are drawn.

### D2. Chu & Evans 2021 — Slowed canonical progress in large fields [CORE]
Chu, J. S. G., & Evans, J. A. (2021). Slowed canonical progress in large fields of science. *PNAS*, 118(41),
e2021636118. doi:10.1073/pnas.2021636118
BibTeX key: `chu2021slowed`
- What it did: 1.8 billion citations to 90 million papers (1960–2014). When fields publish many papers per year,
  citations concentrate on already well-cited work, the canon ossifies, and new papers struggle to gain attention.
- Relevance to us: Predicts that crowding should hurt newcomers and novel work in large topics. Our crowding–acceptance
  result is inconclusive; PH1 finds newcomers in mature topics do slightly worse (−2.8 pp per log unit, Holm 0.02;
  dossier_core.md L394, tier D). Frames ICLR's growth as a test of the "large field" mechanism at the gate.

### D3. Hill & Stein 2025 — Race to the bottom: competition and quality [SUPPORT]
Hill, R., & Stein, C. (2025). Race to the Bottom: Competition and Quality in Science. *Quarterly Journal of Economics*,
140(2), 1111–1185. doi:10.1093/qje/qjaf010
BibTeX key: `hill2025race`
- What it did: Protein Data Bank structures (objective quality measures). Structures with higher ex-ante potential
  attract more competition, are completed faster, and are of lower quality; scientists overestimate scooping risk
  (survey of 877 structural biologists).
- Relevance to us: Mechanism for why late, crowded waves could see a falling acceptance gap (PH6): competition for
  a hot theme lowers average quality of entries. Our crowding test is inconclusive, so cite as motivation, not support.

### D4. Hill, Yin, Stein, Wang, Wang & Jones 2025 — The pivot penalty in research [CORE; CLOSEST PRIOR for far jumps]
Hill, R., Yin, Y., Stein, C., Wang, X., Wang, D., & Jones, B. F. (2025). The pivot penalty in research. *Nature*,
642(8069), 999–1006. doi:10.1038/s41586-025-09048-1
BibTeX key: `hill2025pivot`
- What it did: About 26 million papers and 1.72 million patents. Scientists who move further from their prior work
  get lower impact; the penalty is nearly universal and has grown over five decades; larger pivots show weak engagement
  with established mixtures of prior knowledge and lower publication success rates; also found for COVID-19 pivots.
  Proposed mechanisms: lacking reputation in the new field and lower quality while getting up to speed.
- Relevance to us: Closest prior for our far-jump finding (replicated on held-out papers). Our contribution relative
  to Hill et al.: (i) we observe the decision itself on all submissions, including rejected and withdrawn, under
  double-blind review; (ii) we pair the pivot penalty with its remedy — one topic insider on the team; (iii) we place
  it inside a field-wide story of waves. Given names: "Wang, X." first name not seen in results; surnames and
  order confirmed.

### D5. Azoulay, Fons-Rosen & Graff Zivin 2019 — Does science advance one funeral at a time? [SUPPORT]
Azoulay, P., Fons-Rosen, C., & Graff Zivin, J. S. (2019). Does Science Advance One Funeral at a Time? *American Economic
Review*, 109(8), 2889–2920. doi:10.1257/aer.20161574
BibTeX key: `azoulay2019does`
- What it did: 452 eminent life scientists who died prematurely (1975–2003). After a star's death, collaborators publish
  less in the field while non-collaborators publish markedly more; the newcomers draw on different literature and are
  disproportionately likely to be highly cited.
- Relevance to us: Incumbents can hold back outsiders; outsiders bring different ideas. Supports reading the newcomer
  method-paper finding as outsiders bringing different intellectual content, and the insider premium as incumbency
  advantage at the gate.

### D6. Azoulay, Graff Zivin & Manso 2011 — Incentives and creativity (HHMI) [SUPPORT]
Azoulay, P., Graff Zivin, J. S., & Manso, G. (2011). Incentives and creativity: evidence from the academic life
sciences. *RAND Journal of Economics*, 42(3), 527–554.
BibTeX key: `azoulay2011incentives`
- What it did: HHMI investigators (long horizons, tolerance of early failure) produce high-impact papers at a much higher
  rate than similar NIH-funded scientists and change research direction toward novel lines.
- Relevance to us: Context for why short-cycle conference acceptance (a fast, failure-intolerant reward) may tilt
  authors toward near moves and anchored teams. Optional.

### D7. Myers 2020 — The Elasticity of Science [SUPPORT]
Myers, K. (2020). The Elasticity of Science. *American Economic Journal: Applied Economics*, 12(4), 103–134.
doi:10.1257/app.20180518
BibTeX key: `myers2020elasticity`
- What it did: NIH Requests for Applications plus text similarity between scientists' past work and the requested
  science; scientists respond much more when the call is close to their ongoing work; switching costs are large.
- Relevance to us: Producer-side cost of far moves; together with our acceptance-side far-jump penalty it implies a
  double tax on switching topics.

### D8. Zeng et al. 2019 — Increasing trend of scientists to switch between topics [SUPPORT]
Zeng, A., Shen, Z., Zhou, J., Fan, Y., Di, Z., Wang, Y., Stanley, H. E., & Havlin, S. (2019). Increasing trend of
scientists to switch between topics. *Nature Communications*, 10, 3439. doi:10.1038/s41467-019-11401-8
BibTeX key: `zeng2019increasing`
- What it did: Builds each scientist's paper network via shared references; communities = topics; researchers now switch
  topics more often than earlier; the preprint reports switching negatively correlated with citations per paper at all
  career stages (not checked in the published version).
- Relevance to us: Shows topic switching is common and rising, which makes our far-jump penalty consequential.

### D9. Zeng, Fan, Di, Wang & Havlin 2021 — Fresh teams [SUPPORT]
Zeng, A., Fan, Y., Di, Z., Wang, Y., & Havlin, S. (2021). Fresh teams are associated with original and
multidisciplinary research. *Nature Human Behaviour*, 5(10), 1314–1324. doi:10.1038/s41562-021-01084-x
BibTeX key: `zeng2021fresh`
- What it did: Teams with fewer prior collaborations among members produce more original and multidisciplinary work,
  more so in larger teams; fully fresh teams publish fewer papers. Data include computer-science papers.
- Relevance to us: Fresh/new teams generate originality (our newcomer method finding) yet our gate rewards having one
  topic insider; together suggest an optimal mix rather than pure freshness.

### D10. Guimerà, Uzzi, Spiro & Amaral 2005 — Team assembly mechanisms [SUPPORT]
Guimerà, R., Uzzi, B., Spiro, J., & Amaral, L. A. N. (2005). Team assembly mechanisms determine collaboration network
structure and team performance. *Science*, 308(5722), 697–702. doi:10.1126/science.1106340
BibTeX key: `guimera2005team`
- What it did: Model of team formation driven by team size, share of newcomers and incumbents' tendency to repeat
  collaborations; team performance in artistic and scientific fields depends on the newcomer/incumbent mix.
- Relevance to us: Classic prior for "incumbents plus newcomers" composition; our one-insider premium is a
  conference-acceptance version of this mixing result.

### D11. Jones 2009 — The Burden of Knowledge [SUPPORT]
Jones, B. F. (2009). The Burden of Knowledge and the "Death of the Renaissance Man": Is Innovation Getting Harder?
*Review of Economic Studies*, 76(1), 283–317. doi:10.1111/j.1467-937X.2008.00531.x
BibTeX key: `jones2009burden`
- What it did: As knowledge accumulates, innovators need more training, specialise more and work in larger teams.
- Relevance to us: Explains why topic-specific knowledge (an insider) helps at the gate and why team size gradients
  appear; frames "knowing the topic's conventions" as a cost newcomers must pay.

### D12. Sun, Kaur, Milojević, Flammini & Menczer 2013 — Social dynamics of science [SUPPORT]
Sun, X., Kaur, J., Milojević, S., Flammini, A., & Menczer, F. (2013). Social Dynamics of Science. *Scientific Reports*,
3, 1069. doi:10.1038/srep01069
BibTeX key: `sun2013social`
- What it did: Agent-based model in which disciplines emerge from splitting and merging of collaboration communities;
  reproduces stylised facts about disciplines, authors and publications.
- Relevance to us: Fields/topics are emergent social objects, not fixed categories; supports our methodological point
  that topic boundaries drawn with hindsight can create apparent waves.

### D13. Fortunato et al. 2018 — Science of science [CORE, one-line]
Fortunato, S., Bergstrom, C. T., Börner, K., Evans, J. A., Helbing, D., Milojević, S., Petersen, A. M., Radicchi, F.,
Sinatra, R., Uzzi, B., Vespignani, A., Waltman, L., Wang, D., & Barabási, A.-L. (2018). Science of science. *Science*,
359(6379), eaao0185. doi:10.1126/science.aao0185
BibTeX key: `fortunato2018science`
- What it did: Review of the transdisciplinary field using large-scale data on science production to find universal and
  domain-specific patterns. (Results confirmed 14 authors, first Fortunato, last Barabási, with D. Wang; the middle names
  are from my knowledge of the record and should be checked against the PMC copy PMC5949209.)
- Relevance to us: Positions the paper in science of science; cite once in the introduction.

---

## E. Unverified or partially verified candidates (do NOT cite as verified)

- **Heo et al. 2026 (EMNLP), "What Drives Paper Acceptance? A Process-Centric Analysis of Modern Peer Review."**
  ACL Anthology entry 2026.emnlp-main.1123, pages 25711–25731, listed as Heo et al.; arXiv 2509.25701 lists authors as
  Sangkeun Jung, Goun Pyeon, Inbum Heo, Hyungjin Ahn. ICLR 2017–2025, more than 28,000 submissions; rebuttal
  interaction, clearer writing, earlier submission correlate with acceptance. **Author order unresolved** between the
  two records. Very relevant as an ICLR acceptance study (process factors, not topic/novelty/team history) — likely
  belongs to the ML-peer-review literature notes; verify author list on the Anthology page before citing.
- **Crane 1969** end page (441 vs 444) not confirmed; see A6.
- **Barber 1969**, "The functions and dysfunctions of 'fashion' in science: a case for the study of social change",
  Mens en Maatschappij (seen in results; year/volume/pages not confirmed).
- **Merton 1988**, "The Matthew Effect in Science, II", *Isis* 79, 606–623 (seen only inside one search result as
  context; not independently verified).
- **Boyack & Klavans 2014** replication of Uzzi et al. (mentioned in a result; not searched).
- Not searched for lack of time but potentially relevant: Leahey, Beckman & Stanko 2017 (ASQ, interdisciplinarity
  prominent but less productive); Bloom, Jones, Van Reenen & Webb 2020 (AER, ideas getting harder to find);
  Rzhetsky, Foster, Foster & Evans 2015 (PNAS, choosing experiments); Dasgupta & David 1994 (Research Policy, new
  economics of science); Ke et al. 2015 (PNAS, sleeping beauties). Treat all as unverified.

---

## (a) What this literature already knows

1. **The essential tension is real and stable.** Scientists overwhelmingly choose tradition-deepening strategies;
   innovative strategies are rarer, riskier, and more variable in payoff (Kuhn 1977; Foster et al. 2015; Wang et al.
   2017).
2. **The best-rewarded novelty is anchored.** High-impact work combines mostly conventional knowledge with a small
   atypical intrusion (Uzzi et al. 2013); evaluators penalise only the extreme right tail of novelty (Boudreau et al.
   2016).
3. **Whether gatekeepers penalise novelty is contested.** Grant evaluators (Boudreau 2016) and journal Impact Factor
   placement (Wang 2017) suggest a penalty; journal review files at 49 journals show none (Teplitskiy et al. 2022);
   negativity bias in group evaluation can make allocation conservative (Lane et al. 2022).
4. **Proximity cuts both ways.** Evaluators near a proposal are both better informed and more biased; expertise usually
   dominates (Li 2017); network proximity shapes judgement (Teplitskiy et al. 2018); name visibility advantages famous
   authors in CS review (Tomkins et al. 2017).
5. **Moving away costs.** Scientists who pivot further from their past work get less impact and publication success
   (Hill et al. 2025); switching costs are large (Myers 2020) even though switching is rising (Zeng et al. 2019).
6. **Outsiders and fresh teams bring novelty but are under-rewarded.** Outsiders produce surprising combinations (Shi
   & Evans 2023), enter after incumbents leave (Azoulay et al. 2019), young authors try new ideas (Packalen &
   Bhattacharya 2019), and minorities innovate more but are discounted (Hofstra et al. 2020); fresh teams are more
   original (Zeng et al. 2021); newcomer–incumbent mix shapes team performance (Guimerà et al. 2005).
7. **Timing and size matter for reward.** Early papers in a field gain lasting citation advantage (Newman 2009, via
   Price 1976 cumulative advantage; Merton 1957 priority); large fields entrench the canon (Chu & Evans 2021);
   competition lowers quality (Hill & Stein 2025); science is consolidating (Park et al. 2023; Wu et al. 2019 on team
   size).

## (b) What it does not know that our data can speak to

1. **The gate with its failures visible.** Nearly all of the above observes published papers and later citations (a
   survivor sample) or funding decisions. We observe every submission to one selective venue, including rejected and
   withdrawn papers, with the decision itself as the reward, under double-blind review. That separates "the evaluator
   rewards X" from "the citation market rewards X".
2. **Three kinds of novelty side by side.** Prior work measures one novelty (content combinations, pivot distance, or
   topic age) at a time. We can contrast *content type* (method vs benchmark), *biographical distance* (far jump from a
   team's own record), and *temporal position* (young/rising vs post-peak keyword) in one population, and show that
   they are received differently — a way to reconcile Boudreau/Wang (penalty) with Teplitskiy 2022 (no penalty).
3. **The life cycle of an earliness premium at evaluation.** Newman's first-mover advantage is a citation-network
   effect; whether *reviewers* reward earliness, and whether that reward decays after a theme peaks, is unstudied (PH6;
   weak but declared and tested on held-out papers).
4. **A remedy for the pivot penalty.** Hill et al. document the penalty; we show that one topic insider on the team goes
   with higher acceptance (replicated), i.e., anchoring a jump in the receiving topic's tradition.
5. **Who carries novelty into a fast field.** In a field undergoing a paradigm shift (foundation models), we show
   newcomers contribute more method papers and fewer benchmark papers (reversing a registered herding prediction,
   replicated), while paradigm adoption goes with fewer new-architecture papers — a within-field mechanism for the
   consolidation that Park et al. measure in aggregate.
6. **Measurement artefacts in "waves" and "fashions".** The fashion question (Crane 1969) and emergence studies assume
   topics are well defined. We show hindsight-fitted topic maps manufacture emerging topics, echoing Newman's caveat that
   effects vanish where "fields" are not self-contained. Science-of-science work rarely tests the dependence of its
   trend claims on when the taxonomy was fitted.
7. **Registered and held-out evidence.** Few science-of-science studies pre-register and replicate on held-out data; our
   design allows us to label which tension-related results survive.

## (c) Candidate framings our findings could contribute to

1. **"The essential tension at the gate" (recommended main line).** A selective ML venue rewards novelty that is
   anchored in tradition and penalises novelty that is not. Anchoring comes in three forms: biographical (close to the
   team's own record), social (one topic insider on the team), and temporal (joining a rising theme before it peaks).
   Newcomers supply method novelty (opposite to herding) but face the gate's anchoring requirement; paradigm adoption
   (foundation models) shifts work from architecture-building to within-paradigm work. Waves as seen in hindsight
   partly are artefacts, so the real rewards are local (who, how far, how early), not "being on the wave". Positions us
   between Foster et al. 2015 (producer side), Boudreau 2016/Teplitskiy 2022 (evaluator side), Hill et al. 2025 (pivot
   penalty) and Newman 2009 (timing).
2. **"Riding a wave is not the same as catching it early."** Timing framing: earliness is rewarded and decays after a
   peak (PH6, weak), crowding is inconclusive, branded titles give no premium, and waves themselves partly come from
   hindsight. Ties to Merton 1957 priority, Newman 2009, Crane 1969, Hill & Stein 2025. Weaker because PH6 is weak.
3. **"Outsiders innovate, insiders get in."** Newcomer/insider framing: newcomers bring methods but are accepted less;
   far jumps are penalised; one insider helps. Ties to Hofstra 2020 (paradox), Azoulay 2019, Packalen & Bhattacharya
   2019, Guimerà 2005, Li 2017. Strong on replicated results, but risks reading as narrow-team-composition paper.
4. **"Novelty penalty or anchoring premium?"** Reconciliation framing for the contested peer-review conservatism
   debate: content novelty is not penalised (newcomer method papers are not the problem per se), distance is. Useful as
   a Discussion paragraph inside framing 1.
5. **Methodological framing: "Waves you see depend on when you draw the map."** Useful as the paper's
   measurement-validity contribution (hindsight maps), echoing Newman's self-contained-field caveat and Sun et al. on
   emergent fields; best used as a supporting section rather than the headline.

Caveats to carry into the paper: acceptance is a short-window reward (Wang et al. 2017; Wu et al. 2019), so lower
acceptance is not lower long-run value; double-blind ICLR review is partly unblinded by arXiv; our newcomer definition is
ICLR-only; PH6 is weak (declared held-out test only just supported) and federated learning, the starkest discovery case,
was not confirmed on held-out papers.
