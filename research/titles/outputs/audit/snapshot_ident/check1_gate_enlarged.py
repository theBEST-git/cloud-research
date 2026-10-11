"""Audit check 1 (identification skeptic): does the H4a NAME gate (G1) and '0 of 24 identified' (SB2) hold when
(a) the full current enlargement cache is used (not the first 254 records), (b) the audit DiD is period-matched to
the 2024-26 prevalences it corrects, (c) only the new (out-of-sample) enlargement records are used?
Read-only: imports snapshot_bounds functions, writes only to outputs/audit/snapshot_ident/."""
import json, sys
from pathlib import Path
import numpy as np, pandas as pd
from analyses import snapshot_bounds as S
from analyses import _core as C

OUT = Path(__file__).resolve().parent
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
enl_raw = S.read_jsonl(S.ENLARGE_PATH)
print("enlarge records now:", len(enl_raw))
def clean(e):
    e = e[e.error.isna()] if "error" in e else e
    return e.drop_duplicates("submission_id", keep="last")
P = S.build_pairs(orig, U, "original")
Pe254 = S.build_pairs(clean(enl_raw.head(254)), U, "enlarge")
PeAll = S.build_pairs(clean(enl_raw), U, "enlarge")
keys_t = [k for k, *_ in S.TITLE_FEATS]
df = S.universe_frame()
keys_all = keys_t + [k for k, *_ in S.ABS_FEATS]
sums = S.stage_prevalences(df, keys_all)
Ppool, apool = S.pooled(sums, S.POST)
Pt = Ppool[:, :len(keys_t)]
specs = {
    "primary_orig": P,
    "enl254_pooled(reported)": pd.concat([P, Pe254], ignore_index=True),
    "enlAll_pooled": pd.concat([P, PeAll], ignore_index=True),
    "enlAll_pooled_2024_26": pd.concat([P, PeAll], ignore_index=True).query("year>=2024").reset_index(drop=True),
    "enlAll_newonly": PeAll,
    "enlAll_newonly_2024_26": PeAll.query("year>=2024").reset_index(drop=True),
    "orig_2024_26": P.query("year>=2024").reset_index(drop=True),
}
rows, idrows = [], []
for name, PP in specs.items():
    ft, db = S.flip_table(PP, keys_t, name)
    tp = S.tipping_table(Pt, apool, keys_t, ft, db, "2024-26")
    f = ft.set_index("feature").loc["NAME"]; t = tp.set_index("feature").loc["NAME"]
    rows.append(dict(spec=name, n_acc=int(f.n_acc), n_rej=int(f.n_rej), v1p_acc=int(f.v1_present_acc), v1p_rej=int(f.v1_present_rej),
                     adds_acc=int(f.adds_acc), drops_acc=int(f.drops_acc), adds_rej=int(f.adds_rej), drops_rej=int(f.drops_rej),
                     net_acc_pp=100*f.net_acc, net_rej_pp=100*f.net_rej,
                     did_pp=100*f.did, did_lo=100*f.did_lo, did_hi=100*f.did_hi, did_lo_wald=100*f.did_lo_wald, did_hi_wald=100*f.did_hi_wald,
                     tip_dec=t.tip_dec_pp, tip_total=t.tip_total_pp, share_of_tip=f.did*100/t.tip_dec_pp,
                     Gdec_obs=t.G_dec_obs, Gdec_corr90=(round(t.G_dec_corr_lo90,3), round(t.G_dec_corr_hi90,3)),
                     Gtot_obs=t.G_total_obs, Gtot_corr90=(round(t.G_total_corr_lo90,3), round(t.G_total_corr_hi90,3)),
                     Gtot_pass=bool(0.90 <= t.G_total_corr_lo90 and t.G_total_corr_hi90 <= 1.11),
                     Gdec_pass=bool(0.90 <= t.G_dec_corr_lo90 and t.G_dec_corr_hi90 <= 1.11),
                     G_total_sel_point=t.G_total_sel_point))
    tpi = tp.set_index("feature"); fti = ft.set_index("feature")
    idrows.append(dict(spec=name, auditable=sorted(fti[fti.auditable].index.tolist()),
                       identified_dec=sorted(tpi[tpi.G_dec_identified].index.tolist()),
                       passes_gate=sorted(tpi[tpi.claim_dec_passes_gate].index.tolist()),
                       identified_wald=sorted(tpi[tpi.G_dec_identified_wald].index.tolist())))
    if name == "enlAll_pooled":
        tp.to_csv(OUT / "check1_tipping_enlAll.csv", index=False); ft.to_csv(OUT / "check1_flips_enlAll.csv", index=False)
    if name == "enlAll_pooled_2024_26":
        tp.to_csv(OUT / "check1_tipping_enlAll_post.csv", index=False); ft.to_csv(OUT / "check1_flips_enlAll_post.csv", index=False)
R = pd.DataFrame(rows)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
print(R.round(3).to_string())
for r in idrows: print(r)
R.to_csv(OUT / "check1_name_gate_by_spec.csv", index=False)
json.dump(idrows, open(OUT / "check1_identified_by_spec.json", "w"), indent=1)
# per-year NAME net flips for the full pooled audit
PA = specs["enlAll_pooled"]
for y in sorted(PA.year.unique()):
    for dec in ["accepted", "rejected"]:
        g = PA[(PA.year == y) & (PA.decision == dec)]
        print(y, dec, len(g), "v1+", int(g.NAME_v1.sum()), "adds", int(((g.NAME_v1==0)&(g.NAME_or==1)).sum()), "drops", int(((g.NAME_v1==1)&(g.NAME_or==0)).sum()))
