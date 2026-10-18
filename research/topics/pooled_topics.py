"""Topics for the pooled corpus, discovery ∪ confirmation, with every map frozen on discovery (POOLED_SPEC D2, D4).

Nothing is refitted on the pooled corpus. New (confirmation) papers are projected with the frozen discovery PCA in
output/topic_model.npz (assign_topics.project) and placed as below; discovery rows are copied verbatim from the
discovery files once their reproduction is asserted.
- k100 / fine / coarse: assign_topics.assign_projected with topic_model.npz (registered Confirmation step 1). The
  hindsight map mid_pooled and the k sweep's mid_k100 are that same KMeans fit: a new paper gets the raw index paired
  with its k100 code (a bijection on discovery, asserted).
- Alternative maps (k50, k75, k150, k200; seed_refit, balanced, early, middle, late): their centres were never saved,
  so the frozen fits are re-run (same k, seeds, n_init, max_iter, year-balanced weights and fitting years, on the same
  projection). Gate: the argmax labels of every discovery paper equal the saved labels (np.array_equal). A new paper
  takes argmax z·normalize(centres), the raw integer label as saved. If a gate fails, each topic's centre falls back
  to the normalised (weighted) mean of the map's fit-population discovery members (logged). The share of new papers
  whose label differs between the two conventions is reported either way.
- Stability (stable_papers variant): the middle level of evaluate_topics' refits REFIT_SEEDS (the first is the
  seed_refit fit). Each k100 topic's best-Jaccard refit cluster (evaluate_topics.matched) is frozen from discovery.
  Gate: the recomputed discovery mid_stability equals the saved one exactly. A new paper stays in refit r if its
  nearest refit-r centre is its k100 topic's match; mid_stability = mean over refits rounded to 3, as for discovery.
  coarse/fine stability (used by no analysis) stay empty for new papers, as does mid_stability if the gate fails.
- Labels (D4): pooled paper_contributions = discovery ∪ released labels (0 missing in the label columns, asserted).

Writes output_pooled/ in pooled order P (54,579 embedded papers): topic_assignments, k_sensitivity_assignments,
hindsight_assignments, paper_topic_stability and paper_contributions (.csv.gz, discovery schemas), split.csv.gz (kept
apart so the others keep their schemas), map_centroids.npz (re-derived centres), byte-identical copies of the frozen
files the analyses read (COPIES), and pooled_topics_report.json (gates, diagnostics, sha256 of every file). Every
discovery row is checked to be byte-identical to its line in the discovery file, and research/topics/output and every
FREEZE.json-listed file to be unchanged by the run. Outcome-free: content columns, embeddings and labels only.
Multithreaded KMeans sums make re-derived centres differ between runs by about 1e-16, so map_centroids.npz is not
byte-stable; the gates and every label file are (three runs gave byte-identical .csv.gz files).

    ICLR_CORPUS=pooled python research/topics/pooled_topics.py      (after keyword_map.py; ~15 min of KMeans refits)
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import shutil
import time
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from threadpoolctl import threadpool_info

from assign_topics import assign_projected, project
from build_topics import N_INIT_MID, SEEDS
from common import CORPUS, DISCOVERY_OUTPUT, ERAS, OUTPUT, ROOT, embedded_corpus, load_embeddings, write_csv_gz
from evaluate_topics import REFIT_SEEDS, matched
from hindsight_check import REFIT_SEEDS as SEED_REFIT
from k_sensitivity import K_VALUES

FREEZE = ROOT / "research" / "fashion" / "FREEZE.json"
COPIES = ["topic_catalog.csv", "keyword_types.csv", "topic_model.npz", "hindsight_check.json"]
TABLES = ["topic_assignments", "k_sensitivity_assignments", "hindsight_assignments", "paper_topic_stability",
          "paper_contributions"]
LABEL_COLUMNS = ["primary_type", "primary_class", "foundation_model", "uncertain"]
# alternative map column -> (source table, k, seeds, fitting years (None: all discovery), year-balanced weights)
MAPS = {**{f"mid_k{k}": ("k_sensitivity_assignments", k, SEEDS, None, False) for k in K_VALUES if k != 100},
        "mid_seed_refit": ("hindsight_assignments", 100, SEED_REFIT, None, False),
        "mid_balanced": ("hindsight_assignments", 100, SEEDS, None, True),
        "mid_early": ("hindsight_assignments", 100, SEEDS, ERAS["2017-2020"], False),
        "mid_middle": ("hindsight_assignments", 100, SEEDS, ERAS["2021-2023"], False),
        "mid_late": ("hindsight_assignments", 100, SEEDS, ERAS["2024-2026"], False)}
DRIFT_DRAWS, DRIFT_SEED = 200, 0
CODE_SUFFIXES = {".py", ".js", ".md"}


def centres(z: np.ndarray, k: int, seeds: tuple[int, ...], weight: np.ndarray | None = None) -> np.ndarray:
    """The frozen fitting procedure (build_topics, k_sensitivity, hindsight_check, evaluate_topics): best inertia over
    seeds x N_INIT_MID initialisations, unit-length centres."""
    km = min((KMeans(k, n_init=N_INIT_MID, random_state=s, max_iter=300).fit(z, sample_weight=weight) for s in seeds),
             key=lambda f: f.inertia_)
    return normalize(km.cluster_centers_)


def member_means(z: np.ndarray, labels: np.ndarray, k: int, weight: np.ndarray | None = None) -> np.ndarray:
    """Fallback centres: normalised (weighted) mean of each topic's fit-population members."""
    sums = np.zeros((k, z.shape[1]))
    np.add.at(sums, labels, z * (1.0 if weight is None else weight[:, None]))
    if (np.linalg.norm(sums, axis=1) == 0).any():
        raise RuntimeError("A topic has no fit-population member")
    return normalize(sums)


