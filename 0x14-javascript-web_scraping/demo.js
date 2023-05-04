#!/usr/bin/node

const request = require('request');
const eps = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + eps, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const obj = JSON.parse(body);
  console.log(obj.title);
});
