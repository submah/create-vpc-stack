import boto3
region = 'eu-west-1'
bucket_name = 'mydemobucket909090'
#Create a sessiion
session = boto3.session.Session(aws_access_key_id='PROVIDE-YOUR-ACCESSKEY',
                     aws_secret_access_key='PROVIDE-YOUR-SECRET-ACCESSKEY')

#create s3 resource and client
s3_res = session.resource(service_name='s3')
s3_cli = session.client(service_name='s3')


# Create bucket
bucket_response = s3_cli.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
        'LocationConstraint': region})
print(bucket_response)

#Print all s3 bucket
#for bucket in s3_res.buckets.all():
#    print(bucket.name)

