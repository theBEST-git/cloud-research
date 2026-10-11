"""WP4 fixer check: does arXiv metadata ever carry Unicode dash typography or ALL-CAPS titles? (channel criterion)"""
import json, re
import pandas as pd
import features as F
from analyses import _core as C
rows = []
for path in [C.CACHE / "arxiv_audit.jsonl", C.CACHE / "arxiv_audit_enlarge.jsonl", C.CACHE / "arxiv_audit_route.jsonl"]:
    for l in open(path):
        r = json.loads(l)
        for fld in ["v1_title", "latest_title"]:
            t = r.get(fld)
            if isinstance(t, str):
                rows.append(dict(src=path.name, fld=fld, t=t, typo=bool(F.LLM_TYPO.search(t)),
                                 anyuni=bool(re.search("[‐-―]", t)), caps=F.casing_style(t) == "all_caps"))
d = pd.DataFrame(rows)
print(d.groupby(["src", "fld"]).agg(n=("t", "size"), typo=("typo", "sum"), unicode_dash=("anyuni", "sum"), allcaps=("caps", "sum")))
u = C.load_universe(["submission_id", "year", "title"])
u = u[u.year >= 2023]
print("stored titles 2023-26: n", len(u), "typo", u.title.map(lambda t: bool(F.LLM_TYPO.search(t))).sum(),
      "allcaps", (u.title.map(F.casing_style) == "all_caps").sum())
