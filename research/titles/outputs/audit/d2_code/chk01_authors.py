"""Audit D2: author table structure (alignment, positions, kinds, family uniqueness)."""
import numpy as np, pandas as pd
from common import read_table
from analyses import d2_panel as P
a = read_table("submission_authors")
s = read_table("submissions")[["submission_id","year","family_id","split","declared_name_count","declared_id_count","author_list_status"]]
print("family unique:", s.family_id.is_unique, s.family_id.nunique(), len(s))
print(s.split.value_counts())
print(a.columns.tolist())
print(a.name_id_alignment.value_counts(dropna=False))
print(a.declared_id_state.value_counts(dropna=False))
print(pd.crosstab(a.year, a.native_id_kind.fillna("NA")))
# misaligned lists in 2021-26
m = a.merge(s[["submission_id","declared_name_count","declared_id_count"]], on="submission_id")
pp = m.groupby("submission_id").agg(year=("year","first"), npos=("source_list_position","size"), pmax=("source_list_position","max"),
    dnc=("declared_name_count","first"), dic=("declared_id_count","first"), al=("name_id_alignment","first"))
pp["contig"] = pp.npos == pp.pmax+1
print("contiguous positions:", pp.contig.mean())
pp["mis"] = pp.dnc != pp.dic
print(pd.crosstab(pp.year, pp.mis))
print(pd.crosstab(pp.year, pp.al))
# for misaligned papers, is pmax+1 equal to dnc or dic?
x = pp[pp.mis]
print("misaligned n", len(x), "pmax+1==dnc", (x.pmax+1==x.dnc).mean(), "pmax+1==dic", (x.pmax+1==x.dic).mean())
print(x.head(10))
