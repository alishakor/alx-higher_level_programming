// A JavaScript script that fetches the character name from this
// URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character
// You must use the JQuery API
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const characterName = data.name;
  $('#character').text(characterName);
});
