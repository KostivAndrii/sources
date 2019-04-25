resource "aws_db_instance" "rds" {
  allocated_storage    = "${var.db_storage}"
  storage_type         = "${var.storage_type}"
  engine               = "${var.engine}"
  engine_version       = "${var.engine_version}"
  instance_class       = "${var.instance_class}"
  name                 = "${var.instance_name}"
  username             = "${var.username}"
  password             = "${var.password}"
  parameter_group_name = "${var.parameter_group}"
}
