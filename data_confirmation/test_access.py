"""Synthetic permission, eligibility, split preservation and read-only tests."""
import copy, json, sqlite3, tempfile, unittest
from pathlib import Path
import corpus_access as access

POLICY={'release_former_confirmation':True,'allowed_confirmation_reasons':['inherited_confirmation','new_family_fixed_hash']}

def fixture():
    c=sqlite3.connect(':memory:');c.row_factory=sqlite3.Row
    c.executescript('''
    CREATE TABLE submissions(submission_id TEXT PRIMARY KEY,family_id TEXT,year INTEGER,metadata_oid TEXT,split TEXT,discovery_allowed INTEGER,confirmation_allowed INTEGER,split_issue TEXT,outcome_eligible INTEGER,decision TEXT,administrative_status TEXT,similarity_eligible INTEGER,disagreement_eligible INTEGER);
    CREATE TABLE notes(oid TEXT PRIMARY KEY,submission_id TEXT,kind TEXT,is_primary INTEGER,text_eligible INTEGER,author_response_eligible INTEGER,year INTEGER,rating_eligible INTEGER,reviewer_ambiguous INTEGER);
    CREATE TABLE scores(score_id TEXT PRIMARY KEY,submission_id TEXT,oid TEXT,is_primary INTEGER,eligible INTEGER,dimension TEXT,value REAL,year INTEGER);
    CREATE TABLE edges(oid TEXT,submission_id TEXT,year INTEGER,topology_eligible INTEGER,timing_eligible INTEGER,parent_nid TEXT);
    CREATE TABLE score_changes(pair_id TEXT,submission_id TEXT,year INTEGER,pair_eligible INTEGER,dimension TEXT);
    ''')
    for sid,split,disc,reason in [('d','discovery',1,'inherited_discovery'),('c','confirmation',0,'inherited_confirmation'),('p','pending',0,'unresolved_link_excluded_both'),('x','confirmation',0,'alias_split_conflict')]:
        c.execute('INSERT INTO submissions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',(sid,sid,2025,'m'+sid,split,disc,0,reason,1,'accepted','ordinary_submission',1,1))
        c.execute('INSERT INTO notes VALUES(?,?,?,?,?,?,?,?,?)',('n'+sid,sid,'review',1,1,0,2025,1,0))
        c.execute('INSERT INTO scores VALUES(?,?,?,?,?,?,?,?)',('s'+sid,sid,'n'+sid,1,1,'rating',5.,2025))
    access.install_views(c,POLICY)
    return c

