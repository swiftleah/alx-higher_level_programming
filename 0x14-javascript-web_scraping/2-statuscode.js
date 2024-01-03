#!/usr/bin/node
// displays the status code of a GET request

const arg = process.argv;
const req = require('request');
req(arg[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
