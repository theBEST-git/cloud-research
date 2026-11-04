# Herded or Anchored? Testing Conformity in Machine Learning on a Decade of ICLR Submissions

Paper draft, written in the ACL ARR template.

| File | Contents |
|---|---|
| `herded_or_anchored.tex` | Main paper (preprint mode, with author block and acknowledgments). |
| `appendix.tex` | Appendices A–H, pulled in by the main file. |
| `herded_or_anchored_main.pdf` | Short version: pages 1–11 of the full PDF (main text, Limitations, Ethics, Acknowledgments, References; no appendix). |
| `references.bib` | Bibliography: 84 entries, each checked against its source. |
| `make_figures.py` | Draws `figs/fig1`–`fig4` (main text) and `figs/figA_*` (appendix). It reads only outcome-free labels and committed outputs. |
| `analysis/novelty_newcomer.py` | Content-distance analysis: are newcomer papers farther from earlier ICLR work? Results are in `../output/paper_novelty/`. |
| `analysis/newcomer_profiles.py` | First-time teams vs returning topic newcomers vs incumbents (outcome-free). Results are in `../output/paper_profiles/`. |
| `acl.sty`, `acl_natbib.bst` | ACL style files. |

To build:

```bash
python make_figures.py
pdflatex herded_or_anchored && bibtex herded_or_anchored
pdflatex herded_or_anchored && pdflatex herded_or_anchored
```

Every number in the paper traces back to `../RESULTS.md` and to the committed
outputs under `../output/` and `../output_pooled/`. Evidence tiers (A–E) follow
the definitions in Section 1 of the paper.
