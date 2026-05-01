# Employer Engagement (Datavant) stack includes Secrets Manager, ECS Cluster, Task definition, Security group

"""
Who: Devarshee Shah
When : 13-04-2026
Why: Requirement for Datavant
"""

"""
Datavant Stack Architecture:

S3 inbox file lands
      ↓
EventBridge Rule fires ("Object Created" on healthdyne/ or centerwell/ prefix)
      ↓
Lambda: edb_iris_DatavantTriggerLambda (reads key → decides partner)
      ↓
ecs:RunTask → CenterwellTask OR HealthdyneTask (Fargate, 4vCPU / 8GB)
      ↓
Datavant CLI container runs token transform (reads inbox, writes to processed/)
      ↓
Logs → CloudWatch /ecs/datavant

"""

import os
import json
from aws_cdk import (
    Environment,
    Stack,
    aws_logs,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as _ec2,
    aws_ecs as ecs,
    aws_stepfunctions as _stepfunctions
    Duration as _duration,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_secretsmanager as sm,
    SecretValue
)
from constructs import Construct
from cdk.lib.build_config import BuildConfig


class DatavantStack(Stack):
    """Defines AWS infrastructure components for the Datavant module within the IRIS Platform project"""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        config: BuildConfig,
        env:Environment,
        artifact_bucket: s3.IBucket,
        vpc: _ec2.IVpc,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        root_dir = os.path.dirname(os.path.abspath("template.yml"))

        params = config.load_stack_params_file("params.sam.json")

        # glue_params = config.load_stack_params_file("params.glue.json")

        # Datavant IAM Role Import
        datavant_role = iam.Role.from_role_name(
            self,
            "ImportedDatavantRole",
            role_name="edb_data_vant_ecs_task_role"
        )

        # Create a Secrets Manager for credentials
        datavant_secret = sm.Secret(
            self,
            "DatavantB2BSecret",
            secret_name="datavant-b2b-secret",
            secret_object_value={
                "datavant_token": SecretValue.unsafe_plain_text("") # Creates a secret
            }
        )
        datavant_secret.grant_read(datavant_role)   # Grants ECS role permission to read it

        # Create ECS Cluster inside VPC
        # IrisCdkStackdevDatavantStack0086D824-DatavantCluster333BAC2E-WZiVhU0HpanC
        ''' Where IrisCdkStackdev = Stack Name
        DatavantStack0086D824 = Unique hash
        DatavantCluster = Your construct ID
        333BAC2E = Logical ID hash
        WZiVhU0HpanC = Random string for uniqueness
        '''
        cluster = ecs.Cluster(
            self,
            "DatavantCluster",
            vpc=vpc,
            cluster_name="edb_iris_DatavantCluster"
        )
        
        # Create Security Group allowing Outbound traffic
        # Controls network access of ECS tasks. Needs for internet/S3 communication
        # sg-021cdae87921cb782 - IrisCdkStackdevDatavantStack0086D824-DatavantSecurityGroupF22BB0E2-XMKuPjqVKtlC
        sg = _ec2.SecurityGroup(
            self,
            "DatavantSecurityGroup",
            security_group_name="edb_iris_DatavantSecurityGroup",
            vpc=vpc,
            allow_all_outbound=True
        )

        # Cloudwatch Log Group (Stores logs from ECS containers often used for debugging and monitoring execution)
        log_group = aws_logs.LogGroup(
            self,
            "DatavantLogGroup",
            log_group_name="/ecs/datavant",
            retention=aws_logs.RetentionDays.ONE_WEEK
        )
        # allow_all_outbount=True automatically creates
        '''Type: All traffic
            Protocol: All
            Port: All
            Destination: 0.0.0.0/0 (Anywhere IPv4)'''

        # Reusable ECS Task Definition Function
        def create_task(name, command):
            '''Creating ECS fargate task with:
            1) CPU and memory config
            2) Docker image
            3) Command execution
            4) Logging
            5) Secrets injection'''
            task = ecs.FargateTaskDefinition(
                self,
                name,
                cpu=4096,                          # 4 vCPU
                memory_limit_mib=8192,             # 8 GB
                task_role=datavant_role,
                execution_role=datavant_role
            )

            # Container image (pulls image from ECR)
            container = task.add_container(
                name + "-container",
                image=ecs.ContainerImage.from_registry(
                    "709825985650.dkr.ecr.us-east-1.amazonaws.com/datavant/datavant:v4.3.2-manifest"
                ),
                # Command Execution: entry_point + command (Runs Datavant CLI inside container)
                entry_point=["/bin/sh", "-c"],
                command=[command],
                # logging (Sends logs to CloudWatch)
                logging=ecs.LogDrivers.aws_logs(
                    stream_prefix=name,
                    log_group=log_group
                ),
                # Secrets Injection (Injects secret as envt variable)
                secrets={
                    "DV_USER_CREDENTIALS": ecs.Secret.from_secrets_manager(
                        datavant_secret,
                        field="datavant_token"
                    )
                }
            )

            container.add_port_mappings(
            ecs.PortMapping(
                container_port=80, 
                protocol=ecs.Protocol.TCP,
                name="cli-80-tcp",
                app_protocol=ecs.AppProtocol.http
            )
            )

            return task

        # Two ECS tasks (as both have different S3 input/output paths and require separate processing pipelines)
        centerwell_task = create_task(
            "CenterwellTask",
            "/app/Datavant transform-tokens -s elililly_b2b --from centerwell "
            "-i s3://lly-edp-raw-us-east-2-dev/centerwell/datavant/data/inbox/ "
            "-o s3://lly-edp-raw-us-east-2-dev/centerwell/datavant/data/processed/ "
            "--environment-credentials --console-log"
        )

        healthdyne_task = create_task(
            "HealthdyneTask",
            "/app/Datavant transform-tokens -s elililly_b2b --from healthdyne "
            "-i s3://lly-edp-raw-us-east-2-dev/healthdyne/datavant/data/inbox/ "
            "-o s3://lly-edp-raw-us-east-2-dev/healthdyne/datavant/data/processed/ "
            "--environment-credentials --console-log"
        )

        '''Step 12: Run Datavant container by running a task in your ECS cluster,
        specifying the task definition, networking, security group, and the command to execute.
        # ECS Run Task Configuration includes:
        1) Subnets
        2) Security Group
        3) Public IP
        4) Cluster
        5) Task Definition
        # We would be using Lambda to trigger ECS when file lands in S3.'''
        trigger_lambda = _lambda.Function(
            self,
            "DatavantTriggerLambda",
            function_name="edb_iris_DatavantTriggerLambda",
            runtime=_lambda.Runtime.PYTHON_3_9, # Specifies Python 3.9 as execution envt (3_11 can be used or not is ?)
            handler="index.lambda_handler",            # file is index.py and function is handler(). Tells which code to run when Lambda is triggered
            code=_lambda.Code.from_asset(f"{root_dir}/lambda/edb_iris_employer_engagement_datavant"), # Uploads local folder to Lambda
            role=datavant_role,                      # Using pre-existing Datavant role
            timeout=_duration.seconds(60),      # Lambda can run max 60 seconds
            environment={
                "CLUSTER": cluster.cluster_name,
                "TASK_DEF_CENTERWELL": centerwell_task.task_definition_arn,
                "TASK_DEF_HEALTHDYNE": healthdyne_task.task_definition_arn,
                "SUBNETS": "subnet-08775232140992cbf,subnet-09d46d07d3d9dd777",
                "SECURITY_GROUP": "sg-0263dce6323823f8f"
            }
        )

        # Lambda + ECS Permissions for Datavant role (using iam.Policy since role is imported)
        iam.Policy(
            self,
            "DatavantLambdaPolicy",
            roles=[datavant_role],
            statements=[
                # Lambda basic execution permissions (CloudWatch Logs)
                iam.PolicyStatement(
                    actions=["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                    resources=[f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_DatavantTriggerLambda:*"]
                ),
                # ECS RunTask permission
                iam.PolicyStatement(
                    actions=["ecs:RunTask"],
                    resources=[
                        centerwell_task.task_definition_arn,
                        healthdyne_task.task_definition_arn,
                    ]
                ),
                # IAM PassRole for ECS task execution
                iam.PolicyStatement(
                    actions=["iam:PassRole"],
                    resources=[
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_data_vant_ecs_task_role"
                    ]
                )
            ]
        )

        # Adding eventBridge rule cause we are skipping S3 event notifications
        rule = _events.Rule(
            self,
            "S3ToLambdaEventBridgeRule",
            rule_name="edb_iris_DatavantS3ToLambdaEventBridgeRule",
            event_pattern={
                "source": ["aws.s3"],
                "detail_type": ["Object Created"],
                "detail": {
                    "bucket": {
                        "name": [config.edb_raw_bucket]
                        },
                "object": {
                "key": [
                    {"prefix": "healthdyne/datavant/data/inbox/"},
                    {"prefix": "centerwell/datavant/data/inbox/"}
                        ]
                    }
                }
            }
        )
        rule.add_target(_targets.LambdaFunction(trigger_lambda))

        # S3 → EventBridge -> Lambda Trigger (Triggers lambda when file is uploaded)
        # Grant EventBridge permission to invoke the Lambda (resource-based policy on the Lambda — no new IAM role created)
        trigger_lambda.add_permission(
            "AllowEventBridgeInvoke",
            principal=iam.ServicePrincipal("events.amazonaws.com"),
            action="lambda:InvokeFunction",
            source_arn=rule.rule_arn,
            source_account=config.deploy_env.account
        )
