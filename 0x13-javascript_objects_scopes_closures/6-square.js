#!/usr/bin/node
/** A class Square that defines a square and inherits from Square */
const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  charPrint (c) {
    const char = c || 'X'; // Default to 'X' if c is undefined
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
