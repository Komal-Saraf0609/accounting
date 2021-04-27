from __future__ import unicode_literals

import os
import unittest

import frappe

from .account import Account

def test_create_account():
	app_path = os.path.dirname(frappe.get_app_path('accounting'))
	json_file = os.path.join(os.getcwd(), app_path, "standard_coa.json")
	Account.load_tree_from_json(json_file)


class TestAccount(unittest.TestCase):
	pass

	