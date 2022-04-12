#!/usr/bin/node

const request = require('request');
const id = (process.argv)[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
