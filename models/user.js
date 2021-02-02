var db = require('../db.js');

exports.getAllUsers = function (done) {
    db.get().query('SELECT * FROM users', function (err, rows) {
        if (err) return done(err);
        done(null, rows);
    })
};

exports.getUser = function (userEmail, done) {
    db.get().query('SELECT * FROM users WHERE email = ?', userEmail, function (err, rows) {
        if (err) return done(err);
        done(null, rows);
    })
};

exports.updateUser = function (google_key, userID, done) {
    db.get().query('UPDATE users SET ? WHERE id = ?', [{google_2fa_key: google_key}, userID], function (err, rows) {
        if (err) return done(err);
        done(null, rows);
    })
};
