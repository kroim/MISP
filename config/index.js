var config = {
    local: {
        mode: 'mode_production',
        port: 7000,
        domain: 'https://127.0.0.1:7000',
    },
    server: {
        domain: 'https://dev.ecrimelabs.net'
    },

    mysql: {
        host: 'localhost',
        user: 'root',
        port: 3306,
        password: '',
        db_name:'misp'
    }
};

module.exports = function(mode) {
    return config;
};