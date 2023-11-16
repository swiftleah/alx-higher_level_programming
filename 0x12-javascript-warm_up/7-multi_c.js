#!/usr/bin/node

const x = parseInt(process.argv[2]);
const message = 'C is fun';
const missing = 'Missing number of occurrences';

if (!x) {
  console.log(missing);
}
for (let i = 0; i < x; i++) {
  console.log(message);
}
