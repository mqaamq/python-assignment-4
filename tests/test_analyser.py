# Test results:
# test_analyse_twice (tests.test_analyser.TestAnalyser.test_analyse_twice) ... ok
# test_result_has_required_keys (tests.test_analyser.TestAnalyser.test_result_has_required_keys) ... ok
# test_result_is_not_empty (tests.test_analyser.TestAnalyser.test_result_is_not_empty) ... ok
# test_total_students (tests.test_analyser.TestAnalyser.test_total_students) ... ok
#
# Ran 4 tests in 0.002s
#
# OK
import unittest
from analytics.analyser import GpaAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [
            {"GPA": "3.8", "country": "USA"},
            {"GPA": "2.5", "country": "India"},
            {"GPA": "3.9", "country": "USA"},
            {"GPA": "1.8", "country": "Canada"},
            {"GPA": "3.5", "country": "India"}
        ]

    def test_result_is_not_empty(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5) 

    def test_result_has_required_keys(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("average_gpa", analyser.result)
        self.assertIn("max_gpa", analyser.result)
        self.assertIn("min_gpa", analyser.result)
        self.assertIn("high_performers", analyser.result)

    def test_analyse_twice(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        first_result = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, first_result) 

if __name__ == '__main__':
    unittest.main()