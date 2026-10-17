"""PH5 cleantext (robustness of the PH5 pivot and position results to post-decision text). Abstracts are the
OpenReview versions after the decision, and accepted papers often add a de-anonymised code link or a "code is
available" sentence (output/posthoc/ph5_fmwave/code_links.csv). Both the novelty of a paper (position) and its distance
from the authors' earlier papers (pivot) are measured on SPECTER2 vectors of that text, so a link shared between a
lab's accepted papers could move a paper towards its authors' earlier work or away from the field.

This module re-runs the declared families of ph5_pivot (E1-E4) and ph5_position (Family 1, P1a-P7, with the same 200
calibration nulls) unchanged, except that every vector comes from research/topics/embed_specter2_clean.py: URLs and
code/data-availability sentences removed from every abstract, the changed papers re-embedded with the same model, all
other rows identical. The frozen reference points (ph5_pivot.REF) and every other input stay as they were, so the only
difference from the committed runs is the text. Post hoc and exploratory, like the analyses it checks.

Outputs: tests (both families, clean vectors, next to the committed estimates), shift (how much each feature moved),
reference_points (ph5_pivot.REF recomputed on the clean vectors; reported, not used), summary.
"""
from __future__ import annotations

import hashlib
import json
from functools import lru_cache
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd

import panel
import ph5_pivot
import ph5_position
from common import OUTPUT, ROOT

CACHE = ROOT / "research" / "topics" / "cache"
CLEAN, CHANGED = CACHE / "specter2_clean.npy", CACHE / "specter2_clean_changed.csv"
CLEAN_SHA256 = "f4a2af266b56dbcafecfbcf4cfedd6f1beb893a13e0604fd10ee520572bd6aa4"   # frozen before the run (PREREGISTRATION.md)
COMMITTED = {"pivot": OUTPUT / "posthoc" / "ph5_pivot" / "tests.csv",
             "position": OUTPUT / "posthoc" / "ph5_position" / "tests.csv"}
KEY = {"pivot": ("E1", "E4"), "position": ("P1b", "P7")}   # the results the robustness check is about
NOTE = ("post hoc exploratory (PH5 cleantext); the PH5 pivot and position families on URL- and availability-stripped "
        "SPECTER2 vectors; associations, not causal effects")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 22), b""):
            h.update(block)
    return h.hexdigest()


def _load_clean() -> tuple[np.ndarray, pd.Series]:
    return np.load(CLEAN), pd.read_csv(CACHE / "specter2_ids.csv").submission_id


@lru_cache(maxsize=1)
def _clean_embeddings() -> np.ndarray:
    """ph5_position.embeddings() on the clean vectors (same centring and normalisation)."""
    X, ids = _load_clean()
    assert (ids.to_numpy() == panel.frame("k100").submission_id.to_numpy()).all()
    X = X.astype(np.float32) - np.load(OUTPUT / "specter2_centring_mean.npy").astype(np.float32)
    return X / np.linalg.norm(X, axis=1, keepdims=True)


_ORIGINAL = {"topic_layer": ph5_pivot.topic_layer, "embeddings": ph5_position.embeddings}


def use(clean: bool) -> None:
    """Point ph5_pivot and ph5_position at the clean (or the original) vectors and clear their feature caches."""
    ph5_pivot.topic_layer = (lambda: SimpleNamespace(load_embeddings=_load_clean)) if clean else _ORIGINAL["topic_layer"]
    ph5_position.embeddings = _clean_embeddings if clean else _ORIGINAL["embeddings"]
    ph5_pivot.features.cache_clear()
    ph5_position.build.cache_clear()


def pivot_tests(k: pd.DataFrame) -> pd.DataFrame:
    """ph5_pivot's declared family (E1-E4, Holm over the four) on the current vectors."""
    _, ar = ph5_pivot.features()
    tests, _, _ = ph5_pivot.declared(ph5_pivot.population(ph5_pivot.prepare(k)), ar)
    return tests


def position_tests(k: pd.DataFrame, nulls: int = ph5_position.NULLS) -> pd.DataFrame:
    """ph5_position's Family 1 (P1a-P7, calibrated p for P3-P7, Holm over the eight) on the current vectors."""
    d = ph5_position.design(ph5_position.population(ph5_position.prepare(k)))
    tests, _ = ph5_position.declared(d)
    return ph5_position.calibrated_p(d, tests, np.random.default_rng(ph5_position.SEED), nulls)


