#!/usr/bin/node

const noArg = 'No argument';
const arg1 = process.argv[2];

if (arg1 === undefined) {
  console.log(noArg);
} else {
  console.log(arg1);
}
