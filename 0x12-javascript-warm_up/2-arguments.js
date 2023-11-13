#!/usr/bin/node
const argCount = process.argv.length;
const msg = argCount === 2 ? 'No argument' : argCount === 3 ? 'Argument found' : 'Arguments found';
console.log(msg);

