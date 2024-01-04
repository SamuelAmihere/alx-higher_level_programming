#!/usr/bin/node
const episode = process.argv[2];
const req = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';

req(URL + episode, (err, res, body) => {
	  if (err) {
		      console.log(err);
		    } else if (res.statusCode === 200) {
			        const JSONres = JSON.parse(body);
			        console.log(JSONres.title);
			      } else {
				          console.log('Error code: ' + res.statusCode);
				        }
});
