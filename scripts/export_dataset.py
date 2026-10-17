"""Export the existing discovery corpus; no acquisition or experimental inputs."""
from __future__ import annotations

import argparse
import collections
import contextlib
import csv
import gzip
import hashlib
import io
import json
import os
import shutil
import sqlite3
import sys
from pathlib import Path

VERSION = "iclr-author-inputs-v1"
NULL = "\\N"
SUBMISSION_FIELDS = (
    "submission_id", "year", "cohort", "forum_ids", "title", "abstract",
    "keywords", "primary_area", "metadata_oid", "administrative_status",
    "decision", "decision_evidence", "family_id", "split", "discovery_allowed",
    "confirmation_allowed", "split_issue", "review_count", "distinct_reviewers",
    "similarity_eligible", "disagreement_eligible", "outcome_eligible",
)
EXTRA_FIELDS = (
    "base_decision", "base_outcome_eligible", "outcome_source_release",
    "normalized_keywords_json", "keyword_assignment_status", "keyword_field_status",
    "author_metadata_status", "author_list_status", "declared_name_count",
    "declared_id_count",
)
AUTHOR_FIELDS = (
    "submission_id", "family_id", "year", "metadata_oid", "source_list_position",
    "declared_name_json", "native_id", "native_id_kind", "declared_id_key",
    "name_id_alignment", "declared_id_state", "email_withheld",
)
PROVENANCE_FIELDS = (
    "submission_id", "metadata_oid", "source_id", "source_type", "native_note_id",
    "snapshot_id", "source_record_location", "captured", "acquired", "capture_status",
    "stage_status", "creation_ms", "modification_ms", "content_hash",
    "source_url", "source_license", "source_file_sha256", "author_field_shape",
    "authorid_field_shape",
)
MAX_NEW_BYTES = 512 * 2**20
FREE_RESERVE = 50 * 2**30
CUMULATIVE_CAP = 200 * 2**30


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(2**20), b""):
            h.update(block)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def readonly(path):
    path = Path(path).resolve()
    wal = Path(str(path) + "-wal")
    if wal.exists() and wal.stat().st_size:
        raise RuntimeError("Nonempty source WAL")
    c = sqlite3.connect(path.as_uri() + "?mode=ro&immutable=1", uri=True)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA query_only=ON")
    c.execute("PRAGMA cache_size=-16384")
    return c


def receipt(db):
    db = Path(db)
    folder = db.parent
    seal = read_json(folder / "release_seal.json")
    manifest = folder / "artifact_manifest.json"
    expected = seal.get("manifest_sha256", seal.get("artifact_manifest_sha256"))
    if sha(manifest) != expected:
        raise RuntimeError("Sealed source manifest mismatch: " + folder.name)
    entries = read_json(manifest)["files"]
    entry = next(r for r in entries if r["path"] == db.name)
    if entry["bytes"] != db.stat().st_size:
        raise RuntimeError("Sealed database size mismatch: " + db.name)
    return {
        "release": folder.name, "database": db.name, "database_bytes": db.stat().st_size,
        "database_mtime_ns": db.stat().st_mtime_ns, "sealed_database_sha256": entry["sha256"],
        "manifest_sha256": sha(manifest), "seal_sha256": sha(folder / "release_seal.json"),
        "verification": "manifest/seal rehashed; database size and mtime recorded; no full database rehash",
    }


def keyword_receipt(path):
    path = Path(path)
    entry = next(r for r in read_json(path.parent / "manifest.json")["files"] if r["path"] == path.name)
    if sha(path) != entry["sha256"] or path.stat().st_size != entry["bytes"]:
        raise RuntimeError("Canonical keyword input changed")
    return {"release": path.parent.parent.name + "/" + path.parent.name,
            "file": path.name, "sha256": entry["sha256"], "bytes": entry["bytes"]}


def unwrap(value):
    return value["value"] if isinstance(value, dict) and "value" in value else value


def parse_field(raw):
    if raw is None:
        return None, "absent"
    try:
        value = json.loads(raw)
    except (ValueError, TypeError):
        return raw, "invalid_json"
    shape = "api2_value" if isinstance(value, dict) and "value" in value else "api1_direct"
    return unwrap(value), shape


