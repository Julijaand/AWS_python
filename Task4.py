# Task 4: List all objects in an S3 bucket.
# •	How to do it: 
# o	Use boto3.resource('s3') to create an S3 resource.
# o	Call Bucket.objects.all() to list all objects in a specific S3 bucket.
# •	Test: Print the list of object keys (names) in the S3 bucket.

import boto3
from decouple import config

aws_access_key = config ('aws_access_key')
aws_secret_key = config ('aws_secret_key')
region_name = config ('region_name')

s3 = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

#List all objects in an S3 bucket:

bucket_name = 'mybucket-julijaand' 
bucket = s3.Bucket(bucket_name)
object_keys = [obj.key for obj in bucket.objects.all()]

print("List of object keys in the S3 bucket:", object_keys)