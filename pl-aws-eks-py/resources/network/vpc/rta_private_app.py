import pulumi_aws as aws
from pulumi import ResourceOptions

import sn_private_app
import rt_private_app

from config import (
    project_name,
    environment,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)

route_table_association_private_app_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ sn_private_app.private_app_subnet_az1, rt_private_app.route_table_private_app_az1 ]),
    subnet_id = sn_private_app.private_app_subnet_az1.id,
    route_table_id = rt_private_app.route_table_private_app_az1.id,
)

route_table_association_private_app_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ sn_private_app.private_app_subnet_az2, rt_private_app.route_table_private_app_az2 ]),
    subnet_id = sn_private_app.private_app_subnet_az2.id,
    route_table_id = rt_private_app.route_table_private_app_az2.id,    
)

route_table_association_private_app_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ sn_private_app.private_app_subnet_az3, rt_private_app.route_table_private_app_az3 ]),
    subnet_id = sn_private_app.private_app_subnet_az3.id,
    route_table_id = rt_private_app.route_table_private_app_az3.id,
)

route_table_association_private_app_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-app',
    opts = ResourceOptions(depends_on = [ sn_private_app.private_app_subnet_az4, rt_private_app.route_table_private_app_az4 ]),
    subnet_id = sn_private_app.private_app_subnet_az4.id,
    route_table_id = rt_private_app.route_table_private_app_az4.id,
)