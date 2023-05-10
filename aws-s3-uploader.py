import os
import boto3

# Set the AWS region and S3 bucket name
region = 'us-east-1'
bucket_name = 'ccfinalproject1'

#add your access key and secret access key
aws_access_key_id = 'AKIAW4SR6JDQGF4P4Z77'
aws_secret_access_key = 'iX4qW3oo9aGi69/fpKcoatEhTkqyHnMCDWdPpqUa'

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
)
# Create an S3 client
s3 = session.client('s3')

directory_path = 'dataset/'

# Iterate over the files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    # Set the key (filename) under which to store the file in the S3 bucket
    key = f'heart-care/{filename}'
    
    # Upload the file to the S3 bucket
    s3.upload_file(file_path, bucket_name, key)

print('File uploaded successfully.')


