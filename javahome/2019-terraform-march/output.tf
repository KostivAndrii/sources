# This values is printed on console after terraform apply
output "azs" {
  value = "${data.aws_availability_zones.azs.names}"
}
