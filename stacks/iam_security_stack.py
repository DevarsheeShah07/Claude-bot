import cdk_nag
from aws_cdk import (
    Duration,
    Aspects,
    Environment,
    PhysicalName,
    SecretValue,
    Stack,
    aws_iam as iam,
    aws_kms as kms,
    aws_logs as logs,
    aws_s3 as s3,
    aws_secretsmanager as sm
)
from constructs import Construct
from cdk.lib.build_config import BuildConfig
from cdk.lib.aspects import *


class IamStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *, config: BuildConfig, env: Environment, artifact_bucket: s3.IBucket, **kwargs) -> None:
        super().__init__(scope, construct_id, env=env, **kwargs)

        iris_platform_lambda_execution_service_role = iam.Role.from_role_name(self, 'iris_platform_lambda_execution_service_role', role_name=f'Iris-Platform-LambdaExecutionRole-{config.env}')

        iam.Policy(
            self, "IrisPlatformLambdaVpcPolicy11",
            roles=[iris_platform_lambda_execution_service_role],
            statements=[
                iam.PolicyStatement(
                    actions=[
                        "ec2:AssignPrivateIpAddresses",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DescribeNetworkInterfaces",
                        "ec2:DescribeSecurityGroups",
                        "ec2:DescribeSubnets",
                        "ec2:DescribeVpcs",
                        "ec2:UnassignPrivateIpAddresses"
                    ],
                    effect=iam.Effect.ALLOW,
                    resources=["*"]
                )
            ]
        )    

        # self.iam_artifact_bucket_rw_policy = iam.ManagedPolicy(
        #     self, 'iris-artifact-rw-policy',
        #     description='Iris Ecs Service Policy',
        #     document=iam.PolicyDocument(
        #         assign_sids=True,
        #         minimize=True,
        #         statements=[
        #             iam.PolicyStatement(
        #                 actions=['s3:*'],
        #                 effect=iam.Effect.ALLOW,
        #                 resources=[artifact_bucket.arn_for_objects("*")]
        #             )
        #         ]
        #     )
        # )

        # self.ecs_iam_service_policy = iam.ManagedPolicy(
        #     self, 'iris-ecs-service-policy1',
        #     description='Iris ECS Service Policy',
        #     document=iam.PolicyDocument(
        #         assign_sids=True,
        #         minimize=True,
        #         statements=[
        #             iam.PolicyStatement(actions=[
        #                 'ecs:List*',
        #                 'ecs:Describe*',
        #                 'ecr:GetAuthorizationToken',
        #                 "ecr:BatchCheckLayerAvailability",
        #                 "ecr:BatchGetImage",
        #                 'events:Describe*',
        #                 'events:List*',
        #                 'ec2:CreateNetworkInterface',
        #                 'ec2:DeleteNetworkInterface',
        #                 'ec2:Describe*'                        
        #                 ],
        #                 resources=['*']
        #             ),
		# 			iam.PolicyStatement(
        #                 actions=[
        #                     'ecr:GetDownloadUrlForLayer'
        #                 ],
        #                 resources=["arn:aws:ecr:us-east-2:346644684160:repository/edb_iris_*"]
		# 			)
        #         ]
        #     ),
        #     managed_policy_name='iris-ecs-service-policy1'
        # )

        iris_engine_oidc_policy = iam.ManagedPolicy.from_managed_policy_name(
            self,
            "iris-engine-actions-policy",
            managed_policy_name="iris-engine-actions-policy",
        )

        self.iris_aet_oidc_cf_policy = iam.ManagedPolicy(
            self,
            "iris-aet-cf-policy",
            description="Define Cloudformation access the GitHub Actions Role has for AET",
            document=iam.PolicyDocument(
                assign_sids=True,
                minimize=True,
                statements=[
                    iam.PolicyStatement(
                        actions=["cloudformation:CreateChangeSet",
                                "cloudformation:CreateStackSet",
                                "cloudformation:CreateStackInstances",
                                "cloudformation:DeleteChangeSet",
                                "cloudformation:DeleteStackInstances",
                                "cloudformation:DeleteStackSet",
                                "cloudformation:Describe*",
                                "cloudformation:ExecuteChangeSet",
                                "cloudformation:Get*",
                                "cloudformation:List*",
                                "cloudformation:UpdateStackSet",
                                "cloudformation:TagResource",
                                "cloudformation:ValidateTemplate"],
                        resources=[f"arn:aws:cloudformation:{env.region}:{env.account}:stack/AetCdkStack*"]
                    ),
                    # iam.PolicyStatement(
                    #     actions=["cloudformation:DeleteStack"],
                    #     resources=[f"arn:aws:cloudformation:{env.region}:{env.account}:stack/AetCdkStack*"]
                    # )
                ],
            ),
            managed_policy_name="iris-aet-cf-policy", 
        )

        lilly_iam_boundary = iam.ManagedPolicy.from_managed_policy_name(
            self, "lz-iam-boundry", "LZ-IAM-Boundary"
        )
		
        iam.Role(
            self,
            "IrisGHOIDCRole_AET",
            assumed_by=iam.CompositePrincipal(
                iam.ServicePrincipal("cloudformation.amazonaws.com"),
                iam.FederatedPrincipal(
                    f"arn:aws:iam::{env.account}:saml-provider/LillyUserAPIGW",
                    assume_role_action="sts:AssumeRoleWithSAML",
                    conditions={
                        "StringEquals": {
                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                        }
                    },
                ),
                iam.FederatedPrincipal(
                    f"arn:aws:iam::{env.account}:oidc-provider/token.actions.githubusercontent.com",
                    assume_role_action="sts:AssumeRoleWithWebIdentity",
                    conditions={
                        "StringLike": {
                            "token.actions.githubusercontent.com:sub": f"repo:EliLillyCo/lusa-automated-enhancement-tool:environment:{config.env}"
                        },
                        "ForAllValues:StringEquals": {
                            "token.actions.githubusercontent.com:iss": "https://token.actions.githubusercontent.com",
                            "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
                        },
                    },
                ),
            ),
            managed_policies=[iris_engine_oidc_policy,self.iris_aet_oidc_cf_policy],
            max_session_duration=Duration.hours(10),
            permissions_boundary=lilly_iam_boundary,
            role_name="IAMRoleForGithubOIDC_AET",
        )
