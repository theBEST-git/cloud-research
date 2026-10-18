"""Verify delivery without decoding any scientific data or outcome values."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda:stream.read(1024**2),b''):
            h.update(chunk)
    return h.hexdigest()
seal=json.loads((root/'release_seal.json').read_text(encoding='utf-8-sig'))
assert sha(root/'release_manifest.json')==seal['manifest_sha256']
manifest=json.loads((root/'release_manifest.json').read_text(encoding='utf-8-sig'))
for record in manifest['files']:
    path=root/record['path']
    assert path.resolve().is_relative_to(root.resolve())
    assert path.stat().st_size==record['bytes'] and sha(path)==record['sha256'],record['path']
print(json.dumps({'status':'passed','sealed_files':len(manifest['files']),'outcome_values_decoded':False,'external_database_required':False}))
