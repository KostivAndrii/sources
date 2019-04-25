output "pub_subnet_ids" {
  value = "${aws_subnet.public_subnets.*.id}"
}
