#!/usr/bin/node

class Rectangle extends require('./0-rectangle'){
  width;
  height;
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
