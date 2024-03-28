import pulumi_aws as aws


from config import (
    project_name,
    environment,
    owner,
)


# Create an IAM role for VPC Flow Logs
flow_log_role = aws.iam.Role(
    resource_name = f'{project_name}-{environment}-vpc-flow-logs-role',
    assume_role_policy = json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Sid": "",
                    "Principal": {
                        "Service": "vpc-flow-logs.amazonaws.com",
                    },
                }
            ],
        }
    ),
    tags = {
        'Name': f'{project_name}-{environment}-vpc-flow-logs-role',
        'Owner': owner,
        'Project': project_name,
        'Environment': environment,
    },
)

flow_log_role_policy = aws.iam.RolePolicy('flow-log-role-policy',
    role=flow_log_role.id,
    policy=flow_log_policy_document.json
)

# Crear una política de IAM que permita escribir en el bucket y asociarla con el rol.
flow_log_policy = aws.iam.RolePolicy("flowLogPolicy",
    role=flow_log_role.id,
    policy=s3_bucket.arn.apply(lambda arn: json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": f"{arn}/*"
        }]
    }))
)

# Attach a policy to the role that allows publishing to CloudWatch Logs
flow_log_policy = aws.iam.RolePolicy("flowLogPolicy",
    role=flow_log_role.id,
    policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents",
                    "logs:DescribeLogGroups",
                    "logs:DescribeLogStreams"
                ],
                "Effect": "Allow",
                "Resource": "*"
            }
        ]
    }""")



# Crear un Flow Log para el VPC y configurar la entrega de registros al bucket de S3
flow_log = aws.ec2.FlowLog("vpc-flow-log",
    iam_role_arn=flow_log_role.arn,
    log_destination=flow_log_bucket.arn,
    log_destination_type="s3",
    traffic_type="ALL",
    vpc_id=vpc.id
)