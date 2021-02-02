#### MISP Dashboard
--------------
```bash
cd /var/www
sudo mkdir misp-dashboard
sudo chown www-data:www-data misp-dashboard
sudo -u www-data git clone https://github.com/MISP/misp-dashboard.git
cd misp-dashboard
sudo -H /var/www/misp-dashboard/install_dependencies.sh
sudo sed -i "s/^host\ =\ localhost/host\ =\ 0.0.0.0/g" /var/www/misp-dashboard/config/config.cfg
sudo sed -i -e '$i \sudo -u www-data bash /var/www/misp-dashboard/start_all.sh\n' /etc/rc.local
sudo sed -i '/Listen 80/a Listen 0.0.0.0:8001' /etc/apache2/ports.conf
sudo apt install libapache2-mod-wsgi-py3 -y

echo "<VirtualHost *:8001>
    ServerAdmin admin@misp.local
    ServerName misp.local
    DocumentRoot /var/www/misp-dashboard
    
    WSGIDaemonProcess misp-dashboard \
       user=misp group=misp \
       python-home=/var/www/misp-dashboard/DASHENV \
       processes=1 \
       threads=15 \
       maximum-requests=5000 \
       listen-backlog=100 \
       queue-timeout=45 \
       socket-timeout=60 \
       connect-timeout=15 \
       request-timeout=60 \
       inactivity-timeout=0 \
       deadlock-timeout=60 \
       graceful-timeout=15 \
       eviction-timeout=0 \
       shutdown-timeout=5 \
       send-buffer-size=0 \
       receive-buffer-size=0 \
       header-buffer-size=0 \
       response-buffer-size=0 \
       server-metrics=Off
    WSGIScriptAlias / /var/www/misp-dashboard/misp-dashboard.wsgi
    <Directory /var/www/misp-dashboard>
        WSGIProcessGroup misp-dashboard
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
    LogLevel info
    ErrorLog /var/log/apache2/misp-dashboard.local_error.log
    CustomLog /var/log/apache2/misp-dashboard.local_access.log combined
    ServerSignature Off
</VirtualHost>" | sudo tee /etc/apache2/sites-available/misp-dashboard.conf

sudo a2ensite misp-dashboard
sudo systemctl reload apache2

# Add misp-dashboard to rc.local to start on boot.
sudo sed -i -e '$i \sudo -u www-data bash /var/www/misp-dashboard/start_all.sh > /tmp/misp-dashboard_rc.local.log\n' /etc/rc.local

# Enable ZeroMQ for misp-dashboard
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_event_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_object_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_object_reference_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_attribute_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_sighting_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_user_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_organisation_notifications_enable" true
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_port" 50000
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_redis_host" "localhost"
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_redis_port" 6379
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_redis_database" 1
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_redis_namespace" "mispq"
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_include_attachments" false
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_tag_notifications_enable" false
sudo $CAKE Admin setSetting "Plugin.ZeroMQ_audit_notifications_enable" false
```
