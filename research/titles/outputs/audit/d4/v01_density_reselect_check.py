"""Check that density_reselect row 0 reproduces the cached style density stage gains (selection on full sample)."""
import time
import numpy as np
from analyses import d4_stage_gains as S
t0 = time.time()
df = S.load_frame()
g, _, _ = S.gain_table(df, ["style_density", "F26", "F26_incl_title", "L_union", "L_noR24", "L_abstract"], "chk",
                       n_boot=0, periods={"2024-26": S.POST})
print(g[(g.pooling == "std")].pivot(index="feature", columns="gain", values="est").round(4).to_string())
r, info = S.density_reselect(df, n_boot=200)
print(r[["gain", "est", "lo95", "hi95"]].round(4).to_string())
print(info)
print(f"{time.time() - t0:.0f}s")
