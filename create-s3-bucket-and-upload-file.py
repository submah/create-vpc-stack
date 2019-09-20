import boto3
region = 'us-east-1'
bucket_name = 'PROVICE-NAME-OF-THE-BUCKET-WHICH-WILL-GET-CREATED'
#Create a sessiion
session = boto3.session.Session(aws_access_key_id='PROVICE_YOUR_ACCESS_KEY',
                     aws_secret_access_key='PROVICE_YOUR_SECRET_ACCESS_KEY', region_name=region)

#create s3 resource and client
s3_res = session.resource(service_name='s3')
s3_cli = session.client(service_name='s3')

#If a region is not specified, the bucket is created in the S3 default region (us-east-1).

# Create bucket
bucket_response = s3_cli.create_bucket(Bucket=bucket_name)
print(bucket_response)


s3_res.meta.client.upload_file('./test-s3-file.txt', bucket_name, 'test-s3-file.txt')
