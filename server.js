var fs = require('fs');
var path = require('path');
var request = require('request');
var cheerio = require('cheerio');
var useragent = require('express-useragent');
var http = require('http');
var https = require('https');
var bodyParser = require('body-parser');
var methodOverride = require('method-override');
var privateKey  = fs.readFileSync('sslcert/server.key', 'utf8');
var certificate = fs.readFileSync('sslcert/server.crt', 'utf8');
var credentials = {key: privateKey, cert: certificate};

var express = require('express');
var app = express();
var route = require('./route');
var db = require('./db');
var config = require('./config/index')();
var session = require('express-session');

app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(bodyParser.json({limit: '50mb', extended: true}));
app.use(bodyParser.json({ type: 'application/vnd.api+json' }));
app.use(methodOverride('X-HTTP-Method-Override'));
app.use(session({
    secret:"1234567890",
    resave: false,
    saveUninitialized: false
}));
app.use(useragent.express());
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,Content-type,Accept');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});
app.use('/', route);

var httpsServer = https.createServer(credentials, app);


db.connect(config.local.mode, function (err) {
    if (err) {
        console.log('Unable to connect to MySQL.');
        process.exit(1)
    } else {
        console.log(config.local.domain);
        httpsServer.listen(config.local.port);
    }
});