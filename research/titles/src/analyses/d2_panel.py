"""WP6 / D2 panel: declared-key x paper rows, list-position partitions, stayer/exiter/entrant/returner groups,
team types, and the shared shift-share engine used by d2_shiftshare, d2_markers and d2_support.

Language (README boundaries): a declared profile key is an exact-ID key, not a verified person. "First" and
"last list position" are partition labels only; no seniority, supervision or influence is implied.

Panel definitions (PLAN D2):
  * main panel: native_id_kind == 'profile' keys, 2021-26, U papers only, one row per (key, paper).
  * email-era panel (H2e): native_id_kind == 'email' keys, 2017-20.
  * partitions: last list position (position == max position of the paper's full declared list), first list
    position (position 0), any role (every row, weight 1/#panel keys on the paper so each paper sums to 1).
    A paper whose last (first) position is not a panel key drops out of the last (first) partition.
  * groups for windows E (early) and L (late), defined at the key level from presence in ANY role:
      S stayers   = >= 1 paper in E and >= 1 in L
      X exiters   = in E, not in L
      N entrants  = in L, not in E, never seen in any panel year before L
      R returners = in L, not in E, but seen in a panel year before L outside E (2021 or 2024 for the main windows)
  * team types (paper level), share of the paper's panel keys that are "prior":
      rolling   prior = key seen (any role) in any panel year < paper year (lookback grows from 2021)
      fixed     prior = key seen in the base window 2021-22 (defined for papers 2023+)
      lag1      prior = key seen in year - 1 (fixed one-year lookback)
    type = all_prior (share 1), all_new (share 0), mixed.

Outputs (outputs/d2_carriers/):
  panel_rows.parquet, panel_papers.parquet, email_rows.parquet, panel_summary.csv, panel_keys_per_year.csv

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d2_panel
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from analyses import _core as C
from common import read_table

OUTDIR = C.OUT / "d2_carriers"
PANEL_YEARS = tuple(range(2021, 2027))
EMAIL_YEARS = tuple(range(2017, 2021))
E_WIN, L_WIN = (2022, 2023), (2025, 2026)
NAME_VARS = ["name_primary", "name_strict", "name_loose", "name_compound"]
SIZE_BINS = [0, 2, 3, 4, 5, 7, 10_000]
SIZE_LABELS = ["1-2", "3", "4", "5", "6-7", "8+"]


# --------------------------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------------------------
def load_papers(extra_feature_cols: list[str] | None = None) -> pd.DataFrame:
    feats = C.load_features()
    mk = [c for c in feats.columns if c.startswith("mk_")]
    fcols = list(dict.fromkeys(NAME_VARS + mk + ["name_orthography", "casing"] + (extra_feature_cols or [])))
    df = C.load_analysis_frame(
        feature_cols=fcols,
        universe_cols=["submission_id", "year", "topic50", "topic100", "llm_topic", "log_authors",
                       "declared_name_count", "NA", "ACC", "REJ", "WD", "DR", "pool"])
    for c in NAME_VARS + mk + ["llm_topic", "NA", "ACC", "REJ", "WD", "DR"]:
        df[c] = df[c].astype(int)
    df["size_bin"] = pd.cut(df.declared_name_count.clip(lower=1), SIZE_BINS, labels=SIZE_LABELS).astype(str)
    return df


def load_author_rows(papers: pd.DataFrame) -> pd.DataFrame:
    """All declared list positions of U papers with first/last flags from the FULL declared list."""
    a = read_table("submission_authors")[["submission_id", "year", "source_list_position", "native_id",
                                          "native_id_kind", "declared_id_key"]]
    a = a[a.submission_id.isin(set(papers.submission_id))].copy()
    pmax = a.groupby("submission_id").source_list_position.transform("max")
    a["is_first"] = a.source_list_position.eq(0)
    a["is_last"] = a.source_list_position.eq(pmax)
    a["list_len"] = pmax + 1
    return a


def make_panel(a: pd.DataFrame, kind: str, years: tuple[int, ...]) -> pd.DataFrame:
    """Rows of one key kind in the given years; one row per (key, paper); any-role weight 1/#keys."""
    p = a[a.native_id_kind.eq(kind) & a.year.isin(years) & a.declared_id_key.notna()].copy()
    # one row per (paper, key); a key listed twice keeps its first position but inherits first/last flags
    p = (p.sort_values(["submission_id", "source_list_position"])
         .groupby(["submission_id", "declared_id_key"], as_index=False)
         .agg(year=("year", "first"), pos=("source_list_position", "first"), native_id=("native_id", "first"),
              is_first=("is_first", "max"), is_last=("is_last", "max"), list_len=("list_len", "first")))
    p = p.rename(columns={"declared_id_key": "key"})
    p["n_pkeys"] = p.groupby("submission_id").key.transform("size")
    p["w_any"] = 1.0 / p.n_pkeys
    if kind == "profile":
        # alias collapse (upper bound on stayer status): ~First_Last1 / ~First_Last2 -> ~First_Last
        p["alias"] = p.native_id.fillna(p.key).str.replace(r"\d+$", "", regex=True)
    else:
        p["alias"] = p.key
    return p


