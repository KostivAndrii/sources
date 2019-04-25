# Get VPC ID, Public IP of all EC2 instances
import boto3
client = boto3.client('ec2','ap-south-1')
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation["Instances"]:
        vpc_id = instance['VpcId']
        print(f' VPC is is  {vpc_id}')
        # Check if key 'PublicIpAddress' exists in dict before accessing it
        if 'PublicIpAddress' in  instance:
            public_ip = instance['PublicIpAddress']
            print(f' Public IP is {public_ip}')
        else:
            print('Public Ip not foud')
