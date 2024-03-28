import pulumi_aws as aws
from pulumi import ResourceOptions

import vpc

from config import (
    project_name,
    environment,
    owner,
    aws_region,
)


############## Create Internet Gateway ##############
# projectName-environmentName-aws:region-igw
# ej. project-dev-us-east-1-igw
internet_gateway = aws.ec2.InternetGateway(
    resource_name = f'{project_name}-{environment}-{aws_region}-igw',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags={
        'Name': f'{project_name}-{environment}-{aws_region}-igw',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)