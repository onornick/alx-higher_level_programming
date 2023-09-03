#!/usr/bin/node
/**
 * function that returns the reversed version of a list:
 * Prototype: exports.esrever = function (list)
 * You are not allow to use the built-in method reverse
 */
exports.esrever = function (list) {
  const reversedList = [];
  let i = list.length - 1;
  for (; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