class AccessTests(unittest.TestCase):
    def setUp(self):self.c=fixture()
    def tearDown(self):self.c.close()
    def ids(self,name):return {r['submission_id'] for r in self.c.execute('SELECT * FROM '+name)}
    def test_original_discovery_preserved(self):self.assertTrue(access.is_allowed('discovery',1,'inherited_discovery',POLICY))
    def test_authorized_confirmation_released(self):self.assertTrue(access.is_allowed('confirmation',0,'inherited_confirmation',POLICY))
    def test_unknown_reason_not_released(self):self.assertFalse(access.is_allowed('confirmation',0,'unknown_problem',POLICY))
    def test_pending_not_released(self):self.assertFalse(access.is_allowed('pending',0,'unresolved_link_excluded_both',POLICY))
    def test_conflicting_alias_not_released(self):self.assertFalse(access.is_allowed('confirmation',0,'alias_split_conflict',POLICY))
    def test_no_unilateral_release(self):
        p=copy.deepcopy(POLICY);p['release_former_confirmation']=False
        self.assertFalse(access.is_allowed('confirmation',0,'inherited_confirmation',p))
    def test_two_accessible_populations(self):self.assertEqual(self.ids('analysis_submissions'),{'d','c'})
    def test_original_flags_not_rewritten(self):
        r=self.c.execute("SELECT * FROM analysis_submissions WHERE submission_id='c'").fetchone()
        self.assertEqual((r['split'],r['discovery_allowed'],r['confirmation_allowed'],r['analysis_allowed'],r['released_from_confirmation']),('confirmation',0,0,1,1))
    def test_original_table_not_changed(self):self.assertEqual(self.c.execute('SELECT SUM(discovery_allowed),SUM(confirmation_allowed) FROM submissions').fetchone()[:],(1,0))
    def test_restricted_notes_and_scores_not_leaked(self):
        self.assertEqual(self.ids('analysis_reviews'),{'d','c'});self.assertEqual(self.ids('analysis_ratings'),{'d','c'})
    def test_invalid_score_still_excluded(self):
        self.c.execute("UPDATE scores SET eligible=0 WHERE submission_id='c'");self.assertEqual(self.ids('analysis_ratings'),{'d'})
    def test_superseded_review_still_excluded(self):
        self.c.execute("UPDATE notes SET is_primary=0 WHERE submission_id='c'");self.assertEqual(self.ids('analysis_reviews'),{'d'})
    def test_unusable_text_still_excluded(self):
        self.c.execute("UPDATE notes SET text_eligible=0 WHERE submission_id='c'");self.assertEqual(self.ids('analysis_reviews'),{'d'})
    def test_recommendation_fallback_not_spliced(self):
        self.c.execute("UPDATE scores SET eligible=0 WHERE submission_id='c'")
        self.c.execute("INSERT INTO scores VALUES('rec','c','nc',1,1,'recommendation',4,2025)")
        self.assertEqual([r['dimension'] for r in self.c.execute("SELECT * FROM analysis_ratings WHERE submission_id='c'")],['recommendation'])
        self.c.execute("UPDATE scores SET eligible=1 WHERE score_id='sc'")
        self.assertEqual([r['dimension'] for r in self.c.execute("SELECT * FROM analysis_ratings WHERE submission_id='c'")],['rating'])
    def test_ambiguous_reviewer_remains_pair_restricted(self):
        self.c.execute("UPDATE notes SET reviewer_ambiguous=1 WHERE submission_id='c'")
        self.assertNotIn('c',self.ids('analysis_similarity_reviews'));self.assertNotIn('c',self.ids('analysis_disagreement_reviews'))
        self.assertIn('c',self.ids('analysis_reviews'))
    def test_withdrawal_not_rejection(self):
        self.c.execute("UPDATE submissions SET administrative_status='withdrawn' WHERE submission_id='c'")
        self.assertEqual(self.ids('analysis_acceptance_submissions'),{'d'})
    def test_unknown_outcome_not_accepted(self):
        self.c.execute("UPDATE submissions SET outcome_eligible=0,decision='unknown' WHERE submission_id='c'")
        self.assertEqual(self.ids('analysis_acceptance_submissions'),{'d'})
    def test_author_specific_2017_restriction(self):
        self.c.execute("UPDATE notes SET kind='comment',author_response_eligible=1,year=2017 WHERE submission_id='c'")
        self.assertEqual(self.ids('analysis_author_responses'),set())
    def test_author_response_view_only_uses_discussion_messages(self):
        self.c.execute("UPDATE notes SET author_response_eligible=1 WHERE submission_id='c'")
        self.assertEqual(self.ids('analysis_author_responses'),set())
        self.c.execute("UPDATE notes SET kind='comment' WHERE submission_id='c'")
        self.assertEqual(self.ids('analysis_author_responses'),{'c'})
    def test_archived_graph_observations_are_not_conversation_primaries(self):
        self.c.execute("INSERT INTO edges VALUES('nc','c',2025,1,1,'parent')")
        self.c.execute("UPDATE notes SET is_primary=0 WHERE submission_id='c'")
        self.assertEqual(self.ids('analysis_conversation_edges'),set())
        self.assertEqual(self.ids('analysis_timed_edges'),set())
    def test_2018_timing_restriction(self):
        self.c.executemany('INSERT INTO edges VALUES(?,?,?,?,?,?)',[('nc','c',2018,1,1,'parent'),('nd','d',2025,1,1,'parent')])
        self.assertEqual(self.ids('analysis_conversation_edges'),{'d','c'});self.assertEqual(self.ids('analysis_timed_edges'),{'d'})
    def test_reconstructed_pairs_restrictions(self):
        self.c.executemany('INSERT INTO score_changes VALUES(?,?,?,?,?)',[('a','c',2025,1,'rating'),('b','c',2025,0,'rating'),('z','p',2025,1,'rating'),('y','c',2026,1,'rating')])
        self.assertEqual([r['pair_id'] for r in self.c.execute('SELECT * FROM analysis_score_changes')],['a'])
    def test_readonly_connection_guard(self):
        self.c.execute('PRAGMA query_only=ON')
        with self.assertRaises(sqlite3.OperationalError):self.c.execute("UPDATE submissions SET split='discovery'")
    def test_network_guard(self):
        with self.assertRaises(RuntimeError):access.offline('socket.connect',())

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(AccessTests))
    access.write(Path(__file__).parent/'test_access_results.json',{'status':'passed' if result.wasSuccessful() else 'failed','tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors)})
    raise SystemExit(0 if result.wasSuccessful() else 1)