#!/usr/bin/node
/* This script prints the addition of 2 integers */

const int1 = process.argv[2];
const int2 = process.argv[3];

function add (a, b) {
  return a + b;
}
const a = parseInt(int1);
const b = parseInt(int2);

console.log(add(a, b));
