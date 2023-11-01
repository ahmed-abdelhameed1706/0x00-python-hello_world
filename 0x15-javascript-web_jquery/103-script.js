$(function (){

	$('INPUT#btn_translate').click(function () {
		const answer = $('INPUT#language_code').val()
		$.ajax({
                	type: 'GET',
                	url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + answer,
                	success: function(data) {
                		$('DIV#hello').text(data.hello)
			}
        	});
	})

	$('INPUT#language_code').on('keypress', function(e) {
		if (e.which === 13) {
			$('INPUT#btn_translate').click();
		}
	})
});
