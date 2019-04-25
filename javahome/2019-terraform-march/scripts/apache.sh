#!/bin/bash
yum install httpd -y
chkconfig httpd on
echo "This app is deployed by Terraform!!!!" > /var/www/html/index.html
service httpd start
