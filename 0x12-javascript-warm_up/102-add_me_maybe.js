#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
   const y = ++x;
   theFunction(y);
};
