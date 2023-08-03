# Task 5: Delete all objects in an S3 bucket and then delete the bucket.
# •	How to do it: 
# o	Use boto3.resource('s3') to create an S3 resource.
# o	Call Bucket.objects.all() to list all objects in the S3 bucket.
# o	Iterate through the objects and call delete() to delete each object.
# o	Finally, call delete() to delete the S3 bucket.
# •	Test: Verify that all objects are deleted and the S3 bucket is no longer present.

import boto3
from decouple import config

aws_access_key = config ('aws_access_key')
aws_secret_key = config ('aws_secret_key')
region_name = config ('region_name')

s3 = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

#Delete all objects in an S3 bucket:

bucket_name = 'mybucket-julijaand'
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    obj.delete()
print("All objects in the S3 bucket deleted.")

# Delete the S3 bucket

bucket.delete()
print("S3 bucket deleted.")