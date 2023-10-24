#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

let count = 0;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const movies = data.results;

    for (const movie of movies) {
      for (const character of movie.characters) {
        const id = character.split('/')[5];
        if (id === '18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
