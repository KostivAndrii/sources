provider "aws" {
  region = "ap-south-1"
}

# SNS Topic

resource "aws_sns_topic" "app_alets" {
  name = "javahome-app"
}

# EC2 instance

resource "aws_instance" "web" {
  ami           = "ami-0ad42f4f66f6c1cc9"
  instance_type = "t2.micro"

  tags = {
    Name = "javahome-app"
  }
}
