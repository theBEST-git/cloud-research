"""Identification audit D2, check 3 (H2b, life-cycle vs cohort; H2d mechanical slope).

(a) First-position newcomer premium by year with a SYMMETRIC 2-year lookback (new = key not seen in y-1 or
    y-2; years 2023-2026 so every year has a full 2-year lookback): raw, size+topic FE, last-key FE.  If the
    premium already existed in 2023 (pre-LLM-boom), the first-position 'generational increment' is (partly) a
    stable newcomer/life-cycle effect amplified by field growth, not a post-2023 cohort taste.
    Also the newcomer share at first position by year.
(b) H2d: slope / r of within-subset change on population change across the 85 markers when the 'stayer'
    subset is replaced by a RANDOM paper subset with the same E/L weights (shows slope~1, r~.99 is the
    expectation for any large subset), and under the pure first-author-generational null for NAME.
"""
import json
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d2_panel as P

papers, prof, _ = P.load_panel()
pp = papers.set_index("submission_id")
r = prof.copy()
ky = set(zip(r.key, r.year))
r["new2"] = [not (((k, y - 1) in ky) or ((k, y - 2) in ky)) for k, y in zip(r.key, r.year)]
f = r[r.is_first & r.year.between(2023, 2026)].drop_duplicates("submission_id")
lk = r[r.is_last].drop_duplicates("submission_id").set_index("submission_id").key
f = f.assign(last_key=f.submission_id.map(lk), y=f.submission_id.map(pp.name_primary).astype(float),
             size_bin=f.submission_id.map(pp.size_bin), topic100=f.submission_id.map(pp.topic100),
             new=f.new2.astype(float))
f = f[f.last_key.notna() & f.last_key.ne(f.key)]
f["lk"] = pd.factorize(f.last_key)[0]
rows = []
for yr in [2023, 2024, 2025, 2026]:
    d = f[f.year.eq(yr)]
    row = dict(year=yr, n=len(d), share_new_first=d.new.mean(), NAME_new=d[d.new.eq(1)].y.mean(),
               NAME_prior=d[d.new.eq(0)].y.mean())
    for lab, fe in [("raw", []), ("size_topic", ["size_bin", "topic100"]), ("lastkey", ["lk"]),
                    ("lastkey_size_topic", ["lk", "size_bin", "topic100"])]:
        res = C.feols(d, "y", ["new"], fe=fe, cluster="lk")
        row[f"gap_{lab}"] = float(res.params["new"]); row[f"se_{lab}"] = float(res.se["new"])
    rows.append(row)
t = pd.DataFrame(rows)
pd.set_option("display.width", 250)
print(t.round(3).to_string())
t.to_csv("../outputs/audit/d2_ident/chk03a_newcomer_premium.csv", index=False)
# pooled test of premium change 2023 vs 2025-26 (last-key FE)
d = f[f.year.isin([2023, 2025, 2026])].assign(post=lambda x: x.year.ge(2025).astype(float))
d["new_post"] = d.new * d.post
d["yr"] = d.year.astype(str)
res = C.feols(d, "y", ["new", "new_post"], fe=["lk", "yr", "size_bin", "topic100"], cluster="lk")
print(f"premium 2023 (lk+yr+size+topic FE) {res.params['new']:.4f} ({res.se['new']:.4f}); "
      f"change in premium 2025-26 vs 2023 {res.params['new_post']:.4f} ({res.se['new_post']:.4f})")

# shift-share at first position with symmetric definition: how much of the 2023->2025-26 first-position change is
# composition (newcomer share) vs within new / within prior
a, b = f[f.year.eq(2023)], f[f.year.isin([2025, 2026])]
sa, sb = a.new.mean(), b.new.mean()
pa = a.groupby("new").y.mean(); pb = b.groupby("new").y.mean()
D = b.y.mean() - a.y.mean()
within = ((sa + sb) / 2) * (pb[1] - pa[1]) + (1 - (sa + sb) / 2) * (pb[0] - pa[0])
comp = (sb - sa) * ((pa[1] + pb[1]) / 2 - (pa[0] + pb[0]) / 2)
print(f"first-position 2023 -> 2025-26: delta {D:.4f}; within-new/prior {within:.4f} ({within/D:.2f}); "
      f"composition (newcomer share {sa:.3f} -> {sb:.3f}) {comp:.4f} ({comp/D:.2f}); "
      f"prior-first change {pb[0]-pa[0]:.4f} ({(pb[0]-pa[0])/D:.2f}), new-first change {pb[1]-pa[1]:.4f}")

# ---------------- (b) H2d mechanical ----------------
mres = json.loads((P.OUTDIR / "markers_results.json").read_text())
markers = mres["style_markers"] + mres["topic_markers"]
for k in [m for m in markers if m.startswith("topic_")]:
    papers[k] = (papers.topic100 == int(k.split("_")[1])).astype(int)
EL = papers[papers.year.isin(P.E_WIN + P.L_WIN)].copy()
isL = EL.year.isin(P.L_WIN).to_numpy()
Y = EL[markers].to_numpy(float)
# stayer any-role weight per paper
g = P.key_groups(prof, P.E_WIN, P.L_WIN)
rr = prof[prof.year.isin(P.E_WIN + P.L_WIN)].assign(S=lambda x: x.key.map(g.S).fillna(False))
ws = rr[rr.S].groupby("submission_id").w_any.sum().reindex(EL.submission_id).fillna(0).to_numpy()
wall = rr.groupby("submission_id").w_any.sum().reindex(EL.submission_id).fillna(0).to_numpy()
def slope_r(wsub):
    dpop = (Y[isL] * wall[isL, None]).sum(0) / wall[isL].sum() - (Y[~isL] * wall[~isL, None]).sum(0) / wall[~isL].sum()
    dsub = (Y[isL] * wsub[isL, None]).sum(0) / wsub[isL].sum() - (Y[~isL] * wsub[~isL, None]).sum(0) / wsub[~isL].sum()
    b = np.cov(dpop, dsub)[0, 1] / np.var(dpop, ddof=1)
    return b, np.corrcoef(dpop, dsub)[0, 1], dpop, dsub
b, rr_, dpop, dsub = slope_r(ws)
print(f"\nH2d observed (recomputed, any role): slope {b:.3f}, r {rr_:.3f}")
rng = np.random.default_rng(3)
sim = []
for _ in range(50):
    # random paper subset with the same expected stayer weight in E and L
    pE, pL = ws[~isL].sum() / wall[~isL].sum(), ws[isL].sum() / wall[isL].sum()
    u = rng.random(len(EL))
    wr = np.where(isL, (u < pL), (u < pE)).astype(float) * wall
    sim.append(slope_r(wr)[:2])
sim = np.array(sim)
print(f"random paper subset (same E/L stayer weights): slope mean {sim[:,0].mean():.3f} [{np.quantile(sim[:,0],.025):.3f},{np.quantile(sim[:,0],.975):.3f}], r mean {sim[:,1].mean():.3f}")
