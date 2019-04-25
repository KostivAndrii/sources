locals {
  azs         = "${data.aws_availability_zones.azs.names}"
  pub_sub_ids = "${aws_subnet.public_subnets.*.id}"
}

resource "aws_vpc" "app_vpc" {
  cidr_block = "${var.vpc_cidr}"

  tags = "${var.vpc_tags}"
}

resource "aws_subnet" "public_subnets" {
  count                   = "${var.no_of_pub_subnets}"
  vpc_id                  = "${aws_vpc.app_vpc.id}"
  cidr_block              = "${var.pub_cidrs[count.index]}"
  availability_zone       = "${local.azs[count.index]}"
  map_public_ip_on_launch = "${var.public_ip}"
}

resource "aws_internet_gateway" "igw" {
  count  = "${var.no_of_pub_subnets==0 ? 0 : 1}"
  vpc_id = "${aws_vpc.app_vpc.id}"
}

resource "aws_route_table" "pub_rt" {
  count  = "${var.no_of_pub_subnets==0 ? 0 : 1}"
  vpc_id = "${aws_vpc.app_vpc.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.igw.id}"
  }
}

resource "aws_route_table_association" "a" {
  count          = "${length(var.no_of_pub_subnets)}"
  subnet_id      = "${local.pub_sub_ids[count.index]}"
  route_table_id = "${aws_route_table.pub_rt.id}"
}
