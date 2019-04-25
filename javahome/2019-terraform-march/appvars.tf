variable "region" {
  description = "Enter region where you want your resources"
  default     = "ap-south-1"
}

variable "app_env" {
  default = "dev"
}

variable "elb_access_logs" {
  default = "javahome-elb-acceslogs"
}

variable "vpc_cidr" {
  description = "Enter VPC cidr"
  default     = "173.20.0.0/16"
}

variable "vpc_tags" {
  type = "map"

  default = {
    Name        = "JavaHomeVPC"
    Location    = "Banglore"
    Environment = "Development"
  }
}

variable "web_cidrs" {
  type    = "list"
  default = ["173.20.0.0/24", "173.20.1.0/24"]
}

variable "web_sub_count" {
  default = 2
}

variable "instance_type" {
  default = "t2.micro"
}

variable "web_servers_count" {
  default = "2"
}

variable "ec2_ami" {
  type = "map"

  default = {
    ap-south-1 = "ami-0ad42f4f66f6c1cc9"
    us-east-1  = "ami-0080e4c5bc078760e"
  }
}
