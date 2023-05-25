#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

//Import the request and fs modules
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line argument
const url = process.argv[2];
const file = process.argv[3];

// Make a GET request to teh URL and store the response object
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
     if (error) {
       console.error(error);
     } else {
       console.log(`${file}`);
       }
     });
   }
 });
