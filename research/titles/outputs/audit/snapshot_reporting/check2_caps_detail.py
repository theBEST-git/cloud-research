"""Reporting audit: per-cap detail for features that become identified as the enlargement grows."""
from pathlib import Path
import pandas as pd
from analyses import _core as C
from analyses import snapshot_bounds as SB

OUT = Path(__file__).resolve().parent
U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = SB.read_jsonl(SB.ORIG_PATH)
P = SB.build_pairs(orig, U, "original")
keys_t = [k for k, *_ in SB.TITLE_FEATS]
df = SB.universe_frame()
sums = SB.stage_prevalences(df, keys_t)
Ppool, apool = SB.pooled(sums, SB.POST)
enl_all = SB.read_jsonl(SB.ENLARGE_PATH).head(1611)
rows = []
for cap in [254, 300, 400, 500, 600, 800, 1000, 1200, 1400, 1611]:
    enl = enl_all.head(cap)
    enl = enl[enl.error.isna()] if "error" in enl else enl
    enl = enl.drop_duplicates("submission_id", keep="last")
    Pe = SB.build_pairs(enl, U, "enlarge")
    Pall = pd.concat([P, Pe], ignore_index=True)
    ft, db = SB.flip_table(Pall, keys_t, f"enl{cap}")
    tq = SB.tipping_table(Ppool, apool, keys_t, ft, db, "2024-26").set_index("feature")
    fti = ft.set_index("feature")
    for k in ["NAME", "compound", "sentence_case", "O_union", "title_case", "mixed_case_name"]:
        r, f = tq.loc[k], fti.loc[k]
        rows.append(dict(cap=cap, feature=k, v1=f"{f.v1_present_acc}/{f.v1_present_rej}",
                         flips=f"+{f.adds_acc}/-{f.drops_acc} | +{f.adds_rej}/-{f.drops_rej}", auditable=r.auditable,
                         did=r.did_pp, lo=r.did_lo_pp, hi=r.did_hi_pp, tip=r.tip_dec_pp,
                         ident=r.G_dec_identified, gate=r.claim_dec_passes_gate,
                         G_dec_corr95=f"[{r.G_dec_corr_lo95:.3f}, {r.G_dec_corr_hi95:.3f}]"))
t = pd.DataFrame(rows)
t.to_csv(OUT / "check2_caps_detail.csv", index=False)
pd.set_option("display.width", 250)
print(t.round(2).to_string())
