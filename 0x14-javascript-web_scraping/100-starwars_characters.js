#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request

// Import the request module
const request = require('request');

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Define the url of the Star wars API
const url = 'https://swapi-api.alx-tools.com/api/films';

// Make a GET request to the films endpoint with the movie ID
request(url + '/' + `${movieId}`, (error, response, body) => {
  // Check if there was error making the request and print it
  if (error) {
    console.error(error);
  } else {
    // Parse the response as JSON
    const movieData = JSON.parse(body);
    // Get the list of characters URL from the movie data
    const charUrls = movieData.characters;
    // Loop through each character URL
    charUrls.forEach((charUrl) => {
      // Make a GET request to the character URL
      request(charUrl, (error, response, body) => {
        // check if there was error making request and print it
        if (error) {
          console.error(error);
        } else {
          // Parse the response to JSOn
          const charData = JSON.parse(body);
          // Print the name of the character line by line
          console.log(charData.name);
        }
      });
    });
  }
});
