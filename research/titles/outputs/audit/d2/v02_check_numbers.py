"""Fixer check (D2 audit): targeted consistency check of RESULTS.md against the D2 output files.

Each check formats a value (or CI) from an output file exactly as RESULTS.md writes it and asserts that the string
occurs in RESULTS.md. A global "does this number occur anywhere" check is useless for 2-decimal numbers (the
pre-fix RESULTS.md with stale CIs passed it), so the checks are explicit. Prints every failing check.

Run: cd research/titles/src && PYTHONPATH=. /home/user/venv/bin/python ../outputs/audit/d2/v02_check_numbers.py
"""
import json
import sys
from pathlib import Path

import pandas as pd

D = Path(__file__).resolve().parents[2] / "d2_carriers"
R = (Path(sys.argv[1]) if len(sys.argv) > 1 else D / "RESULTS.md").read_text()
J = lambda f: json.loads((D / f).read_text())
ss, mk, idr, res, sp = J("shiftshare_results.json"), J("markers_results.json"), J("ident_results.json"), \
    J("results.json"), J("support_results.json")
t21 = pd.read_csv(D / "T2_1_decomposition.csv")
tw = pd.read_csv(D / "T2_1b_twoway_se.csv").set_index("stat")
fe = pd.read_csv(D / "T2_2_author_fe.csv")
ap = pd.read_csv(D / "T2_2b_allprior.csv")
nf = pd.read_csv(D / "T2_4_newcomer_free.csv")
s21 = pd.read_csv(D / "s2_1_resubmission.csv")
s22 = pd.read_csv(D / "s2_2_future_tie.csv")
gap = pd.read_csv(D / "h2b_first_position.csv")
prem = pd.read_csv(D / "h2b_newcomer_premium_by_year.csv")
team = pd.read_csv(D / "team_type_shiftshare.csv")
H = {h["id"]: h for h in res["hypotheses"]}

fails, n = [], 0


def m(x, k=3):
    s = f"{x:.{k}f}"
    return s.replace("-", "−")


def c(est, lo, hi, k=3, f=1.0, sign=False):
    e = f"{est * f:+.{k}f}" if sign else f"{est * f:.{k}f}"
    return f"{e} [{lo * f:.{k}f}, {hi * f:.{k}f}]".replace("-", "−")


def chk(s, label):
    global n
    n += 1
    if s not in R:
        fails.append((label, s))


def T(spec, o="name_primary"):
    return t21[(t21.spec == spec) & (t21.outcome == o)].iloc[0]


# --- T2.1 and robustness table ---
for part in ("last", "any", "first"):
    r = T(f"main|{part}|paper")
    chk(c(r.rho, r.rho_lo, r.rho_hi), f"rho {part}")
    w = tw.loc[f"rho_{part}"]
    chk(f"[{m(w.cgm_lo)}, {m(w.cgm_hi)}]", f"two-way {part}")
    chk(c(r.rho_ipw, r.rho_ipw_lo, r.rho_ipw_hi), f"ipw {part}")
    chk(f"{r.bound_a:.2f} [{r.bound_a_lo:.2f}, {r.bound_a_hi:.2f}], {r.bound_b:.2f}", f"scenario {part}")
    chk(f"{r.kit_within_share:.2f} / {r.kit_repl_share:.2f} / {r.kit_shift_share:.2f}", f"kitagawa {part}")
    chk(f"{r.rho_noR:.3f} [{r.rho_noR_lo:.3f}, {r.rho_noR_hi:.3f}]", f"rho_noR {part}")
for tag in ["NA_pool", "no_email_papers", "non_llm", "excl2026", "L2025_only", "L2026_only", "2023to2026",
            "trim_top1pct", "partition_specific_stayers", "alias_restricted", "alias_collapse"]:
    for part in ("last", "any", "first"):
        r = T(f"{tag}|{part}|paper")
        chk(c(r.rho, r.rho_lo, r.rho_hi), f"rho {tag} {part}")
for part in ("last", "any", "first"):
    r = T(f"adj_topic100|{part}|paper", "name_adj_topic"); chk(c(r.rho, r.rho_lo, r.rho_hi), f"adj topic {part}")
    r = T(f"adj_size_bin|{part}|paper", "name_adj_size"); chk(c(r.rho, r.rho_lo, r.rho_hi), f"adj size {part}")
    r = T(f"main|{part}|author"); chk(c(r.rho, r.rho_lo, r.rho_hi), f"author {part}")
    for o in ("name_strict", "name_loose", "name_compound"):
        rr = ss["name_defs"][o][part]; chk(c(rr["est"], rr["lo"], rr["hi"]), f"{o} {part}")
