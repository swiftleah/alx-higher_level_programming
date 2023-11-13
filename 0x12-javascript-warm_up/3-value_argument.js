#!/usr/bin/node

const noArg = 'No argument';
const arg1 = process.argv[2];
const argnum = process.argv.length - 2;

if (argnum === 0) {
  console.log(noArg);
} else {
  console.log(arg1);
}
