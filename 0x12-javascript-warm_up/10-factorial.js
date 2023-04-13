#!/usr/bin/node

//a script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer)
// used for computing the factorial
// Factorial of NaN is 1
// You must do it recursively
// You must use a function
// You must use console.log(...) to print all output
// You are not allowed to use var

function Factorial (numb) {
  let Fact_result = 1;
  for (i = 2; i <= numb; i++) {
    Fact_result *= i;
  }
  return Fact_result;
}

const arg1 = process.argv[2];
if (arg1) {
  const result = Factorial(arg1);
  console.log(result);
} else if (isNaN) {
    console.log(1);
}

