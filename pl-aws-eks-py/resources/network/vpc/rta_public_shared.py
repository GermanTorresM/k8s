import pulumi_aws as aws
from pulumi import ResourceOptions

import sn_public_shared
import rt_public_shared

from config import (
    project_name,
    environment,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)


route_table_association_public_shared_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-shared',
    subnet_id = sn_public_shared.public_shared_subnet_az1.id,
    route_table_id = rt_public_shared.route_table_public_shared_az1.id,
)

route_table_association_public_shared_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-shared',
    subnet_id = sn_public_shared.public_shared_subnet_az2.id,
    route_table_id = rt_public_shared.route_table_public_shared_az2.id,
)

route_table_association_public_shared_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-shared',
    subnet_id = sn_public_shared.public_shared_subnet_az3.id,
    route_table_id = rt_public_shared.route_table_public_shared_az3.id,
)

route_table_association_public_shared_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-shared',
    subnet_id = sn_public_shared.public_shared_subnet_az4.id,
    route_table_id = rt_public_shared.route_table_public_shared_az4.id,
)