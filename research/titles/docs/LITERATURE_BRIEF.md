# Research brief: Paper titles as a lens on research fashion at ICLR, 2017–2026

*This brief combines six literature reviews (each with citation checks) and four dataset-scouting reports. No work came back `not_found`. Where a check corrected a work, the corrected details are used. Claims that the checks could not confirm are marked **[unverified]**. Dataset numbers come from the scouts' scripts in `scratchpad/scout_*` and from the convenience extract. They are pilot numbers and must be re-run in a single harmonized pipeline before they are reported.*

---

## 0. Executive summary

- **What the literature covers.** About 60 years of title scientometrics links title form (length, colons, questions, humour, acronyms) to **citations** in **published** papers. These effects are small, depend on the field, and are heavily confounded by venue.
- **What it does not cover.**
  - No large-scale study links title form to **peer-review decisions** in ML. The closest are one ecology journal (Fox & Burns 2015), one causal estimate on an arXiv proxy (Veitch et al. 2020), and one PeerRead feature.
  - No study covers the **full submission population**, including rejected, withdrawn and desk-rejected papers.
  - No study analyses **ML title templates or branding as fashion**.
  - No study measures **LLM-era style change in titles** inside a single venue with yearly cohorts and author IDs.
- **What our data shows.** Four facts stand out, and none is documented elsewhere:
  1. **The "branding turn".** Colon titles went from 19% to about 60%, and "NAME:"-headed titles from about 7% to about 37%. The rise accelerates sharply at ICLR 2024. It happens within areas and in non-LLM papers, and it is driven by existing authors changing style rather than by new authors entering.
  2. **The post-ChatGPT excess in titles is about content, not style.** This is unlike abstracts. Style shifts do show up once meaning is held fixed inside a title slot (Enhancing vs Improving, OR about 4).
  3. **Most "fashion declines" are dilution.** For 84% of collapsed title terms, the 2026 count is at least as large as the count in their peak year.
  4. **Most raw title–acceptance "effects" are explained by team size and topic.**
- **Main risks.**
  - **Titles are a post-decision snapshot**, so camera-ready edits could reverse the causal direction.
  - **The export is a "discovery split"** covering about 77–83% of public counts, and `family_id` is unique for every row.
  - **Author IDs are only usable from 2021.**

---

## 1. State of the art by theme

### 1.1 Title form and citations (classic title scientometrics)

