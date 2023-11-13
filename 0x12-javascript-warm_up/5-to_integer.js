#!/usr/bin/node
const argv = Number(Math.floor(process.argv[2])));
const msg = isNaN(argv) ? 'Not a number' : `My number: ${argv}`;
console.log(msg);
