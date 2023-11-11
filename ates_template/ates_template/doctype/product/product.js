// Copyright (c) 2023, Harpiya Software Technologies, LLC and contributors

harpiya.ui.form.on("Product", {
	refresh: function (frm) {
		frm.trigger("add_product_images");
		frm.trigger("add_variant_images");
		frm.trigger("add_publish_button");
	},
	title: function (frm) {
		frm.trigger("set_route");
	},

	product_categories(frm) {
		frm.trigger("set_route");
	},
	set_route(frm) {
		if (frm.doc.route) return;
		if (frm.doc.title && frm.doc.product_categories) {
			frm.call("make_route").then((r) => {
				frm.set_value("route", r.message);
			});
		}
	},
	add_publish_button(frm) {
		frm.add_custom_button(frm.doc.published ? __("Yayınlanmadı") : __("Yayınlandı"), () => {
			frm.set_value("published", !frm.doc.published);
			frm.save();
		});
	},

	add_variant_images(frm) {
		frm.add_custom_button(__('Varyant Resmi Yükle'), () => {
			const d = new harpiya.ui.Dialog({
				title: __('Klasörden Resimleri Getir'),
				fields: [
					{
						label: __('Klasör Adı'),
						fieldtype: 'Link',
						fieldname: 'folder',
						options: 'File',
						reqd: 1
					}
				],
				primary_action_label: __('Tabloya Ekle'),
				primary_action: ({ folder }) => {
					harpiya.db.get_list('File', {
						fields: ['file_url', 'file_name'],
						filters: {
							folder: folder
						}
					}).then(variant_images => {
						frm.doc.variant_images = frm.doc.variant_images || [];
						variant_images.forEach(image => {
							console.log(image)
							var new_row = frm.add_child("variant_images");
							new_row.image_title = image.file_name;
							new_row.image = image.file_url;
						});

						frm.refresh_field('variant_images');
						d.hide();
					});
				}
			});

			d.show();
		})
	},

	add_product_images(frm) {
		frm.add_custom_button(__('Ürün Resmi Yükle'), () => {
			const d = new harpiya.ui.Dialog({
				title: __('Klasörden Resimleri Getir'),
				fields: [
					{
						label: __('Klasör Adı'),
						fieldtype: 'Link',
						fieldname: 'folder',
						options: 'File',
						reqd: 1
					}
				],
				primary_action_label: __('Tabloya Ekle'),
				primary_action: ({ folder }) => {
					harpiya.db.get_list('File', {
						fields: ['file_url', 'file_name'],
						filters: {
							folder: folder
						}
					}).then(images => {
						frm.doc.images = frm.doc.images || [];
						images.forEach(image => {
							console.log(image)
							var new_row = frm.add_child("images");
							new_row.image_title = image.file_name;
							new_row.image = image.file_url;
						});

						frm.refresh_field('images');
						d.hide();
					});
				}
			});

			d.show();
		})
	}
});
