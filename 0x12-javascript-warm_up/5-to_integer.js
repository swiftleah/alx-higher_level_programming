#!/usr/bin/node

const arg1 = parseInt(process.argv[2]);
const notnum = 'Not a number';
const mynum = 'My number:' + ' ' + arg1;

if (!isNaN(arg1)) {
  console.log(mynum);
} else {
  console.log(notnum);
}
