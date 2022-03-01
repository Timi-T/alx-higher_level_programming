#!/usr/bin/node

const oldArray = require('./100-data').list;
const newArray = oldArray.map(x => x * oldArray.indexOf(x));
console.log(oldArray);
console.log(newArray);
