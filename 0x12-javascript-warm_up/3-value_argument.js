#!/usr/bin/node

let myArgs = process.argv;
if (myArgs[2]) {
  myArgs = myArgs.slice(2);
  myArgs.forEach(function (myArgs) {
    console.log(myArgs);
  });
} else {
  console.log('No argument');
}
