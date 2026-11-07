# Literature notes: fashions, bandwagons, hype and research waves

Area brief: theories of fads, fashions, bandwagons and hype in science and organisations, and ML-specific critiques of trend-following.

Verification standard: a work is listed as VERIFIED only if authors, title, year and venue (and volume/issue/pages where applicable) were seen in at least one reliable search result (publisher page, JSTOR/IDEAS-RePEc, PMC, Semantic Scholar, university repository, ACM/NeurIPS proceedings page, library catalogue). Where a detail could not be confirmed it is flagged inline ("not confirmed"). Content summaries are based on abstracts or secondary descriptions seen in search results; where only secondary descriptions were seen, this is said. WebFetch could not reach dblp.org or pdodds.w3.uvm.edu (DNS blocked in this session), so no full texts were read.

BibTeX key convention: firstauthorlastname + year + first title word, lower case, skipping a leading article or preposition ("The", "A", "On", "In").

Our findings are quoted only qualitatively, except where a number was read from `/home/user/cloud-research/research/fashion/RESULTS.md` (line given).

---

## 1. Management fashion and fads (organisation theory)

### 1.1 Abrahamson 1991 — VERIFIED
Abrahamson, Eric. 1991. Managerial fads and fashions: The diffusion and rejection of innovations. *Academy of Management Review* 16(3): 586–612.
Key: `abrahamson1991managerial`

What it did: Theory paper. Argues that the dominant diffusion-of-innovations literature carries a "pro-innovation bias" (it assumes what diffuses benefits adopters), which leaves it unable to explain when technically inefficient innovations diffuse and when efficient ones are rejected. Builds alternative perspectives (including fad and fashion perspectives, in which imitation and fashion-setting organisations drive adoption) and argues that efficient-choice and fad/fashion processes can coexist.

Relevance to us: The canonical source for the idea that popularity waves need not track merit. Frames our whole design: we ask whether ICLR's popularity waves (topics, keywords, foundation models) look like efficient choice or like fashion, using the gatekeeper's verdict (acceptance) as the merit-side signal. Our "young rising keywords modestly favoured, gap falls after the peak" pattern is a reviewer-side analogue of fad dynamics; our null for branded titles argues against a pure symbolic-fashion premium. Framing work, not closest prior.

### 1.2 Abrahamson 1996 — VERIFIED
Abrahamson, Eric. 1996. Management fashion. *Academy of Management Review* 21(1): 254–285.
Key: `abrahamson1996management`

What it did: Defines management fashion as "a relatively transitory collective belief, disseminated by management fashion setters, that a management technique leads rational management progress" (p. 257, as quoted in a secondary source). Fashion is a supply-and-demand market between fashion setters (consultants, gurus, business schools, press) and fashion followers; it must appear both rational and progressive. Argues management fashion is not just a case of aesthetic fashion.

Relevance to us: Gives the vocabulary of "fashion setters" vs "followers" and the norm that fashions must look like *progress*. In ML the conference itself (reviewers, area chairs) is partly a fashion setter. Our finding that newcomers write more *method* papers and fewer *benchmark* papers (opposite to the registered herding prediction) fits the "norm of progress": entrants enter by claiming progress, not by cheap following. Framing.

### 1.3 Abrahamson and Fairchild 1999 — VERIFIED
Abrahamson, Eric, and Gregory Fairchild. 1999. Management fashion: Lifecycles, triggers, and collective learning processes. *Administrative Science Quarterly* 44(4): 708–740. DOI 10.2307/2667053.
Key: `abrahamson1999management`

What it did: Theory-building case study of the quality-circles fashion using counts of print discourse over time. Finds that variation in when knowledge entrepreneurs begin, continue and stop promoting a fashion explains variation in lifecycles; upswings show enthusiastic discourse, downswings more measured discourse, read as "superstitious" collective learning. Draws on collective-behaviour theory (social strain, weakened institutional constraints, bandwagon imitation).

