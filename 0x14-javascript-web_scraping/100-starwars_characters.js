#!/usr/bin/node

const req = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

req(url, function (err, res, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;

    chars.forEach((ch) => {
      req(ch, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
