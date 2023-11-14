#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./concat_files.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Read content from the first file
const file1Content = fs.readFileSync(file1Path, 'utf-8');

// Read content from the second file
const file2Content = fs.readFileSync(file2Path, 'utf-8');

// Concatenate the contents
const concatenatedContent = file1Content + file2Content;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationPath, concatenatedContent, 'utf-8');

console.log(`Files ${file1Path} and ${file2Path} successfully concatenated to ${destinationPath}`);
