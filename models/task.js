var db = require('../db.js')

exports.create = function(title, status, done) {
    var values = [title, status];

    db.get().query('INSERT INTO task (user_id, text, date) VALUES(?, ?, ?)', values, function(err, result) {
        if (err) return done(err);
        done(null, result.insertId)
    })
};

exports.getAll = function(done) {
    db.get().query('SELECT * FROM comments', function (err, rows) {
        if (err) return done(err);
        done(null, rows)
    })
};

exports.getAllByUser = function(userId, done) {
    db.get().query('SELECT * FROM comments WHERE user_id = ?', userId, function (err, rows) {
        if (err) return done(err);
        done(null, rows)
    })
};