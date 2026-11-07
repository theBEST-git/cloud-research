# Proofreading fixes for the SCIE30001 report (decided; implement all)

Scope: the document itself (errors, consistency, readability, prose that reads machine-written). Do not re-check
results against data; use only numbers already in the report or given below. Files: Thesis.tex, Preamble/*.tex,
Chapters/Chapter1–6.tex, Bibliography.bib (this folder). Figures in figs/ are final (already regenerated: Fig 4.1
panel spacing and title "(b) The shift to foundation models", end labels 54.4% / 7.5%; Fig 5.1 rows "Measurement
paper (benchmark, dataset or evaluation)" and "First-time team vs returning topic newcomer: method paper"; Fig 6.1
"percentile pts"). Do not edit figures.

## Hard constraints (from the author)
- Do NOT mention use of AI or LLM assistance for writing or coding anywhere (no preface paragraph, no
  acknowledgement). The LLM that labels contribution types is part of the research method and stays, described
  generically ("an LLM with a fixed codebook"); do not name a product.
- Keep this exact phrase once: "a pre-registered out-of-sample replication, not a certified untouched holdout".
- Keep evidence labels on findings (\lab{replicated}, \lab{held-out supported}, \lab{exploratory}; and the words
  inconclusive / uninformative), but they may be stated once per paragraph in prose instead of tagged after every
  number. Tables keep a Label column.
- Voice: "we" in the chapters (academic convention); "I/my" only in the Declaration, Preface and Acknowledgements.
  Replace "the author" with "we" in chapters and with "my" in the Preface.
- Keep `% TODO(author)` next to the hand-check sentence ("we hand-checked a small random sample"); no numbers.
- Associations only; no causal wording. Keep chapter structure and the template.

## Errors to fix
1. Crowding contradiction. The registered crowding test predicted a PENALTY for crowded topics. Table 2.1 Gate cell
   for imitation → "Acceptance responds to crowding (the registered test predicted a penalty); a premium for branded
   titles and for keywords near their peak". Ch2 text: say imitation's entry predictions and the registered crowding
   test are the hypotheses registered before any outcome was read; rewarded imitation would predict a premium, so
   either sign would show review responding to the crowd.
2. Labels and rules (Ch1 definitions, Ch3 protocol):
   - REPLICATED = "a registered test whose discovery result, in either direction, was confirmed on held-out papers by
     a test registered before the held-out data were read".
   - Add in Ch3: "A declared held-out test is supported if its one-sided p is below 0.05; Holm-adjusted values across
     the six secondary held-out tests are reported alongside but do not set the label." (keeps the insider HELD-OUT
     SUPPORTED, consistent with the Emerging-keyword row being exploratory for other reasons: its two-sided interval
     includes 0 and it was demoted).
   - Define in Ch3: a test that is not supported is "uninformative" when its estimate lies below its MDE80 and
     "inconclusive" otherwise or when no MDE80 is available.
   - Replace "replicated" used as a plain verb for held-out-supported results with "held up on held-out papers"
     (Ch1 summary, Ch6 opener, Ch6 field-record paragraph).
   - Table 5.1 flocking row: held-out cell "--" and a note "no held-out test was registered".
   - Label columns: set every entry in the same style (small caps via \lab{}), including inconclusive,
     uninformative and "registered variant".
3. Explain the discovery/held-out split in Ch3 Corpus: "The discovery set (43,480 submissions with a usable abstract)
   was used to develop and run the registered tests. The held-out set (11,099 papers) consists of submissions that the
   data source had reserved for confirmation; they were released to us only after the discovery tests had been
   registered and run." Gloss "discovery corpus" at first use in Ch1 ("our discovery set (Chapter 3)").
4. Pointers to material not in the report:
   - Ch3: "The registration and each later declaration are dated documents kept with the analysis code."
   - Define once in Ch3: "Each registered test was re-run under pre-specified variants (other topic maps and numbers of
     topics, a year-balanced map, subsets of years and of papers); tests were grouped into families by research
     question for the Holm correction." Then "in its family", "counted variants" read correctly; "All 10" → "All ten".
   - Ch6 "the six keywords inspected first" → "the six keywords examined before this test was declared".
   - Table 6.1 note c: list all six: topic-edge slope 0.019, edge prediction 0.026, same-author closeness 0.026,
     insider 0.052, Emerging keywords 0.063, same-author distance slope 0.22.
   - Co-author simulation: "though unmeasured differences in co-author quality could also bias it; a simulation run
     before the held-out test showed that such a confounder can shift the estimate."
   - Declaration: "exclusive of tables, figures and the bibliography."
5. Front matter: Declaration grammar → "declare that this report, titled `…', and the work presented in it are my
   own". Preface: "This report is my own work for …". Abbreviations: expand "large language models (LLMs)" at first
   use (Ch1) and "percentage points (pp)" at first use; "p10" in Table 6.1 → "10th percentile". Symbols: delete the
   b row (or use "slope b" in Ch6 — choose one); "κ" → "Cohen's κ" (and "Cohen's κ = 0.93" in Ch3); unit "cosine" →
   "cosine similarity".
6. Terminology:
   - One name for the category: "measurement paper" (define once: dataset, benchmark or evaluation paper); Ch4's
     "empirical or evaluation papers" is a different registered measure — say "empirical or evaluation papers (a
     separate registered measure)".
   - "class" / "type" → "contribution type".
   - Define "the FM era" once as 2024–2026 and use it only for that period; the FM-uptake analysis covers 2023–2026 and
     must not be called the FM era.
   - "fits every route" → "fits both routes".
   - Define Emerging (young, rising keywords) and Mainstream (old, flat keywords) at first use.
   - Define declining topics in Ch4: "and declining if its 2024–2026 share is at most a third of its 2017–2020 share".
   - Define "topic map" in Ch3: "A topic map is one k-means clustering (k = 100) of SPECTER2 embeddings fitted on a
     given set of years; a topic is one cluster."
   - Table 6.1 row → "Change in FM premium per logit unit of prior adoption". Table 6.1 group headings to match Fig 6.1:
     "Referenced to the team's own record", "Referenced to others or the field".
   - "pre-registered" elsewhere → "registered" (except the mandated phrase).
   - "one logged, gated run" → "one logged run".
7. Undefined terms before use: "follow-on entry" → "follow-on work (benchmarking or evaluating others' methods)";
   "the popular form" / "riding a wave" → "branded titles (a short coined name and a colon) or keywords near their
   peak"; "the rising curve" → "the rising FM share (Figure 4.1b)".
8. Numbers and signs:
   - Newcomer share: write "73%" (the profile shares 26.3% + 46.7% sum to 73.0%).
   - Avoid "less often … −x": Ch5 FM-uptake → "the gap in FM-paper share is −4.58 pp [−6.55, −2.60], widening to
     −14.71 [−19.82, −9.61] as adoption rises"; Ch6 within-person → "the same author's acceptance is 1.37 pp lower
     (−1.37 [−2.74, −0.004])"; footnote → "Newcomer papers as a whole have 10.2 pp lower acceptance (−10.2 [−11.8,
     −8.7])".
   - Fig 1.1 and acceptance tests start in 2018: add "(2017 serves only as earlier history)" where 2018–2026 first
     appears in Ch3.
   - "Across/for every decided submission" → "using decided submissions, rejected ones included"; drop the Ch6
     repetition.
   - Fig 4.1 caption: "out-of-sample R² = 0.28 against −0.03"; also "contribution types assigned by the LLM" instead
     of "LLM labels".
   - Table 5.1 held-out "−0.98": show "−0.98 (p = 0.10)".
   - "the method gap does not move" → "the method gap barely changes".
   - Use "=" in statistics: "κ = 0.93", "p = 0.089", "p = 0.16", "Holm-adjusted p = 0.052", "power = 0.89",
     "power = 0.47".
   - "accepted +1.74 pp … more often" → "accepted 1.74 pp more often"; same for "+0.55 pp … higher".
9. Citations: Ch2 → "we borrow the distinction but not their welfare conclusions, which \citet{alexander2015epistemic}
   dispute." Bibliography: add `howpublished = {Blog post}` to the Sutton entry if absent.
10. Grammar: Ch1 NLP sentence → "The LLM wave also involves natural language processing (NLP) researchers, who
    increasingly publish at ML venues"; "too small to confirm" → "lacked the power to confirm"; "We registered that"
    → "We registered the prediction that"; "held on held-out papers" → "were supported on the held-out papers"; Fig 5.1
    caption row 3 → "row 3 compares papers by returning topic newcomers with incumbent papers"; "fourth fifth" →
    "fourth quintile"; ranges "from 2017–2026" → "in 2017–2026" (or "from 2017 to 2026").
11. Layout: tables \scriptsize → \footnotesize (widen or wrap columns so nothing overflows). Fig 4.1 at 0.62\textwidth
    or wider. Fig 1.1 caption: "Keyword trends at ICLR" (GANs and LLMs are trends, not waves by the definition);
    keep the wave-count sentence. Avoid near-empty pages and a float alone on a page with a large gap (try [tb]/[htbp]).

## Prose that reads machine-written (fix)
- "direction, not size" appears ~8 times: keep ONE sentence in Ch3 ("Because held-out tests are one-sided, a supported
  held-out test confirms the sign of an association; its size should not be compared with the discovery estimate.")
  and delete the rest (captions, tables, Ch4, Ch5).
- Reduce "X, not Y" antitheses: abstract last sentence → "The conformity visible at ICLR is anchored to researchers'
  own records rather than driven by the crowd." (uses the title word); Ch3 LLM consistency sentence → "This measures
  consistency between two LLM passes; it does not establish agreement with human coders, which for zero-shot LLM labels
  is often only fair \citep{ziems2024can}."; Ch5 heading → "Topic newcomers and first-time ICLR teams"; drop ", not
  farther"; "keeps part of its edge, not all of it" → "keeps only part of its edge".
- Vary "detectable/detectably/neither…nor" (≈11 uses) and "goes with / sits with / sit farther" (≈13 uses): use
  "is associated with", "is higher for", "is concentrated among", "lies farther from", and state the evidence.
- Private shorthand: use "record" only for the team's own earlier work; elsewhere "earlier ICLR submissions" or
  "earlier ICLR work as a whole" ("a topic's record" → "a topic's existing body of work"; "the field's record" →
  "earlier ICLR work as a whole"). "sites" → "levels". Abstract "Where the routes part" → "Where the two routes make
  different predictions". "is real but regresses" → "persists but shrinks towards the mean". "the newcomer flag" →
  "newcomer status (r = −0.57)". Insider sentence → "status explains it equally well: each additional insider adds only
  0.58 pp more than each additional experienced author from another topic (p = 0.16)". "rewarded imitation" →
  "imitation, if review rewards it,". "These associations are referenced to a record" → "These associations all involve
  closeness to the team's own earlier work". Table 5.1 "Flocking" → "Entry into hot topics". "In the same space" → "In
  the same SPECTER2 embedding space".
- Process notes: Ch1 → "Hypotheses were registered before any paper in the full corpus was labelled, and outcomes
  were examined only once, in a single pre-specified analysis run, ..."; Ch3 → "Outcomes were examined only by
  pre-committed analysis code, in a single logged run"; Ch2 → "continuity's predictions were formulated after the tests
  had been run and are used here only to organise the results." Delete "Uses no acceptance data." from the three
  captions and say once in Ch3 that the field and entry analyses use no acceptance decisions. Fig 6.1 caption: keep the
  colour key, verdict key and scales; move the provenance sentences (registered / explored / post hoc / declared) to
  the Ch6 text in one sentence. "We disclose two weaknesses." → "Two limitations should be noted." Drop annotations
  "(the declared primary test)", "(two different comparisons)" → explain in a clause.
- Hedges: keep "To our knowledge" once (Ch1) and drop "among the works we checked"; delete the Ch2 repeat. Ch6
  titles: "the held-out test is uninformative (below its MDE80 of 3.2), so the premium remains exploratory". Ch4
  "not supported, inconclusive" → "inconclusive". Ch5 → "Neither contribution type nor embedding distance measures
  originality; these results argue against newcomers following others but say nothing about whether their work is more
  original."
- Compressed sentences: apply — Ch3 code links ("Links to code repositories, usually added after acceptance, appear in
  17.6% of accepted but only 0.5% of rejected 2023–2026 abstracts and so leak the outcome [cite]. Removing them leaves
  the discovery estimates of the distance-based acceptance tests unchanged; the check is not possible for held-out
  papers."); Ch5 t-statistics ("are too large to be explained by the inflated false-positive rate reported in Chapter
  3"); "present in every era, so it predates the FM wave" → "it appears in every period, including before 2023";
  "team size is the only resource we measure" → "team size is the only resource we observe; others, such as compute,
  may also matter"; "In 2023–2026 topics at 5–50% prior FM adoption" → "Among 2023–2026 papers in topics where 5–50% of
  the previous year's papers built on FMs"; "The plainest imitation-like spread in the corpus is in form" → "The
  clearest sign of imitation in the corpus is in title style"; "about half goes with topic, type, FM use and team
  size" → "about half of each gap is explained by topic, contribution type, FM use and team size"; "Neither shows the
  flat premium that rewarded imitation of what is popular predicts" → "Neither pattern shows the constant premium for
  popular keywords that imitation would predict if review rewarded it."
- Repetition: give Ch4, Ch5 and Ch6 one-sentence openers that state the chapter's question instead of repeating the
  Ch1 summary (e.g. Ch4: "This chapter asks which changes in the field are passing fashions and which persist."). Keep
  the Hill et al. comparison in Ch1 only. Avoid "also … also".
- Conference residue: in Ch1 turn "We contribute:" bullets into "This report makes three contributions." with First /
  Second / Third (bullets may stay but read as prose); add a closing roadmap paragraph: "Chapter 2 sets out the two
  routes and what each predicts. Chapter 3 describes the data, measures and testing protocol. Chapters 4, 5 and 6 report
  results for the field, for entry to topics and for the acceptance decision."
- Use "anchored" in the abstract's last sentence and once in the Ch6 opener.

## Abstract (use this, adapted to "we")
"Machine learning is often said to herd: researchers chase what is popular, and peer review rewards them for it. But a
field can converge without copying. Researchers may instead stay close to a record: their own earlier work, or a topic
they already know. We call these two routes to conformity imitation and continuity, and test the herding account where
they make different predictions. The data are 43,480 ICLR submissions from 2017 to 2026, including rejected and
withdrawn papers; hypotheses were registered before any outcome was examined and re-tested on 11,099 held-out papers.
The field did converge on foundation models, but both routes predict this, and the number of topics that appear to be
emerging depends on hindsight: between 8 and 29, depending on which years the topic model is fitted to. Where the two
routes make different predictions, we find no evidence of herding. Researchers new to a topic propose methods more
often than incumbents do, the reverse of our registered prediction. At review, papers in crowded topics are accepted
neither more nor less often, whereas papers far from their authors' earlier work are accepted less often (a post hoc
finding, confirmed on held-out papers). The conformity visible at ICLR is anchored to researchers' own records rather
than driven by the crowd."

## Done when
Full build `pdflatex Thesis && bibtex Thesis && pdflatex Thesis && pdflatex Thesis`: 0 errors, 0 undefined
references/citations, 0 overfull boxes; no "??", "[?]"; no near-empty pages; render all pages (pdftoppm -r 50) and look
at them. grep the chapters for: "direction, not size", "detectabl", "goes with", "sits with", "package", "gated",
"frozen", "full-corpus", "the author", "AI", "Claude", "replicated" (as a verb) and confirm each remaining use is
intended.
