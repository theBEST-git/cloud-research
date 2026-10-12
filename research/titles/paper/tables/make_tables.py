"""Derive paper-layout versions of the generated tables in ../../outputs/tables/.

The numbers are not touched: only the float wrappers change.
- table1_hypotheses: table* -> longtable (it is taller than one page).
- table2-4: table* -> table inside a landscape page, tabular scaled to the line width if needed.

Run from research/titles/paper:  python tables/make_tables.py
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent.parent / "outputs" / "tables"


def parts(tex):
    cap = re.search(r"\\caption\{(.*?)\}\n\\label\{(.*?)\}", tex, re.S)
    tab = re.search(r"\\begin\{tabular\}\{(.*?)\}\n(.*?)\\end\{tabular\}", tex, re.S)
    note = re.search(r"\\parbox\{\\linewidth\}\{(.*)\}\n\\end\{table\*\}", tex, re.S)
    return cap.group(1), cap.group(2), tab.group(1), tab.group(2), note.group(1) if note else ""


# Pilot values quoted in docs/PLAN.md (pilot analyses on the same discovery rows, run before the plan was locked).
# Added in review round 1 (R5/M6) so that readers can see which predictions were informed by pilots.
PILOT = {
    "H1a": "OR 1.28/yr (colon titles, not NAME)",
    "H1b": "29\\% fixed; 42\\% rolling; 45\\% unmasked bge",
    "H1c": "1.7 $\\rightarrow$ 3.9 pp/yr (ratio 2.3)",
    "H1d": "26\\% (size $\\times$ LLM topic)",
    "H1e": "colon adjOR 1.24",
    "H2a": "last $\\approx$ 1.00; any 0.83",
    "H2b": "first 0.58 vs last 1.00",
    "H2c": "0.60 (rolling)",
    "H2d": "slope 0.97",
    "H2e": "--",
    "S2.1": "0.000 (se 0.025; 28/28; n = 297)",
    "S2.2": "past .045 vs future .118",
    "H3a": "2.69 [1.80, 4.01]; controls 0.87",
    "H3b": "R24 down 12/16; R26 up 16/16",
    "H3c": "1.29 vs 0.83",
    "H3d": "$\\approx$ 2.7 vs $\\approx$ 1.24",
    "H3e": "$\\approx$ 0.55 (2024)",
    "H4a": "1.01--1.04 (2024--26)",
    "H4b": "typography 0.79; ALL-CAPS 0.37",
    "H4c": "12.8/8.7/3.0 vs 15.8/12.0/5.8 pp",
    "H4d": "+3.6 vs $-$1.4 pp",
    "H4e": "--",
    "Gate": "--",
}
NOTE_ADD = (" Pilot: value quoted in the locked plan from pilot analyses of the same discovery rows, run before the "
            "plan was locked; predictions and thresholds were informed by these pilots. Holm p tests the "
            "pre-registered statistic; the verdict also weighs the identification checks added in the audits, so a "
            "small Holm p can coexist with `not identified' (e.g.\\ H2a).")


def add_pilot(spec, body, note):
    spec = "l p{2.5cm} p{2.2cm} p{3.9cm} p{3.2cm} r"
    out = []
    for line in body.split("\n"):
        m = re.match(r"^(\S+) & (.*?) & (.*)$", line)
        if line.startswith("\\multicolumn{5}"):
            line = line.replace("\\multicolumn{5}", "\\multicolumn{6}", 1)
        elif line.startswith("ID & Prediction"):
            line = line.replace("ID & Prediction &", "ID & Prediction & Pilot (plan) &", 1)
        elif m and m.group(1) in PILOT:
            line = f"{m.group(1)} & {m.group(2)} & {PILOT[m.group(1)]} & {m.group(3)}"
        out.append(line)
    body = "\n".join(out)
    # wording only (review N2/M2): the 2024 break ratio is 0.50 [-0.15, 1.16]; "halved" overstates it
    body = body.replace("2024 break halved", "2024 break about half as large (CI $-$0.15 to 1.16)")
    return spec, body, note + NOTE_ADD


def longtable(name):
    tex = (SRC / f"{name}.tex").read_text()
    caption, label, spec, body, note = parts(tex)
    if name == "table1_hypotheses":
        spec, body, note = add_pilot(spec, body, note)
        caption = caption.replace("Pre-registered hypotheses", "Pre-specified hypotheses (locked plan)")
        note = note.replace("are pre-registered in outputs/prereg/", "are frozen in a hashed bundle (outputs/prereg/)")
    body = body.replace("\\toprule\n", "", 1)
    header, rest = body.split("\\midrule\n", 1)
    rest = rest.replace("\\bottomrule\n", "")
    ncol = len(re.findall(r"p\{[^}]*\}|[lrc]", spec))
    out = [
        f"% derived from outputs/tables/{name}.tex by paper/tables/make_tables.py (numbers unchanged)",
        "{\\scriptsize",
        f"\\begin{{longtable}}{{{spec}}}",
        f"\\caption{{{caption}}}\\label{{{label}}}\\\\",
        "\\toprule", header.rstrip(), "\\midrule", "\\endfirsthead",
        f"\\multicolumn{{{ncol}}}{{l}}{{\\textit{{Table \\ref{{{label}}}, continued}}}}\\\\",
        "\\toprule", header.rstrip(), "\\midrule", "\\endhead",
        "\\bottomrule", "\\endfoot",
        rest.rstrip(),
        "\\end{longtable}",
        f"\\par\\noindent {note}\\par",
        "}",
    ]
    (HERE / f"{name}.tex").write_text("\n".join(out) + "\n")


XREF = [("Table 1", "Table~\\ref{tab:hypotheses}"), ("Fig. 5", "Figure~\\ref{fig:nt-gains}"),
        ("Fig. 6b", "Figure~\\ref{fig:nt-bias}b")]


def landscape(name):
    tex = (SRC / f"{name}.tex").read_text()
    for a, b in XREF:  # output-table numbering -> this paper's labels
        tex = tex.replace(a, b)
    caption, label, spec, body, note = parts(tex)
    out = [
        f"% derived from outputs/tables/{name}.tex by paper/tables/make_tables.py (numbers unchanged)",
        "\\begin{landscape}",
        "\\begin{table}[p]",
        "\\centering",
        "\\scriptsize",
        f"\\caption{{{caption}}}",
        f"\\label{{{label}}}",
        "\\begin{adjustbox}{max width=\\linewidth}",
        f"\\begin{{tabular}}{{{spec}}}",
        body.rstrip(),
        "\\end{tabular}",
        "\\end{adjustbox}",
        "\\par\\smallskip",
        f"\\parbox{{\\linewidth}}{{{note}}}",
        "\\end{table}",
        "\\end{landscape}",
    ]
    (HERE / f"{name}.tex").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    longtable("table1_hypotheses")
    for n in ("table2_acceleration", "table3_content_bracket", "table4_filter_audit"):
        landscape(n)
    print("wrote", sorted(p.name for p in HERE.glob("table*.tex")))
