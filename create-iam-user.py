import boto3

#Create a Session
session = boto3.session.Session(aws_access_key_id='PROVICE_YOUR_ACCESS_KEY',
                     aws_secret_access_key='PROVICE_YOUR_SECRET_ACCESS_KEY', region_name='us-east-1')

# Create IAM resource
iam_res = session.resource(service_name='iam')

#Create user
define_user = fakeuser1
user_response = iam_res.create_user(UserName=define_user)
print(user_response)
