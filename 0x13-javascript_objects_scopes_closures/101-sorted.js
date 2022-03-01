#!/usr/bin/node

const oldDict = require('./101-data.js').dict;
const newDict = {};
let array = [];
let value;
for (const key in oldDict) {
  value = oldDict[key];
  if (!newDict[value]) {
    for (const k in oldDict) {
      if (oldDict[k] === value) {
        array.push(k);
      }
    }
    newDict[value] = array;
    array = [];
  }
}
console.log(newDict);
