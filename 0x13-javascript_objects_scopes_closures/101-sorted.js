#!/usr/bin/node
/* imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence
*/
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const occurrence = dict[key].length;

  if (newDict[occurrence] === undefined) {
    newDict[occurrence] = [key];
  } else {
    newDict[occurrence].push(key);
  }
}

console.log(newDict);
