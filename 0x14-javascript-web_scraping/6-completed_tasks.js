#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const obj = {};

    for (const item of data) {
      const userId = item.userId;
      if (userId in obj) {
        if (item.completed === true) {
          obj[userId] += 1;
        }
      } else {
        if (item.completed === true) {
          obj[userId] = 1;
        }
      }
    }
    console.log(obj);
  }
});
