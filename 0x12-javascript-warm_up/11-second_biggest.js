#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));
const sortedargs = numbers.sort((a, b) => b - a);
const second = sortedargs[1] || 0;
console.log(second);
