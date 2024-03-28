import pulumi
import pulumi_aws as aws
from pulumi_aws.config import region

# Read
config = pulumi.Config()

# Retrieve the current region AZs
availableZones = aws.get_availability_zones(state="available")

# Region
aws_region = region

# Available Zones
availability_zone_az1 = availableZones.names[1]
availability_zone_az2 = availableZones.names[2]
availability_zone_az3 = availableZones.names[3]
availability_zone_az4 = availableZones.names[4]

# Project Name
project_name = config.require('project_name') or 'acme'

# Environment
environment = pulumi.get_stack() #config.require('environment') or 'dev'

# Owner
owner = config.require('owner') or 'cysce'

# CIDR block for the VPC.
vpc_cidr = config.require('vpc_cidr') or '10.0.0.0/16'

# Subnets
public_alb_subnet_cidr_az1 = config.require('public_alb_subnet_cidr_az1') or '10.0.32.0/22'
public_alb_subnet_cidr_az2 = config.require('public_alb_subnet_cidr_az2') or '10.0.36.0/22'
public_alb_subnet_cidr_az3 = config.require('public_alb_subnet_cidr_az3') or '10.0.40.0/22'
public_alb_subnet_cidr_az4 = config.require('public_alb_subnet_cidr_az4') or '10.0.44 .0/22'
public_shared_subnet_cidr_az1 = config.require('public_shared_subnet_cidr_az1') or '10.0.48.0/22'
public_shared_subnet_cidr_az2 = config.require('public_shared_subnet_cidr_az2') or '10.0.52.0/22'
public_shared_subnet_cidr_az3 = config.require('public_shared_subnet_cidr_az3') or '10.0.56.0/22'
public_shared_subnet_cidr_az4 = config.require('public_shared_subnet_cidr_az4') or '10.0.60.0/22'
private_app_subnet_cidr_az1 = config.require('private_app_subnet_cidr_az1') or '10.0.0.0/21'
private_app_subnet_cidr_az2 = config.require('private_app_subnet_cidr_az2') or '10.0.8.0/21'
private_app_subnet_cidr_az3 = config.require('private_app_subnet_cidr_az3') or '10.0.16.0/21'
private_app_subnet_cidr_az4 = config.require('private_app_subnet_cidr_az4') or '10.0.24.0/21'
private_db_subnet_cidr_az1 = config.require('private_db_subnet_cidr_az1') or '10.0.80.0/22'
private_db_subnet_cidr_az2 = config.require('private_db_subnet_cidr_az2') or '10.0.84.0/22'
private_db_subnet_cidr_az3 = config.require('private_db_subnet_cidr_az3') or '10.0.88.0/22'
private_db_subnet_cidr_az4 = config.require('private_db_subnet_cidr_az4') or '10.0.92.0/22'
private_keycloak_subnet_cidr_az1 = config.require('private_keycloak_subnet_cidr_az1') or '10.0.96.0/22'
private_keycloak_subnet_cidr_az2 = config.require('private_keycloak_subnet_cidr_az2') or '10.0.100.0/22'
private_keycloak_subnet_cidr_az3 = config.require('private_keycloak_subnet_cidr_az3') or '10.0.104.0/22'
private_keycloak_subnet_cidr_az4 = config.require('private_keycloak_subnet_cidr_az4') or '10.0.108.0/22'
private_kafka_subnet_cidr_az1 = config.require('private_kafka_subnet_cidr_az1') or '10.0.112.0/22'
private_kafka_subnet_cidr_az2 = config.require('private_kafka_subnet_cidr_az2') or '10.0.116.0/22'
private_kafka_subnet_cidr_az3 = config.require('private_kafka_subnet_cidr_az3') or '10.0.120.0/22'
private_kafka_subnet_cidr_az4 = config.require('private_kafka_subnet_cidr_az4') or '10.0.124.0/22'
private_cache_subnet_cidr_az1 = config.require('private_cache_subnet_cidr_az1') or '10.0.128.0/22'
private_cache_subnet_cidr_az2 = config.require('private_cache_subnet_cidr_az2') or '10.0.132.0/22'
private_cache_subnet_cidr_az3 = config.require('private_cache_subnet_cidr_az3') or '10.0.136.0/22'
private_cache_subnet_cidr_az4 = config.require('private_cache_subnet_cidr_az4') or '10.0.140.0/22'
private_spare_subnet_cidr_az1 = config.require('private_spare_subnet_cidr_az1') or '10.0.64.0/22'
private_spare_subnet_cidr_az2 = config.require('private_spare_subnet_cidr_az2') or '10.0.68.0/22'
private_spare_subnet_cidr_az3 = config.require('private_spare_subnet_cidr_az3') or '10.0.72.0/22'
private_spare_subnet_cidr_az4 = config.require('private_spare_subnet_cidr_az4') or '10.0.76.0/22'

# TCP/IP port number used in DB tier for Network ACL (NACL). Default is 3306 for MySQL. Examples; 5432 for PostgreSQL, 1433 for SQL Server, , 11211 for Memcache/Elasticache, 6379 for Redis.
db_tcp_port_number = config.require('db_tcp_port_number') or 3306

domain_name = f"{project_name}.com"