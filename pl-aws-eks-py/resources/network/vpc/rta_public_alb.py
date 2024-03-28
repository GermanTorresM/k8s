import pulumi_aws as aws
from pulumi import ResourceOptions

import rt_public
import sn_public_alb

from config import (
    project_name,
    environment,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)

# Route Table Subnet Associations
route_table_association_public_alb_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-alb',
    subnet_id = sn_public_alb.public_alb_subnet_az1.id,
    route_table_id = rt_public.route_table_public.id,
)

route_table_association_public_alb_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-alb',
    subnet_id = sn_public_alb.public_alb_subnet_az2.id,
    route_table_id = rt_public.route_table_public.id,
)

route_table_association_public_alb_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-alb',
    subnet_id = sn_public_alb.public_alb_subnet_az3.id,
    route_table_id = rt_public.route_table_public.id,
)

route_table_association_public_alb_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-alb',
    subnet_id = sn_public_alb.public_alb_subnet_az4.id,
    route_table_id = rt_public.route_table_public.id,
)