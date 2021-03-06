#!/usr/bin/env python
# -*- coding: utf-8  -*-

import email
import os.path

from xtx.storage.text_file_storage import TextFileStorage
from xtx.storage.html_storage import HtmlStorage

class EmlStorage(TextFileStorage):

	def __init__(self, filepath = None):
		super().__init__(filepath)

	def write(self, data, overwrite = True):
		raise NotImplementedError

	def read(self, limit = -1, encoding = "utf-8"):
		html = self.__get_html(encoding = encoding)
		hs = HtmlStorage(filepath = None, content = html)
		tables = hs.read(limit = limit, encoding = encoding)
		return tables

	def __get_html(self, encoding):
		html = None
		with open(self.filepath, encoding = encoding) as file:
			msg = email.message_from_file(file)
			for part in msg.walk():
				if not part.is_multipart():
					r = part.get_payload(decode=True)
					html = r.decode("UTF8")
			file.close()
		return html
