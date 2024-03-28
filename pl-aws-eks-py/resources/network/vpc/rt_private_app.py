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
)

############## Create Route Table Private ##############
# StackName-environmentName-aws:availabilityZone1-private1-rtb
# ej. project-dev-us-east-1a-private-app-rtb
route_table_private_app_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1b-private-app-rtb
route_table_private_app_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1c-private-app-rtb
route_table_private_app_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1d-private-app-rtb
route_table_private_app_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-app-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-app-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)