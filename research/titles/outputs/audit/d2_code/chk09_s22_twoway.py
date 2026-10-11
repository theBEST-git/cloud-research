"""Audit D2/S2.2: two-way (focal key, paper) CGM SEs for the primary placebo spec (NAME and llm_topic)."""
import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d2_panel as P
from analyses.d2_support import exposure_sets, future_tie
papers, prof, _ = P.load_panel()
S = exposure_sets(prof)
ft, panel = future_tie(S, papers)
for yname in ["name_primary", "llm_topic"]:
    d = panel[panel.outcome.eq(yname) & panel.clean & panel["T"].between(2023, 2025)].copy()
    ctr = ["own_prev", "log_authors"] + ([] if yname == "llm_topic" else ["llm_topic"])
    x = ["expo_past", "expo_future"]
    d = d.dropna(subset=x + ctr + ["y"]).reset_index(drop=True)
    d["rowid"] = np.arange(len(d))
    V = {}
    for cl in ["k", "p", "rowid"]:
        res = C.feols(d, "y", x + ctr, fe=["T", "topic100"], cluster=cl); V[cl] = res.vcov; b = res.params
    Vc = V["k"] + V["p"] - V["rowid"]
    c = pd.Series(0.0, index=b.index); c["expo_past"] = 1; c["expo_future"] = -1
    print(yname, "n", len(d), "papers", d.p.nunique(), "past %.4f se_k %.4f se_cgm %.4f | fut %.4f se_k %.4f se_cgm %.4f | diff %.4f se_k %.4f se_cgm %.4f" % (
        b.expo_past, np.sqrt(V["k"].loc["expo_past","expo_past"]), np.sqrt(Vc.loc["expo_past","expo_past"]),
        b.expo_future, np.sqrt(V["k"].loc["expo_future","expo_future"]), np.sqrt(Vc.loc["expo_future","expo_future"]),
        c @ b, np.sqrt(c @ V["k"] @ c), np.sqrt(c @ Vc @ c)))
