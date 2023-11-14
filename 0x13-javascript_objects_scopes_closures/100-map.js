#!/usr/bin/node

const list = require('./100-data');

// Original list
console.log('Original list:', list);

// New list computed using map
const newList = list.map((value, index) => value * index);

console.log('New list:', newList);
