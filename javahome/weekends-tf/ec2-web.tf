resource "aws_instance" "web" {
  count                       = "${length(aws_subnet.webservers.*.id)}"
  ami                         = "${lookup(var.web_ami,var.region)}"
  instance_type               = "t2.micro"
  subnet_id                   = "${aws_subnet.webservers.*.id[count.index]}"
  associate_public_ip_address = true
  vpc_security_group_ids      = ["${aws_security_group.web_sg.id}"]
  key_name                    = "weekend"

  user_data = "${file("scripts/apache.sh")}"

  tags = {
    Name = "WebInstance-${count.index + 1}"
  }
}

# Create Security Group for Web instances
resource "aws_security_group" "web_sg" {
  name        = "web_sg"
  description = "Allow all inbound traffic"
  vpc_id      = "${aws_vpc.myvpc.id}"

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
    cidr_blocks = ["103.227.97.212/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
