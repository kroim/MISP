<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInitedc96aef29366d061f2c8407a3db5da1
{
    public static $prefixLengthsPsr4 = array (
        'P' => 
        array (
            'Psr\\Log\\' => 8,
        ),
        'M' => 
        array (
            'Monolog\\' => 8,
        ),
        'C' => 
        array (
            'Composer\\Installers\\' => 20,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Psr\\Log\\' => 
        array (
            0 => __DIR__ . '/..' . '/psr/log/Psr/Log',
        ),
        'Monolog\\' => 
        array (
            0 => __DIR__ . '/..' . '/monolog/monolog/src/Monolog',
        ),
        'Composer\\Installers\\' => 
        array (
            0 => __DIR__ . '/..' . '/composer/installers/src/Composer/Installers',
        ),
    );

    public static $prefixesPsr0 = array (
        'R' => 
        array (
            'ResqueStatus' => 
            array (
                0 => __DIR__ . '/..' . '/kamisama/resque-status/src',
            ),
            'ResqueScheduler' => 
            array (
                0 => __DIR__ . '/..' . '/kamisama/php-resque-ex-scheduler/lib',
            ),
            'Resque' => 
            array (
                0 => __DIR__ . '/..' . '/kamisama/php-resque-ex/lib',
            ),
        ),
        'P' => 
        array (
            'PEAR' => 
            array (
                0 => __DIR__ . '/..' . '/pear/pear_exception',
            ),
        ),
        'N' => 
        array (
            'Net' => 
            array (
                0 => __DIR__ . '/..' . '/pear/net_geoip',
            ),
        ),
        'M' => 
        array (
            'MonologInit' => 
            array (
                0 => __DIR__ . '/..' . '/kamisama/monolog-init/src',
            ),
        ),
        'C' => 
        array (
            'Crypt' => 
            array (
                0 => __DIR__ . '/..' . '/pear/crypt_gpg',
            ),
            'Console' => 
            array (
                0 => __DIR__ . '/..' . '/pear/console_commandline',
            ),
        ),
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInitedc96aef29366d061f2c8407a3db5da1::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInitedc96aef29366d061f2c8407a3db5da1::$prefixDirsPsr4;
            $loader->prefixesPsr0 = ComposerStaticInitedc96aef29366d061f2c8407a3db5da1::$prefixesPsr0;

        }, null, ClassLoader::class);
    }
}