# --------------------------------------------------------------------------------------------
# Groups
# --------------------------------------------------------------------------------------------
def key_groups(rows: pd.DataFrame, E: tuple[int, ...], L: tuple[int, ...], key: str = "key",
               years_universe: tuple[int, ...] | None = None) -> pd.DataFrame:
    """Key-level group flags for windows E and L from presence in any role (rows = the panel to use)."""
    yrs = rows[[key, "year"]].drop_duplicates()
    inE = set(yrs.loc[yrs.year.isin(E), key])
    inL = set(yrs.loc[yrs.year.isin(L), key])
    before_L = set(yrs.loc[(yrs.year < min(L)) & ~yrs.year.isin(E), key])
    keys = pd.Index(sorted(inE | inL), name=key)
    g = pd.DataFrame(index=keys)
    g["inE"] = g.index.isin(inE)
    g["inL"] = g.index.isin(inL)
    g["S"] = g.inE & g.inL
    g["X"] = g.inE & ~g.inL
    g["R"] = ~g.inE & g.inL & g.index.isin(before_L)
    g["N"] = ~g.inE & g.inL & ~g.index.isin(before_L)
    return g


def first_seen(rows: pd.DataFrame, key: str = "key") -> pd.Series:
    return rows.groupby(key).year.min()


# --------------------------------------------------------------------------------------------
# Team types
# --------------------------------------------------------------------------------------------
def team_types(rows: pd.DataFrame, base_years=(2021, 2022)) -> pd.DataFrame:
    """Paper-level prior-share and team type under the rolling, fixed-base and lag-1 definitions."""
    r = rows[["submission_id", "key", "year"]].copy()
    fy = first_seen(r)
    r["prior_roll"] = r.key.map(fy) < r.year
    base = set(r.loc[r.year.isin(base_years), "key"])
    r["prior_fixed"] = r.key.isin(base)
    ky = set(zip(r.key, r.year))
    r["prior_lag1"] = [(k, y - 1) in ky for k, y in zip(r.key, r.year)]
    g = r.groupby("submission_id").agg(year=("year", "first"), n_pkeys=("key", "size"),
                                       share_roll=("prior_roll", "mean"), share_fixed=("prior_fixed", "mean"),
                                       share_lag1=("prior_lag1", "mean"))
    for d in ["roll", "fixed", "lag1"]:
        s = g[f"share_{d}"]
        g[f"team_{d}"] = np.select([s.eq(1.0), s.eq(0.0)], ["all_prior", "all_new"], "mixed")
    g.loc[g.year < 2023, "team_fixed"] = np.nan  # base window overlaps; fixed definition only for 2023+
    g.loc[g.year <= min(PANEL_YEARS), ["team_roll", "team_lag1"]] = np.nan  # no lookback in the first panel year
    return g.reset_index()


