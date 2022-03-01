#!/usr/bin/node

const Squared = require('./5-square.js');
class Square extends Squared {
  charPrint (c) {
    if (c) {
      let sq = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          sq += 'C';
        }
        console.log(sq);
        sq = '';
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
