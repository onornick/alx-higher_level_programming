#!/usr/bin/node

const request = require('request');
if (process.argv.length < 3) {
  console.log('Usage: ./6-completed_tasks.js [url]');
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 1;
      } else {
        completedTasksByUser[task.userId]++;
      }
    }
  });

  console.log(completedTasksByUser);
});
