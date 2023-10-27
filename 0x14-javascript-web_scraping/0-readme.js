#!/usr/bin/node

const fs = require('fs');
if (process.argv.length < 3) {
  console.log('Usage: ./0-readme.js [filename]');
  process.exit(1);
}
const filepath = process.argv[2];
fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.log('Error: ', err);
  }
  console.log(data);
});
