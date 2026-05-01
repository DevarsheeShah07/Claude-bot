# pylint: disable=too-many-arguments,too-many-locals,too-many-statements,unused-argument,too-many-lines,import-error
"""
IRIS Service Role  Stack - for removing duplicate permission to IRIS service Role Artifact bucket
"""

from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_s3 as s3
)

from constructs import Construct
from cdk.lib.build_config import BuildConfig

class irisservicerole(Stack):
    '''class for creating of IRIS Vendor Extract project components'''

    def __init__(self, scope: Construct, construct_id: str, *, config: BuildConfig, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.iris_artifact_bucket = s3.Bucket.from_bucket_arn(
            self, "ArtifactBucket", bucket_arn=f"arn:aws:s3:::{config.artifact_bucket}"
        )

        service_role = iam.Role.from_role_name(self, "iris_service_role", role_name="edb_buids_iris_service_role")

        # Group 1: Core prefixes for list bucket operations
        allowed_prefixes_group1 = [
            "finance-g2n-*",
            "glue/*",
            "iceberg/*",
            "inovacore/*",
            "iris*",
            "job_logs/*",
            "lambda/*",
            "lasre/*",
            "lib/*",
        ]

        # Group 2: Additional prefixes
        allowed_prefixes_group2 = [
            "lly-pipeline-artifacts-*",
            "models/*",
            "pipeline-*",
            "prefect/*",
            "processed_alerts/*",
            "Unsaved/*",
            "VEEVA_URGENT_FILES/*",
            "flow_dynamic_single_job_public.py",
            "input_file_queries.sql",
        ]

        all_prefixes = allowed_prefixes_group1 + allowed_prefixes_group2

        object_arns = [
            self.iris_artifact_bucket.arn_for_objects(p)
            for p in all_prefixes
        ]

        # Use a managed policy instead of an inline policy to stay under the
        # AWS IAM 10,240-byte combined inline-policy-per-role quota.
        # The role already carries several inline policies from other stacks;
        # moving this one to a managed policy keeps the inline total within
        # limits while the managed-policy count stays well below the 20-per-role
        # default quota.
        object_policy = iam.ManagedPolicy(
            self,
            "IrisServiceRoleS3ObjectPolicy",
            managed_policy_name=f"iris-service-role-s3-objects-{config.env}",
            statements=[
                iam.PolicyStatement(
                    sid="ReadWriteAllowedObjects",
                    actions=[
                        "s3:GetObject",
                        "s3:GetObjectVersion",
                        "s3:PutObject",
                        "s3:AbortMultipartUpload",
                        "s3:ListMultipartUploadParts",
                        "s3:ListBucket"
                    ],
                    resources=object_arns
                )
            ],
            roles=[service_role]
        )