def best_match(final: np.ndarray, refit: np.ndarray) -> dict:
    """evaluate_topics.matched's best-Jaccard refit cluster of each final topic, as a refit label."""
    f_codes, f = np.unique(final, return_inverse=True)
    r_codes, r = np.unique(refit, return_inverse=True)
    inter = np.zeros((f.max() + 1, r.max() + 1))
    np.add.at(inter, (f, r), 1)
    jac = inter / (inter.sum(1, keepdims=True) + inter.sum(0, keepdims=True) - inter)
    return dict(zip(f_codes, r_codes[jac.argmax(axis=1)]))


def interleave(disc: pd.DataFrame, new: pd.DataFrame, is_new: np.ndarray) -> pd.DataFrame:
    """Discovery rows and new rows (each already in its split's P order) merged into pooled order P."""
    pos = np.empty(len(is_new), dtype=int)
    pos[~is_new], pos[is_new] = np.arange(len(disc)), len(disc) + np.arange(len(new))
    return pd.concat([disc, new], ignore_index=True).iloc[pos].reset_index(drop=True)


def same(a: pd.DataFrame, b: pd.DataFrame) -> bool:
    return list(a.columns) == list(b.columns) and len(a) == len(b) and all(
        np.array_equal(a[c].to_numpy(), b[c].to_numpy()) for c in a.columns)


def total_variation(a: np.ndarray, b: np.ndarray) -> float:
    pa, pb = pd.Series(a).value_counts(normalize=True), pd.Series(b).value_counts(normalize=True)
    return float(0.5 * pa.sub(pb, fill_value=0).abs().sum())


def drift(disc: np.ndarray, new: np.ndarray, rng: np.random.Generator) -> dict:
    """Topic-share total variation between the splits, against its sampling noise: two samples of the splits' sizes
    drawn from one set of shares (the discovery shares)."""
    shares = pd.Series(disc).value_counts(normalize=True)
    p, nd, nn = shares.to_numpy() / shares.sum(), len(disc), len(new)
    ref = [0.5 * np.abs(rng.multinomial(nd, p) / nd - rng.multinomial(nn, p) / nn).sum() for _ in range(DRIFT_DRAWS)]
    return {"tv_confirmation_vs_discovery": round(total_variation(disc, new), 4),
            "tv_sampling_noise_mean": round(float(np.mean(ref)), 4),
            "tv_sampling_noise_p95": round(float(np.quantile(ref, 0.95)), 4),
            "topics_used_discovery": int(pd.Series(disc).nunique()), "topics_used_confirmation": int(pd.Series(new).nunique())}


def stable_share(mid_stability: np.ndarray) -> float:
    return round(float((mid_stability >= 2 / 3 - 1e-9).mean()), 4)                    # `stable` as in panel.py


def lines(path: Path) -> list[str]:
    return gzip.decompress(path.read_bytes()).decode("utf-8").split("\n")


