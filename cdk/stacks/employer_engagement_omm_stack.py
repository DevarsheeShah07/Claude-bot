
"""
Employer Engagement Omm Stack - Generic Components
"""

from aws_cdk import (
    Environment,
    Stack,
    aws_lambda as _lambda,
    aws_glue as _glue,
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


class EmployerEngagementOmmStack(Stack):
    """Defines AWS infrastructure components for the Employer Engagement Omm module within the IRIS Platform project"""

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

        edb_landing_to_raw_employer_omm_put_event_rule = _events.Rule(
            self,
            "edbLandingToRawEmployerOmmPutEventBridgeRule",
            rule_name="edb_landing_to_raw_employer_omm_put_event_rule",
            description="Event bridge rule for mapping landing put EMPLOYER OMM object events to EDB Landing to Raw lambda.",
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
                            {"prefix": "omm_9am/lilly_rx/data/inbox"},
                            {"prefix": "omm_9am/comp_rx/data/inbox"},
                            {"prefix": "omm_9am/client_list/data/inbox"},
                            {"prefix": "omm_andel/lilly_rx/data/inbox"},
                            {"prefix": "omm_andel/comp_rx/data/inbox"},
                            {"prefix": "omm_andel/client_list/data/inbox"},
                            {"prefix": "omm_calibrate/lilly_rx/data/inbox"},
                            {"prefix": "omm_calibrate/comp_rx/data/inbox"},
                            {"prefix": "omm_calibrate/client_list/data/inbox"},
                            {"prefix": "omm_crux/lilly_rx/data/inbox"},
                            {"prefix": "omm_crux/comp_rx/data/inbox"},
                            {"prefix": "omm_crux/client_list/data/inbox"},
                            {"prefix": "omm_emed/lilly_rx/data/inbox"},
                            {"prefix": "omm_emed/comp_rx/data/inbox"},
                            {"prefix": "omm_emed/client_list/data/inbox"},
                            {"prefix": "omm_flyte/lilly_rx/data/inbox"},
                            {"prefix": "omm_flyte/comp_rx/data/inbox"},
                            {"prefix": "omm_flyte/client_list/data/inbox"},
                            {"prefix": "omm_form/lilly_rx/data/inbox"},
                            {"prefix": "omm_form/comp_rx/data/inbox"},
                            {"prefix": "omm_form/client_list/data/inbox"},
                            {"prefix": "omm_goodpath/lilly_rx/data/inbox"},
                            {"prefix": "omm_goodpath/comp_rx/data/inbox"},
                            {"prefix": "omm_goodpath/client_list/data/inbox"},
                            {"prefix": "omm_ilant/lilly_rx/data/inbox"},
                            {"prefix": "omm_ilant/comp_rx/data/inbox"},
                            {"prefix": "omm_ilant/client_list/data/inbox"},
                            {"prefix": "omm_onsera/lilly_rx/data/inbox"},
                            {"prefix": "omm_onsera/comp_rx/data/inbox"},
                            {"prefix": "omm_onsera/client_list/data/inbox"},
                            {"prefix": "omm_salta/lilly_rx/data/inbox"},
                            {"prefix": "omm_salta/comp_rx/data/inbox"},
                            {"prefix": "omm_salta/client_list/data/inbox"},
                            {"prefix": "omm_waltz/lilly_rx/data/inbox"},
                            {"prefix": "omm_waltz/comp_rx/data/inbox"},
                            {"prefix": "omm_waltz/client_list/data/inbox"},
                        ],
                    },
                },
            ),
        )

        edb_landing_to_raw_employer_eng_omm_put_event_rule = _events.Rule(
            self,
            "edbLandingToRawEmployerEngOmmPutEventBridgeRule",
            rule_name="edb_landing_to_raw_employer_eng_omm_put_event_rule",
            description="Event bridge rule for mapping landing put EMPLOYER OMM object events to EDB Landing to Raw lambda.",
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
                            {"prefix": "omm_costplus/lilly_rx/data/inbox"},
                            {"prefix": "omm_costplus/comp_rx/data/inbox"},
                            {"prefix": "omm_costplus/client_list/data/inbox"},
                            {"prefix": "omm_revive/lilly_rx/data/inbox"},
                            {"prefix": "omm_revive/comp_rx/data/inbox"},
                            {"prefix": "omm_revive/client_list/data/inbox"},
                            {"prefix": "omm_teladoc/lilly_rx/data/inbox"},
                            {"prefix": "omm_teladoc/comp_rx/data/inbox"},
                            {"prefix": "omm_teladoc/client_list/data/inbox"},
                            {"prefix": "omm_goodrx/lilly_rx/data/inbox"},
                            {"prefix": "omm_goodrx/comp_rx/data/inbox"},
                            {"prefix": "omm_goodrx/client_list/data/inbox"},
                            {"prefix": "omm_sesame/lilly_rx/data/inbox"},
                            {"prefix": "omm_sesame/comp_rx/data/inbox"},
                            {"prefix": "omm_sesame/client_list/data/inbox"},
                            {"prefix": "omm_transcarent/client_list/data/inbox"},
                            {"prefix": "omm_transcarent/lilly_rx/data/inbox"},
                            {"prefix": "omm_transcarent/comp_rx/data/inbox"},                          
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
        edb_landing_to_raw_employer_omm_put_event_rule.add_target(
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

        edb_landing_to_raw_employer_eng_omm_put_event_rule.add_target(
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

        ## commenting this code out because generic raw to refined lambda has reached its EB rule limit thus we are unable to add it as target added the prefixes in the generic stack##
        # edb_iris_raw_s3_processRawFile= _lambda.Function.from_function_arn(
        #     self,
        #     "edbRawtoRefinedLambda",
        #     f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile",
        # )

        # # EventBridge Rule for mapping Raw put object events to raw-refined lambda
        # s3_raw_employer_omm_put_event_rule = _events.Rule(
        #     self,
        #     "edbIrisS3RawEMPLOYEROMMPutEventBridgeRule",
        #     rule_name="edb-iris-s3-raw-employer-omm-put-event-rule",
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
        #                     {"prefix": "omm_9am/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_9am/comp_rx/data/inbox"},
        #                     {"prefix": "omm_9am/client_list/data/inbox"},
        #                     {"prefix": "omm_andel/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_andel/comp_rx/data/inbox"},
        #                     {"prefix": "omm_andel/client_list/data/inbox"},
        #                     {"prefix": "omm_calibrate/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_calibrate/comp_rx/data/inbox"},
        #                     {"prefix": "omm_calibrate/client_list/data/inbox"},
        #                     {"prefix": "omm_crux/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_crux/comp_rx/data/inbox"},
        #                     {"prefix": "omm_crux/client_list/data/inbox"},
        #                     {"prefix": "omm_emed/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_emed/comp_rx/data/inbox"},
        #                     {"prefix": "omm_emed/client_list/data/inbox"},
        #                     {"prefix": "omm_flyte/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_flyte/comp_rx/data/inbox"},
        #                     {"prefix": "omm_flyte/client_list/data/inbox"},
        #                     {"prefix": "omm_form/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_form/comp_rx/data/inbox"},
        #                     {"prefix": "omm_form/client_list/data/inbox"},
        #                     {"prefix": "omm_goodpath/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_goodpath/comp_rx/data/inbox"},
        #                     {"prefix": "omm_goodpath/client_list/data/inbox"},
        #                     {"prefix": "omm_ilant/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_ilant/comp_rx/data/inbox"},
        #                     {"prefix": "omm_ilant/client_list/data/inbox"},
        #                     {"prefix": "omm_onsera/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_onsera/comp_rx/data/inbox"},
        #                     {"prefix": "omm_onsera/client_list/data/inbox"},
        #                     {"prefix": "omm_salta/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_salta/comp_rx/data/inbox"},
        #                     {"prefix": "omm_salta/client_list/data/inbox"},
        #                     {"prefix": "omm_waltz/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_waltz/comp_rx/data/inbox"},
        #                     {"prefix": "omm_waltz/client_list/data/inbox"},
        #                     {"prefix": "judy_diamond_form55/rhm_map/data/inbox"},
        #                 ],
        #             },
        #         },
        #     ),
        # )

        # s3_raw_employer_eng_omm_put_event_rule = _events.Rule(
        #     self,
        #     "edbIrisS3RawEMPLOYERENGOMMPutEventBridgeRule",
        #     rule_name="edb-iris-s3-raw-employer-eng-omm-put-event-rule",
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
        #                     {"prefix": "omm_costplus/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_costplus/comp_rx/data/inbox"},
        #                     {"prefix": "omm_costplus/client_list/data/inbox"},
        #                     {"prefix": "omm_revive/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_revive/comp_rx/data/inbox"},
        #                     {"prefix": "omm_revive/client_list/data/inbox"},
        #                     {"prefix": "omm_teladoc/lilly_rx/data/inbox"},
        #                     {"prefix": "omm_teladoc/comp_rx/data/inbox"},
        #                     {"prefix": "omm_teladoc/client_list/data/inbox"},
        #                 ],
        #             },
        #         },
        #     ),
        # )

        # # Add lambda as a target to the EB rule
        # s3_raw_employer_omm_put_event_rule.add_target(
        #     _targets.LambdaFunction(edb_iris_raw_s3_processRawFile)
        # )

        # # Add lambda as a target to the new EB rule
        # s3_raw_employer_eng_omm_put_event_rule.add_target(
        #     _targets.LambdaFunction(edb_iris_raw_s3_processRawFile)
        # )

        # # Add a permisson to update the lambda's resource policy to allow EB rule to invoke the lambda
        # _lambda.CfnPermission(
        #     self,
        #     "EMPLOYEROMMRawRefinedLambdaInvokePermission",
        #     action="lambda:InvokeFunction",
        #     function_name=f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile",
        #     principal="events.amazonaws.com",
        #     source_arn=s3_raw_employer_omm_put_event_rule.rule_arn,
        # )

        # _lambda.CfnPermission(
        #     self,
        #     "EMPLOYERENGOMMRawRefinedLambdaInvokePermission",
        #     action="lambda:InvokeFunction",
        #     function_name=f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile",
        #     principal="events.amazonaws.com",
        #     source_arn=s3_raw_employer_eng_omm_put_event_rule.rule_arn,
        # )

        
        # Define all Glue jobs in a list of tuples (ID suffix, job name)
        glue_jobs = [
            ("Omm9amLillyRx", "omm_9am_lilly_rx"),
            ("Omm9amCompRx", "omm_9am_comp_rx"),
            ("Omm9amClientList", "omm_9am_client_list"),
            ("OmmAndelLillyRx", "omm_andel_lilly_rx"),
            ("OmmAndelCompRx", "omm_andel_comp_rx"),
            ("OmmAndelClientList", "omm_andel_client_list"),
            ("OmmCalibrateLillyRx", "omm_calibrate_lilly_rx"),
            ("OmmCalibrateCompRx", "omm_calibrate_comp_rx"),
            ("OmmCalibrateClientList", "omm_calibrate_client_list"),
            ("OmmCruxLillyRx", "omm_crux_lilly_rx"),
            ("OmmCruxCompRx", "omm_crux_comp_rx"),
            ("OmmCruxClientList", "omm_crux_client_list"),
            ("OmmEmedLillyRx", "omm_emed_lilly_rx"),
            ("OmmEmedCompRx", "omm_emed_comp_rx"),
            ("OmmEmedClientList", "omm_emed_client_list"),
            ("OmmFlyteLillyRx", "omm_flyte_lilly_rx"),
            ("OmmFlyteCompRx", "omm_flyte_comp_rx"),
            ("OmmFlyteClientList", "omm_flyte_client_list"),
            ("OmmFormLillyRx", "omm_form_lilly_rx"),
            ("OmmFormCompRx", "omm_form_comp_rx"),
            ("OmmFormClientList", "omm_form_client_list"),
            ("OmmGoodpathLillyRx", "omm_goodpath_lilly_rx"),
            ("OmmGoodpathCompRx", "omm_goodpath_comp_rx"),
            ("OmmGoodpathClientList", "omm_goodpath_client_list"),
            ("OmmIlantLillyRx", "omm_ilant_lilly_rx"),
            ("OmmIlantCompRx", "omm_ilant_comp_rx"),
            ("OmmIlantClientList", "omm_ilant_client_list"),
            ("OmmCostplusLillyRx", "omm_costplus_lilly_rx"),
            ("OmmCostplusCompRx", "omm_costplus_comp_rx"),
            ("OmmCostplusClientList", "omm_costplus_client_list"),
            ("OmmOnseraLillyRx", "omm_onsera_lilly_rx"),
            ("OmmOnseraCompRx", "omm_onsera_comp_rx"),
            ("OmmOnseraClientList", "omm_onsera_client_list"),
            ("OmmSaltaLillyRx", "omm_salta_lilly_rx"),
            ("OmmSaltaCompRx", "omm_salta_comp_rx"),
            ("OmmSaltaClientList", "omm_salta_client_list"),
            ("OmmWaltzLillyRx", "omm_waltz_lilly_rx"),
            ("OmmWaltzCompRx", "omm_waltz_comp_rx"),
            ("OmmWaltzClientList", "omm_waltz_client_list"),
            ("OmmReviveLillyRx", "omm_revive_lilly_rx"),
            ("OmmReviveCompRx", "omm_revive_comp_rx"),
            ("OmmReviveClientList", "omm_revive_client_list"),
            ("OmmTeladocLillyRx", "omm_teladoc_lilly_rx"),
            ("OmmTeladocCompRx", "omm_teladoc_comp_rx"),
            ("OmmTeladocClientList", "omm_teladoc_client_list"),
            ("OmmGoodrxLillyRx", "omm_goodrx_lilly_rx"),
            ("OmmGoodrxCompRx", "omm_goodrx_comp_rx"),
            ("OmmGoodrxClientList", "omm_goodrx_client_list"),
            ("OmmSesameLillyRx", "omm_sesame_lilly_rx"),
            ("OmmSesameCompRx", "omm_sesame_comp_rx"),
            ("OmmSesameClientList", "omm_sesame_client_list"),
            ("OmmTranscarentLillyRx", "omm_transcarent_lilly_rx"),
            ("OmmTranscarentCompRx", "omm_transcarent_comp_rx"),
            ("OmmTranscarentClientList", "omm_transcarent_client_list"),
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

        employer_engagement_judy_diamond_form55_rhm_map = IrisRawToRefinedGlueJob(
            self,
            id='edbIrisRawToRefinedEmployerEngagementJudyDiamondForm55RhmMap',
            name='edb_iris_raw_to_refined_judy_diamond_form55_rhm_map',
            env=env,
            artifact_bucket=artifact_bucket,
            config=config
        ).Jobv1
        

