#!/usr/bin/node

exports.callMeMoby = function (times, fn) {
  while (times) {
    fn();
    times--;
  }
};