def new_coauthor_share(rows: pd.DataFrame, definition: str = "roll") -> pd.Series:
    """For each (key, paper) row: share of the OTHER panel keys on the paper that are new.

    roll: new = first panel year of the key == paper year; lag1: new = key not seen in year - 1.
    Solo-key papers get 0 (no coauthors) and are flagged by n_pkeys == 1.
    """
    r = rows[["submission_id", "key", "year", "n_pkeys"]].copy()
    if definition == "roll":
        fy = first_seen(r)
        r["new"] = (r.key.map(fy) == r.year).astype(float)
    elif definition == "lag1":
        ky = set(zip(r.key, r.year))
        r["new"] = [float((k, y - 1) not in ky) for k, y in zip(r.key, r.year)]
    else:
        raise ValueError(definition)
    tot = r.groupby("submission_id").new.transform("sum")
    others = (r.n_pkeys - 1).astype(float)
    share = np.where(others > 0, (tot - r.new) / others.where(others > 0, 1.0), 0.0)
    return pd.Series(share, index=rows.index)


# --------------------------------------------------------------------------------------------
# Shift-share engine (vectorised; key-cluster bootstrap by multinomial key counts)
# --------------------------------------------------------------------------------------------
CELLS = ["SE", "XE", "SL", "NL", "RL"]


@dataclass
class Spec:
    """One decomposition: rows (with period E/L), a weight column, outcomes, key-level groups."""
    name: str
    rows: pd.DataFrame            # must contain: key_code, period ('E'/'L'), weight column, outcome columns
    weight: str
    outcomes: list[str]
    groups: pd.DataFrame          # indexed by key_code: S, X, N, R (bool)
    ipw: pd.Series | None = None  # key_code -> inverse-probability weight for stayers
    meta: dict = field(default_factory=dict)


def spec_matrix(spec: Spec, K: int) -> tuple[np.ndarray, list[str]]:
    """K x columns matrix of key-level sums: for each cell c: w_c, then y_c[outcome] (and IPW versions)."""
    r = spec.rows
    kc = r.key_code.to_numpy()
    w = r[spec.weight].to_numpy(float)
    per = r.period.to_numpy()
    g = spec.groups.reindex(np.arange(K)).fillna(False).astype(bool)
    cellmask = {
        "SE": (per == "E") & g.S.to_numpy()[kc],
        "XE": (per == "E") & g.X.to_numpy()[kc],
        "SL": (per == "L") & g.S.to_numpy()[kc],
        "NL": (per == "L") & g.N.to_numpy()[kc],
        "RL": (per == "L") & g.R.to_numpy()[kc],
    }
    ipw = None
    if spec.ipw is not None:
        ipw = spec.ipw.reindex(np.arange(K)).fillna(0.0).to_numpy(float)[kc]
    cols, names = [], []
    Y = r[spec.outcomes].to_numpy(float)
    for c in CELLS:
        m = cellmask[c].astype(float)
        cols.append(np.bincount(kc, weights=w * m, minlength=K)); names.append(f"w_{c}")
        for j, o in enumerate(spec.outcomes):
            cols.append(np.bincount(kc, weights=w * m * Y[:, j], minlength=K)); names.append(f"y_{c}_{o}")
        if ipw is not None and c in ("SE", "SL"):
            cols.append(np.bincount(kc, weights=w * m * ipw, minlength=K)); names.append(f"wi_{c}")
            for j, o in enumerate(spec.outcomes):
                cols.append(np.bincount(kc, weights=w * m * ipw * Y[:, j], minlength=K)); names.append(f"yi_{c}_{o}")
    return np.column_stack(cols).astype(np.float32), names


