"""WP8 / D4: published-only bias atlas (H4e), Kobak-style LLM bounds accepted vs all (H4c) and the decision-stage
bound from the arXiv camera-ready audit (T4.2).

(1) Decision-stage bound (snapshot module; D4's own copy of the flip tables, on the SAME pair sample as WP4).
    Integration pass: the pairs are WP4's frozen primary audit (outputs/snapshot/audit_pairs.csv: original audit +
    complete enlargement, 2023-26 pre-decision pairs, 803 accepted / 508 rejected; freeze hash in
    outputs/snapshot/results.json -> meta.audit_freeze). The original 331-pair audit (cache/arxiv_audit.jsonl,
    2022-26) is kept as the sensitivity spec 'original audit only'. Primary DiD CI = WP4's Wald with a pseudo-flip
    variance floor (one pseudo-add and one pseudo-drop per arm); plain Wald and bootstrap CIs reported alongside.
    Auditable = WP4's canonical rule: >= 10 v1-present titles in BOTH arms and measurable through arXiv metadata
    (arXiv titles are never ALL-CAPS and never carry U+2011/U+2013 typography, so ALL-CAPS title, title typography
    and the unions containing them are channel-unauditable). D4's interim rule is kept as auditable_d4rule.
    Pairs: audit rows found on arXiv whose v1 predates the ICLR decision date (arxiv_audit.DECISION_DATE).
    Title features are computed with features_v2.build on the v1 title and on the stored title (same abstract).
    Per feature and decision: flip matrix (v1 x stored), adds, drops, feature-present v1 denominators, net flip
    rate (adds - drops)/n. Net-flip DiD = accepted - rejected (the rejected rate is the pre-ICLR retitling noise
    floor). Pseudo-flip Wald (primary), plain Wald and bootstrap (2,000, stratified by decision) CIs.
    Editing-corrected prevalences: accepted papers sit in every stage set, so a camera-ready net addition D
    shifts P(f|s_k) by D * a_k (a_k = accepted share of s_k). Selection-only gains: G(D) = (P3 - D)/(P_k - a_k D).
    Tipping points: D*_dec = (P3 - P2)/(1 - a2), D*_total = (P3 - P0)/(1 - a0). G_dec is "identified" only if the
    tipping point lies beyond the audit's 95% CI on the side that would move G to 1.
(2) H4c: Kobak-style lower bound on LLM-styled abstracts (any RARE21 word = F24): bound_Y = p_Y - q_Y with the
    conservative baseline q_Y = max(OLS line through 2021-23 extrapolated to Y (floored at 0), max(p2022, p2023)),
    computed separately within each set (all = s0, s1, s2, accepted = s3, NA pool, REJ). Ratio accepted/all per
    year, bootstrap CIs (2,000, stratified by year). Robustness: other marker sets and baselines.
(3) H4e atlas: pre-registered fashion statistics computed on each stage set s0..s3 (2024-26 unless stated):
    M  prevalence of NAME, compound, phrase colon, mixed-case name, Title Case (year-standardised);
       ITS slope-change OR for NAME (D1 spec, 2018-26); colon premium (acceptance OR of compound titles, 2024-26,
       decided-only s2 vs all s0: a premium cannot be computed on accepted papers alone) and its trend
       (compound x year, 2018-26); LLM abbreviation-only share (among titles naming language models; a naming
       fashion, classed M); snowclone share (d4_lexicon snowclones); name-collapsed opener entropy (first title
       word, NAME leads collapsed to one token; exact expected plug-in entropy under rarefaction to the accepted
       n of each year, mean over 2024-26); lexical-turnover JSD (title word distribution year y vs y-1, rarefied
       to the accepted n of both years, mean over 2024-26); peak years of the top-30 title fashions (2018-26).
    O  prevalence of ALL-CAPS title, sentence case, question opener, O-union.
    L  prevalence of title typography, R24, R26, F24, F26, abstract em dash, style density, L-union;
       RARE21 Kobak bound (mean 2024-26).
    Gap = log(T(s3)/T(s0)) = desk + exit + decision parts (log ratios between consecutive stage sets). The desk and
    exit parts compare the submission-stage text of exiting papers with survivor sets that still contain accepted,
    camera-ready text, so they are not pure selection; camera-ready-free versions (accepted papers removed from
    every stage set) are reported alongside (log_desk_crf, log_exit_crf). For auditable title features the audit
    DiD gives the editing interval implied by its CI; no decision split is identified, so the figure draws every
    decision part as 'not separable'. The +/-10% criterion is applied on the effect scale: prevalence/mean
    statistics as ratios, OR statistics as ratios of log-ORs (delta-method CI from the joint IF covariance). The
    pre-registered colon-premium trend (decided-only analogue) enters the M count; the level is supplementary.
    Entropy/JSD intervals are random-selection null bands (not CIs). BH q-values over all atlas tests.

Outputs (outputs/d4_filter/): audit_pairs.csv, T4_2_audit_flips.csv, T4_2_decision_bound.csv, kobak_bounds.csv,
kobak_series.csv, atlas.csv, atlas_peaks.csv, bias_atlas.json, fig_F4_2_bias_atlas.*, fig_F4_3_kobak_bounds.*,
d4_bias_atlas.log

Run:  cd research/titles/src && OMP_NUM_THREADS=2 /home/user/venv/bin/python -m analyses.d4_bias_atlas
"""
from __future__ import annotations

import json
import re
import sys
import time
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse, stats

from analyses import _core as C
from analyses import d4_stage_gains as S

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from arxiv_audit import DECISION_DATE  # noqa: E402

OUTDIR = S.OUTDIR
POST = S.POST
N_BOOT = S.N_BOOT
N_NULL = 1000
SEED = S.SEED + 1
AUDIT_PATH = C.CACHE / "arxiv_audit.jsonl"
WP4_PAIRS = C.OUT / "snapshot" / "audit_pairs.csv"     # WP4 frozen primary audit (integration pass)
WP4_FLIPS = C.OUT / "snapshot" / "T4_2_flip_matrices.csv"
MIN_AUDIT_N = 10
Z95 = 1.959963984540054
# arXiv metadata cannot carry these (WP4 channel check: 0 of ~3,600 arXiv titles are ALL-CAPS or typographic)
CHANNEL_UNAUDITABLE = {"all_caps_title", "title_typo", "O_union", "L_title"}

AUDIT_FEATURES = [
    ("NAME", "name_primary"), ("compound", "name_compound"), ("phrase_colon", "phrase_colon"),
    ("mixed_case_name", "ortho_mixed_case"), ("title_case", "case_title_case"), ("all_caps_title", "case_all_caps"),
    ("sentence_case", "case_sentence_case"), ("question_opener", "question_opener"), ("O_union", "O_union"),
    ("title_typo", "title_typo"), ("R24", "r24_any"), ("R26", "r26_any"), ("L_title", "L_title"),
    ("NAME_strict", "name_strict"), ("NAME_loose", "name_loose"), ("allcaps_name", "ortho_all_caps"),
    ("snowclone", "snowclone"), ("llm_abbrev_only", "llm_t_abbrev_only"),
]


def log(msg, fh=None):
    S.log(msg, fh)


def snowclone_col(df: pd.DataFrame) -> pd.Series:
    cols = [f"tpl_{k}" for k in S.lexicon()["snowclones"]]
    return df[cols].astype(int).max(axis=1)


# --------------------------------------------------------------------------------------------
# (1) Audit
# --------------------------------------------------------------------------------------------
def audit_pairs(source: str = "complete") -> pd.DataFrame:
    """source='complete': WP4's frozen primary pairs (original + complete enlargement, 2023-26);
    source='original': the original 331-pair audit (cache/arxiv_audit.jsonl, 2022-26), D4's pre-integration copy."""
    from analyses import features_v2 as FV
    u = C.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract"])
    if source == "complete":
        d = pd.read_csv(WP4_PAIRS, dtype={"submission_id": str, "arxiv_id": str},
                        usecols=["submission_id", "year", "decision", "v1_title", "v1_date", "arxiv_id", "or_title",
                                 "source"])
        p = d.merge(u, on=["submission_id", "year"], how="inner", validate="1:1")
        assert len(p) == len(d), "WP4 audit pairs missing from the universe"
    else:
        d = pd.read_json(AUDIT_PATH, lines=True, dtype={"submission_id": str})
        d["pre"] = d.found.astype(bool) & d.v1_date.notna() & d.v1_title.notna() & \
            (d.v1_date.astype(str) < d.year.map(DECISION_DATE))
        d["source"] = "original"
        p = d[d.pre].merge(u, on=["submission_id", "year"], how="inner", validate="1:1")
    assert (p.or_title == p.title).all(), "audit or_title differs from universe title"
    p = p.reset_index(drop=True)
    stored = FV.build(p[["submission_id", "year", "title", "title_nfkc", "abstract"]])
    v1in = p[["submission_id", "year", "abstract"]].copy()
    v1in["title"] = p.v1_title.astype(str)
    v1in["title_nfkc"] = v1in.title.map(C.nfkc)
    v1 = FV.build(v1in[["submission_id", "year", "title", "title_nfkc", "abstract"]])
    out = p[["submission_id", "year", "decision", "or_title", "v1_title", "v1_date", "arxiv_id", "source"]].copy()
    for frame, tag in [(stored, "or"), (v1, "v1")]:
        fr = frame.copy()
        fr["O_union"] = fr[["case_all_caps", "case_sentence_case", "question_opener"]].max(axis=1)
        fr["L_title"] = fr[["title_typo", "r24_any", "r26_any"]].max(axis=1)
        fr["snowclone"] = snowclone_col(fr)
        for k, c in AUDIT_FEATURES:
            out[f"{k}_{tag}"] = fr[c].astype(int).to_numpy()
    out["acc"] = out.decision.eq("accepted").astype(int)
    norm = lambda t: re.sub(r"[^a-z0-9]+", " ", str(t).lower()).strip()  # noqa: E731
    out["title_changed"] = (out.v1_title.map(norm) != out.or_title.map(norm)).astype(int)
    return out