chk(f"0.028, 0.024 and 0.054", "cgm se list")
for st, lab in [("rho_last", "last"), ("rho_any", "any"), ("rho_first", "first")]:
    pass
chk(f"{tw.loc['rho_last','se_cgm']:.3f}, {tw.loc['rho_any','se_cgm']:.3f} and {tw.loc['rho_first','se_cgm']:.3f}", "cgm ses")
chk(f"{tw.loc['rho_last','se_key']:.3f}, {tw.loc['rho_any','se_key']:.3f} and {tw.loc['rho_first','se_key']:.3f}", "key ses")
chk(f"{tw.loc['rho_last','se_pigeonhole']:.3f}, {tw.loc['rho_any','se_pigeonhole']:.3f} and {tw.loc['rho_first','se_pigeonhole']:.3f}", "pig ses")
chk(f"[{m(tw.loc['rho_last','pig_lo'])}, {m(tw.loc['rho_last','pig_hi'])}]", "pig last")
fl = tw.loc["first_minus_last"]
chk(f"[{m(fl.cgm_lo)}, {m(fl.cgm_hi)}]", "two-way first-last"); chk(f"[{m(fl.pig_lo)}, {m(fl.pig_hi)}]", "pig first-last")
# --- null table ---
nu = ss["null_rho"]["main"]
for part in ("last", "any"):
    chk(f"{nu[part]['null_Nfirst']['est']:.3f} | {nu[part]['null_NRfirst']['est']:.3f} | {nu[part]['null_anyN']['est']:.3f}", f"null {part}")
    o = ss["obs_minus_null"][f"main|{part}|null_Nfirst"]
    chk(c(o["est"], o["lo"], o["hi"], sign=True), f"obs-null {part}")
    w = tw.loc[f"rho_minus_null_{part}"]; chk(f"two-way [{m(w.cgm_lo)}, {m(w.cgm_hi)}]", f"obs-null 2way {part}")
chk(f"{nu['first']['null_anyN']['est']:.3f}", "null first anyN")
o = ss["obs_minus_null"]["main|last|null_NRfirst"]; chk(c(o["est"], o["lo"], o["hi"], sign=True), "obs-null NR last")
o = ss["obs_minus_null"]["main|any|null_NRfirst"]; chk(c(o["est"], o["lo"], o["hi"], sign=False), "obs-null NR any")
o = ss["obs_minus_null"]["NA_pool|last|null_Nfirst"]; chk(c(o["est"], o["lo"], o["hi"], sign=True), "NA obs-null last")
o = ss["obs_minus_null"]["NA_pool|any|null_NRfirst"]; chk(c(o["est"], o["lo"], o["hi"], sign=True), "NA obs-null any")
# --- newcomer-free table ---
lab = {"all-stayer teams (every declared position a stayer key)": None,
       "fixed 2021-22-base all-prior teams, E = 2023": None, "last=S; L papers with no entrant or returner key": None,
       "last=S; L papers with no entrant key": None, "papers with a repeated stayer dyad; L without entrant key": None,
       "2-year-lookback all-prior teams, E = 2023": None, "first=S and last=S (distinct keys)": None,
       "last=S; lag-1 all-prior team in both windows (symmetric)": None, "lag-1 all-prior teams": None,
       "last=S (rho_last numerator)": None, "last=S; L papers with an entrant first author": None}
for k in lab:
    r = nf[(nf["sample"] == "all") & (nf.contrast == k)].iloc[0]
    chk(f"{int(r.n_E):,} → {int(r.n_L):,} | {f'{r.P_E:.3f}'[1:]} → {f'{r.P_L:.3f}'[1:]} | "
        f"{c(r.ratio, r.ratio_lo, r.ratio_hi, 2)} | {c(r.ctl_ratio, r.ctl_ratio_lo, r.ctl_ratio_hi, 2)}", f"nf {k}")
for k, txt in [("all-stayer teams (every declared position a stayer key)", "all-stayer teams: "),
               ("last=S; L papers with no entrant key", "last = S with no entrant key: "),
               ("lag-1 all-prior teams", "lag-1 all-prior teams: ")]:
    r = nf[(nf["sample"] == "NA_pool") & (nf.contrast == k)].iloc[0]
    chk(txt + c(r.ratio, r.ratio_lo, r.ratio_hi, 2), f"nf NA {k}")
