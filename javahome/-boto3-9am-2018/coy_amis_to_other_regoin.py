# Create Image for EC2 and copy to other regions.

import boto3
client = boto3.client('ec2','ap-south-1')

ec2_singapore = boto3.client('ec2','ap-southeast-1')
# Find ec2 instances with tag(Key=Backup, Value=Yes) and create AMI
resp = client.describe_instances(
    Filters =[
        {
            'Name': 'tag:Backup',
            'Values':['Yes', 'yes', 'YES']
        }
    ]
)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        image_resp = client.create_image(
            InstanceId=instance['InstanceId'],
            Description='Workind On Boto3 Demo',
            Name = 'Workind On Boto3 Demo'
        )
        image_id = image_resp['ImageId']
        print(f'ImageId = {image_id}')
        # copy image to singapore
        # Wait for Image to be in available state
        waiter = client.get_waiter('image_available')
        print('Before Wait')
        waiter.wait(
            ImageIds=[image_id],
            Owners=[
                '999999999999'
            ]
        )
        print('After Wait')
        ec2_singapore.copy_image(
            SourceImageId=image_id,
            Name='Image Copied Fro Mumbai',
            SourceRegion = 'ap-south-1'
        )
