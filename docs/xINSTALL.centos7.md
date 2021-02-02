# INSTALLATION INSTRUCTIONS
## for CentOS 7.x

### 0/ MISP CentOS 7 Minimal NetInstall - Status
--------------------------------------------

!!! notice
    Semi-maintained and tested by @SteveClement, CentOS 7.5-1804 on 20181113<br />
    It is still considered experimental as not everything works seemlessly.


CentOS 7.5-1804 [NetInstallURL](http://mirror.centos.org/centos/7.5.1804/os/x86_64/)

{!generic/globalVariables.md!}

```bash
# CentOS Specific
RUN_PHP='/usr/bin/scl enable rh-php71 '
RUN_PYTHON='/usr/bin/scl enable rh-python36 '

PHP_INI=/etc/opt/rh/rh-php71/php.ini
```

### 1/ Minimal CentOS install
-------------------------

Install a minimal CentOS 7.x system with the software:

- OpenSSH server
- LAMP server (actually, this is done below)
- Mail server


```bash
# Make sure you set your hostname CORRECTLY vs. like an brute (manually in /etc/hostname)
sudo hostnamectl set-hostname misp.local # or whatever you want it to be

# Make sure your system is up2date:
sudo yum update -y
```

### 2/ Dependencies *
----------------
Once the system is installed you can perform the following steps as root or with sudo.

```bash
# We need some packages from the Extra Packages for Enterprise Linux repository
sudo yum install epel-release -y

# Since MISP 2.4 PHP 5.5 is a minimal requirement, so we need a newer version than CentOS base provides
# Software Collections is a way do to this, see https://wiki.centos.org/AdditionalResources/Repositories/SCL
sudo yum install centos-release-scl -y

# Install vim (optional)
sudo yum install vim -y

# Install the dependencies:
sudo yum install gcc git httpd zip redis mariadb mariadb-server python-devel python-pip python-zmq libxslt-devel zlib-devel ssdeep-devel -y

# Install PHP 7.1 from SCL, see https://www.softwarecollections.org/en/scls/rhscl/rh-php71/
sudo yum install rh-php71 rh-php71-php-fpm rh-php71-php-devel rh-php71-php-mysqlnd rh-php71-php-mbstring rh-php71-php-xml rh-php71-php-bcmath rh-php71-php-opcache -y

# Install Python 3.6 from SCL, see
# https://www.softwarecollections.org/en/scls/rhscl/rh-python36/
sudo yum install rh-python36 -y

# rh-php71-php only provided mod_ssl mod_php for httpd24-httpd from SCL
# if we want to use httpd from CentOS base we can use rh-php71-php-fpm instead
sudo systemctl enable rh-php71-php-fpm.service
sudo systemctl start  rh-php71-php-fpm.service

sudo $RUN_PHP "pear channel-update pear.php.net"
sudo $RUN_PHP "pear install Crypt_GPG"    # we need version >1.3.0
```

!!! notice
    $RUN_PHP makes php available for you if using rh-php71. e.g: sudo $RUN_PHP "pear list | grep Crypt_GPG"

```bash
# GPG needs lots of entropy, haveged provides entropy
sudo yum install haveged -y
sudo systemctl enable haveged.service
sudo systemctl start  haveged.service


# Enable and start redis
sudo systemctl enable redis.service
sudo systemctl start  redis.service
```

### 3/ MISP code
------------
```bash
# Download MISP using git in the /var/www/ directory.
sudo mkdir $PATH_TO_MISP
sudo chown apache:apache $PATH_TO_MISP
cd /var/www
sudo -u apache git clone https://github.com/MISP/MISP.git
cd $PATH_TO_MISP
sudo -u apache git checkout tags/$(git describe --tags `git rev-list --tags --max-count=1`)
# if the last shortcut doesn't work, specify the latest version manually
# example: git checkout tags/v2.4.XY
# the message regarding a "detached HEAD state" is expected behaviour
# (you only have to create a new branch, if you want to change stuff and do a pull request for example)

# Fetch submodules
sudo -u apache git submodule update --init --recursive
# Make git ignore filesystem permission differences for submodules
sudo -u apache git submodule foreach --recursive git config core.filemode false

# Create a python3 virtualenv
sudo -u apache $RUN_PYTHON "virtualenv -p python3 $PATH_TO_MISP/venv"
sudo mkdir /usr/share/httpd/.cache
sudo chown apache:apache /usr/share/httpd/.cache
sudo -u apache $PATH_TO_MISP/venv/bin/pip install -U pip setuptools

# install Mitre's STIX and its dependencies by running the following commands:
sudo yum install python-importlib python-lxml python-dateutil python-six -y
cd /var/www/MISP/app/files/scripts
sudo -u apache git clone https://github.com/CybOXProject/python-cybox.git
sudo -u apache git clone https://github.com/STIXProject/python-stix.git
cd /var/www/MISP/app/files/scripts/python-cybox
# If you umask is has been changed from the default, it is a good idea to reset it to 0022 before installing python modules
UMASK=$(umask)
umask 0022
cd /var/www/MISP/app/files/scripts/python-stix
sudo -u apache $PATH_TO_MISP/venv/bin/pip install .

# install maec
sudo -u apache $PATH_TO_MISP/venv/bin/pip install -U maec

# install zmq
sudo -u apache $PATH_TO_MISP/venv/bin/pip install -U zmq

# install redis
sudo -u apache $PATH_TO_MISP/venv/bin/pip install -U redis

# install magic, lief, pydeep
sudo -u apache $PATH_TO_MISP/venv/bin/pip install -U python-magic lief git+https://github.com/kbandla/pydeep.git

# install mixbox to accommodate the new STIX dependencies:
cd /var/www/MISP/app/files/scripts/
sudo -u apache git clone https://github.com/CybOXProject/mixbox.git
cd /var/www/MISP/app/files/scripts/mixbox
sudo -u apache $PATH_TO_MISP/venv/bin/pip install .

# install PyMISP
cd /var/www/MISP/PyMISP
sudo -u apache $PATH_TO_MISP/venv/bin/pip install enum34
sudo -u apache $PATH_TO_MISP/venv/bin/pip install .

# Enable python3 for php-fpm
echo 'source scl_source enable rh-python36' | sudo tee -a /etc/opt/rh/rh-php71/sysconfig/php-fpm
sudo sed -i.org -e 's/^;\(clear_env = no\)/\1/' /etc/opt/rh/rh-php71/php-fpm.d/www.conf
sudo systemctl restart rh-php71-php-fpm.service

umask $UMASK
```

### 4/ CakePHP
-----------
#### CakePHP is now included as a submodule of MISP and has been fetch by a previous step.
#### Install CakeResque along with its dependencies if you intend to use the built in background jobs.
```bash
sudo chown -R apache:apache /var/www/MISP
sudo mkdir /usr/share/httpd/.composer
sudo chown apache:apache /usr/share/httpd/.composer
cd /var/www/MISP/app
sudo -u apache $RUN_PHP "php composer.phar require kamisama/cake-resque:4.1.2"
sudo -u apache $RUN_PHP "php composer.phar config vendor-dir Vendor"
sudo -u apache $RUN_PHP "php composer.phar install"

# CakeResque normally uses phpredis to connect to redis, but it has a (buggy) fallback connector through Redisent. It is highly advised to install phpredis using "yum install php-redis"
sudo $RUN_PHP "pecl install redis"
echo "extension=redis.so" |sudo tee /etc/opt/rh/rh-php71/php-fpm.d/redis.ini
sudo ln -s ../php-fpm.d/redis.ini /etc/opt/rh/rh-php71/php.d/99-redis.ini
sudo systemctl restart rh-php71-php-fpm.service

# If you have not yet set a timezone in php.ini
echo 'date.timezone = "Europe/Luxembourg"' |sudo tee /etc/opt/rh/rh-php71/php-fpm.d/timezone.ini
sudo ln -s ../php-fpm.d/timezone.ini /etc/opt/rh/rh-php71/php.d/99-timezone.ini

# Recommended: Change some PHP settings in /etc/opt/rh/rh-php71/php.ini
# max_execution_time = 300
# memory_limit = 512M
# upload_max_filesize = 50M
# post_max_size = 50M
for key in upload_max_filesize post_max_size max_execution_time max_input_time memory_limit
do
    sudo sed -i "s/^\($key\).*/\1 = $(eval echo \${$key})/" $PHP_INI
done
sudo systemctl restart rh-php71-php-fpm.service

# To use the scheduler worker for scheduled tasks, do the following:
sudo cp -fa /var/www/MISP/INSTALL/setup/config.php /var/www/MISP/app/Plugin/CakeResque/Config/config.php
```

### 5/ Set the permissions
----------------------
```bash
# Make sure the permissions are set correctly using the following commands as root:
sudo chown -R root:apache /var/www/MISP
sudo find /var/www/MISP -type d -exec chmod g=rx {} \;
sudo chmod -R g+r,o= /var/www/MISP
sudo chmod -R 750 /var/www/MISP
sudo chmod -R g+ws /var/www/MISP/app/tmp
sudo chmod -R g+ws /var/www/MISP/app/files
sudo chmod -R g+ws /var/www/MISP/app/files/scripts/tmp
sudo chown apache:apache /var/www/MISP/app/files
sudo chown apache:apache /var/www/MISP/app/files/terms
sudo chown apache:apache /var/www/MISP/app/files/scripts/tmp
sudo chown apache:apache /var/www/MISP/app/Plugin/CakeResque/tmp
sudo chown -R apache:apache /var/www/MISP/app/Config
sudo chown -R apache:apache /var/www/MISP/app/tmp
sudo chown -R apache:apache /var/www/MISP/app/webroot/img/orgs
sudo chown -R apache:apache /var/www/MISP/app/webroot/img/custom
```

### 6/ Create a database and user
-----------------------------
```bash
# Enable, start and secure your mysql database server
sudo systemctl enable mariadb.service
sudo systemctl start  mariadb.service

sudo yum install expect -y

# Add your credentials if needed, if sudo has NOPASS, comment out the relevant lines
#pw="Password1234"

expect -f - <<-EOF
  set timeout 10

  spawn sudo mysql_secure_installation
  #expect "*?assword*"
  #send -- "$pw\r"
  expect "Enter current password for root (enter for none):"
  send -- "\r"
  expect "Set root password?"
  send -- "y\r"
  expect "New password:"
  send -- "${DBPASSWORD_ADMIN}\r"
  expect "Re-enter new password:"
  send -- "${DBPASSWORD_ADMIN}\r"
  expect "Remove anonymous users?"
  send -- "y\r"
  expect "Disallow root login remotely?"
  send -- "y\r"
  expect "Remove test database and access to it?"
  send -- "y\r"
  expect "Reload privilege tables now?"
  send -- "y\r"
  expect eof
EOF

sudo yum remove tcl expect -y

# Additionally, it is probably a good idea to make the database server listen on localhost only
echo [mysqld] |sudo tee /etc/my.cnf.d/bind-address.cnf
echo bind-address=127.0.0.1 |sudo tee -a /etc/my.cnf.d/bind-address.cnf
sudo systemctl restart mariadb.service


# Enter the mysql shell
mysql -u root -p
```

```
MariaDB [(none)]> create database misp;
MariaDB [(none)]> grant usage on *.* to misp@localhost identified by 'XXXXXXXXX';
MariaDB [(none)]> grant all privileges on misp.* to misp@localhost ;
MariaDB [(none)]> exit
```

#### copy/paste:

```bash
sudo mysql -u $DBUSER_ADMIN -p$DBPASSWORD_ADMIN -e "create database $DBNAME;"
sudo mysql -u $DBUSER_ADMIN -p$DBPASSWORD_ADMIN -e "grant usage on *.* to $DBNAME@localhost identified by '$DBPASSWORD_MISP';"
sudo mysql -u $DBUSER_ADMIN -p$DBPASSWORD_ADMIN -e "grant all privileges on $DBNAME.* to '$DBUSER_MISP'@'localhost';"
sudo mysql -u $DBUSER_ADMIN -p$DBPASSWORD_ADMIN -e "flush privileges;"
```

#### Import the empty MySQL database from MYSQL.sql
```bash
sudo -u apache cat $PATH_TO_MISP/INSTALL/MYSQL.sql | mysql -u $DBUSER_MISP -p$DBPASSWORD_MISP $DBNAME
```


### 7/ Apache configuration
-----------------------

!!! notice
    SELinux note, to check if it is running:
    ```bash
    $ sestatus
    SELinux status:                 disabled
    ```
    If it is disabled, you can ignore the **chcon/setsebool/semanage/checkmodule/semodule*** commands.

!!! warning
    This guide only copies a stock **NON-SSL** configuration file.

```bash
# Now configure your apache server with the DocumentRoot /var/www/MISP/app/webroot/
# A sample vhost can be found in /var/www/MISP/INSTALL/apache.misp.centos7

sudo cp /var/www/MISP/INSTALL/apache.misp.centos7.ssl /etc/httpd/conf.d/misp.ssl.conf

# If a valid SSL certificate is not already created for the server, create a self-signed certificate:
sudo openssl req -newkey rsa:4096 -days 365 -nodes -x509 \
-subj "/C=${OPENSSL_C}/ST=${OPENSSL_ST}/L=${OPENSSL_L}/O=${OPENSSL_O}/OU=${OPENSSL_OU}/CN=${OPENSSL_CN}/emailAddress=${OPENSSL_EMAILADDRESS}" \
-keyout /etc/pki/tls/private/misp.local.key -out /etc/pki/tls/certs/misp.local.crt

# Since SELinux is enabled, we need to allow httpd to write to certain directories
sudo chcon -t usr_t /var/www/MISP/venv
sudo chcon -t httpd_sys_rw_content_t /var/www/MISP/app/files
sudo chcon -t httpd_sys_rw_content_t /var/www/MISP/app/files/terms
sudo chcon -t httpd_sys_rw_content_t /var/www/MISP/app/files/scripts/tmp
sudo chcon -t httpd_sys_rw_content_t /var/www/MISP/app/Plugin/CakeResque/tmp
sudo chcon -R -t usr_t /var/www/MISP/venv
sudo chcon -R -t httpd_sys_rw_content_t /var/www/MISP/app/tmp
sudo chcon -R -t httpd_sys_rw_content_t /var/www/MISP/app/tmp/logs
sudo chcon -R -t httpd_sys_rw_content_t /var/www/MISP/app/webroot/img/orgs
sudo chcon -R -t httpd_sys_rw_content_t /var/www/MISP/app/webroot/img/custom
```

!!! warning
    Revise all permissions so update in Web UI works.

```bash
sudo chcon -R -t httpd_sys_rw_content_t /var/www/MISP/app/tmp


# Allow httpd to connect to the redis server and php-fpm over tcp/ip
sudo setsebool -P httpd_can_network_connect on

# Enable and start the httpd service
sudo systemctl enable httpd.service
sudo systemctl start  httpd.service

# Open a hole in the iptables firewall
sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
sudo firewall-cmd --zone=public --add-port=443/tcp --permanent
sudo firewall-cmd --reload

# We seriously recommend using only HTTPS / SSL !
# Add SSL support by running: sudo yum install mod_ssl
# Check out the apache.misp.ssl file for an example
```

!!! warning
    To be fixed - Place holder


### 8/ Log rotation
---------------
```bash
# MISP saves the stdout and stderr of it's workers in /var/www/MISP/app/tmp/logs
# To rotate these logs install the supplied logrotate script:

sudo cp $PATH_TO_MISP/INSTALL/misp.logrotate /etc/logrotate.d/misp
sudo chmod 0640 /etc/logrotate.d/misp

# Now make logrotate work under SELinux as well
# Allow logrotate to modify the log files
sudo semanage fcontext -a -t httpd_log_t "/var/www/MISP/app/tmp/logs(/.*)?"
sudo chcon -R -t httpd_log_t /var/www/MISP/app/tmp/logs

# Allow logrotate to read /var/www
sudo checkmodule -M -m -o /tmp/misplogrotate.mod $PATH_TO_MISP/INSTALL/misplogrotate.te
sudo semodule_package -o /tmp/misplogrotate.pp -m /tmp/misplogrotate.mod
sudo semodule -i /tmp/misplogrotate.pp
```

### 9/ MISP configuration
---------------------
```bash
# There are 4 sample configuration files in $PATH_TO_MISP/app/Config that need to be copied
sudo -u apache cp -a $PATH_TO_MISP/app/Config/bootstrap.default.php $PATH_TO_MISP/app/Config/bootstrap.php
sudo -u apache cp -a $PATH_TO_MISP/app/Config/database.default.php $PATH_TO_MISP/app/Config/database.php
sudo -u apache cp -a $PATH_TO_MISP/app/Config/core.default.php $PATH_TO_MISP/app/Config/core.php
sudo -u apache cp -a $PATH_TO_MISP/app/Config/config.default.php $PATH_TO_MISP/app/Config/config.php

echo "<?php
class DATABASE_CONFIG {
        public \$default = array(
                'datasource' => 'Database/Mysql',
                //'datasource' => 'Database/Postgres',
                'persistent' => false,
                'host' => '$DBHOST',
                'login' => '$DBUSER_MISP',
                'port' => 3306, // MySQL & MariaDB
                //'port' => 5432, // PostgreSQL
                'password' => '$DBPASSWORD_MISP',
                'database' => '$DBNAME',
                'prefix' => '',
                'encoding' => 'utf8',
        );
}" | sudo -u apache tee $PATH_TO_MISP/app/Config/database.php

# Configure the fields in the newly created files:
# config.php   : baseurl (example: 'baseurl' => 'http://misp',) - don't use "localhost" it causes issues when browsing externally
# core.php   : Uncomment and set the timezone: `// date_default_timezone_set('UTC');`
# database.php : login, port, password, database
# DATABASE_CONFIG has to be filled
# With the default values provided in section 6, this would look like:
# class DATABASE_CONFIG {
#   public $default = array(
#       'datasource' => 'Database/Mysql',
#       'persistent' => false,
#       'host' => 'localhost',
#       'login' => 'misp', // grant usage on *.* to misp@localhost
#       'port' => 3306,
#       'password' => 'XXXXdbpasswordhereXXXXX', // identified by 'XXXXdbpasswordhereXXXXX';
#       'database' => 'misp', // create database misp;
#       'prefix' => '',
#       'encoding' => 'utf8',
#   );
#}

# Important! Change the salt key in /var/www/MISP/app/Config/config.php
# The admin user account will be generated on the first login, make sure that the salt is changed before you create that user
# If you forget to do this step, and you are still dealing with a fresh installation, just alter the salt,
# delete the user from mysql and log in again using the default admin credentials (admin@admin.test / admin)

# If you want to be able to change configuration parameters from the webinterface:
sudo chown apache:apache /var/www/MISP/app/Config/config.php
sudo chcon -t httpd_sys_rw_content_t /var/www/MISP/app/Config/config.php

# Generate a GPG encryption key.
cat >/tmp/gen-key-script <<EOF
    %echo Generating a default key
    Key-Type: default
    Key-Length: $GPG_KEY_LENGTH
    Subkey-Type: default
    Name-Real: $GPG_REAL_NAME
    Name-Comment: $GPG_COMMENT
    Name-Email: $GPG_EMAIL_ADDRESS
    Expire-Date: 0
    Passphrase: $GPG_PASSPHRASE
    # Do a commit here, so that we can later print "done"
    %commit
    %echo done
EOF

sudo gpg --homedir /var/www/MISP/.gnupg --batch --gen-key /tmp/gen-key-script
sudo rm -f /tmp/gen-key-script
sudo chown -R apache:apache /var/www/MISP/.gnupg

# And export the public key to the webroot
sudo gpg --homedir /var/www/MISP/.gnupg --export --armor $GPG_EMAIL_ADDRESS |sudo tee /var/www/MISP/app/webroot/gpg.asc
sudo chown apache:apache /var/www/MISP/app/webroot/gpg.asc

# Start the workers to enable background jobs
sudo chmod +x /var/www/MISP/app/Console/worker/start.sh
sudo -u apache $RUN_PHP /var/www/MISP/app/Console/worker/start.sh

if [ ! -e /etc/rc.local ]
then
    echo '#!/bin/sh -e' | sudo tee -a /etc/rc.local
    echo 'exit 0' | sudo tee -a /etc/rc.local
    sudo chmod u+x /etc/rc.local
fi

sudo sed -i -e '$i \su -s /bin/bash apache -c "scl enable rh-php71 /var/www/MISP/app/Console/worker/start.sh" > /tmp/worker_start_rc.local.log\n' /etc/rc.local
# Make sure it will execute
sudo chmod +x /etc/rc.local

echo "Admin (root) DB Password: $DBPASSWORD_ADMIN"
echo "User  (misp) DB Password: $DBPASSWORD_MISP"
```

```
# some misp-modules dependencies
sudo yum install -y openjpeg-devel

sudo chmod 2777 /usr/local/src
sudo chown root:users /usr/local/src
cd /usr/local/src/
git clone https://github.com/MISP/misp-modules.git
cd misp-modules
# pip install
sudo -u apache $PATH_TO_MISP/venv/bin/pip install -I -r REQUIREMENTS
sudo -u apache $PATH_TO_MISP/venv/bin/pip install .
sudo yum install rubygem-rouge rubygem-asciidoctor -y
##sudo gem install asciidoctor-pdf --pre

# install STIX2.0 library to support STIX 2.0 export:
sudo -u apache $PATH_TO_MISP/venv/bin/pip install stix2

# install additional dependencies for extended object generation and extraction
sudo -u apache ${PATH_TO_MISP}/venv/bin/pip install maec lief python-magic pathlib
sudo -u apache ${PATH_TO_MISP}/venv/bin/pip install git+https://github.com/kbandla/pydeep.git

# Start misp-modules
sudo -u apache ${PATH_TO_MISP}/venv/bin/misp-modules -l 0.0.0.0 -s &

sudo sed -i -e '$i \sudo -u apache /var/www/MISP/venv/bin/misp-modules -l 127.0.0.1 -s &\n' /etc/rc.local
```

{!generic/MISP_CAKE_init_centos.md!}

{!generic/INSTALL.done.md!}

{!generic/recommended.actions.md!}

{!generic/hardening.md!}
