#!/usr/bin/node

const first = parseInt(process.argv[2]);

function factorial (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(first));
