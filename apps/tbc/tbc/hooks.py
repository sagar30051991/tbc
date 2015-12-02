# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "tbc"
app_title = "TBC"
app_publisher = "Frappe"
app_description = "App for Loan Handling System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sagar.s@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tbc/css/tbc.css"
# app_include_js = "/assets/tbc/js/tbc.js"

# include js, css files in header of web template
# web_include_css = "/assets/tbc/css/tbc.css"
# web_include_js = "/assets/tbc/js/tbc.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tbc.install.before_install"
# after_install = "tbc.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tbc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tbc.tasks.all"
# 	],
# 	"daily": [
# 		"tbc.tasks.daily"
# 	],
# 	"hourly": [
# 		"tbc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tbc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tbc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tbc.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tbc.event.get_events"
# }

