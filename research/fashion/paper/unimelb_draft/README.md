# Sections 1–6 draft in the University of Melbourne thesis template

Built from the Overleaf "University of Melbourne Thesis Template" (Ricardo Garcia-Rosas, CC BY 4.0;
https://www.overleaf.com/latex/templates/university-of-melbourne-thesis-template/ngytrznvqbcg), unmodified except:

- `Thesis.cls`: the logo line is commented out, as the template itself instructs for compliance; the title page prints
  `\degree{...}` instead of the fixed "degree of Doctor of Philosophy"; the abstract page says "Science Research Project (SCIE30001)"
  instead of "Doctor of Philosophy".
- `SCIE30001.tex`: title, author, school, chapters 1–6, real abbreviation and symbol lists (no physical constants), no
  appendix (pointers to the full paper's appendix are removed); vector Latin Modern fonts (T1).

Build (BibTeX is required, or citations print as [?]): `pdflatex SCIE30001 && bibtex SCIE30001 && pdflatex SCIE30001 && pdflatex SCIE30001`. On Overleaf, upload the whole folder; it runs BibTeX automatically.
