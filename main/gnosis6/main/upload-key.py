# Upload secret key to s3 bucket and return the s3 bucket URL using Python boto3

import boto3

# Set the name of your S3 bucket
bucket_name = 'project-ubuntu-gnosis-2023'

# Set the path and name of the file to upload
file_path = '/tmp/secret.key'
file_name = 'secret.key'



# Set the name of your AWS profile
aws_profile_name = 'default'

# Create an S3 resource using the specified AWS profile
session = boto3.Session(profile_name=aws_profile_name)
s3 = session.resource('s3')

# Upload the file to the S3 bucket
s3.Bucket(bucket_name).upload_file(file_path, file_name)

# Generate a URL for the uploaded file
s3_object = s3.Object(bucket_name, file_name)
s3_url = s3_object.get().get('ResponseMetadata').get('HTTPHeaders').get('x-amz-presigned-url')

# Print the S3 URL of the uploaded file
# print(s3_url)

#print list of files from above bucket

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    print(obj.key)
