// a JavaScript script that adds a <li> element to a list when
// the user clicks on the tag DIV#add_item:
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list
$('#add_item').on('click', function () {
  const newElement = $('<li>Item</li>');
  $('ul.my_list').append(newElement);
});
