#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os
import os.path
from abc import ABCMeta,abstractmethod

from xtx.storage.file_storage import FileStorage
from xtx.storage.exceptions import *

class BinFileStorage(FileStorage, metaclass = ABCMeta):
	"""
	binary file
	"""

	def __init__(self, filepath = None):
		super().__init__(filepath)
		self.filepath = self.location

	@abstractmethod
	def create(self, force = False):
		pass

	@abstractmethod
	def clear(self, force = False):
		pass

	@abstractmethod
	def write(self, data, overwrite = False):
		pass

	@abstractmethod
	def read(self, limit = -1):
		pass
