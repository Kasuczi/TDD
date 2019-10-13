"""
Test for hamming_metric
"""

import unittest

from src.DNA_RNA import hamming_metric, i_am_your_father

class testHamming(unittest.TestCase):

    def testHamming(self):
        testDna1 = 'GCTAC'
        testDna2 = 'CCTAT'
        hamming_metric(testDna1, testDna2)
        self.assertEqual(hamming_metric(testDna1, testDna2), 3)


    def testFather(self):
        fathers = ['ATCAG', 'GCTAT', 'GTCCG']
        child = ['GCTAT']
        self.assertEqual(i_am_your_father(fathers, child),0)