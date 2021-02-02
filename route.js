var express = require('express');
var router = express.Router();
var config = require('./config/index')();

var homeContoller = require('./controllers/HomeController');
router.get('/', function(req, res, next){
    homeContoller.home(req, res, next);
});
router.get('/misp/login', function (req, res, next) {
    homeContoller.login(req, res, next)
});
router.get('/users/login', function (req, res, next) {
    homeContoller.tlogin(req, res, next)
});
router.post('/misp/login-post', function (req, res, next) {
    homeContoller.login_post(req, res, next);
});


module.exports = router;
