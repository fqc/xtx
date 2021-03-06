#!/usr/bin/env python
# -*- coding: utf-8  -*-

"""
execute the unittest file in project root directory.
"""
import sys
sys.path.append(r"../xtx/")

import unittest

from xtx.storage import *
from tests.testing import Testing

class FileStorageTest(Testing):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_instance(self):
		with self.assertRaises(TypeError):
			s = FileStorage() # can not instance

def suite():
	suite = unittest.TestSuite()
	suite.addTest(FileStorageTest("test_instance"))
	return suite

if __name__ == "__main__":
	unittest.main(defaultTest = "suite")