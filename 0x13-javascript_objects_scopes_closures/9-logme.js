#!/usr/bin/node
/** Function that prints the number of arguments
and the current argument value */
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
