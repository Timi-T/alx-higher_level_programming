#!/usr/bin/node

let myOutput;
if (process.argv.length === 2) {
  myOutput = 'No argument';
} else {
  myOutput = 'Argument found';
}
console.log(myOutput);
