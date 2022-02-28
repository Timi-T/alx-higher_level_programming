#!/usr/bin/node

const myArgs = process.argv.slice(2);

function add (a, b) {
  return a + b;
}
const a = Number(myArgs[0]);
const b = Number(myArgs[1]);
const sum = add(a, b);
console.log(sum);
