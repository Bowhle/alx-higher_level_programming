#!/usr/bin/node
/* This script prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/

const args = process.argv[2];

if (args === undefined || isNaN(parseInt(args))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args));
}
