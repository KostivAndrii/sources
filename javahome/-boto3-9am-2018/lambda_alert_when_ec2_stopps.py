import json
import boto3
sns_client = boto3.client('sns')
sns_arn = 'arn:aws:sns:ap-south-1:962103112291:dynamodb'
def lambda_handler(event, context):
    print(event)
    instance_id = event['detail']['instance-id']
    sns_client.publish(
        TopicArn=sns_arn,
        Message = f'Instance with {instance_id}, EC2 Instance stopped!!!!',
        Subject = 'Alert-EC2 Stopped !!!'
        )
