#!/usr/bin/node
// writes a string to a file

const fs = require('fs');
const filepath = process.argv[2];
const str = process.argv[3];

fs.writeFile(filepath, str, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
