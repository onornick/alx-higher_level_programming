#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.log('Usage: ./5-request_store.js [url] [filename]');
  process.exit(1);
}

const url = process.argv[2];
const filename = process.argv[3];

request(url).pipe(fs.createWriteStream(filename, 'utf-8'));
