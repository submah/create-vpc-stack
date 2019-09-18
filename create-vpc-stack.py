import boto3

ec2 = boto3.resource('ec2', aws_access_key_id='PROVICE-YOUR-ACCESS_KEY',
                     aws_secret_access_key='PROVIDE-YOUR-SECRET_ACCESS_KEY',
                     region_name='us-east-1')


# create VPC
vpc = ec2.create_vpc(CidrBlock='90.0.0.0/16')

# we can assign a name to vpc, or any resource, by using tag
vpc.create_tags(Tags=[{"Key": "Name", "Value": "VPC-A"}])
vpc.wait_until_available()
print('VPC-ID is: ', vpc.id)

# create then attach internet gateway
ig = ec2.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=ig.id
    )
print('InternetGateway ID is: ' ,ig.id)

# create a route table and a public route
route_table = vpc.create_route_table()
route = route_table.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig.id
)
print('Public Routetable ID is: ', route_table.id)

# create Pulblic subnets
public_subnet1 = ec2.create_subnet(
    AvailabilityZone='us-east-1a',
    CidrBlock='90.0.1.0/24',
    VpcId=vpc.id)
print('Public_subnet1 ID is: ', public_subnet1.id)


public_subnet2 = ec2.create_subnet(
    AvailabilityZone='us-east-1b',
    CidrBlock='90.0.3.0/24',
    VpcId=vpc.id)
print('Public_subnet2 ID is: ', public_subnet2.id)

#create Private subnets
private_subnet1 = ec2.create_subnet(
    AvailabilityZone='us-east-1a',
    CidrBlock='90.0.2.0/24',
    VpcId=vpc.id)
print('Private_subnet1 ID is: ', private_subnet1.id)

private_subnet2 = ec2.create_subnet(
    AvailabilityZone='us-east-1b',
    CidrBlock='90.0.4.0/24',
    VpcId=vpc.id)
print('Private_subnet2 ID is: ', private_subnet2.id)


#Tag the subnets
public_subnet1.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-public-subnet'
            }
        ]
    )

public_subnet2.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-public-subnet'
            }
        ]
    )


private_subnet1.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-private-subnet'
            }
        ]
    )

private_subnet2.create_tags(Tags=[{'Key': 'Name','Value': 'vpc-a-private-subnet'}])

# create a route table and a public route
public_route_table = vpc.create_route_table()

public_route = public_route_table.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=ig.id
)
print('public_route_table ID is: ', public_route_table.id)

#tag the public_route_table
public_route_table.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-public-rt'
            }
        ]
    )

# create a route table and a private route
private_route_table = vpc.create_route_table()
print('public_route_table ID is: ', private_route_table.id)

#tag the public_route_table
private_route_table.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-private-rt'
            }
        ]
    )


# associate the public routetable to public subnet
public_route_table.associate_with_subnet(SubnetId=public_subnet1.id)
public_route_table.associate_with_subnet(SubnetId=public_subnet2.id)
# associate the private routetable to private subnet
private_route_table.associate_with_subnet(SubnetId=private_subnet1.id)
private_route_table.associate_with_subnet(SubnetId=private_subnet2.id)


# Create public security group
public_sec_group = ec2.create_security_group(
    GroupName='vpc-a-public-sg',
    Description='vpc-a-public-sg',
    VpcId=vpc.id)

print('public_sec_group ID is: ', public_sec_group.id)


public_sec_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22)

public_sec_group.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-public-sg'
            }
        ]
    )

# Create private security group
private_sec_group = ec2.create_security_group(GroupName='vpc-a-private-sg', Description='vpc-a-private-sg', VpcId=vpc.id)
print('private_sec_group ID is: ', private_sec_group.id)

private_sec_group.authorize_ingress(CidrIp='0.0.0.0/0', IpProtocol='tcp', FromPort=22, ToPort=22)
private_sec_group.create_tags(
    Tags=[
            {
                'Key': 'Name',
                'Value': 'vpc-a-private-sg'
            }
        ]
    )
