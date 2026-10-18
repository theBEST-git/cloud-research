"""Verify the published package without the external source database."""
import json,sys
from pathlib import Path
import corpus_access as access
import export_released as export

def main():
    sys.addaudithook(access.offline);access.verify_release()
    manifest=access.read(Path(__file__).parent/'export_manifest.json')
    submissions=next(t for t in manifest['tables'] if t['table']=='submissions')
    import gzip
    ids=set()
    for f in submissions['files']:
        with gzip.open(export.DATA/f['path'],'rt',encoding='utf-8') as stream:
            for text in stream:
                row=json.loads(text)
                if row['split']!='confirmation' or row['released_from_confirmation']!=1 or row['analysis_allowed']!=1:raise RuntimeError('Wrong publication population')
                ids.add(row['submission_id'])
    if len(ids)!=manifest['submissions']:raise RuntimeError('Wrong submission count')
    counts={t['table']:export.check_shards(export.DATA,t,allowed_ids=ids) for t in manifest['tables']}
    print(json.dumps({'status':'passed','submissions':len(ids),'tables':counts,'scope':'Published checksums, canonical rows, membership and unique keys; no external database required.'},indent=2))
if __name__=='__main__':main()
