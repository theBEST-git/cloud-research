"""WP7 / D3-H3a: meaning-fixed LLM title slots against control pairs (PLAN.md D3).

Frozen inventory. The slot words of lexicons.json (v2.0) minus the variants dropped by validation V2
(outputs/validation/slot_variants_dropped.json: exploit/unlocking, exploit/enabling, reveal/decoding). Dropping a word
removes it from its slot on both sides: a title opening with a dropped word counts as 'slot not filled'. The frozen
inventory is written to outputs/d3_register/slot_inventory.json before any model is fitted.

Opener rule (primary). PLAN D3 text: the title-opening gerund, after an optional "NAME:" lead (features_v2
`opener_word`). V2 found lower sense precision for titles that fill a slot only under the any-compound-lead rule
(0.83 vs 0.90), so the any-lead rule (`opener_word_al`, close to the pilot) is a robustness variant.

Models (2018+; SEs clustered by topic100):
    pooled slots     logit y ~ slot FE + slot x (t-2023) + post + llm_topic         -> post OR (H3a, pred >= 2)
    control pairs    same model on towards/toward, novel/new, via/using            -> post OR (pred in [0.67, 1.5])
    stacked          slots + controls with post + post x LLM-slot                   -> confirmatory parameter (CT4)
y = 1 for the LLM-favoured variant, 0 for the neutral variant. Robustness: topic100 FE, LPM, NA pool, non-LLM subset,
abstract-verb exclusion, leave-one-variant-out, opener position, excluding 2026, 2024-only, with 2017, unweighted V2
drop rule, no sense filter, log authors, bge topics, placebo break years with randomization p, year-level
random-effects meta-regression on slot x year cells (year shocks), per-slot estimates with BH, and the camera-ready
audit of opener-word flips among pre-decision arXiv v1 pairs.

Outputs (outputs/d3_register/):
    slot_inventory.json, slots_results.json, T3_1_slot_models.{csv,md}, slot_robustness.csv, slot_shares_by_year.csv,
    slot_loo.csv, slot_placebo_breaks.csv, slot_year_level.csv, slot_audit_flips.csv, slot_audit_pairs.csv,
    fig_F3_1_slot_shares.{pdf,png,csv}

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d3_slots
"""
from __future__ import annotations

import hashlib
import json
import time
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests

from analyses import _core as C
from analyses import features_v2 as FV

warnings.filterwarnings("ignore")
OUTDIR = C.OUT / "d3_register"
VALID = C.OUT / "validation"
SLOTS = ["improve", "reveal", "exploit", "study_adj"]
CTRLS = ["towards", "novel", "via"]
SLOT_LABEL = {"improve": "S-improve", "reveal": "S-reveal", "exploit": "S-exploit", "study_adj": "S-study-adj",
              "towards": "towards/toward", "novel": "novel/new", "via": "via/using"}
SEED = 20261011
BOOST_ALG = (r"\bboosting\s+(?:algorithms?|methods?|trees?|machines?|classifiers?|ensembles?)\b"
             r"|\bgradient\s+boosting\b|\badaboost\b")
POOLED = "y ~ C(slot) + C(slot):t + post + llm_topic"
STACKED = "y ~ C(slot) + C(slot):t + post + post:llm_slot + llm_topic"
BASE_COLS = ["submission_id", "year", "topic100", "topic100_bge", "log_authors", "llm_topic", "non_llm", "NA", "ACC",
             "pool", "opener_pos", "F_any", "f24", "f26", "title_typo", "name_primary", "n_words"]


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    return o


def write_json(obj, path: Path):
    path.write_text(json.dumps(jsonable(obj), indent=1))


# ------------------------------------------------------------------------------------------------
# Frozen inventory
# ------------------------------------------------------------------------------------------------
def frozen_inventory(rule: str = "weighted") -> dict:
    """Slot words after the V2 drops. rule='weighted' (primary, the V2 rule) or 'unweighted' (sensitivity)."""
    lx = FV.lexicon()["slots"]
    dv = json.loads((VALID / "slot_variants_dropped.json").read_text())
    drops = dv["dropped_words"] if rule == "weighted" else dv["sensitivity_unweighted_rule"]["dropped_words"]
    inv = {}
    for s in SLOTS:
        inv[s] = {side: [w for w in lx[s][side] if w not in set(drops.get(s, []))] for side in ("llm", "neutral")}
    return inv


def write_inventory() -> dict:
    lx = FV.lexicon()
    dv = json.loads((VALID / "slot_variants_dropped.json").read_text())
    inv = frozen_inventory("weighted")
    out = {
        "frozen_by": "analyses/d3_slots.py (WP7 / D3), before any D3 model was fitted",
        "lexicons_json_sha256": sha(Path(FV.__file__).parent / "lexicons.json"),
        "validation_file": "outputs/validation/slot_variants_dropped.json",
        "validation_file_sha256": sha(VALID / "slot_variants_dropped.json"),
        "v2_rule": dv["rule"],
        "inventory": inv,
        "dropped": [{k: d[k] for k in ("slot", "word", "variant", "precision_w", "n", "n_sense_y")}
                    for d in dv["dropped"]],
        "drop_semantics": "a title whose opener (or study adjective) is a dropped word counts as 'slot not filled'",
        "borderline_kept": dv["borderline_kept"],
        "sensitivity_unweighted_rule_inventory": frozen_inventory("unweighted"),
        "opener_rule_primary": "PLAN D3: first word of the title, or of the subtitle when the title is 'NAME: ...' "
                               "(features_v2 opener_word; name_primary lead). Robustness: any compound lead "
                               "(opener_word_al), title-start only, post-NAME only.",
        "opener_rule_reason": "PLAN text; V2 sense precision is lower (0.83 vs 0.90) for titles that fill a slot only "
                              "under the any-lead rule",
        "sense_filter": "pre-V2 heuristic filter kept for 'boosting' as the algorithm (lexicons.json "
                        "slot_sense_exclusions_preV2.boosting_algorithm); the 'decoding' filters are moot because "
                        "'decoding' is dropped",
        "study_adj": {"regex": lx["slots"]["study_adj"]["regex"], "llm": inv["study_adj"]["llm"],
                      "neutral": inv["study_adj"]["neutral"]},
        "control_pairs": lx["control_pairs"],
        "years": "2018+ (PLAN D3 slot logit); 2017 added as robustness",
    }
    OUTDIR.mkdir(parents=True, exist_ok=True)
    write_json(out, OUTDIR / "slot_inventory.json")
    return out


