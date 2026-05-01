# pylint: disable=too-many-arguments,too-many-locals,too-many-statements,unused-argument,too-many-lines,import-error

"""
Employer Engagement Stack - Generic Components
"""

import os
import boto3
from aws_cdk import (
    Environment,
    Stack,
    aws_logs,
    CfnOutput,
    aws_lambda as _lambda,
    aws_glue as _glue,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as _ec2,
    Duration as _duration,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_stepfunctions as _stepfunctions
)
from constructs import Construct
from cdk.lib.build_config import BuildConfig
from cdk.lib.iris_raw_to_refined_glue_job import IrisRawToRefinedGlueJob


class EmployerEngagementStack(Stack):
    """Defines AWS infrastructure components for the Employer Engagement module within the IRIS Platform project"""

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

        glue_params = config.load_stack_params_file("params.glue.json")

        service_role = iam.Role.from_role_name(
            self, "iris_service_role", role_name="edb_buids_iris_service_role"
        )


        s3_bucket = s3.Bucket.from_bucket_arn(
            self, "Bucket", bucket_arn=f"arn:aws:s3:::{artifact_bucket.bucket_name}"
        )

        lambda_client = boto3.client("lambda")

        edb_landing_to_raw_employer_put_event_rule = _events.Rule(
            self,
            "edbLandingToRawEmployerPutEventBridgeRule",
            rule_name="edb-landing-to-raw-employer-put-event-rule",
            description="Event bridge rule for mapping landing files from Pharmacy files (centerwell and Healthdyne) events to EDB Landing to Raw Bucket.",
            enabled=True,
            event_pattern=_events.EventPattern(
                source=["aws.s3"],
                detail_type=["AWS API Call via CloudTrail"],
                detail={
                    "eventSource": ["s3.amazonaws.com"],
                    "eventName": ["PutObject", "CopyObject", "CompleteMultipartUpload"],
                    "requestParameters": {
                        "bucketName": [config.edb_landing_bucket],
                        "key": [
                            {"prefix": "centerwell/patient/data/inbox"},
                            {"prefix": "centerwell/fulfillment_dispensing/data/inbox"},
                            {"prefix": "centerwell/shipment/data/inbox"},
                            {"prefix": "centerwell/inventory/data/inbox"},
                            {"prefix": "centerwell/shipment_fill_request/data/inbox"},
                            {"prefix": "centerwell/audit/data/inbox"},
                            {"prefix": "centerwell/prescription/data/inbox"},
                            {"prefix": "centerwell/prescriber/data/inbox"},
                            {"prefix": "healthdyne/patient/data/inbox"},
                            {"prefix": "healthdyne/fulfillment_dispensing/data/inbox"},
                            {"prefix": "healthdyne/shipment/data/inbox"},
                            {"prefix": "healthdyne/inventory/data/inbox"},
                            {"prefix": "healthdyne/shipment_fill_request/data/inbox"},
                            {"prefix": "healthdyne/audit/data/inbox"},
                            {"prefix": "healthdyne/prescription/data/inbox"},
                            {"prefix": "healthdyne/prescriber/data/inbox"},
                            
                        ],
                    },
                },
            ),
        )

        edb_core_landing_to_raw_lambda = _lambda.Function.from_function_arn(
            self,
            "edbCoreLandingToRawLambda",
            f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_core_landing_to_raw_lambda",
        )

        # Add lambda as a target to the EB rule
        edb_landing_to_raw_employer_put_event_rule.add_target(
            _targets.LambdaFunction(
                edb_core_landing_to_raw_lambda,
                event=_events.RuleTargetInput.from_object(
                    {
                        "detail": _events.EventField.from_path("$.detail"),
                        "config_file": "iris/Landing_to_Raw_Lambda_2.0/landing_to_raw_employer_config.json",
                    }
                ),
            )
        )

        # edb_iris_raw_s3_processRawFile= _lambda.Function.from_function_arn(
        #     self,
        #     "edbRawtoRefinedLambda",
        #     f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile",
        # )

        # # EventBridge Rule for mapping Raw put object events to raw-refined lambda
        # s3_raw_employer_put_event_rule = _events.Rule(
        #     self,
        #     "edbIrisS3RawEMPLOYERPutEventBridgeRule",
        #     rule_name="edb-iris-s3-raw-employer-put-event-rule",
        #     description="Event bridge rule for mapping Raw put object events to raw-refined lambda",
        #     enabled=True,
        #     event_pattern=_events.EventPattern(
        #         source=["aws.s3"],
        #         detail_type=["AWS API Call via CloudTrail"],
        #         detail={
        #             "eventSource": ["s3.amazonaws.com"],
        #             "eventName": ["PutObject", "CopyObject", "CompleteMultipartUpload"],
        #             "requestParameters": {
        #                 "bucketName": [config.edb_raw_bucket],
        #                 "key": [
        #                     {"prefix": "centerwell/patient/data/inbox"},
        #                     {"prefix": "centerwell/fulfillment_dispensing/data/inbox"},
        #                     {"prefix": "centerwell/shipment/data/inbox"},
        #                     {"prefix": "centerwell/inventory/data/inbox"},
        #                     {"prefix": "centerwell/shipment_fill_request/data/inbox"},
        #                     {"prefix": "centerwell/audit/data/inbox"},
        #                     {"prefix": "centerwell/prescription/data/inbox"},
        #                     {"prefix": "centerwell/prescriber/data/inbox"},
        #                     {"prefix": "healthdyne/patient/data/inbox"},
        #                     {"prefix": "healthdyne/fulfillment_dispensing/data/inbox"},
        #                     {"prefix": "healthdyne/shipment/data/inbox"},
        #                     {"prefix": "healthdyne/inventory/data/inbox"},
        #                     {"prefix": "healthdyne/shipment_fill_request/data/inbox"},
        #                     {"prefix": "healthdyne/audit/data/inbox"},
        #                     {"prefix": "healthdyne/prescription/data/inbox"},
        #                     {"prefix": "healthdyne/prescriber/data/inbox"},
        #                     {"prefix": "judy_diamond_form55/Broker/data/inbox"},
        #                     {"prefix": "judy_diamond_form55/Filing/data/inbox"},
        #                 ],
        #             },
        #         },
        #     ),
        # )

        # # Add lambda as a target to the EB rule
        # s3_raw_employer_put_event_rule.add_target(
        #     _targets.LambdaFunction(edb_iris_raw_s3_processRawFile)
        # )

        # # Add a permisson to update the lambda's resource policy to allow EB rule to invoke the lambda
        # _lambda.CfnPermission(
        #     self,
        #     "EMPLOYERRawRefinedLambdaInvokePermission",
        #     action="lambda:InvokeFunction",
        #     function_name=f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile",
        #     principal="events.amazonaws.com",
        #     source_arn=s3_raw_employer_put_event_rule.rule_arn,
        # )
        
        # Define all Glue jobs in a list of tuples (ID suffix, job name)
        glue_jobs = [
            ("CenterwellPatient", "centerwell_patient"),
            ("CenterwellFulfillmentDispensing", "centerwell_fulfillment_dispensing"),
            ("CenterwellShipment", "centerwell_shipment"),
            ("CenterwellInventory", "centerwell_inventory"),
            ("CenterwellShipmentFillRequest", "centerwell_shipment_fill_request"),
            ("CenterwellAudit", "centerwell_audit"),
            ("CenterwellPrescription", "centerwell_prescription"),
            ("CenterwellPrescriber", "centerwell_prescriber"),
            ("HealthdynePatient", "healthdyne_patient"),
            ("HealthdyneFulfillmentDispensing", "healthdyne_fulfillment_dispensing"),
            ("HealthdyneShipment", "healthdyne_shipment"),
            ("HealthdyneInventory", "healthdyne_inventory"),
            ("HealthdyneShipmentFillRequest", "healthdyne_shipment_fill_request"),
            ("HealthdyneAudit", "healthdyne_audit"),
            ("HealthdynePrescription", "healthdyne_prescription"),
            ("HealthdynePrescriber", "healthdyne_prescriber")
        ]
        # Loop through and create Glue jobs dynamically
        for job_id_suffix, job_name in glue_jobs:
            IrisRawToRefinedGlueJob(
                self,
                id=f"edbIrisRawToRefinedEmployerEngagement{job_id_suffix}",
                name=f"edb_iris_raw_to_refined_{job_name}",
                env=env,
                artifact_bucket=artifact_bucket,
                config=config
            ).Jobv1



            
        employer_engagement_judy_diamond_form55_broker = IrisRawToRefinedGlueJob(
            self,
            id='edbIrisRawToRefinedEmployerEngagementJudyDiamondForm55Broker',
            name='edb_iris_raw_to_refined_judy_diamond_form55_Broker',
            env=env,
            artifact_bucket=artifact_bucket,
            config=config
        ).Jobv1

        employer_engagement_judy_diamond_form55_filing = IrisRawToRefinedGlueJob(
            self,
            id='edbIrisRawToRefinedEmployerEngagementJudyDiamondForm55Filing',
            name='edb_iris_raw_to_refined_judy_diamond_form55_Filing',
            env=env,
            artifact_bucket=artifact_bucket,
            config=config
        ).Jobv1
		
        employer_engagement_judy_diamond_form55_Industry_Mapping = IrisRawToRefinedGlueJob(
            self,
            id='edbIrisRawToRefinedEmployerEngagementJudyDiamondForm55IndustryMapping',
            name='edb_iris_raw_to_refined_judy_diamond_form55_Industry_Mapping',
            env=env,
            artifact_bucket=artifact_bucket,
            config=config
        ).Jobv1
