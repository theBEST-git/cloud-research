"""Export only the explicitly released population; deterministic, bounded, offline.

Selected observations retain their source/eligibility fields. Historical text is
not exported. Original split flags describe the source, not current permission.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, os, shutil, sys, time
from pathlib import Path
import corpus_access as access

HERE=Path(__file__).resolve().parent
DATA=HERE/'released_data'
SHARD_BYTES=32*1024**2
MAX_FILE_BYTES=48*1024**2
TABLES=('submissions','notes','scores','edges','score_changes','selection_ledger','issues')
KEYS={'submissions':'submission_id','notes':'oid','scores':'score_id','edges':'oid','score_changes':'pair_id','selection_ledger':'oid','issues':'issue_id'}


def line(row):
    return (json.dumps(dict(row),sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':'))+'\n').encode('utf-8')


def released_ids(c):
    return [r[0] for r in c.execute('SELECT submission_id FROM analysis_access WHERE released_from_confirmation=1 ORDER BY submission_id')]


def source_rows(c,table,ids):
    if table not in TABLES:raise ValueError('Table is not approved for publication')
    if table=='submissions':
        for sid in ids:
            yield from c.execute('SELECT * FROM analysis_submissions WHERE submission_id=? AND released_from_confirmation=1',(sid,))
    elif table in ('notes','scores'):
        for sid in ids:
            yield from c.execute('SELECT * FROM '+table+' WHERE submission_id=? AND is_primary=1 ORDER BY '+KEYS[table],(sid,))
    elif table=='edges':
        for sid in ids:
            yield from c.execute('SELECT e.* FROM edges e JOIN notes n USING(oid) WHERE e.submission_id=? AND n.is_primary=1 ORDER BY e.oid',(sid,))
    elif table=='selection_ledger':
        # Submission index restricts this join before per-paper ordering; no text selected.
        for sid in ids:
            yield from c.execute('SELECT l.* FROM notes n JOIN selection_ledger l USING(oid) WHERE n.submission_id=? ORDER BY l.oid',(sid,))
    else:
        yield from c.execute('SELECT x.* FROM '+table+' x JOIN analysis_access a USING(submission_id) WHERE a.released_from_confirmation=1 ORDER BY x.'+KEYS[table])


def write_shards(rows,dest,table,target=SHARD_BYTES,max_file=MAX_FILE_BYTES):
    """Keep one row in memory; target uncompressed bytes bounds each output file."""
    dest=Path(dest);dest.mkdir(parents=True,exist_ok=True)
    files=[];stream=hashlib.sha256();total=0;fields=None;writer=None;raw=None
    count=0;size=0;digest=None;temp=None;final=None
    def finish():
        nonlocal writer,raw
        if writer is None:return
        writer.close();raw.flush();os.fsync(raw.fileno());raw.close()
        if temp.stat().st_size>max_file:raise RuntimeError('Shard exceeds Git publication ceiling')
        os.replace(temp,final)
        files.append({'path':final.name,'rows':count,'bytes':final.stat().st_size,'sha256':access.sha(final),'uncompressed_bytes':size,'uncompressed_sha256':digest.hexdigest()})
        writer=None;raw=None
    try:
        for row in rows:
            row=dict(row)
            if fields is None:fields=sorted(row)
            elif sorted(row)!=fields:raise RuntimeError('Schema changed within export table')
            b=line(row)
            if len(b)>max_file-1024:raise RuntimeError('One record exceeds safe shard size')
            if writer is not None and size+len(b)>target:finish()
            if writer is None:
                final=dest/(table+'-'+str(len(files)+1).zfill(4)+'.jsonl.gz');temp=final.with_name(final.name+'.partial')
                raw=temp.open('wb');writer=gzip.GzipFile(fileobj=raw,mode='wb',filename='',mtime=0,compresslevel=6)
                count=0;size=0;digest=hashlib.sha256()
            writer.write(b);stream.update(b);digest.update(b);count+=1;size+=len(b);total+=1
        finish()
    finally:
        if writer is not None:writer.close()
        if raw is not None:raw.close()
    return {'table':table,'rows':total,'columns':fields or [],'stream_sha256':stream.hexdigest(),'files':files}


def check_shards(dest,table_info,expected_rows=None,allowed_ids=None):
    dest=Path(dest);stream=hashlib.sha256();total=0;seen=set();table=table_info['table']
    expected=iter(expected_rows) if expected_rows is not None else None
    for f in table_info['files']:
        p=dest/f['path']
        if p.stat().st_size!=f['bytes'] or access.sha(p)!=f['sha256']:raise RuntimeError('Compressed shard changed: '+p.name)
        h=hashlib.sha256();n=0;size=0
        with gzip.open(p,'rb') as data:
            for b in data:
                row=json.loads(b)
                if line(row)!=b:raise RuntimeError('Noncanonical JSONL record')
                if sorted(row)!=table_info['columns']:raise RuntimeError('Wrong columns')
                if allowed_ids is not None and row['submission_id'] not in allowed_ids:raise RuntimeError('Out-of-population record')
                key=row[KEYS[table]]
                if key in seen:raise RuntimeError('Duplicate primary key')
                seen.add(key)
                if expected is not None:
                    source=next(expected,None)
                    if source is None or line(source)!=b:raise RuntimeError('Export differs from current read-only source: '+table)
                h.update(b);stream.update(b);n+=1;size+=len(b);total+=1
        if (n,size,h.hexdigest())!=(f['rows'],f['uncompressed_bytes'],f['uncompressed_sha256']):raise RuntimeError('Shard row/hash mismatch')
    if expected is not None and next(expected,None) is not None:raise RuntimeError('Source contains omitted rows')
    if total!=table_info['rows'] or stream.hexdigest()!=table_info['stream_sha256']:raise RuntimeError('Table row/hash mismatch')
    return total


def export(root):
    if (HERE/'release_seal.json').exists():raise RuntimeError('Cannot change sealed release')
    DATA.mkdir(exist_ok=True)
    if shutil.disk_usage(DATA).free<50*1024**3:raise RuntimeError('Less than 50 GiB free')
    lock=HERE/'export.lock';fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY);os.close(fd)
    started=time.monotonic();c=None
    try:
        before=access.source_receipts(root);c=access.open_analysis_corpus(root,verify=False);ids=released_ids(c)
        if len(ids)!=access.policy()['expected_released_confirmation']:raise RuntimeError('Wrong released population')
        info=[]
        for table in TABLES:
            checkpoint=DATA/(table+'.json')
            if checkpoint.exists():
                saved=access.read(checkpoint);check_shards(DATA,saved);info.append(saved)
                print(json.dumps({'table':table,'rows':saved['rows'],'resumed':True}),flush=True);continue
            result=write_shards(source_rows(c,table,ids),DATA,table)
            access.write(checkpoint,result);info.append(result)
            print(json.dumps({'table':table,'rows':result['rows'],'compressed_bytes':sum(f['bytes'] for f in result['files'])}),flush=True)
        access.verify_sources(before)
        manifest={'version':'former-confirmation-export-20261018-v1','submissions':len(ids),'population':'Only analysis_access.released_from_confirmation=1','selected_observations_only':True,'original_flags_preserved':True,'manuscripts_included':False,'unselected_prose_histories_included':False,'source_receipts_sha256':access.sha(HERE/'source_receipts.json'),'tables':info,'compressed_bytes':sum(f['bytes'] for t in info for f in t['files']),'raw_jsonl_bytes':sum(f['uncompressed_bytes'] for t in info for f in t['files']),'max_shard_bytes':MAX_FILE_BYTES,'seconds_this_invocation':round(time.monotonic()-started,2),'independent_confirmation_available':False,'content_read_for_authorized_export':True}
        if manifest['compressed_bytes']>=2*1024**3:raise RuntimeError('Data exceeds one GitHub push limit; do not push')
        access.write(HERE/'export_manifest.json',manifest)
        print(json.dumps({'status':'exported','bytes':manifest['compressed_bytes'],'seconds':manifest['seconds_this_invocation']}),flush=True)
    finally:
        if c is not None:c.close()
        lock.unlink(missing_ok=True)


def validate(root):
    before=access.source_receipts(root);m=access.read(HERE/'export_manifest.json');c=access.open_analysis_corpus(root,verify=False)
    try:
        ids=released_ids(c);allowed=set(ids);counts={};expected_files=set()
        if len(ids)!=m['submissions'] or len(ids)!=access.policy()['expected_released_confirmation']:raise RuntimeError('Wrong population')
        for t in m['tables']:
            counts[t['table']]=check_shards(DATA,t,source_rows(c,t['table'],ids),allowed)
            expected_files.update(f['path'] for f in t['files'])
            print(json.dumps({'validated':t['table'],'rows':counts[t['table']]}),flush=True)
        if {p.name for p in DATA.glob('*.jsonl.gz')}!=expected_files:raise RuntimeError('Unexpected or missing data shards')
        # Verify source linkage without substituting or splicing observations.
        for table in ('scores','edges'):
            if table=='scores':extra=' AND x.is_primary=1'
            else:extra=' AND n.is_primary=1'
            q='SELECT COUNT(*) FROM analysis_access a CROSS JOIN '+table+' x ON x.submission_id=a.submission_id LEFT JOIN notes n ON n.oid=x.oid WHERE a.released_from_confirmation=1'+extra+' AND (n.oid IS NULL OR n.submission_id!=x.submission_id)'
            if c.execute(q).fetchone()[0]:raise RuntimeError('Broken selected observation linkage')
        access.verify_sources(before)
        result={'status':'passed','all_export_values_replayed_against_source':True,'population':len(ids),'tables':counts,'no_discovery_or_pending_records':True,'sources_preserved':True,'compressed_bytes':m['compressed_bytes'],'max_file_bytes':max(f['bytes'] for t in m['tables'] for f in t['files']),'fresh_full_source_database_hash':False}
        if not (HERE/'release_seal.json').exists():access.write(HERE/'export_validation.json',result)
        elif result!=access.read(HERE/'export_validation.json'):raise RuntimeError('Validation differs from sealed result')
        print(json.dumps(result,indent=2),flush=True)
    finally:c.close()


def main():
    p=argparse.ArgumentParser();p.add_argument('operation',choices=('export','validate'));p.add_argument('--corpus-root');a=p.parse_args();sys.addaudithook(access.offline)
    root=access.default_root(a.corpus_root)
    if a.operation=='export':export(root)
    else:validate(root)
if __name__=='__main__':main()
