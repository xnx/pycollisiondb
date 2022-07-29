"""
Unit tests for the search keywords of PyCollisionDB
"""

import unittest
from pycollisiondb.pycollisiondb import PyCollision, PyCollisionDBKeywordError


class PyCollisionDBTest(unittest.TestCase):
    def test_query_keyword_validation(self):
        pycoll = PyCollision()
        pycoll.query(pks=[89433])
        self.assertRaises(PyCollisionDBKeywordError, pycoll.query, notakey=1)
        self.assertRaises(PyCollisionDBKeywordError, pycoll.query, pk=1, pks=[3, 4])