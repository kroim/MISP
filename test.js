var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var http = require('http');
var https = require('https');
var privateKey  = fs.readFileSync('sslcert/server.key', 'utf8');
var certificate = fs.readFileSync('sslcert/server.crt', 'utf8');

var credentials = {key: privateKey, cert: certificate};
var express = require('express');
var app = express();

app.get('/scrape', function(req, res){
    // The URL we will scrape from - in our example Anchorman 2.

    url = 'https://dev.ecrimelabs.net/users/login';

    // The structure of our request call
    // The first parameter is our URL
    // The callback function takes 3 parameters, an error, response status code and the html

    process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;
    request(url, function(error, response, html){

        // First we'll check to make sure no errors occurred when making the request

        if(!error){
            // Next, we'll utilize the cheerio library on the returned html which will essentially give us jQuery functionality
            console.log("get pages");
            var $ = cheerio.load(html);

            // Finally, we'll define the variables we're going to capture
            console.log(html);
        } else if (error) {
            console.log(error);
        }
    })

})
var httpServer = http.createServer(app);
var httpsServer = https.createServer(credentials, app);

httpServer.listen(8080);
httpsServer.listen(8443);

console.log('Magic happens on port 8080');

exports = module.exports = app;