def keyword_status(raw):
    value, state = parse_field(raw)
    if state == "invalid_json":
        return state
    if value is None:
        return "missing_or_null"
    if isinstance(value, list):
        if not value:
            return "empty_list"
        return "text_list" if all(isinstance(v, str) for v in value) else "nontext_list"
    if isinstance(value, str):
        return "empty_string" if not value.strip() else "string"
    return "nontext_value"


def author_rows(row, names, ids):
    names_are_list = isinstance(names, list)
    ids_are_list = isinstance(ids, list)
    ns, xs = names if names_are_list else [], ids if ids_are_list else []
    aligned = bool(ns) and names_are_list and ids_are_list and len(ns) == len(xs)
    status = "aligned_lists" if aligned else "list_length_mismatch" if names_are_list and ids_are_list else "missing_or_nonlist_field"
    result = []
    for position in range(max(len(ns), len(xs))):
        name = ns[position] if position < len(ns) else None
        raw = xs[position] if position < len(xs) else None
        has_email = isinstance(raw, str) and "@" in raw
        name_email = isinstance(name, str) and "@" in name
        kind = "email" if has_email else "profile" if isinstance(raw, str) and raw.startswith("~") else "missing" if raw is None else "other"
        token = "native_" + hashlib.sha256(canonical(["declared-id-v1", raw]).encode()).hexdigest() if raw is not None else None
        result.append({
            "submission_id": row["submission_id"], "family_id": row["family_id"], "year": row["year"],
            "metadata_oid": row["metadata_oid"], "source_list_position": position,
            "declared_name_json": canonical(None if name_email else name),
            "native_id": raw if isinstance(raw, str) and not has_email else None,
            "native_id_kind": kind, "declared_id_key": token,
            "name_id_alignment": "aligned_lists" if aligned else "unresolved_not_a_verified_name_id_pair",
            "declared_id_state": "absent_position" if position >= len(xs) else "null" if raw is None else "text" if isinstance(raw, str) else "nontext",
            "email_withheld": int(has_email or name_email),
        })
    return result, status, len(ns), len(xs)


@contextlib.contextmanager
def csv_writer(path, fields):
    # Fixed gzip header makes unchanged inputs byte reproducible.
    with Path(path).open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=6) as gz:
            with io.TextIOWrapper(gz, encoding="utf-8", newline="") as text:
                writer = csv.DictWriter(text, fieldnames=fields, lineterminator="\n", extrasaction="raise")
                writer.writeheader()
                def write(row):
                    if any(row.get(k) == NULL for k in fields):
                        raise RuntimeError("Literal value conflicts with CSV null sentinel")
                    writer.writerow({k: NULL if row.get(k) is None else row[k] for k in fields})
                yield write


def rows(path):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            yield {k: None if v == NULL else v for k, v in row.items()}


def reconcile_keyword(row, kw):
    if kw is None:
        return None, "not_in_frozen_keyword_export"
    if kw["family_id"] != row["family_id"] or int(kw["year"]) != row["year"]:
        raise RuntimeError("Keyword submission/family/year join conflict")
    if (kw["ordinary"] == "True") != (row["administrative_status"] == "ordinary_submission"):
        raise RuntimeError("Keyword administrative-status join conflict")
    value = json.loads(kw["normalized_keywords"])
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value) or len(set(value)) != len(value):
        raise RuntimeError("Frozen keyword list is not a unique text list")
    return canonical(value), "existing_frozen_cleaning_assignment"


def apply_patch(row, patched):
    row = dict(row)
    row["base_decision"] = row["decision"]
    row["base_outcome_eligible"] = row["outcome_eligible"]
    row["outcome_source_release"] = "eda_ready_20260913T143255Z"
    if patched:
        if row["year"] != 2019:
            raise RuntimeError("Outcome correction outside 2019")
        for name in ("decision", "decision_evidence", "outcome_eligible"):
            row[name] = patched[name]
        row["outcome_source_release"] = "outcome_repair_20260923T104907Z"
    return row