# ------------------------------------------------------------------------------------------------
# Data
# ------------------------------------------------------------------------------------------------
def load_frame() -> pd.DataFrame:
    feats = ["opener_word", "opener_word_al", "opener_pos", "slot_study_adj_word", "slot_word_in_abstract",
             "slot_study_adj_word_in_abstract", "ctrl_towards", "ctrl_novel", "ctrl_via", "name_primary", "F_any",
             "f24", "f24_2", "f24_words", "f24_n", "f26", "f26_words", "f26_typo", "title_typo", "n_words",
             "r24_any", "r26_any", "r24_n", "r26_n"] + \
            [f"slot_{s}{v}" for s in ("improve", "reveal", "exploit") for v in ("", "_raw", "_al")] + \
            ["slot_study_adj", "slot_study_adj_raw"] + \
            [f"r24_{w}" for w in ("enhanc", "leverag", "unveil", "unleash", "harness", "empower", "elevat", "boost")] + \
            [f"r26_{w}" for w in ("unified", "unifying", "beyond", "bridging")]
    ucols = ["submission_id", "year", "title", "title_nfkc", "abstract", "topic100", "log_authors", "llm_topic",
             "non_llm", "NA", "ACC", "REJ", "WD", "DR", "pool", "area_h", "area_short", "emb_row", "llm_regex"]
    df = C.load_analysis_frame(feature_cols=feats, universe_cols=ucols, with_bge_topics=True)
    for c in ["llm_topic", "non_llm", "NA", "ACC", "REJ", "WD", "DR", "name_primary", "F_any", "f24", "f24_2", "f26",
              "f26_words", "f26_typo", "title_typo", "r24_any", "r26_any", "llm_topic_bge"]:
        df[c] = df[c].astype(int)
    return df


def slot_y(df: pd.DataFrame, slot: str, inv: dict, rule: str = "primary", sense: bool = True):
    """(y, word) for one slot: y = 1 LLM-favoured, 0 neutral, NaN not filled (dropped words -> NaN)."""
    llm, neu = set(inv[slot]["llm"]), set(inv[slot]["neutral"])
    if slot == "study_adj":
        word = df.slot_study_adj_word.fillna("").astype(str)
    else:
        word = (df.opener_word if rule == "primary" else df.opener_word_al).fillna("").astype(str)
    y = pd.Series(np.where(word.isin(llm), 1.0, np.where(word.isin(neu), 0.0, np.nan)), index=df.index)
    if sense and slot != "study_adj":
        if rule == "primary":
            excl = df[f"slot_{slot}_raw"].notna() & df[f"slot_{slot}"].isna()
        else:
            excl = word.eq("boosting") & C.rx_contains(df.title_nfkc.fillna("").str.lower(), BOOST_ALG)
        y = y.where(~excl)
    return y, word.where(y.notna(), "")


def slot_panel(df: pd.DataFrame, inv: dict, rule: str = "primary", sense: bool = True, controls: bool = True,
               years_from: int = 2018) -> pd.DataFrame:
    """Long panel: one row per paper x filled slot (and per paper x control pair)."""
    rows = []
    cols = [c for c in BASE_COLS if c in df.columns]
    for s in SLOTS:
        y, w = slot_y(df, s, inv, rule, sense)
        m = y.notna()
        g = df.loc[m, cols].copy()
        g["y"], g["word"], g["slot"], g["llm_slot"] = y[m].astype(int), w[m], s, 1
        ia = df.slot_study_adj_word_in_abstract if s == "study_adj" else df.slot_word_in_abstract
        g["in_abs"] = ia[m] if rule == "primary" else np.nan
        rows.append(g)
    if controls:
        lx = FV.lexicon()["control_pairs"]
        for k in CTRLS:
            y = df[f"ctrl_{k}"]
            m = y.notna()
            g = df.loc[m, cols].copy()
            g["y"], g["slot"], g["llm_slot"], g["in_abs"] = y[m].astype(int), k, 0, np.nan
            g["word"] = np.where(g.y.eq(1), lx[k]["variant"], lx[k]["reference"])
            rows.append(g)
    P = pd.concat(rows, ignore_index=True)
    P = P[P.year >= years_from].copy()
    P["t"] = P.year - 2023
    P["post"] = (P.year >= 2024).astype(int)
    P["slot"] = P.slot.astype(str)  # plain strings: patsy then builds dummies for observed slots only
    return P.reset_index(drop=True)


# ------------------------------------------------------------------------------------------------
# Models
# ------------------------------------------------------------------------------------------------
def drop_nonvarying(P: pd.DataFrame, fe: str) -> pd.DataFrame:
    """Drop FE groups without outcome variation (they carry no information for the slope in a FE logit)."""
    v = P.groupby(fe, observed=True).y.transform("std").fillna(0)
    return P[v > 0]


def term_row(res, term: str, label: str, **extra) -> dict:
    t = C.or_table(res, [term]).iloc[0]
    z = t.coef / t.se
    return dict(label=label, term=term, coef=t.coef, se=t.se, OR=t.OR, OR_lo=t.OR_lo, OR_hi=t.OR_hi,
                p_two=2 * stats.norm.sf(abs(z)), p_one=stats.norm.sf(z), z=z, nobs=int(res.nobs),
                n_clusters=None, **extra)


