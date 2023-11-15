#!/usr/bin/node
const { dict } = require('./101-data');
const converted = Object.entries(dict);
const newDict = {};
converted.forEach(item => {
  newDict[item[1]] ? newDict[item[1]].push(item[0]) : newDict[item[1]] = [item[0]];
});
console.log(newDict);
