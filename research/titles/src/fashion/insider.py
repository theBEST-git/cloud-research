"""Area insiders vs entrants: is the team already working near this paper's idea?

For each submission of year t >= 2020, take every earlier submission (year < t) that shares at least one declared
author key. team_prev_n = number of such submissions, team_area_cos = max cosine between this paper and any of them
(name-masked bge), team_area_acc = 1 if a team submission with cos >= 0.80 was accepted.
entry = 'newcomer' (no earlier ICLR submission), 'entrant' (earlier submissions, none within cos 0.80 = new area for
this team), 'insider' (an earlier submission within cos 0.80). Keys are declared IDs, not verified persons.
Writes outputs/fashion/insider.parquet.
"""
from __future__ import annotations

from collections import defaultdict

import numpy as np
import pandas as pd

from analyses import _core as C
from fashion.frame import _norm

TAU = 0.80


def main(min_year=2020):
    f = pd.read_parquet(C.OUT / "fashion" / "frame.parquet")[["submission_id", "year", "emb_row", "ACC"]]
    Em, found = C.load_masked_embedding(f)
    Ea = C.load_embedding(f, "abstract", "bge-small-en-v1.5")
    E = _norm(np.where(found[:, None], Em, Ea))
    a = pd.read_csv(C.DATA / "submission_authors.csv.gz", usecols=["submission_id", "declared_id_key"],
                    keep_default_na=False, na_values=[r"\N"]).dropna()
    a = a[a.submission_id.isin(f.submission_id)]
    idx = dict(zip(f.submission_id, range(len(f))))
    yr, acc = f.year.to_numpy(), f.ACC.to_numpy()
    by_key = defaultdict(list)
    for s, k in zip(a.submission_id, a.declared_id_key):
        by_key[k].append(idx[s])
    keys_of = a.groupby("submission_id").declared_id_key.apply(list).to_dict()
    rows = []
    for s, i in idx.items():
        if yr[i] < min_year:
            continue
        prior = {j for k in keys_of.get(s, []) for j in by_key[k] if yr[j] < yr[i]}
        if not prior:
            rows.append((s, 0, np.nan, 0))
            continue
        P = np.fromiter(prior, int)
        sims = E[P] @ E[i]
        rows.append((s, len(P), float(sims.max()), int((acc[P] & (sims >= TAU)).any())))
    r = pd.DataFrame(rows, columns=["submission_id", "team_prev_n", "team_area_cos", "team_area_acc"])
    r["entry"] = np.where(r.team_prev_n == 0, "newcomer", np.where(r.team_area_cos >= TAU, "insider", "entrant"))
    r.to_parquet(C.OUT / "fashion" / "insider.parquet")
    print(r.merge(f, on="submission_id").groupby(["year", "entry"]).size().unstack())


if __name__ == "__main__":
    main()
