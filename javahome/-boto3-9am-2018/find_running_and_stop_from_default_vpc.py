# Get Instance ids  of all EC2 instances in running state
import boto3
client = boto3.client('ec2','ap-south-1')
def find_instances_in_default_vpc():
    resp = client.describe_instances(
        Filters=[
            # {
            #     'Name': 'instance-state-name',
            #     'Values':['running']
            # },
            {
                'Name': 'vpc-id',
                'Values': ['vpc-79ab8b11']
            }
        ]
    )

    resp
    instance_ids = list()
    default_vpc = get_default_vpc_id()

    for reservation in resp['Reservations']:
        for instance in reservation["Instances"]:
            instance_id = instance['InstanceId']
            vpc_id = instance['VpcId']
            if default_vpc == vpc_id:
                instance_ids.append(instance_id)
                print(f' Instance id is  {instance_id}')

    if len(instance_ids):
        client.stop_instances(
            InstanceIds=instance_ids
        )


def get_default_vpc_id():
    vpc_resp =client.describe_vpcs(
        Filters = [
            {
                'Name': 'isDefault',
                'Values' : ['true']
            }
        ]
    )
    return vpc_resp['Vpcs'][0]['VpcId']


# call method
find_instances_in_default_vpc()