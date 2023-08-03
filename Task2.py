
# Stop a running EC2 instance.
# •	How to do it: 
# o	Use boto3.client('ec2') to create an EC2 client.
# o	Call stop_instances() and provide the instance ID to stop a running EC2 instance.
# •	Test: Verify that the EC2 instance is stopped by checking its state.


import boto3
from decouple import config

aws_access_key = config ('aws_access_key')
aws_secret_key = config ('aws_secret_key')
region_name = config ('region_name')


ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

#Stop a running EC2 instance:

instance_id_to_stop = 'i-xxxxxxxxxxxxxxxxx'
response = ec2.stop_instances(InstanceIds=[instance_id_to_stop])
print("Stopping instance with ID:", instance_id_to_stop)


#Verify the instance's state:
response = ec2.describe_instances(InstanceIds=[instance_id_to_stop])
instance_state = response['Reservations'][0]['Instances'][0]['State']['Name']

print("Instance state after stopping:", instance_state)