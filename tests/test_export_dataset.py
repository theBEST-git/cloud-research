from __future__ import annotations

import csv
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_dataset as ex


class ExportTests(unittest.TestCase):
    def row(self, **changes):
        r = {name: None for name in ex.SUBMISSION_FIELDS}
        r.update(submission_id="s1", family_id="f1", metadata_oid="o1", year=2019,
                 discovery_allowed=1, confirmation_allowed=0, administrative_status="ordinary_submission",
                 decision="unknown", decision_evidence="[]", outcome_eligible=0, keywords="[]")
        r.update(changes)
        return r

    def test_ids_and_email_suppression(self):
        a, status, n, m = ex.author_rows(self.row(), ["Author A", "Author B"], ["~A1", "a@example.com"])
        self.assertEqual((status, n, m), ("aligned_lists", 2, 2))
        self.assertEqual(a[0]["native_id"], "~A1")
        self.assertIsNone(a[1]["native_id"])
        self.assertEqual(a[1]["email_withheld"], 1)
        b = ex.author_rows(self.row(submission_id="s2"), ["Another"], ["a@example.com"])[0]
        self.assertEqual(a[1]["declared_id_key"], b[0]["declared_id_key"])

    def test_mismatched_lists_are_not_paired(self):
        a, status, n, m = ex.author_rows(self.row(), ["Name"], ["~A", "~B"])
        self.assertEqual((n, m), (1, 2))
        self.assertEqual(status, "list_length_mismatch")
        self.assertEqual(len(a), 2)
        self.assertTrue(all(x["name_id_alignment"] != "aligned_lists" for x in a))

    def test_missing_and_nontext_fields(self):
        self.assertEqual(ex.author_rows(self.row(), None, None)[0], [])
        a = ex.author_rows(self.row(), [123, None], [42, None])[0]
        self.assertEqual(a[0]["declared_name_json"], "123")
        self.assertEqual(a[0]["native_id_kind"], "other")
        self.assertEqual(a[1]["declared_id_state"], "null")
        self.assertEqual(ex.parse_field('{"value":["A"]}'), (["A"], "api2_value"))

    def test_keyword_join_checks(self):
        kw = dict(family_id="f1", year="2019", ordinary="True", normalized_keywords='["transformer"]')
        self.assertEqual(ex.reconcile_keyword(self.row(), kw)[0], '["transformer"]')
        for modified in (dict(kw, family_id="wrong"), dict(kw, year="2025"), dict(kw, normalized_keywords='["x","x"]')):
            with self.assertRaises(RuntimeError):
                ex.reconcile_keyword(self.row(), modified)

    def test_original_statuses_preserved(self):
        self.assertEqual(ex.keyword_status("null"), "missing_or_null")
        self.assertEqual(ex.keyword_status("[]"), "empty_list")
        self.assertEqual(ex.keyword_status('""'), "empty_string")
        self.assertEqual(ex.keyword_status('[1]'), "nontext_list")
        self.assertEqual(ex.keyword_status("not json"), "invalid_json")

    def test_outcome_patch_only_2019(self):
        patch = dict(decision="accepted", decision_evidence="[1]", outcome_eligible=1)
        r = ex.apply_patch(self.row(administrative_status="withdrawn"), patch)
        self.assertEqual(r["decision"], "accepted")
        self.assertEqual(r["base_decision"], "unknown")
        self.assertEqual(r["administrative_status"], "withdrawn")
        with self.assertRaises(RuntimeError):
            ex.apply_patch(self.row(year=2025), patch)

    def test_gzip_is_deterministic_and_keeps_null_empty(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as folder:
            files = [Path(folder) / "a.gz", Path(folder) / "b.gz"]
            for p in files:
                with ex.csv_writer(p, ("a", "b", "c")) as write:
                    write(dict(a=None, b="", c="line1\nline2"))
            self.assertEqual(files[0].read_bytes(), files[1].read_bytes())
            self.assertEqual(list(ex.rows(files[0])), [dict(a=None, b="", c="line1\nline2")])

    def test_readonly_database(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as folder:
            p = Path(folder) / "source.sqlite"
            c = sqlite3.connect(p)
            c.execute("CREATE TABLE t(x)")
            c.commit()
            c.close()

    def test_end_to_end_discovery_export_and_rebuild(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1]) as folder:
            root = Path(folder)
            clean, source, patch = [root / name / "source.sqlite" for name in ("clean", "official", "correction")]
            for p in (clean, source, patch):
                p.parent.mkdir()
            c = sqlite3.connect(clean)
            integer = {"year", "discovery_allowed", "confirmation_allowed", "outcome_eligible"}
            c.execute("CREATE TABLE submissions(" + ",".join(k + (" INTEGER" if k in integer else " TEXT") for k in ex.SUBMISSION_FIELDS) + ")")
            inputs = [self.row(), self.row(submission_id="s2", family_id="f2", metadata_oid="o2", year=2026),
                      self.row(submission_id="closed", title="DO_NOT_EXPORT", discovery_allowed=0, confirmation_allowed=1)]
            for r in inputs:
                c.execute("INSERT INTO submissions VALUES(" + ",".join("?" for _ in ex.SUBMISSION_FIELDS) + ")", [r[k] for k in ex.SUBMISSION_FIELDS])
            c.commit()
            c.close()
            c = sqlite3.connect(source)
            c.execute("CREATE TABLE observations(oid TEXT,source_id TEXT,source_type TEXT,nid TEXT,sid TEXT,location TEXT,captured TEXT,acquired TEXT,capture_status TEXT,stage_status TEXT,cdate INTEGER,mdate INTEGER,content_hash TEXT,content_json TEXT,kind TEXT)")
            c.execute("CREATE TABLE sources(source_id TEXT,path TEXT,url TEXT,license TEXT,sha256 TEXT)")
            c.execute("INSERT INTO sources VALUES('source','fixture','https://example.org/','unspecified','fixture_hash')")
            for oid, names, ids in (("o1", ["A", "B"], ["a@example.com"]), ("o2", ["C"], ["~C1"])):
                c.execute("INSERT INTO observations VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                          (oid,"source","official","native","snapshot","fixture_location",None,None,"unknown","unknown",None,None,"content_hash",json.dumps(dict(authors=names,authorids=ids)),"submission"))
            c.commit()
            c.close()
            c = sqlite3.connect(patch)
            c.execute("CREATE TABLE outcome_patch(submission_id TEXT,decision TEXT,decision_evidence TEXT,outcome_eligible INTEGER)")
            c.execute("INSERT INTO outcome_patch VALUES('s1','accepted','[]',1)")
            c.commit()
            c.close()
            for p in (clean, source, patch):
                ex.write_json(p.parent / "artifact_manifest.json", {"files":[{"path":p.name,"bytes":p.stat().st_size,"sha256":ex.sha(p)}]})
                ex.write_json(p.parent / "release_seal.json", {"manifest_sha256":ex.sha(p.parent / "artifact_manifest.json")})
            kw = root / "keywords" / "final" / "submission_keywords.csv"
            kw.parent.mkdir(parents=True)
            with kw.open("w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["submission_id","family_id","year","ordinary","normalized_keywords"])
                w.writeheader()
                for r in inputs[:2]:
                    w.writerow({k:r[k] for k in ("submission_id","family_id","year")} | {"ordinary":"True","normalized_keywords":"[]"})
            ex.write_json(kw.parent / "manifest.json", {"files":[{"path":kw.name,"bytes":kw.stat().st_size,"sha256":ex.sha(kw)}]})
            outputs = [root / "export_a", root / "export_b"]
            for out in outputs:
                ex.build(SimpleNamespace(clean=clean, upstream=source, patch=patch, keywords=kw, output=out))
            records = list(ex.rows(outputs[0] / "submissions.csv.gz"))
            self.assertEqual([r["submission_id"] for r in records], ["s1","s2"])
            self.assertEqual(records[0]["decision"], "accepted")
            self.assertEqual(records[0]["base_decision"], "unknown")
            self.assertEqual(records[0]["author_list_status"], "list_length_mismatch")
            for name in ("submissions.csv.gz","submission_authors.csv.gz","metadata_provenance.csv.gz"):
                self.assertEqual(ex.sha(outputs[0] / name), ex.sha(outputs[1] / name))
            # Tampering must invalidate reuse, rather than trusting the cached receipt.
            with (outputs[0] / "submissions.csv.gz").open("ab") as f:
                f.write(b"corrupt")
            with self.assertRaises(RuntimeError):
                ex.validate(outputs[0])
            c = ex.readonly(p)
            with self.assertRaises(sqlite3.OperationalError):
                c.execute("INSERT INTO t VALUES(1)")
            c.close()


if __name__ == "__main__":
    unittest.main()
