"""Audit check 2: G3/G4 abstract audit. (a) enlarge the abstract audit with the v1 abstracts the enlargement already
cached; (b) test a mechanical alternative for the positive F24 DiD: arXiv abstracts are capped (1,920 chars) and
written in TeX, so stored OpenReview abstracts can be longer; if accepted stored abstracts grow more vs v1, RARE21 adds
are a length artefact rather than LLM polishing. Read-only."""
from pathlib import Path
import numpy as np, pandas as pd, statsmodels.formula.api as smf
from analyses import snapshot_bounds as S
from analyses import _core as CORE
OUT = Path(__file__).resolve().parent
U = CORE.load_universe(["submission_id", "year", "title", "title_nfkc", "abstract", "ACC", "REJ"])
orig = S.read_jsonl(S.ORIG_PATH)
v1a = S.read_jsonl(S.V1ABS_PATH); v1a = v1a[v1a.error.isna()] if "error" in v1a else v1a
v1a = v1a.drop_duplicates("submission_id", keep="last")
o2 = orig.drop(columns=["v1_title", "v1_date"]).merge(v1a[["submission_id", "v1_title", "v1_date", "v1_summary"]], on="submission_id")
Pa = S.build_pairs(o2, U, "v1abs", v1_abstract=True)
enl = S.read_jsonl(S.ENLARGE_PATH); enl = enl[enl.error.isna()].drop_duplicates("submission_id", keep="last")
Pe = S.build_pairs(enl, U, "enlarge", v1_abstract=True)
keys_a = [k for k, *_ in S.ABS_FEATS]
df = S.universe_frame()
keys_t = [k for k, *_ in S.TITLE_FEATS]
sums = S.stage_prevalences(df, keys_t + keys_a, n_boot=500)
Ppool, apool = S.pooled(sums, S.POST)
Pa_t = Ppool[:, len(keys_t):]
# word counts of abstracts (v1 vs stored), recomputed from the raw text
U2 = U.set_index("submission_id")
def wc(s): return len(str(s).split())
res = []
for name, PP in {"orig_v1abs(reported)": Pa, "enlarge_only": Pe, "pooled": pd.concat([Pa, Pe], ignore_index=True)}.items():
    ft, db = S.flip_table(PP, keys_a, name)
    tp = S.tipping_table(Pa_t[:501], apool[:501], keys_a, ft, db[:500], "2024-26")
    for k in ["F24", "L_abs_words", "F26_words"]:
        f = ft.set_index("feature").loc[k]; t = tp.set_index("feature").loc[k]
        res.append(dict(spec=name, feat=k, n_acc=f.n_acc, n_rej=f.n_rej, v1p_acc=f.v1_present_acc, v1p_rej=f.v1_present_rej,
                        adds_acc=f.adds_acc, drops_acc=f.drops_acc, adds_rej=f.adds_rej, drops_rej=f.drops_rej,
                        did=100*f.did, lo=100*f.did_lo, hi=100*f.did_hi, tipT=t.tip_total_pp, GT=t.G_total_obs,
                        identT=t.G_total_identified, auditable=f.auditable))
R = pd.DataFrame(res); pd.set_option("display.width", 250)
print(R.round(3).to_string())
# length artefact
PP = pd.concat([Pa, Pe], ignore_index=True)
# need v1 summary text: rebuild from the sources
v1txt = pd.concat([v1a[["submission_id", "v1_summary"]], enl[["submission_id", "v1_summary"]]]).drop_duplicates("submission_id", keep="last").set_index("submission_id").v1_summary
PP["w_v1"] = PP.submission_id.map(v1txt).map(wc)
PP["w_or"] = PP.submission_id.map(U2.abstract).map(wc)
PP["dlogw"] = np.log(PP.w_or.clip(lower=1)) - np.log(PP.w_v1.clip(lower=1))
PP["c_v1"] = PP.submission_id.map(v1txt).str.len()
PP["c_or"] = PP.submission_id.map(U2.abstract).str.len()
PP["net_f24"] = PP.F24_or - PP.F24_v1
PP["add_f24"] = ((PP.F24_v1 == 0) & (PP.F24_or == 1)).astype(int)
print("\nabstract length by arm (words): ")
print(PP.groupby("decision")[["w_v1", "w_or", "dlogw", "c_v1", "c_or"]].mean().round(3))
print("share stored abstract > 1920 chars:", PP.groupby("decision").apply(lambda g: (g.c_or > 1920).mean()).round(3).to_dict())
print("share stored grew >10% words:", PP.groupby("decision").apply(lambda g: (g.dlogw > np.log(1.1)).mean()).round(3).to_dict())
print("F24 adds by growth bin:")
PP["grow"] = pd.cut(PP.dlogw, [-10, -0.05, 0.05, 0.2, 10], labels=["shrunk", "~same", "+5-20%", ">+20%"])
print(PP.groupby(["decision", "grow"]).agg(n=("add_f24", "size"), adds=("add_f24", "sum"), net=("net_f24", "mean")).to_string())
for f in ["net_f24 ~ acc", "net_f24 ~ acc + dlogw", "net_f24 ~ acc + dlogw + C(year)"]:
    m = smf.ols(f, PP).fit(cov_type="HC1")
    print(f, "acc coef %.4f se %.4f p %.3f" % (m.params["acc"], m.bse["acc"], m.pvalues["acc"]),
          ("dlogw %.4f (%.4f)" % (m.params["dlogw"], m.bse["dlogw"])) if "dlogw" in m.params else "")
# DiD restricted to pairs with near-identical length
sm = PP[PP.dlogw.abs() <= 0.05]
for dec, g in sm.groupby("decision"):
    print("near-same-length", dec, len(g), "net F24 pp %.2f" % (100 * g.net_f24.mean()), "adds", int(g.add_f24.sum()), "drops", int(((g.F24_v1 == 1) & (g.F24_or == 0)).sum()))
R.to_csv(OUT / "check2_abstract_audit.csv", index=False)
PP[["submission_id", "year", "decision", "w_v1", "w_or", "dlogw", "F24_v1", "F24_or", "abs_jacc"]].to_csv(OUT / "check2_abstract_pairs.csv", index=False)
