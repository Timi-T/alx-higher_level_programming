#!/usr/bin/node

const myArgs = process.argv.slice(2);
let secondBiggest = 0;
let newBiggest = 0;
const arrayLen = myArgs.length;

function max (a, b) {
  if (a >= b) {
    return a;
  } else {
    return b;
  }
}

if (arrayLen === 2) {
  const a = Number(myArgs[0]);
  const b = Number(myArgs[1]);
  if (max(a, b) === a) {
    newBiggest = b;
  } else {
    newBiggest = a;
  }
}
if (arrayLen > 2) {
  let a, b, c, x, y;
  for (let i = 0; i < arrayLen - 2; i++) {
    a = Number(myArgs[i]);
    b = Number(myArgs[i + 1]);
    c = Number(myArgs[i + 2]);

    x = max(a, b);
    if (x === a) {
      y = max(a, c);
    } else {
      y = max(b, c);
    }
    if (y === a) {
      secondBiggest = max(c, b);
    } else if (y === c) {
      secondBiggest = max(a, b);
    } else if (y === b) {
      secondBiggest = max(a, c);
    }
    if (secondBiggest > newBiggest) {
      newBiggest = secondBiggest;
    }
  }
}
console.log(newBiggest);
