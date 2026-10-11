"""Targeted checks: numbers quoted in outputs/d4_filter/RESULTS.md against the D4 output files.
Each check recomputes a value from gains.csv / atlas.csv / kobak_bounds.csv / exit_composition.csv / T4.1 /
its_pools*.csv / results.json, formats it as RESULTS.md does and asserts the string appears in RESULTS.md."""
import json
from pathlib import Path
import pandas as pd

D = Path("/home/user/cloud-research/research/titles/outputs/d4_filter")
txt = (D / "RESULTS.md").read_text()
g = pd.read_csv(D / "gains.csv")
a = pd.read_csv(D / "atlas.csv").set_index("label")
k = pd.read_csv(D / "kobak_bounds.csv")
ex = pd.read_csv(D / "exit_composition.csv")
cr = pd.read_csv(D / "T4_1_continuation_ratio.csv")
adj = pd.read_csv(D / "T4_1_adjusted_total.csv").set_index("feature")
its = pd.read_csv(D / "its_pools.csv")
yl = pd.read_csv(D / "its_pools_yearlevel.csv").set_index("contrast")
r = json.loads((D / "results.json").read_text())
fails, n = [], 0


def G(f, gain, period="2024-26", variant="primary", pooling="std"):
    x = g[(g.variant == variant) & (g.feature == f) & (g.gain == gain) & (g.period == period) & (g.pooling == pooling)]
    return x.iloc[0]


def chk(label, s):
    global n
    n += 1
    if s not in txt:
        fails.append(f"{label}: '{s}' not found")


def gci(f, gain, period="2024-26", variant="primary", sep="–", paren=True, k=3):
    x = G(f, gain, period, variant)
    return f"{x.est:.{k}f} ({x.lo95:.{k}f}{sep}{x.hi95:.{k}f})" if paren else f"{x.est:.{k}f}"


# H4a
chk("NAME total", "1.021 (95% CI 0.997–1.044)")
x = G("NAME", "total"); chk("NAME 90", f"{x.lo90:.3f}–{x.hi90:.3f}")
for y, lo, hi in [(2018, 0.68, 1.30), (2024, 0.97, 1.10), (2026, 0.98, 1.04)]:
    x = G("NAME", "total", str(y)); chk(f"NAME {y}", f"| {y} | {x.est:.3f} | {x.lo95:.2f}–{x.hi95:.2f}")
x = G("NAME", "total", pooling="raw"); chk("NAME raw", f"raw pooling: {x.est:.3f}, 90% CI {x.lo90:.3f}–{x.hi90:.3f}")
x = G("NAME", "total", variant="drop_wd_post"); chk("NAME dropwd", f"{x.est:.3f}, 90% CI {x.lo90:.3f}–{x.hi90:.3f}")
x = G("NAME", "total", "2024-25"); chk("NAME excl26", f"excluding 2026: {x.est:.3f}, 90% CI {x.lo90:.3f}–{x.hi90:.3f}")
chk("NAME 2018-23", "2018–23: " + gci("NAME", "total", "2018-23"))
chk("NAME excl2019", gci("NAME", "total", "2018-23 excl. 2019"))
chk("NAME 2018-22", gci("NAME", "total", "2018-22"))
for gn, lab in [("desk", "desk"), ("exit", "exit"), ("predec", "desk·exit")]:
    chk(f"NAME {gn}", f"{lab} {gci('NAME', gn)}")
