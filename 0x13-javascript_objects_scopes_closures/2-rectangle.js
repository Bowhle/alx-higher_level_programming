#!/usr/bin/node
/** A class Rectangle that defines a rectangle */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    // If w or h is not valid, the instance remains an empty object
  }
};
