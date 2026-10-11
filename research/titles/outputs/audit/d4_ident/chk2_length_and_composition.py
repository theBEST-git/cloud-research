"""D4 identification audit, check 2.
(a) Abstract length by pool and year: are accepted (camera-ready) abstracts longer? F24 = 'any of 21 words' is
    mechanically length-dependent, so a camera-ready length gap would move accepted-only marker rates and the
    accepted-only Kobak baseline.
(b) Kobak F24 bounds (primary 'cons' baseline) with each set's F24 rate standardised, within year, to the s0
    abstract-length distribution (length deciles on 2021-26 s0).
(c) Which markers carry the L-union depletion? L-union without R24, and the R24 pre/post contrast.
(d) Length-standardised identified-stage gains (predec_crf) for F24 and L_abstract, 2024-26 vs 2018-23.
"""
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/cloud-research/research/titles/src")
from analyses import d4_stage_gains as S  # noqa: E402
from analyses import d4_bias_atlas as A  # noqa: E402

OUT = "/home/user/cloud-research/research/titles/outputs/audit/d4_ident/"
df = S.load_frame(min_year=2018, density=False)
df["alen"] = df.abstract.fillna("").str.split().str.len()
pd.set_option("display.width", 200)

# (a) abstract length
print("(a) median abstract words by year x pool")
print(df.groupby(["year", "pool"]).alen.median().unstack().round(0).to_string())
print("mean words ACC / REJ by year:")
m = df.groupby(["year", "pool"]).alen.mean().unstack()
print((m.ACC / m.REJ).round(3).to_string())

# (b) Kobak with length standardisation
d = df[df.year >= 2021].copy()
edges = np.quantile(d.loc[d.s0 == 1, "alen"], np.linspace(0, 1, 11))
edges[0], edges[-1] = -1, 1e9
d["lbin"] = np.digitize(d.alen, edges[1:-1])


def prev(d, col, st, std):
    out = {}
    for y in range(2021, 2027):
        dy = d[d.year == y]
        if not std:
            out[y] = dy.loc[dy[st] == 1, col].mean()
            continue
        w = dy.loc[dy.s0 == 1, "lbin"].value_counts(normalize=True)
        r = dy[dy[st] == 1].groupby("lbin")[col].mean()
        out[y] = float((w * r.reindex(w.index)).sum() / w[r.reindex(w.index).notna()].sum())
    return out


rows = []
for std in [False, True]:
    for bl in ["cons", "max2122"]:
        P0 = prev(d, "f24", "s0", std)
        P3 = prev(d, "f24", "s3", std)
        for Y in (2024, 2025, 2026):
            b0 = float(A.kobak_from_prev({k: np.array(v) for k, v in P0.items()}, Y, bl))
            b3 = float(A.kobak_from_prev({k: np.array(v) for k, v in P3.items()}, Y, bl))
            rows.append(dict(length_std=std, baseline=bl, year=Y, all_pp=100 * b0, acc_pp=100 * b3, ratio=b3 / b0,
                             acc_base_2023=100 * P3[2023], all_base_2023=100 * P0[2023]))
kb = pd.DataFrame(rows)
print("\n(b) Kobak F24 bounds, raw vs length-standardised")
print(kb.round(3).to_string())
kb.to_csv(OUT + "chk2b_kobak_lengthstd.csv", index=False)

# (c) L-union composition
df["L_noR24"] = df[["title_typo", "r26_any", "f24", "f26", "abs_emdash"]].max(axis=1)
S.FEAT_COL["L_noR24"] = "L_noR24"
S.FEAT_SET["L_noR24"] = "L2"
g, _, _ = S.gain_table(df, ["L_union", "L_noR24", "R24", "L_title", "L_abstract", "F24", "style_density"]
                       if "xs_per100" in df else ["L_union", "L_noR24", "R24", "L_title", "L_abstract", "F24"],
                       "audit", n_boot=1000, periods={"2024-26": S.POST, "2018-23": S.PRE})
gg = g[(g.pooling == "std") & g.gain.isin(["total", "predec", "predec_crf", "dec"])]
print("\n(c) gains, std pooling")
print(gg[["feature", "period", "gain", "est", "lo95", "hi95", "p_ge1"]].round(3).to_string())
gg.to_csv(OUT + "chk2c_L_composition.csv", index=False)

# (d) length-standardised identified-stage gain (s2n vs s0n) for abstract markers
rows = []
edges_all = np.quantile(df.alen, np.linspace(0, 1, 11))
edges_all[0], edges_all[-1] = -1, 1e9
df["lbin"] = np.digitize(df.alen, edges_all[1:-1])
for per, yrs in {"2024-26": S.POST, "2018-23": S.PRE}.items():
    for col in ["f24", "L_abstract", "abs_emdash", "L_union", "name_primary"]:
        num, den, numr, denr = 0, 0, 0, 0
        wsum = 0
        for y in yrs:
            dy = df[df.year == y]
            wy = (dy.s0 == 1).sum()
            w = dy.loc[dy.s0n == 1, "lbin"].value_counts(normalize=True)
            ra = dy[dy.s2n == 1].groupby("lbin")[col].mean().reindex(w.index)
            rb = dy[dy.s0n == 1].groupby("lbin")[col].mean().reindex(w.index)
            num += wy * float((w * ra).sum())
            den += wy * float((w * rb).sum())
            numr += wy * dy.loc[dy.s2n == 1, col].mean()
            denr += wy * dy.loc[dy.s0n == 1, col].mean()
        rows.append(dict(period=per, feature=col, predec_crf_raw=numr / denr, predec_crf_lenstd=num / den))
        # also mean length by s2n vs exiting
    print()
ld = pd.DataFrame(rows)
print("(d) identified-stage gains, raw vs length-standardised")
print(ld.round(4).to_string())
ex = df[(df.s0n == 1)].assign(exited=lambda x: 1 - x.s2n)
print("mean abstract words, non-accepted: exited (WD/DR) vs stayed (REJ), by period")
print(ex.groupby([ex.year >= 2024, "exited"]).alen.mean().round(1).to_string())
