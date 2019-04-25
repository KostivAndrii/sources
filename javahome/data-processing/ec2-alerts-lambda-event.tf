resource "aws_cloudwatch_event_rule" "ec2_state_change" {
  name        = "ec2AlertsTf"
  description = "Capture each AWS Console Sign In"

  event_pattern = "${file("cw-events-pattern/ec2_alerts.json")}"
}

resource "aws_cloudwatch_event_target" "lambda" {
  rule      = "${aws_cloudwatch_event_rule.ec2_state_change.name}"
  target_id = "SendToSNS"
  arn       = "${aws_lambda_function.ec2_alerts.arn}"
}