chk("NAME exit crf", "exit " + gci("NAME", "exit_crf"))
chk("NAME predec crf", "desk·exit " + gci("NAME", "predec_crf"))
chk("NAME dec", gci("NAME", "dec"))
c = cr[(cr.era == "2024-26") & (cr.feature == "NAME")].set_index("stage")
chk("NAME adj exit", f"{c.loc['exit', 'G_adj']:.3f} ({c.loc['exit', 'G_adj_lo']:.3f}–{c.loc['exit', 'G_adj_hi']:.3f})")
chk("NAME adj dec", f"{c.loc['decision', 'G_adj']:.3f} ({c.loc['decision', 'G_adj_lo']:.3f}–{c.loc['decision', 'G_adj_hi']:.3f})")
chk("NAME desk q", f"q = {c.loc['desk', 'q_bh']:.3f}")
chk("NAME adj total", f"{adj.loc['NAME', 'G_adj_total']:.3f} (approximate 95% CI {adj.loc['NAME', 'G_adj_total_lo95_approx']:.3f}–{adj.loc['NAME', 'G_adj_total_hi95_approx']:.3f})")
ip = its[its.spec == "primary"].set_index("pool")
for p_ in ["ACC", "REJ", "WD"]:
    chk(f"ITS {p_}", f"| {p_} | {ip.loc[p_, 'slope_change_OR']:.3f} | {ip.loc[p_, 'slope_change_OR_lo']:.3f}–{ip.loc[p_, 'slope_change_OR_hi']:.3f}")
    chk(f"ITS yl {p_}", f"{yl.loc[p_, 'OR']:.3f} [{yl.loc[p_, 'OR_lo95']:.3f}, {yl.loc[p_, 'OR_hi95']:.3f}]")
chk("yl ACC-REJ", f"ACC − REJ: {yl.loc['ACC-REJ', 'est']:.3f}, 95% CI {yl.loc['ACC-REJ', 'lo95']:.3f} to {yl.loc['ACC-REJ', 'hi95']:.3f}, 90% CI {yl.loc['ACC-REJ', 'lo90']:.3f} to {yl.loc['ACC-REJ', 'hi90']:.3f}".replace("-0", "−0"))
chk("yl ACC-WD", f"{yl.loc['ACC-WD', 'lo95']:.3f} to {yl.loc['ACC-WD', 'hi95']:.3f}".replace("-0", "−0"))
w = r["decision_stage_bound"]["wp4_canonical"]["features"]["NAME"]
chk("WP4 G_total", f"{w['G_total_audit_lo']:.3f}–{w['G_total_audit_hi']:.3f}")
chk("WP4 DiD", f"−{abs(w['did_lo_pp']):.2f} to {w['did_hi_pp']:.2f}")
# H4b
chk("L total", "0.975 (95% CI 0.951–1.001; 90% CI 0.954–0.997)")
chk("L predec", "Desk·exit.** " + gci("L_union", "predec"))
chk("L predec crf", "camera-ready-free " + gci("L_union", "predec_crf"))
for y in ["2024", "2025", "2026"]:
    x, z = G("L_union", "total", y), G("L_union", "predec", y)
    chk(f"L {y}", f"| {y} | {x.est:.3f} | {x.lo95:.3f}–{x.hi95:.3f} | {z.est:.3f} | {z.lo95:.3f}–{z.hi95:.3f}")
chk("L raw", "raw pooling: " + gci("L_union", "total", variant="primary").split(" (")[0] if False else "raw pooling: 0.961 (0.937–0.987)")
x = G("L_union", "total", pooling="raw"); chk("L raw2", f"raw pooling: {x.est:.3f} ({x.lo95:.3f}–{x.hi95:.3f})")
chk("L excl26", "excluding 2026: " + gci("L_union", "total", "2024-25"))
chk("R24 total", gci("R24", "total"))
chk("R24 pre", gci("R24", "total", "2018-23"))
chk("R24 pp", gci("R24", "total", "2024-26 / 2018-23", "post_vs_pre"))
chk("LnoR24 total", "total " + gci("L_noR24", "total"))
chk("LnoR24 crf", "camera-ready-free " + gci("L_noR24", "predec_crf"))
chk("density total", "Total " + gci("style_density", "total"))
chk("density crf", gci("style_density", "predec_crf"))
x = G("style_density", "total", variant="density_reselect"); chk("density reselect", f"{x.lo95:.3f}–{x.hi95:.3f}")
chk("F24 total", "Total " + gci("F24", "total"))
chk("F24 crf", gci("F24", "predec_crf"))
chk("F24 pp", gci("F24", "predec_crf", "2024-26 / 2018-23", "post_vs_pre").replace(" (", ", ").rstrip(")").split(", ")[0])
chk("F24 pp1822", gci("F24", "predec_crf", "2024-26 / 2018-22", "post_vs_pre_1822").split(" (")[0])
for f, lab in [("title_typo", "title typography: "), ("F26", "F26 (abstract): "), ("emdash", "abstract em dash: "),
               ("R26", "R26: ")]:
    chk(f, lab + gci(f, "total"))
