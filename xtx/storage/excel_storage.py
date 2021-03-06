#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path

from xtx.storage.bin_file_storage import BinFileStorage
from xtx.storage.excel_2003_storage import Excel2003Storage
from xtx.storage.excel_2007_storage import Excel2007Storage
from xtx.storage.exceptions import (StorageExistsError
	, StorageNotFoundError
	, UnmatchExtensionError
	, ArgumentsAbsenceError)


class ExcelStorage(BinFileStorage):

	def __init__(self, filepath = None, sheetIndex = -1, sheetName = None):
		super().__init__(filepath)

		ext = self.filepath.split(".")[-1]
		if ext == "xls":
			self.excelStorage = Excel2003Storage(filepath = filepath, sheetIndex = sheetIndex, sheetName = sheetName)
		elif ext == "xlsx":
			self.excelStorage = Excel2007Storage(filepath = filepath, sheetIndex = sheetIndex, sheetName = sheetName)
		else:
			raise UnmatchExtensionError(self.filepath)


	def create(self, force = False):
		return self.excelStorage.create(force = force)


	def clear(self, force = False):
		return self.excelStorage.clear(force = force)

		
	def write(self, data, overwrite = False):
		return self.excelStorage.write(data = data, overwrite = overwrite)


	def read(self, limit = -1):
		return self.excelStorage.read(limit = limit)
	
