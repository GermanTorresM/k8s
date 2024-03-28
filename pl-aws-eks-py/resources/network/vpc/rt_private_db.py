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

# StackName-environmentName-aws:availabilityZone1-private-db-rtb
# ej. project-dev-us-east-1a-private-db-rtb
route_table_private_db_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# StackName-environmentName-aws:availabilityZone2-private-db-rtb
# ej. project-dev-us-east-1b-private-db-rtb
route_table_private_db_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# StackName-environmentName-aws:availabilityZone3-private-db-rtb
# ej. project-dev-us-east-1c-private-db-rtb
route_table_private_db_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# StackName-environmentName-aws:availabilityZone4-private-db-rtb
# ej. project-dev-us-east-1d-private-db-rtb
route_table_private_db_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-db-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,    
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-db-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)