# Talk: "Riding the Wave?"

A talk of 15 minutes or less (strict limit) on the research-fashion study and its held-out replication, by Minghan Li
(supervisor: A/Prof Jianzhong Qi). Revised after the supervisor's feedback: two post hoc slides cut (far jumps, why areas
lose favour), "pre-registered" dropped from the titles, "topic map" defined, and every slide reduced to its key point.

Data credit (slide 6 and references): a provenance-preserving ICLR corpus built from our own dated official
OpenReview snapshots. Re² (Zhang et al., 2025), the Louis archive (`MlouisBE/iclr-rebuttal-analysis`) and Paper
Copilot (Yang, Wei & Pei, 2025) informed coverage and source audits but were not pooled into the analytical corpus.

| File | Contents |
|---|---|
| `slides.pdf` | The compiled deck, 17 pages: 16 slides and a references page |
| `slides.tex` | Beamer source (academic Madrid theme, pdflatex) |
| `script.md` | Spoken script with a per-slide timing table computed from word counts: about 1,120 words, 9:20 at 120 words a minute; the rounded-up table ends at 9:45. Allowing for spoken numbers and slide changes, expect about 10:00–10:30 (about 4–5 minutes of buffer under 15:00) |
| `qa.md` | Expected questions with short answers (including the held-out replication, the k sensitivity and the material of the cut slides), one-line summaries of the cited papers, a glossary (English and Chinese) and the key numbers |
| `shortlist.md` | Post hoc PH5 shortlist; its top section records each finding's status after the held-out run |
| `make_figures.py` | Slide figures and the three generated tables (`replication_summary.tex`, `replication_table.tex`, `pooled_table.tex`); reads only committed discovery outputs, outcome-free labels, the held-out run's estimates (`output_pooled/confirmation_run`) and the pooled re-run's estimates (`output_pooled/`, for `pooled_table.tex`) |
| `figs/` | Figure files. `finding*.png` come from the title analysis (Notion report); `keyword_year_heatmap.png` from the earlier keyword analysis; `area_ranking` and `fl_story` from post hoc PH4; `replication_summary.tex` (slide 13, generated) from the held-out run; `far_jump`, `premia_scatter` and the full `replication_table.tex` (generated) from PH5 and the held-out run, for questions; `pooled_table.tex` from the pooled re-run. Only `hindsight_diversity`, `lifecycle_flip`, `fm_trend`, `newcomers` and `replication_summary.tex` are in the deck |

Slides: 1 title, 2 outline, 3 motivation, 4 research questions, 5 related work, 6 data, 7–8 hindsight, 9 strategy,
10 RQ1, 11 RQ2, 12 RQ3, 13 held-out replication, 14 contributions, 15 limitations, 16 thank you, then references. No
appendix; detailed and pooled numbers are in RESULTS.md.

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