def shift_stats(T: np.ndarray, names: list[str], outcomes: list[str], has_ipw: bool = False) -> dict:
    """Decomposition statistics from (B x cols) totals (B may be 1). Returns {outcome: {stat: array(B)}}."""
    T = np.atleast_2d(T)
    ix = {n: i for i, n in enumerate(names)}
    col = lambda n: T[:, ix[n]]
    out = {}
    with np.errstate(divide="ignore", invalid="ignore"):
        for o in outcomes:
            w = {c: col(f"w_{c}") for c in CELLS}
            y = {c: col(f"y_{c}_{o}") for c in CELLS}
            P = {c: y[c] / w[c] for c in CELLS}
            WE, WL = w["SE"] + w["XE"], w["SL"] + w["NL"] + w["RL"]
            PE = (y["SE"] + y["XE"]) / WE
            PL = (y["SL"] + y["NL"] + y["RL"]) / WL
            sE, sL = w["SE"] / WE, w["SL"] / WL
            POL = (y["NL"] + y["RL"]) / (w["NL"] + w["RL"])
            D = PL - PE
            DS = P["SL"] - P["SE"]
            sbar = (sE + sL) / 2
            within = sbar * DS
            repl = (1 - sbar) * (POL - P["XE"])
            shift = (sL - sE) * ((P["SE"] + P["SL"]) / 2 - (P["XE"] + POL) / 2)
            PL_noR = (y["SL"] + y["NL"]) / (w["SL"] + w["NL"])
            d = dict(P_E=PE, P_L=PL, delta=D, P_SE=P["SE"], P_SL=P["SL"], P_XE=P["XE"], P_NL=P["NL"],
                     P_RL=P["RL"], P_OL=POL, s_E=sE, s_L=sL, delta_S=DS, rho=DS / D,
                     kit_within=within, kit_repl=repl, kit_shift=shift,
                     kit_within_share=within / D, kit_repl_share=repl / D, kit_shift_share=shift / D,
                     bound_a=sE * DS / D, bound_b=(sE * DS + (1 - sE) * (P["NL"] - P["XE"])) / D,
                     gap_NS_L=P["NL"] - P["SL"], gap_XS_E=P["XE"] - P["SE"], gap_RS_L=P["RL"] - P["SL"],
                     rho_noR=DS / (PL_noR - PE), delta_noR=PL_noR - PE,
                     share_R_in_L=w["RL"] / WL, share_N_in_L=w["NL"] / WL)
            if has_ipw:
                PSEi = col(f"yi_SE_{o}") / col("wi_SE")
                PSLi = col(f"yi_SL_{o}") / col("wi_SL")
                d.update(P_SE_ipw=PSEi, P_SL_ipw=PSLi, rho_ipw=(PSLi - PSEi) / D)
            out[o] = d
    return out


def cell_counts(spec: Spec) -> dict:
    """Row and key counts per cell (unweighted) for reporting."""
    r = spec.rows
    g = spec.groups
    out = {}
    for c, (per, grp) in {"SE": ("E", "S"), "XE": ("E", "X"), "SL": ("L", "S"), "NL": ("L", "N"),
                          "RL": ("L", "R")}.items():
        keys = set(g.index[g[grp]])
        m = r.period.eq(per) & r.key_code.isin(keys)
        out[f"rows_{c}"] = int(m.sum())
        out[f"keys_{c}"] = int(r.loc[m, "key_code"].nunique())
        out[f"wsum_{c}"] = float(r.loc[m, spec.weight].sum())
    return out


def run_specs(specs: list[Spec], K: int, n_boot: int = 1000, seed: int = 20260, chunk: int = 50) -> dict:
    """Point estimates and a joint key-cluster bootstrap (same key draws for every spec)."""
    mats, slices, start = [], {}, 0
    for s in specs:
        A, names = spec_matrix(s, K)
        mats.append(A)
        slices[s.name] = (start, start + A.shape[1], names)
        start += A.shape[1]
    A = np.hstack(mats)
    del mats
    point = A.sum(0, keepdims=True, dtype=np.float64)
    res = {}
    for s in specs:
        a, b, names = slices[s.name]
        res[s.name] = {"point": shift_stats(point[:, a:b], names, s.outcomes, s.ipw is not None),
                       "boot": None, "counts": cell_counts(s), "meta": s.meta}
    if n_boot:
        boots = {s.name: [] for s in specs}
        for W in C.boot_weights(K, n_boot, seed=seed, chunk=chunk):
            Tb = (W @ A).astype(np.float64)
            for s in specs:
                a, b, names = slices[s.name]
                boots[s.name].append(shift_stats(Tb[:, a:b], names, s.outcomes, s.ipw is not None))
        for s in specs:
            merged = {}
            for o in s.outcomes:
                merged[o] = {k: np.concatenate([bb[o][k] for bb in boots[s.name]]) for k in boots[s.name][0][o]}
            res[s.name]["boot"] = merged
    return res


