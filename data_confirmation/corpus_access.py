"""Read-only access to discovery plus explicitly released former confirmation.

The original splits and all sealed databases remain unchanged. analysis_* views
express the new permission; original discovery_allowed is never rewritten.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, os, re, sqlite3, sys
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
CHANGED_OUTCOMES={'decision','decision_evidence','outcome_eligible'}
TABLES=('notes','scores','edges','score_changes','selection_ledger','issues','transformation_ledger')


def read(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
def write(path,value):
    path=Path(path);temp=path.with_name(path.name+'.partial')
    with temp.open('wb') as f:
        f.write((json.dumps(value,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode());f.flush();os.fsync(f.fileno())
    os.replace(temp,path)
def write_csv(path,rows):
    path=Path(path);temp=path.with_name(path.name+'.partial');rows=list(rows)
    fields=sorted({k for row in rows for k in row})
    with temp.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows);f.flush();os.fsync(f.fileno())
    os.replace(temp,path)
def offline(event,args):
    if event.startswith('socket.') and event!='socket.gethostname':raise RuntimeError('Access build is offline')


def default_root(value=None):
    if value:return Path(value).resolve()
    if os.environ.get('SCIRESEARCH_CORPUS_ROOT'):return Path(os.environ['SCIRESEARCH_CORPUS_ROOT']).resolve()
    for p in (HERE.parents[2],Path(sys.executable).resolve().parents[2]):
        if (p/'data/phase1b/eda_ready_20260913T143255Z/eda.sqlite').is_file():return p
    raise RuntimeError('Set SCIRESEARCH_CORPUS_ROOT or pass corpus_root to the local sealed corpus repository')


def policy():
    p=read(HERE/'policy.json')
    if p.get('release_former_confirmation') is not True or p.get('independent_confirmation_available') is not False:
        raise RuntimeError('Released exploratory policy is not active')
    return p


def is_allowed(split,discovery_allowed,reason,release_policy):
    if split=='discovery' and discovery_allowed==1:return True
    return (release_policy.get('release_former_confirmation') is True and split=='confirmation'
            and discovery_allowed==0 and reason in release_policy['allowed_confirmation_reasons'])


def source_receipts(root):
    clean=Path(root)/'data/phase1b/eda_ready_20260913T143255Z'
    repair=Path(root)/'data/phase1b/outcome_repair_20260923T104907Z'
    manifest=clean/'artifact_manifest.json';seal=read(clean/'release_seal.json')
    if sha(manifest)!=seal['manifest_sha256']:raise RuntimeError('Clean source manifest changed')
    repair_manifest=repair/'artifact_manifest.json'
    if not repair_manifest.exists():repair_manifest=repair/'manifest.json'
    repair_seal=read(repair/'release_seal.json')
    if sha(repair_manifest)!=repair_seal['manifest_sha256']:raise RuntimeError('2019 correction manifest changed')
    expected={r['path']:r for r in read(repair_manifest)['files']}
    for name in ('config.json','validation.json','outcomes.sqlite'):
        if sha(repair/name)!=expected[name]['sha256']:raise RuntimeError('2019 correction file changed: '+name)
    cfg=read(repair/'config.json')
    if sha(manifest)!=cfg['source_manifest_sha256']:raise RuntimeError('Correction refers to a different clean source')
    expected_db=next(r for r in read(manifest)['files'] if r['path']=='eda.sqlite')
    db=clean/'eda.sqlite';st=db.stat()
    if st.st_size!=expected_db['bytes'] or st.st_size!=cfg['source_bytes']:raise RuntimeError('Clean database size changed')
    if expected_db['sha256']!=cfg['source_sha256']:raise RuntimeError('Recorded clean database hashes disagree')
    old=Path(root)/'data/phase1b/eda_ready_20260913T143255Z/release_seal.json'
    files=[manifest,old,repair_manifest,repair/'release_seal.json',repair/'config.json',repair/'validation.json',repair/'outcomes.sqlite',clean/'splits.csv',clean.parent/'harmonized_20260910T125430Z/split_overlay.csv']
    records=[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
    for p in (db,repair/'outcomes.sqlite'):
        wal=Path(str(p)+'-wal')
        if wal.exists() and wal.stat().st_size:raise RuntimeError('Nonempty source WAL')
    return {'files':records,'database':{'path':str(db),'bytes':st.st_size,'mtime_ns':st.st_mtime_ns,'recorded_sha256':expected_db['sha256'],'fresh_full_database_hash':False},'scope':'Consumed seal/correction/split files freshly hashed; clean database seal/size/mtime/WAL verified, not a new full raw-corpus checksum audit.'}


def verify_sources(receipts):
    for r in receipts['files']:
        p=Path(r['path'])
        if p.stat().st_size!=r['bytes'] or sha(p)!=r['sha256']:raise RuntimeError('Protected source changed: '+str(p))
    r=receipts['database'];p=Path(r['path'])
    if p.stat().st_size!=r['bytes'] or p.stat().st_mtime_ns!=r['mtime_ns']:raise RuntimeError('Protected database stat changed')
    wal=Path(str(p)+'-wal')
    if wal.exists() and wal.stat().st_size:raise RuntimeError('Source WAL changed')


def install_views(c,release_policy):
    """Called before query_only, so only temporary in-memory definitions change."""
    reasons=release_policy['allowed_confirmation_reasons']
    if any(r not in ('inherited_confirmation','new_family_fixed_hash') for r in reasons):raise RuntimeError('Unrecognized release reason')
    quoted=','.join("'"+r+"'" for r in reasons)
    allowed="(s.split='discovery' AND s.discovery_allowed=1) OR (s.split='confirmation' AND s.discovery_allowed=0 AND s.split_issue IN ("+quoted+"))"
    c.execute('CREATE TEMP VIEW analysis_access AS SELECT s.submission_id,s.family_id,s.year,s.metadata_oid,s.split AS original_split,s.discovery_allowed AS original_discovery_allowed,s.confirmation_allowed AS original_confirmation_allowed,s.split_issue,CASE WHEN '+allowed+' THEN 1 ELSE 0 END AS analysis_allowed,CASE WHEN s.split=\'confirmation\' AND ('+allowed+') THEN 1 ELSE 0 END AS released_from_confirmation FROM submissions s')
    c.execute('CREATE TEMP VIEW analysis_submissions AS SELECT s.*,a.analysis_allowed,a.released_from_confirmation FROM submissions s JOIN analysis_access a USING(submission_id) WHERE a.analysis_allowed=1')
    c.execute('CREATE TEMP VIEW analysis_notes AS SELECT n.*,a.analysis_allowed,a.released_from_confirmation FROM notes n JOIN analysis_access a USING(submission_id) WHERE a.analysis_allowed=1')
    c.execute("CREATE TEMP VIEW analysis_reviews AS SELECT * FROM analysis_notes WHERE kind='review' AND is_primary=1 AND text_eligible=1")
    c.execute("CREATE TEMP VIEW analysis_messages AS SELECT * FROM analysis_notes WHERE kind='comment' AND is_primary=1 AND text_eligible=1")
    c.execute("CREATE TEMP VIEW analysis_metareviews AS SELECT * FROM analysis_notes WHERE kind='metareview' AND is_primary=1 AND text_eligible=1")
    c.execute("CREATE TEMP VIEW analysis_author_responses AS SELECT * FROM analysis_messages WHERE author_response_eligible=1 AND year!=2017")
    c.execute('CREATE TEMP VIEW analysis_scores AS SELECT s.*,a.analysis_allowed,a.released_from_confirmation FROM scores s JOIN analysis_access a USING(submission_id) WHERE a.analysis_allowed=1 AND s.is_primary=1 AND s.eligible=1')
    c.execute("CREATE TEMP VIEW analysis_ratings AS SELECT s.* FROM analysis_scores s JOIN notes n USING(oid) WHERE n.kind='review' AND n.rating_eligible=1 AND n.is_primary=1 AND (s.dimension='rating' OR (s.dimension='recommendation' AND NOT EXISTS(SELECT 1 FROM scores x WHERE x.oid=s.oid AND x.dimension='rating' AND x.eligible=1)))")
    c.execute('CREATE TEMP VIEW analysis_edges AS SELECT e.*,a.analysis_allowed,a.released_from_confirmation FROM edges e JOIN analysis_access a USING(submission_id) WHERE a.analysis_allowed=1')
    c.execute("CREATE TEMP VIEW analysis_conversation_edges AS SELECT e.* FROM analysis_edges e JOIN notes n USING(oid) WHERE n.is_primary=1 AND e.topology_eligible=1 AND e.parent_nid!=''")
    c.execute("CREATE TEMP VIEW analysis_timed_edges AS SELECT e.* FROM analysis_edges e JOIN notes n USING(oid) WHERE n.is_primary=1 AND e.timing_eligible=1 AND e.parent_nid!='' AND e.year!=2018")
    c.execute("CREATE TEMP VIEW analysis_score_changes AS SELECT p.*,a.analysis_allowed,a.released_from_confirmation FROM score_changes p JOIN analysis_access a USING(submission_id) WHERE a.analysis_allowed=1 AND p.pair_eligible=1 AND p.year IN (2024,2025) AND p.dimension='rating'")
    c.execute('CREATE TEMP VIEW analysis_similarity_reviews AS SELECT n.* FROM analysis_reviews n JOIN submissions s USING(submission_id) WHERE n.reviewer_ambiguous=0 AND s.similarity_eligible=1')
    c.execute("CREATE TEMP VIEW analysis_disagreement_reviews AS SELECT n.* FROM analysis_notes n JOIN submissions s USING(submission_id) WHERE n.kind='review' AND n.is_primary=1 AND n.rating_eligible=1 AND n.reviewer_ambiguous=0 AND s.disagreement_eligible=1")
    c.execute('CREATE TEMP VIEW analysis_outcome_submissions AS SELECT * FROM analysis_submissions WHERE outcome_eligible=1')
    c.execute("CREATE TEMP VIEW analysis_acceptance_submissions AS SELECT * FROM analysis_outcome_submissions WHERE administrative_status='ordinary_submission' AND decision IN ('accepted','rejected')")


def open_analysis_corpus(corpus_root=None,verify=True):
    root=default_root(corpus_root);p=policy()
    if verify and (HERE/'release_manifest.json').exists():verify_release()
    receipts=source_receipts(root)
    c=sqlite3.connect(':memory:',uri=True);c.row_factory=sqlite3.Row
    c.execute('PRAGMA cache_size=-32768');c.execute('PRAGMA temp_store=MEMORY')
    for name,path in (('base',Path(receipts['database']['path'])),('fix',root/'data/phase1b/outcome_repair_20260923T104907Z/outcomes.sqlite')):
        c.execute('ATTACH DATABASE ? AS '+name,(path.as_uri()+'?mode=ro&immutable=1',))
    cols=[r['name'] for r in c.execute('PRAGMA base.table_info(submissions)')]
    select=','.join('COALESCE(p."'+f+'",s."'+f+'") AS "'+f+'"' if f in CHANGED_OUTCOMES else 's."'+f+'"' for f in cols)
    c.execute('CREATE TEMP VIEW submissions AS SELECT '+select+' FROM base.submissions s LEFT JOIN fix.outcome_patch p USING(submission_id)')
    available={r[0] for r in c.execute("SELECT name FROM base.sqlite_master WHERE type='table'")}
    for name in TABLES:
        if name in available:c.execute('CREATE TEMP VIEW '+name+' AS SELECT * FROM base.'+name)
    install_views(c,p);c.execute('PRAGMA query_only=ON')
    if c.execute('PRAGMA query_only').fetchone()[0]!=1:raise RuntimeError('Read-only analysis connection unavailable')
    return c


def collect(c,release_policy):
    # Explicit metadata-only projection; this access-index check selects no prose or numeric outcomes.
    fields='submission_id,family_id,year,metadata_oid,original_split,original_discovery_allowed,original_confirmation_allowed,split_issue,analysis_allowed,released_from_confirmation'
    ledger=[dict(r) for r in c.execute('SELECT '+fields+' FROM analysis_access ORDER BY year,submission_id')]
    if len(ledger)!=len({r['submission_id'] for r in ledger}):raise RuntimeError('Duplicate reconciled identity')
    allowed=[r for r in ledger if r['analysis_allowed']]
    if len(allowed)!=len({r['family_id'] for r in allowed}):raise RuntimeError('Duplicate accessible family requires explicit review')
    original=sum(r['original_discovery_allowed']==1 for r in ledger);released=sum(r['released_from_confirmation'] for r in ledger);restricted=len(ledger)-len(allowed)
    if (original,released,len(allowed),restricted)!=(release_policy['expected_original_discovery'],release_policy['expected_released_confirmation'],release_policy['expected_exploratory_submissions'],release_policy['expected_restricted_submissions']):raise RuntimeError('Access population differs from frozen expectations')
    for r in ledger:
        assert bool(r['analysis_allowed'])==is_allowed(r['original_split'],r['original_discovery_allowed'],r['split_issue'],release_policy)
        if r['original_split']=='pending':assert r['analysis_allowed']==0
    counts=Counter((r['year'],r['original_split'],r['analysis_allowed'],r['released_from_confirmation']) for r in ledger)
    annual=[dict(year=y,original_split=s,analysis_allowed=a,released_from_confirmation=r,submissions=n) for (y,s,a,r),n in sorted(counts.items())]
    summary={'original_discovery':original,'released_former_confirmation':released,'exploratory_submissions':len(allowed),'restricted':restricted,'independent_confirmation_available':False,'released_records_read_for_substantive_analysis':False,'validation_scope':'This access-index check reads identity, year, split and access flags only. A separate authorized publication export reads research content and retires the holdout.'}
    return ledger,annual,summary


def verify_release():
    m=HERE/'release_manifest.json';seal=read(HERE/'release_seal.json')
    if sha(m)!=seal['manifest_sha256']:raise RuntimeError('Access manifest changed')
    for r in read(m)['files']:
        if sha(HERE/r['path'])!=r['sha256']:raise RuntimeError('Access artifact changed: '+r['path'])


def build(root):
    if (HERE/'release_seal.json').exists():raise RuntimeError('Access release is already sealed; validate instead')
    before=source_receipts(root)
    c=open_analysis_corpus(root,verify=False)
    try:ledger,annual,summary=collect(c,policy())
    finally:c.close()
    write_csv(HERE/'access_ledger.csv',ledger);write_csv(HERE/'coverage_by_year.csv',annual)
    write(HERE/'summary.json',summary);write(HERE/'source_receipts.json',before)
    verify_sources(before)
    write(HERE/'validation.json',{'status':'passed','metadata_membership_replayed':len(ledger),'active_count':len(ledger)-summary['restricted'],'source_files_preserved':True,'original_split_labels_unchanged':True,'new_untouched_holdout_claim':False,'access_index_check_read_substantive_content':False,'scope':'Access index only; authorized research-content export has its own validation record'})
    print(json.dumps(summary,indent=2))


def validate(root):
    verify_release();receipts=read(HERE/'source_receipts.json');verify_sources(receipts)
    c=open_analysis_corpus(root)
    try:ledger,annual,summary=collect(c,policy())
    finally:c.close()
    with (HERE/'access_ledger.csv').open(newline='',encoding='utf-8') as f:cached=list(csv.DictReader(f))
    assert len(cached)==len(ledger)
    for a,b in zip(cached,ledger):assert all(a[k]==str(v) for k,v in b.items())
    assert summary==read(HERE/'summary.json')
    verify_sources(receipts);print(json.dumps({'status':'passed','accessible':summary['exploratory_submissions'],'released':summary['released_former_confirmation'],'restricted':summary['restricted'],'sources_preserved':True},indent=2))


def seal():
    paths=[p for p in HERE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name not in ('release_manifest.json','release_seal.json') and not p.name.endswith(('.partial','.lock'))]
    files=[{'path':p.relative_to(HERE).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(paths)]
    write(HERE/'release_manifest.json',{'files':files});write(HERE/'release_seal.json',{'manifest_sha256':sha(HERE/'release_manifest.json'),'files':len(files),'bytes':sum(r['bytes'] for r in files),'status':'released_for_exploratory_use'})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('operation',choices=('build','validate','seal'));parser.add_argument('--corpus-root');args=parser.parse_args();sys.addaudithook(offline)
    root=default_root(args.corpus_root)
    if args.operation=='build':build(root)
    elif args.operation=='validate':validate(root)
    else:seal()
if __name__=='__main__':main()