for k in ["rolling all-prior; L teams containing an entrant key", "rolling all-prior; L teams with a returner, no entrant",
          "rolling all-prior; L teams of stayer keys only"]:
    r = nf[(nf["sample"] == "all") & (nf.contrast == k)].iloc[0]
    chk(c(r.ratio, r.ratio_lo, r.ratio_hi, 2) + " ×", f"rolling split {k}")
# --- team types ---
for d_ in ("roll", "fixed", "lag1"):
    for cells in ("type", "type_x_size"):
        t = team[(team.definition == d_) & (team.window == "main") & (team.cells == cells) & (team.stat == "within_share")].iloc[0]
        chk(c(t.est, t.lo, t.hi), f"team {d_} {cells}")
# --- H2b ---
for k, v in H["H2b"]["estimate"]["first_minus_last_other_variants"].items():
    if k in ("alias_collapse_extreme_bound",):
        chk(c(v["est"], v["lo"], v["hi"]), k); continue
    chk(c(v["est"], v["lo"], v["hi"]), f"h2b variant {k}")
for k in ("first_minus_last", "first_minus_last_author_wt", "first_minus_last_NA_pool", "first_minus_last_excl2026"):
    v = H["H2b"]["estimate"][k]; chk(c(v["est"], v["lo"], v["hi"]), k)
g0 = gap.set_index("spec")
r = gap.iloc[0]; chk(f"{r.est * 100:.1f} pp [{r.lo * 100:.1f}, {r.hi * 100:.1f}]", "gap raw")
chk(f"{gap.iloc[1].est * 100:.1f} pp", "gap size topic"); chk(f"{gap.iloc[2].est * 100:.1f} pp", "gap lastkey")
r = gap.iloc[3]; chk(f"{r.est * 100:.1f} pp [{r.lo * 100:.1f}, {r.hi * 100:.1f}]", "gap lk size topic")
r = gap.iloc[4]; chk(f"{r.est * 100:+.1f} pp [{r.lo * 100:.1f}, {r.hi * 100:.1f}]", "premium change")
for _, r in prem.iterrows():
    chk(f"| {int(r.year)} | {m(r.premium_raw * 100, 1) if r.premium_raw < 0 else '+' + format(r.premium_raw * 100, '.1f')} pp | "
        f"{m(r.premium_lastkey_size_topic * 100, 1) if r.premium_lastkey_size_topic < 0 else '+' + format(r.premium_lastkey_size_topic * 100, '.1f')} pp |",
        f"premium {r.year}")
sy = idr["h2b_first_position"]["symmetric_prior_first"]
chk(f"{sy['ratio_prior']:.2f} [{sy['ratio_prior_lo']:.2f}, {sy['ratio_prior_hi']:.2f}]", "sym prior first")
chk(f"{sy['newcomer_share_E']:.3f}"[1:] + " → " + f"{sy['newcomer_share_L']:.3f}"[1:], "newcomer share")
# --- H2c ---
for _, r in fe.iterrows():
    chk(f"{r.change_EtoL_at_share_new0 * 100:.2f} pp | {r.ratio_to_pop:.2f} [{r.ratio_lo:.2f}, {r.ratio_hi:.2f}]", f"h2c {r.model}")
