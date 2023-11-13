#!/usr/bin/node

const X = parseInt(process.argv[2]);

if (!X || isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < X; i++) {
    let row = '';
    for (let j = 0; j < X; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
