#!/usr/bin/node

const message = 'C is fun';
const iter = Number(process.argv[2]);

if (iter) {
  for (let i = 0; i < iter; i++) {
    console.log(message);
  }
} else {
  console.log('Missing number of occurrences');
}
