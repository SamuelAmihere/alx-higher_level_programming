#!/usr/bin/node

const req = require('request');
const req_id = process.argv[2];
req(req_id, (err, res, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
