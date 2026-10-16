# Talk: "Following the Fashion?"

A talk of 15 minutes or less on the research-fashion study, with backup slides.

| File | Contents |
|---|---|
| `slides.pdf` | The compiled deck: 12 main slides plus backups B1–B11 |
| `slides.tex` | Beamer source (metropolis theme, pdflatex) |
| `script.md` | Spoken script with per-slide timing, about 12.5 minutes |
| `qa.md` | Expected questions with short answers, a glossary (English and Chinese) and the key numbers |
| `make_figures.py` | Slide figures; reads only committed outputs and outcome-free labels |
| `figs/` | Figure files. `finding*.png` come from the title analysis (Notion report) |

Build:

```text
python research/fashion/presentation/make_figures.py
cd research/fashion/presentation && pdflatex slides && pdflatex slides
```
