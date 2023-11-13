#!/usr/bin/node
const argv = process.argv[2];
const msg = typeof argv === 'undefined' ? `My number: ${argv}` : 'Not a number';
console.log(msg);
