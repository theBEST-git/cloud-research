"""Reporting audit (WP4 snapshot): targeted recomputations. Read-only on data/cache and outputs/snapshot.

1. Reproduce the primary NAME tipping row from the module's own functions (sanity).
2. Enlarged-audit gate (H4a NAME G_total corrected 90% CI) at enlargement caps 248, 254, 500, 1000 and all
   records now in the cache: does the 'passes only with the enlarged audit' verdict hold?
3. Per-year accepted/all F24 prevalence ratios (RESULTS section 6 reading 1: 0.93 / 0.94 / 1.02).
4. Audit-size statements in section 4 ('no audit size would identify', '3.2x', '54% usable rate').
Writes CSV/JSON next to this script.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from analyses import _core as C
from analyses import snapshot_bounds as SB

OUT = Path(__file__).resolve().parent
Z = 1.959963984540054


def main():
    U = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
    orig = SB.read_jsonl(SB.ORIG_PATH)
    P = SB.build_pairs(orig, U, "original")
    keys_t = [k for k, *_ in SB.TITLE_FEATS]
    keys_a = [k for k, *_ in SB.ABS_FEATS]
    flips, did_b = SB.flip_table(P, keys_t, "primary", Wb=SB.boot_matrix(P))
    df = SB.universe_frame()
    sums = SB.stage_prevalences(df, keys_t + keys_a)
    Ppool, apool = SB.pooled(sums, SB.POST)
    Pt = Ppool[:, :len(keys_t)]
    tp = SB.tipping_table(Pt, apool, keys_t, flips, did_b, "2024-26").set_index("feature")
    out = {"primary_NAME": tp.loc["NAME", ["did_pp", "did_lo_pp", "did_hi_pp", "tip_dec_pp", "G_total_corr_lo90",
                                          "G_total_corr_hi90", "G_dec_corr_lo90", "G_dec_corr_hi90"]].to_dict()}

    # 2. enlarged audit at several caps
    enl_all = SB.read_jsonl(SB.ENLARGE_PATH)
    out["enlarge_records_now"] = int(len(enl_all))
    rows = []
    for cap in [248, 254, 500, 1000, len(enl_all)]:
        enl = enl_all.head(cap)
        enl = enl[enl.error.isna()] if "error" in enl else enl
        enl = enl.drop_duplicates("submission_id", keep="last")
        Pe = SB.build_pairs(enl, U, "enlarge")
        Pall = pd.concat([P, Pe], ignore_index=True)
        ft, db = SB.flip_table(Pall, keys_t, f"enl{cap}")
        tq = SB.tipping_table(Pt, apool, keys_t, ft, db, "2024-26").set_index("feature")
        fti = ft.set_index("feature")
        nm = tq.loc["NAME"]
        rows.append(dict(cap=cap, n_records=len(enl), n_usable_new=len(Pe), usable_rate_new=len(Pe) / len(enl),
                         n_acc=int(fti.loc["NAME", "n_acc"]), n_rej=int(fti.loc["NAME", "n_rej"]),
                         name_did=nm.did_pp, name_lo=nm.did_lo_pp, name_hi=nm.did_hi_pp,
                         Gtot_corr_lo90=nm.G_total_corr_lo90, Gtot_corr_hi90=nm.G_total_corr_hi90,
                         gate_total_pass=bool(0.90 <= nm.G_total_corr_lo90 and nm.G_total_corr_hi90 <= 1.11),
                         Gdec_corr_lo90=nm.G_dec_corr_lo90, Gdec_corr_hi90=nm.G_dec_corr_hi90,
                         n_identified=int(tq.G_dec_identified.sum()),
                         identified=",".join(tq.index[tq.G_dec_identified]),
                         identified_wald_or_boot=",".join(tq.index[(tq.G_dec_identified_wald |
                                                                     tq.G_dec_identified_boot) & tq.auditable]),
                         auditable=",".join(tq.index[tq.auditable]),
                         sentence_case_v1=f"{fti.loc['sentence_case', 'v1_present_acc']}/"
                                          f"{fti.loc['sentence_case', 'v1_present_rej']}",
                         sentence_case_tip=tq.loc["sentence_case", "tip_dec_pp"],
                         sentence_case_ci=f"[{tq.loc['sentence_case', 'did_lo_pp']:.2f}, "
                                          f"{tq.loc['sentence_case', 'did_hi_pp']:.2f}]"))
    enl_tab = pd.DataFrame(rows)
    enl_tab.to_csv(OUT / "check1_enlarged_gate_by_cap.csv", index=False)
    print(enl_tab.round(3).to_string())

    # 3. per-year accepted/all ratios for F24 (stored abstracts), s3 / s0
    j = (keys_t + keys_a).index("F24")
    rat = {}
    for y in (2024, 2025, 2026):
        S, N = sums[y]
        p0 = S[0, j, 0] / N[0, 0]
        p3 = S[0, j, 2] / N[0, 2]
        rat[y] = dict(P_s0=p0, P_s3=p3, ratio=p3 / p0)
    out["F24_acc_over_all_by_year"] = rat
    print("F24 accepted/all by year:", {y: round(v["ratio"], 3) for y, v in rat.items()})

    # 4. audit size statements (NAME, primary)
    f = flips.set_index("feature").loc["NAME"]
    se, D, tip = f.did_se, f.did, tp.loc["NAME", "tip_dec_pp"] / 100
    n_pairs = len(P)
    k50 = (Z * se / tip) ** 2
    k80 = ((Z + 0.8416) * se / tip) ** 2
    # at the observed point estimate (D < tip): the upper bound D + Z se/sqrt(k) clears tip when
    k_at_point = (Z * se / (tip - D)) ** 2 if tip > D else np.inf
    out["audit_size"] = dict(n_pairs=n_pairs, se_pp=100 * se, tip_pp=100 * tip, did_pp=100 * D,
                             mult_if_D0_50pct=k50, pairs_if_D0_50pct=k50 * n_pairs,
                             mult_if_D0_80pct_power=k80, pairs_if_D0_80pct_power=k80 * n_pairs,
                             mult_at_observed_point=k_at_point, pairs_at_observed_point=k_at_point * n_pairs,
                             original_usable_rate=n_pairs / len(orig))
    # same using the enlarged (254) estimate
    r254 = enl_tab[enl_tab.cap == 254].iloc[0]
    se254 = (r254.name_hi - r254.name_lo) / (2 * Z) / 100
    k_pt_254 = (Z * se254 / (tip - r254.name_did / 100)) ** 2
    out["audit_size"]["enlarged254_mult_at_point"] = k_pt_254
    out["audit_size"]["enlarged254_pairs_at_point"] = k_pt_254 * (r254.n_acc + r254.n_rej)
    print(json.dumps(out["audit_size"], indent=1))
    (OUT / "check1_recompute.json").write_text(json.dumps(C.jsonable(out) if hasattr(C, "jsonable") else
                                                          SB.jsonable(out), indent=1))


if __name__ == "__main__":
    main()