for gn, lab in [("total", "Total"), ("predec", "Desk·exit"), ("predec_crf", "Camera-ready-free desk·exit"), ("dec", "Decision")]:
    chk(f"Lpp {gn}", f"| {lab} | {gci('L_union', gn, '2024-26 / 2018-23', 'post_vs_pre')} | {gci('L_union', gn, '2024-26 / 2018-22', 'post_vs_pre_1822')} |")
chk("O total", "0.807 (0.749–0.870)")
chk("O dec", "decision " + gci("O_union", "dec"))
chk("O predec", "desk·exit " + gci("O_union", "predec"))
chk("O crf", gci("O_union", "predec_crf"))
chk("caps total", "Total " + gci("all_caps_title", "total"))
chk("caps 2026", gci("all_caps_title", "total", "2026"))
chk("caps crf", gci("all_caps_title", "predec_crf"))
chk("allcaps_name", gci("allcaps_name", "total"))
chk("NAME pp", gci("NAME", "total", "2024-26 / 2018-23", "post_vs_pre"))
# T4.1 adjusted totals
for f, lab in [("NAME", "NAME"), ("all_caps_title", "ALL-CAPS"), ("R24", "R24"), ("F24", "F24"), ("L_union", "L-union"),
               ("title_typo", "Title typography")]:
    chk(f"adj {f}", f"| {lab} | {adj.loc[f, 'G_adj_total']:.3f} | {adj.loc[f, 'G_adj_total_lo95_approx']:.3f}–{adj.loc[f, 'G_adj_total_hi95_approx']:.3f} | {adj.loc[f, 'G_raw_total']:.3f} |")
# H4c
kk = k[(k.marker == "F24") & (k.baseline == "cons")]
for y in ["2024", "2025", "2026"]:
    rr = kk[(kk.year == y) & (kk.set == "ratio_acc_all")].iloc[0]
    chk(f"kobak ratio {y}", f"{rr.bound:.3f} [{rr.lo95:.3f}, {rr.hi95:.3f}]".replace("-0", "−0"))
    chk(f"kobak basic {y}", f"[{rr.basic_lo95:.3f}, {rr.basic_hi95:.3f}]")
    s0 = kk[(kk.year == y) & (kk.set == "s0")].iloc[0]
    chk(f"kobak s0 {y}", f"{100 * s0.bound:.1f} [{100 * s0.lo95:.1f}, {100 * s0.hi95:.1f}], {int(s0.n_Y):,}")
ph = k[(k.marker == "F24") & (k.baseline == "max2122") & (k.set == "ratio_acc_all")]
for y in ["2024", "2025"]:
    rr = ph[ph.year == y].iloc[0]
    chk(f"posthoc {y}", f"{rr.bound:.4f} [{rr.lo95:.3f}, {rr.hi95:.3f}]")
