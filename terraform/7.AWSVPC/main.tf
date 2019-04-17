provider "aws" {
  region = "eu-west-2"
}

data "aws_region" "current" {}
data "aws_availability_zones" "available_az" {}


#=======================================
output "list_aws_region" {
  value = "${data.aws_region.current.name}"
}



output "list_aws_availability_zones" {
  value = "${data.aws_availability_zones.available_az.names}"
}