def fit_set(P: pd.DataFrame, label: str, extra: str = "", fe: str | None = None, cluster: str = "topic100",
            stacked: bool = True, drop_llm_topic: bool = False) -> list[dict]:
    """Pooled-slot post OR, control post OR, and the stacked post x LLM-slot interaction for one panel."""
    out = []
    fml_pool, fml_stack = POOLED + extra, STACKED + extra
    if drop_llm_topic:
        fml_pool, fml_stack = fml_pool.replace(" + llm_topic", ""), fml_stack.replace(" + llm_topic", "")
    if fe:
        fml_pool += f" + C({fe})"
        fml_stack += f" + C({fe})"
    S = P[P.llm_slot == 1]
    Cc = P[P.llm_slot == 0]
    for nm, d, fml, term in [("slots_post", S, fml_pool, "post"), ("controls_post", Cc, fml_pool, "post"),
                             ("stacked_interaction", P, fml_stack, "post:llm_slot")]:
        if nm == "stacked_interaction" and not stacked:
            continue
        if len(d) == 0:
            continue
        dd = drop_nonvarying(d, fe) if fe else d
        try:
            r = C.logit(fml, dd, cluster=cluster)
            row = term_row(r, term, label, model=nm, n_post=int(dd.post.sum()),
                           n_slots=int(dd.slot.nunique()), share_post=float(dd.loc[dd.post == 1, "y"].mean()),
                           share_pre=float(dd.loc[dd.post == 0, "y"].mean()))
            row["n_clusters"] = int(dd[cluster].nunique())
            out.append(row)
        except Exception as e:  # noqa: BLE001
            out.append(dict(label=label, model=nm, error=str(e)[:200]))
    return out


def lpm_set(P: pd.DataFrame, label: str) -> list[dict]:
    """LPM version (slot FE, slot-specific trends, post, llm_topic; CRV1 by topic100)."""
    out = []
    for nm, d, xs in [("slots_post", P[P.llm_slot == 1], ["post"]), ("controls_post", P[P.llm_slot == 0], ["post"]),
                      ("stacked_interaction", P, ["post", "post_llm"])]:
        d = d.copy()
        d["post_llm"] = d.post * d.llm_slot
        tr = []
        for s in d.slot.unique():
            c = f"tr_{s}"
            d[c] = d.t * (d.slot == s)
            tr.append(c)
        d["slot_s"] = d.slot.astype(str)
        r = C.feols(d, "y", xs + tr + ["llm_topic"], fe=["slot_s"], cluster="topic100")
        term = xs[-1]
        b, se = float(r.params[term]), float(r.se[term])
        out.append(dict(label=label, model=nm, term=term, coef=b, se=se, pp=100 * b, pp_lo=100 * (b - 1.96 * se),
                        pp_hi=100 * (b + 1.96 * se), p_one=stats.norm.sf(b / se), p_two=2 * stats.norm.sf(abs(b / se)),
                        nobs=int(r.nobs), n_clusters=int(r.n_clusters)))
    return out


def per_slot(P: pd.DataFrame) -> pd.DataFrame:
    """Per-slot / per-control post effect: logit y ~ t + post + llm_topic; LPM when the pre period has < 30 titles."""
    rows = []
    for s in [s for s in SLOTS + CTRLS if s in set(P.slot.astype(str))]:
        d = P[P.slot.astype(str) == s]
        n_pre, n_post = int((d.post == 0).sum()), int(d.post.sum())
        base = dict(slot=s, label=SLOT_LABEL[s], llm_slot=int(d.llm_slot.iloc[0]), n=len(d), n_pre=n_pre,
                    n_post=n_post, share_pre=d.loc[d.post == 0, "y"].mean(), share_post=d.loc[d.post == 1, "y"].mean())
        if n_pre >= 30:
            r = C.logit("y ~ t + post + llm_topic", d, cluster="topic100")
            t = C.or_table(r, ["post"]).iloc[0]
            z = t.coef / t.se
            rows.append(dict(base, estimator="logit", coef=t.coef, se=t.se, OR=t.OR, OR_lo=t.OR_lo, OR_hi=t.OR_hi,
                             p_one=stats.norm.sf(z), p_two=2 * stats.norm.sf(abs(z))))
        else:
            r = C.feols(d, "y", ["t", "post", "llm_topic"], fe=None, cluster="topic100")
            b, se = float(r.params["post"]), float(r.se["post"])
            rows.append(dict(base, estimator="LPM (sparse pre period)", coef=b, se=se, pp=100 * b,
                             pp_lo=100 * (b - 1.96 * se), pp_hi=100 * (b + 1.96 * se), p_one=stats.norm.sf(b / se),
                             p_two=2 * stats.norm.sf(abs(b / se))))
    out = pd.DataFrame(rows)
    for fam in (1, 0):
        m = out.llm_slot == fam
        out.loc[m, "q_BH_one_sided"] = multipletests(out.loc[m, "p_one"], method="fdr_bh")[1]
        out.loc[m, "q_BH_two_sided"] = multipletests(out.loc[m, "p_two"], method="fdr_bh")[1]
    return out


def placebo_breaks(P: pd.DataFrame) -> pd.DataFrame:
    """Break at each candidate year (full 2018+ data) and pre-only placebos (2018-23 data)."""
    rows = []
    for scope, d0, years in [("full_2018_26", P, range(2020, 2026)), ("pre_only_2018_23", P[P.year <= 2023],
                                                                        range(2020, 2023))]:
        for B in years:
            d = d0.copy()
            d["post"] = (d.year >= B).astype(int)
            for r in fit_set(d, f"break_{B}"):
                r.update(scope=scope, break_year=B)
                rows.append(r)
            # stacked with year FE: common year shocks absorbed, only the slot-vs-control contrast breaks
            r = C.logit("y ~ C(slot) + C(slot):t + C(year) + post:llm_slot + llm_topic", d, cluster="topic100")
            r = term_row(r, "post:llm_slot", f"break_{B}", model="stacked_interaction_yearFE")
            r.update(scope=scope, break_year=B)
            rows.append(r)
    out = pd.DataFrame(rows)
    return out


