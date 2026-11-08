# Handoff: paper and SCIE30001 report (state on 2026-11-07)

Read this first when you resume. It is the context from the cloud session that produced the paper and report.
Branch: `claude/clever-edison-oe9pzv` (all work is pushed there; no PR exists).

## 1. What the project is

A study of conformity at ICLR during the foundation-model (FM) wave, by Minghan Li (supervisor: A/Prof Jianzhong Qi,
University of Melbourne). It is assessed as **Science Research Project (SCIE30001)**.

- Question: does ML research "herd" (imitation: follow what others do now), or does it stay anchored to a record
  (continuity: the team's own earlier work)? Tested at three levels: the field, entry to a topic, and the
  accept/reject decision ("the gate").
- Data: 43,480 discovery ICLR submissions 2017–2026 (rejected and withdrawn included) plus 11,099 held-out papers.
  Hypotheses registered in `research/fashion/PREREGISTRATION.md` before outcomes were read; every number is in
  `research/fashion/RESULTS.md` and the committed outputs under `research/fashion/output*/`.
- Main findings:
  - Field: keyword waves are real, but the count of "emerging" topics ranges from 8 to 29 depending on which years the
    topic map is fitted on; the shift to FMs fits both routes.
  - Entry: newcomers to a topic write more method papers (+3.7 pp, replicated; the reverse of the registered herding
    prediction). This holds for researchers with ICLR work elsewhere and predates the FM wave. Measurement papers sit
    with incumbents and larger teams in 2024–2026.
  - Gate: no detectable crowding premium or penalty; branded titles show a small premium that the held-out test could
    not confirm. Papers far from the team's own earlier work are accepted less often (far jump −5.44 pp discovery,
    −6.09 held-out; held-out supported). Status and expertise could explain the record-side results equally well.

## 2. Files

| Path | What |
|---|---|
| `research/fashion/paper/unimelb_draft/SCIE30001.tex` / `.pdf` | **The current deliverable**: report for SCIE30001, Chapters 1–6, University of Melbourne thesis template (Overleaf template by R. Garcia-Rosas; copy verified identical). Chapters in `Chapters/`, front matter in `Preamble/`, bibliography `Bibliography.bib`. Build: `pdflatex SCIE30001 && bibtex SCIE30001 && pdflatex SCIE30001 && pdflatex SCIE30001` (BibTeX is required). |
| `research/fashion/paper/feedback/SCIE30001_draft1_supervisor_comments.pdf` | Supervisor's annotated copy of draft 1 (see section 4). |
| `research/fashion/paper/herded_or_anchored.tex` / `.pdf` + `appendix.tex` | Full ACL-template paper (8-page main text + appendices A–H). `_main.pdf` = no appendix; `_sec1-6.pdf` = Sections 1–6 only. |
| `research/fashion/paper/make_figures.py`, `figs/` | All figures (read only outcome-free labels and committed outputs). |
| `research/fashion/paper/analysis/` | Paper-only analyses: `novelty_newcomer.py`, `newcomer_profiles.py`. |
| `research/fashion/paper/notes/literature/` | Literature sweep notes and verified `.bib` files (`landscape.md` is the synthesis; `references_merged.bib` the verified master list). |
| `research/fashion/paper/notes/story/` | Story design: four candidate storylines (`story_P1–P4.md`), judge reviews, the chosen `blueprint.md`, and evidence dossiers. |
| `research/fashion/paper/notes/revision_specs/` | The decided revision specs and fix lists applied so far (useful as a record of decisions). |
| `research/fashion/ph5_titles.py` | PH7 branded-title test (declared 2026-11-04, run once; outputs `output_pooled/posthoc/ph5_titles/`). |

## 3. Standing constraints (from the author)

- Associations only; no causal or advice language. Every finding carries an evidence label (replicated / held-out
  supported / exploratory; inconclusive / uninformative for registered tests without a verdict).
- Keep the phrase "a pre-registered out-of-sample replication, not a certified untouched holdout" for the held-out set.
- Data provenance: own dated OpenReview acquisitions; Re² and other datasets were audited, not pooled.
- Never print or export author names or IDs. Never read outcome/decision columns outside a gated `posthoc.py` run
  (new acceptance analyses must be declared in PREREGISTRATION.md and committed before they are run).
- In the SCIE30001 report: do not mention AI/LLM assistance for writing or coding (the author's instruction; the LLM
  that labels contribution types is part of the method and stays). Note: the university expects generative-AI use to
  be acknowledged; this was flagged to the author, who decides.
- Front matter: author Minghan Li; "A report submitted for Science Research Project (SCIE30001)"; supervisor
  A/Prof Jianzhong Qi; School of Computing and Information Systems, Faculty of Engineering and IT (unconfirmed).

