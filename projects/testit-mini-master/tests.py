"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])

    def test_max_run_bug_finder(self):
        #black box tests
        self.assertEqual(max_run([2,2,2,3,3,3,3]), [3,3,3,3]) # bug found here only does first set
        self.assertEqual(max_run([2,2,3,3,3]), [3,3,3])
        self.assertEqual(max_run([1,2,3,4,5]), [1,2,3,4,5]) # bug if all the same doesn't work
        self.assertEqual(max_run([2,2,3,3]), [2,2,3,3])

        #glass box tests
        #None bugs found through black box
        
if __name__ == "__main__":
    unittest.main()

