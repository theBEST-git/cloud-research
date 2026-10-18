"""Run the unchanged exporter on frozen released IDs, preserving source flags.

Only runtime selection and its matching validation guard are adapted. Author
fields, identity hashing, suppression and CSV construction are untouched.
"""
import argparse,ast,csv,gzip,hashlib,json,re,sys
from pathlib import Path

EXPECTED_SCRIPT_SHA256='6cfb11fb7b9c537b6772330e95c0f89d5739b954789ecdab2771f3b0cb33898c'
EXPECTED_SUBMISSIONS=11113
ID_PATTERN=re.compile(rb'(?<!\\)"submission_id"\s*:\s*("(?:[^"\\]|\\.)*")')

def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1024**2),b''):h.update(block)
    return h.hexdigest()

def load_released(folder):
    folder=Path(folder).resolve()
    seal=json.loads((folder/'release_seal.json').read_text(encoding='utf-8-sig'))
    assert sha(folder/'release_manifest.json')==seal['manifest_sha256']
    entries={r['path']:r for r in json.loads((folder/'release_manifest.json').read_text(encoding='utf-8-sig'))['files']}
    paths=[folder/'access_ledger.csv']+sorted((folder/'released_data').glob('submissions-*.jsonl.gz'))
    for path in paths:
        r=entries[path.relative_to(folder).as_posix()]
        assert path.stat().st_size==r['bytes'] and sha(path)==r['sha256']
    released=set()
    for path in paths[1:]:
        with gzip.open(path,'rb') as stream:
            for line in stream:
                matches=ID_PATTERN.findall(line)
                assert len(matches)==1
                sid=json.loads(matches[0])  # Decode only the identifier, no outcome fields.
                assert isinstance(sid,str) and sid not in released
                released.add(sid)
    flags={}
    with paths[0].open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f):
            if r['released_from_confirmation']=='1':
                assert r['original_split']=='confirmation' and r['analysis_allowed']=='1'
                flags[r['submission_id']]=(r['original_discovery_allowed'],r['original_confirmation_allowed'])
    assert set(flags)==released and len(released)==EXPECTED_SUBMISSIONS
    assert set(flags.values())=={('0','0')}
    return flags

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('operation',choices=('build','validate'))
    p.add_argument('--script',default=str(Path(__file__).resolve().parents[1]/'scripts/export_dataset.py'))
    p.add_argument('--released-root')
    for name in ('clean','upstream','patch','keywords'):p.add_argument('--'+name)
    p.add_argument('--output',required=True)
    args=p.parse_args()
    script=Path(args.script).resolve()
    assert sha(script)==EXPECTED_SCRIPT_SHA256,'Original exporter changed; review before using this adapter'
    released_root=Path(args.released_root).resolve() if args.released_root else script.parent.parent/'data_confirmation'
    flags=load_released(released_root)
    original=script.read_text(encoding='utf-8-sig')
    old='if (r["discovery_allowed"], r["confirmation_allowed"]) != allowed or not 2017 <= int(r["year"]) <= 2026:'
    new='if sid not in RELEASED_FLAGS or r["split"] != "confirmation" or (r["discovery_allowed"], r["confirmation_allowed"]) != RELEASED_FLAGS[sid] or not 2017 <= int(r["year"]) <= 2026:'
    assert original.count(old)==1
    adapted=original.replace(old,new,1)
    def function_source(source,name):
        node=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name==name)
        return ast.get_source_segment(source,node)
    for name in ('author_rows','canonical','csv_writer','apply_patch','reconcile_keyword'):
        assert function_source(original,name)==function_source(adapted,name)
    ns={'__name__':'released_export_adapter','__file__':str(script),'RELEASED_FLAGS':flags}
    exec(compile(adapted,str(script),'exec'),ns)
    where="split='confirmation' AND submission_id IN ("+','.join("'"+sid.replace("'","''")+"'" for sid in sorted(flags))+')'
    ns['SPLITS']['confirmation']=(where,ns['SPLITS']['confirmation'][1])
    if args.operation=='build':
        for name in ('clean','upstream','patch','keywords'):
            if not getattr(args,name):p.error('--'+name+' is required for build')
        connection=ns['readonly'](args.clean)
        try:
            original_count=connection.execute('SELECT COUNT(*) FROM submissions WHERE confirmation_allowed=1 AND year BETWEEN 2017 AND 2026').fetchone()[0]
            actual={r['submission_id']:(str(r['discovery_allowed']),str(r['confirmation_allowed'])) for r in connection.execute('SELECT submission_id,discovery_allowed,confirmation_allowed FROM submissions WHERE '+where)}
            assert actual==flags
        finally:connection.close()
        argv=[str(script),'build','--split','confirmation']
        for name in ('clean','upstream','patch','keywords','output'):argv.extend(['--'+name,str(getattr(args,name))])
    else:argv=[str(script),'validate','--output',args.output]
    sys.argv=argv
    ns['main']()
    out=Path(args.output).resolve()
    ids=[r['submission_id'] for r in ns['rows'](out/'submissions.csv.gz')]
    assert len(ids)==EXPECTED_SUBMISSIONS and set(ids)==set(flags)
    if args.operation=='build':
        record={'original_exporter_sha256':EXPECTED_SCRIPT_SHA256,'original_cli_arguments':argv[1:],'released_population_source':str(released_root),'released_ids':len(flags),'original_confirmation_allowed_1_rows':original_count,'runtime_selection':'Exact frozen released IDs and source split=confirmation','runtime_validator_change':'Validate membership and unchanged per-ID original flags (0,0), rather than require confirmation_allowed=1','existing_files_modified':False,'database_flags_modified':False,'author_fields':list(ns['AUTHOR_FIELDS']),'author_identity_function_unchanged':True,'identity_rule':'native_ + sha256(canonical([declared-id-v1, raw_id])); no salt','email_suppression_unchanged':True,'environment_storage_guards_changed':False,'source_policy_independent_confirmation_available':False}
        ns['write_json'](out/'adapter_reproduction.json',record)
    print(json.dumps({'released_id_membership':'passed','submissions':len(ids),'outcome_analysis_performed':False}),flush=True)

if __name__=='__main__':main()
