"""ID/count/key-only checks for the released CSV export; no outcome analysis."""
import argparse,ast,collections,csv,gzip,hashlib,json,re
from pathlib import Path

NULL='\\N'
ID_PATTERN=re.compile(rb'(?<!\\)"submission_id"\s*:\s*("(?:[^"\\]|\\.)*")')

def project(path,columns):
    with gzip.open(path,'rt',encoding='utf-8',newline='') as f:
        reader=csv.reader(f);header=next(reader);indices=[header.index(c) for c in columns]
        for row in reader:
            yield tuple(None if row[i]==NULL else row[i] for i in indices)

def header(path):
    with gzip.open(path,'rt',encoding='utf-8',newline='') as f:return next(csv.reader(f))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository',default=str(Path(__file__).resolve().parents[1]))
    args=parser.parse_args();repo=Path(args.repository).resolve();out=repo/'data_confirmation_csv';released_root=repo/'data_confirmation'
    tree=ast.parse((repo/'scripts/export_dataset.py').read_text(encoding='utf-8-sig'))
    constants={n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in ('SUBMISSION_FIELDS','EXTRA_FIELDS','AUTHOR_FIELDS','PROVENANCE_FIELDS')}
    assert header(out/'submissions.csv.gz')==list(constants['SUBMISSION_FIELDS']+constants['EXTRA_FIELDS'])==header(repo/'data/submissions.csv.gz')
    assert header(out/'submission_authors.csv.gz')==list(constants['AUTHOR_FIELDS'])==header(repo/'data/submission_authors.csv.gz')
    assert header(out/'metadata_provenance.csv.gz')==list(constants['PROVENANCE_FIELDS'])
    released=set()
    for p in sorted((released_root/'released_data').glob('submissions-*.jsonl.gz')):
        with gzip.open(p,'rb') as f:
            for line in f:
                matches=ID_PATTERN.findall(line);assert len(matches)==1
                sid=json.loads(matches[0]);assert sid not in released;released.add(sid)
    submissions={};year_papers=collections.Counter()
    for sid,year in project(out/'submissions.csv.gz',('submission_id','year')):
        assert sid not in submissions;submissions[sid]=int(year);year_papers[int(year)]+=1
    assert len(submissions)==11113 and set(submissions)==released
    discovery={sid for sid, in project(repo/'data/submissions.csv.gz',('submission_id',))}
    overlap=set(submissions)&discovery
    assert len(discovery)==43516 and not overlap
    authors=collections.Counter();with_key=collections.defaultdict(set);keys=set();seen_positions=set();recomputed=0;mismatched=0
    for sid,year,key,native_id,pos in project(out/'submission_authors.csv.gz',('submission_id','year','declared_id_key','native_id','source_list_position')):
        year=int(year);assert sid in submissions and submissions[sid]==year
        assert (sid,pos) not in seen_positions;seen_positions.add((sid,pos));authors[year]+=1
        if key is not None:
            assert re.fullmatch(r'native_[0-9a-f]{64}',key)
            keys.add(key);with_key[year].add(sid)
        if native_id is not None:
            assert '@' not in native_id
            expected='native_'+hashlib.sha256(json.dumps(['declared-id-v1',native_id],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            recomputed+=1;mismatched+=int(expected!=key)
    assert mismatched==0
    old_keys={key for key, in project(repo/'data/submission_authors.csv.gz',('declared_id_key',)) if key is not None}
    shared=keys&old_keys
    if len(shared)<1000:raise RuntimeError('STOP: shared author-key count is not in the thousands: '+str(len(shared)))
    years=[{'year':year,'submissions':year_papers[year],'author_rows':authors[year],'papers_with_declared_id_key':len(with_key[year]),'share_with_declared_id_key':len(with_key[year])/year_papers[year]} for year in sorted(year_papers)]
    count=sum(authors.values())
    assert count==json.loads((out/'manifest.json').read_text())['counts']['author_positions']
    paper_key_count=sum(len(s) for s in with_key.values())
    result={'status':'passed','a':{'submission_rows':len(submissions),'released_ids':len(released),'exact_released_id_set_match':True},'b':{'discovery_rows':len(discovery),'submission_id_overlap':len(overlap)},'c':{'author_rows':count,'papers_with_declared_id_key':paper_key_count,'share_with_declared_id_key':paper_key_count/len(submissions),'by_year':years},'d':{'new_distinct_declared_id_keys':len(keys),'discovery_distinct_declared_id_keys':len(old_keys),'distinct_keys_shared_with_discovery':len(shared),'public_native_id_keys_recomputed':recomputed,'key_recomputation_mismatches':mismatched,'salt_added':False},'schema_checks':'all three headers match the original schema; submission/author headers also match discovery data directly','checks_use_only_ids_counts_keys':True,'outcome_analysis_performed':False,'e':{'limit_bytes':50000000,'all_files_under_50_MB':True,'files':[]}}
    (out/'id_key_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    with (out/'author_coverage_by_year.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(years[0]));writer.writeheader();writer.writerows(years)
    files=[{'path':p.relative_to(out).as_posix(),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file()]
    assert all(f['bytes']<50000000 for f in files)
    result['e']['files']=[f for f in files if f['path']!='id_key_checks.json']
    result['e']['largest_file_bytes']=max(f['bytes'] for f in files)
    (out/'id_key_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    assert (out/'id_key_checks.json').stat().st_size<50000000
    print(json.dumps({k:v for k,v in result.items() if k!='e'},indent=2))
    print(json.dumps({'e':{'all_files_under_50_MB':True,'largest_file_bytes':result['e']['largest_file_bytes'],'file_count':len(files)}},indent=2))

if __name__=='__main__':main()
