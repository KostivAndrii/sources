resource "aws_s3_bucket" "elb_logs" {
  bucket = "${var.elb_access_logs}"
  acl    = "private"
  policy = "${file("iam/elb-s3-accesslogs-policy.json")}"

  tags = {
    Name        = "javahome bucket"
    Environment = "Dev"
  }
}
