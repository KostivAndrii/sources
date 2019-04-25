provider "aws" {
  region = "${var.region}"
}

module "networking" {
  source            = "modules/networking"
  no_of_pub_subnets = 2

  vpc_tags = {
    Name = "hari_vpc_${terraform.workspace}"
    Env  = "${terraform.workspace}"
  }
}

module "web_instances" {
  source         = "modules/ec2"
  pub_subnet_ids = "${module.networking.pub_subnet_ids}"
}

module "rds" {
  source   = "modules/rds"
  password = "Admin1234"
}
