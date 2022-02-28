#!/usr/bin/node

const myArgs = process.argv.slice(2);

let firstArg = 'undefined';
const secArg = ' is ';
let thirdArg = 'undefined';

if (myArgs[0]) {
  firstArg = myArgs[0];
}
if (myArgs[1]) {
  thirdArg = myArgs[1];
}
console.log(firstArg + secArg + thirdArg);