Relevance to us: Closest organisational analogue to our keyword-wave analysis (PH6): a fashion is measured as a rise-and-fall in discourse share, and the evaluation climate differs between upswing and downswing. Our PH6 result (a keyword's acceptance gap is lower after its share peaks than up to the peak; declared held-out test supported at one-sided p 0.043, RESULTS.md line 977, "weak", line 983) is a gatekeeper-side version of their upswing/downswing asymmetry. Strong framing; near-closest prior outside ML.

### 1.4 Strang and Macy 2001 — VERIFIED
Strang, David, and Michael W. Macy. 2001. In search of excellence: Fads, success stories, and adaptive emulation. *American Journal of Sociology* 107(1): 147–182. DOI 10.1086/323039.
Key: `strang2001search`

What it did: Combines organisational cognition and institutional mimicry into a model of "adaptive emulation": firms that perceive failure imitate their most successful peers, with beliefs about strategy efficacy inferred from others' performance. Simulations show this can produce faddish adoption-abandonment cycles, including of maladaptive strategies; secondary summaries say faddish cycles are most robust when innovations have only modest positive effects. Argues this matters in a business world shaped by media success stories. (Content from abstract-level and secondary descriptions; full text not read.)

Relevance to us: Supplies a mechanism that predicts exactly our timing pattern without assuming the topic is worthless: early adopters of a modestly useful idea do well, success stories attract imitators, and later adopters do not reap the same gains. Fits "young rising keywords modestly favoured" and the post-peak decline (PH6). Also warns that single success/failure stories (our federated-learning case, starkest in discovery but not confirmed held-out, RESULTS.md lines 51–52, 988) are the raw material of fads, so a field narrative built on one case is itself fad-prone. Key framing.

### 1.5 Strang and Still 2004 — VERIFIED
Strang, David, and Mary C. Still. 2004. In search of the élite: Revising a model of adaptive emulation with evidence from benchmarking teams. *Industrial and Corporate Change* 13(2): 309–333. DOI 10.1093/icc/dth013.
Key: `strang2004search`

What it did: Revises the Strang–Macy model using evidence from corporate benchmarking teams; managers describe innovation as problem-driven and performance-focused, but also attend closely to prestigious firms.

Relevance to us: Imitation follows prestige as well as performance. Relevant to our team findings (one topic insider in the team goes with higher acceptance, replicated): who carries an idea matters alongside what it is. Minor framing.

## 2. Herding and informational cascades (economics)

### 2.1 Bikhchandani, Hirshleifer and Welch 1992 — VERIFIED
Bikhchandani, Sushil, David Hirshleifer, and Ivo Welch. 1992. A theory of fads, fashion, custom, and cultural change as informational cascades. *Journal of Political Economy* 100(5): 992–1026.
Key: `bikhchandani1992theory`

What it did: Sequential model in which agents with private signals observe predecessors' actions; once the public history outweighs a private signal, agents ignore their own information and an informational cascade starts. Cascades can start from a few early movers, explain conformity, and are fragile ("precarious"), so small shocks produce rapid, short-lived fluctuations (fads, booms, crashes).

Relevance to us: Canonical theory behind our registered herding prediction (newcomers would pile into hot topics with cheap follow-on work such as benchmarks). Our replicated finding goes the other way (newcomers write more method papers, fewer benchmark papers), so the cascade picture of the *entrant* is not supported in ICLR. The model's fragility prediction (fast reversals) is consistent with the post-peak fall in the acceptance gap (PH6), but our data cannot separate cascade fragility from simple saturation. Framing; contradicted in one respect.

### 2.2 Banerjee 1992 — VERIFIED
Banerjee, Abhijit V. 1992. A simple model of herd behavior. *Quarterly Journal of Economics* 107(3): 797–817.
Key: `banerjee1992simple`

What it did: Sequential decision model in which each decision maker sees earlier choices; rational agents herd and the resulting equilibrium is inefficient (information is lost).

Relevance to us: Twin canonical herding model; cite with Bikhchandani et al. for "herding is individually rational but collectively inefficient". Our data measure topic entry and acceptance, not information loss, so we can only speak to the observable side (who enters, what they write, how they fare). Framing.

### 2.3 Weisberg 2013 — VERIFIED
Weisberg, Michael. 2013. Modeling herding behavior and its risks. *Journal of Economic Methodology* 20(1): 6–18. DOI 10.1080/1350178X.2013.774843.
Key: `weisberg2013modeling`

What it did: Models scientific communities that herd because members avoid research risk; studies epistemic consequences and the surprising robustness of herding; finds incentives for risky research have a small but significant effect on community progress.

Relevance to us: The closest "economics/philosophy of herding among researchers" source found. Its premise (researchers herd to avoid risk) predicts that far jumps are penalised and staying close is rewarded, which matches our replicated finding that far jumps from a team's own past work go with lower acceptance. Our data add that the penalty is visible at the gatekeeper, i.e. the incentive to herd is real in ML peer review. Framing; supports.

### 2.4 Baddeley 2013 — VERIFIED (bibliographic details from a search summary listing JEM 20(1):35–44; abstract not read)
Baddeley, Michelle. 2013. Herding, social influence and expert opinion. *Journal of Economic Methodology* 20(1): 35–44.
Key: `baddeley2013herding`

What it did (as described in search results): Links herding among experts to reputation building and conformity, and discusses the relative rewards of consensus versus contrarianism.

Relevance to us: Supports reading the insider and far-jump findings as reputational conformity incentives. Minor framing; verify abstract before citing substantively.

### 2.5 Akerlof and Michaillat 2018 — VERIFIED
Akerlof, George A., and Pascal Michaillat. 2018. Persistence of false paradigms in low-power sciences. *Proceedings of the National Academy of Sciences* 115(52): 13228–13233. DOI 10.1073/pnas.1816454115.
Key: `akerlof2018persistence`

What it did: Model of tenure/promotion with homophily: evaluators favour candidates who share their paradigm. When evaluation "power" is low, a false paradigm can prevail if few scientists start with the better one; case studies from astronomy, medicine, economics.

Relevance to us: Gives a gatekeeper-centred mechanism: evaluators reward their own paradigm. Our replicated "one topic insider in the team goes with higher acceptance" and "far jumps go with lower acceptance" are the kind of in-group evaluation pattern this model assumes. Framing for the reward side of the story.

### 2.6 Park, Peacey and Munafò 2014 — VERIFIED (content on herding not seen)
Park, In-Uck, Mike W. Peacey, and Marcus R. Munafò. 2014. Modelling the effects of subjective and objective decision making in scientific peer review. *Nature* 506: 93–96. DOI 10.1038/nature12786.
Key: `park2014modelling`

What it did: Models how different reviewer decision rules affect publication and the aggregation of knowledge, asking whether peer review is intrinsically prone to failure. Search summaries elsewhere describe it as showing that herding exposes a community to converging on wrong answers and that some reviewer subjectivity can curb it, but that description was not confirmed from the paper itself.

Relevance to us: Puts peer review itself inside the herding loop: reviewers' rules shape what the field converges on. Supports framing acceptance as the field's selection mechanism for waves. Cite cautiously.

## 3. Bandwagons and the life cycle of scientific specialties (sociology of science)

### 3.1 Fujimura 1988 — VERIFIED (bibliographic; content from secondary descriptions)
Fujimura, Joan H. 1988. The molecular biological bandwagon in cancer research: Where social worlds meet. *Social Problems* 35(3): 261–283.
Key: `fujimura1988molecular`

What it did: Ethnographic/historical study of how proto-oncogene research became a bandwagon in cancer research. Per secondary descriptions of this work and its dissertation/book versions, a "standardized package" of theory plus methods (recombinant DNA, sequencers, probes) made problems "do-able" for many labs, and the transportability of that package drove the rush of laboratories, funders and other social worlds into the area.

Relevance to us: The best theory for our foundation-model finding. Foundation models are a standardized, transportable package (pretrained weights plus fine-tuning recipe) that makes many problems do-able; our replicated result that foundation-model adoption in a topic goes with fewer new-architecture papers (H1d, −11.0 pp held-out, RESULTS.md line 745) is what a package bandwagon predicts: the package displaces the craft of building new architectures. Also predicts that newcomers would ride the package with cheap work; our newcomer result (more method, fewer benchmark papers) contradicts that part. Key framing.

### 3.2 Price 1963 — VERIFIED
Price, Derek J. de Solla. 1963. *Little Science, Big Science*. New York: Columbia University Press.
Key: `price1963little`

What it did: Based on 1962 Pegram Lectures; measures exponential growth of science (scientists, journals, papers) over three centuries and argues growth must turn logistic (saturate).

Relevance to us: Origin of the logistic/saturation view of research areas; underlies the "maturity" and "crowding" variables. Our crowding-and-acceptance result is inconclusive, so we cannot say saturation lowers per-paper reward. Background framing.

### 3.3 Crane 1972 — VERIFIED
Crane, Diana. 1972. *Invisible Colleges: Diffusion of Knowledge in Scientific Communities*. Chicago: University of Chicago Press.
Key: `crane1972invisible`

What it did: Accepts Price's logistic model of growth and argues that research areas grow through social networks ("invisible colleges"); areas have life cycles, growing and fading with the state of the central research problem.

Relevance to us: Canonical "life cycle of a research area" account, with growth driven by entry of new people through networks. Our newcomer/insider variables operationalise who enters a topic and who carries it; the replicated insider premium fits Crane's view that networks carry areas. Framing.

### 3.4 Mullins 1972 — VERIFIED (bibliographic)
Mullins, Nicholas C. 1972. The development of a scientific specialty: The phage group and the origins of molecular biology. *Minerva* 10(1): 51–82. DOI 10.1007/BF01881390.
Key: `mullins1972development`

What it did: Historical-network study of how the phage group developed into a specialty (molecular biology) through stages of increasingly dense communication and organisation. (Stage details not confirmed from the text in this session.)

Relevance to us: Classic specialty-development model; supports treating topics as social as well as cognitive units (insiders vs newcomers). Background.

### 3.5 Mullins 1973 — VERIFIED (bibliographic; stage model content not confirmed)
Mullins, Nicholas C. (with Carolyn J. Mullins). 1973. *Theories and Theory Groups in Contemporary American Sociology*. New York: Harper & Row.
Key: `mullins1973theories`

What it did: Classifies sociology's theory groups and traces their development; tied to the Griffith–Mullins theory of scientific group formation. The commonly cited normal → network → cluster → specialty stage sequence was not confirmed from a source seen here.

Relevance to us: Optional background for a stage model of topics. Cite only if needed.

### 3.6 Foster, Rzhetsky and Evans 2015 — VERIFIED (end page not confirmed)
Foster, Jacob G., Andrey Rzhetsky, and James A. Evans. 2015. Tradition and innovation in scientists' research strategies. *American Sociological Review* 80(5): 875–908 (start page confirmed; end page from common citation). DOI 10.1177/0003122415601618.
Key: `foster2015tradition`

What it did: Using millions of MEDLINE abstracts represented as chemical-relation networks, classifies research strategies as tradition (deepening known relations) vs innovation (new chemicals/relations). The distribution of strategies is stable and conservative; innovative work is more often ignored but more likely to earn high impact and prizes.

Relevance to us: Closest empirical prior for our "far jumps" finding: risky distance from known work has a lower expected payoff but higher variance. Our replicated result that far jumps from a team's own past work go with lower acceptance is the conference-gatekeeper version of the "innovative work is more likely to be ignored" half. Note these are associations in both studies. Closest prior for the far-jump finding (shared with the novelty/reward literature).

### 3.7 Rzhetsky, Foster, Foster and Evans 2015 — VERIFIED
Rzhetsky, Andrey, Jacob G. Foster, Ian T. Foster, and James A. Evans. 2015. Choosing experiments to accelerate collective discovery. *Proceedings of the National Academy of Sciences* 112(47): 14569–14574. DOI 10.1073/pnas.1509757112.
Key: `rzhetsky2015choosing`

What it did: Models knowledge as a network uncovered by experiments; finds that experiment-choice habits that help careers slow collective discovery, especially in mature fields; more risk-taking and publishing failures would speed discovery.

Relevance to us: Individual-collective tension: the conservative choices our acceptance data reward (insider teams, near moves) are individually rational and collectively costly. Framing for the discussion.

### 3.8 Chu and Evans 2021 — VERIFIED
Chu, Johan S. G., and James A. Evans. 2021. Slowed canonical progress in large fields of science. *Proceedings of the National Academy of Sciences* 118(41): e2021636118. DOI 10.1073/pnas.2021636118.
Key: `chu2021slowed`

What it did: 1.8 billion citations to 90 million papers (1960–2014): in large fields, the most-cited papers keep their lead, new papers struggle to become canonical, and a flood of papers hinders new ideas.

Relevance to us: Field size as a brake on novelty. Our crowding-and-acceptance tests are inconclusive, so we neither confirm nor refute a size penalty at the paper level; but the foundation-model/new-architecture result fits a field converging on a canon. Framing.

## 4. Diffusion and hype cycles

### 4.1 Rogers 2003 — VERIFIED
Rogers, Everett M. 2003. *Diffusion of Innovations*. 5th ed. New York: Free Press.
Key: `rogers2003diffusion`

What it did: Standard synthesis of diffusion research: adoption over time follows an S-curve; adopters fall into innovators, early adopters, early majority, late majority and laggards (chapter 7, "Innovativeness and adopter categories").

Relevance to us: Gives the adopter-category language for timing. Our "young rising keywords modestly favoured" and the pre-peak vs post-peak acceptance gap (PH6) are, in Rogers' terms, a reward to early adopters over the late majority. Also the target of Abrahamson's pro-innovation-bias critique. Framing.

### 4.2 Linden and Fenn 2003 — VERIFIED (Gartner report; seen via citation records, not the report)
Linden, Alexander, and Jackie Fenn. 2003. Understanding Gartner's hype cycles. Gartner Research report, 30 May 2003.
Key: `linden2003understanding`

What it did: Practitioner description of the hype cycle (technology trigger, peak of inflated expectations, trough of disillusionment, slope of enlightenment, plateau of productivity) as a tool for technology planners. Descriptive, not a test.

Relevance to us: The popular template behind "ML hype waves". Cite as the template we do *not* assume; our waves are defined by observed submission share, not by a stage template. Framing.

### 4.3 Fenn and Raskino 2008 — VERIFIED
Fenn, Jackie, and Mark Raskino. 2008. *Mastering the Hype Cycle: How to Choose the Right Innovation at the Right Time*. Boston: Harvard Business Press.
Key: `fenn2008mastering`

What it did: Book-length practitioner account of the hype cycle (originated by Fenn at Gartner in 1995) and of strategies for adopting innovations at the right point.

Relevance to us: Popular claim that adoption timing matters; our PH6/kwtiming results are an empirical, gatekeeper-side check of a timing advantage in research. Framing.

### 4.4 Dedehayir and Steinert 2016 — VERIFIED
Dedehayir, Ozgur, and Martin Steinert. 2016. The hype cycle model: A review and future directions. *Technological Forecasting and Social Change* 108: 28–41. DOI 10.1016/j.techfore.2016.04.005.

Key: `dedehayir2016hype`

What it did: Critical review of the hype cycle using evidence from empirical studies; finds incongruences with Gartner's reports and calls for research on hype dynamics generally rather than the single-curve model.

Relevance to us: Academic critique that hype-cycle shapes are not reliably found when tested. Supports our methodological point that waves drawn from hindsight-fitted topic maps can be manufactured by the map (our hindsight checks; several registered tests fail the hindsight requirement, e.g. RESULTS.md lines 79, 82). Framing; supports.

### 4.5 van Lente, Spitters and Peine 2013 — VERIFIED
van Lente, Harro, Charlotte Spitters, and Alexander Peine. 2013. Comparing technological hype cycles: Towards a theory. *Technological Forecasting and Social Change* 80(8): 1615–1628. DOI 10.1016/j.techfore.2012.12.004.
Key: `vanlente2013comparing`

What it did: Compares hypes in VoIP, gene therapy and high-temperature superconductivity; finds hype patterns vary considerably and are shaped by interacting expectations at different levels; no single hype-cycle shape.

Relevance to us: Supports reporting waves keyword by keyword and expecting heterogeneity (17 of 68 keywords rose and fell, RESULTS.md line 968; vision transformer has the largest drop in both splits, line 987; federated learning does not decline held-out, line 988). Framing; supports.

### 4.6 Borup, Brown, Konrad and van Lente 2006 — VERIFIED
Borup, Mads, Nik Brown, Kornelia Konrad, and Harro van Lente. 2006. The sociology of expectations in science and technology. *Technology Analysis & Strategic Management* 18(3–4): 285–298.
Key: `borup2006sociology`

What it did: Programmatic review founding the "sociology of expectations": expectations and visions are performative; they mobilise resources and coordinate actors before technologies exist.

Relevance to us: Frames branded titles and foundation-model talk as expectation work. Our null for branded titles (no acceptance premium) suggests expectation language does not buy acceptance at ICLR. Framing.

## 5. ML-specific critiques of trend-following

### 5.1 Hooker 2021 — VERIFIED (page range not confirmed)
Hooker, Sara. 2021. The hardware lottery. *Communications of the ACM* 64(12) (December 2021), Research and Advances. Preprint arXiv:2009.06489 (2020).
Key: `hooker2021hardware`

What it did: Essay coining "hardware lottery": a research idea wins because it suits available hardware and software, not because it is better; historical examples from computing; argues specialised hardware makes straying from the mainstream costlier.

Relevance to us: Path-dependence explanation for why the field converges on one package. Our foundation-model result (adoption goes with fewer new-architecture papers) is consistent with the lottery's prediction that alternatives get crowded out once a winner fits the infrastructure. Framing.

### 5.2 Sutton 2019 — VERIFIED (essay)
Sutton, Richard S. 2019. The bitter lesson. Essay, 13 March 2019. http://www.incompleteideas.net/IncIdeas/BitterLesson.html
Key: `sutton2019bitter`

What it did: Argues that over seventy years general methods that leverage computation (search and learning) beat methods built on human knowledge.

Relevance to us: The normative counterpoint to "fashion": convergence on scaled general models may be *efficient* choice, not fad. Our design cannot rule this out; the FM/new-architecture association is compatible with both readings. Frame the FM result as the test case where fashion and efficient choice are hardest to separate.

### 5.3 Lipton and Steinhardt 2019 — VERIFIED
Lipton, Zachary C., and Jacob Steinhardt. 2019. Troubling trends in machine learning scholarship. *Queue* 17(1): 45–77. DOI 10.1145/3317287.3328534. Short version: Research for practice: Troubling trends in machine-learning scholarship, *Communications of the ACM* 62(6): 45–53 (2019). Preprint arXiv:1807.03341 (ICML 2018 Debates).
Key: `lipton2019troubling`

What it did: Identifies four trends: failure to separate explanation from speculation; failure to identify sources of empirical gains; "mathiness"; misuse of language (suggestive definitions, overloaded terms, suitcase words). Suggests causes include rapid community growth, thin reviewer pools and incentives favouring short-term success.

Relevance to us: Names the incentive environment (growth, thin reviewing) in which fashion could pay. Our null for branded titles bears directly on "misuse of language": catchy names do not carry an acceptance premium at ICLR. Framing; partly contradicts the worry that rhetorical packaging is rewarded.

### 5.4 Dehghani et al. 2021 — VERIFIED (arXiv preprint)
Dehghani, Mostafa, Yi Tay, Alexey A. Gritsenko, Zhe Zhao, Neil Houlsby, Fernando Diaz, Donald Metzler, and Oriol Vinyals. 2021. The benchmark lottery. arXiv:2107.07002.
Key: `dehghani2021benchmark`

What it did: Argues that which benchmarks a community adopts largely determines which methods appear superior, so progress claims depend on a "lottery" of benchmark choice; illustrates across ML subfields. (Content from title, abstract-level descriptions.)

Relevance to us: Benchmarks as the field's coordination device. Our contribution-type result (newcomers write fewer benchmark papers) speaks to *who* builds benchmarks: insiders, not entrants. Framing.

### 5.5 Koch, Denton, Hanna and Foster 2021 — VERIFIED
Koch, Bernard, Emily Denton, Alex Hanna, and Jacob G. Foster. 2021. Reduced, reused and recycled: The life of a dataset in machine learning research. In *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks 1 (NeurIPS 2021)*. arXiv:2112.01716.
Key: `koch2021reduced`

What it did: Papers With Code data (2015–2020 per NeurIPS/arXiv records): dataset use concentrates on fewer datasets within task communities, communities borrow datasets from other tasks, and many widely used datasets come from a few elite institutions.

Relevance to us: Closest ML-specific empirical prior on concentration/homogenization in research practice, using a scientometric design like ours. Complements our newcomer result: benchmark creation is concentrated and is not where newcomers enter. Closest prior (ML, concentration).

### 5.6 Bommasani et al. 2021 — VERIFIED (arXiv)
Bommasani, Rishi, et al. (114 authors). 2021. On the opportunities and risks of foundation models. arXiv:2108.07258.
Key: `bommasani2021opportunities`

What it did: Defines "foundation models"; argues scale yields emergence and that effectiveness across tasks "incentivizes homogenization", which gives leverage but means defects are inherited downstream; frames AI's history as increasing emergence and homogenization.

Relevance to us: Directly names the homogenization our FM result measures: in topics where FM adoption rises, fewer papers propose new architectures (replicated). Our data provide topic-level evidence of methodological homogenization at a major venue. Key framing; supports.

### 5.7 Raji, Bender, Paullada, Denton and Hanna 2021 — VERIFIED
Raji, Inioluwa Deborah, Emily M. Bender, Amandalynne Paullada, Emily Denton, and Alex Hanna. 2021. AI and the everything in the whole wide world benchmark. In *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks 1 (NeurIPS 2021)*. arXiv:2111.15366.
Key: `raji2021ai`

What it did: Argues a few influential benchmarks are treated as measures of general capability, a construct-validity problem; benchmarks are finite and contextual.

Relevance to us: Benchmark culture as status-conferring; with Dehghani and Koch it frames benchmark papers as an insider activity. Framing.

---

## Unverified candidates (do not cite as verified)

- Järvenpää, H. M., and S. J. Mäkinen. 2008. "An empirical study of the existence of the hype cycle: A case of DVD technology" and "Empirically detecting the hype cycle with the life cycle indicators: An exploratory analysis of three technologies" (IEEM 2008). Titles seen on a Tampere University portal; venue/pages not confirmed.
- Stelmakh, I., et al. "A large scale randomized controlled trial on herding in peer-review discussions" (arXiv:2011.15083; apparently PLOS ONE 2023, article e0287443). Reports no herding detected in reviewer discussions. Authors and journal details not confirmed. Potentially useful: herding in *peer review* at ML venues was tested and not found.
- Kuhn, T. S. 1962. *The Structure of Scientific Revolutions*. Not searched in this session.
- Griffith, B. C., and N. C. Mullins. 1972. "Coherent social groups in scientific change" (Science). Mentioned in a search result; not verified.
- A 2025 systematic review of the hype cycle "finding multiple inconsistencies" (seen only in a search summary; authors/venue unknown).

---

## Synthesis

### (a) What this literature already knows
1. Popularity waves need not track merit (Abrahamson 1991, 1996). Fashions spread through fashion setters and imitation, must look like progress, and have life cycles with an enthusiastic upswing and a cooler downswing (Abrahamson and Fairchild 1999).
2. Herding is individually rational and collectively inefficient; cascades start from few early movers and are fragile (Bikhchandani et al. 1992; Banerjee 1992). In science, risk aversion produces robust herding (Weisberg 2013) and conservative strategies dominate though risky ones have higher upside (Foster et al. 2015; Rzhetsky et al. 2015).
3. Imitating success stories can generate fad cycles even for modestly useful innovations; early adopters gain, late imitators do not (Strang and Macy 2001).
4. Bandwagons in science form around standardized, transportable theory–method packages that make problems do-able (Fujimura 1988). Research areas have logistic life cycles carried by social networks (Price 1963; Crane 1972; Mullins 1972).
5. The hype cycle is a practitioner template (Linden and Fenn 2003; Fenn and Raskino 2008) that academic tests find inconsistent and heterogeneous (Dedehayir and Steinert 2016; van Lente et al. 2013); expectations are performative (Borup et al. 2006).
6. In ML, critics argue the field converges for reasons other than merit: hardware fit (Hooker 2021), benchmark choice (Dehghani et al. 2021), dataset concentration in elite institutions (Koch et al. 2021), benchmark construct validity (Raji et al. 2021), homogenization around foundation models (Bommasani et al. 2021), and rhetorical inflation under growth and thin reviewing (Lipton and Steinhardt 2019). Sutton (2019) counters that convergence on general, compute-scaled methods is the efficient lesson.

### (b) What it does not know that our data can speak to
1. **The gatekeeper's side of a fashion.** Management-fashion and hype studies measure discourse volume (supply/adoption); they rarely observe an independent verdict on each adopter. We observe acceptance for every submission, including rejected and withdrawn ones, so we can ask whether a wave is *rewarded* differently on the way up and on the way down (PH6, kwtiming) — not just whether it exists.
2. **Whether waves survive hindsight.** Hype-cycle and specialty-life-cycle work usually draws curves with hindsight-defined categories. Our dated snapshots and early-vs-late topic maps show that hindsight-fitted maps can manufacture waves; this is a measurement result the fashion literature has not confronted.
3. **Who rides the wave.** Herding/cascade theory implies late entrants imitate cheaply. We can test this with the newcomer definition and contribution types, and the replicated answer is the opposite: newcomers write more method papers and fewer benchmark papers.
4. **The package bandwagon in ML, measured.** Fujimura's package theory and Bommasani's homogenization claim have not been tested at topic level across a decade of one venue; our FM-adoption/new-architecture result (replicated) is such a test.
5. **Out-of-sample discipline.** Fad narratives are built from vivid cases (Strang and Macy's success stories). We have a held-out replication: some patterns replicate (FM, newcomer, far-jump, insider, young keywords; PH6 weakly), while the starkest single case (federated learning) does not, and crowding and branding show no reward.
6. **Critiques of ML trend-following are mostly essays.** Hooker, Sutton, Lipton–Steinhardt, Dehghani et al., Raji et al. and Bommasani et al. are arguments or illustrations; Koch et al. is the main large-scale empirical study, and it covers datasets, not topics, authors or acceptance.

### (c) Candidate framings our findings could contribute to
1. **"Fashion is in the verdict, not in the map."** Main story candidate. Topic waves in ML are partly artefacts of hindsight-fitted maps, but a fashion-like signature does show up where the literature never measured it: in the gatekeeper's verdict, which favours early, rising ideas and cools after a wave's peak, while rewarding insiders and near moves. Organises: hindsight finding (measurement), PH6 + kwtiming (timing), insider + far-jump (who and how far), branding null and crowding null (what is *not* rewarded), FL (a vivid case that does not replicate).
2. **"Bandwagons without herders."** Fujimura-style package bandwagon (foundation models displacing new architectures) coexists with entrants who do *not* behave like cascade followers (newcomers write methods, not benchmarks). Contrasts package-driven convergence with the herding-of-individuals story that critics of ML assume.
3. **"Testing ML's self-critique."** Use the essay literature (hardware/benchmark lottery, troubling trends, homogenization) as a set of testable claims and report which hold at ICLR 2017–2026 under pre-registration and held-out replication: homogenization yes; rhetorical branding pays no; herding entrants no; timing advantage weakly yes.
4. **"Adaptive emulation in a conference."** Strang–Macy as the mechanism: modestly useful ideas, success stories, early adopters rewarded, late imitators not; the conference's acceptance gap is the performance signal that drives emulation. Cautious, since we have associations only.
5. **Methodological contribution to the hype-cycle literature:** dated snapshots plus held-out replication as a remedy for retrospective curve-fitting criticised by Dedehayir and Steinert (2016) and van Lente et al. (2013).
