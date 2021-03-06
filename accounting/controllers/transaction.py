from __future__ import unicode_literals

from datetime import date

import frappe
from frappe.model.document import Document


class Transaction(Document):


	def _make_gl_entry(self, account: str, debit: float = 0, credit: float = 0):
		frappe.get_doc(
			doctype="GL Entry",
			posting_date=date.today(),
			account=account,
			debit=debit,
			credit=credit,
			voucher_type=self.doctype,
			voucher_no=self.name
		).insert()

	def _make_reverse_gl_entry(self, account: str, debit: float = 0, credit: float = 0):
		frappe.get_doc(
			doctype="GL Entry",
			posting_date=date.today(),
			account=account,
			debit=credit,
			credit=debit,
			voucher_type=self.doctype,
			voucher_no=self.name
		).insert()

	def _make_gl_entries(self, amount: float):
		try:
			self._make_gl_entry(self.debit_account, debit=amount)
			self._make_gl_entry(self.credit_account, credit=amount)
		except frappe.exceptions.ValidationError:
			frappe.db.rollback()

	def _make_reverse_gl_entries(self, amount: float):
		try:
			self._make_reverse_gl_entry(self.debit_account, credit=amount)
			self._make_reverse_gl_entry(self.credit_account, debit=amount)
		except frappe.exceptions.ValidationError:
			frappe.db.rollback()

	def on_submit(self):
		self._make_gl_entries(self.amount)

	def on_cancel(self):
		self._make_reverse_gl_entries(self.amount)