def event_study(P: pd.DataFrame, years=(2023, 2024, 2025, 2026)) -> pd.DataFrame:
    """Year deviations from slot-specific linear trends fitted on 2018-2022: logit with year dummies for 2023-26.
    Slots and controls separately, and the slot-minus-control contrast (stacked, with year FE)."""
    d = P.copy()
    dn = []
    for y in years:
        d[f"d{y}"] = (d.year == y).astype(int)
        dn.append(f"d{y}")
    rows = []
    for nm, dd, fml, terms in [
            ("slots", d[d.llm_slot == 1], "y ~ C(slot) + C(slot):t + " + " + ".join(dn) + " + llm_topic", dn),
            ("controls", d[d.llm_slot == 0], "y ~ C(slot) + C(slot):t + " + " + ".join(dn) + " + llm_topic", dn),
            ("controls_without_via", d[(d.llm_slot == 0) & (d.slot != "via")],
             "y ~ C(slot) + C(slot):t + " + " + ".join(dn) + " + llm_topic", dn),
            ("slot_minus_control", d, "y ~ C(slot) + C(slot):t + C(year) + " +
             " + ".join(f"{x}:llm_slot" for x in dn) + " + llm_topic", [f"{x}:llm_slot" for x in dn]),
            ("slot_minus_control_without_via", d[d.slot != "via"], "y ~ C(slot) + C(slot):t + C(year) + " +
             " + ".join(f"{x}:llm_slot" for x in dn) + " + llm_topic", [f"{x}:llm_slot" for x in dn])]:
        r = C.logit(fml, dd, cluster="topic100")
        t = C.or_table(r, terms)
        for term, y in zip(terms, years):
            z = t.loc[term, "coef"] / t.loc[term, "se"]
            rows.append(dict(model=nm, year=y, OR=t.loc[term, "OR"], OR_lo=t.loc[term, "OR_lo"],
                             OR_hi=t.loc[term, "OR_hi"], p_two=2 * stats.norm.sf(abs(z)), nobs=int(r.nobs)))
    return pd.DataFrame(rows)


# ---- year-level inference: random-effects meta-regression on slot x year cells --------------------------------
def _gls(y, S, X):
    Si = np.linalg.inv(S)
    Vb = np.linalg.inv(X.T @ Si @ X)
    b = Vb @ X.T @ Si @ y
    return b, Vb


def _reml(y, V, X, Z):
    from scipy import optimize
    ZZ = Z @ Z.T

    def negll(lt):
        S = V + np.exp(lt) * ZZ
        Si = np.linalg.inv(S)
        XtSiX = X.T @ Si @ X
        b = np.linalg.solve(XtSiX, X.T @ Si @ y)
        r = y - X @ b
        return 0.5 * (np.linalg.slogdet(S)[1] + np.linalg.slogdet(XtSiX)[1] + r @ Si @ r)
    opt = optimize.minimize_scalar(negll, bounds=(-20, 2), method="bounded")
    return float(np.exp(opt.x))


def year_level(P: pd.DataFrame, min_n: int = 5) -> pd.DataFrame:
    """Cells = slot x year empirical logits (0.5 continuity; cells with n < min_n dropped). Model: slot FE + slot
    trends + post (+ post x LLM-slot) with a random shock per group x year (LLM slots vs controls), tau^2 by REML.
    Inference: t with df = #group-years - #group-year-level parameters."""
    g = P.groupby(["slot", "year"], observed=True).agg(k=("y", "sum"), n=("y", "size"),
                                                       llm=("llm_slot", "first")).reset_index()
    g = g[g.n >= min_n].copy()
    g["slot"] = g.slot.astype(str)
    g["el"] = np.log((g.k + 0.5) / (g.n - g.k + 0.5))
    g["v"] = 1 / (g.k + 0.5) + 1 / (g.n - g.k + 0.5)
    g["t"] = g.year - 2023
    g["post"] = (g.year >= 2024).astype(float)
    rows = []
    for nm, d in [("slots_post", g[g.llm == 1]), ("controls_post", g[g.llm == 0]), ("stacked_interaction", g)]:
        d = d.reset_index(drop=True)
        slots = sorted(d.slot.unique())
        Xs = [(d.slot == s).astype(float).to_numpy() for s in slots]
        Xt = [((d.slot == s) * d.t).astype(float).to_numpy() for s in slots]
        cols = Xs + Xt + [d.post.to_numpy()]
        if nm == "stacked_interaction":
            cols.append((d.post * d.llm).to_numpy())
        X = np.column_stack(cols)
        grp_year = d.llm.astype(str) + "_" + d.year.astype(str)
        Z = pd.get_dummies(grp_year).to_numpy(dtype=float)
        V = np.diag(d.v.to_numpy())
        y = d.el.to_numpy()
        tau2 = _reml(y, V, X, Z)
        b, Vb = _gls(y, V + tau2 * Z @ Z.T, X)
        b0, Vb0 = _gls(y, V, X)
        n_gy = Z.shape[1]
        n_grp = d.llm.nunique()
        dfree = max(n_gy - (2 * n_grp + (2 if nm == "stacked_interaction" else 1)), 1)
        se, se0 = float(np.sqrt(Vb[-1, -1])), float(np.sqrt(Vb0[-1, -1]))
        tq = stats.t.ppf(0.975, dfree)
        rows.append(dict(model=nm, n_cells=len(d), n_group_years=n_gy, df=dfree, tau=np.sqrt(tau2), coef=b[-1],
                         se=se, OR=np.exp(b[-1]), OR_lo=np.exp(b[-1] - tq * se), OR_hi=np.exp(b[-1] + tq * se),
                         p_one_t=stats.t.sf(b[-1] / se, dfree), coef_tau0=b0[-1], se_tau0=se0,
                         OR_tau0=np.exp(b0[-1])))
    return pd.DataFrame(rows)


