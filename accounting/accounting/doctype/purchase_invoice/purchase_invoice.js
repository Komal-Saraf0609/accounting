// Copyright (c) 2021, Komal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Purchase Invoice', {
	refresh: function (frm) {
		frappe.ui.form.on('Purchase Invoice', {
			refresh: function (frm) {
				frappe.require('/assets/accounting/js/add_button.js', () => {
					add_accounting_ledger_btn(frm);
				});
			},
		});

	},
});


