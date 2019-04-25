locals {
  elb_count = "${terraform.workspace == "prod" ? 1 : 0}"
  elb_name  = "javahome-elb-${terraform.workspace}"
}

output "elb_count" {
  value = "${local.elb_count}"
}

# Create a new load balancer
resource "aws_elb" "javahome_elb" {
  count           = "${local.elb_count}"
  name            = "${local.elb_name}"
  subnets         = ["${aws_subnet.webservers.*.id}"]
  security_groups = ["${aws_security_group.elb.id}"]

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }

  access_logs {
    bucket        = "${aws_s3_bucket.elb_logs.id}"
    bucket_prefix = "elb-logs"
    interval      = 5
  }

  # arn:aws:s3:::javahome-elb-acceslogs/elb-logs/AWSLogs/962103112291/*

  health_check {
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 3
    target              = "HTTP:80/index.html"
    interval            = 30
  }
  instances                   = ["${aws_instance.web_servers.*.id}"]
  cross_zone_load_balancing   = true
  idle_timeout                = 60
  connection_draining         = true
  connection_draining_timeout = 60
  tags = {
    Name = "javahome-terraform-elb"
  }
}

resource "aws_security_group" "elb" {
  name        = "elb_allow_tls"
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