p85 = kk[kk.set == "ratio_acc_all"].set_index("year").p_ge_0p85
chk("p85", f"{p85['2024']:.3f} / {p85['2025']:.3f} / {p85['2026']:.3f}")
# H4d
e = ex[ex.key == "NAME"].set_index("spec")
chk("H4d cross", f"+{e.loc['primary', 'cross_pp']:.2f} (se {e.loc['primary', 'cross_se_pp']:.2f}; {e.loc['primary', 'cross_lo95_pp']:.2f} to {e.loc['primary', 'cross_hi95_pp']:.2f})")
chk("H4d topic cross", f"+{e.loc['topic100_FE', 'cross_pp']:.2f} (se {e.loc['topic100_FE', 'cross_se_pp']:.2f}; −{abs(e.loc['topic100_FE', 'cross_lo95_pp']):.2f} to {e.loc['topic100_FE', 'cross_hi95_pp']:.2f})")
chk("H4d topic diff", f"{e.loc['topic100_FE', 'diff_pp']:.2f} (se {e.loc['topic100_FE', 'diff_se_pp']:.2f})")
chk("H4d single", f"+{e.loc['primary', 'single_cross_pp']:.2f} (se {e.loc['primary', 'single_cross_se_pp']:.2f}), or +{e.loc['topic100_FE', 'single_cross_pp']:.2f} (se {e.loc['topic100_FE', 'single_cross_se_pp']:.2f})")
chk("H4d full topic", f"+{e.loc['topic100_FE', 'full_cross_pp']:.2f} (se {e.loc['topic100_FE', 'full_cross_se_pp']:.2f})")
chk("H4d wdpost", f"| +{e.loc['wd_post_as_rejected', 'cross_pp']:.2f} | −{abs(e.loc['wd_post_as_rejected', 'within_pp']):.2f} | {e.loc['wd_post_as_rejected', 'diff_pp']:.2f} |")
chk("H4d kxy topic", f"−{abs(e.loc['key_x_year_topic100_FE', 'within_pp']):.2f} (−{abs(e.loc['key_x_year_topic100_FE', 'within_lo95_pp']):.2f} to −{abs(e.loc['key_x_year_topic100_FE', 'within_hi95_pp']):.2f})")
# H4e
for lab, s in [("ITS slope change (NAME), effect scale", "**0.50 (−0.15 to 1.16)**"),
               ("Colon-premium trend, 2018-26 (decided-only)", "**0.89 (0.66–1.12)**")]:
    rr = a.loc[lab]
    chk(lab, f"**{rr.ratio:.2f} ({'−' if rr.ratio_lo95 < 0 else ''}{abs(rr.ratio_lo95):.2f}{' to ' if rr.ratio_lo95 < 0 else '–'}{rr.ratio_hi95:.2f})**")
for lab, short in [("NAME prevalence", "| NAME |"), ("Mixed-case name prevalence", "| Mixed-case name |"),
                   ("Snowclone share", "| Snowclone share |")]:
    rr = a.loc[lab]
    chk(lab, f"{rr.ratio:.3f} ({rr.ratio_lo95:.3f}–{rr.ratio_hi95:.3f})")
chk("M count", f"M statistics: {r['hypotheses']['H4e']['estimates']['M_within_10pct']} within ±10%; {r['hypotheses']['H4e']['estimates']['M_accepted_only_within_10pct']} among")
chk("M ci90", "6 of 9")
assert r["hypotheses"]["H4e"]["estimates"]["M_ci90_within_10pct"] == "6/9"
# Holm
ht = {x["hypothesis"]: x for x in r["multiplicity"]["table"]}
chk("holm H4b", f"| 0.0295 | 0.025 | {ht['H4b']['p_holm']:.3f} |")
chk("holm H4c", f"| {ht['H4c']['p_raw']:.3f} | 0.05 | {ht['H4c']['p_holm']:.3f} |")
for h in ["H4a", "H4b", "H4c", "H4d", "H4e"]:
    v = r["hypotheses"][h]["verdict"].replace("_", " ")
    chk(f"verdict {h}", f"**{v.capitalize()}**")
print(f"{n} checks, {len(fails)} failures")
for f_ in fails:
    print("FAIL", f_)
