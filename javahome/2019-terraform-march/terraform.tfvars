region = "ap-south-1"

vpc_cidr = "173.20.0.0/16"

vpc_tags = {
  Name        = "JavaHomeVPC"
  Location    = "Pune"
  Environment = "Production"
}

subnet_cidrs = ["173.20.0.0/24", "173.20.1.0/24"]
