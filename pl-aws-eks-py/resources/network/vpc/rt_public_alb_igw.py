import pulumi_aws as aws
from pulumi import ResourceOptions

import vpc
import internet_gateway

from config import (
    project_name,
    environment,
    owner,
    aws_region,
)

############## Create Route Table Public ##############
# StackName-environmentName-public-rtb
# ej. project-dev-public-rtb
route_table_public = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{aws_region}-public-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{aws_region}-public-rtb',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

route_public_igw = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{aws_region}-route',
    opts = ResourceOptions(depends_on = [ internet_gateway, route_table_public ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = internet_gateway.id,
    route_table_id = route_table_public.id,
)