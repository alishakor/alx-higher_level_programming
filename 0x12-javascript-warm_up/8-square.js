#!/usr/bin/node

//a script that prints a square
//The first argument is the size of the square
//If the first argument can’t be converted to an integer, print “Missing size”
//You must use the character X to print the square
//You must use console.log(...) to print all output
//You are not allowed to use var
//You must use a loop (while, for, etc.)

const square_size = parseInt(process.argv[2]);

if (isNaN(square_size)) {
  console.log('Missing size');
}
for (let i = 0; i < square_size; i++) {
  console.log('X'.repeat(square_size));
}
