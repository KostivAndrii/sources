provider "aws" {
  region = "${var.region}"
}

terraform {
  backend "s3" {
    bucket         = "javahome-elb-acceslogs"
    key            = "dev/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "s3-lock"
  }
}
