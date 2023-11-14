#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  x = ++x
  theFunction(x);
};
