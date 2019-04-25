variable "vpc_cidr" {
  default = "173.16.0.0/16"
}

variable "vpc_tags" {
  default = {
    Name = "app_vpc"
  }
}

variable "no_of_pub_subnets" {
  default = "2"
}

variable "pub_cidrs" {
  default = ["173.16.0.0/24", "173.16.1.0/24"]
}

variable "public_ip" {
  default = true
}
