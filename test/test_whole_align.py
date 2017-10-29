# -*- coding: utf-8 -*-
import os.path
import unittest
import sys
from pprint import  pprint
import operator
sys.path.append(os.path.abspath('..'))

from align import align, align_html
from hunalign import align_with_lang


class TestHunalign(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        pass

    def testUnalignedText(self):
        left = open(r'c:\project\books\1korean\murakami\03ko.txt', encoding='utf8').read()
        right = open(r'c:\project\books\1korean\murakami\03ru.txt', encoding='utf8').read()
        result = align(left, right)
        result = list(result)
        pprint(result)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHunalign)
    unittest.TextTestRunner(verbosity=2).run(suite)
