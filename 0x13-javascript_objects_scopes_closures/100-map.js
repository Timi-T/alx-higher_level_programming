#!/usr/bin/node

const increment = {}
increment.index = 0;
const oldArray = require('./100-data').list;
const newArray = oldArray.map(myFunction);
function myFunction (x) {
  return x * increment.index++;
}
console.log(oldArray);
console.log(newArray);
