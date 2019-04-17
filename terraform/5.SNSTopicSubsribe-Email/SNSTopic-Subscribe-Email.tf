# --------------------------------------------------------------------------------------------------
# Terraform example of AWS SNS Topic Subscribe email address which is not supported yet by Terarform
#
# Author: Denis Astahov
#
# Version      Date                 Name                Info
# 1.0          07-February-2019    Denis Astahov       Initial Version
#
# --------------------------------------------------------------------------------------------------

provider "aws" {
  region = "us-west-2"
}


variable "SNSTopicName" {
  default     = "SupportLevel1"
}

variable "SNSTopicEmail" {
  default     = "support@example.com"
}


resource "aws_sns_topic" "mySNSTopic" {
  name         = "${var.SNSTopicName}"
}

resource "aws_cloudformation_stack" "SubscribeEmailforxxx" {
   name          = "subsribe-email-to-${aws_sns_topic.mySNSTopic.name}"
   template_body = <<STACK
AWSTemplateFormatVersion: '2010-09-09'
Description: Subscribe email to SNS Topic ${aws_sns_topic.mySNSTopic.name}
Resources:
 EmailSubscription:
  Type: "AWS::SNS::Subscription"
  Properties:
     Protocol: email
     Endpoint: ${var.SNSTopicEmail}
     TopicArn: ${aws_sns_topic.mySNSTopic.arn}
STACK
}
