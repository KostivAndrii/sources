{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1552442037224",
      "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::javahomebucket/${app_env}/*"
    }
  ]
}
