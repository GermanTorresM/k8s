"""
Deploys:
- Network: VPC, Subnets, Security Groups

"""

# VPC
import resources.network.vpc.vpc
# Subnet Public Application Load Balancer
import resources.network.vpc.sn_public_alb
# Subnet Public Shared
import resources.network.vpc.sn_public_shared
# Subnet Private Applications
import resources.network.vpc.sn_private_app
# Subnet Private Database
import resources.network.vpc.sn_private_db
# Subnet Private Cache
import resources.network.vpc.sn_private_cache
# Subnet Private Keycloak
import resources.network.vpc.sn_private_keycloak
# Subnet Private Kafka
import resources.network.vpc.sn_private_kafka
# Subnet Private Spare
import resources.network.vpc.sn_private_spare
# Internet Gateway
import resources.network.vpc.internet_gateway
# Route / RouteTable Public ALB
import resources.network.vpc.rt_public_alb_igw
import resources.network.vpc.rta_public_alb
# Route / RouteTable Public Shared
import resources.network.vpc.rt_public_shared_igw
import resources.network.vpc.rta_public_shared
# Route / RouteTable Private Application
import resources.network.vpc.rt_private_app
import resources.network.vpc.rta_private_app
# Route / RouteTable Private Database
import resources.network.vpc.rt_private_db
import resources.network.vpc.rta_private_db
# Route / RouteTable Private Spare
import resources.network.vpc.rt_private_spare
import resources.network.vpc.rta_private_spare
# Elastic IP
import resources.network.vpc.eip
# Nat Gateway
import resources.network.vpc.nat_gateway
# Route Table NAT Gateway
import resources.network.vpc.rt_private_app_nat_gw
# Role IAM VPC FLow Logs
#import resources.network.iam.role_vpc_flow_logs
# VPC Flow Logs

# Network ACLs
import resources.network.vpc.nacl_public_alb
import resources.network.vpc.nacl_public_shared
import resources.network.vpc.nacl_private_app
import resources.network.vpc.nacl_private_db





# Add your exports here
#pulumi.export("project name", project_name)

#pulumi.export('vpc_id', vpc.id)
#pulumi.export('public_alb_network_acl', public_alb_network_acl.id)
#pulumi.export('public_shared_network_acl', public_shared_network_acl.id)
#pulumi.export('private_app_network_acl', private_app_network_acl.id)
#pulumi.export('private_db_network_acl', private_db_network_acl.id)




'''
pulumi.export('public_alb_subnet_az1', public_alb_subnet_az1.id)
pulumi.export('public_alb_subnet_az2', public_alb_subnet_az2.id)
pulumi.export('public_alb_subnet_az3', public_alb_subnet_az3.id)
pulumi.export('public_alb_subnet_az4', public_alb_subnet_az4.id)

pulumi.export('public_shared_subnet_az1', public_shared_subnet_az1.id)
pulumi.export('public_shared_subnet_az2', public_shared_subnet_az2.id)
pulumi.export('public_shared_subnet_az3', public_shared_subnet_az3.id)
pulumi.export('public_shared_subnet_az4', public_shared_subnet_az4.id)

pulumi.export('private_app_subnet_az1', private_app_subnet_az1.id)
pulumi.export('private_app_subnet_az2', private_app_subnet_az2.id)
pulumi.export('private_app_subnet_az3', private_app_subnet_az3.id)
pulumi.export('private_app_subnet_az4', private_app_subnet_az4.id)

pulumi.export('private_db_subnet_az1', private_db_subnet_az1.id)
pulumi.export('private_db_subnet_az2', private_db_subnet_az2.id)
pulumi.export('private_db_subnet_az3', private_db_subnet_az3.id)
pulumi.export('private_db_subnet_az4', private_db_subnet_az4.id)

pulumi.export('private_keycloak_subnet_az1', private_keycloak_subnet_az1.id)
pulumi.export('private_keycloak_subnet_az2', private_keycloak_subnet_az2.id)
pulumi.export('private_keycloak_subnet_az3', private_keycloak_subnet_az3.id)
pulumi.export('private_keycloak_subnet_az4', private_keycloak_subnet_az4.id)

pulumi.export('private_kafka_subnet_az1', private_kafka_subnet_az1.id)
pulumi.export('private_kafka_subnet_az2', private_kafka_subnet_az2.id)
pulumi.export('private_kafka_subnet_az3', private_kafka_subnet_az3.id)
pulumi.export('private_kafka_subnet_az4', private_kafka_subnet_az4.id)

pulumi.export('private_cache_subnet_az1', private_cache_subnet_az1.id)
pulumi.export('private_cache_subnet_az2', private_cache_subnet_az2.id)
pulumi.export('private_cache_subnet_az3', private_cache_subnet_az3.id)
pulumi.export('private_cache_subnet_az4', private_cache_subnet_az4.id)

pulumi.export('private_spare_subnet_az1', private_spare_subnet_az1.id)
pulumi.export('private_spare_subnet_az2', private_spare_subnet_az2.id)
pulumi.export('private_spare_subnet_az3', private_spare_subnet_az3.id)
pulumi.export('private_spare_subnet_az4', private_spare_subnet_az4.id)

pulumi.export('internet_gateway', internet_gateway.id)

pulumi.export('route_table_public', route_table_public.id)
'''