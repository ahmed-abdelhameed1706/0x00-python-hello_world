#!/usr/bin/node
// Searching for second biggest number

const length = process.argv.length;

if (length <= 3) {
  console.log(0);
} else {
  const list = process.argv;
  list.sort().reverse();
  console.log(list[1]);
}
