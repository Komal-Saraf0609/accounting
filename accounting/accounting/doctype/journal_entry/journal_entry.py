# -*- coding: utf-8 -*-
# Copyright (c) 2021, Komal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
import frappe
from frappe import _
from datetime import date

class JournalEntry(Document):

	def _check_for_balanced_entries(self):
		debit_sum = 0
		credit_sum = 0
		for entry in self.accounts:
			debit_sum += entry.debit
			credit_sum += entry.credit
			self.total_credit = credit_sum
			self.total_debit = debit_sum
		if debit_sum != credit_sum:
			frappe.throw(
				msg=_(
					"Total credits don't equal debits. Make them equal and try again."
				)
			)


	def before_submit(self):
		self._check_for_balanced_entries()

	def _make_gl_entry(self, account: str, debit: float = 0, credit: float = 0):
		"""Make GL Entry for today with voucher info."""
		frappe.get_doc(
			doctype="GL Entry",
			posting_date=date.today(),
			account=account,
			debit=debit,
			credit=credit,
			voucher_type=self.doctype,
			voucher_no=self.name
		).insert()


	def _make_gl_entries_for_accounts(self):
		for entry in self.accounts:
			self._make_gl_entry(
				account=entry.account, debit=entry.debit, credit=entry.credit
			)

	def _make_gl_entries_for_accounts_on_cancel(self):
		for entry in self.accounts:
			self._make_gl_entry(
				account=entry.account, debit=entry.credit, credit=entry.debit
			)	

	def on_submit(self):
		self._make_gl_entries_for_accounts()

	def on_cancel(self):
		self._make_gl_entries_for_accounts_on_cancel()
