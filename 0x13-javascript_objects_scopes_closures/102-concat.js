#!/usr/bin/node

const fs = require('fs');

const myArgs = process.argv.slice(2);
let textOne;
fs.readFile(myArgs[0], 'utf-8', (err, data) => {
  if (err) throw err;
  textOne = data;
  fs.readFile(myArgs[1], 'utf-8', (err, data) => {
    if (err) throw err;
    const textThree = textOne + data;
    fs.writeFile(myArgs[2], textThree, (err) => {
      if (err) throw err;
    });
  });
});
