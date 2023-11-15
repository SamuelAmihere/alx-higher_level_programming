#!/usr/bin/node
const dict = require('./101-data.js').dict;
let dictNew = {};
for (let key in dict) {
  var value = dictNew[dict[key]];
  if (value === undefined) {
    value = [key];
  } else {
    value.push(key);
  }
  dictNew[dict[key]] = value;
}
console.log(dictNew);
