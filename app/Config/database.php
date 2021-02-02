<?php
class DATABASE_CONFIG {
        public $default = array(
                'datasource' => 'Database/Mysql',
                //'datasource' => 'Database/Postgres',
                'persistent' => false,
                'host' => 'localhost',
                'login' => 'misp',
                'port' => 3306, // MySQL & MariaDB
                //'port' => 5432, // PostgreSQL
                'password' => '0782f132aaf9f2d003fc08e514e78c9df75d7f163778f0ca81d5d00f9be19cd6',
                'database' => 'misp',
                'prefix' => '',
                'encoding' => 'utf8',
        );
}
