$(document).ready(function(){
  // Add this item to the list when DIV#add_item is clicked
  $('#add_item').on('click', function(){
    $('ul.my_list').append('<li>Item</li>');
  })

  // Remove this item from the list when DIV#remove_item is clicked
  $('#remove_item').on('click', function(){
    $('ul.my_list li:last').remove();
  })

  // Clear all items from the list when DIV#clear_list is clicked
  $('#clear_list').on('click', function(){
    $('ul.my_list').empty();
  })
})