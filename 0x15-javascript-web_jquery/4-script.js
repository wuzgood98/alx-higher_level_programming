$(document).ready(function(){
  // Add a click event handler to the DIV#red_header element
  $('#toggle_header').click(function(){
    // Check the current class and toggle between 'red' and 'green'
    if($('header').hasClass('red')) {
      $('header').removeClass('red').addClss('green')
    } else {
      $('header').removeClass('green').addClass('red')
    }
  })
})