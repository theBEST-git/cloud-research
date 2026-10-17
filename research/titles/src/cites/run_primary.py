"""Run the 8 pre-registered primary tests once (real outcomes), Holm-adjust, save outputs/cites/primary.json."""
from __future__ import annotations

import warnings

from cites import core

warnings.filterwarnings("ignore")


def main():
    df = core.load()
    prim = {f: core.primary(df, f) for f in core.FEATURES}
    adj = core.holm({f: r["p"] for f, r in prim.items()})
    for f in prim:
        prim[f]["p_holm"] = adj[f]
        prim[f]["label"] = core.FEATURES[f]
    core.save({"n_papers": int(len(df)), "years": list(core.YEARS), "primary": prim}, "primary.json")
    for f, r in prim.items():
        print(f"{f:16s} {r['pct']*100:+6.1f}%  [{r['lo']*100:+.1f}, {r['hi']*100:+.1f}]  p={r['p']:.4f}  holm={r['p_holm']:.4f}  n_with={r.get('n_with','-')}")


if __name__ == "__main__":
    main()
