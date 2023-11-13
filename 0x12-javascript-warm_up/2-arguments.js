#!/usr/bin/node

const numArgs = process.argv.length - 2;
const noArg = 'No argument';
const oneArg = 'Argument found';
const moreArgs = 'Arguments found';

if (numArgs === 0) {
  console.log(noArg);
} else if (numArgs === 1) {
  console.log(oneArg);
} else {
  console.log(moreArgs);
}
