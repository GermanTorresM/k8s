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

# StackName-environmentName-aws:availabilityZone1-private-spare-rtb
# ej. project-dev-us-east-1a-private-spare-rtb
route_table_private_spare_az1 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# StackName-environmentName-aws:availabilityZone2-private-spare-rtb
# ej. project-dev-us-east-1b-private-spare-rtb
route_table_private_spare_az2 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# StackName-environmentName-aws:availabilityZone3-private-spare-rtb
# ej. project-dev-us-east-1c-private-spare-rtb
route_table_private_spare_az3 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# StackName-environmentName-aws:availabilityZone4-private-spare-rtb
# ej. project-dev-us-east-1d-private-spare-rtb
route_table_private_spare_az4 = aws.ec2.RouteTable(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-private-spare-rtb',
    opts = ResourceOptions(depends_on = [ vpc ]),
    vpc_id = vpc.id,
    tags = {
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-private-spare-rtb',
        'Network': 'private',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)