# ------------------------------------------------------------------------------------------------
# Camera-ready audit: opener-word flips among pre-decision arXiv v1 pairs
# ------------------------------------------------------------------------------------------------
def audit(df: pd.DataFrame, inv: dict) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    import sys
    src = str(Path(__file__).resolve().parents[1])
    if src not in sys.path:
        sys.path.insert(0, src)
    from arxiv_audit import DECISION_DATE

    def read(p: Path, nmax=None):
        rows = []
        if not p.exists():
            return pd.DataFrame()
        with p.open() as fh:
            for i, line in enumerate(fh):
                if nmax is not None and i >= nmax:
                    break
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    continue
        return pd.DataFrame(rows)
    orig = read(C.CACHE / "arxiv_audit.jsonl")
    orig["source"] = "original"
    enl_path = C.CACHE / "arxiv_audit_enlarge.jsonl"
    n_enl_lines = sum(1 for _ in enl_path.open()) if enl_path.exists() else 0
    enl = read(enl_path, n_enl_lines)
    if len(enl):
        enl["source"] = "enlarge"
    rec = pd.concat([orig, enl], ignore_index=True)
    rec = rec.drop_duplicates("submission_id", keep="first")
    rec["usable"] = rec.found.astype(bool) & rec.v1_title.notna() & rec.v1_date.notna() & \
        (rec.v1_date.astype(str) < rec.year.map(DECISION_DATE).astype(str))
    p = rec[rec.usable].merge(df[["submission_id", "year", "title", "title_nfkc", "abstract"]],
                              on=["submission_id", "year"], how="inner").reset_index(drop=True)
    cols = ["submission_id", "year", "title", "title_nfkc", "abstract"]
    v1_in = p[["submission_id", "year", "abstract"]].copy()
    v1_in["title"] = p.v1_title.astype(str).map(lambda t: " ".join(t.split()))
    v1_in["title_nfkc"] = v1_in.title.map(C.nfkc)
    st = FV.build(p[cols].copy())
    v1 = FV.build(v1_in[cols])
    st["title_nfkc"], v1["title_nfkc"] = p.title_nfkc.values, v1_in.title_nfkc.values

    def state(fr):
        ys = {s: slot_y(fr, s, inv)[0] for s in SLOTS}
        Y = pd.DataFrame(ys)
        llm = (Y == 1).any(axis=1)
        neu = (Y == 0).any(axis=1)
        word = pd.Series([""] * len(fr), index=fr.index)
        for s in SLOTS:
            w = slot_y(fr, s, inv)[1]
            word = word.where(word != "", w)
        return np.where(llm, "llm", np.where(neu, "neutral", "none")), word
    s_or, w_or = state(st)
    s_v1, w_v1 = state(v1)
    pairs = p[["submission_id", "year", "decision", "source", "v1_date", "v1_title"]].copy()
    pairs["or_title"] = p.title
    pairs["state_v1"], pairs["state_or"] = s_v1, s_or
    pairs["word_v1"], pairs["word_or"] = w_v1.values, w_or.values
    pairs["r24_v1"], pairs["r24_or"] = v1.r24_any.astype(int).values, st.r24_any.astype(int).values
    pairs["acc"] = pairs.decision.eq("accepted").astype(int)
    pairs["llm_v1"], pairs["llm_or"] = (pairs.state_v1 == "llm").astype(int), (pairs.state_or == "llm").astype(int)
    pairs["filled_v1"] = (pairs.state_v1 != "none").astype(int)
    pairs["filled_or"] = (pairs.state_or != "none").astype(int)
    pairs["word_changed"] = (pairs.word_v1 != pairs.word_or).astype(int)
    rows = []
    for period, m in [("all", pairs.year >= 2022), ("2024-26", pairs.year >= 2024)]:
        for dec in ("accepted", "rejected"):
            d = pairs[m & pairs.decision.eq(dec)]
            rows.append(dict(period=period, decision=dec, n_pairs=len(d),
                             n_slot_filled_v1=int(d.filled_v1.sum()), n_slot_filled_or=int(d.filled_or.sum()),
                             n_llm_v1=int(d.llm_v1.sum()), n_llm_or=int(d.llm_or.sum()),
                             adds_llm=int(((d.llm_v1 == 0) & (d.llm_or == 1)).sum()),
                             drops_llm=int(((d.llm_v1 == 1) & (d.llm_or == 0)).sum()),
                             slot_word_changed=int(((d.filled_v1 + d.filled_or) > 0).mul(d.word_changed).sum()),
                             llm_to_neutral=int(((d.state_v1 == "llm") & (d.state_or == "neutral")).sum()),
                             neutral_to_llm=int(((d.state_v1 == "neutral") & (d.state_or == "llm")).sum()),
                             r24_adds=int(((d.r24_v1 == 0) & (d.r24_or == 1)).sum()),
                             r24_drops=int(((d.r24_v1 == 1) & (d.r24_or == 0)).sum()),
                             net_llm_per100=100 * (d.llm_or.mean() - d.llm_v1.mean()) if len(d) else np.nan))
    fl = pd.DataFrame(rows)
    # DiD of net LLM-slot adds (accepted - rejected), paper bootstrap stratified by year x decision
    rng = np.random.default_rng(SEED)
    did = {}
    for period, m in [("all", pairs.year >= 2022), ("2024-26", pairs.year >= 2024)]:
        d = pairs[m].reset_index(drop=True)
        net = (d.llm_or - d.llm_v1).to_numpy(float)
        acc = d.acc.to_numpy()
        est = net[acc == 1].mean() - net[acc == 0].mean()
        strata = (d.year.astype(str) + d.decision).to_numpy()
        bs = []
        for _ in range(2000):
            idx = C.boot_indices(len(d), strata=strata, rng=rng)
            a = acc[idx]
            bs.append(net[idx][a == 1].mean() - net[idx][a == 0].mean())
        lo, hi = np.quantile(bs, [0.025, 0.975])
        did[period] = dict(did_pp=100 * est, lo_pp=100 * lo, hi_pp=100 * hi, n_acc=int((acc == 1).sum()),
                           n_rej=int((acc == 0).sum()))
    meta = dict(n_original_records=len(orig), n_enlarge_lines_frozen=int(n_enl_lines), n_records=len(rec),
                n_usable_pairs=len(pairs), did_net_llm_adds=did)
    return pairs, fl, meta


