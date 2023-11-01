$(function () {
	$('DIV#add_item').click(function () {
        	cosnt new_element = $('<li>Item</li>')
        	$('UL.my_list').append(new_element)
	});

	$('DIV#remove_item').click(function () {
		('UL.my_list li:last-child').remove()
	});

	$('DIV#clear_list').click(function () {
		('UL.my_list').empty();
	});
})
