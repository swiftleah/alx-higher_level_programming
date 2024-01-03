#!/usr/bin/node
// gets content of specified webpage and stores it in a file

const filepath = process.argv[2];
const fs = require('fs');
const req = require('request');
req(filepath).pipe(fs.createWriteStream(process.argv[3]));
