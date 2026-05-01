from aws_cdk import (
    Environment,
    aws_glue as glue,
    aws_s3 as s3
)
from constructs import Construct
from .build_config import BuildConfig

class IrisRawToRefinedGlueJob(Construct):
    def __init__(self, scope: Construct, id:str, *, name: str, artifact_bucket:s3.IBucket, config:BuildConfig, env:Environment,role='edb_buids_iris_service_role', script='edb_iris_raw_to_refined_generic.py', **kwargs):
        super().__init__(scope, id, **kwargs)
        abc_config = config.get_abc_config()
        self.Jobv1 = glue.CfnJob(
            self, id,
            name = name,
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                python_version="3",
                script_location=artifact_bucket.s3_url_for_object(f"aws_glue/scripts/edb-iris/{script}")
            ),
            role=f"arn:aws:iam::{env.account}:role/{role}",
            connections=glue.CfnJob.ConnectionsListProperty(
                connections=["edb_iris_abc_db_connection"]
            ),
            default_arguments={
                "--TempDir": artifact_bucket.s3_url_for_object("aws_glue/temp"),
                "--raw_bucket": config.edb_raw_bucket,
                "--refined_bucket": config.edb_refined_bucket,
                "--source_config_location": "aws_glue/config/edb-iris/source_configuration.json",
                "--artifact_bucket": config.artifact_bucket,
                "--AbcSchema": abc_config['abcSchema'],
                "--AuroraSecret": abc_config['abcAuroraSecret'],
                "--job-bookmark-option": "job-bookmark-enable",
                "--use-postgres-driver": "true",
                "--extra-py-files": f"{artifact_bucket.s3_url_for_object('aws_glue/scripts/edb-iris/edb_iris_common.py')},s3://{config.edb_codeconfig_bucket}/edb-core/core/abc/libs/glue/glueetl/edb_abc_libraries.zip,{artifact_bucket.s3_url_for_object('aws_glue/scripts/edb-iris/edb_iris_glue_monitoring.py')}",
                "--enable-auto-scaling": "true",
                "--additional-python-modules": "watchtower",
                "--enable-continuous-cloudwatch-log": "true",
                "--continuous-log-logGroup": "/aws-glue/jobs/edb-iris-gluejob-info-logs",
                "--continuous-log-errorlogGroup": "/aws-glue/jobs/edb-iris-gluejob-error-logs"
            },
            execution_class=config.glue_execution_class,
            glue_version="3.0",
            number_of_workers=10,
            tags=config.tags,
            worker_type="G.2X"
        )
