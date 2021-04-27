# -*- coding: utf-8 -*-
# Copyright (c) 2021, Komal and Contributors
# See license.txt
from __future__ import unicode_literals

import unittest

import frappe

from ..account.test_account import test_create_account


def create_test_customer(user: str = frappe.mock("name")):
	test_create_account()
	return frappe.get_doc({
		"doctype": "Customer",
		"user": user,
	}).insert(ignore_if_duplicate=True)


class TestCustomer(unittest.TestCase):
	pass