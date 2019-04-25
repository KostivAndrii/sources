# Create NAT Instance
resource "aws_instance" "nat" {
  ami                         = "${lookup(var.nat_ami,var.region)}"
  instance_type               = "t2.micro"
  subnet_id                   = "${aws_subnet.webservers.*.id[0]}"
  source_dest_check           = false
  associate_public_ip_address = true
  vpc_security_group_ids      = ["${aws_security_group.nat_sg.id}"]
  key_name                    = "weekend"

  tags = {
    Name = "NatInstance"
  }
}

# Create Security Group for NAT instance
resource "aws_security_group" "nat_sg" {
  name        = "nat_sg"
  description = "Allow all inbound traffic"
  vpc_id      = "${aws_vpc.myvpc.id}"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