def summarise(res: dict, stats=("rho", "delta", "delta_S", "P_E", "P_L", "P_SE", "P_SL", "P_XE", "P_NL", "P_RL",
                                 "s_E", "s_L", "kit_within_share", "kit_repl_share", "kit_shift_share", "bound_a",
                                 "bound_b", "gap_NS_L", "gap_XS_E", "rho_noR", "rho_ipw", "share_R_in_L")) -> pd.DataFrame:
    rows = []
    for name, r in res.items():
        for o, d in r["point"].items():
            for st in stats:
                if st not in d:
                    continue
                est = float(d[st][0])
                row = dict(spec=name, outcome=o, stat=st, est=est)
                if r["boot"] is not None:
                    b = r["boot"][o][st]
                    b = b[np.isfinite(b)]
                    if len(b) > 1:
                        row.update(se=float(np.std(b, ddof=1)), lo=float(np.quantile(b, .025)),
                                   hi=float(np.quantile(b, .975)), n_boot=int(len(b)))
                row.update({k: v for k, v in r["meta"].items() if isinstance(v, (str, int, float))})
                rows.append(row)
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------------------------
def build(write: bool = True) -> dict:
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    papers = load_papers()
    a = load_author_rows(papers)
    prof = make_panel(a, "profile", PANEL_YEARS)
    email = make_panel(a, "email", EMAIL_YEARS)
    tt = team_types(prof)
    papers = papers.merge(tt.drop(columns=["year"]), on="submission_id", how="left")
    papers["n_pkeys"] = papers.n_pkeys.fillna(0).astype(int)
    prof["share_new_coauth_roll"] = new_coauthor_share(prof, "roll")
    prof["share_new_coauth_lag1"] = new_coauthor_share(prof, "lag1")

    # --- coverage summary (V6-style) ---
    summ = []
    for y in range(2017, 2027):
        ay = a[a.year.eq(y)]
        py = papers[papers.year.eq(y)]
        pr = prof[prof.year.eq(y)] if y >= 2021 else email[email.year.eq(y)]
        kind = "profile" if y >= 2021 else "email"
        last_cov = ay[ay.is_last].native_id_kind.eq(kind).mean()
        first_cov = ay[ay.is_first].native_id_kind.eq(kind).mean()
        kp = pr.groupby("key").size()
        summ.append(dict(year=y, panel_kind=kind, papers_U=len(py), list_positions=len(ay),
                         panel_rows=len(pr), panel_keys=int(pr.key.nunique()),
                         papers_with_panel_key=int(pr.submission_id.nunique()),
                         share_last_pos_panel_key=round(float(last_cov), 4),
                         share_first_pos_panel_key=round(float(first_cov), 4),
                         papers_per_key_mean=round(float(kp.mean()), 3), papers_per_key_p99=float(kp.quantile(.99)),
                         papers_per_key_max=int(kp.max()), keys_over_40=int((kp > 40).sum())))
    summ = pd.DataFrame(summ)
    g = key_groups(prof, E_WIN, L_WIN)
    gsum = g[["S", "X", "N", "R"]].sum().to_dict()
    ga = key_groups(prof, E_WIN, L_WIN, key="alias")
    gasum = ga[["S", "X", "N", "R"]].sum().to_dict()
    info = dict(n_profile_rows=len(prof), n_profile_keys=int(prof.key.nunique()),
                n_alias_keys=int(prof.alias.nunique()), n_email_rows=len(email),
                n_email_keys=int(email.key.nunique()),
                groups_main={k: int(v) for k, v in gsum.items()}, groups_alias={k: int(v) for k, v in gasum.items()},
                elapsed_s=round(time.time() - t0, 1))
    if write:
        prof.to_parquet(OUTDIR / "panel_rows.parquet", index=False)
        email.to_parquet(OUTDIR / "email_rows.parquet", index=False)
        papers.to_parquet(OUTDIR / "panel_papers.parquet", index=False)
        summ.to_csv(OUTDIR / "panel_summary.csv", index=False)
        (OUTDIR / "panel_info.json").write_text(json.dumps(info, indent=1))
    print(summ.to_string())
    print(json.dumps(info, indent=1))
    return dict(papers=papers, prof=prof, email=email, summary=summ, info=info)


def load_panel() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """(papers, profile rows, email rows) as written by build()."""
    return (pd.read_parquet(OUTDIR / "panel_papers.parquet"), pd.read_parquet(OUTDIR / "panel_rows.parquet"),
            pd.read_parquet(OUTDIR / "email_rows.parquet"))


if __name__ == "__main__":
    build()
