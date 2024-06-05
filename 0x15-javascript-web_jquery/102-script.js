$(document).ready(function(){
  // Function to fetch and display the translation of 'Hello'
  function fetchTranslation(languageCode) {
    // Fetch the translation from the API
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      method: 'GET',
      success: function(data) {
        // Display the translation in the DIV#hello element
        $('#hello').text(data.hello);
      },
      error: function() {
        console.error('An error occured while fetching the translation data')
        // Display an error message in the DIV#hello element
        $('#hello').text('Error: Translation not found')
      }
    })
  }
})

// Event handler for the btn_translate button
$('#btn_translate').on('click', function(){
  // Get the language code entered by the user
  const languageCode = $('#language_code').val();
  // Fetch and display the translation for the entered language code
  fetchTranslation(languageCode);
})