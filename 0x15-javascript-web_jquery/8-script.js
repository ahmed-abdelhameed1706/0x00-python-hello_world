$(function (){
	$.ajax({
		type: 'GET',
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		success: function(data) {
			$.each(data, function (i, item) {
				$('UL#list_movies').append(item.title)
			})
		}
	});
});
