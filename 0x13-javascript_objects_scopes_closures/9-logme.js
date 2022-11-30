#!/usr/bin/node
let nargt = 0;

exports.logMe = function (item) {
  console.log(nargt + ': ' + item);
  nargt++;
};