# ------------------------------------------------------------------------------------------------
# Shares by year and figure F3.1
# ------------------------------------------------------------------------------------------------
def wilson(k, n, z=1.96):
    k, n = np.asarray(k, float), np.asarray(n, float)
    p = np.where(n > 0, k / np.maximum(n, 1), np.nan)
    den = 1 + z ** 2 / n
    c = (p + z ** 2 / (2 * n)) / den
    h = z * np.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / den
    return c - h, c + h


def shares_by_year(P: pd.DataFrame) -> pd.DataFrame:
    g = P.groupby(["slot", "year"], observed=True).y.agg(k="sum", n="size").reset_index()
    g["slot"] = g.slot.astype(str)
    pooled = P[P.llm_slot == 1].groupby("year").y.agg(k="sum", n="size").reset_index()
    pooled["slot"] = "pooled_slots"
    pc = P[P.llm_slot == 0].groupby("year").y.agg(k="sum", n="size").reset_index()
    pc["slot"] = "pooled_controls"
    g = pd.concat([g, pooled, pc], ignore_index=True)
    g["share"] = g.k / g.n
    g["lo"], g["hi"] = wilson(g.k, g.n)
    g["label"] = g.slot.map(SLOT_LABEL).fillna(g.slot)
    return g


def fig_f31(sh: pd.DataFrame, min_n: int = 10):
    import matplotlib.pyplot as plt  # noqa: F401
    fig, axes = C.new_fig("double", height=2.75, ncols=2, sharey=True)
    d = sh[(sh.n >= min_n) & (sh.year >= 2018)].copy()
    ax = axes[0]
    yrs = pd.Index(range(2018, 2027), name="year")
    for i, s in enumerate(SLOTS):
        g = d[d.slot == s].set_index("year").reindex(yrs).reset_index()  # NaN for years with n < min_n: line breaks
        ax.plot(g.year, g.share, color=C.color(i), marker="o", ms=5, lw=2, label=SLOT_LABEL[s])
        ax.fill_between(g.year, g.lo, g.hi, color=C.color(i), alpha=0.10, lw=0)
    ax.set_title("LLM slots: share using the LLM-favoured variant", loc="left", fontsize=9)
    ax.set_ylabel("share of slot-filled titles")
    ax2 = axes[1]
    styles = {"towards": "-", "novel": "--", "via": ":"}
    marks = {"towards": "o", "novel": "s", "via": "^"}
    for s in CTRLS:
        g = d[d.slot == s].set_index("year").reindex(yrs).reset_index()
        ax2.plot(g.year, g.share, color=C.GREY, ls=styles[s], marker=marks[s], ms=5, lw=2, label=SLOT_LABEL[s])
        last = g.dropna(subset=["share"]).iloc[-1]
        C.label_end(ax2, last.year, last.share, SLOT_LABEL[s].split("/")[0], C.TEXT2, dx=0.2, fontsize=7.5)
    ax2.set_title("Control pairs: share of towards, novel, via", loc="left", fontsize=9)
    for a in axes:
        a.axvspan(2023.5, 2026.4, color=C.GRID, alpha=0.45, lw=0, zorder=0)
        a.set_xticks(range(2018, 2027))
        a.set_xticklabels([str(y)[2:] if y not in (2018, 2026) else str(y) for y in range(2018, 2027)])
        a.set_xlim(2017.6, 2026.4 if a is axes[0] else 2027.3)
        a.set_ylim(0, 1.0)
        a.text(2023.6, 0.02 if a is axes[0] else 0.995, "post (2024+)", color=C.TEXT2, fontsize=7,
               va="bottom" if a is axes[0] else "top")
    axes[0].legend(loc="upper left", ncol=2, fontsize=7.5, handlelength=1.6, columnspacing=0.8)
    axes[1].legend(loc="lower right", bbox_to_anchor=(1.0, 0.02), ncol=1, fontsize=7, handlelength=2.6)
    fig.tight_layout()
    data = d[["slot", "label", "year", "k", "n", "share", "lo", "hi"]].sort_values(["slot", "year"])
    return C.save_fig(fig, "fig_F3_1_slot_shares", OUTDIR, data=data)


# ------------------------------------------------------------------------------------------------
def fmt_or(r):
    if "OR" in r and pd.notna(r.get("OR")):
        return f"{r['OR']:.2f} [{r['OR_lo']:.2f}, {r['OR_hi']:.2f}]"
    if "pp" in r and pd.notna(r.get("pp")):
        return f"{r['pp']:+.1f} pp [{r['pp_lo']:+.1f}, {r['pp_hi']:+.1f}]"
    return ""


