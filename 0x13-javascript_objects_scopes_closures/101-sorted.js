#!/usr/bin/node

const dict = require('./101-data').dict;

const reversedDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];

  if (reversedDict[occurrences] === undefined) {
    reversedDict[occurrences] = [userId];
  } else {
    reversedDict[occurrences].push(userId);
  }
}

console.log(reversedDict);
