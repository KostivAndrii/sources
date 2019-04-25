resource "aws_iam_role" "ec2_alerts_lambda" {
  name               = "ec2-alertslambda-assume-role"
  assume_role_policy = "${file("iam/ec2-alertslambda-assume-role.json")}"
}

# Create Policy

resource "aws_iam_policy" "ec2_alerts_lambda" {
  name   = "ec2_alerts_lambda"
  path   = "/"
  policy = "${file("iam/ec2-alertslambda-policy.json")}"
}

# Attach policy to role

resource "aws_iam_policy_attachment" "ec2-alerts-attach" {
  name       = "ec2-alerts-attach"
  roles      = ["${aws_iam_role.ec2_alerts_lambda.name}"]
  policy_arn = "${aws_iam_policy.ec2_alerts_lambda.arn}"
}
