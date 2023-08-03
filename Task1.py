# Task 1: Launch an EC2 instance and list its details.
# •	How to do it: 
# o	Use boto3.client('ec2') to create an EC2 client.
# o	Call run_instances() to launch a new EC2 instance.
# o	Call describe_instances() to get information about the launched instance.
# •	Test: Print the instance ID, IP address, instance type, and other relevant details of the launched EC2 instance.

import boto3
from decouple import config

aws_access_key = config ('aws_access_key')
aws_secret_key = config ('aws_secret_key')
region_name = config ('region_name')

# Create an EC2 client
ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


#Launch an EC2 instance
instance = ec2.run_instances(
    ImageId='ami-040d60c831d02d41c',  
    InstanceType='t3.micro',          
    MinCount=1,
    MaxCount=1,
    KeyName='julias_key_pair',
)

#Wait for the instance to be fully launched:
instance_id = instance['Instances'][0]['InstanceId']


#Get information about the launched instance:
response = ec2.describe_instances(InstanceIds=[instance_id])
instance_info = response['Reservations'][0]['Instances'][0]

# Extract relevant details
instance_ip = instance_info['PublicIpAddress']
instance_type = instance_info['InstanceType']

# Print the details
print("Instance ID:", instance_id)
print("IP Address:", instance_ip)
print("Instance Type:", instance_type)

