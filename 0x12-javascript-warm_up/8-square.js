#!/usr/bin/node

let message = '';
const iter = Number(process.argv[2]);

if (iter) {
  for (let i = 0; i < iter; i++) {
    for (let j = 0; j < iter; j++) {
      message += 'X';
    }
    console.log(message);
    message = '';
  }
} else {
  console.log('Missing size');
}
