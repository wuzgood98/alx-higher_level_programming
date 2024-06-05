$(document).ready(function(){
  // Fetch the characer name from the given URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(data) {
      // Update the text of the DIV#character with the character's name
      $('#character').text(data.name)
    },
    error: function() {
      console.error('An error occured while fetching the character data.')
    }
  })
})