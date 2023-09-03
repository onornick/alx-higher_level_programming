#!/usr/bin/node
/**
 * class Square that defines a square and inherits from Square of 5-square.js:
 * You must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */
class Square extends require('./5-square') {
  charPrint (char = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += char;
      }
      console.log(row);
    }
  }
}
