#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: ./1-writeme.js [filename]');
  process.exit(1);
}

const filepath = process.argv[2];
const data = process.argv[3];
fs.writeFile(filepath, data, 'utf8', (err) => {
  if (err) {
    console.log('Error: ', err);
  }
});
