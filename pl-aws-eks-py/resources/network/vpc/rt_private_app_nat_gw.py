import pulumi_aws as aws
from pulumi import ResourceOptions

import nat_gateway
import rt_private_app

from config import (
    project_name,
    environment,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)


route_table_private_app_internet_route_az1 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway.nat_gateway_az1 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway.nat_gateway_az1.id,
    route_table_id = rt_private_app.route_table_private_app_az1.id,
)

route_table_private_app_internet_route_az2 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway.nat_gateway_az2 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway.nat_gateway_az2.id,
    route_table_id = rt_private_app.route_table_private_app_az2.id,    
)

route_table_private_app_internet_route_az3 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway.nat_gateway_az3 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway.nat_gateway_az3.id,
    route_table_id = rt_private_app.route_table_private_app_az3.id,
)

route_table_private_app_internet_route_az4 = aws.ec2.Route(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-app-route',
    opts = ResourceOptions(depends_on = [ nat_gateway.nat_gateway_az4 ]),
    destination_cidr_block = '0.0.0.0/0',
    gateway_id = nat_gateway.nat_gateway_az4.id,
    route_table_id = rt_private_app.route_table_private_app_az4.id,
)