resource "aws_iam_role" "ec2_s3" {
  name = "ec2_s3_7am_2019"

  assume_role_policy = "${file("iam/assume-role-for-ec2-with-s3.json")}"
}

data "template_file" "ec2_iam_policy_s3" {
  template = "${file("iam/role-for-ec2-with-s3.tpl")}"

  vars = {
    app_env = "${var.app_env}"
  }
}

resource "aws_iam_policy" "policy_for_ec2" {
  name        = "policy_for_ec2"
  path        = "/"
  description = "policy for ec2"

  policy = "${data.template_file.ec2_iam_policy_s3.rendered}"
}

resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = "${aws_iam_role.ec2_s3.name}"
  policy_arn = "${aws_iam_policy.policy_for_ec2.arn}"
}

resource "aws_iam_instance_profile" "ec2_s3_profile_new" {
  name = "ec2_s3_profile"
  role = "${aws_iam_role.ec2_s3.name}"
}
