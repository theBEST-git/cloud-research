"""Re-run the D3 camera-ready slot audit on the enlargement file as it stands now (read-only)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from analyses import _core as C
from analyses import d3_slots as S
OUT = Path(__file__).resolve().parent
inv = json.load(open(C.OUT / "d3_register" / "slot_inventory.json"))
inv = inv.get("inventory", inv)
df = S.load_frame()
pairs, flips, meta = S.audit(df, inv)
print(json.dumps(meta, indent=1, default=str))
print(flips.to_string())
flips.to_csv(OUT / "audit_flips_current.csv", index=False)
json.dump(meta, open(OUT / "audit_meta_current.json", "w"), indent=1, default=str)