def check_storage(folder):
    used = sum(p.stat().st_size for p in Path(folder).rglob("*") if p.is_file())
    if used > MAX_NEW_BYTES or shutil.disk_usage(folder).free < FREE_RESERVE:
        raise RuntimeError("Package storage/free-space limit reached")


def tree_bytes(folder):
    total = 0
    if not Path(folder).exists():
        return total
    for root, dirs, files in os.walk(folder, followlinks=False):
        dirs[:] = [d for d in dirs if not Path(root, d).is_symlink()]
        for name in files:
            p = Path(root, name)
            if not p.is_symlink():
                total += p.stat().st_size
    return total


SPLITS = {"discovery": ("discovery_allowed=1", "discovery submissions, ICLR 2017–2026; no confirmation candidates"),
          "confirmation": ("confirmation_allowed=1", "confirmation (held-out) submissions, ICLR 2017–2026; no discovery submissions")}


def build(args):
    split = getattr(args, "split", "discovery") or "discovery"
    where, scope = SPLITS[split]
    clean, upstream, patch, kw_path = map(Path, (args.clean, args.upstream, args.patch, args.keywords))
    out = Path(args.output).resolve()
    if out.exists():
        raise RuntimeError("Refusing to overwrite an existing data export")
    out.mkdir(parents=True)
    roots = [clean.parent.parent.resolve(), kw_path.parent.parent.parent.resolve(),
             Path(__file__).resolve().parents[2] / "research" / "author_experience"]
    unique_roots = [p for p in set(roots) if not any(p != q and p.is_relative_to(q) for q in roots)]
    baseline = sum(tree_bytes(p) for p in unique_roots)
    if baseline + MAX_NEW_BYTES > CUMULATIVE_CAP:
        raise RuntimeError("Insufficient cumulative Phase 1B headroom")
    check_storage(out)
    before = {"clean": receipt(clean), "upstream": receipt(upstream), "patch": receipt(patch), "keywords": keyword_receipt(kw_path)}
    # Unlike the large inputs, the small additive correction is fully rehashed.
    if sha(patch) != before["patch"]["sealed_database_sha256"]:
        raise RuntimeError("Outcome correction database checksum mismatch")
    with kw_path.open(encoding="utf-8-sig", newline="") as f:
        keywords = {}
        for r in csv.DictReader(f):
            if r["submission_id"] in keywords:
                raise RuntimeError("Duplicate keyword submission")
            keywords[r["submission_id"]] = r
    counts = collections.Counter()
    source_receipts = {}
    with contextlib.closing(readonly(clean)) as c, contextlib.closing(readonly(upstream)) as u, contextlib.closing(readonly(patch)) as p:
        with csv_writer(out / "submissions.csv.gz", SUBMISSION_FIELDS + EXTRA_FIELDS) as write_s, \
             csv_writer(out / "submission_authors.csv.gz", AUTHOR_FIELDS) as write_a, \
             csv_writer(out / "metadata_provenance.csv.gz", PROVENANCE_FIELDS) as write_p:
            query = "SELECT " + ",".join(SUBMISSION_FIELDS) + f" FROM submissions WHERE {where} AND year BETWEEN 2017 AND 2026 ORDER BY year,submission_id"
            for raw in c.execute(query):
                row = dict(raw)
                correction = p.execute("SELECT decision,decision_evidence,outcome_eligible FROM outcome_patch WHERE submission_id=?", (row["submission_id"],)).fetchone() if row["year"] == 2019 else None
                row = apply_patch(row, correction)
                row["normalized_keywords_json"], row["keyword_assignment_status"] = reconcile_keyword(row, keywords.pop(row["submission_id"], None))
                row["keyword_field_status"] = keyword_status(row["keywords"])
                source = u.execute("""SELECT o.source_id,o.source_type,o.nid,o.sid,o.location,o.captured,o.acquired,
                    o.capture_status,o.stage_status,o.cdate,o.mdate,o.content_hash,
                    json_extract(o.content_json,'$.authors') names,
                    json_extract(o.content_json,'$.authorids') ids
                    FROM observations o
                    WHERE o.oid=? AND o.kind='submission' AND o.source_type='official'""", (row["metadata_oid"],)).fetchone()
                if source:
                    source = dict(source)
                    source_id = source["source_id"]
                    if source_id not in source_receipts:
                        matches = u.execute("SELECT url,license,sha256 FROM sources WHERE source_id=? ORDER BY path", (source_id,)).fetchall()
                        if not matches or any(tuple(x) != tuple(matches[0]) for x in matches):
                            raise RuntimeError("Missing or conflicting source receipt")
                        source_receipts[source_id] = dict(matches[0])
                    source.update(source_receipts[source_id])
                names, ns = parse_field(source["names"] if source else None)
                ids, ix = parse_field(source["ids"] if source else None)
                authors, state, n, m = author_rows(row, names, ids)
                row.update(author_metadata_status="official_observation" if source else "missing_official_observation",
                           author_list_status=state, declared_name_count=n, declared_id_count=m)
                write_s(row)
                for a in authors:
                    write_a(a)
                    counts["author_positions"] += 1
                    counts["email_positions_withheld"] += a["email_withheld"]
                provenance = {k: None for k in PROVENANCE_FIELDS}
                provenance.update(submission_id=row["submission_id"], metadata_oid=row["metadata_oid"], author_field_shape=ns, authorid_field_shape=ix)
                if source:
                    fields = {"source_id":"source_id", "source_type":"source_type", "native_note_id":"nid", "snapshot_id":"sid", "source_record_location":"location", "captured":"captured", "acquired":"acquired", "capture_status":"capture_status", "stage_status":"stage_status", "creation_ms":"cdate", "modification_ms":"mdate", "content_hash":"content_hash", "source_url":"url", "source_license":"license", "source_file_sha256":"sha256"}
                    provenance.update({k: source[v] for k, v in fields.items()})
                write_p(provenance)
                counts["submissions"] += 1
                counts[f"year_{row['year']}"] += 1
                counts[f"status_{row['administrative_status']}"] += 1
                counts[f"author_lists_{state}"] += 1
                if counts["submissions"] % 5000 == 0:
                    check_storage(out)
                    print(canonical({"exported_submissions": counts["submissions"]}), flush=True)
    if keywords and split == "discovery":       # the frozen keyword export covers discovery only
        raise RuntimeError("Frozen keyword export contains out-of-scope submissions")
    after = {"clean": receipt(clean), "upstream": receipt(upstream), "patch": receipt(patch), "keywords": keyword_receipt(kw_path)}
    if before != after:
        raise RuntimeError("Source evidence changed during export")
    paths = sorted(out.glob("*.csv.gz"))
    files = [{"path": p.name, "bytes": p.stat().st_size, "sha256": sha(p)} for p in paths]
    write_json(out / "manifest.json", {
        "version": VERSION, "scope": scope,
        "sources": before, "files": files, "counts": dict(sorted(counts.items())),
        "source_preservation_checks_passed": True, "network_requests": 0,
        "storage": {"existing_phase1b_and_keyword_author_workspace_bytes":baseline,
                    "new_export_cap_bytes":MAX_NEW_BYTES, "free_space_minimum_bytes":FREE_RESERVE,
                    "cumulative_cap_bytes":CUMULATIVE_CAP},
        "experimental_inputs": [], "identity_policy": "Declared IDs are not verified people; email identifiers withheld, exact-ID hash retained.",
        "counting_policy": "One submission row; zero-based original author-list positions; no inferred name/ID alignment.",
    })
    check_storage(out)
    validate(out)


