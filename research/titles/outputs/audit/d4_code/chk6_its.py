import numpy as np, pandas as pd
from analyses import _core as C
from analyses import d4_stage_gains as S
df = S.load_frame(density=False)
for pool in ["ACC", "REJ", "WD"]:
    d = S.its_design(df[df.pool.eq(pool)])
    res = C.logit(S.ITS_FORMULA.format(y="name_primary"), d, cluster="topic100")
    ct = d.groupby("topic100").name_primary.agg(["mean", "size"])
    print(pool, "method", res.mle_settings.get("optimizer"), "converged", res.mle_retvals.get("converged"),
          "post_t", round(res.params["post_t"], 4), "se", round(res.bse["post_t"], 4),
          "topics all-0/all-1:", int((ct["mean"] == 0).sum()), int((ct["mean"] == 1).sum()), "n topics", len(ct))
    # LPM check with topic FE
    r = C.feols(d, "name_primary", ["tc", "post", "post_t", "log_authors", "llm_topic"], fe=["topic100"], cluster="topic100")
    print("   LPM post_t", round(r.params["post_t"], 4), "se", round(r.se["post_t"], 4))
