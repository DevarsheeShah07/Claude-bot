import os
import json
from aws_cdk import (
    DefaultStackSynthesizer,
    Environment,
    IAspect,
    Tags
)
from constructs import Construct
import jsii
from ..lib.aspects import *


class IrisSynthesizer(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)
        config = BuildConfig()
        self.synth = DefaultStackSynthesizer(
            # ARN of the role assumed by the CLI and Pipeline to deploy here
            deploy_role_arn=os.environ.get(
                'DEPLOY_ROLE_ARN', f'arn:aws:iam::{config.deploy_env.account}:role/iris-cdk-deploy-role'),

            # Name of the S3 bucket for file assets
            file_assets_bucket_name=config.artifact_bucket,
            bucket_prefix="cdk",

            # ARN of the role used for file asset publishing (assumed from the CLI role)
            file_asset_publishing_role_arn=os.environ.get('DEPLOY_ROLE_ARN'),

            # ARN of the role used for Docker asset publishing (assumed from the CLI role)
            image_asset_publishing_role_arn=os.environ.get('DEPLOY_ROLE_ARN'),

            image_assets_repository_name=f'iris-cdk-container-assets-{config.deploy_env.account}-{config.deploy_env.region}',

            # ARN of the role passed to CloudFormation to execute the deployments
            cloud_formation_execution_role=os.environ.get('DEPLOY_ROLE_ARN'),

            # ARN of the role used to look up context information in an environment
            lookup_role_arn=os.environ.get('DEPLOY_ROLE_ARN'),
        )


