#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Using the reduce function to count occurrences
  return list.reduce((count, currentElement) => {
    return (currentElement === searchElement) ? count + 1 : count;
  }, 0);
};
