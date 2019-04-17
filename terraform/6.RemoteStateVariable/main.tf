provider "aws" {
  region = "eu-west-2"
}


variable "Env" {
  description = "Environemnt Name: prod,test,staging"
}

terraform {
    backend "s3" {
        bucket = "adv.state-tf"
        region = "eu-west-1"
    }
}


resource "aws_vpc" "vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags ={
      Name = "${var.Env}"

    }

}
