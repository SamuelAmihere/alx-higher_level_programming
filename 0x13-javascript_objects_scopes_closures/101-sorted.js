#!/usr/bin/node
const dict = require('./101-data.js').dict;
let dc = {};
for (let key in dict) {
  if (dc[dict[key]] === undefined) {
    dc[dict[key]] = [key];
  } else {
    dc[dict[key]].push(key);
  }
}
console.log(dc);
