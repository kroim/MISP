var request = require('request');
var cheerio = require('cheerio');
var useragent = require('express-useragent');
var speakeasy = require('speakeasy');
var crypto = require('crypto');
var bcrypt = require('bcrypt');
var config = require('../config/index')();
var View = require('../views/base');

var userModel = require('../models/user');

module.exports = {
    name: "HomeController",
    home: async function (req, res, next) {
        return res.redirect('/misp/login');
    },

    tlogin: function(req, res, next){
        return res.render('test');
    },

    login: async function (req, res, next) {

        console.log(req.headers.cookie);


        await userModel.getAllUsers(function (err, rows) {
            if (err) return res.send(err.message);
            rows.forEach(async function (row) {
                if (row['external_auth_required'] == 1 && (row['google_2fa_key'] == null || row['google_2fa_key'] == '')) {
                    var google_key = speakeasy.generateSecret({length: 21}).base32;
                    console.log(row['id']);
                    console.log(google_key);
                    await userModel.updateUser(google_key, row['id'], function (err, rows) {
                        if (err) console.log(err);
                        else console.log('success');
                    })
                }
            })
        });
        var login_page_url = config.server.domain + '/users/login';
        process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 0;

        request.get({url: login_page_url, headers: {Cookie: req.headers.cookie}}, function (err, response, html){
            console.log(response.body);
        });


        request(login_page_url, function(error, response, html){
            if(!error){
                var $ = cheerio.load(html);
                var page_content = $('#UserLoginForm').html();
                var v1 = new View(res, 'home');
                v1.render({
                    config: config,
                    page_content: page_content
                });
            } else if (error) {
                var v2 = new View(res, 'error');
                v2.render({

                });
            }
        });
    },
    login_post: async function (req, res, next) {
        var email = req.body.email;
        var password = req.body.password;
        var code = req.body.code;
        await userModel.getUser(email, function (err, users) {
            if (err) return res.send({status: 'error', message: 'Not found a user'});
            if (users.length == 0) return res.send({status: 'error', message: 'Not found a user'});
            else {
                var user = users[0];
                if (!bcrypt.compareSync(password, user['password']))
                    return res.send({status: 'error', message: 'Password is incorrect.'});
                var tokenVerified = speakeasy.totp.verify({
                    secret: user['google_2fa_key'],
                    encoding: 'base32',
                    token: code
                });
                if (!tokenVerified) return res.send({status: 'error', message: 'Google Authenticated Token is incorrect'});
                return res.send({status: 'success', message: 'Found a user in success.'});
            }
        });
    },
};
