# -*- coding: utf-8 -*-
# Copyright (c) 2021, Komal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
import frappe



class Item(Document):
	def on_save(self):
		if self.item_name == "":
			self.item_name = self.item_code
		frappe.throw("Test")
