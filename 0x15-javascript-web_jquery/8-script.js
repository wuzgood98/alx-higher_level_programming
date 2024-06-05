$(document).ready(function(){
  // Fetch and list the title for all movies
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      // Loop through the movies and create a new <li> element for each movie
      $.each(data.results, function(index, movie) {
        const movieItem = $('<li></li>');
        movieItem.text(movie.title);
        // Append the new <li> element to the <ul> element with class 'my_list'
        $('#list_movies').append(movieItem);
      })
    },
    error: function() {
      console.error('An error occured while fetching the movie data')
    }
  })
})