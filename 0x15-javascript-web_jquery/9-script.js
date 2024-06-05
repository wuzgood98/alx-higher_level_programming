$(document).ready(function(){
  // Fetch the translation of 'Hello' from the given URL
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(data) {
      // Update the text of the DIV#hello with the translation of 'Hello'
      $('#hello').text(data.hello)
    },
    error: function() {
      console.error('An error occured while fetching the translation data')
    }
  })
})