#!/usr/bin/node
/* This script prints two arguments passed to it, in the following format: “ is ” */

const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

console.log(arg1 + ' is ' + arg2);
