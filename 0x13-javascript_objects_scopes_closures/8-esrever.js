#!/usr/bin/node
// A function that returns the reversed version of a list
exports.esrever = function (list) {
  const rlist = [];
  while (list.length > 0) {
    rlist.push(list.pop());
  }
  return list.sort(() => 1);
};