def flip_table(pairs: pd.DataFrame, weights: np.ndarray | None = None, label: str = "primary",
               n_boot: int = N_BOOT) -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    w_all = np.ones(len(pairs)) if weights is None else np.asarray(weights, float)
    rows = []
    acc = pairs.acc.to_numpy() == 1
    idx_a, idx_r = np.where(acc)[0], np.where(~acc)[0]
    boots = [(rng.integers(0, len(idx_a), (n_boot, len(idx_a))), rng.integers(0, len(idx_r), (n_boot, len(idx_r))))]
    ba, br = boots[0]
    for k, _ in AUDIT_FEATURES:
        v1 = pairs[f"{k}_v1"].to_numpy()
        orr = pairs[f"{k}_or"].to_numpy()
        net = (orr - v1).astype(float)
        r = dict(spec=label, feature=k)
        for g, m in [("acc", acc), ("rej", ~acc)]:
            w = w_all[m]
            r[f"n_{g}"] = int(m.sum())
            r[f"v1_present_{g}"] = int(v1[m].sum())
            r[f"or_present_{g}"] = int(orr[m].sum())
            r[f"stay0_{g}"] = int(((v1[m] == 0) & (orr[m] == 0)).sum())
            r[f"adds_{g}"] = int(((v1[m] == 0) & (orr[m] == 1)).sum())
            r[f"drops_{g}"] = int(((v1[m] == 1) & (orr[m] == 0)).sum())
            r[f"stay1_{g}"] = int(((v1[m] == 1) & (orr[m] == 1)).sum())
            r[f"drop_rate_{g}"] = r[f"drops_{g}"] / r[f"v1_present_{g}"] if r[f"v1_present_{g}"] else np.nan
            r[f"add_rate_{g}"] = r[f"adds_{g}"] / (r[f"n_{g}"] - r[f"v1_present_{g}"]) \
                if r[f"n_{g}"] > r[f"v1_present_{g}"] else np.nan
            mu = float(np.sum(w * net[m]) / np.sum(w))
            r[f"net_{g}"] = mu
            # weighted variance of the mean (Kish effective n)
            neff = np.sum(w) ** 2 / np.sum(w ** 2)
            var = float(np.sum(w * (net[m] - mu) ** 2) / np.sum(w))
            r[f"net_se_{g}"] = float(np.sqrt(var / max(neff - 1, 1)))
            # WP4 pseudo-flip variance floor (one pseudo-add and one pseudo-drop per arm; snapshot_bounds._arm_stats)
            sw = np.sum(w)
            pa = float(np.sum(w * ((v1[m] == 0) & (orr[m] == 1))) / sw)
            pdr = float(np.sum(w * ((v1[m] == 1) & (orr[m] == 0))) / sw)
            Ns = neff + 2
            pa_s, pd_s = (pa * neff + 1) / Ns, (pdr * neff + 1) / Ns
            r[f"net_var_pf_{g}"] = max((pa_s + pd_s - (pa_s - pd_s) ** 2) / Ns, r[f"net_se_{g}"] ** 2)
        r["did"] = r["net_acc"] - r["net_rej"]
        r["did_se_wald"] = float(np.hypot(r["net_se_acc"], r["net_se_rej"]))
        r["did_lo95_wald"], r["did_hi95_wald"] = r["did"] - Z95 * r["did_se_wald"], r["did"] + Z95 * r["did_se_wald"]
        # primary (WP4 convention): pseudo-flip Wald
        r["did_se"] = float(np.sqrt(r.pop("net_var_pf_acc") + r.pop("net_var_pf_rej")))
        r["did_lo95"], r["did_hi95"] = r["did"] - Z95 * r["did_se"], r["did"] + Z95 * r["did_se"]
        na, nr = net[idx_a], net[idx_r]
        wa, wr = w_all[idx_a], w_all[idx_r]
        bd = (np.sum(wa[ba] * na[ba], 1) / np.sum(wa[ba], 1)) - (np.sum(wr[br] * nr[br], 1) / np.sum(wr[br], 1))
        r["did_boot_lo95"], r["did_boot_hi95"] = float(np.quantile(bd, .025)), float(np.quantile(bd, .975))
        r["auditable_d4rule"] = bool(r["v1_present_acc"] >= MIN_AUDIT_N and r["or_present_acc"] >= MIN_AUDIT_N)
        r["channel_ok"] = k not in CHANNEL_UNAUDITABLE
        r["auditable"] = bool(min(r["v1_present_acc"], r["v1_present_rej"]) >= MIN_AUDIT_N and r["channel_ok"])
        rows.append(r)
    return pd.DataFrame(rows)


def ipw_weights(pairs: pd.DataFrame, years=(2023, 2024, 2025, 2026)) -> tuple[pd.DataFrame, np.ndarray]:
    """Population weights N_pop(year, decision) / n_pairs(year, decision) (acceptance population counts)."""
    u = C.load_universe(["year", "ACC", "REJ"])
    pop = {(y, "accepted"): int(u[(u.year == y) & u.ACC].shape[0]) for y in years}
    pop.update({(y, "rejected"): int(u[(u.year == y) & u.REJ].shape[0]) for y in years})
    p = pairs[pairs.year.isin(years)].reset_index(drop=True)
    cnt = p.groupby(["year", "decision"]).size()
    w = np.array([pop[(y, dd)] / cnt[(y, dd)] for y, dd in zip(p.year, p.decision)], float)
    return p, w / w.mean()


# --------------------------------------------------------------------------------------------
# (2) Kobak bounds
# --------------------------------------------------------------------------------------------
KOBAK_SETS = ["s0", "s1", "s2", "s3", "NAp", "REJp"]
KOBAK_LABEL = {"s0": "all submissions", "s1": "not desk-rejected", "s2": "reviewed (s2)", "s3": "accepted",
               "NAp": "NA pool", "REJp": "rejected"}


def kobak_from_prev(P: dict, Y: int, baseline: str = "cons") -> np.ndarray:
    """P: year -> array of prevalences (any shape). Returns bound for target year Y."""
    x = np.array([2021, 2022, 2023], float)
    B = np.stack([P[2021], P[2022], P[2023]], axis=-1)
    xm = x.mean()
    slope = ((x - xm) * (B - B.mean(-1, keepdims=True))).sum(-1) / ((x - xm) ** 2).sum()
    lin = np.clip(B.mean(-1) - slope * xm + slope * Y, 0, None)
    m23 = np.maximum(P[2022], P[2023])
    # max2122: post hoc sensitivity (not pre-registered): ICLR 2023 camera-ready abstracts were finalised after
    # ChatGPT's release (30 Nov 2022), so the accepted 2023 baseline may itself contain LLM edits.
    q = {"cons": np.maximum(lin, m23), "lin": lin, "max23": m23,
         "max2122": np.maximum(P[2021], P[2022])}[baseline]
    return P[Y] - q


def kobak(df: pd.DataFrame, cols: dict[str, str], n_boot: int = N_BOOT) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    d = df[df.year >= 2021].copy()
    d["NAp"] = d.NA
    d["REJp"] = d.REJ | d.wd_post  # wd_post rows are rejected papers withdrawn after the decision
    keys = list(cols)
    for k, c in cols.items():
        if c not in d:
            raise KeyError(c)
    sums = S.stage_sums(d.assign(**{f"__{k}": d[c] for k, c in cols.items()}), [f"__{k}" for k in keys], KOBAK_SETS,
                        n_boot=n_boot, seed=SEED)
    P = {y: sums[y][0] / sums[y][1][:, None, :] for y in sums}  # (B+1, F, K)
    rows, series = [], []
    boot = {}
    for bl in ["cons", "lin", "max23", "max2122"]:
        for Y in POST:
            Bd = kobak_from_prev(P, Y, bl)  # (B+1, F, K)
            boot[(bl, Y)] = Bd
            for j, k in enumerate(keys):
                for si, s in enumerate(KOBAK_SETS):
                    smr = S.summarise(Bd[:, j, si])
                    rows.append(dict(marker=k, baseline=bl, year=Y, set=s, bound=smr["est"], lo95=smr["lo95"],
                                     hi95=smr["hi95"], se=smr["se"], p_Y=float(P[Y][0, j, si]),
                                     basic_lo95=2 * smr["est"] - smr["hi95"], basic_hi95=2 * smr["est"] - smr["lo95"],
                                     n_Y=float(sums[Y][1][0, si])))
                ratio = Bd[:, j, KOBAK_SETS.index("s3")] / Bd[:, j, KOBAK_SETS.index("s0")]
                smr = S.summarise(ratio)
                rows.append(dict(marker=k, baseline=bl, year=Y, set="ratio_acc_all", bound=smr["est"],
                                 lo95=smr["lo95"], hi95=smr["hi95"], se=smr["se"], p_le1=smr["p_le1"],
                                 p_ge1=smr["p_ge1"], basic_lo95=2 * smr["est"] - smr["hi95"],
                                 basic_hi95=2 * smr["est"] - smr["lo95"],
                                 p_ge_0p9=float(np.mean(ratio[1:] >= 0.9)), p_ge_0p85=float(np.mean(ratio[1:] >= 0.85))))
    # pooled 2024-26 mean bound and its ratio
    for bl in ["cons"]:
        for j, k in enumerate(keys):
            mb = {s: np.mean([boot[(bl, Y)][:, j, si] for Y in POST], axis=0) for si, s in enumerate(KOBAK_SETS)}
            for s in KOBAK_SETS:
                smr = S.summarise(mb[s])
                rows.append(dict(marker=k, baseline=bl, year="2024-26 mean", set=s, bound=smr["est"],
                                 lo95=smr["lo95"], hi95=smr["hi95"], se=smr["se"]))
            smr = S.summarise(mb["s3"] / mb["s0"])
            rows.append(dict(marker=k, baseline=bl, year="2024-26 mean", set="ratio_acc_all", bound=smr["est"],
                             lo95=smr["lo95"], hi95=smr["hi95"], se=smr["se"], p_le1=smr["p_le1"],
                             p_ge_0p9=float(np.mean((mb["s3"] / mb["s0"])[1:] >= 0.9))))
    for j, k in enumerate(keys):
        for si, s in enumerate(KOBAK_SETS):
            for y in sorted(P):
                series.append(dict(marker=k, set=s, year=y, prev=float(P[y][0, j, si]),
                                   n=float(sums[y][1][0, si])))
    return pd.DataFrame(rows), pd.DataFrame(series), dict(P=P, boot=boot, keys=keys)


