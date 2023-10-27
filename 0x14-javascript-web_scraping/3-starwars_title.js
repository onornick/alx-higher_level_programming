#!/usr/bin/node

const request = require('request');
if (process.argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js [id]');
  process.exit(1);
}
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
request(url, (err, response, data) => {
  if (err) {
    console.log('Error:', err);
  }
  const resp = JSON.parse(data);
  console.log(resp.title);
});
