import boto3
# Delete custom AMIs that is not in use

# Step-1, Get list of custom ami ids

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')
images = client.describe_images(
    Owners=['999999999999']
)
# Get all custom images and add it to list
custom_amis = []
for image in images['Images']:
    custom_amis.append(image['ImageId'])

# Describe all ec2 and get image ids it is using

in_use_amis = set()
for instance in ec2.instances.all():
    in_use_amis.add(instance.image_id)

# Delete all instance that are not in use

for ami in custom_amis:
    if ami not in in_use_amis:
        client.deregister_image(ImageId=ami)