# --------------------------------------------------------------------------------------------
# (3) Atlas helpers
# --------------------------------------------------------------------------------------------
STAGE_SETS = ["s0", "s1", "s2", "s3"]


def prevalence_stats(df: pd.DataFrame, items: list[tuple[str, str, str | None]], n_boot: int = N_BOOT) -> dict:
    """items: (name, feature column, conditioning column or None). Returns name -> (B+1, 4) pooled-std values."""
    out = {}
    plain = [(n, c) for n, c, cond in items if cond is None]
    if plain:
        sums = S.stage_sums(df, [c for _, c in plain], STAGE_SETS, n_boot=n_boot, seed=SEED)
        P = S.pooled_prev(sums, POST, "std")
        for j, (n, _) in enumerate(plain):
            out[n] = P[:, j, :]
    for n, c, cond in items:
        if cond is None:
            continue
        d = df.copy()
        for s in STAGE_SETS:
            d[f"{s}c"] = d[s] * d[cond]
        sums = S.stage_sums(d, [c], [f"{s}c" for s in STAGE_SETS], n_boot=n_boot, seed=SEED)
        out[n] = S.pooled_prev(sums, POST, "std")[:, 0, :]
    return out


def tokens_matrix(titles: pd.Series) -> tuple[sparse.csr_matrix, np.ndarray]:
    from sklearn.feature_extraction.text import CountVectorizer
    stop = set(S.lexicon()["stopwords_jsd"])
    import features as F
    txt = titles.fillna("").map(lambda t: F.strip_math(t).lower())
    cv = CountVectorizer(lowercase=False, token_pattern=r"(?u)\b[a-z][a-z0-9\-]{2,}\b", stop_words=sorted(stop),
                         dtype=np.int32)
    X = cv.fit_transform(txt.values).tocsr()
    return X, np.array(cv.get_feature_names_out())


def jsd(p: np.ndarray, q: np.ndarray) -> float:
    p = p / p.sum()
    q = q / q.sum()
    m = 0.5 * (p + q)
    with np.errstate(divide="ignore", invalid="ignore"):
        a = np.where(p > 0, p * np.log2(p / m), 0.0).sum()
        b = np.where(q > 0, q * np.log2(q / m), 0.0).sum()
    return float(0.5 * (a + b))


def rarefied_entropy(counts: np.ndarray, n: int) -> float:
    """Exact expected plug-in Shannon entropy (bits) of a size-n subsample without replacement."""
    counts = counts[counts > 0].astype(int)
    N = int(counts.sum())
    if n >= N:
        p = counts / N
        return float(-(p * np.log2(p)).sum())
    Ks, mult = np.unique(counts, return_counts=True)
    xs, ks, ms = [], [], []
    for K, m in zip(Ks, mult):
        x = np.arange(1, min(K, n) + 1)
        xs.append(x)
        ks.append(np.full(len(x), K))
        ms.append(np.full(len(x), m))
    x, K, m = np.concatenate(xs), np.concatenate(ks), np.concatenate(ms)
    pmf = stats.hypergeom.pmf(x, N, K, n)
    f = (x / n) * np.log2(x / n)
    return float(-(m * pmf * f).sum())


def opener_tokens(df: pd.DataFrame) -> np.ndarray:
    tok = np.where(df.name_primary.astype(int).to_numpy() == 1, "<NAME>", df.first_word.fillna("").astype(str))
    return pd.factorize(pd.Series(tok))[0]


def entropy_stat(codes: np.ndarray, years: np.ndarray, stage: np.ndarray, idx: np.ndarray | None = None) -> np.ndarray:
    """Mean over 2024-26 of rarefied opener entropy per stage set; idx = (bootstrap) row multiset."""
    if idx is None:
        idx = np.arange(len(codes))
    out = np.zeros(4)
    for y in POST:
        r = idx[years[idx] == y]
        n = int(stage[r, 3].sum())
        for k in range(4):
            c = codes[r[stage[r, k] == 1]]
            out[k] += rarefied_entropy(np.bincount(c), n) / len(POST)
    return out


def jsd_stat(X: sparse.csr_matrix, years: np.ndarray, stage: np.ndarray, rng: np.random.Generator,
             idx: np.ndarray | None = None, R: int = 20) -> np.ndarray:
    """Mean over Y in 2024-26 of JSD(title words Y, Y-1) per stage set, each set rarefied to the accepted n."""
    if idx is None:
        idx = np.arange(X.shape[0])
    out = np.zeros(4)
    by = {y: idx[years[idx] == y] for y in (2023,) + POST}
    for y in POST:
        a, b = by[y], by[y - 1]
        na, nb = int(stage[a, 3].sum()), int(stage[b, 3].sum())
        for k in range(4):
            ma, mb = a[stage[a, k] == 1], b[stage[b, k] == 1]
            reps = 1 if k == 3 else R
            vals = []
            for _ in range(reps):
                sa = ma if k == 3 else rng.choice(ma, na, replace=False)
                sb = mb if k == 3 else rng.choice(mb, nb, replace=False)
                pa = np.asarray(X[sa].sum(0)).ravel().astype(float)
                pb = np.asarray(X[sb].sum(0)).ravel().astype(float)
                vals.append(jsd(pa, pb))
            out[k] += np.mean(vals) / len(POST)
    return out


def random_band(codes: np.ndarray, X: sparse.csr_matrix, years: np.ndarray, stage: np.ndarray,
                rng: np.random.Generator, n_draw: int = 1000) -> tuple[np.ndarray, np.ndarray]:
    """Opener entropy and turnover JSD (mean over 2024-26) of random s0 subsets with the accepted per-year sizes."""
    s0 = {y: np.where(years == y)[0] for y in (2023,) + POST}
    n3 = {y: int(((years == y) & (stage[:, 3] == 1)).sum()) for y in (2023,) + POST}
    ent, js = np.zeros(n_draw), np.zeros(n_draw)
    for i in range(n_draw):
        sub = {y: rng.choice(s0[y], n3[y], replace=False) for y in s0}
        for y in POST:
            c = np.bincount(codes[sub[y]])
            p = c[c > 0] / n3[y]
            ent[i] += float(-(p * np.log2(p)).sum()) / len(POST)
            pa = np.asarray(X[sub[y]].sum(0)).ravel().astype(float)
            pb = np.asarray(X[sub[y - 1]].sum(0)).ravel().astype(float)
            js[i] += jsd(pa, pb) / len(POST)
    return ent, js


