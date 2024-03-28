import pulumi_aws as aws
from pulumi import ResourceOptions

import eip
import sn_public_shared

from config import (
    project_name,
    environment,
    owner,
    availability_zone_az1,
    availability_zone_az2,
    availability_zone_az3,
    availability_zone_az4,
)


# The NAT gateway for the private shared  subnet
# ej. project-dev-us-east-1a-nat-gw
nat_gateway_az1 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az1}-nat-gw',
    opts = ResourceOptions(depends_on = [ sn_public_shared.public_shared_subnet_az1 ]),
    allocation_id = eip.shared_nat_eip_az1.id,
    subnet_id = sn_public_shared.public_shared_subnet_az1.id,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az1}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1b-nat-gw
nat_gateway_az2 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az2}-nat-gw',
    opts = ResourceOptions(depends_on = [ sn_public_shared.public_shared_subnet_az2 ]),
    allocation_id = eip.shared_nat_eip_az2.id,
    subnet_id = sn_public_shared.public_shared_subnet_az2.id,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az2}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1c-nat-gw
nat_gateway_az3 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az3}-nat-gw',
    opts = ResourceOptions(depends_on = [ sn_public_shared.public_shared_subnet_az3 ]),
    allocation_id = eip.shared_nat_eip_az3.id,
    subnet_id = sn_public_shared.public_shared_subnet_az3.id,
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az3}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

# ej. project-dev-us-east-1d-nat-gw
nat_gateway_az4 = aws.ec2.NatGateway(
    resource_name = f'{project_name}-{environment}-{availability_zone_az4}-nat-gw',
    opts = ResourceOptions(depends_on = [ sn_public_shared.public_shared_subnet_az4 ]),
    allocation_id = eip.shared_nat_eip_az4.id,
    subnet_id = sn_public_shared.public_shared_subnet_az4.id,    
    tags={
        'Name': f'{project_name}-{environment}-{availability_zone_az4}-nat-gw',
        'Network': 'public',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)