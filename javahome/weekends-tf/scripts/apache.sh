#!/bin/bash
yum install httpd -y
chkconfig httpd on
echo "Welcomet to JavaHome - Terraform" > /var/www/html/index.html
service httpd start
