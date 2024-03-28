import pulumi_aws as aws
from pulumi import ResourceOptions

import vpc

from config import (
    project_name,
    environment,
    owner,
    aws_region,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
    public_alb_subnet_cidr_az1,
    public_alb_subnet_cidr_az2,
    public_alb_subnet_cidr_az3,
    public_alb_subnet_cidr_az4,
)

############## Create Subnet ##############
# projectName-environmentName-aws-availabilityZone1-public-subnet
# ej. project-dev-us-east-1a-public-subnet-alb
public_alb_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{aws_region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone2-public-subnet
# ej. project-dev-us-east-1b-public-subnet-alb
public_alb_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{aws_region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone3-public-subnet
# ej. project-dev-us-east-1c-public-subnet-alb
public_alb_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{aws_region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)

# projectName-environmentName-aws-availabilityZone4-public-subnet
# ej. project-dev-us-east-1d-public-subnet-alb
public_alb_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-subnet-alb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = public_alb_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-subnet-alb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
        f'kubernetes.io/cluster/{project_name}-{environment}-{aws_region}-eks-cluster': 'shared',
        'kubernetes.io/role/elb': '1',
    }
)