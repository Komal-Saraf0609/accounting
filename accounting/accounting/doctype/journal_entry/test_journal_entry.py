# -*- coding: utf-8 -*-
# Copyright (c) 2021, Komal and Contributors
# See license.txt
from __future__ import unicode_literals

from datetime import date
from typing import List

import frappe
from frappe.model.document import Document

from ..account.test_account import test_create_account
import unittest


def get_test_journal_entry_account(credit: int = 0, debit: int = 0):
	test_create_account()
	return frappe.get_doc({
		"doctype": "Journal Entry Account",
		"account": "Debtors",
		"debit": debit,
		"credit": credit
	})


def get_test_journal_entry(accounts: List):
	return frappe.get_doc({
		"doctype": "Journal Entry",
		"accounts": accounts,
		"posting_date": date.today()
	})

def setUp(self):
	pass

def tearDown(self):
	frappe.db.rollback()



class TestJournalEntry(unittest.TestCase):

	def _test_gl_entries_are_balanced(self):
		"""Test if sum(credits) = sum(debits)."""
		credit_sum = frappe.db.sql("SELECT SUM(credit) FROM `tabGL Entry`")[0]
		debit_sum = frappe.db.sql("SELECT SUM(debit) FROM `tabGL Entry`")[0]
		self.assertEqual(credit_sum, debit_sum)

	def test_journal_submission_creates_balanced_gl_entries(self):
		"""Ensure submitting JournalEntry creates balanced GL entries."""
		accounts = [
			get_test_journal_entry_account(100, 0).as_dict(),
			get_test_journal_entry_account(0, 100).as_dict()
		]
		journal_entry = get_test_journal_entry(accounts)
		before = frappe.db.count("GL Entry")

		journal_entry.submit()

		after = frappe.db.count("GL Entry")
		gl_count_increase = after - before
		self.assertEqual(gl_count_increase, 2, msg=frappe.get_all("GL Entry"))
		self._test_gl_entries_are_balanced()

	def test_exception_is_thrown_if_accounting_entries_arent_balanced(self):
		"""
		Ensure submitting JournalEntry with unbalanced accounting entries throws err.
		"""
		accounts = [
			get_test_journal_entry_account(100, 0).as_dict(),
		]
		journal_entry = get_test_journal_entry(accounts)
		self.assertRaises(
			frappe.exceptions.ValidationError, journal_entry.submit
		)
		accounts = [
			get_test_journal_entry_account(100, 0).as_dict(),
			get_test_journal_entry_account(0, 100).as_dict(),
			get_test_journal_entry_account(0, 100).as_dict(),
		]
		journal_entry = get_test_journal_entry(accounts)
		self.assertRaises(
			frappe.exceptions.ValidationError, journal_entry.submit
		)
