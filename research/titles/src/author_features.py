"""Paper-level author-experience covariates from exact declared-ID keys (no identity resolution).

Experience counts only submissions visible in this discovery export (~78-80% of each ICLR year),
and email-to-profile changes around 2021 break linkage, so these covariates are interpretable
from 2022 on. They are controls, not person-level ground truth.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from common import CACHE, load_submissions, read_table


def build() -> pd.DataFrame:
    s = load_submissions()[["submission_id", "year", "decision", "administrative_status"]]
    a = read_table("submission_authors")[["submission_id", "year", "source_list_position", "declared_id_key", "native_id_kind"]]
    a = a[a.declared_id_key.notna()].merge(s[["submission_id", "decision", "administrative_status"]], on="submission_id")
    a["accepted"] = (a.decision.eq("accepted") & a.administrative_status.eq("ordinary_submission")).astype(int)
    last_pos = a.groupby("submission_id").source_list_position.transform("max")
    a["role"] = np.where(a.source_list_position.eq(0), "first", np.where(a.source_list_position.eq(last_pos), "last", "middle"))

    # Per key and year: submissions and acceptances; cumulative counts strictly before each year.
    ky = a.groupby(["declared_id_key", "year"]).agg(n=("submission_id", "nunique"), acc=("accepted", "sum")).reset_index()
    ky = ky.sort_values(["declared_id_key", "year"])
    ky["prior_subs"] = ky.groupby("declared_id_key").n.cumsum() - ky.n
    ky["prior_accs"] = ky.groupby("declared_id_key").acc.cumsum() - ky.acc
    a = a.merge(ky[["declared_id_key", "year", "prior_subs", "prior_accs"]], on=["declared_id_key", "year"])

    g = a.groupby("submission_id")
    out = pd.DataFrame({
        "n_keys": g.declared_id_key.nunique(),
        "max_prior_subs": g.prior_subs.max(),
        "max_prior_accs": g.prior_accs.max(),
        "sum_prior_accs": g.prior_accs.sum(),
        "share_new_authors": g.prior_subs.apply(lambda x: float((x == 0).mean())),
        "profile_share": g.native_id_kind.apply(lambda x: float((x == "profile").mean())),
    })
    last = a[a.role.eq("last")].set_index("submission_id")
    first = a[a.role.eq("first")].set_index("submission_id")
    out["last_prior_subs"] = last.prior_subs.reindex(out.index)
    out["last_prior_accs"] = last.prior_accs.reindex(out.index)
    out["first_prior_subs"] = first.prior_subs.reindex(out.index)
    out = s[["submission_id", "year"]].merge(out, left_on="submission_id", right_index=True, how="left")
    for c in out.columns[2:]:
        if c.startswith(("max_", "sum_", "last_", "first_")):
            out[c] = out[c].fillna(0)
    out["any_prior_acc"] = (out.max_prior_accs > 0).astype(int)
    return out


if __name__ == "__main__":
    f = build()
    CACHE.mkdir(parents=True, exist_ok=True)
    f.to_parquet(CACHE / "author_features.parquet", index=False)
    print(f.groupby("year")[["max_prior_subs", "max_prior_accs", "any_prior_acc", "share_new_authors"]].mean().round(2))
