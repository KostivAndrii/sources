# Terraform Variable files
# File with name "*.tf" will be added automatically to Template


#----------Variables and DEFAULT Values--------------------

variable "aws_region" {
  default = "us-west-2"
}
variable "myVPC_id" {
  default = "vpc-dfd21ba7"
}
variable "myPublicSubnetA_id" {
  default = "subnet-4b2b1e11"
}
variable "myPublicSubnetB_id" {
  default = "subnet-820f55fb"
}
variable "myInstanceSize" {
  default = "t2.nano"
}
variable "tag_owner" {
  default = "Denis Astahov"
}
