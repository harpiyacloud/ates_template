app_name = "ates_template"
app_title = "Ates Template"
app_publisher = "Harpiya Software Technologies, LLC"
app_description = "Template for Ates Triko"
app_email = "info@harpiya.com"
app_license = "mit"


website_route_rules = [
	{"from_route": "/products/<category>", "to_route": "Product"},
]

global_search_doctypes = {
	"Default": [
		{"doctype": "Product"},
	]
}

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ates_template/css/ates_template.css"
# app_include_js = "/assets/ates_template/js/ates_template.js"

# include js, css files in header of web template
# web_include_css = "/assets/ates_template/css/ates_template.css"
# web_include_js = "/assets/ates_template/js/ates_template.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ates_template/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ates_template/public/icons.svg"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ates_template.utils.jinja_methods",
#	"filters": "ates_template.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ates_template.install.before_install"
# after_install = "ates_template.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ates_template.uninstall.before_uninstall"
# after_uninstall = "ates_template.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ates_template.utils.before_app_install"
# after_app_install = "ates_template.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ates_template.utils.before_app_uninstall"
# after_app_uninstall = "ates_template.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See harpiya.core.notifications.get_notification_config

# notification_config = "ates_template.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "harpiya.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "harpiya.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ates_template.tasks.all"
#	],
#	"daily": [
#		"ates_template.tasks.daily"
#	],
#	"hourly": [
#		"ates_template.tasks.hourly"
#	],
#	"weekly": [
#		"ates_template.tasks.weekly"
#	],
#	"monthly": [
#		"ates_template.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ates_template.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"harpiya.desk.doctype.event.event.get_events": "ates_template.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Harpiya apps
# override_doctype_dashboards = {
#	"Task": "ates_template.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ates_template.utils.before_request"]
# after_request = ["ates_template.utils.after_request"]

# Job Events
# ----------
# before_job = ["ates_template.utils.before_job"]
# after_job = ["ates_template.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ates_template.auth.validate"
# ]
