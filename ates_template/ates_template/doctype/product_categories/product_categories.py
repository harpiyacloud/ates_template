# Copyright (c) 2023, Harpiya Software Technologies, LLC
from harpiya.website.utils import clear_cache
from harpiya.website.website_generator import WebsiteGenerator


class ProductCategories(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from harpiya.types import DF

		description: DF.SmallText | None
		preview_image: DF.AttachImage | None
		published: DF.Check
		route: DF.Data | None
		title: DF.Data
	# end: auto-generated types
	def autoname(self):
		# to override autoname of WebsiteGenerator
		self.name = self.scrub(self.title)

	def on_update(self):
		clear_cache()

	def set_route(self):
		# Override products route since it has to been templated
		self.route = "products/" + self.name