#!/usr/bin/node

exports.esrever = function (list) {
  // Copy the original list to avoid modifying it
  const reversedList = list.slice();

  // Swap elements from the beginning and end
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};
