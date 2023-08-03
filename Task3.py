# Task 3: Upload a file to an S3 bucket and download it back.
# •	How to do it: 
# o	Use boto3.client('s3') to create an S3 client.
# o	Call upload_file() to upload a local file to an S3 bucket.
# o	Call download_file() to download the uploaded file back to the local system.
# •	Test: Check that the uploaded file is successfully downloaded and its content matches the original file.

import boto3
from decouple import config

aws_access_key = config ('aws_access_key')
aws_secret_key = config ('aws_secret_key')
region_name = config ('region_name')

s3 = boto3.client('s3', region_name=region_name, aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)


# Upload a file to an S3 bucket:

bucket_name = 'mybucket-julijaand'
local_file_path = 'C:\My\AccentureBootcamp2\codes\python_AWS\index.html'
s3_file_key = 'index.html'  
s3.upload_file(local_file_path, bucket_name, s3_file_key)
print("File uploaded to S3 bucket:", bucket_name)

# Download the uploaded file back:

downloaded_file_path = 'C:\My\AccentureBootcamp2\codes\python_AWS\index.html'  
s3.download_file(bucket_name, s3_file_key, downloaded_file_path)
print("File downloaded from S3 and saved at:", downloaded_file_path)

# Check if files are similar
with open(local_file_path, 'rb') as local_file:
    local_content = local_file.read()

with open(downloaded_file_path, 'rb') as downloaded_file:
    downloaded_content = downloaded_file.read()

if local_content == downloaded_content:
    print("Content matches between original and downloaded files.")
else:
    print("Content does not match between original and downloaded files.")