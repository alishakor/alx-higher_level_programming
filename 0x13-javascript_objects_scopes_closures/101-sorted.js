#!/usr/bin/node

// a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

// Your script must import dict from the file 101-data.js
// In the new dictionary:
// A key is a number of occurrences
// A value is the list of user ids
// Print the new dictionary at the end

const dict = require('./101-data.js').dict

const UserIdOccurences = {};

for (const [userId, occurrences] of Object.entries(dict)) {
  if (!UserIdOccurences[occurrences]) {
    UserIdOccurences[occurrences] = [];
  }
  UserIdOccurences[occurrences].push(userId);
}
console.log(UserIdOccurences);
