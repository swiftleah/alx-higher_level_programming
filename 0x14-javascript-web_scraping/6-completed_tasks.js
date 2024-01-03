#!/usr/bin/node
// computes the number of tasks completed by user ID

const args = process.argv;
const requrl = args[2];
const req = require('request');
req(requrl, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todo = JSON.parse(body);
    const dash = {};
    for (let i = 0; i < todo.length; i++) {
      const status = (todo[i].completed);
      const key = todo[i]['userId'].toString();
      if (status) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
