"""Audit check: leverage of the H2d marker scatter (any-role partition).
Recomputes slope/r/G from markers_changes.csv and shows how much the few large-change markers drive them."""
import numpy as np
import pandas as pd

D = "/home/user/cloud-research/research/titles/outputs/d2_carriers/"
m = pd.read_csv(D + "markers_changes.csv")


def stats(df):
    x, y = df.delta.values, df.delta_S.values
    b, a = np.polyfit(x, y, 1)
    r = np.corrcoef(x, y)[0, 1]
    out = dict(n=len(df), slope=b, intercept=a, r=r)
    for ch in ("style", "topic"):
        d = df[df.channel == ch]
        if len(d):
            b0 = (d.delta * d.delta_S).sum() / (d.delta ** 2).sum()
            out[f"G_{ch}"] = 1 - b0
            out[f"n_{ch}"] = len(d)
    return out


for part in ("any", "last", "first"):
    a = m[m.partition == part].copy()
    print("==", part, {k: round(v, 4) if isinstance(v, float) else v for k, v in stats(a).items()})
    a["x2share"] = a.delta ** 2 / (a.delta ** 2).sum()
    st = a[a.channel == "style"].copy()
    st["x2share_style"] = st.delta ** 2 / (st.delta ** 2).sum()
    print(st.sort_values("x2share_style", ascending=False)[["marker", "delta", "delta_S", "rho", "x2share_style"]].head(12).round(4).to_string())
    big = a.delta.abs().sort_values(ascending=False).index[:10]
    print("  top-10 |delta| markers:", a.loc[big, "marker"].tolist())
    print("  without top-10 |delta|:", {k: round(v, 4) if isinstance(v, float) else v for k, v in stats(a.drop(big)).items()})
    small = a[a.delta.abs() < 0.01]
    print("  markers with |delta|<1pp:", len(small), {k: round(v, 4) if isinstance(v, float) else v for k, v in stats(small).items()})
    namefam = [x for x in a.marker if x.startswith("mk_name") or x in ("mk_compound", "mk_phrase_colon")]
    print("  name family + compound + phrase_colon:", namefam)
    print("  style G without those:", {k: round(v, 4) if isinstance(v, float) else v for k, v in stats(a[~a.marker.isin(namefam)]).items()})
