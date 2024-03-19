import os

import boto3
from boto3.s3.transfer import S3UploadFailedError

templates = ['root.yml',
             'CFSimpleDemo.yml',
             'SubsetDemo.yml',
             'IGW.yml',
             'main.yml',
             'ec2_FastAPI.yml',
             'vpc.yml']
bucket_name = 'uno-cf'
bucket = boto3.resource("s3").Bucket(bucket_name)
if not bucket.creation_date: exit("No creation date")

print(f'Bucket [{bucket.name}]: created at {bucket.creation_date}')
for template in templates:
    obj = bucket.Object(os.path.basename(template))
    try:
        obj.upload_file(template)
        print(
            f"Uploaded file {template} into bucket {bucket.name} with key {obj.key}."
        )
    except S3UploadFailedError as err:
        print(f"Couldn't upload file {template} to {bucket.name}.")
        exit(f"\t{err}")