def rows_verbatim(pooled: Path, source: Path, mask: np.ndarray) -> bool:
    """The pooled file's header and its rows under mask are byte-identical to the source file's lines."""
    p, s = lines(pooled), lines(source)
    return p[0] == s[0] and p[-1] == s[-1] == "" and np.asarray(p[1:-1], dtype=object)[mask].tolist() == s[1:-1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_artefacts() -> list[str]:
    """FREEZE.json-listed data and output files (its code and documents are edited by other work, not by this run)."""
    return [p for p in json.loads(FREEZE.read_text())["sha256"] if Path(p).suffix not in CODE_SUFFIXES]


def protected() -> dict[str, str]:
    """sha256 of the files this run must not touch: research/topics/output/** and the frozen artefacts."""
    files = {p for p in DISCOVERY_OUTPUT.rglob("*") if p.is_file()} | {ROOT / p for p in frozen_artefacts()}
    return {str(p.relative_to(ROOT)): sha256(p) for p in sorted(files) if p.exists()}


def save_npz(path: Path, arrays: dict[str, np.ndarray]) -> None:
    """Compressed .npz with fixed zip timestamps, so equal arrays give byte-identical files."""
    with zipfile.ZipFile(path, "w") as zf:
        for name, a in arrays.items():
            buf = io.BytesIO()
            np.lib.format.write_array(buf, np.ascontiguousarray(a), allow_pickle=False)
            zf.writestr(zipfile.ZipInfo(f"{name}.npy", date_time=(1980, 1, 1, 0, 0, 0)), buf.getvalue(),
                        compress_type=zipfile.ZIP_DEFLATED)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--reuse-centroids", action="store_true",
                    help="take the re-derived centres from output_pooled/map_centroids.npz (the gates still apply)")
    args = ap.parse_args()
    if CORPUS != "pooled" or OUTPUT.resolve() == DISCOVERY_OUTPUT.resolve():
        raise SystemExit("Run with ICLR_CORPUS=pooled (writes research/topics/output_pooled only)")
    OUTPUT.mkdir(exist_ok=True)
    before, t0 = protected(), time.time()

    corpus = embedded_corpus()
    emb, ids = load_embeddings()
    if not ids.equals(corpus.submission_id):
        raise RuntimeError("Pooled embeddings and corpus are not aligned")
    is_new = (corpus.split == "confirmation").to_numpy()
    disc_ids = corpus.submission_id[~is_new].reset_index(drop=True)
    new_ids = corpus.submission_id[is_new].reset_index(drop=True)
    saved = {t: pd.read_csv(DISCOVERY_OUTPUT / f"{t}.csv.gz", dtype={"submission_id": str}) for t in TABLES}
    for t, df in saved.items():
        if not df.submission_id.equals(disc_ids):
            raise RuntimeError(f"{t} is not in the discovery order")
    released = pd.read_csv(DISCOVERY_OUTPUT / "paper_contributions_released.csv.gz", dtype={"submission_id": str})
    if not released.submission_id.equals(new_ids):
        raise RuntimeError("Released labels are not in the confirmation embedded order")
    model = np.load(DISCOVERY_OUTPUT / "topic_model.npz")
    emb = emb.astype(np.float64)
    zd, zn = project(emb[~is_new], model), project(emb[is_new], model)    # discovery z exactly as the frozen fits saw it
    years = corpus.year.to_numpy()[~is_new]
    report = {"corpus": {"embedded_papers": len(corpus), "discovery": len(disc_ids), "confirmation": len(new_ids),
                         "papers_by_year": {s: {int(y): int(n) for y, n in g.year.value_counts().sort_index().items()}
                                            for s, g in corpus.groupby("split")},
                         "discovery_subset_of_P_is_discovery_order": True}}

    # k100 / fine / coarse from the saved model
    ta = saved["topic_assignments"]
    kd, kn = assign_projected(zd, model), assign_projected(zn, model)
    if not same(kd, ta.drop(columns=["submission_id", "year"])):
        raise RuntimeError("topic_model.npz does not reproduce the discovery topic assignments")
    new_ta = pd.concat([corpus.loc[is_new, ["submission_id", "year"]].reset_index(drop=True), kn], axis=1)
    member, codes = pd.factorize(ta.mid, sort=True)
    k100_member = member_means(zd, member, 100)
    report["k100"] = {"discovery_reproduced_exactly": True,
                      "levels": {lvl: drift(ta[lvl].to_numpy(), kn[lvl].to_numpy(), np.random.default_rng(DRIFT_SEED))
                                 for lvl in ("coarse", "mid", "fine")},
                      "mean_mid_similarity": {"discovery": round(float(ta.mid_similarity.mean()), 4),
                                              "confirmation": round(float(kn.mid_similarity.mean()), 4)},
                      "share_mid_margin_below_0.01": {"discovery": round(float((ta.mid_margin < 0.01).mean()), 4),
                                                      "confirmation": round(float((kn.mid_margin < 0.01).mean()), 4)},
                      "confirmation_mid_differs_npz_vs_all_member_means":
                          round(float((codes.to_numpy()[(zn @ k100_member.T).argmax(1)] != kn.mid.to_numpy()).mean()), 4)}

    # alternative maps: re-derived exact centres, gated on the saved discovery labels
    ks, hs = saved["k_sensitivity_assignments"], saved["hindsight_assignments"]
    pair = pd.DataFrame({"mid": ta.mid, "raw": hs.mid_pooled}).drop_duplicates()
    if not (ks.mid_k100.equals(hs.mid_pooled) and len(pair) == 100 and pair.mid.is_unique and pair.raw.is_unique
            and kn.mid.isin(pair.mid).all()):
        raise RuntimeError("mid_pooled / mid_k100 are not a bijection with the k100 codes")
    raw_of = dict(zip(pair.mid, pair.raw))
    new_maps = {"mid_k100": kn.mid.map(raw_of).to_numpy(), "mid_pooled": kn.mid.map(raw_of).to_numpy()}
    reuse = dict(np.load(OUTPUT / "map_centroids.npz")) if args.reuse_centroids else {}
    fits, fit_names, report["maps"] = {}, {}, {}
    counts = pd.Series(years).value_counts()
    for col, (table, k, seeds, era, balanced) in MAPS.items():
        t = time.time()
        fit = np.ones(len(zd), bool) if era is None else (years >= era[0]) & (years <= era[1])
        weight = 1.0 / pd.Series(years).map(counts).to_numpy() if balanced else None    # as hindsight_check
        key = (k, tuple(seeds), era, balanced)
        if key not in fits:
            fits[key] = reuse[col] if col in reuse else centres(zd[fit], k, seeds, weight)
            fit_names[key] = col
        c, labels = fits[key], saved[table][col].to_numpy()
        exact = bool(np.array_equal((zd @ c.T).argmax(1), labels))
        mm = member_means(zd[fit], labels[fit], k, None if weight is None else weight[fit])
        exact_new, mm_new = (zn @ c.T).argmax(1), (zn @ mm.T).argmax(1)
        new_maps[col] = exact_new if exact else mm_new
        report["maps"][col] = {"k": k, "seeds": list(seeds), "fit_years": list(era) if era else "all discovery",
                               "year_balanced_weights": balanced, "fit_papers": int(fit.sum()),
                               "gate_discovery_labels_reproduced": exact,
                               "convention": "exact re-derived centres" if exact else "FALLBACK fit-population member means",
                               "member_mean_discovery_agreement": round(float(((zd @ mm.T).argmax(1) == labels).mean()), 4),
                               "confirmation_label_differs_exact_vs_member_mean": round(float((exact_new != mm_new).mean()), 4),
                               **drift(labels, new_maps[col], np.random.default_rng(DRIFT_SEED)),
                               "seconds": round(time.time() - t, 1)}
        print(col, json.dumps(report["maps"][col]), flush=True)

    # stability: refits' middle level, matches frozen from discovery
    stab, final = saved["paper_topic_stability"], ta.mid.to_numpy()
    stay_d, stay_n, report["stability"] = [], [], {"refit_seeds": [list(s) for s in REFIT_SEEDS]}
    for seeds in REFIT_SEEDS:
        key = (100, tuple(seeds), None, False)
        if key not in fits:
            name = "refit_" + "_".join(map(str, seeds))
            fits[key] = reuse[name] if name in reuse else centres(zd, 100, seeds)
            fit_names[key] = name
        labels = (zd @ fits[key].T).argmax(1)
        best = best_match(final, labels)
        _, stay = matched(final, labels)
        if not np.array_equal(stay, labels == pd.Series(final).map(best).to_numpy()):
            raise RuntimeError("best_match disagrees with evaluate_topics.matched")
        if tuple(seeds) == tuple(SEED_REFIT):
            report["stability"]["refit_1_equals_mid_seed_refit"] = bool(np.array_equal(labels, hs.mid_seed_refit.to_numpy()))
        stay_d.append(stay)
        stay_n.append((zn @ fits[key].T).argmax(1) == kn.mid.map(best).to_numpy())
    gate = bool(np.array_equal(np.mean(stay_d, axis=0).round(3), stab.mid_stability.to_numpy()))
    mid_new = np.mean(stay_n, axis=0).round(3) if gate else np.full(len(zn), np.nan)
    report["stability"] |= {"gate_discovery_mid_stability_reproduced": gate,
                            "convention": "exact refit centres" if gate else "FALLBACK: empty for new papers",
                            "mean_mid_stability": {"discovery": round(float(stab.mid_stability.mean()), 4),
                                                   "confirmation": round(float(np.nanmean(mid_new)), 4) if gate else None},
                            "stable_share": {"discovery": stable_share(stab.mid_stability.to_numpy()),
                                             "confirmation": stable_share(mid_new) if gate else None}}

    # pooled tables (discovery rows verbatim), split, labels
    head = new_ta[["submission_id", "year"]]
    new_rows = {"topic_assignments": new_ta,
                "k_sensitivity_assignments": head.assign(**{c: new_maps[c] for c in ks.columns[2:]}),
                "hindsight_assignments": head.assign(**{c: new_maps[c] for c in hs.columns[2:]}),
                "paper_topic_stability": pd.DataFrame({"submission_id": new_ids, "coarse_stability": np.nan,
                                                       "mid_stability": mid_new, "fine_stability": np.nan}),
                "paper_contributions": released}
    out = {t: interleave(saved[t], new_rows[t], is_new) for t in TABLES}
    for t, df in out.items():
        if list(df.columns) != list(saved[t].columns) or not df.submission_id.equals(corpus.submission_id):
            raise RuntimeError(f"pooled {t} is not in pooled order P with the discovery columns")
    missing = out["paper_contributions"][LABEL_COLUMNS].isna().sum()
    if missing.any():
        raise RuntimeError(f"missing labels: {missing.to_dict()}")
    for t, df in out.items():
        write_csv_gz(df, OUTPUT / f"{t}.csv.gz")
    write_csv_gz(corpus[["submission_id", "split"]], OUTPUT / "split.csv.gz")
    save_npz(OUTPUT / "map_centroids.npz", {fit_names[k]: c for k, c in fits.items()})
    for name in COPIES:
        shutil.copyfile(DISCOVERY_OUTPUT / name, OUTPUT / name)

    # checks on the written files
    verbatim = {t: rows_verbatim(OUTPUT / f"{t}.csv.gz", DISCOVERY_OUTPUT / f"{t}.csv.gz", ~is_new) for t in TABLES}
    verbatim["paper_contributions (released rows)"] = rows_verbatim(
        OUTPUT / "paper_contributions.csv.gz", DISCOVERY_OUTPUT / "paper_contributions_released.csv.gz", is_new)
    copies = {name: sha256(OUTPUT / name) == sha256(DISCOVERY_OUTPUT / name) for name in COPIES}
    after = protected()
    freeze, common_py = json.loads(FREEZE.read_text())["sha256"], "research/topics/common.py"
    report["checks"] = {"discovery_rows_byte_identical": verbatim, "copies_byte_identical": copies,
                        "protected_files_unchanged": after == before, "protected_files": len(after),
                        "label_columns_missing": {c: int(v) for c, v in missing.items()},
                        "frozen_artefacts_match_FREEZE_json": all(after.get(p) == freeze[p] for p in frozen_artefacts()),
                        "topics_common_py_matches_FREEZE_json": sha256(ROOT / common_py) == freeze[common_py]}
    if not (all(verbatim.values()) and all(copies.values()) and after == before):
        raise RuntimeError(f"output checks failed: {json.dumps(report['checks'])}")
    report["files"] = {p.name: sha256(p) for p in sorted(OUTPUT.iterdir())
                       if p.is_file() and p.name != "pooled_topics_report.json"}
    report["map_centroid_sha256"] = {fit_names[k]: hashlib.sha256(np.ascontiguousarray(c).tobytes()).hexdigest()
                                     for k, c in fits.items()}
    report["environment"] = {"numpy": np.__version__, "pandas": pd.__version__, "sklearn": sklearn.__version__,
                             "reused_centroids": bool(args.reuse_centroids), "seconds": round(time.time() - t0),
                             "threadpools": [{k: i[k] for k in ("user_api", "internal_api", "num_threads")}
                                             for i in threadpool_info()]}
    (OUTPUT / "pooled_topics_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("corpus", "stability", "checks")}, indent=1))


if __name__ == "__main__":
    main()
