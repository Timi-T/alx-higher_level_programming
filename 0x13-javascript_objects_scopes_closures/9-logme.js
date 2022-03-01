#!/usr/bin/node

const counter = {};
counter.id = 0;

exports.logMe = function (item) {
  const index = counter.id++;
  console.log(index + ': ' + item);
};
