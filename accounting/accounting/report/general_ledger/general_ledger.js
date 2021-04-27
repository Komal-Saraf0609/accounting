// Copyright (c) 2016, Komal and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports['General Ledger'] = {
	filters: [
		{
			fieldname: 'posting_date',
			label: __('From'),
			fieldtype: 'Date',
		},
		{
			fieldname: 'posting_date',
			label: __('To'),
			fieldtype: 'Date',
			reqd: 1,
			default: frappe.datetime.get_today(),
		},
		{
			fieldname: 'voucher_type',
			label: __('Voucher Type'),
			fieldtype: 'Link',
			options:'DocType'
		},
		{
			fieldname: 'voucher_no',
			label: __('Voucher No'),
			fieldtype: 'Data',
		},
	],
};