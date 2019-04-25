import boto3
client = boto3.client('ec2')
client.start_instances(InstanceIds=['i-086c8df1545018ab0'])