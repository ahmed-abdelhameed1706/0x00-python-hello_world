#!/usr/bin/node

const length = process.argv.length;

if (length <= 3) {
  console.log('0');
} else {
  const list = process.argv;
  list.sort().reverse();
  console.log(parseInt(list[1]));
}
