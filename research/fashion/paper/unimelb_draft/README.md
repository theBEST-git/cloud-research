# Sections 1–6 draft in the University of Melbourne thesis template

Built from the Overleaf "University of Melbourne Thesis Template" (Ricardo Garcia-Rosas, CC BY 4.0;
https://www.overleaf.com/latex/templates/university-of-melbourne-thesis-template/ngytrznvqbcg), unmodified except:

- `Thesis.cls`: the logo line is commented out, as the template itself instructs for compliance; the title page prints
  `\degree{...}` instead of the fixed "degree of Doctor of Philosophy"; the abstract page says "Research report"
  instead of "Doctor of Philosophy".
- `Thesis.tex`: title, author, school, chapters 1–6, real abbreviation and symbol lists (no physical constants), no
  appendix; vector Latin Modern fonts (T1); `xr` reads `fullref.aux` so "Appendix X" mentions keep the full paper's
  letters.

Build: `pdflatex Thesis && bibtex Thesis && pdflatex Thesis && pdflatex Thesis`.
