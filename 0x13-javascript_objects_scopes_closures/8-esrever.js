#!/usr/bin/node

// Write a function that returns the reversed version of a list:
// Prototype: exports.esrever = function (list)
// You are not allow to use the built-in method reverse

exports.esrever = function (list) {
  const reverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
