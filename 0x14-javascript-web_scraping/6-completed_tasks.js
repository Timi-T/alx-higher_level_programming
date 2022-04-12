#!/usr/bin/node

const request = require('request');
const url = (process.argv)[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const todos = JSON.parse(body);
  const ret = {};
  for (let i = 0; i < todos.length; i++) {
    const id = (todos[i]).userId;
    if ((todos[i]).completed) {
      if (ret[String(id)]) {
        ret[String(id)] += 1;
      } else {
        ret[String(id)] = 1;
      }
    }
  }
  console.log(ret);
});
