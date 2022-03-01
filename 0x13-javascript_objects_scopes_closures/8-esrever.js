#!/usr/bin/node

exports.esrever = function (list) {
  const strLen = list.length - 1;
  const newList = [];
  for (let i = strLen, j = 0; i >= 0; i--, j++) {
    newList[j] = list[i];
  }
  return newList;
};