def boot_idx(years: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    return C.boot_indices(len(years), strata=years, rng=rng)


def its_stage_fits(df: pd.DataFrame, outcome: str = "name_primary") -> dict:
    """ITS slope change on each stage set (2018-26), joint IF covariance -> log ratios vs s0."""
    ifs, cls, b, se = [], [], [], []
    for s in STAGE_SETS:
        d = S.its_design(df[df[s] == 1])
        res = C.logit(S.ITS_FORMULA.format(y=outcome), d, cluster="topic100")
        ifs.append(S.logit_if(res, "post_t"))
        cls.append(d.loc[res.model_rows, "topic100"].to_numpy())
        b.append(float(res.params["post_t"]))
        se.append(float(res.bse["post_t"]))
    V, _ = S.joint_cov(ifs, cls)
    return dict(b=np.array(b), V=V, se=np.array(se))


def colon_premium_fits(df: pd.DataFrame) -> dict:
    """Acceptance OR of compound titles, 2024-26 (level) and its 2018-26 trend, on s0, s1, s2 (no s3 version)."""
    out = {}
    for kind in ["level", "trend"]:
        ifs, cls, b, se = [], [], [], []
        for s in ["s0", "s1", "s2"]:
            if kind == "level":
                d = df[(df[s] == 1) & df.year.isin(POST)].copy()
                f = "ACC ~ name_compound + C(year) + log_authors + llm_topic + C(topic100)"
                term = "name_compound"
            else:
                d = df[(df[s] == 1)].copy()
                d["tc"] = d.year - 2023
                d["comp_t"] = d.name_compound * d.tc
                f = "ACC ~ name_compound + comp_t + C(year) + log_authors + llm_topic + C(topic100)"
                term = "comp_t"
            res = C.logit(f, d, cluster="topic100")
            ifs.append(S.logit_if(res, term))
            cls.append(d.loc[res.model_rows, "topic100"].to_numpy())
            b.append(float(res.params[term]))
            se.append(float(res.bse[term]))
        V, _ = S.joint_cov(ifs, cls)
        out[kind] = dict(b=np.array(b), V=V, se=np.array(se))
    return out


def peak_years(df: pd.DataFrame, X: sparse.csr_matrix, vocab: np.ndarray, n_top: int = 30, min_count: int = 100,
               n_null: int = 200) -> tuple[pd.DataFrame, dict]:
    years = df.year.to_numpy()
    Xb = (X > 0).astype(np.float64).tocsr()
    yrs = list(range(2018, 2027))
    stage = df[STAGE_SETS].to_numpy()

    def prev(mask):
        return np.vstack([np.asarray(Xb[np.where(mask & (years == y))[0]].mean(0)).ravel() for y in yrs])

    P0 = prev(stage[:, 0] == 1)  # (9, V)
    tot = np.asarray(Xb.sum(0)).ravel()
    pk = P0.argmax(0)
    peak_val = P0.max(0)
    mean_val = P0.mean(0)
    interior = (pk >= 1) & (pk <= len(yrs) - 2)
    rise_fall = (peak_val >= 2 * P0[0]) & (peak_val >= 2 * P0[-1])
    ok = (tot >= min_count) & interior & rise_fall
    score = np.where(ok, peak_val / np.maximum(mean_val, 1e-12), -np.inf)
    top = np.argsort(-score)[:n_top]
    top = top[np.isfinite(score[top])]
    rows = []
    peaks = {}
    for k, s in enumerate(STAGE_SETS):
        Pk = prev(stage[:, k] == 1)[:, top]
        peaks[s] = np.array(yrs)[Pk.argmax(0)]
    for j, w in enumerate(top):
        rows.append(dict(word=vocab[w], total=int(tot[w]), score=float(score[w]),
                         **{f"peak_{s}": int(peaks[s][j]) for s in STAGE_SETS}))
    tab = pd.DataFrame(rows)
    agree = {s: float(np.mean(peaks[s] == peaks["s0"])) for s in STAGE_SETS}
    mad = {s: float(np.mean(np.abs(peaks[s] - peaks["s0"]))) for s in STAGE_SETS}
    shift = {s: float(np.mean(peaks[s] - peaks["s0"])) for s in STAGE_SETS}
    # null: random s0 subsamples with the accepted per-year sizes
    rng = np.random.default_rng(SEED + 7)
    n3 = {y: int(((years == y) & (stage[:, 3] == 1)).sum()) for y in yrs}
    nul_agree, nul_mad = [], []
    for _ in range(n_null):
        rowsP = []
        for y in yrs:
            pool = np.where(years == y)[0]
            sel = rng.choice(pool, n3[y], replace=False)
            rowsP.append(np.asarray(Xb[sel][:, top].mean(0)).ravel())
        pkr = np.array(yrs)[np.vstack(rowsP).argmax(0)]
        nul_agree.append(np.mean(pkr == peaks["s0"]))
        nul_mad.append(np.mean(np.abs(pkr - peaks["s0"])))
    return tab, dict(agree=agree, mean_abs_diff=mad, mean_shift=shift,
                     null_agree_mean=float(np.mean(nul_agree)), null_agree_lo95=float(np.quantile(nul_agree, .025)),
                     null_agree_hi95=float(np.quantile(nul_agree, .975)), null_mad_mean=float(np.mean(nul_mad)),
                     null_mad_lo95=float(np.quantile(nul_mad, .025)), null_mad_hi95=float(np.quantile(nul_mad, .975)),
                     n_words=int(len(top)))


# --------------------------------------------------------------------------------------------
# Figures
# --------------------------------------------------------------------------------------------
def fig_atlas(atlas: pd.DataFrame):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    a = atlas[atlas.in_forest.astype(bool)].copy().reset_index(drop=True)
    n = len(a)
    fig, (ax1, ax2) = C.new_fig("double", height=0.215 * n + 1.5, ncols=2,
                                gridspec_kw=dict(width_ratios=[1.0, 1.15], wspace=0.06), sharey=True)
    ypos = np.arange(n)[::-1].astype(float)
    cls_col = {"M": C.COLORS[0], "O": C.COLORS[1], "L": C.COLORS[2]}
    ax1.axvspan(0.9, 1.1, color=C.GRID, alpha=0.8, lw=0, zorder=0)
    ax1.axvline(1, color=C.GREY, lw=0.8, ls="--", zorder=0)
    xmin, xmax = 0.25, 1.6
    rows = []
    for yv, r in zip(ypos, a.itertuples()):
        col = cls_col[r.cls]
        band = str(r.interval_type).startswith("random-selection")
        lo, hi = max(r.ratio_lo95, xmin), min(r.ratio_hi95, xmax)
        ax1.plot([lo, hi], [yv, yv], color=col, lw=1.4, solid_capstyle="butt", ls=(0, (2, 1.2)) if band else "-")
        if r.ratio_lo95 < xmin:
            ax1.plot([xmin], [yv], marker="<", color=col, ms=4, lw=0, clip_on=False)
        effect = str(r.scale).startswith("effect")
        ax1.plot([r.ratio], [yv], "D" if effect else "o", color=col, ms=4.6 if effect else 4.8,
                 markerfacecolor="white" if effect else col)
        rows.append(dict(statistic=r.label, cls=r.cls, scale=r.scale, interval_type=r.interval_type,
                         published_set=r.published_set, ratio=r.ratio, lo95=r.ratio_lo95, hi95=r.ratio_hi95,
                         desk=r.log_desk, exit=r.log_exit, decision_total=r.log_dec, desk_crf=r.log_desk_crf,
                         exit_crf=r.log_exit_crf, editing_lo=r.log_edit_lo, editing_hi=r.log_edit_hi,
                         editing_separable=r.edit_separable, y=yv))
    ax1.set_xscale("log")
    ax1.set_xlim(xmin, xmax)
    t = [0.3, 0.5, 0.7, 0.9, 1.1, 1.4]
    ax1.set_xticks(t, [f"{v:g}" for v in t])
    ax1.xaxis.set_minor_formatter(plt.NullFormatter())
    ax1.set_yticks(ypos, a.label)
    ax1.tick_params(axis="y", length=0)
    ax1.grid(axis="y", visible=False)
    ax1.set_xlabel("Published-only / all-submission estimate (log axis)")
    ax1.set_title("a  Accepted-only vs all submissions", loc="left", fontsize=9)
    for i in range(1, n):
        if a.cls[i] != a.cls[i - 1]:
            for ax in (ax1, ax2):
                ax.axhline(ypos[i] + 0.5, color=C.GRID, lw=0.8)
    # panel b: stage decomposition of log(published/all); stage palette distinct from the class colours of panel a
    st_col = {"desk": "#3d3d3a", "exit": "#9a9994", "dec": "#d9d8d3"}
    h = 0.62
    for yv, r in zip(ypos, a.itertuples()):
        if not np.isfinite(r.log_dec):
            ax2.text(-1.08, yv, "effect-scale ratio: no stage split", fontsize=6.4, color=C.TEXT2, ha="left",
                     va="center")
            continue
        pos, neg = 0.0, 0.0
        for key, v in [("desk", r.log_desk), ("exit", r.log_exit), ("dec", r.log_dec)]:
            if not np.isfinite(v):
                continue
            left = pos if v >= 0 else neg + v
            ax2.barh(yv, abs(v), left=left, height=h, color=st_col[key], hatch="////" if key == "dec" else None,
                     edgecolor="#8a8984" if key == "dec" else "white", linewidth=0.0 if key != "dec" else 0.3)
            if v >= 0:
                pos += v
            else:
                neg += v
        if r.edit_separable and np.isfinite(r.log_edit_lo):
            lo_, hi_ = max(r.log_edit_lo, -1.1), min(r.log_edit_hi, 0.55)
            ax2.plot([lo_, hi_], [yv - 0.36, yv - 0.36], color=C.COLORS[3], lw=1.1)
            # off-scale whisker ends: arrow head plus the value (integration pass)
            if r.log_edit_hi > 0.55:
                ax2.plot([0.55], [yv - 0.36], marker=">", color=C.COLORS[3], ms=4, lw=0, clip_on=False)
                ax2.text(0.53, yv - 0.05, f"to {r.log_edit_hi:+.2f}", fontsize=5.8, color=C.TEXT2, ha="right",
                         va="bottom")
            if r.log_edit_lo < -1.1:
                ax2.plot([-1.1], [yv - 0.36], marker="<", color=C.COLORS[3], ms=4, lw=0, clip_on=False)
        elif r.edit_separable:
            ax2.text(0.54, yv, "audit interval unbounded", fontsize=6.2, color=C.TEXT2, ha="right",
                     va="center")
        tot = np.log(r.ratio)
        ax2.plot([tot], [yv], marker="|", color=C.TEXT, ms=7, mew=1.4)
    ax2.axvline(0, color=C.GREY, lw=0.8)
    ax2.set_xlim(-1.1, 0.55)
    ax2.grid(axis="y", visible=False)
    ax2.tick_params(axis="y", length=0)
    ax2.set_xlabel("Contribution to log(published / all)")
    ax2.set_title("b  Where the gap arises (no stage is identified as pure selection)", loc="left", fontsize=9)
    handles = [Patch(color=st_col["desk"], label="Desk stage"), Patch(color=st_col["exit"], label="Exit stage"),
               Patch(facecolor=st_col["dec"], hatch="////", edgecolor="#8a8984",
                     label="Decision (selection + camera-ready editing, not separable)"),
               plt.Line2D([], [], marker="|", color=C.TEXT, lw=0, ms=7, mew=1.4, label="Total log ratio"),
               plt.Line2D([], [], color=C.COLORS[3], lw=1.1,
                          label="Editing implied by the audit 95% CI (complete audit, auditable features)")]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.035), ncol=3, fontsize=7.3,
               handlelength=1.4, columnspacing=1.0)
    fig.text(0.01, -0.05, "Desk and exit compare exiting papers with survivor sets that contain accepted camera-ready "
             "text (camera-ready-free variants in atlas.csv). Hollow diamonds: OR statistics on the effect (log-OR) "
             "scale; dashed intervals: random-selection null bands, not CIs. Colon-premium trend: decided-only "
             "(ACC vs REJ) analogue.", fontsize=6.6, color=C.TEXT2, ha="left", va="top", wrap=True)
    cl_handles = [plt.Line2D([], [], marker="o", color=cls_col[k], lw=1.4, ms=4.8, label=l)
                  for k, l in [("M", "Mainstream (M)"), ("O", "Outsider (O)"), ("L", "LLM-style (L)")]]
    cl_handles.append(Patch(color=C.GRID, label="+/-10% band"))
    ax1.legend(handles=cl_handles, loc="upper left", fontsize=7.5, handlelength=1.4)
    return fig, pd.DataFrame(rows)


