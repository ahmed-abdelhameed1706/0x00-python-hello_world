#!/usr/bin/node

const length = process.argv.length;
const list = process.argv;

if (length <= 3) {
  console.log(0);
} else {
  list.sort().reverse();
  console.log(parseInt(list[1]));
}
