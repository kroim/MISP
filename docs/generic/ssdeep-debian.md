#### Experimental ssdeep correlations
##### installing ssdeep
```
cd /usr/local/src
wget https://github.com/ssdeep-project/ssdeep/releases/download/release-2.14.1/ssdeep-2.14.1.tar.gz
tar zxvf ssdeep-2.14.1.tar.gz
cd ssdeep-2.14.1
./configure
make
sudo make install

#installing ssdeep_php
sudo pecl install ssdeep

# You should add "extension=ssdeep.so" to mods-available - Check /etc/php for your current version
echo "extension=ssdeep.so" | sudo tee ${PHP_ETC_BASE}/mods-available/ssdeep.ini
sudo phpenmod ssdeep
sudo service apache2 restart
```
