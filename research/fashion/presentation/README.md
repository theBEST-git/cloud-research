# Talk: "Following the Fashion?"

A talk of 15 minutes or less on the research-fashion study, with backup slides.

| File | Contents |
|---|---|
| `slides.pdf` | The compiled deck: 18 main slides, appendix A1–A12 and references |
| `slides.tex` | Beamer source (academic Madrid theme, pdflatex) |
| `script.md` | Spoken script with per-slide timing, about 13 minutes |
| `qa.md` | Expected questions with short answers, one-line summaries of the cited papers, a glossary (English and Chinese) and the key numbers |
| `make_figures.py` | Slide figures; reads only committed outputs and outcome-free labels |
| `figs/` | Figure files. `finding*.png` come from the title analysis (Notion report); `keyword_year_heatmap.png` comes from the earlier keyword analysis; `area_ranking` and `fl_story` come from post hoc PH4 |

Build:

```text
python research/fashion/presentation/make_figures.py
cd research/fashion/presentation && pdflatex slides && pdflatex slides
```
