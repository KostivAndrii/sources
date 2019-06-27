##-------------My Not First Terraform template-----------
# Using Terraform Modules
#
# Made by Denis Astahov  on  05-February-2019
#---------------------------------------------------

provider "aws" {
  region     = "us-east-1"
}

module "web_server_sg" {
  source = "terraform-aws-modules/security-group/aws//modules/http-80"

  name        = "web-server"
  description = "Security group for web-server with HTTP ports open within VPC"
  vpc_id      = "vpc-de69b3a4"
  ingress_cidr_blocks = ["0.0.0.0/0"]
}


module "vote_service_sg" {
  source = "terraform-aws-modules/security-group/aws"

  name        = "user-service"
  description = "Security group for user-service with custom ports open within VPC, and PostgreSQL publicly open"
  vpc_id      = "vpc-de69b3a4"

  ingress_cidr_blocks      = ["10.10.0.0/16"]
  ingress_rules            = ["https-443-tcp"]
  ingress_with_cidr_blocks = [
    {
      from_port   = 8080
      to_port     = 8090
      protocol    = "tcp"
      description = "User-service ports"
      cidr_blocks = "10.10.0.0/16"
    },
    {
      rule        = "postgresql-tcp"
      cidr_blocks = "0.0.0.0/0"
    },
  ]
}

/*
module "consul" {
  source = "hashicorp/consul/aws"
  version = "0.3.3"

  aws_region  = "us-east-1" # should match provider region
  num_servers = "3"
}
*/