@jsii.implements(IAspect)
class BuildConfig:
    root_dir = os.path.dirname(os.path.abspath('template.yml'))
    artifact_bucket = os.environ.get(
        'ARTIFACT_BUCKET', 'lly-pipeline-artifacts-2z7uqh17')
    deploy_env = Environment(
        account=os.environ.get('AWS_ACCOUNT_ID', '346644684160'),
        region=os.environ.get('AWS_REGION', 'us-east-2')
    )
    env = os.environ.get('ENVIRONMENT', 'prd')
    params_file_name_mapping = {
        'dev': 'params.edp-dev.json',
        'qa': 'params.edp-stage-qa.json',
        'prd': 'params.edp-prod.json'
    }
    iris_nodx_accont_mapping = {
        'dev': '184408840178',
        'qa': '551537746916',
        'prd': '572922920319'
    }
    iris_dx_account_mapping = {
        'dev': '098387547573',
        'qa': '593306695065',
        'prd': '998543239731'
    }
    legacy_stack_names = {
        'dev': {
            'athena_stack': 'pipeline-iris-dev-AthenaStack-18PL3GR1CQDXJ',
            'databrew_stack': 'pipeline-iris-dev-DatabrewStack-1K3U69ZFN01I3',
            'glue_stack': 'pipeline-iris-dev-GlueStack-FVVDVAJZ9O64',
            'glue_stack1': 'pipeline-iris-dev-GlueStack1-GHPQLI2PFCL2',
            'lambda_stack': 'pipeline-iris-dev-LambdaStack-1J5R1QXEQU11Z',
            'lambda_stack1': 'pipeline-iris-dev-LambdaStack1-1FW8FQ8JI1CDA'
        },
        'qa': {
            'athena_stack': 'pipeline-iris-code-AthenaStack-550UGVVLVNE',
            'databrew_stack': 'pipeline-iris-code-DatabrewStack-1SHRY5KIA207Z',
            'glue_stack': 'pipeline-iris-code-GlueStack-BSZ7DUQAODBQ',
            'glue_stack1': 'pipeline-iris-code-GlueStack1-1RJ696JEEE7DL',
            'lambda_stack': 'pipeline-iris-code-LambdaStack-K0E9WJ5ZJAXM',
            'lambda_stack1': 'pipeline-iris-code-LambdaStack1-1HDP4QIL47B1P'
        },
        'prd': {
            'athena_stack': 'pipeline-iris-code-AthenaStack-1EQLUATHYCOML',
            'databrew_stack': 'pipeline-iris-code-DatabrewStack-L2IPI6KQOU10',
            'glue_stack': 'pipeline-iris-code-GlueStack-5XRSHF40CBPM',
            'glue_stack1': 'pipeline-iris-code-GlueStack1-15L8I8MTQYUB3',
            'lambda_stack': 'pipeline-iris-code-LambdaStack-L8C93UCKIRB6',
            'lambda_stack1': 'pipeline-iris-code-LambdaStack1-UOQTAO15OWH4'
        }
    }

    prefect_config = {
        "dev": {
            "sso_client_id": "fa9fa062-7973-454c-8f46-06d5936f14d5",
            "cert_arn": "8f0d39aa-abb0-499b-a95b-0295ba08bf29"
        },
        "qa": {
            "sso_client_id": "c4ce0e2a-5272-49a6-bcee-9dd5d273d0e4",
            "cert_arn": "29b1eab0-e311-4699-90ae-99e9e84cf487"
        },
        "prd": {
            "sso_client_id": "bec0e982-c473-4831-bb9f-bbb54edda87c",
            "cert_arn": "96d9030f-a281-4092-b5cc-8492cb5849a3"
        },
        "common_config": {
            "sso_tenant_id": "18a59a81-eea8-4c30-948a-d8824cdc2580",
            "alb_name": f"iris-prefect-server-{env}.aws.lilly.com",
            "asg_events_notify_email": "prefect_edb_buids_iris_operations@elililly.onmicrosoft.com"
        }
    }
    
    prefect_agent_config = {
        "dev": {
            'cpu': 1024,
            'memory': 4096
        },
        "qa": {
            'cpu': 4096,
            'memory': 8192
        },
        "prd": {
            'cpu': 4096,
            'memory': 8192
        }
        }

    prefect_tags = {
    "AppName": "EDB IRIS: Orchestration",
    "CostCenter": "100ARAS",
    "CostCenterApprover": "supancik_kent_a@lilly.com",
    "DeployEnvironment": f"{env}",
    "PrimaryItContact": "strandt_ryan@lilly.com",
    "Level1BusinessArea": "Business Units IDS",
    "DataClassification": "Yellow",
    "Hipaa": "No",
    "SourceGitRepo": "lusa-iris-edb",
    "SystemCustodian": "mhanni@lilly.com",
    "SystemOwner": "vargas_ivan@lilly.com",
    "ApplicationCi": "CI00000060998754"
  }

    jumpserver_sg_id = {
        'qa': 'sg-07681c6c83add061e',
        'prd': 'sg-0ef7ca7f281530c6f'
    }

    iris_layer_versions = {
        'dev': '8486',
        'qa': '12032',
        'prd': '622'
    }

    # Data Quality Automation Variables
    dqa_config = {
        'dev': {
            'dqa_glue_rs_sg': 'sg-0dbce262a22ab8f85',
            'dqa_eip_rs_sg': 'sg-048d082b4a5d70c14',
            'dqa_lambda_rs_sg': 'sg-06a411939f380bdaf',
            'dqa_eip_services_sg': 'sg-082b9d64a5b8d59b7',
            'dqa_rs_jdbc_url': 'jdbc:redshift://iris-edb-dev.cnjndgzifrh0.us-east-2.redshift.amazonaws.com:5439/iris_db',
            'dqa_private_subnets_rs': 'subnet-09c000eace6e879fd'
        },
        'qa': {
            'dqa_glue_rs_sg': 'sg-06195a5d9100814a6',
            'dqa_eip_rs_sg': 'sg-00ed50f8662f45d0b',
            'dqa_lambda_rs_sg': 'sg-02cfd8fc444c9aea3',
            'dqa_eip_services_sg': 'sg-0c037aa6a9dfb4272',
            'dqa_rs_jdbc_url': 'jdbc:redshift://iris-edb-qa.cjlwfm8otbqm.us-east-2.redshift.amazonaws.com:5439/iris_db',
            'dqa_private_subnets_rs': 'subnet-07cda239066f5aae4'
        },
        'prd': {
            'dqa_glue_rs_sg': 'sg-01dbc23e3d2a1715b',
            'dqa_eip_rs_sg': 'sg-0ccdda3ad781cd935',
            'dqa_lambda_rs_sg': 'sg-0bf52390e6eb28a36',
            'dqa_eip_services_sg': 'sg-0259245c39d5d6395',
            'dqa_rs_jdbc_url': 'jdbc:redshift://iris-edb-prd.carpdwnmaayt.us-east-2.redshift.amazonaws.com:5439/iris_db',
            'dqa_private_subnets_rs': 'subnet-09cc5df17821908d7'
        },
        'common_config': {
            'dqa_glue_connection_name': 'edb_iris_dqa_redshift_connection',
            'dqa_service_role': 'edb_buids_iris_dqa_service_role',
            'dqa_glue_db_name': 'iris-dqa-database'
        }
    }

     # AP reporting variables
    ap_config = {
        "dev": {
            "ap_glue_rds_sg": "sg-0b25665300852d07a",
            "ap_rds_jdbc_url": "jdbc:postgresql://edb-lms-refined-dev.c8s6jufr6wh8.us-east-2.rds.amazonaws.com:5432/edb_lms_refined_dev",
            "ap_rds_schema_name": "edb_lms_lnd",
            "ap_secret_name": "edb_lms_refined_rds_secret",
        },
        "qa": {
            "ap_glue_rds_sg": "sg-0b556825fbf72f5f8",
            "ap_rds_jdbc_url": "jdbc:postgresql://edb-lms-lnd-db.cnqphliu94gk.us-east-2.rds.amazonaws.com:5432/edb_lms_lnd_db",
            "ap_rds_schema_name": "edb_lms_lnd",
            "ap_secret_name": "edb_lms_refined_rds_secret",
        },
        "prd": {
            "ap_glue_rds_sg": "sg-05638ee109df27529",
            "ap_rds_jdbc_url": "jdbc:postgresql://edb-lms-lnd-db.cluster-ro-ctpbrjab6xmb.us-east-2.rds.amazonaws.com:5432/edb_lms_lnd_db",
            "ap_rds_schema_name": "edb_lms_lnd",
            "ap_secret_name": "edb_lms_refined_rds_secret",
        },
    }

    
    #SOA variables
    soa_config = {
        'dev': {
            'soa_validation_glue_rs_sg': 'sg-0c014ca2c88866b55',
            'soa_validation_eip_rs_sg': 'sg-0cac5ce08cd7a880b',
            'soa_validation_lambda_rs_sg': 'sg-0bc11dbbcda9846d3',
            'soa_validation_eip_services_sg': 'sg-0c684cbb5c0cad76c',
            'soa_validation_private_subnets_rs': 'subnet-09c000eace6e879fd',
            'soa_validation_rs_jdbc_url': 'jdbc:redshift://iris-edb-dev.cnjndgzifrh0.us-east-2.redshift.amazonaws.com:5439/omnisource',
            'username': 'omnisource_soa_ro',
            'password':'dummy'
        },
        'qa': {
            'soa_validation_glue_rs_sg': 'sg-06195a5d9100814a6',
            'soa_validation_eip_rs_sg': 'sg-00ed50f8662f45d0b',
            'soa_validation_lambda_rs_sg': 'sg-02cfd8fc444c9aea3',
            'soa_validation_eip_services_sg': 'sg-0c037aa6a9dfb4272',
            'soa_validation_private_subnets_rs': 'subnet-07cda239066f5aae4',
            'soa_validation_rs_jdbc_url': 'jdbc:redshift://iris-edb-qa.cjlwfm8otbqm.us-east-2.redshift.amazonaws.com:5439/omnisource',
            'username': 'omnisource_soa_ro',
            'password':'dummy'
        },
	'prd': {
            'soa_validation_glue_rs_sg': 'sg-01dbc23e3d2a1715b',
            'soa_validation_eip_rs_sg': 'sg-0ccdda3ad781cd935',
            'soa_validation_lambda_rs_sg': 'sg-0bf52390e6eb28a36',
            'soa_validation_eip_services_sg': 'sg-0259245c39d5d6395',
            'soa_validation_rs_jdbc_url': 'jdbc:redshift://iris-edb-prd.carpdwnmaayt.us-east-2.redshift.amazonaws.com:5439/omnisource',
            'soa_validation_private_subnets_rs': 'subnet-09cc5df17821908d7',
	    'username': 'omnisource_soa_ro',
            'password':'dummy'
        },   
        'common_config': {
            'soa_glue_connection_name': 'edb_iris_soa_databrew_redshift_connection',
            'soa_service_role': 'edb_buids_soa_databrew_service_role',
            'soa_glue_db_name': 'iris-dqa-database',
            'soa_rs_secret_name': f"awsredshift-iris-edb-{env}-SoaroUser"
        }
    }
    redshift_system_user_encryption_key_id = {
        "dev": "d3a5e475-13d2-47e3-a54c-a62c68872a57",
        "qa": "9f2a1e0b-9334-4f75-8a4e-916d3b40d6c4",
        "prd": "4c08f404-7210-4310-a5c7-828fe0280074"
    }
    # EHR Variables
    ehr_config = {
        'common_config': {
            'ehr_dqa_service_role': 'iris_ehr_service_role'
        }
    }

    global_params_dict = {}
    with open(f"{root_dir}/params/{params_file_name_mapping[env]}", "r") as fp:
        global_params_dict = json.loads(fp.read())
        global_params_dict["Parameters"]["ArtifactBucket"] = artifact_bucket
        global_params_dict["Parameters"]["GlueRawBucket"] = global_params_dict["Parameters"]["EdbRawBucket"]
        global_params_dict["Parameters"]["GlueRefinedBucket"] = global_params_dict["Parameters"]["EdbRefinedBucket"]
        global_params_dict["Parameters"]["GlueLandingBucket"] = global_params_dict["Parameters"]["EdbLandingBucket"]
        global_params_dict["Parameters"]["GlueDepartureBucket"] = global_params_dict["Parameters"]["EdbDepartureBucket"]
        global_params_dict["Parameters"]["RedshiftSecurityGroupId"] = global_params_dict["Parameters"]["LambdaSelfReferentialSecurityGroup"]
        global_params_dict["Parameters"]["RedshiftClusterName"] = f"iris-edb-{env}"
        global_params_dict["Parameters"]["EnvType"] = env

    if env == "prd":
        edb_s3_env = "prod"
    else:
        edb_s3_env = env

    edb_athena_bucket = f"lly-edp-athena-us-east-2-{edb_s3_env}"
    edb_codeconfig_bucket = f"lly-edp-codeconfig-us-east-2-{edb_s3_env}"
    edb_departure_bucket = f"lly-edp-departure-us-east-2-{edb_s3_env}"
    edb_exploratory_bucket = f"lly-edp-explrtry-us-east-2-{edb_s3_env}"
    edb_raw_bucket = f"lly-edp-raw-us-east-2-{edb_s3_env}"
    edb_refined_bucket = f"lly-edp-refined-us-east-2-{edb_s3_env}"
    edb_conform_bucket = f"lly-edp-conform-us-east-2-{edb_s3_env}"
    edb_landing_bucket = f"lly-edp-landing-us-east-2-{edb_s3_env}"
    redshift_cluster_name = f"iris-edb-{env}-cdk" if env == "qa" else f"iris-edb-{env}"

    glue_execution_class = ('FLEX' if env != 'prd' else 'STANDARD')
    data_class = ('Red' if env != 'dev' else 'Yellow')
    HIPPA = ('Yes' if env != 'dev' else 'No')
    annotation_config = IrisCDKAnnotationsConfig("warning")

    tags = global_params_dict["Tags"]
    v_edb_s3_kms_key  ={
        "dev": "9dc640c2-48be-41fb-968b-e550a63478e9",
        "qa": "01e6836c-b082-4cab-8c5e-e0c9f7b94e09",
        "prd": "5c38dc12-f847-458b-9cb0-be281caa82f5"
    }

    v_edb_aws_kms_web_hook_eip = {
        "dev": "863f920c-075c-49af-b64b-93c41e4c3c66",
        "qa": "eb429285-1a9f-4206-bff2-caf0a98de9ec",
        "prd": "7c95d4a0-8f5d-46b4-b113-fcbd648f6b73"
    }

    v_aws_kms_iris_sm_key = {
        "dev": "",
        "qa": "",
        "prd": "1780029e-57b7-40b8-ba35-0022e27b5a83"
    }

    tableau_automation = {
		"dev" : {
				"tableau_automation_sec_grp" : ["sg-00bf741799ec3dad5","sg-06a411939f380bdaf","sg-004b96567923f1011","sg-0665dfd37a61d1936"],
				"subnet_id_one" : "subnet-08775232140992cbf",
				"subnet_id_two" : "subnet-02dad4453e2d9e100",
				"tableau_url" : "https://tabedbdev1.aws.lilly.com/api/3.17",
				"payer_db_cluster_name" : "iris-edb-dev",
				"database_name" : "iris_db" ,
                "table_name" : "iris_public.cnf_tableau_refresh_metadata_logs"	
				},
		"qa" :	{
				"tableau_automation_sec_grp" : ["sg-0b06cf3dd033ce15b","sg-0aa219d16317d12b8","sg-049ecd1ecd6d5a044","sg-09478d165670fe8d9"],
				"subnet_id_one" : "subnet-07cda239066f5aae4",
				"subnet_id_two" : "subnet-0385154d2ba834d28",
				"tableau_url" : "https://tableau-edb-q.aws.lilly.com/api/3.17",
				"payer_db_cluster_name" : "iris-edb-qa",
				"database_name" : "iris_db",
                "table_name" : "iris_public.cnf_tableau_refresh_metadata_logs"
				},
		"prd" :	{
				"tableau_automation_sec_grp" : ["sg-0bf52390e6eb28a36","sg-0139626d57e496a99","sg-0cca20ad3f590f87f","sg-0dc1d9486864bfd02"],
				"subnet_id_one" : "subnet-0b402d8ba5e3fbec9",
				"subnet_id_two" : "subnet-03b4ecce39bf6260a",
				"tableau_url" : "https://tableau-edb.aws.lilly.com/api/3.17",
				"payer_db_cluster_name" : "iris-edb-prd",
				"database_name" : "iris_db",
                "table_name" : "iris_public.cnf_tableau_refresh_metadata_logs"
				}
		}
    
    cma_secret_automation = {
		"dev" : {
				"edb_iris_cma_secret_rotation_sec_grp" : ["sg-004fc405931b26f23","sg-06a411939f380bdaf","sg-004b96567923f1011"],
				"subnet_id_one" : "subnet-08775232140992cbf",
				"subnet_id_two" : "subnet-02dad4453e2d9e100",
				"cma_db_cluster_name" : "edb-analytic-consumer-dev",
				"database_name" : "iris_edb_icyte",
                "cma_host_name" : "edb-analytic-consumer-dev.cnjndgzifrh0.us-east-2.redshift.amazonaws.com"
				},
		"qa" :	{
				"edb_iris_cma_secret_rotation_sec_grp" : ["sg-01139348c7ee65c16","sg-0b06cf3dd033ce15b","sg-0aa219d16317d12b8","sg-049ecd1ecd6d5a044"],
				"subnet_id_one" : "subnet-07cda239066f5aae4",
				"subnet_id_two" : "subnet-0385154d2ba834d28",
				"cma_db_cluster_name" : "edb-analytic-consumer-qa",
				"database_name" : "iris_edb_icyte",
                "cma_host_name" : "edb-analytic-consumer-qa.cjlwfm8otbqm.us-east-2.redshift.amazonaws.com"			
				},
		"prd" :	{
				"edb_iris_cma_secret_rotation_sec_grp" : ["sg-03c24ae2a8fd0efc9","sg-0bf52390e6eb28a36","sg-0dc1d9486864bfd02"],
				"subnet_id_one" : "subnet-06bbd4b4b2196a3b0",
				"subnet_id_two" : "subnet-02b45250bac7ab77a",
				"cma_db_cluster_name" : "edb-analytic-consumer-prod",
				"database_name" : "iris_edb_icyte",
				"cma_host_name": "edb-analytic-consumer-prod.carpdwnmaayt.us-east-2.redshift.amazonaws.com"
				}
		}   

    edb_iris_csp_edwin_config = {
		"dev" : {
				"edb_iris_edwin_task_validation_sec_grp" : ["sg-06a411939f380bdaf","sg-004b96567923f1011"],
				"subnet_id_one" : "subnet-08775232140992cbf",
				"subnet_id_two" : "subnet-02dad4453e2d9e100",
				"db_cluster_name" : "iris-edb-dev",
				"database_name" : "iris_db"
				},
		"qa" :	{
				"edb_iris_edwin_task_validation_sec_grp" : ["sg-0b06cf3dd033ce15b","sg-0aa219d16317d12b8","sg-049ecd1ecd6d5a044"],
				"subnet_id_one" : "subnet-07cda239066f5aae4",
				"subnet_id_two" : "subnet-0385154d2ba834d28",
				"db_cluster_name" : "iris-edb-qa-cdk",
				"database_name" : "iris_db"				
				},
		"prd" :	{
				"edb_iris_edwin_task_validation_sec_grp" : ["sg-0bf52390e6eb28a36","sg-0dc1d9486864bfd02"],
				"subnet_id_one" : "subnet-06bbd4b4b2196a3b0",
				"subnet_id_two" : "subnet-02b45250bac7ab77a",
				"db_cluster_name" : "iris-edb-prd",
				"database_name" : "iris_db"
				}
		} 

    edb_iris_pataf_secret_automation = {
		"dev" : {
				"edb_iris_pataf_secret_rotation_sec_grp" : ["sg-06a411939f380bdaf","sg-004b96567923f1011"],
				"subnet_id_one" : "subnet-08775232140992cbf",
				"subnet_id_two" : "subnet-02dad4453e2d9e100",
				"db_cluster_name" : "iris-edb-dev",
				"database_name" : "iris_db"
				},
		"qa" :	{
				"edb_iris_pataf_secret_rotation_sec_grp" : ["sg-0b06cf3dd033ce15b","sg-0aa219d16317d12b8","sg-049ecd1ecd6d5a044"],
				"subnet_id_one" : "subnet-07cda239066f5aae4",
				"subnet_id_two" : "subnet-0385154d2ba834d28",
				"db_cluster_name" : "iris-edb-qa-cdk",
				"database_name" : "iris_db"				
				},
		"prd" :	{
				"edb_iris_pataf_secret_rotation_sec_grp" : ["sg-0bf52390e6eb28a36","sg-0dc1d9486864bfd02"],
				"subnet_id_one" : "subnet-06bbd4b4b2196a3b0",
				"subnet_id_two" : "subnet-02b45250bac7ab77a",
				"db_cluster_name" : "iris-edb-prd",
				"database_name" : "iris_db"
				
				}
		}

    @staticmethod
    def load_stack_params_file(param_file_name):
        params_dict = {}
        param_full_path = f"{BuildConfig.root_dir}/params/{param_file_name}"
        with open(param_full_path, "r") as fp:
            params_dict = json.loads(fp.read())
        params_dict = params_dict['Parameters']
        params_from_global_dict = BuildConfig.global_params_dict["Parameters"]
        for key, value in params_dict.items():
            if "Ref" in value or "Fn::Sub" in value:
                params_dict[key] = params_from_global_dict[key]
        return params_dict

    @staticmethod
    def get_abc_config():
        abc_aurora_secret = 'awsedb-auroradb-secrets'
        abc_schema_mapping = {
            'dev': 'edb_dev_abc',
            'qa': 'edb_qa_abc',
            'prd': 'edb_prod_abc'
        }
        return {'abcAuroraSecret': abc_aurora_secret, 'abcSchema': abc_schema_mapping[BuildConfig.env]}

    @staticmethod
    def get_vpc_id():
        vpc_mapping = {
            'dev': {
                'vpc_id': 'vpc-06a3d8f2cdafb8a6e',
                'LillyOwnedCIDRs': 'pl-0aa25c17244aa70a4'
            },
            'qa': {
                'vpc_id': 'vpc-0d4e782cbe86eb07c',
                'LillyOwnedCIDRs': 'pl-0aa25c17244aa70a4'
            },
            'prd': {
                'vpc_id': 'vpc-0ea80082460c43671',
                'LillyOwnedCIDRs': 'pl-0aa25c17244aa70a4'
            }
        }
        return vpc_mapping[BuildConfig.env]

    @staticmethod
    def apply_tags(scope, tags=tags):
        for key, value in tags.items():
            Tags.of(scope=scope).add(key=key, value=value)

    #VE Aurora variables
    ve_config = {
        'dev': {
            've_glue_rs_sg': 'sg-0b25665300852d07a',
            've_eip_data_sg': 'sg-02065bc4162566926',
            've_lambda_rs_sg': 'sg-0de3834ca72bd7e0d',
            've_private_subnets_rs': 'subnet-0f515003e3178cb67',
            've_rs_jdbc_url': 'jdbc:redshift://iris-edb-dev.cnjndgzifrh0.us-east-2.redshift.amazonaws.com:5439/iris_db',
            'username':'dummy', 
            'password':'dummy' 
        },
        'qa': {
            've_glue_rs_sg': 'sg-0b556825fbf72f5f8',
            've_eip_data_sg': 'sg-08c3d5e9072293980',
            've_lambda_rs_sg': 'sg-0e3879a62fe9bf22c',
            've_private_subnets_rs': 'subnet-0c68d5c1dbfd2e4a0',
            've_rs_jdbc_url': 'jdbc:redshift://iris-edb-qa.cjlwfm8otbqm.us-east-2.redshift.amazonaws.com:5439/iris_db',
            'username':'dummy', 
            'password':'dummy' 
        },
        'prd': {
            've_glue_rs_sg': 'sg-05638ee109df27529',
            've_eip_data_sg': 'sg-00c7d228ae5c3698a',
            've_lambda_rs_sg': 'sg-014c51021866af8e7',
            've_private_subnets_rs': 'subnet-06e6ad8fc6c2762e9',
            've_rs_jdbc_url': 'jdbc:redshift://iris-edb-prd.carpdwnmaayt.us-east-2.redshift.amazonaws.com:5439/iris_db',
            'username':'dummy', 
            'password':'dummy' 
        },
        'common_config': {
            've_glue_connection_name': 'edb_iris_ve_aurora_connection'
        }
    }

    # Config variables to use for lambda functions and stack rd_phmcy_anmly_stack
    rd_phmcy_anmly_lambda_config = {
        "dev": {
            "redshiftSeceretValue": "rd_phmcy_anmly_stack_dev",
            "DB_NAME": "iris_db",
            "CLUSTER_NAME": "iris-edb-dev",
            "pVpcEndpointId": "vpce-069388414a9f87f40"
        },
        "qa": {
            "redshiftSeceretValue": "rd_phmcy_anmly_stack_qa",
            "DB_NAME": "iris_db",
            "CLUSTER_NAME": "iris-edb-qa-cdk",
            "pVpcEndpointId": "vpce-058757a9c034d181c"
        },
        "prd": {
            "redshiftSeceretValue": "rd_phmcy_anmly_stack_prd",
            "DB_NAME": "iris_db",
            "CLUSTER_NAME": "iris-edb-prd",
            "pVpcEndpointId": "vpce-03bee17f69c9802b9"
        }
    }
    pataf_lambda_config = {
        "dev": {
            "CLUSTER_NAME": "iris-edb-dev",
            "aws-kms-iris-scrtmgr-redshift": "d3a5e475-13d2-47e3-a54c-a62c68872a57"
        },
        "qa": {
            "CLUSTER_NAME": "iris-edb-qa-cdk",
            "aws-kms-iris-scrtmgr-redshift": "9f2a1e0b-9334-4f75-8a4e-916d3b40d6c4"
        },
        "prd": {
            "CLUSTER_NAME": "iris-edb-prd",
            "aws-kms-iris-scrtmgr-redshift": "4c08f404-7210-4310-a5c7-828fe0280074"
        }
    }
    rad_awb_project_id_map = {
        "dev": "",
        "qa": "84aba1af6311904243d770826b5204",
        "prd": "002d74c0a94198e8ce66114d95a3a3"
    }

    audit_awb_project_id_map = {
        "dev": "",
        "qa": "13a168ad041a3fceee3f9dcc4ef58a",
        "prd": "c7300fd5f2bb1031f83c24bdefefc1"
    }

    r2p2_awb_project_id_map = {
        "dev": "",
        "qa": "e817ec2d97c185d99fabcac083e14b",
        "prd": "4a3129520b1bc733d9fc375ed57557"
    }

    crm_dt_bia_s3_bucket = {
        "dev": "",
        "qa": "lly-bia-raw-us-east-2-qa-efb8lpxk",
        "prd": "lly-bia-raw-us-east-2-dev-r6t7r1dz",
    }

    crm_dt_bia_account_number = {
        "dev" :"",
        "qa" :"561558700175",
        "prd" :"130087722982"
    }

    rd_proj_matrix_tags = {
        "AppName": "Revenue Defender: Project Matrix",
        "ApplicationCi": "CI00000073733827",
        "CostCenter": "100ARAS",
        "CostCenterApprover": "supancik_kent_a@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "tarini.rout@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "wilson_greg_a@lilly.com",
        "SystemOwner": "johanneman_jefferson_j@lilly.com",
        "ProjectCenter": "705AK39",
        "ApproverGroup": "IRIS-MLOPS-SUPPORT"
    }

    iris_lva_pataf_tags = {
        "AppName": "IRIS EDB: Patient Affordability Reporting",
        "ApplicationCi": "CI00000018450191",
        "CostCenter": "705A882",
        "CostCenterApprover": "wilson_greg_a@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "jonathan.phillips@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "peterson_andrew_john@lilly.com",
        "SystemOwner": "urbanski_ethan_tyler@lilly.com",
        "ProjectCenter": "705A882",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_payer_tags = {
        "AppName": "IRIS: EDB Payer Dashboard",
        "ApplicationCi": "CI00000016065413",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "yadav_brajesh_kumar@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "adammeadows@lilly.com",
        "SystemOwner": "hamilton_michael_s@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_brg_tags = {
        "AppName": "EDB: 340B ESP-REFINE",
        "ApplicationCi": "CI00000083260459",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "tiwari_shubham@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "wilson_greg_a@lilly.com",
        "SystemOwner": "talley_amanda_h@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_sca_tags = {
        "AppName": "EDB: IRIS Supply Chain Analytics Consumption",
        "ApplicationCi": "CI00000007580634",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "jonathan.phillips@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "wilson_greg_a@lilly.com",
        "SystemOwner": "josh.kuiper@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_turbo_tags = {
        "AppName": "IRIS EDB: Turbo",
        "ApplicationCi": "CI00000025284696",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "kurapati_suresh@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "wilson_greg_a@lilly.com",
        "SystemOwner": "angela.wadsworth@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_ehr_tags = {
        "AppName": "EDB: EHR Analytics",
        "ApplicationCi": "CI00000021936916",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "yadav_brajesh_kumar@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "adammeadows@lilly.com",
        "SystemOwner": "paul.porter@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_ia_tags = {
        "AppName": "IRIS EDB Institutional Analytics Extract",
        "ApplicationCi": "CI00000016940686",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "naveen.erigineni@network.lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "wilson_greg_a@lilly.com",
        "SystemOwner": "straatman_andrew_j@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    iris_lva_va_tags = {
        "AppName": "IRIS EDB: Validata Analytics",
        "ApplicationCi": "CI00000007580677",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "naveen.erigineni@network.lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "wilson_greg_a@lilly.com",
        "SystemOwner": "pappu_suresh@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITPLATFORM-US-SUPPORT"
    }

    iris_lva_ddw_tags = {
        "AppName": "IRIS : Deal Development Analytics Data Extracts",
        "ApplicationCi": "CI00000018789208",
        "CostCenter": "705A960",
        "CostCenterApprover": "adammeadows@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "komal.bhowsinka@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "adammeadows@lilly.com",
        "SystemOwner": "telford_dylan_colin@lilly.com",
        "ProjectCenter": "705A960",
        "ApproverGroup": "IRIS-ITMHS-US-APPROVERS"
    }

    csp_iris_tags = {
        "AppName": "Customer Support Program Analytics Reports and Dashboards",
        "ApplicationCi": "CI00000018789195",
        "CostCenter": "100AAY3",
        "CostCenterApprover": "hernandez_lugo_claudia@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "tinganxu.lewisliu@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "tinganxu.lewisliu@lilly.com",
        "SystemOwner": "woolen_joshua@lilly.com",
        "ProjectCenter": "100AAY3",
        "ApproverGroup": "IRIS-ITPLATFORM-US-APPROVERS"
    }
    
    iris_sales_incentive_tags = {
        "AppName": "IRIS EDB: Sales Incentives and Extracts",
        "ApplicationCi": "CI00000007383209",
        "CostCenter": "705AK38",
        "CostCenterApprover": "zdwenger@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "shivam.sitoke@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "zdwenger@lilly.com",
        "SystemOwner": "joachim.walker@lilly.com",
        "ProjectCenter": "705AK38",
        "ApproverGroup": "IRIS-ITPLATFORM-US-APPROVERS"
    }

    iris_sales_ttp_tags = {
        "AppName": "EDB: IRIS Sales TTP",
        "ApplicationCi": "CI00000018450807",
        "CostCenter": "705AK38",
        "CostCenterApprover": "zdwenger@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "shivam.sitoke@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "zdwenger@lilly.com",
        "SystemOwner": "joachim.walker@lilly.com",
        "ProjectCenter": "705AK38",
        "ApproverGroup": "IRIS-ITPLATFORM-US-APPROVERS"
    }

    iris_sales_javelin_tags = {
        "AppName": "Javelin",
        "ApplicationCi": "CI00000000418446",
        "CostCenter": "705AK38",
        "CostCenterApprover": "zdwenger@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "shivam.sitoke@lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "zdwenger@lilly.com",
        "SystemOwner": "joachim.walker@lilly.com",
        "ProjectCenter": "705AK38",
        "ApproverGroup": "IRIS-ITPLATFORM-US-APPROVERS"
    }

    iris_sales_stacks_tags = {
        "AppName": "IRIS EDB: Diabetes Spec Business Unit Standardized Sales Reports",
        "ApplicationCi": "CI00000022615926",
        "CostCenter": "705AK38",
        "CostCenterApprover": "zdwenger@lilly.com",
        "DeployEnvironment": f"{env}",
        "PrimaryItContact": "anushri.jayaswal@network.lilly.com",
        "Level1BusinessArea": "Business Units IDS",
        "DataClassification": "Red",
        "SourceGitRepo": "lusa-iris-edb",
        "SystemCustodian": "zdwenger@lilly.com",
        "SystemOwner": "raborn_thomas@lilly.com",
        "ProjectCenter": "705AK38",
        "ApproverGroup": "IRIS-ITPLATFORM-US-APPROVERS"
    }
