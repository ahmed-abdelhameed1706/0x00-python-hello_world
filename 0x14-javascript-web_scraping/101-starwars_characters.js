#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;

    const getCharacter = async (character) => {
      const characterData = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(error);
          }
        });
      });
      console.log(characterData);
    };

    (async () => {
      for (const character of characters) {
        await getCharacter(character);
      }
    })();
  }
});
