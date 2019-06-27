#!/bin/bash
yum -y update
yum -y install httpd
myip=`curl http://169.254.169.254/latest/meta-data/local-ipv4`
echo "<html><body bgcolor=black><center><h2><p><font color=yellow>This page from WebServer with IP: $myip</h2><br>Build by Terraform!<br</center></body></html>"  >  /var/www/html/index.html
sudo service httpd start
chkconfig httpd on
