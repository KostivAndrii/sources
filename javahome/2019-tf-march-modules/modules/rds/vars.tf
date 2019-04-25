variable "password" {}

variable "username" {
  default = "admin"
}

variable "instance_name" {
  default = "mydb"
}

variable "instance_class" {
  default = "db.t2.micro"
}

variable "engine_version" {
  default = "5.7"
}

variable "engine" {
  default = "mysql"
}

variable "db_storage" {
  default = "20"
}

variable "storage_type" {
  default = "gp2"
}

variable "parameter_group" {
  default = "default.mysql5.7"
}
