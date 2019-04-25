resource "aws_instance" "web" {
  count         = "${var.web_ec2_count}"
  ami           = "ami-0889b8a448de4fc44"
  instance_type = "t2.micro"
  subnet_id     = "${var.pub_subnet_ids[count.index]}"

  tags = {
    Name = "Web-${count.index + 1}"
  }
}
