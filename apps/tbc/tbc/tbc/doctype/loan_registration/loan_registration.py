# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LoanRegistration(Document):
pass
@frappe.whitelist()
def get_amount(source_name):
	target = get_mapped_doc("LoanRegistration", source_name, {
		"LoanRegistration": {
			"doctype": "loan_entry"
		}
	})
	return target
