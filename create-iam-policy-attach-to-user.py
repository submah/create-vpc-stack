import boto3
import json

#Create a Session
session = boto3.session.Session(aws_access_key_id='PROVIDE_YOUR_ACCESS_KEY',
                     aws_secret_access_key='PROVIDE_YOUR_SECRET_ACCESS_KEY', region_name='us-east-1')

# Create IAM resource
iam_res = session.resource(service_name='iam')

# Create IAM client
iam_cli = session.client(service_name='iam')



# Define a policy
my_managed_policy = {
        "Version": "2012-10-17",
        "Statement": [
                {
                        "Action": [
                                "ec2:Describe*",
                                "ec2:Get*"
                        ],
                        "Effect": "Allow",
                        "Resource": "*"
                }
        ]
}

#Create a policy
response = iam_res.create_policy(
        PolicyName='my_policy_by_python1',
        PolicyDocument=json.dumps(my_managed_policy)
        )

policy_arn = response.arn
print(policy_arn)

#Attach policy to user
response = iam_cli.attach_user_policy(
    UserName='fakeuser1', #DEFINE UserName HERE
    PolicyArn=policy_arn
    )
