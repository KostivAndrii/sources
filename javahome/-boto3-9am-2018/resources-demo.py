# Find all running instances and stop
import boto3

"""
    Boto3 client is low level object, it has all operations
    Boto3 Resource is a wrapper around client, resources will not
    have all operation(methods) which client has, resources, 
    can simplify your code.
"""

ec2 = boto3.resource('ec2')

# list(ec2.Instance)
ec2.instances.all().stop()

