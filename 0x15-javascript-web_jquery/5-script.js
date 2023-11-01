$('DIV#add_item').click(function () {
	cosnt new_element = $('<li>Item</li>')
	$('UL.my_list').append(new_element)
});