def main():
    t0 = time.time()
    OUTDIR.mkdir(parents=True, exist_ok=True)
    inv_meta = write_inventory()
    inv = inv_meta["inventory"]
    inv_unw = inv_meta["sensitivity_unweighted_rule_inventory"]
    df = load_frame()
    P = slot_panel(df, inv)
    print("panel", P.groupby(["slot"], observed=True).size().to_dict(), "rows", len(P))

    # ---- primary
    prim = fit_set(P, "primary")
    prim_lpm = lpm_set(P, "primary (LPM)")
    for r in prim:
        print(f"  {r['model']:22s} {fmt_or(r)}  p1={r['p_one']:.2g} n={r['nobs']}")

    # ---- robustness panels
    rob = []

    def add(rows, family):
        for r in rows:
            r["family"] = family
            rob.append(r)
    add(prim, "primary")
    add(fit_set(P, "topic100 FE", fe="topic100"), "fixed effects")
    add(fit_set(P, "bge topic100 FE", fe="topic100_bge"), "fixed effects")
    add(fit_set(P, "+ log authors", extra=" + log_authors"), "controls")
    add(fit_set(P, "no llm_topic control", drop_llm_topic=True), "controls")
    add(fit_set(P[P.NA == 1], "NA pool (camera-ready-free)"), "pool")
    add(fit_set(P[P.ACC == 1], "accepted only"), "pool")
    add(fit_set(P[P.non_llm == 1], "non-LLM subset", drop_llm_topic=True), "subset")
    Pin = P[~((P.llm_slot == 1) & (P.in_abs == 1))]
    add(fit_set(Pin, "exclude titles whose abstract has the slot word"), "title-specific choice")
    Pst = P[(P.llm_slot == 0) | (P.slot.astype(str) == "study_adj") | (P.opener_pos == "start")]
    add(fit_set(Pst, "opener at title start only"), "opener position")
    Ppn = P[(P.llm_slot == 0) | (P.slot.astype(str) == "study_adj") | (P.opener_pos == "post_name")]
    add(fit_set(Ppn, "opener after NAME lead only", stacked=True), "opener position")
    Pal = slot_panel(df, inv, rule="al")
    add(fit_set(Pal, "any-compound-lead opener rule (pilot-like)"), "opener position")
    add(fit_set(P[P.year <= 2025], "excluding 2026"), "years")
    add(fit_set(P[P.year <= 2024], "2024-only post (2018-2024)"), "years")
    add(fit_set(slot_panel(df, inv, years_from=2017), "with 2017"), "years")
    add(fit_set(P[P.year != 2019], "without 2019"), "years")
    add(fit_set(slot_panel(df, inv_unw), "unweighted V2 drop rule (also drops unleashing)"), "inventory")
    add(fit_set(slot_panel(df, inv, sense=False), "no pre-V2 sense filter"), "inventory")
    lx = FV.lexicon()["slots"]
    inv_all = {s: {side: list(lx[s][side]) for side in ("llm", "neutral")} for s in SLOTS}
    add(fit_set(slot_panel(df, inv_all, sense=True), "full lexicon (no V2 drops)"), "inventory")
    add(fit_set(P[P.slot != "via"], "controls without via/using (towards, novel only)"), "controls")
    add(fit_set(P[P.slot != "novel"], "controls without novel/new"), "controls")
    add(fit_set(P[P.slot != "towards"], "controls without towards/toward"), "controls")
    Pno = P[P.slot.astype(str) != "study_adj"]
    add(fit_set(Pno, "opener slots only (no study_adj)"), "inventory")
    # no slot trends: simple pre/post with slot FE
    rows = []
    for nm, d, fml, term in [("slots_post", P[P.llm_slot == 1], "y ~ C(slot) + post + llm_topic", "post"),
                             ("controls_post", P[P.llm_slot == 0], "y ~ C(slot) + post + llm_topic", "post"),
                             ("stacked_interaction", P, "y ~ C(slot) + post + post:llm_slot + llm_topic",
                              "post:llm_slot")]:
        r = C.logit(fml, d, cluster="topic100")
        rows.append(term_row(r, term, "no slot trends (level contrast)", model=nm))
    add(rows, "trend specification")
    rows = []
    for nm, d, fml, term in [("slots_post", P[P.llm_slot == 1], "y ~ C(slot) + t + post + llm_topic", "post"),
                             ("controls_post", P[P.llm_slot == 0], "y ~ C(slot) + t + post + llm_topic", "post"),
                             ("stacked_interaction", P,
                              "y ~ C(slot) + t + t:llm_slot + post + post:llm_slot + llm_topic", "post:llm_slot")]:
        r = C.logit(fml, d, cluster="topic100")
        rows.append(term_row(r, term, "common trend per group", model=nm))
    add(rows, "trend specification")
    # stacked with year FE (absorbs year shocks common to slots and controls)
    r = C.logit("y ~ C(slot) + C(slot):t + C(year) + post:llm_slot + llm_topic", P, cluster="topic100")
    add([term_row(r, "post:llm_slot", "stacked with year FE", model="stacked_interaction")], "trend specification")
    add(lpm_set(P, "LPM"), "estimator")
    add(lpm_set(P[P.NA == 1], "LPM, NA pool"), "estimator")
    robdf = pd.DataFrame(rob)
    robdf.to_csv(OUTDIR / "slot_robustness.csv", index=False)

    # ---- leave-one-variant-out
    loo = []
    for s in SLOTS:
        for side in ("llm", "neutral"):
            for w in inv[s][side]:
                inv2 = json.loads(json.dumps(inv))
                inv2[s][side] = [x for x in inv2[s][side] if x != w]
                if not inv2[s]["llm"] or not inv2[s]["neutral"]:
                    continue
                Pd = slot_panel(df, inv2)
                for r in fit_set(Pd, f"drop {s}/{w}"):
                    if r["model"] == "controls_post":
                        continue
                    r.update(slot=s, word=w, side=side, n_dropped=int(len(P[P.llm_slot == 1]) -
                                                                      len(Pd[Pd.llm_slot == 1])))
                    loo.append(r)
    loo = pd.DataFrame(loo)
    loo.to_csv(OUTDIR / "slot_loo.csv", index=False)

    # ---- per slot + BH
    ps = per_slot(P)
    ps.to_csv(OUTDIR / "slot_per_slot.csv", index=False)

    # ---- placebo breaks + randomization p
    pb = placebo_breaks(P)
    pb.to_csv(OUTDIR / "slot_placebo_breaks.csv", index=False)
    full = pb[pb.scope == "full_2018_26"]
    rand = {}
    for nm in ("slots_post", "stacked_interaction", "stacked_interaction_yearFE"):
        f = full[full.model == nm].set_index("break_year")
        rand[nm] = dict(OR_by_break={int(k): float(v) for k, v in f.OR.items()},
                        z_by_break={int(k): float(v) for k, v in f.z.items()},
                        randomization_p_OR=float((f.OR >= f.OR.loc[2024]).mean()),
                        randomization_p_z=float((f.z >= f.z.loc[2024]).mean()),
                        argmax_OR=int(f.OR.idxmax()), n_candidates=len(f))
    pre = pb[pb.scope == "pre_only_2018_23"]

    # ---- event study (deviations from 2018-22 slot trends)
    es = event_study(P)
    es.to_csv(OUTDIR / "slot_event_study.csv", index=False)
    print(es.to_string())

    # ---- year-level
    yl = year_level(P)
    yl.to_csv(OUTDIR / "slot_year_level.csv", index=False)
    print(yl.to_string())

    # ---- shares and figure
    sh = shares_by_year(slot_panel(df, inv, years_from=2017))
    sh.to_csv(OUTDIR / "slot_shares_by_year.csv", index=False)
    fig_f31(sh)

    # ---- camera-ready audit
    pairs, flips, ameta = audit(df, inv)
    pairs.to_csv(OUTDIR / "slot_audit_pairs.csv", index=False)
    flips.to_csv(OUTDIR / "slot_audit_flips.csv", index=False)
    print(flips.to_string())
    print(ameta)

    # ---- T3.1
    get = {r["model"]: r for r in prim}
    t31 = []
    for nm, lab in [("slots_post", "Pooled LLM slots: post-2024 level shift"),
                    ("controls_post", "Pooled control pairs: post-2024 level shift"),
                    ("stacked_interaction", "Stacked: post x LLM-slot (slot minus control)")]:
        r = get[nm]
        t31.append(dict(block="A. Primary (logit, 2018-26, slot FE + slot trends + llm_topic)", row=lab,
                        estimate=fmt_or(r), p_one_sided=r["p_one"], n=r["nobs"], n_post=r.get("n_post"),
                        share_pre=r.get("share_pre"), share_post=r.get("share_post")))
    for _, r in ps.iterrows():
        t31.append(dict(block="B. Per slot / pair (logit y ~ t + post + llm_topic; LPM if < 30 pre titles)",
                        row=r.label, estimate=fmt_or(r.to_dict()), p_one_sided=r.p_one, q_BH=r.q_BH_one_sided,
                        n=r.n, n_post=r.n_post, share_pre=r.share_pre, share_post=r.share_post))
    for _, r in yl.iterrows():
        t31.append(dict(block="C. Year-level (REML meta-regression on slot x year cells, group-year shocks)",
                        row=r.model, estimate=f"{r.OR:.2f} [{r.OR_lo:.2f}, {r.OR_hi:.2f}]", p_one_sided=r.p_one_t,
                        n=r.n_cells, n_post=None))
    for lab in ["topic100 FE", "NA pool (camera-ready-free)", "non-LLM subset",
                "exclude titles whose abstract has the slot word", "any-compound-lead opener rule (pilot-like)",
                "excluding 2026", "2024-only post (2018-2024)", "stacked with year FE", "LPM"]:
        for _, r in robdf[robdf.label == lab].iterrows():
            t31.append(dict(block="D. Robustness", row=f"{lab}: {r.model}", estimate=fmt_or(r.to_dict()),
                            p_one_sided=r.p_one, n=r.nobs, n_post=r.get("n_post")))
    t31 = pd.DataFrame(t31)
    t31.to_csv(OUTDIR / "T3_1_slot_models.csv", index=False)
    md = ["| Block | Row | Estimate (OR [95% CI] or pp) | one-sided p | BH q | n | n post |", "|---|---|---|---|---|---|---|"]
    for _, r in t31.iterrows():
        q = "" if pd.isna(r.get("q_BH")) else f"{r.q_BH:.3g}"
        npost = "" if pd.isna(r.n_post) else f"{int(r.n_post):,}"
        md.append(f"| {r.block} | {r.row} | {r.estimate} | {r.p_one_sided:.3g} | {q} | {int(r.n):,} | {npost} |")
    (OUTDIR / "T3_1_slot_models.md").write_text("\n".join(md) + "\n")

    # ---- verdict inputs for H3a
    sp, cp, si = get["slots_post"], get["controls_post"], get["stacked_interaction"]
    verdict = dict(
        pooled_OR_ge_2=bool(sp["OR"] >= 2), pooled_CI_excludes_1=bool(sp["OR_lo"] > 1),
        control_OR_in_067_15=bool(0.67 <= cp["OR"] <= 1.5),
        control_CI_inside_067_15=bool(cp["OR_lo"] >= 0.67 and cp["OR_hi"] <= 1.5),
        stacked_diff_gt0=bool(si["coef"] > 0), stacked_CI_excludes_0=bool(si["OR_lo"] > 1),
        falsified=bool(sp["OR_lo"] <= 1 or si["OR_lo"] <= 1),
        p_H3a_intersection_union=float(max(sp["p_one"], si["p_one"])))
    res = dict(
        hypothesis="H3a", inventory=inv, n_panel_rows=len(P),
        n_by_slot={k: int(v) for k, v in P.groupby("slot", observed=True).size().items()},
        n_slot_titles_2018plus=int((P.llm_slot == 1).sum()),
        n_slot_papers_2018plus=int(P.loc[P.llm_slot == 1, "submission_id"].nunique()),
        primary={r["model"]: r for r in prim}, primary_lpm={r["model"]: r for r in prim_lpm},
        per_slot=ps.to_dict(orient="records"), randomization=rand,
        placebo_pre_only=pre[["break_year", "model", "OR", "OR_lo", "OR_hi", "p_one"]].to_dict(orient="records"),
        year_level=yl.to_dict(orient="records"), event_study=es.to_dict(orient="records"),
        robustness=robdf.to_dict(orient="records"),
        loo_summary=dict(
            slots_post_OR_min=float(loo[loo.model == "slots_post"].OR.min()),
            slots_post_OR_max=float(loo[loo.model == "slots_post"].OR.max()),
            slots_post_min_word=loo[loo.model == "slots_post"].sort_values("OR").iloc[0][["slot", "word"]].tolist(),
            stacked_OR_min=float(loo[loo.model == "stacked_interaction"].OR.min()),
            stacked_OR_max=float(loo[loo.model == "stacked_interaction"].OR.max()),
            all_slots_CI_excl_1=bool((loo[loo.model == "slots_post"].OR_lo > 1).all()),
            all_stacked_CI_excl_1=bool((loo[loo.model == "stacked_interaction"].OR_lo > 1).all())),
        audit=dict(meta=ameta, flips=flips.to_dict(orient="records")),
        verdict_inputs=verdict, runtime_s=round(time.time() - t0, 1))
    write_json(res, OUTDIR / "slots_results.json")
    print("verdict", verdict, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
