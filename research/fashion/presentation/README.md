# Talk: "Riding the Wave?"

A talk of 15 minutes or less (strict limit) on the research-fashion study and its held-out replication, with backup
slides.

| File | Contents |
|---|---|
| `slides.pdf` | The compiled deck, 19 pages: 18 slides and a references page |
| `slides.tex` | Beamer source (academic Madrid theme, pdflatex) |
| `script.md` | Spoken script with a per-slide timing table computed from word counts: about 1,530 words, 12:50 at 120 words a minute; the rounded-up table ends at 13:30. Allowing for spoken numbers and slide changes, expect about 13:50–14:10 (about 0:50–1:10 of buffer under 15:00) |
| `qa.md` | Expected questions with short answers (including the held-out replication), one-line summaries of the cited papers, a glossary (English and Chinese) and the key numbers |
| `shortlist.md` | Post hoc PH5 shortlist; its top section records each finding's status after the held-out run |
| `make_figures.py` | Slide figures and the two generated tables; reads only committed discovery outputs, outcome-free labels, the held-out run's estimates (`output_pooled/confirmation_run`) and the pooled re-run's estimates (`output_pooled/`, for A18) |
| `figs/` | Figure files. `finding*.png` come from the title analysis (Notion report); `keyword_year_heatmap.png` from the earlier keyword analysis; `area_ranking` and `fl_story` from post hoc PH4; `far_jump` (slide 13), `premia_scatter` and `replication_table.tex` (slide 16, generated) from PH5 and the held-out run; `pooled_table.tex` from the pooled re-run |

Slides: 1 title, 2 outline, 3 motivation, 4 hypotheses, 5 related work, 6 data, 7–8 hindsight, 9 strategy,
10 RQ1, 11 RQ2, 12 RQ3, 13 far jumps (post hoc, replicated), 14 why areas lose favour, 15 held-out replication
table, 16 contributions, 17 limitations, 18 thank you, then references. No appendix; detailed and pooled numbers are in
RESULTS.md.

Wording rules for the held-out results: the held-out papers are the released former confirmation split, which this
study had never analysed; the results are a pre-registered out-of-sample replication, not a certified untouched
holdout. PH5 findings are post hoc in discovery; their held-out tests were registered before the run. Associations
only.

Build (in the repository):

```text
python research/fashion/presentation/make_figures.py
cd research/fashion/presentation && pdflatex slides && pdflatex slides
```

Build from a copy outside the repository (leave `ICLR_CORPUS` unset so every read resolves to the committed discovery
outputs; `make_figures.py` refuses to run under the pooled corpus):

```text
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<repo>/research/fashion python make_figures.py
pdflatex -interaction=nonstopmode slides.tex && pdflatex -interaction=nonstopmode slides.tex
```
