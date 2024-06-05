// Add a click event handler to the DIV#red_header element
$('#add_item').on('click', function(){
  // Create a new <li> element with the text 'Item'
  const newItem = $('<li>Item</li>');
  // Append the new <li> element to the <ul> element with class 'my_list'
  $('ul.my_list').append(newItem);
})