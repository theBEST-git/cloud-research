"""Integration pass 2 (issue X13): sensitivity of D1's misclassification-corrected tool share to the false-positive
baseline. D1 treats the 2023 F_d1 share as all false positives; D3 and VALIDATION V3 use 2021-22. ICLR 2023 accepted
abstracts are post-ChatGPT camera-ready text (D4), so the 2023 share may contain true positives.
Run: cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python ../outputs/audit/integration/check_fpr_baseline.py
Writes outputs/audit/integration/check_fpr_baseline.json."""
import json
from pathlib import Path

import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from analyses import d1_decompose as DD
from analyses import _core as C

OUT = Path(__file__).resolve().parent
dec = json.loads((C.OUT / "d1_break" / "decompose.json").read_text())
tool = dec["tool"]
d26 = tool["delta_2026"]
dname, s26 = float(tool["dNAME_2023_2026"]), float(tool["share_F_2026"])
df = DD.load()
df = df.merge(C.load_universe(["submission_id", "ACC"]), on="submission_id", how="left", validate="1:1")
y = df.year
shares = {
    "2023 (D1 baseline)": float(df.loc[y == 2023, "F_d1"].mean()),
    "2023 accepted": float(df.loc[(y == 2023) & (df.ACC == 1), "F_d1"].mean()),
    "2023 not accepted": float(df.loc[(y == 2023) & (df.ACC == 0), "F_d1"].mean()),
    "2021-22": float(df.loc[y.isin([2021, 2022]), "F_d1"].mean()),
    "2021-22 F_any (V3 / D3 baseline)": float(df.loc[y.isin([2021, 2022]), "F_any"].mean()),
}
rows = {}
for lab in ["2023 (D1 baseline)", "2021-22", "2023 not accepted"]:
    out = {}
    for A in DD.A_MAX:
        mc = DD.misclass_factor(A, s26, shares[lab])
        if not mc["identified"]:
            out[str(A)] = None
            continue
        k = mc["k"]
        out[str(A)] = dict(share=d26["delta"] / k * A / dname, lo=d26["lo"] / k * A / dname,
                           hi=d26["hi"] / k * A / dname, recall=mc["recall"], k=k)
    rows[lab] = dict(fpr=shares[lab], tool_share_2026_delta=out)
assert abs(rows["2023 (D1 baseline)"]["tool_share_2026_delta"]["0.39"]["share"]
           - tool["tool_share_at_A_corrected_2026_delta"]["0.39"]["share"]) < 1e-12, "does not reproduce D1"
res = dict(note=__doc__.split("\n")[0], F_d1_shares=shares, n_2023_acc=int(((y == 2023) & (df.ACC == 1)).sum()),
           corrected_tool_share_by_fpr_baseline=rows)
(OUT / "check_fpr_baseline.json").write_text(json.dumps(res, indent=1))
for k, v in shares.items():
    print(f"{k:35s} {100 * v:.2f}%")
for lab, r in rows.items():
    t = r["tool_share_2026_delta"]["0.39"]
    print(f"A=0.39, fpr {lab:22s} ({100 * r['fpr']:.2f}%): {100 * t['share']:.1f}% [{100 * t['lo']:.1f}, {100 * t['hi']:.1f}]"
          f" recall {t['recall']:.2f} k {t['k']:.3f}")
