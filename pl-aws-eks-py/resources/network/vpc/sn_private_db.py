import pulumi_aws as aws
from pulumi import ResourceOptions

import vpc

from config import (
    project_name,
    environment,
    owner,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
    private_db_subnet_cidr_az1,
    private_db_subnet_cidr_az2,
    private_db_subnet_cidr_az3,
    private_db_subnet_cidr_az4,
)


# projectName-environmentName-aws-availabilityZone1-private-subnet-db
# ej. project-dev-us-east-1a-private-subnet-db
private_db_subnet_az1 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az1,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az1,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone2-private-subnet-db
# ej. project-dev-us-east-1b-private-subnet-db
private_db_subnet_az2 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az2,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az2,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone3-private-subnet-db
# ej. project-dev-us-east-1c-private-subnet-db
private_db_subnet_az3 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az3,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az3,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)

# projectName-environmentName-aws-availabilityZone4-private-subnet-db
# ej. project-dev-us-east-1d-private-subnet-db
private_db_subnet_az4 = aws.ec2.Subnet(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-db',
    opts = ResourceOptions(depends_on = [ vpc ]),
    cidr_block = private_db_subnet_cidr_az4,
    vpc_id = vpc.id,
    map_public_ip_on_launch = False,
    availability_zone = availability_zone_az4,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-subnet-db',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    }
)