f0 = fe.iloc[0]
chk(f"+{f0.change_EtoL_at_share_new0 * 100:.2f} pp [{f0.lo_change * 100:.2f}, {f0.hi_change * 100:.2f}] (two-way se {f0.se_change * 100:.2f})", "h2c primary")
chk(f"[{f0.ratio_lo_popunc:.2f}, {f0.ratio_hi_popunc:.2f}]", "h2c popunc")
chk(f"p = {f0.p_ratio_ge_0_5:.3f}", "h2c p pred"); chk(f"p = {f0.p_ratio_le_0_3:.2f}", "h2c p fals")
chk(f"+{f0.b_post_x_share_new * 100:.1f} pp (se {f0.se_post_x_share_new * 100:.1f})", "post sn roll")
fl1 = fe.iloc[1]; chk(f"+{fl1.b_post_x_share_new * 100:.1f} pp (se {fl1.se_post_x_share_new * 100:.1f})", "post sn lag1")
chk(f"{f0.se_change_keyonly:.4f}", "key-only se")
chk(", ".join(f"{f0[f'mean_share_new_{y}']:.2f}" for y in range(2022, 2027)), "share_new roll")
chk(", ".join(f"{fl1[f'mean_share_new_{y}']:.2f}" for y in range(2022, 2027)), "share_new lag1")
for (d_, w, smp) in [("roll", "main", "all"), ("lag1", "main", "all"), ("sym2", "E2023", "all"), ("roll", "E2023", "all"),
                     ("fixed", "E2023", "all"), ("roll", "2023to2026", "all"), ("roll", "main", "NA_pool")]:
    r = ap[(ap.definition == d_) & (ap.window == w) & (ap["sample"] == smp)].iloc[0]
    s = (f"{r.allprior_P_E:.3f} → {r.allprior_P_L:.3f} | {r.n_allprior_E:,} → {r.n_allprior_L:,} | "
         f"{r.allprior_change * 100:+.1f} pp [{r.allprior_lo * 100:.1f}, {r.allprior_hi * 100:+.1f}] | "
         f"{r.ratio:.2f} [{r.ratio_lo:.2f}, {r.ratio_hi:.2f}]")
    s = s.replace("0.", ".", 2) if False else s
    s = s.replace(f"{r.allprior_P_E:.3f}", f"{r.allprior_P_E:.3f}"[1:], 1).replace(f"{r.allprior_P_L:.3f}", f"{r.allprior_P_L:.3f}"[1:], 1)
    s = s.replace("-", "−")
    if r.allprior_hi > 0 and r.allprior_lo > 0:
        s = s.replace(f", +{r.allprior_hi * 100:.1f}]", f", {r.allprior_hi * 100:.1f}]")
    chk(s, f"allprior {d_} {w} {smp}")
# --- H2d ---
sa = mk["stats"]["any"]
for k in ["slope_all", "G_style", "G_topic", "G_style_minus_topic", "nollm_nonamefam__G_style", "nollm_nonamefam__G_topic"]:
    chk(c(sa[k]["est"], sa[k]["lo"], sa[k]["hi"]), f"h2d {k}")
for k in ["nollm_nonamefam__G_style_minus_topic", "median_rho_style", "median_rho_topic", "median_rho_style_minus_topic"]:
    chk(c(sa[k]["est"], sa[k]["lo"], sa[k]["hi"], 2), f"h2d {k}")
hb = idr["h2d_benchmark"]
chk(f"{hb['random_subset_slope_mean']:.2f} [{hb['random_subset_slope_lo']:.2f}, {hb['random_subset_slope_hi']:.2f}]", "random subset")
for part in ("last", "first"):
    s_ = mk["stats"][part]
    chk(f"{s_['slope_all']['est']:.3f} | {c(s_['G_style']['est'], s_['G_style']['lo'], s_['G_style']['hi'])} | "
        f"{m(s_['G_topic']['est'])} | {s_['median_rho_style']['est']:.2f} / {s_['median_rho_topic']['est']:.2f}", f"h2d {part}")
