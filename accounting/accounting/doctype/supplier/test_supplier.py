# -*- coding: utf-8 -*-
# Copyright (c) 2021, Komal and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest


from ..account.test_account import test_create_account


def create_test_supplier(supplier_name: str = frappe.mock("name")):
	test_create_account()
	return frappe.get_doc({
		"doctype": "Supplier",
		"supplier_name": supplier_name,
	}).insert(ignore_if_duplicate=True)




class TestSupplier(unittest.TestCase):

	def test_supplier_test(self):
		create_test_supplier()