def validate(out):
    out = Path(out)
    manifest = read_json(out / "manifest.json")
    split = next((k for k, (_, scope) in SPLITS.items() if scope == manifest["scope"]), None)
    if split is None:
        raise RuntimeError("Unknown export scope")
    allowed = ("1", "0") if split == "discovery" else ("0", "1")
    for entry in manifest["files"]:
        p = out / entry["path"]
        if p.stat().st_size != entry["bytes"] or sha(p) != entry["sha256"]:
            raise RuntimeError("Export checksum mismatch: " + entry["path"])
    submissions = {}
    counts = collections.Counter()
    for r in rows(out / "submissions.csv.gz"):
        sid = r["submission_id"]
        if sid in submissions:
            raise RuntimeError("Duplicate submission")
        if (r["discovery_allowed"], r["confirmation_allowed"]) != allowed or not 2017 <= int(r["year"]) <= 2026:
            raise RuntimeError("Discovery isolation failure" if split == "discovery" else "Confirmation isolation failure")
        if r["outcome_eligible"] == "1" and r["decision"] not in ("accepted", "rejected"):
            raise RuntimeError("Eligible outcome is not binary")
        if r["normalized_keywords_json"] is not None:
            kw = json.loads(r["normalized_keywords_json"])
            if len(kw) != len(set(kw)):
                raise RuntimeError("Duplicate canonical keyword")
        submissions[sid] = r
        counts["submissions"] += 1
        counts[f"year_{r['year']}"] += 1
        counts[f"status_{r['administrative_status']}"] += 1
        counts[f"author_lists_{r['author_list_status']}"] += 1
    seen = set()
    author_counts = collections.Counter()
    for r in rows(out / "submission_authors.csv.gz"):
        s = submissions.get(r["submission_id"])
        if s is None or s["family_id"] != r["family_id"] or s["metadata_oid"] != r["metadata_oid"] or s["year"] != r["year"]:
            raise RuntimeError("Author join failure")
        pos = int(r["source_list_position"])
        key = (r["submission_id"], pos)
        if pos < 0 or key in seen:
            raise RuntimeError("Duplicate/invalid author position")
        seen.add(key)
        author_counts[r["submission_id"]] += 1
        if r["native_id"] is not None and "@" in r["native_id"]:
            raise RuntimeError("Email identifier leaked")
        if "@" in r["declared_name_json"]:
            raise RuntimeError("Email author name leaked")
        if r["native_id_kind"] == "email" and (r["native_id"] is not None or r["email_withheld"] != "1"):
            raise RuntimeError("Email suppression failure")
        if r["name_id_alignment"] == "aligned_lists" and s["author_list_status"] != "aligned_lists":
            raise RuntimeError("False name/ID alignment")
        counts["author_positions"] += 1
        counts["email_positions_withheld"] += int(r["email_withheld"])
    for sid, s in submissions.items():
        if author_counts[sid] != max(int(s["declared_name_count"]), int(s["declared_id_count"])):
            raise RuntimeError("Author positions lost")
    provenance = set()
    for r in rows(out / "metadata_provenance.csv.gz"):
        sid = r["submission_id"]
        if sid not in submissions or sid in provenance or r["metadata_oid"] != submissions[sid]["metadata_oid"]:
            raise RuntimeError("Provenance join failure")
        provenance.add(sid)
    if provenance != set(submissions) or dict(sorted(counts.items())) != manifest["counts"]:
        raise RuntimeError("Accounting mismatch")
    write_json(out / "validation.json", {"status":"passed", "version":VERSION,
        "checks": ["file_checksums", "discovery_isolation", "unique_submissions", "author_position_accounting",
                   "stable_family_year_joins", "email_suppression", "keyword_uniqueness", "provenance_coverage", "manifest_counts"],
        "counts": dict(sorted(counts.items())), "network_requests":0})
    print(canonical({"validation":"passed", "submissions":counts["submissions"], "author_positions":counts["author_positions"]}), flush=True)


def main():
    def offline(event, _args):
        if event in ("socket.connect", "socket.getaddrinfo", "socket.sendto", "subprocess.Popen", "os.system"):
            raise RuntimeError("Dataset export is offline")
    sys.addaudithook(offline)
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    b = sub.add_parser("build")
    for arg in ("clean", "upstream", "patch", "keywords", "output"):
        b.add_argument("--" + arg, required=True)
    b.add_argument("--split", choices=sorted(SPLITS), default="discovery")
    v = sub.add_parser("validate")
    v.add_argument("--output", required=True)
    args = parser.parse_args()
    build(args) if args.operation == "build" else validate(args.output)


if __name__ == "__main__":
    main()
