import boto3

# Set the name of your S3 bucket and the file name
bucket_name = 'project-ubuntu-gnosis-2023'
file_name = 'secret.key'

# Set the name of your AWS profile (optional)
aws_profile_name = 'default'

# Create an S3 resource using the specified AWS profile (if provided)
session = boto3.Session(profile_name=aws_profile_name)
s3 = session.resource('s3')

# Get the contents of the file
obj = s3.Object(bucket_name, file_name)
contents = obj.get()['Body'].read().decode('utf-8')

# Print the contents of the file
print(contents)
