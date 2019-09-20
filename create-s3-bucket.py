import boto3
region = 'us-east-1'
bucket_name = 'mydemobucket9090'
#Create a sessiion
session = boto3.session.Session(aws_access_key_id='PROVICE_YOUR_ACCESS_KEY',
                     aws_secret_access_key='PROVICE_YOUR_SECRET_ACCESS_KEY', region_name=region)

#create s3 resource and client
s3_res = session.resource(service_name='s3')
s3_cli = session.client(service_name='s3')


# Create bucket
bucket_response = s3_cli.create_bucket(Bucket=bucket_name)
print(bucket_response)
