#!/usr/bin/node
// Write a script that i if a fil.
// The first argument is the file path
// The content of the file must be read in utf-8
// If an error occurred during the reading, print the error object
const fs = require('fs');

const arg = process.argv[2];

fs.readFile(arg, 'utf8', (error, content) => {
  if (error) {
    console.error(error);
  } else {
      console.log(content);
  }
});
