"""Audit D2: row-level bootstrap to form a Cameron-Gelbach-Miller two-way variance V_key + V_paper - V_row."""
import numpy as np, pandas as pd
exec(open("../outputs/audit/d2_code/chk03_bootstrap_dependence.py").read().split("rng = np.random.default_rng(1)")[0])
rng = np.random.default_rng(2)
rw = []
n = len(r)
for b in range(300):
    rw.append(stats(rng.multinomial(n, np.full(n, 1/n)).astype(float)))
d = pd.DataFrame(rw)
prev = pd.read_csv("../outputs/audit/d2_code/chk03_bootstrap_dependence.csv").pivot(index="stat", columns="scheme", values="se")
prev["row"] = d.std(ddof=1)
prev["cgm"] = np.sqrt(np.clip(prev.key**2 + prev.paper**2 - prev.row**2, 0, None))
print(prev.round(4))
prev.to_csv("../outputs/audit/d2_code/chk03b_cgm.csv")
