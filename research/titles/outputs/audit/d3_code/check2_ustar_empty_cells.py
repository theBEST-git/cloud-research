"""Audit D3/H3e: empty bootstrap cells in ustar_table are scored as share 0 (num/max(den,1e-12)), not skipped.
Count affected draws and recompute the U* CI with empty cells treated as missing (drop that slot-year)."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d3_slots as D3
from analyses import d3_vintage as V
from analyses import d3_signature_bound as SB

inv = D3.frozen_inventory()
df = V.prep(D3.load_frame())
P = D3.slot_panel(df, inv, controls=False)
S = P[P.year >= 2018].reset_index(drop=True)
yv = S.y.to_numpy(float)
post, base = (2024, 2025), (2022, 2023)
keys, cols = [], []
for s in D3.SLOTS:
    ms = (S.slot == s).to_numpy()
    keys.append((s, "pre")); cols.append(ms & S.year.isin(base).to_numpy())
    for yr in post:
        for f in (0, 1):
            keys.append((s, f"F{f}", yr)); cols.append(ms & (S.year == yr).to_numpy() & (S.F_any == f).to_numpy())
        keys.append((s, "all", yr)); cols.append(ms & (S.year == yr).to_numpy())
M = np.column_stack(cols).astype(float)
idx = {k: i for i, k in enumerate(keys)}
den0 = np.ones(len(S)) @ M
W = np.vstack([w.astype(float) for w in C.boot_weights(len(S), 2000, strata=S.year.to_numpy(),
                                                       clusters=S.submission_id.to_numpy(), seed=SB.SEED)])
NUM, DEN = (W * yv) @ M, W @ M
used = [k for k in keys if k[1] != "all"]
empty = {k: float((DEN[:, idx[k]] == 0).mean()) for k in used}
print("share of draws with an empty cell:", {str(k): v for k, v in empty.items() if v > 0})
any_empty = np.zeros(len(W), bool)
for k in used:
    any_empty |= DEN[:, idx[k]] == 0
print("draws with >=1 empty cell:", any_empty.mean())

def ustar(num, den, skip_empty, slots=D3.SLOTS):
    a = np.zeros(num.shape[0]); b = np.zeros(num.shape[0])
    for s in slots:
        pre_d = den[:, idx[(s, "pre")]]
        pre = num[:, idx[(s, "pre")]] / np.maximum(pre_d, 1e-12)
        for yr in post:
            wy = den0[idx[(s, "all", yr)]]
            d0, d1 = den[:, idx[(s, "F0", yr)]], den[:, idx[(s, "F1", yr)]]
            f0 = num[:, idx[(s, "F0", yr)]] / np.maximum(d0, 1e-12)
            f1 = num[:, idx[(s, "F1", yr)]] / np.maximum(d1, 1e-12)
            ok = np.ones_like(f0, bool) if not skip_empty else (pre_d > 0) & (d0 > 0) & (d1 > 0)
            a += np.where(ok, wy * (f0 - pre), 0); b += np.where(ok, wy * (f1 - pre), 0)
    return a / b
u0 = ustar(NUM[:1] * 0 + (np.ones(len(S)) * yv) @ M, den0[None, :], False)
print("point U*", u0)
for skip in (False, True):
    ub = ustar(NUM, DEN, skip)
    print("skip_empty", skip, "CI", np.nanquantile(ub, [0.025, 0.975]).round(3), "P(U*>0.8)", np.nanmean(ub > 0.8).round(3))
ub_noadj = ustar(NUM, DEN, False, slots=["improve", "reveal", "exploit"])
pt = ustar((np.ones(len(S)) * yv) @ M[None, :, :][0][None, :] if False else ((yv) @ M)[None, :], den0[None, :], False,
           slots=["improve", "reveal", "exploit"])
print("opener slots only: point", pt, "CI", np.nanquantile(ub_noadj, [0.025, 0.975]).round(3))
