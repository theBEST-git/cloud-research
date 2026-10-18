"""Bounded-shard and source-replay tests; entirely synthetic."""
import copy,gzip,json,tempfile,unittest
from pathlib import Path
import corpus_access as access
import export_released as export

class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.dest=Path(self.temp.name)
        self.rows=[{'submission_id':'s'+str(i),'text':'Unicode α 中文\nsecond paragraph '+str(i),'value':i} for i in range(9)]
    def tearDown(self):self.temp.cleanup()
    def dump(self,rows=None,**kwargs):return export.write_shards(iter(self.rows if rows is None else rows),self.dest,'submissions',**kwargs)
    def test_unicode_and_whole_paragraphs_round_trip(self):
        info=self.dump();self.assertEqual(export.check_shards(self.dest,info,iter(self.rows),{r['submission_id'] for r in self.rows}),9)
    def test_gzip_and_jsonl_are_deterministic(self):
        a=self.dump(target=220);first=[(self.dest/f['path']).read_bytes() for f in a['files']]
        b=self.dump(target=220);self.assertEqual(a,b);self.assertEqual(first,[(self.dest/f['path']).read_bytes() for f in b['files']])
    def test_sharding_never_splits_an_observation(self):
        a=self.dump(target=220);self.assertGreater(len(a['files']),1)
        self.assertTrue(all(f['uncompressed_bytes']<=220 for f in a['files']))
        self.assertEqual(export.check_shards(self.dest,a,self.rows),9)
    def test_source_change_rejected(self):
        a=self.dump();changed=copy.deepcopy(self.rows);changed[0]['value']=99
        with self.assertRaisesRegex(RuntimeError,'differs'):export.check_shards(self.dest,a,changed)
    def test_source_omission_rejected(self):
        a=self.dump(self.rows[:-1])
        with self.assertRaisesRegex(RuntimeError,'omitted'):export.check_shards(self.dest,a,self.rows)
    def test_extra_export_row_rejected(self):
        a=self.dump()
        with self.assertRaisesRegex(RuntimeError,'differs'):export.check_shards(self.dest,a,self.rows[:-1])
    def test_no_discovery_or_pending_leak(self):
        a=self.dump()
        with self.assertRaisesRegex(RuntimeError,'Out-of-population'):export.check_shards(self.dest,a,allowed_ids={'s0'})
    def test_duplicate_primary_key_rejected(self):
        a=self.dump(self.rows+[self.rows[0]])
        with self.assertRaisesRegex(RuntimeError,'Duplicate'):export.check_shards(self.dest,a)
    def test_corrupt_cache_rejected(self):
        a=self.dump();p=self.dest/a['files'][0]['path'];p.write_bytes(b'damaged')
        with self.assertRaisesRegex(RuntimeError,'changed'):export.check_shards(self.dest,a)
    def test_missing_shard_rejected(self):
        a=self.dump();(self.dest/a['files'][0]['path']).unlink()
        with self.assertRaises(FileNotFoundError):export.check_shards(self.dest,a)
    def test_empty_table_is_explicit(self):
        a=self.dump([]);self.assertEqual(a['rows'],0);self.assertEqual(a['files'],[]);self.assertEqual(export.check_shards(self.dest,a,[]),0)
    def test_oversized_record_refused(self):
        with self.assertRaisesRegex(RuntimeError,'One record'):self.dump([{'submission_id':'s','text':'x'*3000}],max_file=2048)
    def test_no_silent_schema_drift(self):
        with self.assertRaisesRegex(RuntimeError,'Schema'):self.dump(self.rows+[{'submission_id':'different'}])
    def test_resume_checkpoint_reusable_without_source_calls(self):
        a=self.dump();access.write(self.dest/'checkpoint.json',a);cached=access.read(self.dest/'checkpoint.json')
        self.assertEqual(export.check_shards(self.dest,cached),9);self.assertEqual(a,cached)
    def test_unknown_table_rejected(self):
        with self.assertRaises(ValueError):list(export.source_rows(None,'credentials',[]))
    def test_shards_have_no_time_or_filename_metadata(self):
        a=self.dump();b=(self.dest/a['files'][0]['path']).read_bytes()
        self.assertEqual(b[4:8],b'\0'*4);self.assertEqual(b[3]&8,0)

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExportTests))
    access.write(Path(__file__).parent/'test_export_results.json',{'status':'passed' if result.wasSuccessful() else 'failed','tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors)})
    raise SystemExit(0 if result.wasSuccessful() else 1)
