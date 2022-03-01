#!/usr/bin/node

const fs = require('fs');

let textOne;
fs.readFile('fileA', 'utf-8', (err, data) => {
  if (err) throw err;
  textOne = data;
  fs.readFile('fileB', 'utf-8', (err, data) => {
    if (err) throw err;
    const textThree = textOne + data;
    fs.writeFile('fileC', textThree, (err) => {
      if (err) throw err;
    });
  });
});
