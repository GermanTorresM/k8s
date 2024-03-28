import pulumi_aws as aws
from pulumi import ResourceOptions

import vpc
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


# StackName-environmentName-availabilityZone1-public-rtb
# ej. project-dev-us-east-1a-public-shared-rtb
route_table_public_shared_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_public_shared_internet_az1 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az1.id,
)

# StackName-environmentName-availabilityZone2-public-rtb
# ej. project-dev-us-east-1b-public-shared-rtb
route_table_public_shared_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_public_shared_internet_az2 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az2.id,
)

# StackName-environmentName-availabilityZone3-public-rtb
# ej. project-dev-us-east-1c-public-shared-rtb
route_table_public_shared_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_public_shared_internet_az3 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az3.id,
)

# StackName-environmentName-availabilityZone4-public-rtb
# ej. project-dev-us-east-1d-public-shared-rtb
route_table_public_shared_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-public-shared-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-public-shared-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_public_shared_internet_az4 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-shared-route',
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public_shared_az4.id,
)