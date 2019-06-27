provider "aws" {
  region = "${var.aws_region}"
}

#-------------Set Remote State in S3 Bucket
terraform {
  required_version = ">= 0.11.0"
    backend "s3" {
      bucket = "adv.terraform.remote.state"
      key    = "asg-elb.tfstate"
      region = "us-west-2"      # Cannot use Variables, only HARDCODE!
      encrypt= true
  }
}
