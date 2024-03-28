import pulumi_aws as aws
from pulumi import ResourceOptions

from config import (
    project_name,
    environment,
    owner,
    vpc_cidr,
    aws_region,
)

############## Create VPC ##############
# projectName-environmentName-aws:region-vpc
# ej. project-dev-us-east-1-vpc
vpc = aws.ec2.Vpc(
    resource_name = f'{project_name}-{environment}-{aws_region}-vpc',
    cidr_block = vpc_cidr,    
    enable_dns_hostnames = True,
    enable_dns_support = True,
    instance_tenancy = 'default',
    tags={
        'Name': f'{project_name}-{environment}-{aws_region}-vpc',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,        
    },
)