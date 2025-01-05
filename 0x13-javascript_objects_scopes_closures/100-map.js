#!/usr/bin/node
/* Imports an array and computes a new array */
const array = require('./100-data').list;

console.log(array); // Printing the original array

// Using map to multiply each element by its index
console.log(array.map((item, index) => item * index));
