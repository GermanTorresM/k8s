import pulumi_aws as aws
from pulumi import ResourceOptions

import internet_gateway

from config import (
    project_name,
    environment,
    owner,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)


# The NAT IP for the public shared subnet, as seen from within the public one
# ej. project-dev-us-east-1a-public-shared-ip
shared_nat_eip_az1 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1b-public-shared-ip
shared_nat_eip_az2 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1c-public-shared-ip
shared_nat_eip_az3 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1d-public-shared-ip
shared_nat_eip_az4 = aws.ec2.Eip(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-shared-ip',
    opts = ResourceOptions(depends_on = [ internet_gateway ]),
    vpc = True,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-shared-ip',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)