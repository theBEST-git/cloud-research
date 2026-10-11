"""Audit D2: alias-collapse groups (trailing digits stripped): size distribution and papers/year of merged aliases."""
import numpy as np, pandas as pd
from analyses import d2_panel as P
papers, prof, _ = P.load_panel()
ak = prof.groupby("alias").key.nunique().sort_values(ascending=False)
print("aliases:", len(ak), "with >1 key:", (ak>1).sum(), "keys in merged aliases:", ak[ak>1].sum())
print(ak.head(10).to_string())
py = prof.groupby(["alias","year"]).submission_id.nunique()
print("alias-years with >40 papers:", (py>40).sum(), " max:", py.max())
print(py.sort_values(ascending=False).head(8).to_string())
