#!/usr/bin/node
// prints the title of a star wars movie where the episode number matches
// specific int

const req = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(URL, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
