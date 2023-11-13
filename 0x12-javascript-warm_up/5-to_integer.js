#!/usr/bin/node
const argv = process.argv[2];
const msg = typeof argv === 'undefined' ? 'Not a number' : `My number: ${argv}`;
console.log(msg);