def fig_kobak(series: pd.DataFrame, bounds: pd.DataFrame, marker: str = "F24"):
    import matplotlib.pyplot as plt  # noqa: F401
    fig, (ax1, ax2) = C.new_fig("double", height=2.7, ncols=2, gridspec_kw=dict(width_ratios=[1.35, 1], wspace=0.3))
    sets = [("s0", "All submissions", C.COLORS[0]), ("s3", "Accepted", C.COLORS[1]), ("NAp", "NA pool", C.COLORS[2])]
    rows = []
    for s, lab, col in sets:
        x = series[(series.marker == marker) & (series.set == s)].sort_values("year")
        ax1.plot(x.year, 100 * x.prev, "-o", color=col, ms=4.5, lw=1.8, label=lab)
        # conservative baseline for 2024-26
        P = {int(y): float(v) for y, v in zip(x.year, x.prev)}
        xb = np.array([2021, 2022, 2023], float)
        sl, ic = np.polyfit(xb, [P[2021], P[2022], P[2023]], 1)
        q = [max(max(ic + sl * Y, 0), max(P[2022], P[2023])) for Y in POST]
        ax1.plot([2023] + list(POST), 100 * np.array([P[2023]] + q), ls="--", color=col, lw=1.1)
        for y, v in P.items():
            rows.append(dict(panel="a", set=s, year=y, value=100 * v, kind="prevalence"))
        for Y, v in zip(POST, q):
            rows.append(dict(panel="a", set=s, year=Y, value=100 * v, kind="baseline_cons"))
    ax1.set_xticks(range(2021, 2027), [f"{y}" for y in range(2021, 2027)])
    ax1.set_ylim(0, None)
    ax1.set_ylabel("Abstracts with a RARE21 word (%)")
    ax1.set_title("a  Marker prevalence and conservative baselines", loc="left", fontsize=9)
    ax1.legend(loc="upper left", fontsize=7.5)
    b = bounds[(bounds.marker == marker) & (bounds.baseline == "cons") & bounds.year.isin(POST)]
    off = {"s0": -0.18, "s3": 0.0, "NAp": 0.18}
    for s, lab, col in sets:
        x = b[b.set == s].sort_values("year")
        xx = x.year.astype(int) + off[s]
        ax2.errorbar(xx, 100 * x.bound, yerr=[100 * (x.bound - x.lo95), 100 * (x.hi95 - x.bound)], fmt="o", color=col,
                     ms=4.8, elinewidth=1.4, capsize=0, label=lab)
        for r in x.itertuples():
            rows.append(dict(panel="b", set=s, year=int(r.year), value=100 * r.bound, lo95=100 * r.lo95,
                             hi95=100 * r.hi95, kind="bound_pp"))
    rr = b[b.set == "ratio_acc_all"].sort_values("year")
    for r in rr.itertuples():
        top = 100 * b[(b.year == r.year) & b.set.isin(["s0", "s3", "NAp"])].hi95.max()
        ax2.text(int(r.year), top + 0.6, f"acc/all {r.bound:.2f}\n[{r.lo95:.2f}, {r.hi95:.2f}]", ha="center",
                 va="bottom", fontsize=6.6, color=C.TEXT2)
        rows.append(dict(panel="b", set="ratio_acc_all", year=int(r.year), value=r.bound, lo95=r.lo95, hi95=r.hi95,
                         kind="ratio"))
    ax2.axhline(0, color=C.GREY, lw=0.8)
    ax2.set_xticks(list(POST), [str(y) for y in POST])
    ax2.set_xlim(2023.5, 2026.5)
    ax2.set_ylabel("Lower bound on LLM-styled share (pp)")
    ax2.set_title("b  Kobak-style lower bound (95% percentile CIs)", loc="left", fontsize=9)
    ax2.legend(loc="lower left", fontsize=7.2)
    lo_all = 100 * b[b.set.isin(["s0", "s3", "NAp"])].lo95.min()
    hi_all = 100 * b[b.set.isin(["s0", "s3", "NAp"])].hi95.max()
    ax2.set_ylim(min(-1.0, lo_all - 0.5), hi_all * 1.25)
    return fig, pd.DataFrame(rows)


