#!/usr/bin/node

exports.esrever = function (list) {
  let strLen = list.length - 1;
  let newList = [];
  for (let i = strLen, j = 0; i >= 0; i--, j++) {
    newList[j] = list[i];
  }
  return newList;
};