chk(f"{sa['median_rho_big_style']['est']:.2f} (style) and {sa['median_rho_big_topic']['est']:.2f}", "median big")
ws = mk["weight_shares_any"]
chk(f"{ws['topic']['llm_topic'] * 100:.1f}%", "llm weight")
# --- H2e ---
he = ss["h2e"]["email_2018to2020"]
for o, lab_ in [("name_primary", "NAME"), ("name_compound", "compound")]:
    x = he[o]["any"]["rho"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e rho {o}")
    x = he[o]["any"]["kit_within_share"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e lit {o}")
    x = ss["h2e_author"]["email_2018to2020"][o]["any"]["rho"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e author {o}")
    x = ss["h2e"]["email_1718to1920"][o]["any"]["rho"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e 2y {o}")
    x = ss["h2e_author"]["email_1718to1920"][o]["any"]["rho"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e 2y author {o}")
    x = ss["h2e"]["email_1718to1920"][o]["any"]["kit_within_share"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e 2y lit {o}")
    x = ss["obs_minus_null"][f"email_2018to2020|any|null_Nfirst|{o}"]; chk(c(x["est"], x["lo"], x["hi"], 2, sign=True), f"h2e obs-null {o}")
x = ss["obs_minus_null"]["email_1718to1920|any|null_Nfirst|name_primary"]; chk(c(x["est"], x["lo"], x["hi"], 2, sign=True), "h2e 2y obs-null")
en = ss["null_rho"]["email_2018to2020"]["any"]
chk(f"{en['null_Nfirst']['est']:.2f} / {en['null_NRfirst']['est']:.2f}", "h2e null")
chk(f"s̄ = {H['H2e']['estimate']['stayer_weight_sbar_any']:.2f}", "sbar email")
for part in ("last", "first"):
    x = he["name_primary"][part]["rho"]; chk(c(x["est"], x["lo"], x["hi"], 2), f"h2e {part}")
# --- S2.1 / S2.2 ---
s1 = s21[(s21["rule"] == "union") & (s21["sample"] == "dest>=2024")].iloc[0]
chk(f"−{abs(s1.name_primary_change_minus_drift) * 100:.1f} pp (se {s1.name_primary_change_minus_drift_se * 100:.1f}, p = {s1.name_primary_p_change_minus_drift:.3f})", "s21 raw")
chk(f"−{abs(s1.name_primary_change_minus_drift_topicadj) * 100:.1f} pp (se {s1.name_primary_change_minus_drift_topicadj_se * 100:.1f}, p = {s1.name_primary_p_change_minus_drift_topicadj:.3f})", "s21 topicadj")
chk(f"−{abs(s1.name_primary_change_minus_drift_intopic) * 100:.1f} pp (se {s1.name_primary_change_minus_drift_intopic_se * 100:.1f}, p = {s1.name_primary_p_change_minus_drift_intopic:.2f})", "s21 intopic")
chk(f"−{abs(s1.within_pair_minus_samekey) * 100:.1f} pp (se {s1.within_pair_minus_samekey_se * 100:.1f}, p = {s1.p_within_pair_minus_samekey:.2f})", "s21 samekey")
chk(f"+{s1.name_primary_implied_drift_topicadj * 100:.1f} pp", "drift topicadj"); chk(f"+{s1.name_primary_implied_drift_intopic * 100:.1f} pp", "drift intopic")
ss1 = s21[(s21["rule"] == "strict") & (s21["sample"] == "dest>=2024")].iloc[0]
chk(f"−{abs(ss1.name_primary_change_minus_drift) * 100:.1f} pp (se {ss1.name_primary_change_minus_drift_se * 100:.1f}, p = {ss1.name_primary_p_change_minus_drift:.2f})", "s21 strict")
P_ = s22[s22.model.str.startswith("placebo: clean, T 2023-25")].set_index("outcome")
Q_ = s22[s22.model.str.startswith("placebo: clean, no topic FE")].set_index("outcome")
for X, lab_ in [(P_, "primary"), (Q_, "pilot")]:
    for o in ("name_primary", "llm_topic"):
        r = X.loc[o]
        s = (f"{r.b_expo_past:+.3f} ({r.se_expo_past:.3f}) | {r.b_expo_future:+.3f} ({r.se_expo_future:.3f}) | "
             f"{r.past_minus_future:.3f} ({r.se_diff:.3f}) | {r.mde_diff:.3f}").replace("-", "−")
        chk(s, f"s22 {lab_} {o}")
chk(f"{P_.loc['name_primary','past_minus_future'] + 1.96 * P_.loc['name_primary','se_diff']:.3f}".replace("-", "−"), "s22 upper")
# --- removal ---
fam = pd.DataFrame(idr["family_removal"])
for pi in (0.5, 1.0):
    f_ = fam[fam.pi_pairs == pi].set_index("partition")
    chk(f"{abs(f_.loc['last','shift']):.3f} / {abs(f_.loc['any','shift']):.3f} / {abs(f_.loc['first','shift']):.3f}", f"family {pi}")
rem = pd.read_csv(D / "removal_extrapolation.csv")
r2 = rem[rem.frac.eq(0.2)].set_index("partition")
chk(f"{r2.loc['last','rho_sim_sd']:.3f}, {r2.loc['any','rho_sim_sd']:.3f} and {r2.loc['first','rho_sim_sd']:.3f}", "removal sd")
for part in ("last", "any", "first"):
    chk(f"{r2.loc[part,'rho_extrapolated_full']:.3f} (point only)", f"removal extrap {part}")

print(f"{n} checks, {len(fails)} failed")
for lab_, s in fails:
    print(f"  FAIL {lab_}: expected '{s}'")
