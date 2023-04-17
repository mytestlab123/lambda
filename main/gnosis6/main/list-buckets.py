import boto3

# Set the name of your S3 bucket
bucket_name = 'project-ubuntu-gnosis-2023'

# Set the name of your AWS profile (optional)
aws_profile_name = 'default'

# Create an S3 resource using the specified AWS profile (if provided)
session = boto3.Session(profile_name=aws_profile_name)
s3 = session.resource('s3')

# List all objects in the S3 bucket
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    print(obj.key)
