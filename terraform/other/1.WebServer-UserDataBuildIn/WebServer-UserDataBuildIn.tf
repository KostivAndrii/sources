#-------------My First Terraform template-----------
#
# Made by Denis Astahov  on  01-February.2019
#---------------------------------------------------
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "Myinstance1" {
  ami           = "ami-01e24be29428c15b2"
  instance_type = "t2.micro"
  key_name      = "dastahov-oregon"
  user_data     = <<EOF
#!/bin/bash
yum -y update
yum -y install httpd
myip=`curl http://169.254.169.254/latest/meta-data/local-ipv4`
echo "<html><body bgcolor=black><center><h2><p><font color=yellow>This page from WebServer with IP: $myip</h2><br>Build by Terraform!<br</center></body></html>"  >  /var/www/html/index.html
sudo service httpd start
chkconfig httpd on
EOF
  vpc_security_group_ids = ["${aws_security_group.MySecurityGroup1.id}"]
  tags {
    Name = "Terraform-Server"
    Owner = "Denis Astahov"
  }
}

resource "aws_security_group" "MySecurityGroup1" {
  name = "WebServer-UserDataBuildin"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
  from_port       = 0
  to_port         = 0
  protocol        = "-1"
  cidr_blocks     = ["0.0.0.0/0"]
  }


  tags ={
    Name = "SG-for-Terraform"
  }
}
#===============================
output "public_ip" {
  value = "${aws_instance.Myinstance1.public_ip}"
}
