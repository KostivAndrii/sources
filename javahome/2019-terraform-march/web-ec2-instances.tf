locals {
  web_sub_ids = "${aws_subnet.webservers.*.id}"
  azs         = "${data.aws_availability_zones.azs.names}"
}

resource "aws_instance" "web_servers" {
  count = "${var.web_servers_count}"

  # ami                         = "${lookup(var.ec2_ami,var.region)}"
  ami                         = "${var.ec2_ami[var.region]}"
  instance_type               = "${var.instance_type}"
  subnet_id                   = "${local.web_sub_ids[count.index]}"
  associate_public_ip_address = "true"
  vpc_security_group_ids      = ["${aws_security_group.web_sg.id}"]
  iam_instance_profile        = "${aws_iam_instance_profile.ec2_s3_profile_new.name}"
  user_data                   = "${file("scripts/apache.sh")}"

  tags {
    Name = "Web-${count.index + 1}"
  }
}

resource "aws_security_group" "web_sg" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = "${aws_vpc.my_vpc.id}"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