def features() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Pivot distances and position novelty under the current vectors (paper level, panel.frame('k100') order)."""
    f, _ = ph5_pivot.features()
    b, _ = ph5_position.build()
    return f[["submission_id", "F_max", "n_exp"]], b[["submission_id", "nov", "pct", "twins_070"]]


def shift(orig: tuple[pd.DataFrame, pd.DataFrame], clean: tuple[pd.DataFrame, pd.DataFrame],
          changed: np.ndarray, year: np.ndarray) -> pd.DataFrame:
    """How far each feature moved, 2019-2026 submissions (all, and the papers whose own text changed)."""
    rows = []
    sel = (year >= 2019)
    for (name, a), (_, b) in zip([("pivot", orig[0]), ("position", orig[1])], [("pivot", clean[0]), ("position", clean[1])]):
        for col in a.columns[1:]:
            for group, m in [("all", sel), ("text changed", sel & changed), ("text unchanged", sel & ~changed)]:
                x, y = a[col].to_numpy(float)[m], b[col].to_numpy(float)[m]
                ok = np.isfinite(x) & np.isfinite(y)
                rows.append({"analysis": name, "feature": col, "papers": group, "n": int(ok.sum()),
                             "corr": float(np.corrcoef(x[ok], y[ok])[0, 1]) if ok.sum() > 2 else np.nan,
                             "mean_abs_diff": float(np.abs(x[ok] - y[ok]).mean()) if ok.any() else np.nan,
                             "share_changed": float((x[ok] != y[ok]).mean()) if ok.any() else np.nan})
        if name == "position":
            q = lambda p: np.minimum((p * 5).astype(int), 4)   # noqa: E731 (quintile of the cell percentile)
            m = sel & np.isfinite(a.pct.to_numpy()) & np.isfinite(b.pct.to_numpy())
            rows.append({"analysis": name, "feature": "novelty quintile", "papers": "all", "n": int(m.sum()),
                         "share_changed": float((q(a.pct.to_numpy()[m]) != q(b.pct.to_numpy()[m])).mean())})
    return pd.DataFrame(rows)


def compare(clean: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """The clean-vector estimates next to the committed ones."""
    out = []
    for name, t in clean.items():
        c = pd.read_csv(COMMITTED[name]).set_index("test")
        for _, r in t.iterrows():
            o = c.loc[r.test]
            out.append({"analysis": name, "test": r.test, "label": r.label, "key": r.test in KEY[name],
                        "coef_committed": o.coef, "p_holm_committed": o.p_holm,
                        "coef_clean": r.coef, "se_clean": r.se, "ci95_lo_clean": r.ci95_lo, "ci95_hi_clean": r.ci95_hi,
                        "p_clean": r.p, "p_calibrated_clean": r.get("p_calibrated", np.nan),
                        "p_twoway_clean": r.get("p_twoway", np.nan), "p_holm_clean": r.p_holm, "n_clean": r.n,
                        "same_sign": bool(np.sign(r.coef) == np.sign(o.coef)),
                        "ratio": float(r.coef / o.coef) if o.coef else np.nan})
    return pd.DataFrame(out)


def verdict(row: pd.Series) -> str:
    """Declared reading of a key test: holds (same sign, Holm p < .05), attenuated (same sign, Holm p >= .05, the clean
    95% CI contains half the committed estimate or more), or does not hold."""
    if row.same_sign and row.p_holm_clean < 0.05:
        return "holds"
    lo, hi = sorted((row.ci95_lo_clean, row.ci95_hi_clean))
    if row.same_sign and (lo <= row.coef_committed / 2 <= hi or lo <= row.coef_committed <= hi):
        return "attenuated"
    return "does not hold"


def compute(k: pd.DataFrame, nulls: int = ph5_position.NULLS, check_hash: bool = True) -> dict:
    if check_hash:
        assert CLEAN_SHA256 and sha256(CLEAN) == CLEAN_SHA256, "specter2_clean.npy is not the declared file"
    k = k.reset_index(drop=True)
    ids = set(pd.read_csv(CHANGED).submission_id)
    changed = k.submission_id.isin(ids).to_numpy()
    use(False)
    orig = features()
    use(True)
    try:
        clean_f = features()
        tests = {"pivot": pivot_tests(k), "position": position_tests(k, nulls)}
        f, ar = ph5_pivot.features()
        ref = ph5_pivot.reference_points(f, ar, k.year)
    finally:
        use(False)
    table = compare(tests)
    table["verdict"] = [verdict(r) if r.key else "" for _, r in table.iterrows()]
    decided = k.rq3.astype(bool).to_numpy() & (k.year >= 2019).to_numpy()
    acc = k.accepted.to_numpy(float)
    summary = {
        "clean_sha256": sha256(CLEAN), "papers_text_changed": int(changed.sum()),
        "text_changed_share_2019_2026_decided": {"accepted": float(changed[decided & (acc == 1)].mean()),
                                                 "rejected": float(changed[decided & (acc == 0)].mean())},
        "key_tests": table[table.key][["analysis", "test", "coef_committed", "coef_clean", "p_holm_committed",
                                       "p_holm_clean", "verdict"]].to_dict("records"),
        "note": NOTE}
    return {"tests": table, "shift": shift(orig, clean_f, changed, k.year.to_numpy()), "reference_points": ref,
            "summary": summary}


def plot(out_dir: Path) -> None:
    """Committed vs clean estimates of both families (95% CI of the clean run)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    t = pd.read_csv(out_dir / "tests.csv")
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), gridspec_kw={"width_ratios": [4, 8]})
    for ax, (name, g) in zip(axes, t.groupby("analysis", sort=False)):
        scale = 100.0
        y = np.arange(len(g))[::-1]
        ax.axvline(0, color="#888", lw=0.8)
        ax.errorbar(g.coef_clean * scale, y - 0.12, xerr=[(g.coef_clean - g.ci95_lo_clean) * scale,
                                                          (g.ci95_hi_clean - g.coef_clean) * scale],
                    fmt="o", ms=5, color="#2a6fbb", lw=1.5, label="clean text")
        ax.plot(g.coef_committed * scale, y + 0.12, "s", ms=5, color="#999", label="committed run")
        ax.set_yticks(y, [f"{a}{' *' if k else ''}" for a, k in zip(g.test, g.key)])
        ax.set_title(f"PH5 {name}", fontsize=10)
        ax.set_xlabel("estimate (pp)")
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[0].legend(frameon=False, fontsize=8, loc="lower left")
    fig.suptitle("Robustness to post-decision text (URLs and availability sentences removed); * = key test",
                 fontsize=10)
    fig.tight_layout()
    for ext in ("pdf", "png"):
        fig.savefig(out_dir / f"PH5_cleantext.{ext}", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    print(json.dumps({"clean_sha256": sha256(CLEAN), "changed": int(len(pd.read_csv(CHANGED)))}))
