#!/usr/bin/node
const fs = require('fs');

const filepath = process.argv[2];

const stringToWrite = process.argv[3];

fs.writeFile(filepath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
