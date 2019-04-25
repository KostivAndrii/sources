import boto3
client = boto3.client('sns')
def ec2_notifications(event, context):
    instance_id = event['detail']['instance-id']
    # print('Java Home')
    client.publish(
        TopicArn='arn:aws:sns:ap-south-1:172794197511:javahome-app',
        Message= f'EC2 Instance with id {instance_id} is stopping',
        Subject='javahome-ec2-alerts'
    )
