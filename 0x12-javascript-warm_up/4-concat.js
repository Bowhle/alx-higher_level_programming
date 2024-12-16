#!/usr/bin/node
/* This script prints two arguments passed to it, in the following format: “ is ” */

const args1 = process.argv[2];
const args2 = process.argv[3];

console.log(args1 + ' is ' + args2);