# --------------------------------------------------------------------------------------------
def main():
    t0 = time.time()
    fh = open(OUTDIR / "d4_bias_atlas.log", "w")
    rng = np.random.default_rng(SEED)
    df = S.load_frame()
    tf = C.load_features(["submission_id"] + [f"tpl_{k}" for k in S.lexicon()["snowclones"]])
    df = df.merge(tf, on="submission_id", how="left", validate="1:1")
    df["snowclone"] = snowclone_col(df)
    df["llm_t_lm"] = ((df.llm_t_abbrev + df.llm_t_spelled) > 0).astype(int)
    tn = C.load_universe(["submission_id", "title_nfkc"])
    df = df.merge(tn, on="submission_id", how="left", validate="1:1")
    log(f"frame {df.shape} ({time.time() - t0:.0f}s)", fh)

    # ---------------- (1) audit
    pairs = audit_pairs("complete")
    pairs.to_csv(OUTDIR / "audit_pairs.csv", index=False)
    log(f"audit: {len(pairs)} pre-decision pairs (WP4 frozen primary audit); by decision "
        f"{pairs.decision.value_counts().to_dict()}; by source {pairs.source.value_counts().to_dict()}; "
        f"title changed (normalised words) acc {pairs[pairs.acc == 1].title_changed.mean():.3f} "
        f"rej {pairs[pairs.acc == 0].title_changed.mean():.3f}", fh)
    flips = flip_table(pairs)
    flips_post = flip_table(pairs[pairs.year.isin(POST)].reset_index(drop=True), label="audit years 2024-26")
    pw, w = ipw_weights(pairs)
    flips_ipw = flip_table(pw, weights=w, label="population-weighted 2023-26")
    pairs_orig = audit_pairs("original")
    flips_orig = flip_table(pairs_orig, label="original audit only (331 pairs, 2022-26; pre-integration primary)")
    log(f"original audit: {len(pairs_orig)} pairs; by decision {pairs_orig.decision.value_counts().to_dict()}", fh)
    flips_all = pd.concat([flips, flips_post, flips_ipw, flips_orig], ignore_index=True)
    # consistency with WP4's canonical primary flip matrices (same pairs, same features_v2 code, same CI)
    if WP4_FLIPS.exists():
        wf = pd.read_csv(WP4_FLIPS)
        wf = wf[wf.spec.eq("primary")].set_index("feature")
        common = [k for k in flips.feature if k in wf.index]
        fi = flips.set_index("feature").loc[common]
        dev = {c_: float(np.max(np.abs(fi[a_].to_numpy() - wf.loc[common, c_].to_numpy())))
               for a_, c_ in [("did", "did"), ("did_lo95", "did_lo"), ("did_hi95", "did_hi")]}
        aud_mismatch = [k for k in common if bool(fi.loc[k, "auditable"]) != bool(wf.loc[k, "auditable"])]
        log(f"WP4 consistency ({len(common)} common features): max |diff| {dev}; auditable mismatches "
            f"{aud_mismatch}", fh)
        assert max(dev.values()) < 1e-9 and not aud_mismatch, "D4 flip table disagrees with WP4 primary"
    flips_all.to_csv(OUTDIR / "T4_2_audit_flips.csv", index=False)
    log(flips[["feature", "n_acc", "n_rej", "v1_present_acc", "adds_acc", "drops_acc", "v1_present_rej", "adds_rej",
               "drops_rej", "net_acc", "net_rej", "did", "did_se", "auditable"]].round(4).to_string(), fh)

    # stage prevalences (2024-26, year-standardised) and accepted shares for the bound
    keys_bound = [k for k, _ in AUDIT_FEATURES]
    colmap = dict(AUDIT_FEATURES)
    sums = S.stage_sums(df, [colmap[k] for k in keys_bound] + ["ACC"], STAGE_SETS, n_boot=0)
    Pp = S.pooled_prev(sums, POST, "std")[0]  # (F+1, 4)
    a_share = Pp[-1]  # accepted share of each stage set (year-standardised)
    bound_rows = []
    for j, k in enumerate(keys_bound):
        P0, P1, P2, P3 = Pp[j]
        fr = flips.set_index("feature").loc[k]
        D, Dlo, Dhi = fr.did, fr.did_lo95, fr.did_hi95
        a0, a2 = a_share[0], a_share[2]

        def gdec(x):
            return (P3 - x) / (P2 - a2 * x)

        def gtot(x):
            return (P3 - x) / (P0 - a0 * x)
        Gd_obs, Gt_obs = P3 / P2, P3 / P0
        tip_dec = (P3 - P2) / (1 - a2)
        tip_tot = (P3 - P0) / (1 - a0)

        def identified(G_obs, tip):
            if G_obs >= 1:
                return bool(tip > Dhi)
            return bool(tip < Dlo)
        gd = sorted([gdec(Dlo), gdec(Dhi)])
        gt = sorted([gtot(Dlo), gtot(Dhi)])
        bound_rows.append(dict(
            feature=k, auditable=bool(fr.auditable), P_s0=P0, P_s2=P2, P_s3=P3, acc_share_s0=a0, acc_share_s2=a2,
            did_pp=100 * D, did_se_pp=100 * fr.did_se, did_lo95_pp=100 * Dlo, did_hi95_pp=100 * Dhi,
            G_dec_obs=Gd_obs, G_dec_sel_point=gdec(D), G_dec_interval_lo=gd[0], G_dec_interval_hi=gd[1],
            tip_dec_pp=100 * tip_dec, G_dec_identified=identified(Gd_obs, tip_dec) and bool(fr.auditable),
            G_total_obs=Gt_obs, G_total_sel_point=gtot(D), G_total_interval_lo=gt[0], G_total_interval_hi=gt[1],
            tip_total_pp=100 * tip_tot, G_total_identified=identified(Gt_obs, tip_tot) and bool(fr.auditable)))
    bound = pd.DataFrame(bound_rows)
    bound.to_csv(OUTDIR / "T4_2_decision_bound.csv", index=False)
    log("\nT4.2 decision-stage bound (2024-26 std):\n" + bound[["feature", "auditable", "G_dec_obs", "did_pp",
                                                               "did_lo95_pp", "did_hi95_pp", "tip_dec_pp",
                                                               "G_dec_interval_lo", "G_dec_interval_hi",
                                                               "G_dec_identified", "G_total_obs", "tip_total_pp",
                                                               "G_total_identified"]].round(3).to_string(), fh)
    log(f"audit done ({time.time() - t0:.0f}s)", fh)

    # ---------------- (2) Kobak bounds
    kcols = {"F24": "f24", "F24_2": "f24_2", "F26_words": "f26_words", "emdash": "abs_emdash", "F26": "f26_abs",
             "F26_incl_title": "f26", "L_abstract": "L_abstract"}
    kb, ks, kstore = kobak(df, kcols)
    kb.to_csv(OUTDIR / "kobak_bounds.csv", index=False)
    ks.to_csv(OUTDIR / "kobak_series.csv", index=False)
    show = kb[(kb.marker == "F24") & (kb.baseline == "cons")]
    log("\nKobak bounds F24 (cons):\n" + show.pivot_table(index="year", columns="set", values="bound").round(4)
        .to_string(), fh)
    log(show[show.set == "ratio_acc_all"][["year", "bound", "lo95", "hi95", "p_ge_0p9", "p_ge_0p85"]].round(3)
        .to_string(), fh)
    log(f"kobak done ({time.time() - t0:.0f}s)", fh)

    # ---------------- (3) atlas
    # Audit revisions: OR-type statistics are compared on the effect (log-OR) scale (ratio of log-ORs, delta-method CI
    # from the joint IF covariance); the pre-registered colon-premium TREND (decided-only analogue) enters the M count,
    # the level is supplementary; entropy/JSD intervals are random-selection null bands (not CIs) and do not enter the
    # 90%-CI count; camera-ready-free desk/exit parts (accepted papers removed from every stage set) are reported next
    # to the observed ones; BH q-values over all atlas tests.
    prev_items = [
        ("NAME prevalence", "name_primary", None), ("Compound prevalence", "name_compound", None),
        ("Phrase-colon prevalence", "phrase_colon", None), ("Mixed-case name prevalence", "ortho_mixed_case", None),
        ("Title Case prevalence", "case_title_case", None), ("Snowclone share", "snowclone", None),
        ("LLM abbreviation-only share", "llm_t_abbrev_only", "llm_t_lm"),
        ("ALL-CAPS title prevalence", "case_all_caps", None), ("Sentence case prevalence", "case_sentence_case", None),
        ("Question opener prevalence", "question_opener", None), ("O-union prevalence", "O_union", None),
        ("Title typography prevalence", "title_typo", None), ("R24 prevalence", "r24_any", None),
        ("R26 prevalence", "r26_any", None), ("F24 prevalence", "f24", None), ("F26 (abstract) prevalence", "f26_abs", None),
        ("Em dash (abstract) prevalence", "abs_emdash", None), ("Style density (mean)", "xs_per100", None),
        ("L-union prevalence", "L_union", None),
    ]
    PS = prevalence_stats(df, prev_items)
    # camera-ready-free stage sets (accepted papers removed): prevalence on s0n, s1n, s2n (point estimates)
    crf = {}
    for (label, col, cond) in prev_items:
        d_ = df.copy()
        cs = ["s0n", "s1n", "s2n"]
        if cond is not None:
            for c_ in cs:
                d_[c_ + "c"] = d_[c_] * d_[cond]
            cs = [c_ + "c" for c_ in cs]
        sm_ = S.stage_sums(d_, [col], cs, n_boot=0)
        crf[label] = S.pooled_prev(sm_, POST, "std")[0, 0, :]
    cls_of = {"NAME prevalence": "M", "Compound prevalence": "M", "Phrase-colon prevalence": "M",
              "Mixed-case name prevalence": "M", "Title Case prevalence": "M", "Snowclone share": "M",
              "LLM abbreviation-only share": "M", "ALL-CAPS title prevalence": "O", "Sentence case prevalence": "O",
              "Question opener prevalence": "O", "O-union prevalence": "O"}
    audit_key = {"name_primary": "NAME", "name_compound": "compound", "phrase_colon": "phrase_colon",
                 "ortho_mixed_case": "mixed_case_name", "case_title_case": "title_case", "snowclone": "snowclone",
                 "llm_t_abbrev_only": "llm_abbrev_only", "case_all_caps": "all_caps_title",
                 "case_sentence_case": "sentence_case", "question_opener": "question_opener", "O_union": "O_union",
                 "title_typo": "title_typo", "r24_any": "R24", "r26_any": "R26"}
    atlas_rows = []
    fl = flips.set_index("feature")
    base_cols = dict(edit_separable=False, log_dec_sel=np.nan, log_edit=np.nan, log_edit_lo=np.nan, log_edit_hi=np.nan,
                     log_desk_crf=np.nan, log_exit_crf=np.nan, p_two_sided=np.nan, or_ratio=np.nan,
                     or_ratio_lo95=np.nan, or_ratio_hi95=np.nan)

    def add_row(label, cls, vals_boot, kind, edit=None, in_forest=True, note="", crf_vals=None):
        """vals_boot: (B+1, 4) statistic on s0..s3 (row 0 point). Paper-bootstrap percentile CI of T_s3/T_s0."""
        v = vals_boot
        with np.errstate(divide="ignore", invalid="ignore"):
            ratio = v[:, 3] / v[:, 0]
        smr = S.summarise(ratio)
        r = dict(label=label, cls=cls, kind=kind, scale="ratio", published_set="accepted (s3)",
                 interval_type="paper bootstrap (2,000)", in_count=True,
                 T_s0=float(v[0, 0]), T_s1=float(v[0, 1]), T_s2=float(v[0, 2]),
                 T_s3=float(v[0, 3]), ratio=smr["est"], ratio_lo95=smr["lo95"], ratio_hi95=smr["hi95"],
                 ratio_lo90=smr["lo90"], ratio_hi90=smr["hi90"], log_desk=float(np.log(v[0, 1] / v[0, 0])),
                 log_exit=float(np.log(v[0, 2] / v[0, 1])), log_dec=float(np.log(v[0, 3] / v[0, 2])),
                 in_forest=in_forest, note=note, **base_cols)
        r["p_two_sided"] = float(min(1.0, 2 * min(smr["p_ge1"], smr["p_le1"])))
        if crf_vals is not None:
            r["log_desk_crf"] = float(np.log(crf_vals[1] / crf_vals[0]))
            r["log_exit_crf"] = float(np.log(crf_vals[2] / crf_vals[1]))
        r["within_10pct"] = bool(0.9 <= r["ratio"] <= 1.1)
        r["ci90_within_10pct"] = bool(r["ratio_lo90"] >= 0.9 and r["ratio_hi90"] <= 1.1)
        if edit is not None:
            r.update(edit)
        atlas_rows.append(r)

    for (label, col, cond) in prev_items:
        v = PS[label]
        cls = cls_of.get(label, "L")
        edit = None
        ak = audit_key.get(col)
        if ak is not None and ak in fl.index and bool(fl.loc[ak, "auditable"]) and cond is None:
            # accepted share per stage set (year-standardised): from the ACC column
            P = v[0]
            a = a_share
            D, Dlo, Dhi = fl.loc[ak, ["did", "did_lo95", "did_hi95"]]

            def sel_tot(x):
                Pt = P - a * x
                if (Pt <= 0).any():
                    return (np.nan,) * 4
                return np.log(Pt[3] / Pt[0]), np.log(Pt[1] / Pt[0]), np.log(Pt[2] / Pt[1]), np.log(Pt[3] / Pt[2])
            tot_obs = np.log(P[3] / P[0])
            tsel, dsel, esel, decsel = sel_tot(D)
            ends = [tot_obs - sel_tot(Dlo)[0], tot_obs - sel_tot(Dhi)[0]]
            unbounded = bool(not np.all(np.isfinite(ends)))
            e_lo, e_hi = (sorted(ends) if not unbounded else (np.nan, np.nan))
            edit = dict(edit_separable=bool(np.isfinite(tsel)), log_dec_sel=float(decsel),
                        log_edit=float(tot_obs - tsel), log_edit_lo=float(e_lo), log_edit_hi=float(e_hi),
                        log_desk_sel=float(dsel), log_exit_sel=float(esel), audit_did_pp=float(100 * D),
                        audit_did_lo95_pp=float(100 * Dlo), audit_did_hi95_pp=float(100 * Dhi),
                        edit_interval_unbounded=unbounded)
        add_row(label, cls, v, "prevalence" if col != "xs_per100" else "mean", edit=edit,
                note="conditional on titles naming language models" if cond else "", crf_vals=crf[label])
    log(f"atlas prevalence stats done ({time.time() - t0:.0f}s)", fh)

    # Kobak bound mean 2024-26 (F24, cons) per stage set
    kb_idx = kstore["keys"].index("F24")
    mb = np.mean([kstore["boot"][("cons", Y)][:, kb_idx, :4] for Y in POST], axis=0)  # (B+1, 4) for s0..s3
    add_row("RARE21 Kobak bound (2024-26 mean)", "L", mb, "bound")

    zq = stats.norm.ppf(0.975)
    z90 = stats.norm.ppf(0.95)

    def effect_ratio(b, V, i, j=0):
        """b_i / b_j with a delta-method SE from the joint covariance; also the difference b_i - b_j."""
        r_ = b[i] / b[j]
        se_r = float(np.sqrt(V[i, i] - 2 * r_ * V[i, j] + r_ ** 2 * V[j, j]) / abs(b[j]))
        dlt = b[i] - b[j]
        se_d = float(np.sqrt(V[i, i] + V[j, j] - 2 * V[i, j]))
        return dict(ratio=float(r_), ratio_lo95=float(r_ - zq * se_r), ratio_hi95=float(r_ + zq * se_r),
                    ratio_lo90=float(r_ - z90 * se_r), ratio_hi90=float(r_ + z90 * se_r), ratio_se=se_r,
                    diff=float(dlt), diff_se=se_d, diff_lo95=float(dlt - zq * se_d), diff_hi95=float(dlt + zq * se_d),
                    p_two_sided=float(2 * stats.norm.sf(abs(dlt) / se_d)))

    # ITS slope change across stage sets (analytic joint covariance); effect scale = ratio of slope-change log-ORs
    its = its_stage_fits(df)
    b, V = its["b"], its["V"]
    ORs = np.exp(b)
    er = effect_ratio(b, V, 3)
    d30, se30 = er["diff"], er["diff_se"]
    its_row = dict(label="ITS slope change (NAME), effect scale", cls="M", kind="ratio of slope-change log-ORs",
                   scale="effect (log-OR) ratio", published_set="accepted (s3)",
                   interval_type="delta method, joint IF covariance", in_count=True,
                   T_s0=float(b[0]), T_s1=float(b[1]), T_s2=float(b[2]), T_s3=float(b[3]),
                   log_desk=np.nan, log_exit=np.nan, log_dec=np.nan, in_forest=True, **base_cols)
    its_row.update({k: v for k, v in er.items() if k.startswith("ratio")})
    its_row.update(p_two_sided=er["p_two_sided"], or_ratio=float(ORs[3] / ORs[0]),
                   or_ratio_lo95=float(np.exp(d30 - zq * se30)), or_ratio_hi95=float(np.exp(d30 + zq * se30)),
                   diff_s3_s0=d30, diff_se=se30,
                   note=f"slope-change log OR s0 {b[0]:.3f} (se {its['se'][0]:.3f}; OR {ORs[0]:.3f}), s3 {b[3]:.3f} "
                        f"(se {its['se'][3]:.3f}; OR {ORs[3]:.3f}); difference {d30:+.3f} (se {se30:.3f}); "
                        f"ratio of ORs {ORs[3] / ORs[0]:.3f} (the earlier OR-scale comparison)")
    its_row["within_10pct"] = bool(0.9 <= its_row["ratio"] <= 1.1)
    its_row["ci90_within_10pct"] = bool(its_row["ratio_lo90"] >= 0.9 and its_row["ratio_hi90"] <= 1.1)
    atlas_rows.append(its_row)
    log(f"ITS stage fits: logORs {np.round(b, 4)}, ORs {np.round(ORs, 4)}; s3/s0 effect ratio {er['ratio']:.3f} "
        f"[{er['ratio_lo95']:.3f}, {er['ratio_hi95']:.3f}] ({time.time() - t0:.0f}s)", fh)

    # colon premium (level and trend): decided-only (s2) vs all (s0); no accepted-only version exists
    cp = colon_premium_fits(df)
    for kind, lab in [("trend", "Colon-premium trend, 2018-26 (decided-only)"),
                      ("level", "Colon premium, 2024-26 (decided-only; supplementary)")]:
        b, V = cp[kind]["b"], cp[kind]["V"]
        er = effect_ratio(b, V, 2)
        r = dict(label=lab, cls="M", kind="ratio of log-OR slopes" if kind == "trend" else "ratio of log-ORs",
                 scale="effect (log-OR) ratio", published_set="decided (s2: ACC vs REJ)",
                 interval_type="delta method, joint IF covariance", in_count=(kind == "trend"),
                 T_s0=float(b[0]), T_s1=float(b[1]), T_s2=float(b[2]), T_s3=np.nan,
                 log_desk=np.nan, log_exit=np.nan, log_dec=np.nan, in_forest=(kind == "trend"), **base_cols)
        r.update({k: v for k, v in er.items() if k.startswith("ratio")})
        r.update(p_two_sided=er["p_two_sided"], diff_s2_s0=er["diff"], diff_se=er["diff_se"],
                 diff_lo95=er["diff_lo95"], diff_hi95=er["diff_hi95"],
                 se_s0=float(cp[kind]["se"][0]), se_s2=float(cp[kind]["se"][2]),
                 note=("published-only analogue = decided-only (ACC vs REJ incl. post-decision withdrawals); no "
                       "accepted-only version exists" + ("" if kind == "trend" else
                                                         f"; all-submission log-OR {b[0]:.3f} (se "
                                                         f"{cp[kind]['se'][0]:.3f}) is itself near 0, so the relative "
                                                         f"criterion is ill-conditioned; difference {er['diff']:+.3f} "
                                                         f"[{er['diff_lo95']:+.3f}, {er['diff_hi95']:+.3f}]")))
        if kind == "level":
            r.update(or_ratio=float(np.exp(er["diff"])), or_ratio_lo95=float(np.exp(er["diff_lo95"])),
                     or_ratio_hi95=float(np.exp(er["diff_hi95"])))
        r["within_10pct"] = bool(0.9 <= r["ratio"] <= 1.1)
        r["ci90_within_10pct"] = bool(r["ratio_lo90"] >= 0.9 and r["ratio_hi90"] <= 1.1)
        atlas_rows.append(r)
    log(f"colon premium: level b {np.round(cp['level']['b'], 4)}, trend b {np.round(cp['trend']['b'], 4)} "
        f"({time.time() - t0:.0f}s)", fh)

    # entropy and JSD: point estimates on rarefied stage sets; the interval is a RANDOM-SELECTION NULL BAND
    # (statistic on random s0 subsets of the accepted per-year sizes / its expectation), pivoted around the observed
    # ratio. It describes what random acceptance would produce, not sampling uncertainty of the ratio, so it is
    # labelled as a band and kept out of the 90%-CI count. A paper bootstrap is not used: with-replacement duplicates
    # bias the unrarefied accepted set and the rarefied sets differently (bootstrap intervals excluded the point).
    years = df.year.to_numpy()
    stage = df[STAGE_SETS].to_numpy().astype(int)
    codes = opener_tokens(df)
    X, vocab = tokens_matrix(df.title_nfkc)
    ent0 = entropy_stat(codes, years, stage)
    jsd0 = jsd_stat(X, years, stage, rng, R=50)
    ent_null, jsd_null = random_band(codes, X, years, stage, rng, n_draw=N_NULL)
    for lab, kind, v0, nul in [("Opener entropy, NAME-collapsed (rarefied)", "entropy (bits)", ent0, ent_null),
                               ("Lexical turnover JSD (rarefied)", "JSD (bits)", jsd0, jsd_null)]:
        q = nul / nul.mean()
        ratio = v0[3] / v0[0]
        r = dict(label=lab, cls="M", kind=kind, scale="ratio", published_set="accepted (s3)",
                 interval_type="random-selection null band (not a CI)", in_count=True,
                 T_s0=float(v0[0]), T_s1=float(v0[1]), T_s2=float(v0[2]),
                 T_s3=float(v0[3]), ratio=float(ratio),
                 ratio_lo95=float(ratio / np.quantile(q, .975)), ratio_hi95=float(ratio / np.quantile(q, .025)),
                 ratio_lo90=float(ratio / np.quantile(q, .95)), ratio_hi90=float(ratio / np.quantile(q, .05)),
                 log_desk=float(np.log(v0[1] / v0[0])), log_exit=float(np.log(v0[2] / v0[1])),
                 log_dec=float(np.log(v0[3] / v0[2])), in_forest=True, **base_cols)
        r.update(random_band_lo95=float(np.quantile(q, .025)), random_band_hi95=float(np.quantile(q, .975)),
                 p_two_sided=float(2 * min(np.mean(q <= ratio), np.mean(q >= ratio))),
                 note=f"interval = observed ratio pivoted on the random-selection band ({N_NULL} random s0 subsets "
                      f"with accepted per-year sizes); a null band, not a CI; s0-s2 values are exact (entropy) or "
                      f"50-draw (JSD) rarefied")
        r["p_random_two_sided"] = r["p_two_sided"]
        r["within_10pct"] = bool(0.9 <= r["ratio"] <= 1.1)
        r["ci90_within_10pct"] = np.nan  # null band: excluded from the 90%-CI count (D4-8)
        atlas_rows.append(r)
    log(f"entropy {np.round(ent0, 4)}; JSD {np.round(jsd0, 5)}; random band entropy "
        f"{np.quantile(ent_null / ent_null.mean(), [.025, .975]).round(4)}, JSD "
        f"{np.quantile(jsd_null / jsd_null.mean(), [.025, .975]).round(4)} ({time.time() - t0:.0f}s)", fh)

    # peak years
    ptab, pk = peak_years(df, X, vocab)
    ptab.to_csv(OUTDIR / "atlas_peaks.csv", index=False)
    log(f"peaks: {pk}", fh)
    atlas_rows.append(dict(label="Peak years of top-30 title fashions (agreement with all)", cls="M",
                           kind="share of words with identical peak year", scale="agreement share",
                           published_set="accepted (s3)", interval_type="random-subsample null", in_count=False,
                           T_s0=1.0, T_s1=pk["agree"]["s1"],
                           T_s2=pk["agree"]["s2"], T_s3=pk["agree"]["s3"], ratio=np.nan, in_forest=False,
                           note=f"random-subsample null (accepted per-year sizes): agreement {pk['null_agree_mean']:.3f} "
                                f"[{pk['null_agree_lo95']:.3f}, {pk['null_agree_hi95']:.3f}]; mean |shift| accepted "
                                f"{pk['mean_abs_diff']['s3']:.2f} y vs null {pk['null_mad_mean']:.2f} "
                                f"[{pk['null_mad_lo95']:.2f}, {pk['null_mad_hi95']:.2f}]",
                           within_10pct=np.nan))

    order = ["M", "O", "L"]
    atlas = pd.DataFrame(atlas_rows)
    atlas["cls_order"] = atlas.cls.map({c: i for i, c in enumerate(order)})
    atlas = atlas.sort_values(["cls_order"], kind="stable").drop(columns="cls_order").reset_index(drop=True)
    with np.errstate(divide="ignore", invalid="ignore"):
        atlas["abs_log_ratio"] = np.abs(np.log(atlas.ratio.where(atlas.ratio > 0)))
    atlas["q_bh"] = S.bh_q(atlas.p_two_sided.to_numpy())
    atlas.to_csv(OUTDIR / "atlas.csv", index=False)
    log("\natlas:\n" + atlas[["label", "cls", "T_s0", "T_s3", "ratio", "ratio_lo95", "ratio_hi95", "within_10pct",
                              "in_count", "p_two_sided", "q_bh", "log_desk", "log_exit", "log_desk_crf",
                              "log_exit_crf", "log_dec"]].round(4).to_string(), fh)

    # H4e summaries (counted statistics only; the colon-premium level is supplementary)
    ratio_rows = atlas[atlas.ratio.notna() & atlas.in_count.astype(bool)]
    by_cls = ratio_rows.groupby("cls").agg(n=("ratio", "size"), within=("within_10pct", "sum"),
                                           median_abs_log=("abs_log_ratio", "median"),
                                           max_abs_log=("abs_log_ratio", "max"))
    log("\nH4e by class:\n" + by_cls.to_string(), fh)
    M_rows = ratio_rows[ratio_rows.cls == "M"]
    M_acc = M_rows[M_rows.published_set.eq("accepted (s3)")]
    M_ci = M_rows[M_rows.ci90_within_10pct.notna()]
    knife = atlas[atlas.ratio.notna() & atlas.ratio.between(0.88, 0.92)][["label", "ratio", "ratio_lo95", "ratio_hi95"]]
    h4e = dict(
        n_statistics=int(len(atlas)), n_ratio_statistics=int(atlas.ratio.notna().sum()),
        n_counted_ratio_statistics=int(len(ratio_rows)),
        M_all_within_10pct=bool(M_rows.within_10pct.all()), M_within=int(M_rows.within_10pct.sum()),
        M_n=int(len(M_rows)), M_accepted_only_within=int(M_acc.within_10pct.sum()), M_accepted_only_n=int(len(M_acc)),
        M_outside=M_rows[~M_rows.within_10pct.astype(bool)].label.tolist(),
        M_ci90_within=int(M_ci.ci90_within_10pct.astype(bool).sum()), M_ci90_n=int(len(M_ci)),
        by_class=by_cls.reset_index().to_dict(orient="records"),
        deviations_concentrate_in_O_L=bool(by_cls.loc[["O", "L"], "median_abs_log"].min()
                                           > by_cls.loc["M", "median_abs_log"]),
        knife_edge_0p90=knife.to_dict(orient="records"),
        peaks=pk,
    )
    log(f"H4e: {h4e['M_within']}/{h4e['M_n']} M within +/-10% (accepted-only {h4e['M_accepted_only_within']}/"
        f"{h4e['M_accepted_only_n']}); outside: {h4e['M_outside']}", fh)

    # ---------------- figures
    fig, data = fig_atlas(atlas)
    C.save_fig(fig, "fig_F4_2_bias_atlas", OUTDIR, data=data)
    fig, data = fig_kobak(ks, kb)
    C.save_fig(fig, "fig_F4_3_kobak_bounds", OUTDIR, data=data)

    # ---------------- H4c verdict inputs
    r = kb[(kb.marker == "F24") & (kb.baseline == "cons") & (kb.set == "ratio_acc_all")]
    rat = {str(x.year): dict(ratio=x.bound, lo95=x.lo95, hi95=x.hi95, p_ge_0p9=x.p_ge_0p9,
                             p_ge_0p85=getattr(x, "p_ge_0p85", np.nan)) for x in r.itertuples()}
    bnd = kb[(kb.marker == "F24") & (kb.baseline == "cons") & kb.set.isin(["s0", "s3", "NAp", "s2", "REJp"])]
    h4c = dict(
        marker="F24 (any RARE21 word in abstract)", baseline="cons = max(linear 2021-23, max(2022, 2023))",
        bounds={f"{x.set}_{x.year}": dict(bound=x.bound, lo95=x.lo95, hi95=x.hi95) for x in bnd.itertuples()},
        ratio_acc_all=rat,
        understates_15pct_each_year=bool(all(rat[str(Y)]["ratio"] <= 0.85 for Y in POST)),
        falsified=bool(rat["2024"]["ratio"] >= 0.9 and rat["2025"]["ratio"] >= 0.9),
        robustness=kb[(kb.set == "ratio_acc_all")].to_dict(orient="records"),
    )
    # IUT p-values: '>= 15% understatement in each year' (max_Y P(ratio >= 0.85)) and direction (max_Y P(ratio >= 1))
    rr_ = kb[(kb.marker == "F24") & (kb.baseline == "cons") & (kb.set == "ratio_acc_all") & kb.year.isin(POST)]
    h4c["p_iut_ratio_le_0p85"] = float(rr_.p_ge_0p85.max())
    h4c["p_iut_ratio_lt_1"] = float(rr_.p_ge1.max())
    h4c["ratio_p_ge1"] = {str(x.year): float(x.p_ge1) for x in rr_.itertuples()}
    ph = kb[(kb.marker == "F24") & (kb.baseline == "max2122") & (kb.set == "ratio_acc_all") & kb.year.isin(POST)]
    h4c["posthoc_max2122"] = {str(x.year): dict(ratio=x.bound, lo95=x.lo95, hi95=x.hi95, p_ge_0p9=x.p_ge_0p9,
                                                p_ge1=x.p_ge1) for x in ph.itertuples()}
    h4c["falsified_under_posthoc_max2122"] = bool(all(h4c["posthoc_max2122"][str(Y)]["ratio"] >= 0.9
                                                      for Y in (2024, 2025)))
    res = dict(
        meta=dict(n_pairs=int(len(pairs)), pairs_by_decision=pairs.decision.value_counts().to_dict(),
                  pairs_by_year_decision={f"{k[0]}_{k[1]}": int(v) for k, v in
                                          pairs.groupby(["year", "decision"]).size().items()},
                  snapshot_source=("WP4 frozen primary audit (outputs/snapshot/audit_pairs.csv: original + complete "
                                   "enlargement, 2023-26); flip tables recomputed in d4_bias_atlas and checked "
                                   "against outputs/snapshot/T4_2_flip_matrices.csv (primary)"),
                  n_pairs_original_audit=int(len(pairs_orig)),
                  n_boot=N_BOOT, n_random_band_entropy_jsd=N_NULL, runtime_s=round(time.time() - t0, 1)),
        T4_2_flips=flips_all.to_dict(orient="records"), T4_2_bound=bound.to_dict(orient="records"),
        H4c=h4c, H4e=h4e, atlas=atlas.to_dict(orient="records"),
    )
    S.write_json(res, OUTDIR / "bias_atlas.json")
    log(f"done in {time.time() - t0:.0f}s", fh)
    fh.close()


if __name__ == "__main__":
    main()