## 4. Supervisor feedback on draft 1 (2026-11-06) — the next task

Email: "Good work as a first draft, but still a long way to go. Overall, it reads more like a technical blog than a
research report. Please try to find a few MPhil/PhD thesis and study how they organise the content flow, or even just
the ICLR papers that you've been playing with."

Annotations (page numbers of the annotated PDF):
1. p5: Acknowledgements struck out.
2. p13: "Here two routes to conformity diverge." — incomplete sentence.
3. p13: "Here, list the research questions (your three hypotheses?) this report aims to address, then discuss your
   approach to address the questions, not just the findings."
4. p14 (prior-work paragraph): "should be moved earlier, before your approach and findings, to set the technical
   context of what's missing in the literature, which explains why you want to study this problem. You could widen the
   discussion to cover 'research about research' beyond ICLR, e.g., herding in general."
5. p15 (Chapter 2 "Two Routes to Conformity"): "These are your hypotheses. Should survey papers that work on related
   problems, not about hypotheses." And: "The literature review should cover 'research about research' more broadly.
   ... it reads more like a technical blog rather than a research project report. Should read a few MPhil/PhD theses
   and see how they organise their content structure."
6. p17: "decided" struck out twice; "Design" → "Method"; "held-out set (11,099" → "how did we select this set?";
   "blind second labelling pass" → "who did this labeling?".
7. p18: "small" → "how small?"; "we" (hand check) → "who? just you, or is there another person?";
   "zero-shot LLM labels is often only fair [40]" → "what do you mean?".
8. p22: "were released to us" → "just say 'were examined/tested'". Plus: "Overall I found some of the wordings quite
   awkward ... Not sure if this was the AI generation effect. Can you go through the whole thesis, and rewrite it in
   your own plain words?"
9. p30: "Chapters 4–6 can be merged into one Chapter named Results. Add a new chapter on Conclusions and Future work.
   In conclusions, list all key findings of the study, which are not all mixed up in the results chapters."

Planned structure: 1 Introduction (motivation → gap in the literature → research questions RQ1–RQ3 → approach →
contributions → outline); 2 Literature Review (research about research broadly: herding/fashions in science, science
of science on topic choice and novelty, peer-review studies, ML/NLP meta-research, topic-model histories); 3 Method
(data, held-out selection, measures, labelling, protocol); 4 Results (field, entry, gate); 5 Conclusions and Future
Work (all key findings listed; limitations; future work). Discussion and the appendix were withheld from draft 1.

Author's answers (2026-11-08):
- Hand check of LLM labels: the author alone checked 100 labels. About 80 were clearly right. The other ~20 were
  boundary cases the author could not decide either, so the LLM label was kept. Report these ~20 as undecidable, not
  as agreement. No second human coder, so there is no human inter-annotator agreement; list this as a limitation.
- Held-out set: selected randomly (about 20% of all submissions). Still to confirm: was the draw random at paper
  level, and who made it (the data source or the author)?

Decided: the author rewrites the prose in their own words at the end; Claude does structure, literature, factual
fixes. The "blind second labelling pass" is described as a second, independent run of the same LLM (κ = 0.93).

## 4a. Revision status (2026-11-08)

Draft 2 restructure is done in `unimelb_draft/` and builds cleanly (59 pages):
1 Introduction (motivation, gap, RQ1–RQ3, approach, contributions, outline); 2 Literature Review (seven areas of
research about research, only verified references from `notes/literature/`); 3 Method (hypotheses with the
predictions table and a registered-hypotheses table, data with held-out selection and a papers-by-year table,
measures incl. the hand check, protocol, design weaknesses); 4 Results (old Chapters 4–6 merged, plus a verdict table
for every registered hypothesis); 5 Conclusions and Future Work (all prose, by the author's request: summary of
key findings per RQ, discussion against the literature with a results-by-route table, limitations, future work,
closing remarks). Lists were turned into prose to avoid a tech-report feel; only the RQ list in Chapter 1 remains. Acknowledgements removed. All 16 supervisor annotations addressed.

Still open:
- Held-out selection: the report now says the held-out fifth was "selected at random" (author's answer), but the
  repo (`appendix.tex`, Data Provenance) says the source did not document how papers were assigned. The author should
  confirm who made the random draw and at what level, or soften the sentence in Chapter 3, Section 3.2.
- The author's own rewrite of the prose (supervisor comment 8).
- The labelling model is named in Chapter 3 (Claude Haiku), as method disclosure; the author may decide otherwise.

## 5. Environment notes

- Python deps: `pip install -r research/fashion/requirements.txt` (numpy, pandas, scipy, matplotlib pinned).
- LaTeX: pdflatex + bibtex; the report uses `lmodern` + T1.
- Figures: `python research/fashion/paper/make_figures.py` (run with `ICLR_CORPUS` unset).
