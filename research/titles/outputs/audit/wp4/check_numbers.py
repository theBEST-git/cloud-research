"""WP4 fixer check: RESULTS.md agrees with results.json and the tables (verdicts and key numbers), the freeze hash
matches the cache bytes, and snapshot_bounds.py still matches the prereg bundle hash.
Run from research/titles/src:  /home/user/venv/bin/python /home/user/cloud-research/research/titles/outputs/audit/wp4/check_numbers.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import pandas as pd

STUDY = Path(__file__).resolve().parents[3]
OUT = STUDY / "outputs" / "snapshot"
R = json.loads((OUT / "results.json").read_text())
md = (OUT / "RESULTS.md").read_text()
H = {h["id"]: h for h in R["hypotheses"]}
bad = []

# 1. verdicts in the summary table
rows = {m.group(1): m.group(2) for m in re.finditer(r"^\| (SB\d|V7[ab]|G\d b?|G\d|G2b) \|.*\| \*\*([^*]+)\*\*[^|]*\|$", md, re.M)}
for hid, h in H.items():
    if hid == "G4_sens":
        continue
    want = h["verdict"].replace("_", " ").lower()
    got = rows.get(hid, "").lower()
    if not got.startswith(want.split(" (")[0]):
        bad.append(f"verdict {hid}: results.json {want!r} vs RESULTS.md {got!r}")

# 2. key numbers
tp = pd.read_csv(OUT / "T4_2_tipping_points.csv").set_index("feature")
fl = pd.read_csv(OUT / "T4_2_flip_matrices.csv")
fl = fl[fl.spec == "primary"].set_index("feature")
gate = pd.read_csv(OUT / "gate.csv").set_index("claim")
nm, nf = tp.loc["NAME"], fl.loc["NAME"]
fmt = lambda x, d=2: f"{x:.{d}f}".replace("-", "−")  # noqa: E731
need = [fmt(nm.tip_dec_pp), fmt(abs(100 * nf.did)), fmt(nm.G_dec_obs, 3), fmt(nm.G_dec_sel_point, 3),
        gate.loc["H4a NAME G_total within [0.90, 1.11] (2024-26 pooled; audit: primary)", "corrected_ci90"],
        f"{int(tp.passes_holm_dec.sum())} of {len(tp)}", fmt(nm.p_ident_dec, 3)]
for s in need:
    if s not in md:
        bad.append(f"number {s!r} missing from RESULTS.md")

# 3. freeze hash
fz = R["meta"]["audit_freeze"]["enlargement"]
raw = [ln for ln in (STUDY / fz["path"]).read_bytes().splitlines(keepends=True) if ln.endswith(b"\n")][:fz["n_lines_used"]]
if hashlib.sha256(b"".join(raw)).hexdigest() != fz["sha256_of_lines_used"]:
    bad.append("enlargement hash does not match the cache bytes")

# 4. snapshot_bounds.py unchanged vs the prereg bundle
bundle = (STUDY / "outputs" / "prereg" / "bundle.sha256").read_text()
want = [ln.split("  ")[0] for ln in bundle.splitlines() if ln.endswith("src/analyses/snapshot_bounds.py")][0]
got = hashlib.sha256((STUDY / "src" / "analyses" / "snapshot_bounds.py").read_bytes()).hexdigest()
if want != got:
    bad.append("snapshot_bounds.py differs from the prereg bundle hash")

# 5. no placeholders
for pat in [r"\bnan\b", r"PENDING", r"TODO", r"\{[a-z_]+\}"]:
    if re.search(pat, md):
        bad.append(f"placeholder {pat}")

print("\n".join(bad) if bad else f"OK: {len(H)} verdicts, {len(need)} key numbers, freeze hash, prereg hash, placeholders")
sys.exit(1 if bad else 0)
