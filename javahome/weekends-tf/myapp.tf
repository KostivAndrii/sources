provider "aws" {
  region = "${var.region}"
}

terraform {
  backend "s3" {
    bucket = "javahome-weekends-tf"
    key    = "myapp/dev/terraform.tfstate"
    region = "ap-south-1"
  }
}

resource "aws_vpc" "myvpc" {
  cidr_block       = "${var.vpc_cidr}"
  instance_tenancy = "default"
  tags             = "${var.vpc_tags}"
}

# Get AZs dynamically for current region
data "aws_availability_zones" "azs" {}

# Create one public subnet in each zone

resource "aws_subnet" "webservers" {
  count             = "${length(data.aws_availability_zones.azs.names)}"
  vpc_id            = "${aws_vpc.myvpc.id}"
  cidr_block        = "${var.web_cidrs[count.index]}"
  availability_zone = "${data.aws_availability_zones.azs.names[count.index]}"

  tags = {
    Name = "PublicSubnet-${count.index + 1}"
  }
}

# Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = "${aws_vpc.myvpc.id}"

  tags = {
    Name = "MyAppIgw"
  }
}

# Create Route Table for Public Subnet

resource "aws_route_table" "pub_rt" {
  vpc_id = "${aws_vpc.myvpc.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.gw.id}"
  }

  tags = {
    Name = "PublicRT"
  }
}

# Associate With public subnets
resource "aws_route_table_association" "a" {
  count          = "${length(aws_subnet.webservers.*.id)}"
  subnet_id      = "${aws_subnet.webservers.*.id[count.index]}"
  route_table_id = "${aws_route_table.pub_rt.id}"
}

# Add private Subnets

resource "aws_subnet" "private" {
  count             = "${length(data.aws_availability_zones.azs.names)}"
  vpc_id            = "${aws_vpc.myvpc.id}"
  cidr_block        = "${var.private_cidrs[count.index]}"
  availability_zone = "${data.aws_availability_zones.azs.names[count.index]}"

  tags = {
    Name = "PrivateSubnet-${count.index + 1}"
  }
}

# Create route table for private subnets
resource "aws_route_table" "pri_rt" {
  vpc_id = "${aws_vpc.myvpc.id}"

  route {
    cidr_block  = "0.0.0.0/0"
    instance_id = "${aws_instance.nat.id}"
  }

  tags = {
    Name = "PrivateRT"
  }
}

# Associate With private subnets
resource "aws_route_table_association" "b" {
  count          = "${length(aws_subnet.private.*.id)}"
  subnet_id      = "${aws_subnet.private.*.id[count.index]}"
  route_table_id = "${aws_route_table.pri_rt.id}"
}
