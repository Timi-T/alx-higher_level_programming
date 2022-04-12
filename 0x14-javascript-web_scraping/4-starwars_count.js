#!/usr/bin/node

const request = require('request');
const url = (process.argv)[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let count = 0;

  const bodyObj = JSON.parse(body);
  const films = bodyObj.results;
  for (let i = 0; i < films.length; i++) {
    const film = films[i];
    const characters = film.characters;
    for (let j = 0; j < characters.length; j++) {
      if ((characters[j]).includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
