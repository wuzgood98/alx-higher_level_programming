$(document).ready(function() {
  // Add a click event handler to the DIV#red_header element
  $('#red_header').click(function(){
    // Update the text color of the <header> elements to red (#FF0000)
    $('header').css('color', '#FF0000')
  })
})