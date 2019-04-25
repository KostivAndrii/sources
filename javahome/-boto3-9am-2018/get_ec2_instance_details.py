import boto3
client = boto3.client('ec2')
resp = client.describe_instances(InstanceIds=['i-086c8df1545018ab0'])

vpc_id = resp['Reservations'][0]['Instances'][0]['VpcId']
public_ip = resp['Reservations'][0]['Instances'][0]['PublicIpAddress']
print(vpc_id)
print(public_ip)