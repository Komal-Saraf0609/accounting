from __future__ import unicode_literals

from typing import Dict, List

import frappe
import unittest

class TestSalesInvoice(unittest.TestCase):

    def test_gl_entries_are_balanced(self):
        credit_sum = frappe.db.sql("SELECT SUM(credit) FROM `tabGL Entry`")[0]
        debit_sum = frappe.db.sql("SELECT SUM(debit) FROM `tabGL Entry`")[0]
        self.assertEqual(credit_sum, debit_sum)