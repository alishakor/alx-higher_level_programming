// A JavaScript script that fetches and prints how to say “Hello” depending on the language
// You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
// The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
// You can’t use document.querySelector to select the HTML tag
// You must use the JQuery API
// You script must work when imported from the <head> tag
$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    fetchTranslation();
  });

  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) { // Enter key
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

    $.get(apiUrl, function (data) {
      const translation = data.hello;
      $('#hello').text(translation);
    }).fail(function () {
      $('#hello').text('Error occurred while fetching the translation.');
    });
  }
});
