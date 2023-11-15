#!/usr/bin/node
const dict = require('./101-data.js').dict;
let dictNew = {};
for (let key in dict) {
  if (dictNew[dict[key]] === undefined) {
    dictNew[dict[key]] = [key];
  } else {
    dictNew[dict[key]].push(key);
  }
}
console.log(dictNew);
