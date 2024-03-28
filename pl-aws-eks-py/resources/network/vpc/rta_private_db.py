import pulumi_aws as aws
from pulumi import ResourceOptions

import sn_private_db
import rt_private_db

from config import (
    project_name,
    environment,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)


route_table_association_private_db_az1 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ sn_private_db.private_db_subnet_az1, rt_private_db.route_table_private_db_az1 ]),
    subnet_id = sn_private_db.private_db_subnet_az1.id,
    route_table_id = rt_private_db.route_table_private_db_az1.id,
)

route_table_association_private_db_az2 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ sn_private_db.private_db_subnet_az2, rt_private_db.route_table_private_db_az2 ]),
    subnet_id = sn_private_db.private_db_subnet_az2.id,
    route_table_id = rt_private_db.route_table_private_db_az2.id,
)

route_table_association_private_db_az3 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ sn_private_db.private_db_subnet_az3, rt_private_db.route_table_private_db_az3 ]),
    subnet_id = sn_private_db.private_db_subnet_az3.id,
    route_table_id = rt_private_db.route_table_private_db_az3.id,
)

route_table_association_private_db_az4 = aws.ec2.RouteTableAssociation(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-route-table-association-db',
    opts = ResourceOptions(depends_on = [ sn_private_db.private_db_subnet_az4, rt_private_db.route_table_private_db_az4 ]),
    subnet_id = sn_private_db.private_db_subnet_az4.id,
    route_table_id = rt_private_db.route_table_private_db_az4.id,
)