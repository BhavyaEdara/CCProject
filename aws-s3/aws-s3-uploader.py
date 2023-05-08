import os
import boto3

# Set the AWS region and S3 bucket name
region = 'eu-north-1'
bucket_name = 'madarauchiha'

#add your access key and secret access key
aws_access_key_id = 'AKIAW7D42JAN3YB7GL3S'
aws_secret_access_key = 'a96VEWdReugHcqeURV/ikoQuoWlhHJeIbNeIfrGh'

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

