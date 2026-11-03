# Herded or Anchored? Conformity at ICLR during the Foundation-Model Wave

Paper draft, written in the ACL ARR template.

| File | Contents |
|---|---|
| `herded_or_anchored.tex` | Main paper. Uses `[preprint]`; switch to `[review]` for an anonymous ARR submission. |
| `appendix.tex` | Appendices A–H, pulled in by the main file. |
| `references.bib` | Bibliography: 78 entries, each checked against its source. |
| `make_figures.py` | Draws `figs/fig1`–`fig4b`. It reads only outcome-free labels and committed outputs. |
| `analysis/novelty_newcomer.py` | Content-distance analysis: are newcomer papers farther from earlier ICLR work? Results are in `../output/paper_novelty/`. |
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
