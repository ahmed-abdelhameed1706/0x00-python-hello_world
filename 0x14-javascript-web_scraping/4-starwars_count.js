#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

const idToLookUp = 'https://swapi-api.alx-tools.com/api/people/18/';

let count = 0;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const movies = data.results;

    for (const movie of movies) {
      if (movie.characters.includes(idToLookUp)) {
        count++;
      }
    }
    console.log(count);
  }
});
