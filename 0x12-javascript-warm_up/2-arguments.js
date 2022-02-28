#!/usr/bin/node

let myOutput;
const myArgs = process.argv.slice(2);
if (myArgs.length === 0) {
  myOutput = 'No argument';
} else if (myArgs.length === 1) {
  myOutput = 'Argument found';
} else {
  myOutput = 'Arguments found';
}
console.log(myOutput);