- **Length.** Most studies find a weak negative association with citations, and most of it is driven by venue.
  - Letchford et al. (2015, https://pmc.ncbi.nlm.nih.gov/articles/PMC4555861/): the paper-level Kendall τ ≈ −0.07, significant in 7 of 7 years. Adjusted for journal it drops to −0.02, significant in 4 of 7. The journal-level τ is −0.19 over **N=361 journals in 2010** (corrected from 625).
  - Hudson (2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5065898/): length is negative in 10 of 11 REF units; **computer science is not significant**.
  - Null results: Didegah & Thelwall (2013) and Heard et al. (2023).
  - Positive results: Habibzadeh & Yadollahie (2010, https://doi.org/10.3325/cmj.2010.51.165) and Jacques & Sebire (2010, https://pubmed.ncbi.nlm.nih.gov/21103094/).
  - The sign flips after 2000 in economics (Guo et al. 2018). The relation is non-linear (Sienkiewicz & Altmann 2016, https://arxiv.org/abs/1605.07465). Fox & Burns (2015) find an inverted-U for editorial success.
- **Colons and compound titles.**
  - Mostly positive: Buter & van Raan 2011; Hudson 2016 (pooled +0.106); Gnewuch & Wohlrabe 2016 ("short + non-alphanumeric"); Tran, Diep & Mushtarin 2024; Heard et al. 2023.
  - Negative: Jamali & Nikzad 2011. None: Hartley 2007.
  - Field-dependent: Buter & van Raan caution against adding colons where the field does not use them. Donovan (2025, https://journals.sagepub.com/doi/10.1177/09610006241311576) reviews 74 studies.
  - The only causal-style estimate for CS is Sato et al. (2022, https://arxiv.org/abs/2208.09862), a Twin Papers design on DBLP. A colon gives ATE **+0.356 in log2 citations** (about +28%; corrected from "+0.36 citations"). A longer title gives −0.126.
  - Prevalence baselines: DBLP CS colon share was about 10% in the late 1970s, 15–16% through the 2000s, and just over 20% in 2018 (Nelson 2018, https://www.kmjn.org/notes/colons_in_dblp_titles.html). Lewison & Hartley (2005) document lengthening and more colons over time.
- **Questions.**
  - Rose 50% to more than 200% across fields from 1966 to 2005 (Ball 2009).
  - More downloads but fewer citations (Jamali & Nikzad 2011). Negative in Hudson 2016 (−0.169). No benefit in Milojević 2017, and about 0% in maths and robotics there.
- **Declarative titles.** About 14% in ecology (Milojević 2017). Short, result-stating titles are cited more (Paiva et al. 2012). A randomized trial found no effect on readers' beliefs (Wager et al. 2016: 39.8 vs 32.6 mm, p=0.09; adjusted p=0.42).
  - *Jamali & Nikzad's claim that "declarative titles are cited less" could not be verified, so it is dropped.*
- **Humour.**
  - Negative in Sagi & Yechiam (2008). Linked only to downloads in Subotic & Mukherjee (2014).
  - **Heard, Cull & White (2023, https://doi.org/10.1139/facets-2022-0079)**: raw humour is negative, but authors give funny titles to papers they themselves rate as less important (inferred from self-citation). After correcting for that, citations about double from the least to the most humorous titles. Acronyms and taxonomic names are associated with fewer citations.
  - This is the key confounding lesson for our work: title style is chosen based on the author's private view of the paper's quality.
- **Long-run drift.**
  - Jiang & Hyland (2023, Learned Publishing 36(2):239–248): 36k titles from 6 disciplines over 60 years. Titles are about 50% longer, with more compound and question titles. Hard fields increasingly name the method.
  - Milojević (2017): the discipline is the strongest determinant of title form; author age and productivity matter little.
  - Anthony (2001): the pre-deep-learning baseline of 600 CS titles.
- **Acronyms.**
  - Barnett & Doubleday (2020, eLife): 0.7 → 2.4 acronyms per 100 title words (1950–2019), plateauing after about 2000. 79% of acronyms are used fewer than 10 times. Reuse is declining.
  - **Mandyam Rangarajan & Krishnan (2026, arXiv:2605.08889)**: NeurIPS title acronym density rose from 0.33 (1987) to 3.21 per 100 words (2024). *Their "89% rarely reused" figure is an **abstract**-level statistic, not a title one (corrected).*
  - Pottegård et al. (2014, BMJ): trial acronyms rose from 4.0% to 12.4% outside cardiology while acronym quality fell.

### 1.2 Titles in ML and NLP: memes, naming and templates

- **Memes.** Alyakin (2025, https://arxiv.org/abs/2512.19700): 717 arXiv "All You Need" titles, 69.6% in the canonical form, exponential growth in raw counts (R²>0.994), 200 in 2025. It has no denominator, no outcomes and no author analysis.
- **Title terms as topic proxies.** Mohammad (2019, NLP Scholar) uses title terms to track topics, with the "distinctive terms stop being distinctive" argument. It is topical and published-only.
- **Title generation.** Chen & Eger (2023): about 30k NLP/ML abstract-title pairs plus a humour-annotated set. ChatGPT zero-shot matches the best fine-tuned model. Models overfit frequent patterns.
- **Stance.** Beese et al. (2023): NLP/ML papers have become more negative recently, and critical papers are cited more.
- **Naming.** Model naming appears only in journalism (the Muppet-name trend in DeepLearning.AI's The Batch, 2019) and in software engineering (Jiang W. et al. 2025, Hugging Face naming). Snowclones were coined by Glen Whitman and popularized by Pullum (2004, *corrected attribution*).
- **Phrase dynamics, memes and wording.**
  - Kuhn, Perc & Helbing (2014, PRX): meme score = frequency × citation inheritance. Top APS memes are loop quantum cosmology, unparticle and sonoluminescence. *Graphene ranks #26 (corrected).*
  - MemeTracker (Leskovec et al. 2009) clusters phrase variants.
  - Sweed & Shahaf (2021) detect snowclones with wildcard tagging: BERT recall 0.88 on 7.7k pattern–instance pairs.
  - Shaib et al. (2024) measure syntactic templates in LLM output: 76% of model templates appear in pretraining data vs 35% for human text.
  - Danescu-Niculescu-Mizil et al. (2012): memorable phrasing combines distinctive words with a common syntactic frame.
  - Tan, Lee & Pang (2014): a same-author, same-content wording design.
- **Survival of linguistic innovations.**
  - Stewart & Eisenstein (2018): dissemination across linguistic contexts predicts survival (Cox β = −0.33); social dissemination adds nothing (χ²=4.6, p=0.80).
  - Altmann et al. (2011): a word's niche predicts its fate.
  - Del Tredici & Fernández (2018): innovators have many weak ties, and adoption by strong-tie users drives spread (F1 0.62 → 0.76).
  - Danescu-Niculescu-Mizil et al. (2013): users move from an innovative phase to a conservative one.
  - Bentley, Hahn & Shennan (2004): a neutral-drift null model.

### 1.3 Hype and promotional language

- **Lexical hype in biomedicine.**
  - Vinkers et al. (2015): positive words in PubMed rose from 2.0% to 17.5% (+880%); "novel", "robust" and similar words rose by up to 15,000%; neutral control words stayed flat.
  - Millar, Batalo & Budgell (2022): 139 hype adjectives in 8 categories. 130 rose, with a mean relative increase of 1,378%. The share of NIH abstracts with any hype adjective went from 72% to 97%. Only **funded** grants were studied.
  - Hyland & Jiang (2021) and Millar et al. (2019) give the corpus-linguistic grounding.
- **Hype and outcomes.**
  - Lerchenmueller et al. (2019): positive framing is associated with +9.4% citations, with a gender gap in its use.
  - **Peng, Qiu, Fosse & Uzzi (2024), *PNAS* 121:e2320066121, "Promotional language and the adoption of innovative ideas in science"** (*corrected from "Nature Communications"*): promotional language is associated with up to double the probability of funding in NIH, NSF and Novo Nordisk grants. This is the closest precedent showing an evaluator rewarding hype.
- **ML critique.** Lipton & Steinhardt (2018) cover suggestive definitions, overloaded terms and "mathiness". Bowman (2022) warns about underclaiming.
- **Measurement tools.** Certainty scoring (Pei & Jurgens 2021) and exaggeration detection relative to a source text (Wright & Augenstein 2021).
- **ICLR-specific evidence.** Xu et al. (2026) find that the Millar title-hype lexicon does not correlate with topic-level acceptance (r≈0.01).

### 1.4 Research fashion: theory and topic dynamics

- **Theory.**
  - Simmel (1904/1957): fashion is driven by imitation and differentiation. Elites adopt first and abandon first.
  - Abrahamson (1991, *"Managerial Fads and Fashions", AMR 16(3):586–612, doi:10.2307/258919*; 1996). **Correction:** Abrahamson criticizes applying aesthetic-fashion theory *unmodified*. Technical fashions must also appear rational and progressive.
  - Abrahamson & Fairchild (1999): fashion lifecycles in which upswing discourse is emotional and downswing discourse is measured.
  - Lieberson (2000): fashion changes from internal dynamics.
  - Berger & Le Mens (2009, PNAS): first names that rise faster are abandoned faster.
  - Bikhchandani, Hirshleifer & Welch (1992): informational cascades.
  - Fujimura (1988): bandwagons form around "doable problems" and "transportable packages", the analogue of today's benchmarks and APIs.
  - Bramoullé & Saint-Paul (2010): research cycles.
  - March (1991): exploration vs exploitation. Kuhn (1977): the essential tension. Merton (1968): the Matthew effect.
  - Lorenz-Spreen et al. (2019): collective attention is accelerating.
  - Bass (1969): the innovation (p) and imitation (q) diffusion model.
- **NLP and ML histories.**
  - Hall, Jurafsky & Manning (2008): LDA over the ACL Anthology.
  - Anderson, McFarland & Jurafsky (2012): ACL epochs; topics fade once bakeoff funding ends.
  - **Prabhakaran et al. (2016)**: topics framed as methods tend to be in early growth, and topics framed as results tend to be declining.
  - Pramanick et al. (2023): tasks and methods drive change; metrics matter little.
  - Gururaja et al. (2023): cycles in the field's history.
  - Movva et al. (2024): *half of 2023 LLM-paper first authors were **new to LLM research**, mostly from non-NLP CS (corrected).*
  - Abdalla et al. (2023): industry authorship rose 180%.
  - Singh et al. (2023) and Bollmann & Elliott (2020): citation recency. Bollmann & Elliott caution that apparent recency can be a **growth artefact**.
  - Michael et al. (2023): pluralistic ignorance about community beliefs.
  - Saphra et al. (2024): history repeating.
  - Klinger et al. (2020/22): AI research diversity has stagnated.
- **Same-venue competitors.**
  - **González-Márquez & Kobak (2024)**: 24,445 ICLR submissions, 2017–2024. Documents GAN/VAE/RNN declining and diffusion/LLM rising; finds no systematic acceptance differences across subfields. Title counts are anecdotal (366 "understanding", 155 "rethinking", 550 "?").
  - **Xu, Dai, Yang & Zhang (2026, arXiv:2607.27209)**: ICLR 2021–2026, BERTopic, descriptive. Emerging topics have higher acceptance (40.5% vs 32.2% in 2025; 32.5% vs 28.5% in 2026). Test-time scaling fell from 55.9% to 37.5% acceptance as its count grew from 34 to 323. Title hype has r≈0.01 with acceptance. **This is the closest competitor**: topic-level, top-10 topics only, no paper-level lifecycle position, no authors, no withdrawals.
  - **Huang (2026, arXiv:2607.05401)**: 36k ICLR papers. Review scores are unrelated to later disruptiveness (|ρ| ≤ 0.005).
  - Jung et al. (2025): ICLR acceptance drivers (rebuttal interaction, clarity, earlier submission).
  - Yang, Wei & Pei (2025): Paper Copilot review archive. *Its ICLR 2025 counts are unverified.*

### 1.5 Novelty, hotness and how evaluators respond

- **Novelty and impact.** Uzzi et al. (2013): atypical combinations paired with conventional ones roughly double the chance of a hit. Foster, Rzhetsky & Evans (2015): risky strategies are not compensated. Rzhetsky et al. (2015): research herds toward central entities. Wang, Veugelers & Stephan (2017): novel work gets delayed recognition and lands in lower-impact-factor venues.
- **How evaluators react.** Boudreau et al. (2016): +1 SD of novelty lowers a grant's rank by about 4.5 percentile points (*working-paper figure*). Teplitskiy et al. (2022): in journal submissions including rejected papers, novelty adds +5.9 pp and conventionality +19.9 pp.
- **Hotness, crowding and switching.** Sjögårde & Didegah (2022): fast-growing topics carry a citation premium. Newman (2009): first-mover advantage. Chu & Evans (2021): large fields ossify. Park, Leahey & Funk (2023): papers are becoming less disruptive. Hill et al. (2025): a "pivot penalty" for moving away from prior work. Zeng et al. (2019) and Jia, Wang & Szymanski (2017): topic switching. Myers (2020): high switching costs. Leahey, Lee & Funk (2023): new methods are disruptive. Shi & Evans (2023, Nat Commun 14:1641): surprise often comes from outsiders. Hofstra et al. (2020): the diversity–innovation paradox.
- **Text-only influence measures (no citations needed).** Kelly et al. (2021): backward/forward text similarity. Gerow et al. (2018): discursive influence. Shibayama et al. (2021): embedding novelty, built from the titles of *cited references*.

### 1.6 Peer review, text signals and causal inference with text

- **Acceptance prediction.**
  - PeerRead (Kang et al. 2018): on ICLR 2017, 65.3% vs a 57.6% majority baseline. Ablating title_length costs only −1.0 pt on arXiv. "State-of-the-art" in the abstract costs −3.5 on ICLR.
  - Page appearance alone predicts outcomes (Huang 2018). So do superficial text features (Checco et al. 2021) and review sentiment (Ghosal et al. 2019).
- **Closest causal title estimate: Veitch, Sridhar & Blei (2020).** The treatment is a "buzzy" title (deep / neural / embed / adversarial net) on the PeerRead arXiv proxy. The effect is +0.08 unadjusted and **−0.03 ± 0.01** after adjusting for abstract text with causal BERT. A theorem keeps +0.16 to +0.18.
- **Toolkit.** TextCause (Pryzant et al. 2021). Keith et al. (2020). Egami et al. (2022, Sci Adv 8(42), split-sample designs). Feder et al. (2022, TACL).
- **ICLR natural experiments. All of these drop withdrawn and desk-rejected papers or stop by 2022.**
  - Tran et al. (2020): top-10 institutions get a +0.15 score-equivalent boost at the AC level. Reproducibility falls from 75% to 66%. Score–citation correlation is 0.17 for accepted posters.
  - Sun, Barry Danfa & Teplitskiy (2022): double-blind review reduced prestigious authors' scores.
  - Bharadhwaj et al. (2020): arXiv posting plus reputation is correlated with acceptance.
  - Elazar et al. (2024): early arXiving has an effect under 4% in 7 of 9 settings.
  - Zhang et al. (2022): excludes withdrawn and desk-rejected papers.
  - Manzoor & Shah (2021): latent biases are recoverable from review text.
- **Prestige and visibility mechanisms.** Tomkins et al. (2017): single-blind odds multipliers of 1.63 (famous authors), 1.58 (top universities) and 2.10 (top companies). Rastogi et al. (2022): more than a third of reviewers search for the paper online, so distinctive titles aid search.
- **Noise ceilings.** Beygelzimer et al. (2023): committees disagree on 23% of NeurIPS 2021 papers. Cortes & Lawrence (2021): about 50% of score variation is subjective.
- **Other.** Resubmission bias (Stelmakh et al. 2021: −0.78 points). Rebuttals matter at the margin (Gao et al. 2019). Writing style vs review (Hengel 2022). Readability is declining (Plavén-Sigray et al. 2017). Resource and survey papers: NLPeer (Dycke et al. 2023), Kuznetsov et al. (2024), Yuan, Liu & Neubig (2022), The AI Scientist (Lu et al. 2024: 65% vs 66% balanced accuracy on ICLR 2022).

### 1.7 LLM-era writing

- **Distributional mixture estimates (Liang et al.).**
  - Reviews: ICLR reviews went from 1.6% to **10.6%** LLM-modified (ICLR 2024). "Meticulous" ×34.7, "commendable" ×9.8 (ICML 2024).
  - Papers: arXiv CS abstracts reached **22.5%** by Sep 2024 (Nature Human Behaviour 2025; the preprint reported up to 17.5%). Use is higher in crowded areas (23.0% vs 18.7%).
  - Society-wide: adoption plateaued in 2024 (Liang et al. 2025).
  - Detectors are biased against non-native writers (Liang et al. 2023).
- **Excess-vocabulary counterfactuals.**
  - Kobak et al. (2025, Sci Adv 11(27):eadt3813): **at least 13.5%** of 2024 PubMed abstracts, up to about 40% in some subcorpora. Excess words are mostly style verbs. *The count of excess words and the "delves" ratio differ across preprint and final versions, so cite only the 13.5% / 40% figures.*
  - Holzwarth et al. (2026): 89% of PMC open-access papers by end-2025.
- **Coevolution and model drift.**
  - Geng & Trotta (2024): about 35% of CS abstracts are LLM-style. Geng & Trotta (2025, Findings ACL): "delve" fell after being flagged while "significant" kept rising.
  - **Geng, Dong & Poibeau (2026)**: "via" and "beyond" in arXiv titles exceed trend from 2025, and newer models prefer them. *The CS vs non-CS split is shown for "via" only.*
  - Juzek & Ward (2025) point to RLHF as the source of overused words. Reinhart et al. (2025, PNAS) find systematic grammatical differences between LLM and human text.
- **Title-specific evidence (thin).**
  - Comas-Forgas et al. (2025, doi:10.1002/leap.1647): 15 verbs in Scopus titles rise. *The specific verb list is unverified.*
  - **Sebo et al. (2026, JMLA 114(3))**: ChatGPT titles are longer (median 16 vs 12.5 words) and use **colons 100% vs 30%**. n=50 medical abstracts.
  - Sebo et al. (2025, F1000Research): readers preferred AI titles in 61.8% of 1,049 judgements.
- **Other prevalence and complexity studies.** Gray (2024, 2025). Kousha & Thelwall (2025, arXiv; *journal venue unconfirmed*). Bao et al. (2025). Lin et al. (2025). Miletić & Falk (2026, ACL Anthology). Astarita et al. (2024).
- **Homogenization.**
  - Padmakumar & He (2024): writing with InstructGPT reduces content diversity.
  - Sourati et al. (2026, Nature Human Behaviour): complexity variance falls 21–50%.
  - Anderson, Shah & Kreminski (2024): ideas become less distinct.
  - Kirk et al. (2023): RLHF reduces output diversity.
  - Hao et al. (2026, Nature): AI-using science contracts topic range by 4.63%. *Here "AI" means ML methods, not writing tools.*
- **ICLR process confounds.**
  - Latona et al. (2024): at least 15.8% of ICLR 2024 reviews were AI-assisted; +4.9 pp acceptance near the threshold.
  - Thakkar et al. (2025): a randomized LLM review-feedback agent at ICLR 2025.
  - Pangram (Emi 2025, company blog; Naddaf 2025, Nature news): about 21% of ICLR 2026 reviews were fully AI-generated. Papers with more AI text received lower scores. *Not peer reviewed.*
  - Yamada et al. (2025): AI Scientist-v2 manuscripts at an ICLR workshop.
- **Outcome link.** Kusumegi et al. (2025, Science 390(6779):1240–1243): LLM adoption increases productivity, and complex language in LLM-assisted papers predicts lower publication. *These specific figures are **[unverified]**.*

### 1.8 Methods toolkit

- **Contrasts and change detection.**
  - Fightin' Words: log-odds with an informative Dirichlet prior (Monroe et al. 2008).
  - Kleinberg (2002) burst detection.
  - Changepoints: PELT (Killick et al. 2012), Bayesian online changepoint detection (Adams & MacKay 2007), ruptures (Truong et al. 2018), Kulkarni et al. (2015).
  - With only T=10 annual cohorts, prefer **segmented binomial GLMs with an a-priori 2024 break**, plus placebo breaks.
- **Semantic change.** Hamilton et al. (2016): laws of conformity and innovation.
- **Diversity.** Vendi score (Friedman & Dieng 2023). Compression ratio, Self-BLEU and the `diversity` package (Shaib et al. 2025, AACL). These measures correlate weakly, so report several, at **matched n and length**. Rarefied phrase diversity (Milojević 2015, which is computed on titles).

---

## 2. Already established about titles (do NOT claim as novel)

1. Titles are getting longer and more compound or colon-using across science (Lewison & Hartley 2005; Jiang & Hyland 2023; Milojević 2017). CS colon use was rising before 2018 (Nelson 2018).
2. Acronyms are increasing in titles, and most are rarely reused (Barnett & Doubleday 2020). NeurIPS title acronym density has risen about 10× (Mandyam Rangarajan & Krishnan 2026).
3. Title-form effects on impact are small, depend on the field, depend on venue and are often non-linear (Letchford et al.; Hudson; Buter & van Raan; Sienkiewicz & Altmann; Donovan 2025).
4. Question titles have grown in many fields and do not reliably help (Ball 2009; Milojević 2017).
5. Authors choose title style based on their private view of the paper, which confounds raw estimates (Heard et al. 2023).
6. Fashionable "buzzy" title words show no acceptance advantage after text adjustment (Veitch et al. 2020, arXiv proxy).
7. "X is all you need" grew exponentially on arXiv (Alyakin 2025).
8. Positive and hype vocabulary is rising in science (Vinkers et al.; Millar et al.). Promotional language is associated with funding (Peng et al. 2024).
9. LLM-associated vocabulary surged after ChatGPT in abstracts and reviews, CS most of all (Liang et al.; Kobak et al.; Geng & Trotta). Flagged words like "delve" then receded (Geng & Trotta 2025). "Via" and "beyond" rose in arXiv titles (Geng et al. 2026).
10. LLM-written titles are longer and use colons (Sebo et al. 2026), and readers prefer them (Sebo et al. 2025).
11. ML topics move in waves (GAN → diffusion → LLM), and emerging ICLR topics see higher acceptance at the topic level (González-Márquez & Kobak 2024; Xu et al. 2026).
12. Prestige, team resources and arXiv visibility affect ICLR outcomes (Tran et al.; Sun et al.; Bharadhwaj et al.; Elazar et al.).
13. LLM text in writing reduces diversity in controlled studies (Padmakumar & He; Sourati et al.).

---

## 3. Key dataset facts and surprising patterns

### 3.1 Population facts

- **Size.** 43,516 submissions. Per year: 385 / 774 / 1,255 / 2,071 / 2,364 / 2,649 / 3,872 / 5,766 / 8,960 / 15,420 (2017 → 2026), about 40× growth.
- **Acceptance population.** 32,534 papers; acceptance rate 0.315 (2020) to 0.441 (2025).
- **Withdrawals.** 21–25% of 2024–2026 submissions.
- **Desk rejections.** Under 1% until 2025. The 2026 regime is different: 737 papers (4.8%).
- **Area.** `primary_area` exists only for 2024+, and its taxonomy differs between 2024 and 2025–26.
- **Authors.** Profile IDs are usable from 2021. There are 89,131 IDs, 33,749 of them on two or more submissions.
- **Existing assets in the repo** (`research/titles/`):
  - `src/features.py` holds about 24 template regexes; the templates scout built a superset of 140 that should be harmonized with it.
  - Cached MiniLM and BGE title/abstract embeddings, `topics.parquet`, `author_features.parquet` and `resubmissions.parquet`.
  - **A partial camera-ready audit** (`cache/arxiv_audit.jsonl`, 265 rows). Among papers found on arXiv, the arXiv v1 title differs from the stored title for 36/146 accepted (25%) vs 18/55 rejected (33%). This is preliminary, small and selected (rejected papers are found less often), but so far accepted papers do **not** show more retitling.
  - The system Python lacks pyarrow, so the parquet caches cannot be read until it is installed.

### 3.2 The branding turn (shape of titles)

Scouts measure colon and acronym share slightly differently: colon share 58.5–59.7% in 2026, acronym head 34.9–38.4%.

| Measure | 2017 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Colon titles | 19.0% | 32.4% | 40.8% | 49.5% | 59.7% |
| Coined-name head ("NAME: …") | 6.5–7.0% | 17.4–18.8% | 23.9–25.0% | 30.9% | 36.6–38.4% |
| Mean words | 7.24 | 8.49 | – | – | 9.38 |
| Plain descriptive titles (no colon, no template) | 64.3% | – | – | – | 29.8% |

- **Interrupted time series at 2024** (with an LLM-topic control): level OR 1.19 [1.09, 1.30]; **slope OR 1.28/yr** (p=5e-35). Placebo breaks at 2021 and 2022 show no change.
- **Not a composition effect.** In non-LLM papers colon share went 31.9% → 54.8% (2023 → 2026). All 14 large areas rose from 2024 to 2026 (median +14.9 pp). About two thirds of the rise happens within areas.
- **Period effect, not cohort replacement.** Among last authors present in both 2022–23 and 2025–26, acronym use went 16.7% → 33.5%, against 17.4% → 35.1% in the population.
- **Detectable LLM drafting explains little of the shift.** In 2026 the LLM typographic markers (U+2011, en-dash compounds) appear in 1.52% of titles vs ≤0.13% before. Marker presence raises colon odds only to adjOR 1.24. **58.6% of 2026 titles with no markers still have a colon**, vs 32% in 2023. The markers have low recall, though.
- **Title Case has become nearly universal** (83% → 94%). Sentence case fell from 11.5% to 3.1%.

### 3.3 Lexical dynamics

- **Dilution, not abandonment.** Of 62 completed title "fashions" (share fell by at least half from a peak in 2023 or earlier), **52 (84%) had at least as many titles in 2026 as at their peak**.
  - Adversarial: share 9.5% → 1.3%, but count 119 → 203.
  - Only 10 fell in absolute count, e.g. convolutional 36 → 11 and architecture search 29 → 9.
- **Head-noun shift.** "network(s)" fell 31% → 3.6%. "model(s)" rose 9.6% → 20.5%, crossing over in 2023. "learning" stayed flat at about 30% until 2023, then fell to 16%.
- **Abbreviation becomes conventional.** Among LLM-mentioning titles, the abbreviation-only share went 0% (2023) → 28% → 52% → 69% (2026).
  - Pooled over 24 concepts, the abbreviation share grows with log cumulative prior mentions: β=0.30 (se 0.04) with concept and year fixed effects.
  - As a result, "large language" looks like a boom-bust while the concept itself grows.
- **Post-ChatGPT excess in titles is content-driven.** In 2024, only 2 of 24 robust excess words are style words ("enhancing", "meets"); together they make up about 7% of the excess gap. This is the opposite of Kobak's abstracts.
  - The 18 canonical "LLM words" show no significant union excess (ratio 1.04–1.12). "delve" declines.
  - A broader set of 33 marker families gives ratio 1.25–1.46, implying a lower bound of about 2.7–3.7% of titles with LLM-style excess.
- **Slot-controlled synonym competition** (meaning held fixed inside a title slot) shows a clean 2024 break.
  - Enhancing vs Improving: 13.5% (2023) → 44.6% (2024) → 66% (2026). The trend predicted 15.5%. **Post-2024 OR 4.29 [1.90, 9.68]** with topic fixed effects.
  - Comprehensive vs Systematic: OR 15.4.
  - Reveal slot (Unveiling, Uncovering, … vs Understanding, Analyzing, …): OR 3.91.
  - Control pairs show no break: Towards/Toward 1.43 (ns), novel/new 1.29 (ns), via/using 0.78.
- **The register turned over in 2026.** Within areas, the 2024–25 markers fell:
  - enhanc* 36.7 → 25.6 per 1k titles (z=−5.0; down in 12 of 16 areas).
  - Enhancing, Leveraging, Unveiling, Unleashing and Harnessing together: 3.16% → 2.07% (OR 1.54, p=2e-7).
  - Rising instead: "unified" 11.2 → 23.1 per 1k (up in 16 of 16 areas), "beyond" 9.0 → 16.6, "bridging", "unlocking", and "via" 9.0% → 12.5%.
  - There is only one post-reversal year.
- **Lexical turnover accelerated.** Three-year excess JSD was 0.029 for 2020→23 and **0.054 for 2023→26** (about 1.9×). The share of titles containing a word unseen in the previous 3 years rose from 0.70 to 0.85.
- **Short, symmetric cycles.** Median rise time is 2 years and median half-life is 2 years. There is **no Berger–Le Mens coupling** between rise speed and fall speed (ρ=0.04, p=0.73; low power).

### 3.4 Templates and snowclones

- **"All you need" is normalized fatigue.** 79 titles in total. Share peaks at 0.36% in 2023 and falls to 0.13% in 2026 (Fisher p=0.004). Raw arXiv counts hide this.
- **Replacement frames.**
  - "Can/Do LLMs …?" went 0 → 130 titles (0.84%).
  - "When X meets Y": 22 titles before 2024 vs 110 in 2024–26.
  - "X matters": 45 titles in 2026.
  - The snowclone family overall: 4 types in use (2018) → 37 types (2026); share 1.5–2.0%.
- **Fads.** "On the …" peaked in 2021. "Provable" peaked in 2022. "Learning to …" fell from 3.1% to 0.65%.
- **"via" displaced "using".** The via share among via/using titles went 48% (2018) → 91% (2026) gradually, with no 2024 jump.
  - **"using" titles have adjusted acceptance OR 0.64 [0.55, 0.74]**. This is robust to area fixed effects and team experience, and authors who use "using" tend to keep using it (OR 2.28).
- **Habits vs one-shot imitation.** Co-author-prior-use ORs:
  - Stock openers and formats are sticky: "Provable" 6.3, "using" 2.3, acronym colon 1.7.
  - **Snowclones are not repeated by the same authors**: family OR 1.04, and zero repeat users for most individual snowclones.
- **No early-adopter payoff** for 60 rhetorical templates (adoption-quantile OR 1.18 [0.52, 2.70]).
- **Homogenization is a "diversity illusion".**
  - Raw first-word entropy rises (7.42 → 8.23 bits) because every coined name is unique.
  - With names collapsed to `<NAME>`, entropy falls from 7.00 to 5.43 bits.
  - At fixed title length, function-word skeletons repeat more (0.44 in 2019 → 0.54 in 2026). "NAME : X for X" grew from 0.8% to 7.3%.

### 3.5 Outcomes and authors (associational; see the camera-ready caveat in §5)

- **Team size absorbs most raw title effects.** The raw acronym-head premium is +3.2 pp; with log(#authors) it becomes OR 0.94–1.03. The LLM-term premium goes from +1.9 pp to OR 0.99. Acceptance by team size ranges from 17.8% (1 author) to 59.7% (16+ authors).
- **Inconsistent subtype result.** One scout finds mixed-case coinages keep adjOR 1.10–1.14 while ALL-CAPS acronyms do not. This needs harmonized definitions.
- **Colon premium.** OR 1.15 [1.08, 1.23], or +3.2 pp. It holds within the same last author (+3.6 pp) and **shrinks as colons become the norm**: 1.30 in 2017–21 vs 1.12 in 2022–26 (interaction p=0.034).
- **Title length.** OR 0.84 pooled, but this is a **between-author composition effect**: within the same last author it is +2.9 pp per log word. Long titles do predict withdrawal (OR 1.30).
- **ALL-CAPS titles.** Accepted at 16.5% vs 40.5%, with OR about 0.31–0.38 in 9 of 10 years, within the same author, and concentrated among newcomers. **But** in the rejected-vs-withdrawn comparison, which involves no camera-ready stage, the difference is not significant (OR 1.16). Treat it as likely contaminated.
- **Sentence case.** adjOR 0.84 vs Title Case.
- **Withdrawal.** Acronym titles are withdrawn more often (OR 1.15). Among all 2024+ submissions, success is OR 0.92 for acronym titles vs 1.13 for non-acronym colon titles. So the suggested acceptance population carries selection from strategic withdrawal.
- **Momentum premium appears only post-ChatGPT.** Momentum is the mean prior-year growth of a title's words, built without lookahead.
  - 2024–26: OR 1.079/SD, or 1.048 with year × area fixed effects; also holds in non-LM papers.
  - 2019–23: not significant (1.018). Prior crowding was penalized then (OR 0.951).
- **Style is a person- or lab-level signature.** With no shared co-authors, the acronym lift is about 1.5×, and first-author persistence is about 2.1×. Hype words do **not** persist.
- **Newcomers brand more.** Repeat first authors use colons −4.7 pp and acronym heads −5.3 pp less than newcomers, with area fixed effects.
- **Other features.**
  - Digits: OR 1.45 raw, 1.24–1.33 adjusted, driven by "3D" and model versions.
  - Questions: no acceptance effect. In 2026, titles opening with an interrogative are desk-rejected more (7.8% vs 4.7%; "Can …" titles 11/53).
  - Capitalised backronyms and name collisions are rising: 5.6% of named heads in 2026 repeat an earlier head. PRISM appears 14 times.

---

## 4. Gaps where our dataset gives unique leverage

1. **Selection-free title science.** Every prior title, hype, meme or LLM-writing study conditions on publication, preprinting or funding. We observe rejected, withdrawn and desk-rejected papers. That lets us quantify survivorship bias and how the review filter shapes fashion.
2. **Decision-level outcomes in ML at scale.** 32.5k decided papers over 10 years, compared with about 400 in PeerRead and an arXiv proxy in Veitch et al.
3. **A clean pre/post-ChatGPT cohort boundary inside one venue** (2023 vs 2024), with three post cohorts. This allows interrupted time series, placebo breaks and coevolution analyses on *titles*. Title-level LLM evidence so far is only Scopus verbs, arXiv via/beyond, and n=50 regeneration studies.
4. **Author-level longitudinal data (2021+).** Within-author designs (fixed effects, persistence, stayer/entrant decomposition), co-author contagion, and newcomer vs veteran comparisons. Milojević (2017) found little author-level variation outside ML; no ML test exists.
5. **Fashion measurement that separates share from volume.** A 40× growth regime makes dilution vs abandonment testable and pushes for growth-normalized metrics.
6. **Templates and branding as fashion.** No lifecycle, diffusion or outcome analysis of "NAME:" branding, templates or snowclones exists beyond raw arXiv counts.
7. **Slot-controlled style measurement.** Synonym competition within fixed title frames separates style from topic. This is a new design compared with excess-word methods.
8. **Withdrawal as a strategic outcome.** It is never modelled in prior ICLR work, and our data shows it differs by title style.
9. **Paper-level lifecycle position and momentum.** Xu et al. (2026) work at the topic level and descriptively. We can build no-lookahead, paper-level trend exposure and show a regime change.
10. **Influence without citations.** Forward/backward text similarity (Kelly et al.) can test whether fashion-setters were rejected.

---

## 5. Pitfalls, confounders and data quirks

1. **Camera-ready reverse causation (the biggest threat).** All metadata is a single snapshot from 8–9 Sept 2026 with no title history. For accepted papers, the note was modified after the decision.
   - Formatting features (ALL-CAPS, Title Case, colon, name) may be edited after acceptance.
   - Mitigations:
     - Finish and extend the arXiv v1 audit; it currently shows no excess retitling among accepted papers (25% vs 33%), but it is partial.
     - Use rejected-vs-withdrawn contrasts, which involve no camera-ready stage.
     - Use within-author designs.
     - Prefer *descriptive and diachronic* claims, which are robust because they mostly involve the full pool, over acceptance claims.
     - If possible, fetch OpenReview revision history.
2. **Coverage.** The export is a "discovery split" (README), about 77–83% of public submission totals; 2026 has 15,420 vs about 19.6k public. `family_id` is unique for all rows, so resubmission families were removed or never linked.
   - Retitling and resubmission analyses are biased: the scouts found 98.4% "retitled", which is very likely an artefact.
   - State coverage explicitly and check whether the split is random with respect to title features.
3. **Team size and resources.** `declared_name_count` absorbs most raw title effects. Always control for it, plus topic (abstract-embedding clusters or fixed effects) and author track record.
4. **Topic and LLM-boom confound.** LLMs are both the writing tool and the dominant research topic of 2024–26. Separate style words from content words, run non-LLM-paper subsets, and use within-area fixed effects.
5. **Mechanical length effects.** Titles grew from 7.2 to 9.4 words, which inflates any "contains word w" share. Use length-matched or per-token rates.
6. **Sample-size effects.** 2017 has n=385 vs 15,420 in 2026. Diversity, entropy and JSD measures need rarefaction to equal n (and equal length). Fightin' Words priors dominate early years.
7. **Extrapolation fragility.** Kobak-style 3-year-ahead baselines produce floored ratios of 300–700 for declining words. Require excess under several baselines; 2024 is the clean year.
8. **Few time points.** T=10. Prefer a priori breaks, placebo breaks, binomial GLMs and FDR control across terms over generic changepoint detection.
9. **Author-ID censoring.** 2017–2020 IDs are about 99% hashed emails. "Repeat" status is left-censored at 2021, and the lookback grows over time. Use fixed-window robustness checks. Profile IDs are not verified persons. Names exist for 2017–2020 but carry homonym risk.
10. **Outcome coding.**
    - 2017 has no withdrawals. Withdrawn papers from 2018–2023 have decision "unknown"; use `administrative_status`.
    - 349 papers withdrawn in 2026 carry decision "rejected".
    - 27 accepted rows are inconsistent (13 desk-rejected, 14 withdrawn) and are excluded.
    - 2019 decisions come from a meta-review correction; run with and without 2019.
    - 2026 desk rejection is a new regime.
11. **Area taxonomy.** 2024 differs from 2025–26 (e.g. "general machine learning" vs "other topics in ML"). Crosswalk the labels or use year × area fixed effects.
12. **Title-string quirks.**
    - 15 placeholder titles (NA, Withdrawn, title, Placeholder) and 1 empty title.
    - 391 contain LaTeX. Exclude ratio colons (2:4, N:M). Handle 8 fullwidth colons.
    - 557 titles have double spaces; NFKC-normalize.
    - ALL-CAPS is concentrated in 2018–2020, likely PDF copy-paste or an interface change. Some 2026 titles are garbled PDF text.
    - Hyphenation variants (pre-trained / pretrained) need lemma grouping.
13. **Lexicon pitfalls.** Hype lists catch topical words ("navigation", "bridging", "unified", "comprehensive", "robust", "efficient"). The LLM regex catches pre-LLM language-model papers. Validate lexicons with ≥500 human-coded titles and report kappa.
14. **Process confounds.** AI-assisted reviewing (Latona et al.; Pangram), the 2025 LLM review-feedback RCT, and ICLR policy changes all affect 2024–26 outcomes. The 2018 double-blind switch and the 2018 rating-scale change affect early years.
15. **Multiple testing.** About 50–140 templates and features were scanned. Pre-register a confirmatory set, use a discovery/confirmation split (e.g. 2017–2023 vs 2024–26, or a held-out sample), and apply BH correction.
16. **Unverified literature details.** Avoid citing these numbers:
    - Kusumegi et al.'s figures.
    - Boudreau et al.'s published effect size.
    - The Liang NHB 22%/9% beyond the PDF-verified 22.5% CS abstracts.
    - Comas-Forgas's verb list.
    - Hartley's "THE piece" percentages.
    - Lewison & Hartley's 23% vs 6%.
    - The PeerRead ICLR accuracies are verified in one check and unverified in another; cite them from the paper's Table 5.

---

## 6. Candidate research questions

Difficulty and risk are rated L/M/H.

**RQ1. The branding turn: how, when and through whom did ML titles become "NAME: description"?**
- *Why novel:* Nelson 2018, Jiang & Hyland 2023 and Mandyam Rangarajan & Krishnan 2026 document level trends in published papers only. None decomposes the change or links it to the LLM boundary.
- *Data/method:*
  - Segmented logistic interrupted time series with placebo breaks.
  - Decomposition into within-area vs area-mix change (2024+), and stayer / entrant / exiter shift-share (2021+).
  - Non-LLM subsets; an LLM-marker link test.
  - Orthography subtypes (mixed-case vs ALL-CAPS vs backronym).
- *Difficulty/risk:* M / M. ChatGPT cannot be identified as the cause; frame as "accelerated at" rather than "caused by".

**RQ2. How much does the published record misstate title fashion and classic title effects?**
- *Why novel:* All title scientometrics is conditional on publication. Only Fox & Burns 2015 (one journal) includes rejected papers.
- *Data/method:* Compare feature trajectories for accepted vs the full pool vs withdrawn vs desk-rejected. Re-estimate the classic length, colon and question effects on an accepted-only "pseudo-citation" design vs the full pool. Quantify the timing and magnitude errors of fashion measures.
- *Difficulty/risk:* L / M. Some may see it as incremental; package it as a measurement contribution.

**RQ3. Do title features predict review outcomes once team, topic and author are controlled?**
- *Why novel:* Veitch et al. 2020 (4-word dictionary, arXiv proxy) and PeerRead (one feature) are the only precedents.
- *Data/method:*
  - Logit and linear probability models with year × area fixed effects, abstract-embedding controls, and double ML / AIPW.
  - Author fixed effects (first and last author).
  - Multinomial outcome (accept / reject / withdraw / desk-reject).
  - Oster / E-value sensitivity.
  - Rejected-vs-withdrawn contrasts to avoid camera-ready contamination.
- *Difficulty/risk:* M / H. The camera-ready problem and small effects; most raw effects already vanish under controls, which is a publishable null.

**RQ4. Slot-controlled synonym competition: a meaning-preserving measure of LLM-era style shift.**
- *Why novel:* Excess-word methods (Kobak et al.; Liang et al.; Geng et al.) mix topic and style. No study holds meaning fixed or works on titles.
- *Data/method:*
  - Define slot families (improve, reveal, leverage, comprehensive, mitigate) plus matched control pairs.
  - Trend-adjusted logit with topic fixed effects and a 2024 break.
  - Replicate on abstracts.
  - Per-author switching for authors linked across 2023 → 2024.
  - Ground-truth calibration by having several LLMs generate titles for held-out 2022–23 abstracts.
- *Difficulty/risk:* M / M. Slot choices are hand-made, so data-driven slot discovery via embedding paraphrase clusters is needed for robustness.

**RQ5. Do titles resist LLM style compared with abstracts in the same papers?**
- *Why novel:* Prior work covers abstracts or reviews; Geng et al. 2026 give no title-level rates.
- *Data/method:*
  - Kobak-style excess with multiple baselines, and a Liang mixture estimator fitted separately to titles and abstracts of the same papers.
  - Style vs content decomposition.
  - Paper-level coupling (abstract-marker density → title template).
- *Difficulty/risk:* M–H / M. Building the LLM reference distribution (Q) for 8–10-word strings is hard.

**RQ6. Style succession: did the LLM register turn over in 2026?**
- *Why novel:* Geng & Trotta 2025 show "delve" receding in arXiv abstracts. Model-generation signatures appear only in Geng et al. 2026. Neither covers titles, area-standardized rates, or authors.
- *Data/method:*
  - Area-standardized trajectories of flagged vs unflagged markers.
  - Replicate in abstracts.
  - Heterogeneity by author tenure.
  - LLM-version regeneration to map markers to model generations.
- *Difficulty/risk:* L–M / H. Only one post-reversal year; causes cannot be identified.

**RQ7. Dilution vs abandonment: what does "a fashion declines" mean in a growing field?**
- *Why novel:* Bollmann & Elliott 2020 raise the growth caveat for citations. Topic-fashion studies (González-Márquez & Kobak; Xu et al.) use shares.
- *Data/method:*
  - Poisson/NB count models with a log(N) offset plus an absolute trend.
  - A classification of terms into share-only decline vs absolute decline.
  - Generalize to keywords and abstract topics.
  - Duplication sensitivity analysis.
- *Difficulty/risk:* L / M. Risk of seeming obvious; strengthen with consequences, e.g. acceptance rates and author flows in diluted vs abandoned topics.

**RQ8. A regime change in rewarding timeliness: the post-2024 momentum premium.**
- *Why novel:* Xu et al. 2026 is topic-level and descriptive. Sjögårde & Didegah 2022 and Newman 2009 use citations.
- *Data/method:*
  - Paper-level momentum and crowding built without lookahead, from title words, keywords and embedding neighbourhoods.
  - Acceptance and withdrawal models with area fixed effects.
  - Interaction with cohort size and reviewer load.
  - A placebo using future momentum.
- *Difficulty/risk:* M / M. Confounding with topic quality; Xu et al. is a direct competitor, so differentiation is essential.

**RQ9. Lifecycle position: is there an early-adopter or late-adopter payoff for title terms and templates?**
- *Why novel:* Rogers-bin, Berger–Le Mens and Simmel tests have never been run on scientific vocabulary with peer-review outcomes.
- *Data/method:*
  - Adoption percentile per term.
  - Acceptance models on stacked panels with term-clustered standard errors.
  - Rise-vs-fall coupling across terms.
  - A status × timing interaction (2021+).
- *Difficulty/risk:* M / H. Low power; the scouts' pilots are null, which may still be reportable.

**RQ10. Title style as an author or lab signature, and what it implies for double-blind review.**
- *Why novel:* Prior de-anonymization work covers arXiv visibility (Bharadhwaj et al.; Rastogi et al.), not style.
- *Data/method:*
  - Persistence lifts with topic controls and no shared co-authors.
  - A title-only authorship-attribution classifier (top-k accuracy vs topic-only baseline).
  - A variance decomposition into person, lab and field.
- *Difficulty/risk:* M / M. Ethical framing is needed.

**RQ11. Do title templates spread through co-authorship (complex contagion)?**
- *Why novel:* Del Tredici & Fernández 2018 and Kuhn et al. 2014 work on Reddit and citations, not authorship. There is no ML test.
- *Data/method:*
  - An event study around a first collaboration with a template user, with matched controls.
  - Shuffled-network and time-placebo nulls.
  - Contrast sticky conventions with one-shot snowclones.
- *Difficulty/risk:* H / H. Homophily, left-censoring and a short panel.

**RQ12. Snowclones: one-shot imitation and frame replacement.**
- *Why novel:* Alyakin 2025 gives raw counts only.
- *Data/method:*
  - Normalized lifecycles.
  - Frame/filler separation via the topic-dispersion score (D≈1 means a frame, D≈0 means a topical phrase).
  - Author non-repetition vs a null model.
  - Replacement frames ("Can LLMs…?", "X matters").
  - Acceptance and desk-rejection rates.
- *Difficulty/risk:* L–M / M. Small counts; best as one component of a paper.

**RQ13. The diversity illusion: measuring title homogenization correctly.**
- *Why novel:* LLM homogenization evidence is experimental (Padmakumar & He; Sourati et al.). Field narrowing studies cover topics (Klinger et al.). Nobody separates lexical from structural diversity in a real corpus.
- *Data/method:*
  - Rarefied, length-matched entropy of skeletons and openers with names collapsed.
  - Vendi score on embeddings, compression ratio, Self-BLEU.
  - Within-area comparisons; all submissions vs accepted.
- *Difficulty/risk:* M / L–M. A strong methods lesson.

**RQ14. Lexical conventionalization in real time: diachronic Zipf abbreviation.**
- *Why novel:* Barnett & Doubleday measure acronym prevalence. No study measures the full-form → abbreviation transition as a function of cumulative usage.
- *Data/method:*
  - Concept pairs (24 or more, ideally mined automatically from parentheticals in abstracts).
  - A binomial GLM of abbreviation share on log cumulative prior mentions with concept and year fixed effects.
  - Time-to-abbreviation vs adoption speed.
  - Implication: share measures based on the full form underestimate growth.
- *Difficulty/risk:* L–M / L. Clean and NLP-flavoured.

**RQ15. Namespace crowding: coined names, backronyms and collisions.**
- *Why novel:* Barnett & Doubleday and Pottegård et al. cover biomedicine. ML naming has only journalistic and software-engineering coverage.
- *Data/method:*
  - Extract names and classify them (acronym, backronym, word, pun).
  - Collision rate vs a pool-growth null model.
  - Relate orthography and name type to outcomes and withdrawal.
- *Difficulty/risk:* M / M. Needs a validated classifier.

**RQ16. Venue-literacy and conformity signals: are outsider markers penalized?**
- *Why novel:* Hengel 2022 and Danescu-Niculescu-Mizil et al. 2013 do not cover ML conferences.
- *Data/method:*
  - Sentence case, ALL-CAPS, "using", "A novel …", and very long titles.
  - Newcomer concentration and acceptance/withdrawal with author fixed effects.
  - Strict camera-ready audit via arXiv v1 or revisions.
- *Difficulty/risk:* M / H. Camera-ready contamination is likely for formatting features; "using" (a lexical choice) is safer.

**RQ17. Does a concept's rhetorical slot in titles forecast its trajectory?**
- *Why novel:* Prabhakaran et al. 2016 work on abstracts and Web of Science. Titles and ML are untested.
- *Data/method:*
  - Parse titles into method slot ("via X", "X for Y") vs object slot ("Understanding X", "Rethinking X").
  - Predict share growth at t+1 and t+2 against frequency-only baselines (out-of-time evaluation).
- *Difficulty/risk:* M / M.

**RQ18. Prescience without citations: were fashion-setting submissions rejected?**
- *Why novel:* Huang 2026 uses citations and scores. Wang et al. 2017 find bias against novelty, but in journals.
- *Data/method:*
  - Kelly-style forward/backward similarity on title + abstract embeddings, growth-normalized.
  - Compare setter rates across accepted, rejected and withdrawn papers; "missed fashions".
- *Difficulty/risk:* M / M. Forward similarity rises mechanically with growth, so null models are needed.

**RQ19. Hype vs substance: do promotional titles accompany novel content, and are they rewarded?**
- *Why novel:* Peng et al. 2024 (grants) and Millar et al. 2022 (funded grants only). No ML-review test exists.
- *Data/method:*
  - A validated hype lexicon plus a certainty model.
  - Abstract semantic novelty and keyword atypicality (Uzzi-style z-scores).
  - The gap over time; acceptance and withdrawal.
- *Difficulty/risk:* M / M. Lexicon contamination by content words.

**RQ20. Title–abstract alignment and claim strength in the LLM era.**
- *Why novel:* Sebo et al. 2025 predict LLM titles are more aligned with abstracts; this is untested in a field corpus.
- *Data/method:*
  - Cosine and content-word overlap and NLI entailment between title and abstract.
  - Interrupted time series at 2024; association with outcomes.
- *Difficulty/risk:* L–M / M.

**RQ21. Predictability ceiling: how much decision signal does a title carry beyond topic, and is it falling?**
- *Why novel:* PeerRead used 2017 data only.
- *Data/method:* Temporal-split classifiers (title-only, abstract-only, metadata); within-area permutation tests; a ceiling compared with noise benchmarks (Beygelzimer et al.).
- *Difficulty/risk:* L / L. A supporting analysis.

**RQ22. The 2026 desk-rejection regime and title genres.**
- *Why novel:* Desk rejection has never been studied in ML.
- *Data/method:* Interrogative and "Can LLMs…?" titles, LLM typographic markers, and text-quality proxies vs desk rejection.
- *Difficulty/risk:* L / H. Small n and no reasons given.

**RQ23. Retitling on resubmission as a within-paper design.**
- *Why novel:* It mirrors Tan et al. 2014 and Sato et al. 2022, but with acceptance as the outcome.
- *Data/method:* Link by profile ID plus abstract similarity; difference-in-differences of title edits.
- *Difficulty/risk:* H / **very high under the current export**, because resubmission families appear excluded. Pursue only with the full corpus.

**Preliminary triage, for the next stage.** The strongest coherent package is a paper on "the branding turn and the LLM-era style shift in titles":
- Core: RQ1, RQ4, RQ5/6 and RQ13.
- Fashion-measurement contributions: RQ7 and RQ14.
- An outcome section built on the robust associational findings, with explicit camera-ready bounds: RQ3, RQ8 and RQ10.

RQ11, RQ22 and RQ23 are high-risk under the current data.

---

## 7. References (verified or corrected works only; deduplicated)

**Title scientometrics**
- Anthony, L. (2001). Characteristic features of research article titles in computer science. IEEE Transactions on Professional Communication 44(3):187–194. https://eprints.lancs.ac.uk/id/eprint/71623/
- Ball, R. (2009). Scholarly communication in transition: The use of question marks in the titles of scientific articles in medicine, life sciences and physics 1966–2005. Scientometrics 79(3):667–679. https://pred.uni-regensburg.de/id/eprint/28933/
- Barnett, A., & Doubleday, Z. (2020). Meta-Research: The growth of acronyms in the scientific literature. eLife 9:e60080. https://elifesciences.org/articles/60080
- Buter, R. K., & van Raan, A. F. J. (2011). Non-alphanumeric characters in titles of scientific publications. Journal of Informetrics 5(4):608–617. https://ideas.repec.org/a/eee/infome/v5y2011i4p608-617.html
- Didegah, F., & Thelwall, M. (2013). Which factors help authors produce the highest impact research? Journal of Informetrics 7(4):861–873. https://ideas.repec.org/a/eee/infome/v7y2013i4p861-873.html
- Donovan, J. M. (2025). Disciplinary variation in scholarly impact from two article title elements. Journal of Librarianship and Information Science 58(1):363–379 (print 2026). https://journals.sagepub.com/doi/10.1177/09610006241311576
- Fox, C. W., & Burns, C. S. (2015). The relationship between manuscript title structure and success: editorial decisions and citation performance for an ecological journal. Ecology and Evolution 5(10):1970–1980. https://pmc.ncbi.nlm.nih.gov/articles/PMC4449752
- Gnewuch, M., & Wohlrabe, K. (2016). Title characteristics and citations in economics. CESifo Working Paper 6235. https://www.ifo.de/DocDL/cesifo1_wp6235.pdf
- Guo, F., Ma, C., Shi, Q., & Zong, Q. (2018). Succinct effect or informative effect: the relationship between title length and the number of citations. Scientometrics 116(3):1531–1539. https://ideas.repec.org/a/spr/scient/v116y2018i3d10.1007_s11192-018-2805-8.html
- Habibzadeh, F., & Yadollahie, M. (2010). Are shorter article titles more attractive for citations? Croatian Medical Journal 51(2):165–170. https://doi.org/10.3325/cmj.2010.51.165
- Hartley, J. (2007). Planning that title: Practices and preferences for titles with colons in academic articles. Library & Information Science Research 29(4):553–568. https://ease.org.uk/2007/11/b-planning-that-title-and-the-use-of-colons/
- Heard, S. B., Cull, C. A., & White, E. R. (2023). If this title is funny, will you cite me? Citation impacts of humour and other features of article titles in ecology and evolution. FACETS 8:1–15. https://doi.org/10.1139/facets-2022-0079
- Hudson, J. (2016). An analysis of the titles of papers submitted to the UK REF in 2014. Scientometrics 109(2):871–889. https://pmc.ncbi.nlm.nih.gov/articles/PMC5065898/
- Jacques, T. S., & Sebire, N. J. (2010). The impact of article titles on citation hits. JRSM Short Reports 1(1):2. https://pubmed.ncbi.nlm.nih.gov/21103094/
- Jamali, H. R., & Nikzad, M. (2011). Article title type and its relation with the number of downloads and citations. Scientometrics 88(2):653–661. https://ideas.repec.org/a/spr/scient/v88y2011i2d10.1007_s11192-011-0412-z.html
- Jiang, F. K., & Hyland, K. (2023). Titles in research articles: Changes across time and discipline. Learned Publishing 36(2):239–248. https://ueaeprints.uea.ac.uk/id/eprint/90179/
- Letchford, A., Moat, H. S., & Preis, T. (2015). The advantage of short paper titles. Royal Society Open Science 2(8):150266. https://pmc.ncbi.nlm.nih.gov/articles/PMC4555861/
- Lewison, G., & Hartley, J. (2005). What's in a title? Numbers of words and the presence of colons. Scientometrics 63(2):341–356. https://ideas.repec.org/a/spr/scient/v63y2005i2d10.1007_s11192-005-0216-0.html
- Li, Z., & Xu, J. (2019). The evolution of research article titles: the case of Journal of Pragmatics 1978–2018. Scientometrics 121(3):1619–1634. https://link.springer.com/article/10.1007/s11192-019-03244-3
- Milojević, S. (2015). Quantifying the cognitive extent of science. Journal of Informetrics 9(4):962–973. https://arxiv.org/abs/1511.00040
- Milojević, S. (2017). The length and semantic structure of article titles. Frontiers in Research Metrics and Analytics 2:2. https://www.frontiersin.org/journals/research-metrics-and-analytics/articles/10.3389/frma.2017.00002/full
- Nelson, M. J. (2018). Colons in computer-science paper titles (blog note). https://www.kmjn.org/notes/colons_in_dblp_titles.html
- Paiva, C. E., Lima, J. P. S. N., & Paiva, B. S. R. (2012). Articles with short titles describing the results are cited more often. Clinics 67(5):509–513. https://www.elsevier.es/en-revista-clinics-22-estadisticas-articles-with-short-titles-describing-S1807593222018282
- Plavén-Sigray, P., Matheson, G. J., Schiffler, B. C., & Thompson, W. H. (2017). The readability of scientific texts is decreasing over time. eLife 6:e27725. https://doi.org/10.7554/eLife.27725
- Sagi, I., & Yechiam, E. (2008). Amusing titles in scientific journals and article citation. Journal of Information Science 34(5):680–687. https://yeldad.net.technion.ac.il/files/2016/12/JIS0537.pdf
- Sato, R., Yamada, M., & Kashima, H. (2022). Twin Papers: A simple framework of causal inference for citations via coupling. CIKM 2022 (short). https://arxiv.org/abs/2208.09862
- Sienkiewicz, J., & Altmann, E. G. (2016). Impact of lexical and sentiment factors on the popularity of scientific papers. Royal Society Open Science 3(6):160140. https://arxiv.org/abs/1605.07465
- Subotic, S., & Mukherjee, B. (2014). Short and amusing: The relationship between title characteristics, downloads, and citations in psychology articles. Journal of Information Science 40(1):115–124. https://journals.sagepub.com/doi/10.1177/0165551513511393
- Tran, H. D., Diep, P. P. U., & Mushtarin, N. (2024). "Insert witty catchphrase here!": do title elements influence engagement and citation? Scientometrics 129(11):6675–6691. https://ideas.repec.org/a/spr/scient/v129y2024i11d10.1007_s11192-024-05152-7.html
- Wager, E., Altman, D. G., Simera, I., & Toma, T. P. (2016). Do declarative titles affect readers' perceptions of research findings? A randomized trial. Research Integrity and Peer Review 1:11. https://pmc.ncbi.nlm.nih.gov/articles/PMC5803632/

**ML/NLP titles, memes, naming and linguistic innovation**
- Alyakin, A. (2025). "All You Need" is not all you need for a paper title: On the origins of a scientific meme. arXiv:2512.19700. https://arxiv.org/abs/2512.19700
- Altmann, E. G., Pierrehumbert, J. B., & Motter, A. E. (2011). Niche as a determinant of word fate in online groups. PLoS ONE 6(5):e19009. https://arxiv.org/abs/1009.3321
- Beese, D., Altunbaş, B., Güzeler, G., & Eger, S. (2023). Did AI get more negative recently? Royal Society Open Science 10:221159. https://arxiv.org/abs/2202.13610
- Bentley, R. A., Hahn, M. W., & Shennan, S. J. (2004). Random drift and culture change. Proceedings of the Royal Society B 271(1547):1443–1450. https://royalsocietypublishing.org/doi/10.1098/rspb.2004.2746
- Chen, Y., & Eger, S. (2023). Transformers go for the LOLs: Generating (humourous) titles from scientific abstracts end-to-end. Eval4NLP 2023. https://arxiv.org/abs/2212.10522
- Danescu-Niculescu-Mizil, C., Cheng, J., Kleinberg, J., & Lee, L. (2012). You had me at hello: How phrasing affects memorability. ACL 2012, 892–901. https://aclanthology.org/P12-1094/
- Danescu-Niculescu-Mizil, C., West, R., Jurafsky, D., Leskovec, J., & Potts, C. (2013). No country for old members: User lifecycle and linguistic change in online communities. WWW 2013, 307–318. https://dl.acm.org/doi/10.1145/2488388.2488416
- DeepLearning.AI The Batch (2019). Inside AI's Muppet empire. https://www.deeplearning.ai/the-batch/inside-ais-muppet-empire
- Del Tredici, M., & Fernández, R. (2017). Semantic variation in online communities of practice. IWCS 2017. https://aclanthology.org/W17-6804/
- Del Tredici, M., & Fernández, R. (2018). The road to success: Assessing the fate of linguistic innovations in online communities. COLING 2018, 1591–1603. https://aclanthology.org/C18-1135/
- Hofstra, B., Kulkarni, V. V., Munoz-Najar Galvez, S., He, B., Jurafsky, D., & McFarland, D. A. (2020). The diversity–innovation paradox in science. PNAS 117(17):9284–9291. https://www.pnas.org/doi/10.1073/pnas.1915378117
- Jiang, W., Kim, M., Cheung, C., Kim, H., Thiruvathukal, G. K., & Davis, J. C. (2025). "I see models being a whole other thing": An empirical study of pre-trained model naming conventions. Empirical Software Engineering 30:155. https://arxiv.org/abs/2310.01642
- Kuhn, T., Perc, M., & Helbing, D. (2014). Inheritance patterns in citation networks reveal scientific memes. Physical Review X 4:041036. https://arxiv.org/abs/1404.3757
- Leskovec, J., Backstrom, L., & Kleinberg, J. (2009). Meme-tracking and the dynamics of the news cycle. KDD 2009. https://snap.stanford.edu/memetracker/about.html
- Mandyam Rangarajan, A., & Krishnan, J. (2026). Machine learning research has outpaced its communication norms and NeurIPS should act. arXiv:2605.08889. https://arxiv.org/abs/2605.08889
- Mohammad, S. M. (2019). The state of NLP literature: A diachronic analysis of the ACL Anthology. arXiv:1911.03562. https://arxiv.org/abs/1911.03562
- Mohammad, S. M. (2020). NLP Scholar: A dataset for examining the state of NLP research. LREC 2020, 868–877. https://preview.aclanthology.org/setup/2020.lrec-1.109
- Nishi, K. (maintainer). awesome-all-you-need-papers. GitHub. https://github.com/KentoNishi/awesome-all-you-need-papers
- Pottegård, A., et al. (2014). SearCh for humourIstic and Extravagant acroNyms and Thoroughly Inappropriate names For Important Clinical trials (SCIENTIFIC). BMJ 349:g7092. https://pubmed.ncbi.nlm.nih.gov/25516539/
- Pullum, G. K. (2004, Jan 16). Snowclones: lexicographical dating to the second. Language Log (term coined by G. Whitman). http://itre.cis.upenn.edu/~myl/languagelog/archives/000350.html
- Shaib, C., Elazar, Y., Li, J. J., & Wallace, B. C. (2024). Detection and measurement of syntactic templates in generated text. EMNLP 2024. https://arxiv.org/abs/2407.00211
- Stewart, I., & Eisenstein, J. (2018). Making "fetch" happen: The influence of social and linguistic context on nonstandard word growth and decline. EMNLP 2018. https://aclanthology.org/D18-1467/
- Sweed, N., & Shahaf, D. (2021). Catchphrase: Automatic detection of cultural references. ACL-IJCNLP 2021 (short), 1–7. https://aclanthology.org/2021.acl-short.1
- Tan, C., Lee, L., & Pang, B. (2014). The effect of wording on message propagation. ACL 2014, 175–185. https://aclanthology.org/P14-1017/

**Hype and promotional language**
- Bowman, S. R. (2022). The dangers of underclaiming. ACL 2022. https://arxiv.org/abs/2110.08300
- Hyland, K., & Jiang, F. (2021). "Our striking results demonstrate…": Persuasion and the growth of academic hype. Journal of Pragmatics 182:189–202. https://doi.org/10.1016/j.pragma.2021.06.018
- Lerchenmueller, M. J., Sorenson, O., & Jena, A. B. (2019). Gender differences in how scientists present the importance of their research. BMJ 367:l6573. https://doi.org/10.1136/bmj.l6573
- Lipton, Z. C., & Steinhardt, J. (2018). Troubling trends in machine learning scholarship. arXiv:1807.03341 (ICML 2018 Debates). https://arxiv.org/abs/1807.03341
- Millar, N., Batalo, B., & Budgell, B. (2022). Trends in the use of promotional language (hype) in abstracts of successful NIH grant applications, 1985–2020. JAMA Network Open 5(8):e2228676. https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2795635
- Millar, N., Salager-Meyer, F., & Budgell, B. (2019). "It is important to reinforce the importance of…": "Hype" in reports of randomized controlled trials. English for Specific Purposes 54:139–151. https://doi.org/10.1016/j.esp.2019.02.004
- Pei, J., & Jurgens, D. (2021). Measuring sentence-level and aspect-level (un)certainty in science communications. EMNLP 2021. https://arxiv.org/abs/2109.14776
- Peng, H., Qiu, H. S., Fosse, H. B., & Uzzi, B. (2024). Promotional language and the adoption of innovative ideas in science. PNAS 121:e2320066121. https://doi.org/10.1073/pnas.2320066121
- Vinkers, C. H., Tijdink, J. K., & Otte, W. M. (2015). Use of positive and negative words in scientific PubMed abstracts between 1974 and 2014. BMJ 351:h6467. https://pmc.ncbi.nlm.nih.gov/articles/PMC4677695/
- Wright, D., & Augenstein, I. (2021). Semi-supervised exaggeration detection of health science press releases. EMNLP 2021. https://arxiv.org/abs/2108.13493

**Fashion theory and diffusion**
- Abrahamson, E. (1991). Managerial fads and fashions: The diffusion and rejection of innovations. Academy of Management Review 16(3):586–612. https://doi.org/10.2307/258919
- Abrahamson, E. (1996). Management fashion. Academy of Management Review 21(1):254–285. https://cebma.org/assets/Uploads/Abrahamson-1996.pdf
- Abrahamson, E., & Fairchild, G. (1999). Management fashion: Lifecycles, triggers, and collective learning processes. Administrative Science Quarterly 44(4):708–740. https://business.columbia.edu/faculty/research/management-fashion-life-cycle-triggers-and-collective-learning-processes
- Bass, F. M. (1969). A new product growth for model consumer durables. Management Science 15(5):215–227. https://doi.org/10.1287/mnsc.15.5.215
- Berger, J., & Le Mens, G. (2009). How adoption speed affects the abandonment of cultural tastes. PNAS 106(20):8146–8150. https://pmc.ncbi.nlm.nih.gov/articles/PMC2688844
- Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. Journal of Political Economy 100(5):992–1026. https://snap.stanford.edu/class/cs224w-readings/bikhchandani92fads.pdf
- Bramoullé, Y., & Saint-Paul, G. (2010). Research cycles. Journal of Economic Theory 145(5):1890–1920. https://www.tse-fr.eu/articles/research-cycles
- Fujimura, J. H. (1988). The molecular biological bandwagon in cancer research. Social Problems 35(3):261–283. https://doi.org/10.2307/800622
- Kuhn, T. S. (1977). The Essential Tension. University of Chicago Press. https://press.uchicago.edu/
- Lieberson, S. (2000). A Matter of Taste: How Names, Fashions, and Culture Change. Yale University Press. https://yalebooks.yale.edu/9780300173871/a-matter-of-taste
- Lorenz-Spreen, P., Mønsted, B. M., Hövel, P., & Lehmann, S. (2019). Accelerating dynamics of collective attention. Nature Communications 10:1759. https://www.nature.com/articles/s41467-019-09311-w
- March, J. G. (1991). Exploration and exploitation in organizational learning. Organization Science 2(1):71–87. https://ideas.repec.org/a/inm/ororsc/v2y1991i1p71-87.html
- Merton, R. K. (1968). The Matthew effect in science. Science 159(3810):56–63. https://pubmed.ncbi.nlm.nih.gov/5634379
- Simmel, G. (1904/1957). Fashion. International Quarterly 10:130–155; reprinted American Journal of Sociology 62(6):541–558. https://www.gwern.net/doc/sociology/1957-simmel.pdf

**Topic dynamics in NLP, ML and AI**
- Abdalla, M., et al. (2023). The elephant in the room: Analyzing the presence of Big Tech in NLP research. ACL 2023, 13141–13160. https://aclanthology.org/2023.acl-long.734
- Anderson, A., McFarland, D., & Jurafsky, D. (2012). Towards a computational history of the ACL: 1980–2008. ACL Workshop on Rediscovering 50 Years of Discoveries, 13–21. https://aclanthology.org/W12-3202/
- Bollmann, M., & Elliott, D. (2020). On forgetting to cite older papers: An analysis of the ACL Anthology. ACL 2020, 7819–7827. https://aclanthology.org/2020.acl-main.699
- González-Márquez, R., & Kobak, D. (2024). Learning representations of learning representations. DMLR Workshop at ICLR 2024. https://arxiv.org/abs/2404.08403
- Gururaja, S., Bertsch, A., Na, C., Widder, D. G., & Strubell, E. (2023). To build our future, we must know our past. EMNLP 2023, 13310–13325. https://aclanthology.org/2023.emnlp-main.822
- Hall, D., Jurafsky, D., & Manning, C. D. (2008). Studying the history of ideas using topic models. EMNLP 2008, 363–371. https://aclanthology.org/D08-1038/
- Huang, F. (2026). Catalyst papers in artificial intelligence research: A landscape on ICLR from 2017 to 2025. arXiv:2607.05401. https://arxiv.org/abs/2607.05401
- Jung, S., Pyeon, G., Heo, I., & Ahn, H. (2025). What drives paper acceptance? A process-centric analysis of modern peer review. arXiv:2509.25701. https://arxiv.org/abs/2509.25701
- Klinger, J., Mateos-Garcia, J., & Stathoulopoulos, K. (2020/2022). A narrowing of AI research? arXiv:2009.10385. https://arxiv.org/abs/2009.10385
- Michael, J., et al. (2023). What do NLP researchers believe? Results of the NLP community metasurvey. ACL 2023, 16334–16368. https://aclanthology.org/2023.acl-long.903
- Movva, R., Balachandar, S., Peng, K., Agostini, G., Garg, N., & Pierson, E. (2024). Topics, authors, and institutions in large language model research. NAACL 2024, 1223–1243. https://aclanthology.org/2024.naacl-long.67/
- Prabhakaran, V., Hamilton, W. L., McFarland, D., & Jurafsky, D. (2016). Predicting the rise and fall of scientific topics from trends in their rhetorical framing. ACL 2016, 1170–1180. https://aclanthology.org/P16-1111/
- Pramanick, A., Hou, Y., Mohammad, S. M., & Gurevych, I. (2023). A diachronic analysis of paradigm shifts in NLP research. EMNLP 2023, 2312–2326. https://arxiv.org/abs/2305.12920
- Saphra, N., Fleisig, E., Cho, K., & Lopez, A. (2024). First tragedy, then parse: History repeats itself in the new era of large language models. NAACL 2024, 2310–2326. https://aclanthology.org/2024.naacl-long.128
- Singh, J., Rungta, M., Yang, D., & Mohammad, S. M. (2023). Forgotten knowledge: Examining the citational amnesia in NLP. ACL 2023, 6192–6208. https://aclanthology.org/2023.acl-long.341
- Xu, B., Dai, X., Yang, F., & Zhang, K. (2026). Reviewer scores are not comparable across research areas in ML peer review. arXiv:2607.27209. https://arxiv.org/html/2607.27209
- Yang, J., Wei, Q., & Pei, J. (2025). Paper Copilot: Tracking the evolution of peer review in AI conferences. arXiv:2510.13201. https://arxiv.org/html/2510.13201v2

**Novelty, hotness and evaluation**
- Boudreau, K. J., Guinan, E. C., Lakhani, K. R., & Riedl, C. (2016). Looking across and looking beyond the knowledge frontier. Management Science 62(10):2765–2783. https://pubsonline.informs.org/doi/pdf/10.1287/mnsc.2015.2285
- Chu, J. S. G., & Evans, J. A. (2021). Slowed canonical progress in large fields of science. PNAS 118(41):e2021636118. https://pmc.ncbi.nlm.nih.gov/articles/PMC8522281
- Foster, J. G., Rzhetsky, A., & Evans, J. A. (2015). Tradition and innovation in scientists' research strategies. American Sociological Review 80(5):875–908. https://arxiv.org/pdf/1302.6906
- Gerow, A., Hu, Y., Boyd-Graber, J., Blei, D. M., & Evans, J. A. (2018). Measuring discursive influence across scholarship. PNAS 115(13):3308–3313. https://pmc.ncbi.nlm.nih.gov/articles/PMC5879694
- Hill, R., Yin, Y., Stein, C., Wang, X., Wang, D., & Jones, B. F. (2025). The pivot penalty in research. Nature. https://doi.org/10.1038/s41586-025-09048-1
- Jia, T., Wang, D., & Szymanski, B. K. (2017). Quantifying patterns of research-interest evolution. Nature Human Behaviour 1:0078. https://ideas.repec.org/a/nat/nathum/v1y2017i4d10.1038_s41562-017-0078.html
- Kelly, B., Papanikolaou, D., Seru, A., & Taddy, M. (2021). Measuring technological innovation over the long run. AER: Insights 3(3):303–320. https://www.nber.org/papers/w25266
- Leahey, E., Lee, J., & Funk, R. J. (2023). What types of novelty are most disruptive? American Sociological Review 88(3):562–597. https://experts.arizona.edu/en/publications/what-types-of-novelty-are-most-disruptive/
- Myers, K. (2020). The elasticity of science. AEJ: Applied Economics 12(4):103–134. https://www.aeaweb.org/doi/10.1257/app.20180518
- Newman, M. E. J. (2009). The first-mover advantage in scientific publication. EPL 86:68001. https://arxiv.org/abs/0809.0522
- Park, M., Leahey, E., & Funk, R. J. (2023). Papers and patents are becoming less disruptive over time. Nature 613:138–144. https://arxiv.org/abs/2106.11184
- Rzhetsky, A., Foster, J. G., Foster, I. T., & Evans, J. A. (2015). Choosing experiments to accelerate collective discovery. PNAS 112(47):14569–14574. https://pmc.ncbi.nlm.nih.gov/articles/PMC4664375
- Shi, F., & Evans, J. (2023). Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines. Nature Communications 14:1641. https://arxiv.org/abs/1910.09370
- Shibayama, S., Yin, D., & Matsumoto, K. (2021). Measuring novelty in science with word embedding. PLOS ONE 16(7):e0254034. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0254034
- Sjögårde, P., & Didegah, F. (2022). The association between topic growth and citation impact of research publications. Scientometrics 127:1903–1921. https://arxiv.org/abs/2106.08708
- Teplitskiy, M., Peng, H., Blasco, A., & Lakhani, K. R. (2022). Is novel research worth doing? Evidence from peer review at 49 journals. PNAS 119(47):e2118046119. https://pmc.ncbi.nlm.nih.gov/articles/PMC9704701/
- Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013). Atypical combinations and scientific impact. Science 342(6157):468–472. https://doi.org/10.1126/science.1240474
- Wang, J., Veugelers, R., & Stephan, P. (2017). Bias against novelty in science. Research Policy 46(8):1416–1436. https://www.nber.org/papers/w22180
- Zeng, A., et al. (2019). Increasing trend of scientists to switch between topics. Nature Communications 10:3439. https://pmc.ncbi.nlm.nih.gov/articles/PMC6668429/

**Peer review, text signals and causal inference with text**
- Beygelzimer, A., Dauphin, Y. N., Liang, P., & Vaughan, J. W. (2023). Has the machine learning review process become more arbitrary as the field has grown? arXiv:2306.03262. https://arxiv.org/abs/2306.03262
- Bharadhwaj, H., Turpin, D., Garg, A., & Anderson, A. (2020). De-anonymization of authors through arXiv submissions during double-blind review. arXiv:2007.00177. https://arxiv.org/abs/2007.00177
- Checco, A., Bracciale, L., Loreti, P., Pinfield, S., & Bianchi, G. (2021). AI-assisted peer review. Humanities and Social Sciences Communications 8:25. https://doi.org/10.1057/s41599-020-00703-8
- Cortes, C., & Lawrence, N. D. (2021). Inconsistency in conference peer review: Revisiting the 2014 NeurIPS experiment. arXiv:2109.09774. https://arxiv.org/abs/2109.09774
- Dycke, N., Kuznetsov, I., & Gurevych, I. (2023). NLPeer: A unified resource for the computational study of peer review. ACL 2023. https://arxiv.org/abs/2211.06651
- Egami, N., Fong, C. J., Grimmer, J., Roberts, M. E., & Stewart, B. M. (2022). How to make causal inferences using texts. Science Advances 8(42):eabg2652. https://doi.org/10.1126/sciadv.abg2652
- Elazar, Y., Zhang, J., Wadden, D., Zhang, B., & Smith, N. A. (2024). Estimating the causal effect of early arXiving on paper acceptance. CLeaR 2024. https://arxiv.org/abs/2306.13891
- Feder, A., et al. (2022). Causal inference in natural language processing: Estimation, prediction, interpretation and beyond. TACL 10:1138–1158. https://doi.org/10.1162/tacl_a_00511
- Gao, Y., Eger, S., Kuznetsov, I., Gurevych, I., & Miyao, Y. (2019). Does my rebuttal matter? Insights from a major NLP conference. NAACL 2019. https://aclanthology.org/N19-1129/
- Ghosal, T., Verma, R., Ekbal, A., & Bhattacharyya, P. (2019). DeepSentiPeer: Harnessing sentiment in review texts to recommend peer review decisions. ACL 2019, 1120–1130. https://aclanthology.org/P19-1106/
- Hengel, E. (2022). Publishing while female: Are women held to higher standards? Evidence from peer review. The Economic Journal 132(648):2951–2991. https://doi.org/10.1093/ej/ueac032
- Huang, J.-B. (2018). Deep Paper Gestalt. arXiv:1812.08775. https://arxiv.org/abs/1812.08775
- Kang, D., Ammar, W., Dalvi, B., van Zuylen, M., Kohlmeier, S., Hovy, E., & Schwartz, R. (2018). A dataset of peer reviews (PeerRead). NAACL-HLT 2018, 1647–1661. https://aclanthology.org/N18-1149/
- Keith, K. A., Jensen, D., & O'Connor, B. (2020). Text and causal inference: A review of using text to remove confounding from causal estimates. ACL 2020. https://arxiv.org/abs/2005.00649
- Kuznetsov, I., et al. (2024). What can natural language processing do for peer review? arXiv:2405.06563. https://arxiv.org/abs/2405.06563
- Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. arXiv:2408.06292. https://arxiv.org/abs/2408.06292
- Manzoor, E., & Shah, N. B. (2021). Uncovering latent biases in text: Method and application to peer review. AAAI 2021. https://arxiv.org/abs/2010.15300
- Pryzant, R., Card, D., Jurafsky, D., Veitch, V., & Sridhar, D. (2021). Causal effects of linguistic properties. NAACL 2021. https://arxiv.org/abs/2010.12919
- Rastogi, C., et al. (2022). To ArXiv or not to ArXiv: A study quantifying pros and cons of posting preprints online. arXiv:2203.17259. https://arxiv.org/abs/2203.17259
- Stelmakh, I., Shah, N. B., Singh, A., & Daumé III, H. (2021). Prior and prejudice: The novice reviewers' bias against resubmissions in conference peer review. CSCW 2021. https://arxiv.org/abs/2011.14646
- Sun, M., Barry Danfa, J., & Teplitskiy, M. (2022). Does double-blind peer review reduce bias? Evidence from a top computer science conference. JASIST 73(6):811–819. https://doi.org/10.1002/asi.24582
- Tomkins, A., Zhang, M., & Heavlin, W. D. (2017). Reviewer bias in single- versus double-blind peer review. PNAS 114(48):12708–12713. https://doi.org/10.1073/pnas.1707323114
- Tran, D., Valtchanov, A., Ganapathy, K., Feng, R., Slud, E., Goldblum, M., & Goldstein, T. (2020). An open review of OpenReview: A critical analysis of the machine learning conference review process. arXiv:2010.05137 (one review lists the same team's analysis as arXiv:2011.12919; reconcile before citing). https://arxiv.org/abs/2010.05137
- Veitch, V., Sridhar, D., & Blei, D. M. (2020). Adapting text embeddings for causal inference. UAI 2020 (PMLR 124). https://arxiv.org/abs/1905.12741
- Yuan, W., Liu, P., & Neubig, G. (2022). Can we automate scientific reviewing? JAIR 75:171–212. https://doi.org/10.1613/jair.1.12862
- Zhang, J., Zhang, H., Deng, Z., & Roth, D. (2022). Investigating fairness disparities in peer review: A language model enhanced approach. arXiv:2211.06398. https://arxiv.org/abs/2211.06398

**LLM-era writing and review**
- Anderson, B. R., Shah, J. H., & Kreminski, M. (2024). Homogenization effects of large language models on human creative ideation. ACM C&C 2024. https://arxiv.org/abs/2402.01536
- Astarita, S., Kruk, S., Reerink, J., & Gómez, P. (2024). Delving into the utilisation of ChatGPT in scientific publications in astronomy. SPAICE 2024, 241–246. https://arxiv.org/abs/2406.17324
- Bao, T., Zhao, Y., Mao, J., & Zhang, C. (2025). Examining linguistic shifts in academic writing before and after the launch of ChatGPT. Scientometrics. https://arxiv.org/abs/2505.12218
- Comas-Forgas, R., Koulouris, A., & Kouis, D. (2025). "AI-navigating" or "AI-sinking"? An analysis of verbs in research articles titles suspicious of containing AI-generated/assisted content. Learned Publishing 38(1). https://doi.org/10.1002/leap.1647
- Emi, B. (Pangram Labs) (2025). Pangram predicts 21% of ICLR reviews are AI-generated (company blog, not peer reviewed). https://www.pangram.com/blog/pangram-predicts-21-of-iclr-reviews-are-ai-generated
- Geng, M., Dong, Y., & Poibeau, T. (2026). Beyond Via: Analysis and estimation of the impact of large language models in academic papers. arXiv:2603.25638. https://arxiv.org/abs/2603.25638
- Geng, M., & Trotta, R. (2024). Is ChatGPT transforming academics' writing style? arXiv:2404.08627. https://arxiv.org/abs/2404.08627
- Geng, M., & Trotta, R. (2025). Human-LLM coevolution: Evidence from academic writing. Findings of ACL 2025. https://arxiv.org/abs/2502.09606
- Gray, A. (2024). ChatGPT "contamination": estimating the prevalence of LLMs in the scholarly literature. arXiv:2403.16887. https://arxiv.org/abs/2403.16887
- Gray, A. (2025). Estimating the prevalence of LLM-assisted text in scholarly writing. arXiv:2512.01560. https://arxiv.org/abs/2512.01560
- Hao, Q., Xu, F., Li, Y., & Evans, J. (2026). Artificial intelligence tools expand scientists' impact but contract science's focus. Nature (arXiv:2412.07727). https://arxiv.org/abs/2412.07727
- Holzwarth, L., González-Márquez, R., & Kobak, D. (2026). Most biomedical publications show signs of LLM-assisted writing. arXiv:2608.10715. https://arxiv.org/abs/2608.10715
- Juzek, T. S., & Ward, Z. B. (2025). Why does ChatGPT "delve" so much? COLING 2025. https://arxiv.org/abs/2412.11385
- Kirk, R., Mediratta, I., Nalmpantis, C., Luketina, J., Hambro, E., Grefenstette, E., & Raileanu, R. (2023). Understanding the effects of RLHF on LLM generalisation and diversity. arXiv:2310.06452. https://arxiv.org/abs/2310.06452
- Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. Science Advances 11(27):eadt3813. https://arxiv.org/abs/2406.07016
- Kousha, K., & Thelwall, M. (2025). How much are LLMs changing the language of academic papers after ChatGPT? arXiv:2509.09596 (journal venue unconfirmed). https://arxiv.org/abs/2509.09596
- Kusumegi, K., Yang, X., Ginsparg, P., de Vaan, M., Stuart, T., & Yin, Y. (2025). Scientific production in the era of large language models. Science 390(6779):1240–1243 (specific figures unverified). https://doi.org/10.1126/science.adw3000
- Latona, G. R., Horta Ribeiro, M., Davidson, T. R., Veselovsky, V., & West, R. (2024). The AI review lottery. arXiv:2405.02150. https://arxiv.org/abs/2405.02150
- Liang, W., Izzo, Z., Zhang, Y., et al. (2024). Monitoring AI-modified content at scale: A case study on the impact of ChatGPT on AI conference peer reviews. ICML 2024 (PMLR 235). https://proceedings.mlr.press/v235/liang24b.html
- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). GPT detectors are biased against non-native English writers. Patterns. https://arxiv.org/abs/2304.02819
- Liang, W., Zhang, Y., Codreanu, M., Wang, J., Cao, H., & Zou, J. (2025). The widespread adoption of large language model-assisted writing across society. arXiv:2502.09747. https://arxiv.org/abs/2502.09747
- Liang, W., Zhang, Y., Wu, Z., et al. (2025). Quantifying large language model usage in scientific papers. Nature Human Behaviour (preprint: Mapping the increasing use of LLMs in scientific papers, arXiv:2404.01268). https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf
- Lin, D., Zhao, N., Tian, D., & Li, J. (2025). Large language models reshape the language of science (v1: ChatGPT as linguistic equalizer?). arXiv:2504.12317. https://arxiv.org/abs/2504.12317
- Miletić, F., & Falk, N. (2026). What are LLMs doing to scientific communication? LREC 2026. https://arxiv.org/abs/2605.19936
- Naddaf, M. (2025). Major AI conference flooded with peer reviews written fully by AI. Nature (news). https://www.nature.com/articles/d41586-025-03506-6
- Padmakumar, V., & He, H. (2024). Does writing with language models reduce content diversity? ICLR 2024. https://arxiv.org/abs/2309.05196
- Reinhart, A., et al. (2025). Do LLMs write like humans? Variation in grammatical and rhetorical styles. PNAS 122:e2422455122. https://arxiv.org/abs/2410.16107
- Sebo, P., Nie, B., & Wang, T. (2025). Can ChatGPT write better scientific titles? F1000Research 14:1470. https://f1000research.com/articles/14-1470
- Sebo, P., Nie, B., & Wang, T. (2026). How ChatGPT writes scientific titles in medical research. Journal of the Medical Library Association 114(3). https://jmla.pitt.edu/ojs/jmla/article/view/2266
- Si, C., Yang, D., & Hashimoto, T. (2024). Can LLMs generate novel research ideas? arXiv:2409.04109. https://arxiv.org/abs/2409.04109
- Sourati, Z., et al. (2026). The shrinking landscape of linguistic diversity in the age of large language models. Nature Human Behaviour. https://arxiv.org/abs/2502.11266
- Thakkar, N., et al. (2025). Can LLM feedback enhance review quality? A randomized study of 20K reviews at ICLR 2025. arXiv:2504.09737. https://arxiv.org/abs/2504.09737
- Yamada, Y., et al. (2025). The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv:2504.08066. https://arxiv.org/abs/2504.08066

**Methods**
- Adams, R. P., & MacKay, D. J. C. (2007). Bayesian online changepoint detection. arXiv:0710.3742. https://arxiv.org/abs/0710.3742
- Friedman, D., & Dieng, A. B. (2023). The Vendi Score: A diversity evaluation metric for machine learning. TMLR. https://arxiv.org/abs/2210.02410
- Hamilton, W. L., Leskovec, J., & Jurafsky, D. (2016). Diachronic word embeddings reveal statistical laws of semantic change. ACL 2016. https://arxiv.org/abs/1605.09096
- Killick, R., Fearnhead, P., & Eckley, I. A. (2012). Optimal detection of changepoints with a linear computational cost. JASA 107(500):1590–1598. https://arxiv.org/abs/1101.1438
- Kleinberg, J. (2002). Bursty and hierarchical structure in streams. KDD 2002 (DMKD 7(4):373–397, 2003). https://dl.acm.org/doi/10.1145/775047.775061
- Kulkarni, V., Al-Rfou, R., Perozzi, B., & Skiena, S. (2015). Statistically significant detection of linguistic change. WWW 2015. https://arxiv.org/abs/1411.3315
- Monroe, B. L., Colaresi, M. P., & Quinn, K. M. (2008). Fightin' words: Lexical feature selection and evaluation for identifying the content of political conflict. Political Analysis 16(4):372–403. https://www.cambridge.org/core/journals/political-analysis/article/fightin-words-lexical-feature-selection-and-evaluation-for-identifying-the-content-of-political-conflict/81B3703230D21620B81EB6E2266C7A66
- Shaib, C., Govindarajan, V. S., Barrow, J., Sun, J., Siu, A. F., Wallace, B. C., & Nenkova, A. (2025). Standardizing the measurement of text diversity: A tool and a comparative analysis of scores. AACL 2025. https://arxiv.org/abs/2403.00553
- Truong, C., Oudre, L., & Vayatis, N. (2018). ruptures: change point detection in Python. arXiv:1801.00826. https://arxiv.org/abs/1801.00826

*Corrections applied:*
- Letchford: journal-level N is 361.
- Jamali & Nikzad: the declarative-title claim is dropped.
- Sato et al.: the effect is in log2 citations.
- Mandyam Rangarajan: first-author name corrected; the reuse statistic is abstract-level.
- Abrahamson (1991): DOI and title; Abrahamson (1996): argument direction.
- Movva et al.: "new to LLM research".
- Kuhn et al.: meme ranking.
- Peng et al. (2024): PNAS, not Nature Communications.
- Pullum: Whitman coined "snowclone".
- Heard et al.: the actual finding.
- Kobak et al.: published version.
- Jiang & Hyland, Habibzadeh & Yadollahie, Jacques & Sebire, Li & Xu, Comas-Forgas, Kusumegi et al.: bibliographic details completed.
- Pangram: cited as blog and news.

*Relevant local files:*
- Scout outputs: `/tmp/claude-0/-home-user-cloud-research/ac787a97-846c-54b7-93f0-8bd8a69ad531/scratchpad/scout_{surface-form,lexical-dynamics,templates-snowclones,outcomes-authors}/`
- Existing pipeline: `/home/user/cloud-research/research/titles/src/` (features.py, arxiv_audit.py, author_features.py, embed.py)
- Caches: `/home/user/cloud-research/research/titles/cache/` (embeddings, topics.parquet, resubmissions.parquet, arxiv_audit.jsonl)
- Data documentation: `/home/user/cloud-research/README.md`, `/home/user/cloud-research/DATA_DICTIONARY.md`