# Terraform Variable settting file
# File with name "*.auto.tfvars" will be used for Variable file: Webserver-Variables.tf

#WebServer-Variables.tf           <- List of Variables and Default values
#WebServer-Variables.auto.tfvars  <- Values of Variables for previous file

#----------Variables--------------------
aws_region         = "us-west-2"
myVPC_id           = "vpc-dfd21ba7"
myPublicSubnetA_id = "subnet-4b2b1e11"
myPublicSubnetB_id = "subnet-bfa6e2f4"  # subnet-bfa6e2f4, subnet-820f55fb, subnet-4b2b1e11
myInstanceSize     = "t3.nano"
tag_owner          = "ADV-IT"
