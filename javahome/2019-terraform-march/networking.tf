# Create VPC using Terraform

resource "aws_vpc" "my_vpc" {
  cidr_block = "${var.vpc_cidr}"

  tags = "${var.vpc_tags}"
}

# Create coule of usbnets under my_vpc

resource "aws_subnet" "webservers" {
  count             = "${var.web_sub_count}"
  vpc_id            = "${aws_vpc.my_vpc.id}"
  cidr_block        = "${var.web_cidrs[count.index]}"
  availability_zone = "${local.azs[count.index]}"

  tags {
    Name = "Web-${count.index + 1}"
  }
}

# Internet Gateway for Web server_address

resource "aws_internet_gateway" "igw" {
  vpc_id = "${aws_vpc.my_vpc.id}"

  tags = {
    Name = "JavaHomeIGW"
  }
}

# Create Route Table for Webservers

resource "aws_route_table" "web" {
  vpc_id = "${aws_vpc.my_vpc.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.igw.id}"
  }

  tags = {
    Name = "WebRouteTable"
  }
}

resource "aws_route_table_association" "web" {
  count          = "${var.web_sub_count}"
  subnet_id      = "${local.web_sub_ids[count.index]}"
  route_table_id = "${aws_route_table.web.id}"
}
