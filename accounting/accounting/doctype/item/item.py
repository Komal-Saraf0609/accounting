# -*- coding: utf-8 -*-
# Copyright (c) 2021, Komal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.website.website_generator import WebsiteGenerator
import frappe



class Item(WebsiteGenerator):
	def on_save(self):
		if self.item_name == "":
			self.item_name = self.item_code
		frappe.throw("Test")
