# Copyright (c) 2023, Harpiya Software Technologies, LLC and contributors


from math import ceil

import harpiya
from harpiya import _
from harpiya.utils import (
	cint,
	get_fullname,
	global_date_format,
	markdown,
	sanitize_html,
	strip_html_tags,
	today,
)
from harpiya.website.utils import (
	clear_cache,
	find_first_image,
	get_comment_list,
	get_html_content_based_on_type,
)
from harpiya.website.website_generator import WebsiteGenerator


class Product(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from harpiya.types import DF

		product_categories: DF.Link
		meta_description: DF.TextEditor | None
		product_image: DF.AttachImage | None
		images: DF.Attach | None
		published: DF.Check
		route: DF.Data | None
		title: DF.Data
	# end: auto-generated types

	@harpiya.whitelist()
	def make_route(self):
		if not self.route:
			return (
				harpiya.db.get_value("Product Categories", self.product_categories, "route")
				+ "/"
				+ self.scrub(self.title)
			)
		
	def validate(self):
		super().validate()

	def on_update(self):
		super().on_update()
	
	def on_trash(self):
		super().on_trash()

	def get_context(self, context):
		# this is for double precaution. usually it wont reach this code if not published
		if not cint(self.published):
			raise Exception("This product has not been published yet!")

		context.category = harpiya.db.get_value(
			"Product Categories", context.doc.product_categories, ["title", "route"], as_dict=1
		)
		context.parents = [
			{"name": _("Anasayfa"), "route": "/"},
			{"name": "Ürünler", "route": "/products"},
			{"label": context.category.title, "route": context.category.route},
		]

	def fetch_social_links_info(self):
		url = harpiya.local.site + "/" + self.route

		return [
			{
				"icon": "twitter",
				"link": "https://twitter.com/intent/tweet?text=" + self.title + "&url=" + url,
			},
			{
				"icon": "facebook",
				"link": "https://www.facebook.com/sharer.php?u=" + url,
			},
			{
				"icon": "linkedin",
				"link": "https://www.linkedin.com/sharing/share-offsite/?url=" + url,
			},
			{
				"icon": "envelope",
				"link": "mailto:?subject=" + self.title + "&body=" + url,
			},
		]

def get_product_category(route):
    return harpiya.db.get_value("Product Categories", {"name": route}, "title") or route

def get_list_context(context=None):
    list_context = harpiya._dict(
        get_list=get_product_list,
        no_breadcrumbs=False,
        hide_filters=True,
        # show_search = True,
        title=_('Ürünler')
    )

    category = harpiya.utils.escape_html(harpiya.local.form_dict.product_categories or harpiya.local.form_dict.category)
    if category:
        category_title = get_product_category(category)
        list_context.sub_title = _("Posts filed under {0}").format(category_title)
        list_context.title = category_title

    elif harpiya.local.form_dict.txt:
        list_context.sub_title = _('Filtered by "{0}"').format(sanitize_html(harpiya.local.form_dict.txt))

    if list_context.sub_title:
        list_context.parents = [{"label": _("Anasayfa"), "route": "/"},
                                {"label": _("Ürünler"), "route": "/product"}]
    else:
        list_context.parents = [{"label": _("Anasayfa"), "route": "/"}]

    return list_context



def get_product_list(
	doctype, txt=None, filters=None, limit_start=0, limit_page_length=20, order_by=None
):
	conditions = []
	if filters and filters.get("product_categories"):
		category = filters.get("product_categories")
	else:
		category = harpiya.utils.escape_html(
			harpiya.local.form_dict.product_categories or harpiya.local.form_dict.category
		)

	if category:
		conditions.append("product_categories=%s" % harpiya.db.escape(category))


	if conditions:
		harpiya.local.no_cache = 1

	query = """\
		select
			*
		from `tabProduct`
		where published = 1
		{condition}
		order by name asc
		limit {page_len} OFFSET {start}""".format(
		start=limit_start,
		page_len=limit_page_length,
		condition=(" and " + " and ".join(conditions)) if conditions else "",
	)

	posts = harpiya.db.sql(query, as_dict=1)

	for post in posts:
		if post.content:
			post.content = strip_html_tags(post.content)


		post.category = harpiya.db.get_value(
			"Product Categories", post.product_categories, ["name", "route", "title"], as_dict=True
		)


	return posts