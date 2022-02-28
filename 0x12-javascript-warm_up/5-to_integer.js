#!/usr/bin/node

const myArg = process.argv.slice(2);

const myNum = Number(myArg[0]);

if (myNum) {
  console.log('My number:', myNum);
} else {
  console.log('Not a number');
}
