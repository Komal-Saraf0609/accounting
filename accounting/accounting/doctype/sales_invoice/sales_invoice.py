from __future__ import unicode_literals

import frappe
from datetime import date
from frappe.utils import today

from accounting.controllers.transaction import Transaction


class SalesInvoice(Transaction):

	def validate(self):
		self.validate_date()

	def validate_date(self):
		date = today()
		self.total_price = 0
		self.sales_invoice_total_quantity = 0
		#frappe.throw(date)
		if not self.posting_date >= date:
			frappe.throw("Posting Date should be greater than or equal to today's date")
		for sales_invoice_item in self.item:
			item = frappe.get_doc("Item", sales_invoice_item.item)
			self.amount = item.price * sales_invoice_item.quantity
			sales_invoice_item.amount = self.amount
			self.total_price += sales_invoice_item.amount
			self.sales_invoice_total_quantity += sales_invoice_item.quantity
			self.total = self.total_price
			self.total_quantity = self.sales_invoice_total_quantity
			if sales_invoice_item.quantity == 0:
				frappe.throw("The quantity cannot be zero")
			elif self.total_quantity == 0:
				frappe.throw("The total quantity cannot be zero")
			elif self.total == 0:
				frappe.throw("The total cannot be zero")

			


	def before_submit(self):
		self.debit_account = "Sales"
		customer = frappe.get_doc("Customer", self.customer)
		self.credit_account = customer.account
	
	def before_cancel(self):
		self.debit_account = "Sales"
		customer = frappe.get_doc("Customer", self.customer)
		self.credit_account = customer.account

	def on_submit(self):
		self.amount = 0
		for sales_invoice_item in self.item:
			item = frappe.get_doc("Item", sales_invoice_item.item)
			self.amount += item.price * sales_invoice_item.quantity
			#sales_invoice_item.amount = self.amount
		super().on_submit()

	def on_cancel(self):
		self.amount = 0
		for sales_invoice_item in self.item:
			item = frappe.get_doc("Item", sales_invoice_item.item)
			self.amount += item.price * sales_invoice_item.quantity
		
		super().on_cancel()
		