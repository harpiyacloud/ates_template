// Copyright (c) 2022, Harpiya Software Technologies


harpiya.ready(function() {

	if(harpiya.utils.get_url_arg('subject')) {
	  $('[name="subject"]').val(harpiya.utils.get_url_arg('subject'));
	}

	$('.btn-send').off("click").on("click", function() {
		var email = $('[name="email"]').val();
		var fullname = $('[name="name"]').val();
		var message = $('[name="message"]').val();

		if(!(fullname && email && message)) {
			harpiya.msgprint('{{ _("Size geri dönebilmemiz için lütfen hem e-posta adresinizi hem de mesajınızı giriniz. Teşekkürler!") }}');
			return false;
		}

		if(!validate_email(email)) {
			harpiya.msgprint('{{ _("E-posta adresiniz hatalı. Geri dönebilmemiz için lütfen geçerli bir e-posta adresi girin.") }}');
			$('[name="email"]').focus();
			return false;
		}

		$("#contact-alert").toggle(false);
		harpiya.call({
			type: "POST",
			method: "harpiya.www.contact.send_message",
			args: {
				subject: $('[name="subject"]').val(),
				sender: email,
				message: fullname + "<br>"+ message,
			},
			callback: function(r) {
				if (!r.exc) {
					harpiya.msgprint('{{ _("Mesajın için teşekkürler") }}');
				}
				$(':input').val('');
			},
		});
	});
});

var msgprint = function(txt) {
	if(txt) $("#contact-alert").html(txt).toggle(true);
}
