#!/usr/bin/node

let num = process.argv[2];
num = Number(num);

function factorial (num) {
  if (!num) {
    return (1);
  }
  return (num * factorial(num - 1));
}
const fact = factorial(num);
console.log(fact);
