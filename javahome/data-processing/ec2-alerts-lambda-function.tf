# Create Zip for lambda function

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "lambda-python/ec2-alerts.py"
  output_path = "lambda-python/ec2-alerts.zip"
}

resource "aws_lambda_function" "ec2_alerts" {
  filename = "lambda-python/ec2-alerts.zip"

  # source_code_hash = "${base64sha256("lambda-python/ec2-alerts.py")}"
  source_code_hash = "${data.archive_file.lambda_zip.output_base64sha256}"
  function_name    = "ec2InstanceAlerts"
  role             = "${aws_iam_role.ec2_alerts_lambda.arn}"
  handler          = "ec2-alerts.ec2_notifications"
  runtime          = "python3.7"
}
