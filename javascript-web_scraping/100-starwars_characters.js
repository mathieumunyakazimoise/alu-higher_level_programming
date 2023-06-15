#!/usr/bin/node

const request = require('request');
const path = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(path, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body);
    for (const item of result.characters) {
      request(item, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
