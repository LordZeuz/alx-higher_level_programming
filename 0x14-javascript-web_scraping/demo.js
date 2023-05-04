#!/usr/bin/node

const request = require('request');
//const eps = process.argv[2];
const url = 'https://www.youtube.com';
request(url, (error,response, body) => {
    console.log(`code: ${response.statusCode}`);
 //   const almost = JSON.parse(body);
    console.log(body);
});
