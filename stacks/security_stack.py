import os

from aws_cdk import (
    Environment,
    Stack,
    Duration,
    CfnOutput,
    Fn,
    aws_ec2 as _ec2,
    CfnCondition as _condition,
    cloudformation_include as cfn_inc,
    aws_s3 as s3,
    Aws as _aws,
    aws_secretsmanager as _secretsmanager,
    aws_kms as _kms,
    aws_iam as _iam,
    Duration, 
    CfnParameter as _parameter,
    Tags as _tag
)
from constructs import Construct
from cdk.lib.build_config import BuildConfig
from cdk.lib.template_helper import TemplateHelper


class SecurityStack(Stack):
    """
    This cdk stack houses the existing Security stack
    """
    def __init__(self, scope: Construct, construct_id: str, *, config:BuildConfig,vpc:_ec2.Vpc, env:Environment, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        root_dir = os.path.dirname(os.path.abspath('template.yml'))
        template_path = f"{root_dir}/templates/legacy/{config.env}/security_stack.json"
        params = config.load_stack_params_file('params_cdk.security-prd.json')
        TemplateHelper.remove_resources(
            template_path = template_path,
            resource_logical_ids = [
                'BASServiceRoleName',
                'BRMSServiceRoleName',
                'DMSIrisKMSKey',
                'DMSIrisKMSKeyAlias',
                'DQASnowSecret',
                'edbAuroraDHCspSecret',
                'edbAuroraLashCspSecret',
                'edbIrisDDWESIPortalSecretReference',
                'edbIrisDDWKMSAlias',
                'edbIrisDDWKMSKey',
                'FlexDataArchivePolicy',
                'IrisMonitoringWebhook',
                'IrisPatafReportingSystemSecret',
                'IrisTableauCSP',
                'IrisTableauCSPBUSecret',
                'IrisTableauDataSourceRefresh',
                'IrisTableauPAT',
                'LMServiceRoleName',
                'mpBASGlueJobPolicy',
                'mpBASLambdaPolicy',
                'mpBASRedshiftDataPolicy',
                'mpBASS3RWPolicy',
                'mpBIAS3RefinedROPolicy',
                'mpBRGLambdaPolicy',
                'mpBRMSDatabrewPolicy',
                'mpBRMSGlueJobPolicy',
                'mpBRMSLambdaPolicy',
                'mpBRMSRedshiftDataPolicy',
                'mpBRMSS3RWPolicy',
                'mpBRMSStateMachinePolicy',
                'mpCCPAGluePolicy',
                'mpCCPALambdaPolicy',
                'mpCCPAStateMachinePolicy',
                'mpDQADatabrewPolicy',
                'mpDQAGlueJobPolicy',
                'mpDQALambdaPolicy',
                'mpDQAMiscPolicy',
                'mpDQARedshiftDataPolicy',
                'mpDQAS3RWPolicy',
                'mpDQAStateMachinePolicy',
                'mpEdbEPHS3Policy',
				'mpEdbIrisRadAwbPolicy',
				'mpEdbIrisS3ExplrtryPolicy',
                'mpEdbEPHSecretsPolicy',
                'mpEdbIrisAthenaPolicyAdmin',
                'mpEdbIrisBrmsDatabrewSecurityPolicy',
                'mpIrisHospitalAnomalyDetectionPolicy',
                'mpEdbIrisConsolePolicy',
                'mpEdbIrisFederatedServicePolicy',
                'mpEdbIrisFederatedServicePolicy1',
                'mpEdbIrisGluePolicy',
                'mpEdbIrisKmsRWPolicy',
                'mpEdbIrisLambdaPolicy',
                'mpEdbIrisLogPipelinePolicy',
                'mpEdbIrisRDSAdminPolicy',
                'mpEdbIrisReadMinusS3Policy',
                'mpEdbIrisRedshiftAdminPolicy',
                'mpEdbIrisRedshiftDataPolicy',
                'mpEdbIrisS3AdminConformedPolicy',
                'mpEdbIrisS3AdminLandingPolicy',
                'mpEdbIrisS3AdminRawPolicy',
                'mpEdbIrisS3AdminRawOmmPolicy',
                'mpAnaplanS3AdminDeparturePolicy',
                'mpEdbIrisS3AdminRefinedPolicy',
                'mpEdbIrisSecretsPolicy',
                'mpEdbIrisSecretsPolicyTwo',
                'mpEdbIrisServicePolicy',
                'mpEdbIrisStateMachinePolicy',
                'mpEHRDatabrewPolicy',
                'mpEHRGlueJobPolicy',
                'mpEHRLambdaPolicy',
                'mpEHRPiLambdaPolicy',
                'mpEHRPiS3RWPolicy',
                'mpEHRMiscPolicy',
                'mpEHRRedshiftDataPolicy',
                'mpEHRS3RWPolicy',
                'mpEHRStateMachinePolicy',
                'mpLMGlueJobPolicy',
                'mpLMLambdaPolicy',
                'mpLMRedshiftDataPolicy',
                'mpLMS3RWPolicy',
                'oDMSIrisKMSKeyAlias',
                'OracleRDRSecretforDT',
                'RedshiftSecretforHospitalAnomalyDetection',
                'pAthenaIrisActPolicy',
                'pAthenaIrisAdsPolicy',
                'pAthenaIrisBrgPolicy',
                'pAthenaIrisCapgeminiPolicy',
                'pAthenaIrisCcpaPolicy',
                'pAthenaIrisCptPolicy',
                'pAthenaIrisEdiPolicy',
                'pAthenaIrisErxPolicy',
                'pAthenaIrisEversanaPolicy',
                'pAthenaIrisFive9Policy',
                'pAthenaIrisIncentivesPolicy',
                'pAthenaIrisIqviaPolicy',
                'pAthenaIrisJavelinPolicy',
                'pAthenaIrisManualFilesPolicy',
                'pAthenaIrisMtmPolicy',
                'pAthenaIrisOpusPolicy',
                'pAthenaIrisPublicPolicy',
                'pAthenaIrisRelayHealthPolicy',
                'pAthenaIrisSapPolicy',
                'pAthenaIrisSymphonyPolicy',
                'pAthenaIrisTcmPolicy',
                'PayerRedshiftReportingUserSecret',
                'pBrgMedicaidPolicy',
                'pFlexIrisManualExtractsPolicy',
                'rAthenaIrisTurboUsersPolicy',
                'rBASServiceRole',
                'rBrgHashingBinaryPolicy',
                'rBRGServiceRole',
                'rBRMSConfigUpdatePolicy',
                'rBRMSConsoleRole',
                'rBRMSGlueConnectionPolicy',
                'rBRMSServiceRole',
                'rCCOrchServiceRole',
                'rCCPAServiceRole',
                'rCEHBiaRole',
                'rMDMServicerole',
                'rCloudFormationRolePolicy',
                'rCmaServiceRole',
                'rDeveloperRole',
                'rDQAGlueConnectionPolicy',
                'rDQAServiceRole',
                'RedshiftKMSKey',
                'RedshiftKMSKeyAlias',
                'RedshiftSecretforSalesReporting',
                'rEHRServiceRole',
                'rEPHServiceRole',
                'rGatewayRole',
                'rIrisActRestrictedRole',
                'rIrisAdsRestrictedRole',
                'rIrisAuroradbDevSecurityGroupIngress',
                'rIrisAuroraDbSecurityGroup',
                'rIrisAuroraJumpSecurityGroupIngress',
                'rIrisBIAARole',
                'rIrisBIACapgeminiBiaMarketplaceRole',
                'rIrisBIADDRole',
                'rIrisBIADGRole',
                'rIrisBrgRestrictedRole',
                'rIrisCapgeminiRestrictedRole',
                'rIrisCcpaRestrictedRole',
                'rIrisCptRestrictedRole',
                'rIrisDBMigrationsPolicy',
                'rIrisDHCDbSecurityGroup',
                'rIrisDHCDbSecurityGroupId',
                'rIrisDHCSecurityGroupIngress',
                'rIrisDTGlueConnectionSecurityGroupIngress',
                'rIrisDTGlueSecurityGroup',
                'rIrisDTGlueSecurityGroup',
                'rIrisEdiRestrictedRole',
                'rIrisEngineGitHubOIDCRolePermissions',
                'rIrisEPHCODSPolicy',
                'rIrisEPHLOVPolicy',
                'rIrisErxRestrictedRole',
                'rIrisEversanaRestrictedRole',
                'rIrisFive9RestrictedRole',
                'rIrisIdsCspRole',
                'rIrisIdsLvaRole',
                'rIrisIdsMarketingRole',
                'rIrisIdsSalesRole',
                'rIrisIncentivesRestrictedRole',
                'rIrisIqviaRestrictedRole',
                'rIrisJavelinRestrictedRole',
                'rIrisLashDbSecurityGroup',
                'rIrisLashDbSecurityGroupId',
                'rIrisLashSecurityGroupIngress',
                'rIrisManualFilesRestrictedRole',
                'rIrisMtmRestrictedRole',
                'rIrisNBEEPHPolicy',
                'rIrisOpusRestrictedRole',
                'rIrisPrefectPolicy',
                'rIrisPublicRole',
                'rIrisRelayHealthRestrictedRole',
                'rIrisS3IqviaScrubPolicy',
                'rIrisSapScaRestrictedRole',
                'rIrisSesPolicy',
                'rIrisSymphonyRestrictedRole',
                'rIrisTcmRestrictedRole',
                'rIrisTurboUsersRestrictedRole',
                'rIrisZsFieldInsightsRestrictedRole',
                'rLMGlueConnectionPolicy',
                'rLMServiceRole',
                'rOperationRole',
                'rPCPServiceRole',
                'rRedshiftServicePolicy',
                'rRedshiftServiceRole',
                'rS3EdbABCLibPolicy',
                'rS3IrisActPolicy',
                'rS3IrisAdsPolicy',
                'rS3IrisBiaaRoPolicy',
                'rS3IrisBiaDDRoPolicy',
                'rS3IrisBiaDGRoPolicy',
                'rS3IrisBiaOmnichannelPolicy',
                'rS3IrisBrgPolicy',
                'rS3IrisCapgeminiBiaMarketplaceRoPolicy',
                'rS3IrisCapgeminiPolicy',
                'edbAuroraMDMSecret',
                'rS3IrisCcpaPolicy',
                'rS3IrisConformPublicPolicy',
                'rS3IrisCptPolicy',
                'rS3IrisEdiPolicy',
                'rS3IrisErxPolicy',
                'rS3IrisEversanaPolicy',
                'rS3IrisFive9Policy',
                'rS3IrisIncentivesPolicy',
                'rS3IrisIqviaPolicy',
                'rS3IrisJavelinPolicy',
                'rS3IrisListPolicy',
                'rS3IrisManualFilesPolicy',
                'rS3IrisMTMPolicy',
                'rS3IrisOpusPolicy',
                'rS3IrisRawPublicPolicy',
                'rS3IrisReadWritePolicy',
                'rS3IrisRefPublicPolicy',
                'rS3IrisRelayHealthPolicy',
                'rS3IrisSapScaPolicy',
                'rS3IrisSymphonyPolicy',
                'rS3IrisTcmPolicy',
                'rS3IrisTurboUsersReadPolicy',
                'rS3IrisTurboUsersWriteDeletePolicy',
                'rS3IrisZsFieldInsightsPolicy',
                'rS3LndGatewayPolicy',
                'rSecretsManagerRole',
                'rServiceRole',
                'rVES3DepartureRWPolicy',
                'rZSDataTransferServiceRole',
                'rVanigentDataTransferServiceRole',
                'SecretsManagerIrisKMSKey',
                'SecretsManagerIrisKMSKeyAlias',
                'statemachinePolicyForCodePipelineRole',
                'STRRedshiftReportingUserSecret',
                'TurboGeocodingAPISecret',
                'TurboRedshiftReportingUserSecret',
                'VEG3pCustSubUserAuroraSecret',
                'VEG3pMtlSubUserAuroraSecret',
                'VEHbtSubUserAuroraSecret',
                'VEPhhSubUserAuroraSecret',
                'VEPRD287OracleSecret',
                'VEPRD300CusSubUserOracleSecret',
                'VEPRD300Gp3MtmUserOracleSecret',
                'VEPRD300OracleSecret',
                'VEPRD300PhhOracleSecret',
                'VEAlignmentEDBSecret',
                'rG2nAnaplanServiceRole',
                'mpG2NAnaplanPolicy',
                'G2NAnaplanSecret'
                ])

        print("Before cfn include")
        cfn_template = cfn_inc.CfnInclude(
            self,
            "IrisecurityStack",
            template_file = template_path,
            parameters = params
        )
        print("After cfn include")
        secret_key = _kms.Alias.from_alias_name(self,
                                          "awskms_scrtmgr_eip",
                                           "alias/awskms-scrtmgr-eip")
        secret_key_arn = secret_key.key_id
        policy = _iam.ManagedPolicy.from_managed_policy_name(
            self ,
            "LZ-IAM-Boundary",
            managed_policy_name= "LZ-IAM-Boundary"
        )

#################  secrets ######################################################
        
        secret_string_user = '{  "username": "", "password": "", "host": "", "port": "", "dbname": ""}'
        RedshiftSecretforSalesReporting = _secretsmanager.CfnSecret(self, "RedshiftSecretforSalesReporting",
            description="Redshift Tableau Account for Sales Reporting",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
            name="edb-iris-redshift-tableau-secret",
            secret_string = '{ "username": "", "password": "" }'
        )

        DQASnowSecret = _secretsmanager.CfnSecret(self, "DQASnowSecret",
            description="Snow API Secret for DQA",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
            name="edb-iris-dqa-snow-secret",
            secret_string = '{ "username": "REST_DQAUSER_Standard", "password": "dummy", "apiUrl":"https://lilly.service-now.com"}'
        )

        TurboRedshiftReportingUserSecret = _secretsmanager.CfnSecret(
            self,
            "TurboRedshiftReportingUserSecret",
            description= "This is the secret for storing Turbo Redshift Reporting User Password",
            name=f"awsRedshift-iris-edb-{params['pEnvironment']}-TurboReportingUser",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{ "username": "", "password": "" }'
        )

        STRRedshiftReportingUserSecret = _secretsmanager.CfnSecret(
            self,
            "STRRedshiftReportingUserSecret",
            description= "This is the secret for storing STR Redshift Reporting User Password",
            name= f"awsRedshift-iris-edb-{params['pEnvironment']}-STRReportingUser",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{ "username": "", "password": "" }'
        )

        TurboGeocodingAPISecret = _secretsmanager.CfnSecret(
            self,
            "TurboGeocodingAPISecret",
            description= "This is the secret for storing Turbo Geocoding API key",
            name= "edb_iris_turbo_google_maps_api_key",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{ "key": "" }'
        )

        VEPRD287OracleSecret = _secretsmanager.CfnSecret(
            self,
            "VEPRD287OracleSecret",
            description= "This is the secret for storing Oracle PRD287 VE user secret",
            name= "edb_iris_ve_prd287_oracle_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )

        VEPRD300OracleSecret = _secretsmanager.CfnSecret(
            self,
            "VEPRD300OracleSecret",
            description= "This is the secret for storing Oracle PRD300 VE user secret",
            name= "edb_iris_ve_prd300_oracle_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )

        VEPRD300CusSubUserOracleSecret = _secretsmanager.CfnSecret(
            self,
            "VEPRD300CusSubUserOracleSecret",
            description= "This is the secret for storing Oracle PRD300 VE user secret",
            name= "edb_iris_ve_prd300_csu_oracle_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )

        VEPRD300Gp3MtmUserOracleSecret = _secretsmanager.CfnSecret(
            self,
            "VEPRD300Gp3MtmUserOracleSecret",
            description= "This is the secret for storing Oracle PRD300 VE user secret",
            name= "edb_iris_ve_prd300_gmu_oracle_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )

        VEPRD300PhhOracleSecret = _secretsmanager.CfnSecret(
            self,
            "VEPRD300PhhOracleSecret",
            description= "This is the secret for storing Oracle PRD300 VE phh user secret",
            name= "edb_iris_ve_prd300_oracle_db_phh_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )

        VEG3pMtlSubUserAuroraSecret = _secretsmanager.CfnSecret(
            self,
            "VEG3pMtlSubUserAuroraSecret",
            description= "This is the secret for storing Aurora G3P mtl_sub_user secret",
            name= "edb_iris_ve_g3p_mtl_sub_user_aurora_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{  "username": "*", "password": "*", "host": "*", "port": "*", "dbname": "*"}'
        )

        VEG3pCustSubUserAuroraSecret = _secretsmanager.CfnSecret(
            self,
            "VEG3pCustSubUserAuroraSecret",
            description= "This is the secret for storing Aurora G3P CUS_SUB_OWNER secret",
            name= "edb_iris_ve_g3p_cust_sub_user_aurora_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{  "username": "*", "password": "*", "host": "*", "port": "*", "dbname": "*"}'
        )

        VEPhhSubUserAuroraSecret = _secretsmanager.CfnSecret(
            self,
            "VEPhhSubUserAuroraSecret",
            description= "This is the secret for  storing VE workforce - Aurora  phh_sub_user secret",
            name= "edb_iris_ve_phh_sub_user_aurora_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{  "username": "*", "password": "*", "host": "*", "port": "*", "dbname": "*"}'
        )

        VEAlignmentEDBSecret = _secretsmanager.CfnSecret(
            self,
            "VEAlignmentEDBSecret",
            description= "This is the secret for storing VE alignment edb useven user secret",
            name= "edb_iris_ve_alignment_edb_aurora_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )         

        VEHbtSubUserAuroraSecret = _secretsmanager.CfnSecret(
            self,
            "VEHbtSubUserAuroraSecret",
            description= "This is the secret for storing VE workforce - Aurora  hbt_sub_user secret",
            name= "edb_iris_ve_hbt_sub_user_aurora_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{  "username": "*", "password": "*", "host": "*", "port": "*", "dbname": "*"}'
        )

        PayerRedshiftReportingUserSecret = _secretsmanager.CfnSecret(
            self,
            "PayerRedshiftReportingUserSecret",
            description= "This is the secret for storing Payer Redshift Reporting User Password",
            name= f"awsRedshift-iris-edb-{params['pEnvironment']}-PayerReportingUser",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{ "username": "", "password": "" }'
        )

        IrisPatafReportingSystemSecret = _secretsmanager.CfnSecret(
            self,
            "IrisPatafReportingSystemSecret",
            description= "This Secrets Manager for Patient Affordability and store the reporting credentials",
            name=  f"awsTableau-iris-edb-{params['pEnvironment']}-PATAFReportingSystem",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= secret_string_user
        )

        OracleRDRSecretforDT = _secretsmanager.CfnSecret(
            self,
            "OracleRDRSecretforDT",
            description= "Database Secret for Oracle ODS of radar for Dynamic Targeting",
            name= "edb-iris-oracle-rdr-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{ "username": "", "password": "" , "host": "", "port": "", "dbname": "", "driver": ""}'
        )

        G2NAnaplanSecret = _secretsmanager.CfnSecret(
            self,
            "G2NAnaplanSecret",
            description= "This secret is used to vault G2N Anaplan IAM User credentials",
            name= "G2N_Anaplan-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"iam_user_key": "","lly_ana_sftp_private_key": "","lly_ana_sftp_public_key": ""}'
        )

        RedshiftSecretforHospitalAnomalyDetection = _secretsmanager.CfnSecret(
            self,
            "RedshiftSecretforHospitalAnomalyDetection",
            description= "Secret for hospital anomaly detection adm_turbo rw",
            name= "adm_turbo_sys_acc_secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{ "AdmTurboAccName" : "", "AdmTurboAccSecret" : "" }'
        )

        IrisMonitoringWebhook = _secretsmanager.CfnSecret(
            self,
            "IrisMonitoringWebhook",
            description= "Iris Webhook secret for Monitoring Framework for Team Notifications",
            name= "iris_monitoring_webhook_url",
            kms_key_id= secret_key_arn,
            secret_string= '{ "AlertChannelWebhookURL": "", "InfoChannelWebhookURL": "" }'
        )

        IrisTableauPAT = _secretsmanager.CfnSecret(
            self,
            "IrisTableauPAT",
            description=   "Tableau Prod PAT for Report Refresh",
            name= "edb_iris_tableau_pds_prd_refresh_pat",
            kms_key_id= secret_key_arn,
            secret_string= '{ "PATName" : "", "PATSecret" : "" }'
        )

        edbAuroraLashCspSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraLashCspSecret",
            description= "This secret has Lash Aurora DB connection",
            name= "edb-iris-auroraLash-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )
        
        edbAuroraSonexusCRMCspSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraSonexusCRMCspSecret",
            description= "This secret has SonexusCRM Aurora DB connection",
            name= "edb-iris-auroraSonexusCRM-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        edbAuroraIqviaClaimsCspSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraIqviaClaimsCspSecret",
            description= "This secret has IqviaClaims Aurora DB connection",
            name= "edb-iris-auroraIqviaClaims-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )
        
        edbAuroraEversanaCRMCspSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraEversanaCRMCspSecret",
            description= "This secret has EversanaCRM Aurora DB connection",
            name= "edb-iris-auroraEversanaCRM-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )
        
        edbAuroraEversanaCspSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraEversanaCspSecret",
            description= "This secret has Eversana Aurora DB connection",
            name= "edb-iris-auroraEversana-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        edbAuroraDHCspSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraDHCspSecret",
            description= "This secret has DH Aurora DB connection",
            name= "edb-iris-auroraDHCsp-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        IrisTableauCSP = _secretsmanager.CfnSecret(
            self,
            "IrisTableauCSP",
            description= "Tableau Prod CSP for Report Refresh",
            name= f"edb_iris_tableau_pds_{params['pEnvironment']}_refresh_csp",
            kms_key_id= secret_key_arn,
            secret_string= '{ "CSPName" : "", "CSPSecret" : "" }'
        )

        IrisTableauCSPBUSecret = _secretsmanager.CfnSecret(
            self,
            "IrisTableauCSPBUSecret",
            description= "Tableau Prod CSP BU for Report Refresh",
            name= "edb_iris_adm_csp_bus_user_secret",
            kms_key_id= secret_key_arn,
            secret_string= '{ "CSPBUName" : "", "CSPBUSecret" : "" }'
        )

        IrisTableauDataSourceRefresh = _secretsmanager.CfnSecret(
            self,
            "IrisTableauDataSourceRefresh",
            description= "Tableau Token for Report Refresh",
            name= "edb_iris_tableau_data_source_refresh_pat",
            kms_key_id= secret_key_arn,
            secret_string= '{ "personal_access_token" : "", "personal_access_token_secret" : "" }'
        )

        edbAuroraMDMSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraMDMSecret",
            description= "This secret has DH Aurora DB connection",
            name= "edb-iris-auroraMDM-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        edbAuroraMDMCustomerSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraMDMCustomerSecret",
            description= "This secret has DH Aurora DB connection for Customer data",
            name= "edb-iris-auroraMDMCustomer-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        edbirisIFPSharepointSecret = _secretsmanager.CfnSecret(
            self,
            "edbIFPSharepointSecret",
            description= "This secret has Client Creds for IFP Sharepoint Application",
            name= "edb-iris-ifp-Sharepoint-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"ClientID": "","ClientPassword": "","TenantID": "","Sharepointpath": ""}'
        )


        edbLightspeedSecretQA = _secretsmanager.CfnSecret(
            self,
            "edbLightspeedSecretQA",
            description= "This secret has DH Aurora DB connection",
            name= "edb-iris-Lightspeed-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"Clientid": "","ClientSecret": "","Tenantid": "","Others": ""}'
        )
	    

        edbAuroraMDMAlignmentSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraMDMAlignmentSecret",
            description= "This secret has DH Aurora DB connection for Alignment data",
            name= "edb-iris-auroraMDMAlignment-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        edbAuroraWrkrSecret = _secretsmanager.CfnSecret(
            self,
            "edbAuroraWrkrSecret",
            description= "This secret has DH Aurora Wrkr Table connection",
            name= "edb-iris-auroraWrkr-secret",
            kms_key_id= params['pSMIrisKMSKey'],
            secret_string= '{"engine": "","host": "","username": "","password": "","dbname": "","port": ""}'
        )

        # ---- PGP Encryption Public Key Secret ----
        # Secret Manager to store PGP public key used for PGP encryption
        edbIrisCspPgpPublicKeySecret = _secretsmanager.CfnSecret(
            self,
            "edbIrisCspPgpPublicKeySecret",
            description="PGP public key used for PGP encryption",
            name="edb_iris_csp_pgp_public_key",
            kms_key_id=secret_key_arn,
            secret_string='{"pgp_public_key": "", "key_id": "", "key_owner": ""}'
        )

        VEWrkradmSubUserAuroraSecret = _secretsmanager.CfnSecret(
            self,
            "VEWrkradmSubUserAuroraSecret",
            description= "This is the secret for storing Aurora workeradm secret",
            name= "edb_iris_ve_wrkradm_aurora_db_secret",
            kms_key_id= f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-iris-scrtmgr-redshift",
            secret_string= '{  "username": "*", "password": "*", "host": "*", "port": "*", "dbname": "*"}'
        )	    

####################### KMS KEYS  #################################################################


        eip_redshift_lambda_execution_role = _iam.Role.from_role_name(self, "eipRedshiftLambdaExecutionRole", role_name="EIP_REDSHIFT_LAMBDA_EXECUTION_ROLE")
        eip_redshift_sm_rotate_role = _iam.Role.from_role_name(self, "eipRedshiftSmRotateRole", role_name="EIP_REDSHIFT_SM_ROTATE_ROLE")
        aws_redshift_admins = _iam.Role.from_role_name(self, "awsRedshiftAdmins", role_name="aws_redshift_admins")
        iris_platform_lambda_execution_role = _iam.Role.from_role_name(self, "irisPlatformLambdaExecutionRole", role_name="Iris-Platform-LambdaExecutionRole-prd")

        mpIrisPlatformLambdaVpcPolicy = _iam.ManagedPolicy(
            self, "mpIrisPlatformLambdaVpcPolicy",
            managed_policy_name="Iris-Platform-Lambda-VPC-Policy",
            document= _iam.PolicyDocument(statements=[
                    _iam.PolicyStatement(
                        actions=[
                            "ec2:Describe*",
                            "ec2:CreateNetworkInterface",
                            "ec2:DeleteNetworkInterface",
                            "ec2:CreateTags",
                            "ec2:DeleteTags"
                        ],
                        effect=_iam.Effect.ALLOW,
                        resources=[
                            "arn:aws:ec2:*:*:instance/*",
                            "arn:aws:ec2:*:*:security-group/*",
                            "arn:aws:ec2:*:*:network-interface/*"
                        ],
                        conditions={
                            "ForAllValues:StringEquals": {
                                "aws:TagKeys": "aws-glue-service-resource"
                            }
                        }
                    ),
                    _iam.PolicyStatement(
                        actions=[
                            "ec2:AssignPrivateIpAddresses",
                            "ec2:AttachNetworkInterface",
                            "ec2:UnassignPrivateIpAddresses",
                            "ec2:CreateNetworkInterface",
                            "ec2:DeleteNetworkInterface",
                            "ec2:Describe*",
                            "ec2:ENI*",
                            "ec2:ModifyNetworkInterfaceAttribute",
                            "ec2:SearchTransitGatewayRoutes"
                        ],
                        effect=_iam.Effect.ALLOW,
                        resources=["*"]
                    )
                ]
            )
        )

        iris_platform_lambda_execution_role.add_managed_policy(mpIrisPlatformLambdaVpcPolicy)

        RedshiftKMSKey =  _kms.Key(
            self,
            "RedshiftKMSKey",
            description= "Scrtmgr Redshift IRIS specific KMS key",
            enable_key_rotation= True,
            pending_window= Duration.days(30),
            policy= _iam.PolicyDocument(
                statements= [
                    _iam.PolicyStatement(
                        effect=  _iam.Effect.ALLOW,
                        principals=[_iam.AccountRootPrincipal()],
                        actions= ["kms:*"],
                        resources= ["*"],
                        sid= "Enable IAM User Permissions"
                    ),
                    _iam.PolicyStatement(
                        effect= _iam.Effect.ALLOW,
                        principals=[ _iam.ArnPrincipal(eip_redshift_lambda_execution_role.role_arn),
                            _iam.ArnPrincipal(eip_redshift_sm_rotate_role.role_arn),
                            _iam.ArnPrincipal(aws_redshift_admins.role_arn),
                            _iam.ArnPrincipal(iris_platform_lambda_execution_role.role_arn)
                        ],
                        actions= ["kms:Encrypt","kms:Decrypt","kms:ReEncrypt*","kms:GenerateDataKey*","kms:DescribeKey","kms:List*","kms:GetKeyRotationStatus"],
                        resources= ["*"],
                        sid= "Allow use of the key"
                    ),
                    _iam.PolicyStatement(
                        effect= _iam.Effect.ALLOW,
                        principals=[_iam.ArnPrincipal(eip_redshift_lambda_execution_role.role_arn),
                            _iam.ArnPrincipal(eip_redshift_sm_rotate_role.role_arn),
                            _iam.ArnPrincipal(aws_redshift_admins.role_arn),
                            _iam.ArnPrincipal(iris_platform_lambda_execution_role.role_arn)
                        ],
                        actions= ["kms:CreateGrant","kms:ListGrants","kms:RevokeGrant"],
                        resources= ["*"],
                        sid= "Allow attachment of persistent resources",
                        conditions= {"Bool": {
                                    "kms:GrantIsForAWSResource": "true"
                                }}
                    )
                    ]
            )
        )
        cfn_func = RedshiftKMSKey.node.default_child
        cfn_func.override_logical_id("RedshiftKMSKey")
        RedshiftKMSKeyAlias = _kms.Alias(
            self,
            "RedshiftKMSKeyAlias",
            alias_name= "alias/aws-kms-iris-scrtmgr-redshift",
            target_key= RedshiftKMSKey
        )
        cfn_func = RedshiftKMSKeyAlias.node.default_child
        cfn_func.override_logical_id("RedshiftKMSKeyAlias")


        SecretsManagerIrisKMSKey =  _kms.Key(
            self,
            "SecretsManagerIrisKMSKey",
            description= "Secrets manager IRIS specific KMS key",
            enable_key_rotation= True,
            pending_window= Duration.days(30),
            policy= _iam.PolicyDocument(
                statements= [
                    _iam.PolicyStatement(
                        effect=  _iam.Effect.ALLOW,
                        principals=[_iam.AccountRootPrincipal()],
                        actions= ["kms:*"],
                        resources= ["*"],
                        sid= "Enable IAM Policies"
                    )
                    ]
            )
        )
        cfn_func = SecretsManagerIrisKMSKey.node.default_child
        cfn_func.override_logical_id("SecretsManagerIrisKMSKey")
        SecretsManagerIrisKMSKeyAlias = _kms.Alias(
            self,
            "SecretsManagerIrisKMSKeyAlias",
            alias_name= "alias/aws-kms-iris-secrets-manager",
            target_key= SecretsManagerIrisKMSKey
        )
        cfn_func = SecretsManagerIrisKMSKeyAlias.node.default_child
        cfn_func.override_logical_id("SecretsManagerIrisKMSKeyAlias")



        DMSIrisKMSKey =  _kms.Key(
            self,
            "DMSIrisKMSKey",
            description= "Database Migration Service IRIS specific KMS key",
            enable_key_rotation= True,
            pending_window= Duration.days(30),
            policy= _iam.PolicyDocument(
                statements= [
                    _iam.PolicyStatement(
                        effect=  _iam.Effect.ALLOW,
                        principals=[_iam.AccountRootPrincipal()],
                        actions= ["kms:*"],
                        resources= ["*"],
                        sid= "Enable IAM Policies"
                    )
                    ]
            )
        )
        cfn_func = DMSIrisKMSKey.node.default_child
        cfn_func.override_logical_id("DMSIrisKMSKey")
        DMSIrisKMSKeyAlias = _kms.Alias(
            self,
            "DMSIrisKMSKeyAlias",
            alias_name= "alias/aws-kms-iris-dms",
            target_key= DMSIrisKMSKey
        )
        cfn_func = DMSIrisKMSKeyAlias.node.default_child
        cfn_func.override_logical_id("DMSIrisKMSKeyAlias")

        edbIrisDDWKMSKey =  _kms.Key(
            self,
            "edbIrisDDWKMSKey",
            description= "Deal Development KMS key for secretes manager encryption and decryption",
            enabled= True,
            policy= _iam.PolicyDocument(
                statements= [
                    _iam.PolicyStatement(
                        effect=  _iam.Effect.ALLOW,
                        principals=[_iam.AccountRootPrincipal()],
                        actions= ["kms:*"],
                        resources= ["*"]
                    )
                    ]
            )
        )
        cfn_func = edbIrisDDWKMSKey.node.default_child
        cfn_func.override_logical_id("edbIrisDDWKMSKey")
        edbIrisDDWKMSAlias = _kms.Alias(
            self,
            "edbIrisDDWKMSAlias",
            alias_name= "alias/aws-ddw-sm-kms",
            target_key= edbIrisDDWKMSKey
        )
        cfn_func = edbIrisDDWKMSAlias.node.default_child
        cfn_func.override_logical_id("edbIrisDDWKMSAlias")

        edbIrisDDWESIPortalSecretReference = _secretsmanager.CfnSecret(
            self,
            "edbIrisDDWESIPortalSecretReference",
            description= "Secret for Deal Development Workbench ESI Portal.",
            name= "edb-iris-ddw-esi-portal-reference",
            kms_key_id= edbIrisDDWKMSKey.key_id,
            secret_string= "empty"
        )


######################################### Managed Policies ###################################


        mpDQARedshiftDataPolicy = _iam.ManagedPolicy(
            self,
            "mpDQARedshiftDataPolicy",
            description=  "DQA policy for Redshift Data API operations",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[
                        "redshift-data:CancelStatement",
                        "redshift-data:GetStatementResult",
                        "redshift-data:List*",
                        "redshift-data:Describe*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ "*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[
                        "redshift-data:Get*",
                        "redshift-data:BatchExecuteStatement",
                        "redshift-data:ExecuteStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    )
                ]
            )
        )
        cfn_func = mpDQARedshiftDataPolicy.node.default_child
        cfn_func.override_logical_id("mpDQARedshiftDataPolicy")

        mpEdbIrisS3ExplrtryPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3ExplrtryPolicy",
            managed_policy_name="edb-iris-s3-explrtry",
            description=  "EDB IRIS policy for S3 exploratory bucket",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[
                        "s3:ListBucket"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [ 
                        f"arn:aws:s3:::lly-edp-explrtry-{params['pBucketPrefix']}"]
                    ),
                    _iam.PolicyStatement(
                    actions=[
                        "s3:PutObject",
                        "s3:GetObject",
                        "s3:DeleteObject",
                        "s3:DeleteObjectVersion",
                        "s3:ListBucketMultipartUploads",
                        "s3:PutObjectVersionTagging",
                        "s3:GetObjectAcl",
                        "s3:GetObjectVersionAcl",
                        "s3:GetObjectTagging",
                        "s3:PutObjectTagging",
                        "s3:GetObjectVersion"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [ 
                        f"arn:aws:s3:::lly-edp-explrtry-{params['pBucketPrefix']}/AWB/002d74c0a94198e8ce66114d95a3a3",
                        f"arn:aws:s3:::lly-edp-explrtry-{params['pBucketPrefix']}/AWB/002d74c0a94198e8ce66114d95a3a3/*",
                        f"arn:aws:s3:::lly-edp-explrtry-{params['pBucketPrefix']}/AWB/dc7ca292d5efdda8f64feed23a7dd4",
                        f"arn:aws:s3:::lly-edp-explrtry-{params['pBucketPrefix']}/AWB/dc7ca292d5efdda8f64feed23a7dd4/*"
                    ]
                    )
                            
                ]
            )
        )
        cfn_func = mpEdbIrisS3ExplrtryPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3ExplrtryPolicy")

        mpEdbIrisRadAwbPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisRadAwbPolicy",
            managed_policy_name= "mp-edb-iris-rad-awb",
            description=  "EDB IRIS policy for rebate anomoly detection role",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[
                        "logs:DescribeLogGroups"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "logs:DescribeLogStreams",
                                "logs:FilterLogEvents"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/sagemaker/ProcessingJobs:*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "logs:GetLogEvents"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:/aws/sagemaker/ProcessingJobs:log-stream:rev-def-rebate-*"]
                    )
                ]
            )
        )

        cfn_func = mpEdbIrisRadAwbPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisRadAwbPolicy")

        # Attach the policy to the role
        # role = _iam.Role.from_role_name(self, "aws_awb_revenuede", role_name="aws_awb_revenuede_002d74c0a94198e8ce66114d95a3a3")
        role = _iam.Role.from_role_arn(self, "aws_awb_revenuede", role_arn=f"arn:aws:iam::{config.deploy_env.account}:role/aws_awb_revenuede_002d74c0a94198e8ce66114d95a3a3")
        role.add_managed_policy(mpEdbIrisRadAwbPolicy)

        mpDQAStateMachinePolicy = _iam.ManagedPolicy(
            self,
            "mpDQAStateMachinePolicy",
            managed_policy_name="dqa-managed-policy-statemachine",
            description=  "IRIS SQA policy for State Machine",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_dqa*",
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_dqa*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpDQAStateMachinePolicy.node.default_child
        cfn_func.override_logical_id("mpDQAStateMachinePolicy")


        mpDQAGlueJobPolicy = _iam.ManagedPolicy(
            self,
            "mpDQAGlueJobPolicy",
            description=  "IRIS DQA policy for Glue Job",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "glue:Get*",                                "glue:BatchGetJobs",
                                "glue:ListJobs",
                              "glue:ListJobRuns",
                                "glue:StartJobRun"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_dqa*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "glue:Get*",
                                "glue:CreateConnection"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/AwsGlueDataBrew-{params['pDataQualityAutomationProjectTag']}*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "glue:ListCrawls"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/iris-dqa-*"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpDQAGlueJobPolicy.node.default_child
        cfn_func.override_logical_id("mpDQAGlueJobPolicy")

        mpDQALambdaPolicy = _iam.ManagedPolicy(
            self,
            "mpDQALambdaPolicy",
            managed_policy_name="dqa-managed-policy-lambda",
            description=  "IRIS SQA policy for Lambda",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[   "lambda:InvokeAsync",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_dqa_*",
                      f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*",
                      f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:RedShift-secrets-rotation"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_dqa_*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpDQALambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpDQALambdaPolicy")


        mpDQADatabrewPolicy = _iam.ManagedPolicy(
            self,
            "mpDQADatabrewPolicy",
            managed_policy_name="dqa-managed-policy-databrew",
            description=  "IRIS SQA policy for Databrew",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewlist'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdescribe'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-dqa-ds*",
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-dqa-rcp*",
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-dqa-job*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdatasetcrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-dqa-ds*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewrecipecrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-dqa-rcp*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewjobcrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-dqa-job*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpDQADatabrewPolicy.node.default_child
        cfn_func.override_logical_id("mpDQADatabrewPolicy")

        mpDQAS3RWPolicy = _iam.ManagedPolicy(
            self,
            "mpDQAS3RWPolicy",
            managed_policy_name="dqa-managed-policy-s3",
            description=  "IRIS DQA policy for S3 Config",
            document= _iam.PolicyDocument(
                statements=[
                    _iam.PolicyStatement(
                        actions= [ "s3:List*"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::{params['ArtifactBucket']}*"
                            ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}*"
                            ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*"
                            ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=[   "s3:PutObject",
                                    "s3:GetObject",
                                    "s3:DeleteObject",
                                    "s3:ListBucketMultipartUploads",
                                    "s3:RestoreObject",
                                    "s3:PutObjectVersionTagging",
                                    "s3:GetObjectAcl",
                                    "s3:PutObjectAcl",
                                    "s3:GetObjectVersionAcl",
                                    "s3:GetObjectTagging",
                                    "s3:PutObjectTagging",
                                    "s3:GetObjectVersion"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                        f"arn:aws:s3:::{params['ArtifactBucket']}/deploy/iris/*"
                        ,f"arn:aws:s3:::{params['ArtifactBucket']}/iris/*"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}/deploy/iris/*"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}/iris/*"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/data_quality_automation/*"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/data_quality_automation/temp_dataset_output/*"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpDQAS3RWPolicy.node.default_child
        cfn_func.override_logical_id("mpDQAS3RWPolicy")

        mpBRGLambdaPolicy =  _iam.ManagedPolicy(
            self,
            "mpBRGLambdaPolicy",
            managed_policy_name= "brg-managed-policy-lambda",
            description= "IRIS BRG policy for Lambda",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= ["lambda:InvokeAsync",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_brg_*"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_monitoring_metric_publish"
                                ]
                ),
                _iam.PolicyStatement(
                    actions= [  "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_brg_*"
                                ,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:edb_iris_brg_*"],
                )
                ]
            )
        )
        cfn_func = mpBRGLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpBRGLambdaPolicy")

        mpBIAS3ConfROPolicy =  _iam.ManagedPolicy(
            self,
            "mpBIAS3ConfROPolicy",
            managed_policy_name= "bia-conf-s3-policy",
            description= "BIA Service policy for ibu midas data S3",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= [ "s3:GetBucketLocation",
                                "s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                                f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}*"
                                ]
                ),
                _iam.PolicyStatement(
                    actions= [  "s3:GetObject",
                                "s3:ListBucketMultipartUploads",
                                "s3:GetObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:GetObjectVersion"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/data_products_midas/*"
                    ],
                )
                ]
            )
        )

        mpBIAS3RefinedROPolicy =  _iam.ManagedPolicy(
            self,
            "mpBIAS3RefinedROPolicy",
            managed_policy_name= "bia-refined-s3-policy",
            description= "BIA Service policy for S3",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= [ "s3:GetBucketLocation",
                                "s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*",
                                f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}*"
                                ]
                ),
                _iam.PolicyStatement(
                    actions= [  "s3:ListBucketMultipartUploads",
                                "s3:PutObject",
                                "s3:GetObject",
                                "s3:DeleteObject"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_zaidyn_omnichannel/*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_ama_physicians_masterfile_us/*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/campaign_contracting_lists/*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mlr_brand_specialties_us/bas/inbox/",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mlr_brand_specialties_us/ttp/data/inbox/",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lilly_mdm/hcp_common_and_standard/data/inbox/",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/campaign_contracting_lists/out/email_execution_list/",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/archive/zs/",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/out/medscape_bse_eng_gloss/*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_zaidyn_omnichannel/*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_omnichannel_field_suggestions/commercial_reporting/*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_campaign_metadata/data/processed/*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_campaign_metadata/campaign_extract/data/processed/*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_elaad/*", #RITM5150675
                                f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eph/Iqvia_commercial_customer_profiles/*" #RITM5119833
                                
                                ],
                ),
                _iam.PolicyStatement(
                    actions= [  "s3:GetObject",
                                "s3:ListBucketMultipartUploads",
                                "s3:GetObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:GetObjectVersion"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/campaign_contracting_lists/out/execution_lists_medicalprospecting/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/archive/veeva_alignments/dynamic_targeting/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/archive/alignment_hierarchy/dynamic_targeting/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ascension_hcp_us/*", #RITM4030576
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hibbert_hcp_consent/*", #RITM4030576
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mlr_brand_specialties_us/*", #RITM4030576
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/master_target_lists_us/*", #RITM4030576
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/physician_exclusion_us/*", #RITM4030576
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/verso/out/bia/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/verso/campaign_target_list/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/adobe_experience_manager_content_metadata/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/everyday_health_omnichannel/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_lusa_access_monitor_restricted/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_campaign_metadata/*", #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_omnichannel_field_suggestions/*", #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*", #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",  #RITM4232591
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lilly_mdm/hcp_common_and_standard/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/list_management/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/shared_zs/archive/gccp_consent/gccp_consent_archived_data/*", #RITM4398046
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/HCP/*", #RITM4398046
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/out/archive/hcp_universe/hcp_archived_data/*", #RITM4398046
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/out/archive/veeva_alignments/HCP_REP/*", #RITM4398046
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/list_management/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions_restricted/media_cost_data/data/inbox/*", #RITM5154371
                        f"arn:aws:s3:::s3://lly-edp-refined-us-east-2-prod/publicis_ehr_marketing_interactions/", #RITM4382283
                        f"arn:aws:s3:::s3://lly-edp-refined-us-east-2-prod/match_list_lusa_marketing_restricted/", #RITM4382283
                        f"arn:aws:s3:::s3://lly-edp-refined-us-east-2-prod/canopy_lusa_campaign_metadata/", #RITM4382283
                        f"arn:aws:s3:::s3://lly-edp-refined-us-east-2-prod/lusa_lilly_play/", #RITM4382283
                        f"arn:aws:s3:::s3://lly-edp-raw-us-east-2-prod/lilly_mdm/", #RITM4382283
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_omnichannel_field_suggestions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/adobe_experience_manager_content_metadata/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/adobe_experience_manager_content/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/verso/archive/zs/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/salesforce_marketing_cloud/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/veeva_medcomms/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/embase/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/medfocus_marl/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/adobe_experience_manager_content_metadata/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/adobe_experience_manager_content/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/archive/zs/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/salesforce_marketing_cloud/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/veeva_medcomms/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/embase/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/medfocus_marl/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*", #RITM4555805
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/omms_engagement_glossary/*", #RITM4897367
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/veeva_vvpm/*",#RITM4925630
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_campaign_metadata/campaign_extract/data/processed/*"
                        ],
                )
                ]
            )
        )
        cfn_func = mpBIAS3RefinedROPolicy.node.default_child
        cfn_func.override_logical_id("mpBIAS3RefinedROPolicy")
        
        mpBIAS3RefinedROPolicy1 =  _iam.ManagedPolicy(
            self,
            "mpBIAS3RefinedROPolicy1",
            managed_policy_name= "bia-refined-s3-policy-1",
            description= "BIA Service policy for S3",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= [ "s3:GetBucketLocation",
                                "s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*",
                                f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}*",
                                f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}*"
                                ]
                ),
                _iam.PolicyStatement(
                    actions= [  "s3:ListBucketMultipartUploads", 
                                "s3:PutObject",
                                "s3:GetObject",
                                "s3:DeleteObject"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_zaidyn_omnichannel/*",
                                f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/met_extract/*", #RITM5954107
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/txo_oncology/*" #RITM5821335 
                                ],
                ),
                _iam.PolicyStatement(
                    actions= [  "s3:GetObject",
                                "s3:ListBucketMultipartUploads",
                                "s3:GetObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:GetObjectVersion"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/verso/campaign_contracting_lists/out/execution_lists_medicalprospecting/*",
			    	f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/miba_oncology/*", #RITM5556627
			    	f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/foundation_medicine/*", #RITM5939897
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/florida_cancer_specialist/SLL_DEMOGRAPHICS_processed/*",#RITM5949338
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/florida_cancer_specialist/SLL_LABS_processed/*",#RITM5949338
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/florida_cancer_specialist/SLL_LOT_processed/*"#RITM5949338
                        ],
                )
                ]
            )
        )

        mpBASRedshiftDataPolicy = _iam.ManagedPolicy(
            self,
            "mpBASRedshiftDataPolicy",
            description= "BAS policy for Redshift Data API operations",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=["redshift-data:GetStatementResult",
                            "redshift-data:CancelStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "redshift-data:List*",
                                "redshift-data:Describe*",
                                "redshift-data:Get*",
                                "redshift-data:BatchExecuteStatement",
                                "redshift-data:ExecuteStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpBASRedshiftDataPolicy.node.default_child
        cfn_func.override_logical_id("mpBASRedshiftDataPolicy")

        mpLMLambdaPolicy =  _iam.ManagedPolicy(
            self,
            "mpLMLambdaPolicy",
            managed_policy_name= "lm-managed-policy-lambda",
            description= "IRIS LM policy for Lambda",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=  [ "lambda:InvokeAsync",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_omt_*",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_omt_*",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:RedShift-secrets-rotation"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "logs:CreateLogStream",
                              "logs:CreateLogGroup",
                              "logs:AssociateKmsKey",
                              "logs:PutLogEvents",
                              "logs:Describe*",
                              "logs:FilterLogEvents",
                              "logs:Get*",
                              "logs:List*",
                              "logs:StartQuery",
                              "logs:TestMetricFilter"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_omt_*"]
                    )
                ]
            )
        )
        cfn_func = mpLMLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpLMLambdaPolicy")

        mpLMS3RWPolicy =  _iam.ManagedPolicy(
            self,
            "mpLMS3RWPolicy",
            managed_policy_name= "lm-managed-policy-s3",
            description= "IRIS LM policy for S3 Config",
            document= _iam.PolicyDocument(
			statements= [_iam.PolicyStatement(
                    actions=  [ "s3:ListBucket*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:s3:::{config.artifact_bucket}*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:PutObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:s3:::{params['ArtifactEdbBucket']}",
                                f"arn:aws:s3:::{params['ArtifactEdbBucket']}/iris/*",
                                f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws-glue/*",
                                f"arn:aws:s3:::{params['ArtifactEdbBucket']}/edb/*",
                                f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws/*",
                                f"arn:aws:s3:::{params['ArtifactEdbBucket']}/redshift/*"]
                    ),
                    _iam.PolicyStatement(
                    actions=["s3:ListBucketMultipartUploads"],
                    effect= _iam.Effect.ALLOW,
                    resources=[f"arn:aws:s3:::{config.artifact_bucket}",
                                f"arn:aws:s3:::{params['ArtifactEdbBucket']}"]
                    )
                ]
            )
        )
        cfn_func = mpLMS3RWPolicy.node.default_child
        cfn_func.override_logical_id("mpLMS3RWPolicy")

        if config.env in ['dev']:
            prod_grp= f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/*:*"
        else:
            prod_grp = f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/omt-job-*:*"

        mpLMGlueJobPolicy =  _iam.ManagedPolicy(
            self,
            "mpLMGlueJobPolicy",
            description= "IRIS LM policy for Glue Job",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=  [  "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [prod_grp]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "glue:Get*",
                               "glue:BatchGetJobs",
                               "glue:ListJobs",
                               "glue:ListJobRuns",
                               "glue:StartJobRun"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_omt*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_omt*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_verso*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/omt_lm"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpLMGlueJobPolicy.node.default_child
        cfn_func.override_logical_id("mpLMGlueJobPolicy")

        mpLMRedshiftDataPolicy = _iam.ManagedPolicy(
            self,
            "mpLMRedshiftDataPolicy",
            description= "LM policy for Redshift Data API operations",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=["redshift-data:GetStatementResult",
                            "redshift-data:CancelStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "redshift-data:List*",
                                "redshift-data:Describe*",
                                "redshift-data:Get*",
                                "redshift-data:BatchExecuteStatement",
                                "redshift-data:ExecuteStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    )
                ]
            )
        )
        cfn_func = mpLMRedshiftDataPolicy.node.default_child
        cfn_func.override_logical_id("mpLMRedshiftDataPolicy")

        mpBRMSRedshiftDataPolicy = _iam.ManagedPolicy(
            self,
            "mpBRMSRedshiftDataPolicy",
            description=  "BRMS policy for Redshift Data API operations",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  "redshift-data:List*",
                                "redshift-data:Describe*",
                                "redshift-data:GetStatementResult",
                                "redshift-data:CancelStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ "*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "redshift-data:Get*",
                                "redshift-data:BatchExecuteStatement",
                                "redshift-data:ExecuteStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    )
                ]
            )
        )
        cfn_func = mpBRMSRedshiftDataPolicy.node.default_child
        cfn_func.override_logical_id("mpBRMSRedshiftDataPolicy")

        if config.env in ['dev']:
            BAS_resrc = f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/*:*"
        else :
            BAS_resrc = f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/bas-job-*:*"

        mpBASGlueJobPolicy = _iam.ManagedPolicy(
            self,
            "mpBASGlueJobPolicy",
            description= "IRIS BAS policy for Glue Job",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[    "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [BAS_resrc
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[    "glue:Get*",                                "glue:BatchGetJobs",
                                "glue:ListJobs",
                              "glue:ListJobRuns",
                                "glue:StartJobRun"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_bas*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_lusa_bas*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_bas*"
                                ]
                    ),
                     _iam.PolicyStatement(
                    actions=[  "glue:Get*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/aws_lusa_bas*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/AwsGlueDataBrew-{params['pDatabrewProjectTag']}*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpBASGlueJobPolicy.node.default_child
        cfn_func.override_logical_id("mpBASGlueJobPolicy")

        mpBRMSGlueJobPolicy = _iam.ManagedPolicy(
            self,
            "mpBRMSGlueJobPolicy",
            description=  "IRIS BRMS policy for Glue Job",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[ "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "glue:Get*",                                "glue:BatchGetJobs",
                                "glue:ListJobs",
                              "glue:ListJobRuns",
                                "glue:StartJobRun"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_brms*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "glue:Get*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/AwsGlueDataBrew-{params['pDatabrewProjectTag']}*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpBRMSGlueJobPolicy.node.default_child
        cfn_func.override_logical_id("mpBRMSGlueJobPolicy")

        mpBRMSStateMachinePolicy = _iam.ManagedPolicy(
            self,
            "mpBRMSStateMachinePolicy",
            managed_policy_name=  "brms-managed-policy-statemachine",
            description=  "IRIS BRMS policy for State Machine",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_brms*",
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_brms*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpBRMSStateMachinePolicy.node.default_child
        cfn_func.override_logical_id("mpBRMSStateMachinePolicy")

        mpBASLambdaPolicy = _iam.ManagedPolicy(
            self,
            "mpBASLambdaPolicy",
            managed_policy_name= "bas-managed-policy-lambda",
            description= "IRIS BAS policy for Lambda",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[   "lambda:InvokeAsync",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_bas_*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_bas_*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:RedShift-secrets-rotation"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_bas_*"
                        ,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_bas_*"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpBASLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpBASLambdaPolicy")

        mpBRMSLambdaPolicy = _iam.ManagedPolicy(
            self,
            "mpBRMSLambdaPolicy",
            managed_policy_name=  "brms-managed-policy-lambda",
            description=  "IRIS BRMS policy for Lambda",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[   "lambda:InvokeAsync",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_brms_*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:RedShift-secrets-rotation"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "logs:CreateLogStream",
                              "logs:CreateLogGroup",
                              "logs:AssociateKmsKey",
                              "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_brms_*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpBRMSLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpBRMSLambdaPolicy")

        mpBRMSDatabrewPolicy = _iam.ManagedPolicy(
            self,
            "mpBRMSDatabrewPolicy",
            managed_policy_name=  "brms-managed-policy-databrew",
            description=  "IRIS BRMS policy for Databrew",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewlist'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdescribe'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-brms-ds*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-brms-rcp*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-brms-job*",
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdatasetcrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-brms-ds*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewrecipecrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-brms-rcp*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewjobcrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-brms-job*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpBRMSDatabrewPolicy.node.default_child
        cfn_func.override_logical_id("mpBRMSDatabrewPolicy")

        mpBASS3RWPolicy = _iam.ManagedPolicy(
            self,
            "mpBASS3RWPolicy",
            managed_policy_name= "bas-managed-policy-s3",
            description= "IRIS BAS policy for S3 Config",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[    "s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::{params['ArtifactBucket']}*"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}*"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*"
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "s3:PutObject",
                                "s3:GetObject",
                                "s3:DeleteObject",
                                "s3:PutObjectAcl",
                                "s3:RestoreObject",
                                "s3:PutObjectVersionTagging",
                                "s3:GetObjectAcl",
                                "s3:PutObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:PutObjectTagging",
                                "s3:GetObjectVersion"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
						f"arn:aws:s3:::lly-pipeline-artifacts-boftu8u8",
						f"arn:aws:s3:::lly-pipeline-artifacts-boftu8u8/iris/*",
						f"arn:aws:s3:::lly-pipeline-artifacts-boftu8u8/aws-glue/*",
						f"arn:aws:s3:::lly-pipeline-artifacts-boftu8u8/edb/*",
						f"arn:aws:s3:::lly-pipeline-artifacts-boftu8u8/aws/*",
						f"arn:aws:s3:::lly-pipeline-artifacts-boftu8u8/redshift/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mlr_brand_specialties_us/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/*",
						]
                    ),
                    _iam.PolicyStatement(
                    actions=["s3:ListBucketMultipartUploads"],
                    effect= _iam.Effect.ALLOW,
                    resources=[
                        f"arn:aws:s3:::{params['ArtifactBucket']}"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}"
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpBASS3RWPolicy.node.default_child
        cfn_func.override_logical_id("mpBASS3RWPolicy")

        mpBRMSS3RWPolicy = _iam.ManagedPolicy(
            self,
            "mpBRMSS3RWPolicy",
            managed_policy_name=  "brms-managed-policy-s3",
            description=  "IRIS BRMS policy for S3 Config",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  "s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::{params['ArtifactBucket']}*"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}*"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*"
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:PutObjectAcl",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:PutObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::{params['ArtifactBucket']}/deploy/iris/platform/brms/*"
                        ,f"arn:aws:s3:::{params['ArtifactBucket']}/aws_glue/*"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}/deploy/iris/platform/brms/*"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws_glue/*"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/brms_test/*"
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/brms_test/*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpBRMSS3RWPolicy.node.default_child
        cfn_func.override_logical_id("mpBRMSS3RWPolicy")

        mpEHRLambdaPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRLambdaPolicy",
            managed_policy_name =  "ehr-managed-policy-lambda",
            description=  "EHR policy for Lambda",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[   "lambda:InvokeAsync",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_dqa_*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_ehr_*"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[    "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_dqa_*",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_ehr_*",
                                ]
                    )
                ]
            )
        )
        cfn_func = mpEHRLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRLambdaPolicy")

        mpEHRDatabrewPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRDatabrewPolicy",
            managed_policy_name="ehr-managed-policy-databrew",
            description=  "EHR policy for Databrew",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewlist'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdescribe'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-dqa-ds*",
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-dqa-rcp*",
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-dqa-job*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdatasetcrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-dqa-ds*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewrecipecrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-dqa-rcp*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewjobcrud'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                      f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-dqa-job*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpEHRDatabrewPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRDatabrewPolicy")

        mpEHRS3RWPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRS3RWPolicy",
            managed_policy_name="ehr-managed-policy-s3",
            description=  "EHR policy for S3 Config",
            document= _iam.PolicyDocument(
                statements=[
                    _iam.PolicyStatement(
                        actions= [ "s3:List*"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::{params['ArtifactBucket']}*"
                            ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}*"
                            ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*"
                            ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=[   "s3:PutObject",
                                    "s3:GetObject",
                                    "s3:ListBucketMultipartUploads",
                                    "s3:RestoreObject",
                                    "s3:PutObjectVersionTagging",
                                    "s3:GetObjectAcl",
                                    "s3:PutObjectAcl",
                                    "s3:GetObjectVersionAcl",
                                    "s3:GetObjectTagging",
                                    "s3:PutObjectTagging",
                                    "s3:GetObjectVersion"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                          f"arn:aws:s3:::{params['ArtifactBucket']}/deploy/iris/*"
                            ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}/deploy/iris/*"
                            ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/publicis_ehr_marketing_interactions/data_quality_automation/*"
                            ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/data_quality_automation/thrshld_output/*"
                            ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/data_quality_automation/temp_dataset_output/*"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpEHRS3RWPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRS3RWPolicy")

        mpEHRStateMachinePolicy = _iam.ManagedPolicy(
            self,
            "mpEHRStateMachinePolicy",
            managed_policy_name="ehr-managed-policy-statemachine",
            description=  "EHR policy for State Machine",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_ehr*",
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_ehr*"
                    ]
                    )
                ]
            )
        )
        cfn_func = mpEHRStateMachinePolicy.node.default_child
        cfn_func.override_logical_id("mpEHRStateMachinePolicy")

        mpEHRRedshiftDataPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRRedshiftDataPolicy",
            description=  "EHR policy for Redshift Data API operations",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  "redshift-data:List*",
                              "redshift-data:Describe*",
                              "redshift-data:GetStatementResult",
                              "redshift-data:CancelStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "redshift-data:Get*",
                              "redshift-data:BatchExecuteStatement",
                              "redshift-data:ExecuteStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    )
                ]
            )
        )
        cfn_func = mpEHRRedshiftDataPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRRedshiftDataPolicy")

        mpEHRGlueJobPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRGlueJobPolicy",
            description=  "EHR policy for Glue Job",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  "glue:BatchCreatePartition",
                                "glue:BatchGetPartition",
                                "glue:CreateDatabase",
                                "glue:CreateTable",
                                "glue:Get*",                                "glue:StartCrawler",
                                "glue:UpdateConnection",
                                "glue:UpdatePartition",
                                "glue:UpdateTable"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris_dqa*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/iris-dqa-*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/iris-dqa-*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/iris-dqa-*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris_lms*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris*"
 
                               ]
                    )
                ]
            )
        )
        cfn_func = mpEHRGlueJobPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRGlueJobPolicy")

        mpEHRPiLambdaPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRPiLambdaPolicy",
            description=  "EHR PI policy for lambda Job",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[   "lambda:InvokeAsync",
							    "lambda:UpdateFunctionCode",
                                "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_ehr_pi_*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_revitl_*" 
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "iam:CreateRole",
                                "iam:PassRole",
                                "iam:ListRoleTags",
                                "iam:GetRolePolicy"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_ehr_*"
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=[    "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:PutRetentionPolicy",
                                "logs:DeleteRetentionPolicy",
                                "logs:DescribeLogGroups"
                                ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_ehr_pi_*",
                                ]
                    )
                ]
            )
        )
        cfn_func = mpEHRPiLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRPiLambdaPolicy")

        mpEHRPiS3RWPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRPiS3RWPolicy",
            managed_policy_name="ehr-pi-managed-policy-s3",
            description=  "EHR policy for S3 Config",
            document= _iam.PolicyDocument(
                statements=[
                    _iam.PolicyStatement(
                        actions= [ "s3:List*",
                                  "s3:GetBucketLocation"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}*"
                            ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=[  "s3:Put*",
                                    "s3:GetObject",
                                    "s3:DeleteObject",
                                    "s3:ListBucketMultipartUploads",
                                    ],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ehr_pi_autofill/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ehr_pi_autofill/forms_output/*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=[   "s3:RestoreObject",
                                    "s3:PutObjectVersionTagging",
                                    "s3:GetObjectAcl",
                                    "s3:PutObjectAcl",
                                    "s3:GetObjectVersionAcl",
                                    ],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ehr_pi_autofill/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ehr_pi_autofill/forms_output/*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=[   "s3:GetObjectTagging",
                                    "s3:PutObjectTagging",
                                    "s3:GetObjectVersion",
                                    "s3:GetObjectVersionTagging",
                                    "s3:PutLifecycleConfiguration",
                                    "s3:GetLifecycleConfiguration"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ehr_pi_autofill/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ehr_pi_autofill/forms_output/*"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpEHRPiS3RWPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRPiS3RWPolicy")

        mpEHRMiscPolicy = _iam.ManagedPolicy(
            self,
            "mpEHRMiscPolicy",
            managed_policy_name="ehr-managed-policy-misc",
            description=  "EHR policy for EC2",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  
                        "ec2:Describe*",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:CreateTags",
                        "ec2:DeleteTags"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ec2:*:*:instance/*",
                        "arn:aws:ec2:*:*:security-group/*",
                        "arn:aws:ec2:*:*:network-interface/*"
                    ],
                    conditions={
                        "ForAllValues:StringEquals": {
                            "aws:TagKeys": "aws-glue-service-resource"
                        }
                    }
                    )
                ]
            )
        )
        cfn_func = mpEHRMiscPolicy.node.default_child
        cfn_func.override_logical_id("mpEHRMiscPolicy")

        mpCCPAStateMachinePolicy = _iam.ManagedPolicy(
            self,
            "mpCCPAStateMachinePolicy",
            managed_policy_name= "ccpa-managed-policy-statemachine",
            description=  "IRIS CCPA policy for State Machine",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_ccpa*"
                        ,f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_ccpa*"
                        ,f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_redshift_trigger_sp_state_machine"
                        ,f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_redshift_trigger_sp_state_machine"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[    "events:PutTargets",
                                "events:PutRule",
                                "events:DescribeRule"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                         f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpCCPAStateMachinePolicy.node.default_child
        cfn_func.override_logical_id("mpCCPAStateMachinePolicy")

        mpCCPAGluePolicy = _iam.ManagedPolicy(
            self,
            "mpCCPAGluePolicy",
            managed_policy_name= "ccpa-managed-policy-glue",
            description=  "IRIS CCPA policy for using Glue",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['glue'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_ccpa*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris_ccpa*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris_ccpa*"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[
                        "glue:BatchGetJobs",
                        "glue:BatchStopJobRun",
                        "glue:Get*",
                        "glue:ListJob",
                        "glue:ListJobs",
                        "glue:ListJobRuns",
                        "glue:StartJobRun",
                        "glue:UpdateJob"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                          f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_ccpa*"
                                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "ec2:Describe*"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  
                        "ec2:Describe*",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:CreateTags",
                        "ec2:DeleteTags"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ec2:*:*:instance/*",
                        "arn:aws:ec2:*:*:security-group/*",
                        "arn:aws:ec2:*:*:network-interface/*"
                    ],
                    conditions={
                        "ForAllValues:StringEquals": {
                            "aws:TagKeys": "aws-glue-service-resource"
                        }
                    }
                    )
                ]
            )
        )
        cfn_func = mpCCPAGluePolicy.node.default_child
        cfn_func.override_logical_id("mpCCPAGluePolicy")

        mpCCPALambdaPolicy = _iam.ManagedPolicy(
            self,
            "mpCCPALambdaPolicy",
            managed_policy_name= "ccpa-managed-policy-lambda",
            description=  "IRIS CCPA policy for Lambda",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['lambda'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_ccpa*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_ccpa_dsar_glue_trigger:*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_trigger_state_machine"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_ccpa*",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_inc_snow",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_trigger_state_machine",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:*",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/error:*",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/testconnection/output/edb_iris_ccpa*",
                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/testconnection/error/edb_iris_ccpa*"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpCCPALambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpCCPALambdaPolicy")

        mpEdbIrisKmsRWPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisKmsRWPolicy",
            description= "IRIS RW Policy for KMS",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= ["kms:Decrypt",
                                "kms:Encrypt",
                                "kms:DescribeKey",
                                "kms:GenerateDataKey*",
                                "kms:ReEncrypt*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pKmsKeyIrisDMS']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{config.powerbi_jira_secret_kms_key_id}"
                                ]
                ),
                _iam.PolicyStatement(
                    actions= [ "kms:ListKeys",
                                "kms:ListAliases"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                ),
                _iam.PolicyStatement(
                    actions= [  "kms:DisableKey",
                                "kms:ScheduleKeyDeletion"],
                    effect= _iam.Effect.DENY,
                    resources= ["*"]
                )
                ]
            )
        )
        cfn_func = mpEdbIrisKmsRWPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisKmsRWPolicy")

        mpEdbIrisReadMinusS3Policy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisReadMinusS3Policy",
            description= "IRIS RO Policy for Resources excluding S3",
            document= _iam.PolicyDocument(
                statements= [
                    _iam.PolicyStatement(
                    actions=  [ "access-analyzer:ValidatePolicy",
                              "athena:ListDataCatalogs",
                              "athena:ListWorkgroups",
                              "codebuild:BatchGet*",
                              "codebuild:List*",
                              "codedeploy:List*",
                              "codepipeline:List*",
                              "dms:Describe*",
                              "dms:List*",
                              "ec2:Describe*",
                              "ec2:SearchTransitGatewayRoutes",
                              "ec2messages:Get*",
                              "ecr-public:List*",
                              "ecr-public:Describe*",
                              "ecr:List*",
                              "ecr:Describe*",
                              "ecs:List*",
                              "ecs:Describe*",
                              "events:Describe*",
                              "events:List*",
                              "glue:GetCrawler",
                              "glue:GetCrawlerMetrics",
                              "glue:GetCrawlers",
                              "lambda:List*",
                              "logs:Describe*",
                              "logs:ListTagsLogGroup",
                              "logs:TestMetricFilter",
                              "rds:Describe*",
                              "rds:List*",
                              "redshift:Describe*",
                              "redshift:View*",
                              "redshift-data:Describe*",
                              "redshift-data:List*",
                              "secretsmanager:Describe*",
                              "secretsmanager:List*",
                              "sns:Check*",
                              "sns:Get*",
                              "sns:List*",
                              "sqs:List*",
                              "ssm:Describe*",
                              "ssm:List*",
                              "states:Describe*",
                              "states:List*",
                              "tag:Get*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "apigateway:GET"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:apigateway:{config.deploy_env.region}::/restapis/*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "cloudformation:Describe*",
                              "cloudformation:Detect*",
                              "cloudformation:Estimate*",
                              "cloudformation:List*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "cloudformation:GetTemplate",
                              "cloudformation:GetStackPolicy",
                              "cloudformation:GetStack",
                              "cloudformation:GetStackResources",
                              "cloudformation:Preview*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/Iris*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/pipeline-lusa*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/Infra-ECS*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/pipeline-iris*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/buit-aws-core*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/IrisLusa*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/iris-verso*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/IrisCore*/*",
                        f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/iris-*/*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "cloudwatch:Describe*",
                              "cloudwatch:Get*",
                              "cloudwatch:List*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:cloudwatch:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "codepipeline:Get*",
                              "codepipeline:StartPipelineExecution"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "connect:Describe*",
                              "connect:List*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:connect:{config.deploy_env.region}:{config.deploy_env.account}:instance/*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "ec2:Get*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:ec2:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "ecr-public:Get*",
                              "ecr-public:BatchCheck*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:ecr-public::{config.deploy_env.account}:repository/edb-iris*",
                        f"arn:aws:ecr-public::{config.deploy_env.account}:repository/edb_iris*",
                        f"arn:aws:ecr-public::{config.deploy_env.account}:repository/iris-*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "ecr:Get*",
                              "ecr:BatchCheck*",
                              "ecr:BatchGet*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb-iris*",
                        f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb_iris*",
                        f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/iris-*",
                        f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/pipeline-iris*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "glue:BatchGetCrawlers",
                              "glue:BatchGetJobs",
                              "glue:Get*",
                              "glue:ListDatabases",
                              "glue:ListTables",
                              "glue:ListJobs",
                              "glue:ListJobRuns",
                              "glue:ListCrawlers"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "iam:Generate*",
                              "iam:Get*",
                              "iam:List*",
                              "iam:Simulate*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:iam::{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "kms:Get*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRDSSecretKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMedbKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisSmKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisDDWKMSKey']}"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "lambda:Get*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "logs:FilterLogEvents",
                              "logs:Get*",
                              "logs:StartQuery"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "sagemaker:Describe*",
                              "sagemaker:Get*",
                              "sagemaker:List*",
                              "sagemaker:Search"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:sagemaker:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "ses:SendEmail",
                              "ses:SendRawEmail"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ses:us-east-1:539199905087:identity/lilly.com"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "sqs:Receive*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:sqs:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "ssm:Get*",
                              "ssm:GetParameter",
                              "ssm:Put*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris*",
                        f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/iris*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "states:Get*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "databrew:Describe*",
                              "databrew:List*",
                              "databrew:StartJobRun"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "databrew:Delete*",
                              "databrew:BatchDeleteRecipeVersion",
                              "databrew:Update*",
                              "databrew:StopJobRun"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-dqa-*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-dqa-*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-dqa-*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:ruleset/iris-dqa-*",
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "lambda:Update*",
                              "lambda:Invoke*",
                              "glue:Update*"
                           ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_global_vvpm_gluejob_trigger_lambda",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/omnichannel_global_data_raw_to_refine"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisReadMinusS3Policy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisReadMinusS3Policy")

        mpEdbIrisConsolePolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisConsolePolicy",
            description= "IRIS S3 Console Policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "s3:ListAllMyBuckets",
                                "s3:GetBucketLocation",
                                "s3:ListAccessPoints",
                                "cloudwatch:GetMetricData",
                                "cloudwatch:GetMetricStatistics",
                                "cloudwatch:GetMetricStream",
                                "cloudwatch:GetMetricWidetImage",
                                "cloudwatch:GetMetricWidgetImage",
                                "cloudwatch:GetService",
                                "cloudwatch:GetServiceData",
                                "cloudwatch:PutMetricData"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [  "cloudwatch:PutDashboard",
                                "cloudwatch:DeleteDashboards"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:cloudwatch::{config.deploy_env.account}:dashboard/edb_iris*" ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [  "ssm:GetParameter"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris*" ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [  "ecr:CompleteLayerUpload",
                                "ecr:UploadLayerPart",
                                "ecr:InitiateLayerUpload",
                                "ecr:BatchCheckLayerAvailability",
                                "ecr:PutImage"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb-iris*" ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisConsolePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisConsolePolicy")

        mpEdbIrisSecretsPolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisSecretsPolicy",
            description=  "DQA policy for using secrets manager",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret",
                              "secretsmanager:PutSecretValue",
                              "secretsmanager:UpdateSecret",
                              "secretsmanager:RotateSecret"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-SystemUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-bas-SystemUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-user-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsredshift-rsadmin-iris-edb-{params['pEnvironment']}-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsrds-iris-dms-flex-load-user-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsrds-gdm-aurora-pgsql-iris-edb-rds-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-janrain-api-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-lillyplay-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:iris_jira_service_account-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:itqs-testing-iris-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:iris_monitoring_webhook_url-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:iris_srvc_account_pat-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-redshift-tableau-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_tableau_pds_{params['pEnvironment']}_refresh_pat-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraLash-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-ddw-esi-portal-reference-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-TurboReportingUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_turbo_google_maps_api_key-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-STRReportingUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_tableau_pds_{params['pEnvironment']}_refresh_csp-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-PayerReportingUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_prd300_oracle_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_prd300_csu_oracle_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_prd300_gmu_oracle_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_prd300_oracle_db_phh_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_prd287_oracle_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_adm_csp_bus_user_secret-?????"
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsTableau-iris-edb-{params['pEnvironment']}-PATAFReportingSystem-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_tableau_data_source_refresh_pat-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-oracle-rdr-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_g3p_mtl_sub_user_aurora_db_secret-??????",                
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_g3p_cust_sub_user_aurora_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:gems_insight_sharepnt_secret_copay-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-PayerReportingSecretRotation-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ms_teams_pataf_monitoring_webhook_url-??????",  
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_snow_api_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:aws-lusa-iris-jira-powerbi-token-api-creds-??????",
			            f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_wrkradm_aurora_db_secret-??????"
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsedb-auroradb-secrets-??????"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "kms:Decrypt",
                              "kms:GenerateDataKey"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRdsKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRDSSecretKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMedbKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisSmKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisDDWKMSKey']}"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "ssm:GetParameter",
                              "ssm:GetParameters",
                              "ssm:GetParametersByPath",
                              "ssm:PutParameter"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "s3:DeleteBucketLifecycle",
                              "s3:Get*",
                              "s3:PutBucketLifecycleConfiguration",
                              "s3:PutLifecycleConfiguration",
                              "s3:PutBucketLifecycle"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::{params['ArtifactBucket']}",
                        f"arn:aws:s3:::{params['ArtifactEdbBucket']}"
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=["secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret",
                              "secretsmanager:PutSecretValue",
                              "secretsmanager:UpdateSecret",
                              "secretsmanager:RotateSecret"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:omnisource-cit-db-system-user-??????"],
                    conditions = {
                              "StringEquals": {
                                  "aws:PrincipalArn": [
                                      {
                                          "Fn::Sub": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_prd_secrets_manager"
                                      }
                                  ]
                              }
                          }
                    ),
                    _iam.PolicyStatement(
                    actions=["kms:Decrypt",
                              "kms:GenerateDataKey"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['OmniSourceKMSKey']}"],
                    conditions = {
                              "StringEquals": {
                                  "aws:PrincipalArn": [
                                      {
                                          "Fn::Sub": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_prd_secrets_manager"
                                      }
                                  ]
                              }
                          }
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisSecretsPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisSecretsPolicy")

        mpEdbIrisSecretsPolicyTwo = _iam.ManagedPolicy(
            self,
            "mpEdbIrisSecretsPolicyTwo",
            description= "IRIS policy 2 for using secrets manager",
            document= _iam.PolicyDocument(
                statements= [
                    _iam.PolicyStatement(
                    actions=[ "secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret",
                              "secretsmanager:PutSecretValue",
                              "secretsmanager:UpdateSecret",
                              "secretsmanager:RotateSecret"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraDHCsp-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraSonexusCRM-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraIqviaClaims-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraEversanaCRM-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraEversana-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_hbt_sub_user_aurora_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_phh_sub_user_aurora_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:adm_turbo_sys_acc_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-LMSystemUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraMDM-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraMDMAlignment-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraWrkr-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-auroraMDMCustomer-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_lms_refined_rds_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ve_alignment_edb_aurora_db_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-csp-edwin-Secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-ifp-Sharepoint-secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-Lightspeed-secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_iq_CT_GOV_secret_prd-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_rft_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_optum_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_product_list_cross_vendor_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_maat_rft_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_laad_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_humana_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_fcdr_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_esi_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_crossvendor_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_cmm_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_caremark_report_refresh_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_business_case_summary_report_refresh_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_laad_report_refresh_secret",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_maat_rds_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_iq_GSIP_DB_secret_prd-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:iqviaPGPPrivate-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_pataf_paysign_ptr_claims_secret-??????",
						f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_csp_edwin_dbx_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:G2N_Anaplan-secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:omnisource_prefect_sso_secret-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_csp_pgp_public_key-??????"
						
                    ]),
                    _iam.PolicyStatement(
                    actions=[ "kms:Decrypt",
                              "kms:Encrypt",
                              "kms:DescribeKey",
                              "kms:GenerateDataKey*",
                              "kms:ReEncrypt*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
			f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisSmKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pOmniSourcePrefectSsoKmsKey']}"
                    ]),
                    _iam.PolicyStatement(
                    actions=["iam:CreateAccessKey",
							 "iam:UpdateAccessKey",
							 "iam:DeleteAccessKey",
							 "iam:TagUser"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:iam::346644684160:user/edb_iris_buids_splunk_user_prod"
                    ])                  
                ]
            )
        )
        cfn_func = mpEdbIrisSecretsPolicyTwo.node.default_child
        cfn_func.override_logical_id("mpEdbIrisSecretsPolicyTwo")

        mpEdbEPHSecretsPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbEPHSecretsPolicy",
            description= "IRIS policy for using secrets manager",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[   "secretsmanager:GetSecretValue",
                                "secretsmanager:DescribeSecret"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:secretsmanager::{config.deploy_env.account}:secret:aws-lusa-verso-edb-oauth2-Secret-??????"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "secretsmanager:ListSecrets"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "kms:Decrypt",
                                "kms:GenerateDataKey"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:kms::{config.deploy_env.account}:key/{params['pVersoSmKmsKey']}"]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "ssm:PutParameter",
                                "ssm:GetParameter"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:ssm::{config.deploy_env.account}:parameter/iris_eph_hco_export_lambda*",
                        f"arn:aws:ssm::{config.deploy_env.account}:parameter/iris_eph_affiliation_export_lambda*"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpEdbEPHSecretsPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbEPHSecretsPolicy")

        mpIrisHospitalAnomalyDetectionPolicy = _iam.ManagedPolicy(
            self,
            "mpIrisHospitalAnomalyDetectionPolicy",
            managed_policy_name= "IRIS_hospital_anomaly_detection_policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  
                         "s3:GetObject",
                         "s3:GetObjectAcl",
                         "s3:GetObjectVersionAcl",
                         "s3:GetObjectTagging",
                         "s3:GetObjectVersion",
                         "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}:/hospital_anomaly_detection/*"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  
                         "kms:Decrypt",
                         "kms:Encrypt",
                         "kms:DescribeKey",
                         "kms:GenerateDataKey",
                         "kms:ReEncrypt"
                                ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}"
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  
                         "secretsmanager:GetSecretValue",
                         "secretsmanager:DescribeSecret",
                         "secretsmanager:PutSecretValue",
                         "secretsmanager:UpdateSecret",
                         "secretsmanager:RotateSecret"
                                ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:adm_turbo_sys_acc_secret-??????"
                        ]
                    )
                ]
            )
        )
        
        cfn_func = mpIrisHospitalAnomalyDetectionPolicy.node.default_child
        cfn_func.override_logical_id("mpIrisHospitalAnomalyDetectionPolicy")

        # Attach the policy to the role
        role = _iam.Role.from_role_name(self, "aads_awb_aws_sm_role", role_name="aads_awb_aws_sm_f81b167d3cbcd3dd186c72001aa684")
        role.add_managed_policy(_iam.ManagedPolicy.from_aws_managed_policy_name("IRIS_hospital_anomaly_detection_policy"))

        mpEdbEPHS3Policy = _iam.ManagedPolicy(
            self,
            "mpEdbEPHS3Policy",
            description= "IRIS EPH policy for S3",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "s3:List*",
                                "s3:GetObject*",
                                "s3:PutObject*",
                                "s3:DeleteObject*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lilly_mdm/iris_eph_data_extract/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lilly_mdm/iris_eph_data_extract/*",
                        f"arn:aws:s3:::lly-edp-conformed-{params['pBucketPrefix']}/lilly_mdm/iris_eph_data_extract/*"
                                ]
                    )
                ]
            )
        )
        cfn_func = mpEdbEPHS3Policy.node.default_child
        cfn_func.override_logical_id("mpEdbEPHS3Policy")

        mpEdbIrisRedshiftAdminPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisRedshiftAdminPolicy",
            description= "IRIS policy for Redshift Data API operations",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "redshift:CreateScheduledAction",
                                "redshift:ModifyScheduledAction",
                                "redshift:DeleteScheduledAction"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:scheduled-action:iris-edb-{params['pEnvironment']}",
                        f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"
                    ]),
                    _iam.PolicyStatement(
                    actions=  [  "redshift:RebootCluster",
                                "redshift:PauseCluster",
                                "redshift:ResumeCluster"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisRedshiftAdminPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisRedshiftAdminPolicy")

        mpEdbIrisRDSAdminPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisRDSAdminPolicy",
            description= "IRIS policy for RDS admin operations",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "rds:StartDBCluster",
                                "rds:StopDBCluster",
                                "rds:RestoreDBClusterFromSnapshot",
                                "rds:ModifyDBCluster",
                                "rds:ModifyDBInstance"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:og:*",
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:cluster-pg:*",
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:cluster:*iris*",
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:cluster-snapshot:*iris*",
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:db:*iris*",
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:secgrp:*",
                        f"arn:aws:rds:{config.deploy_env.region}:{config.deploy_env.account}:pg:*"
                    ])
                ]
            )
        )
        cfn_func = mpEdbIrisRDSAdminPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisRDSAdminPolicy")

        mpEdbIrisRedshiftDataPolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisRedshiftDataPolicy",
            description= "IRIS policy for Redshift Data API operations",
            managed_policy_name= "IRIS_redshift_data_execution_policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=  [ "redshift-data:CancelStatement",
                                "redshift-data:GetStatementResult"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "redshift-data:ExecuteStatement",
                                "redshift-data:DescribeStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisRedshiftDataPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisRedshiftDataPolicy")

        mpEdbIrisLambdaPolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisLambdaPolicy",
            description= "IRIS policy for Lambda",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['lambda'],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"]
                    ),
                    _iam.PolicyStatement(
                    actions=  [  "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_*",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                            ]
                    )
                
                ]
            )
        )
        cfn_func = mpEdbIrisLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisLambdaPolicy")

        mpEdbIrisDmsLambdaPolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisDmsLambdaPolicy",
            description= "IRIS policy for DMS Lambda",
            document= _iam.PolicyDocument(
                 statements= [_iam.PolicyStatement(
                    actions= [  "dms:StartReplicationTask",
                                "dms:StopReplicationTask",
                                "dms:DescribeReplicationTasks"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:DY3DTOPBVE2MTKTT7YKEQ4YAPO5JBZWQA5HPC3Q",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:5GP6FPYPAFUHDYFGIADUR6WFIAOV2BCRYH6LJ3A",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:MUTSDNENEMMEUOQO2B5THYNPP73XXDTUTQPIHRI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:K7DDO7KHEKQ2SPKEJUM5F3BHOKQUXMS5J7YH22Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:GGUPSLYJMPUUR4CEDGC7HITBV4JTVQ27FDJIUVI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:EZ3XY7BF25FTJCGWETTNT26N2BMVIB3D7YSPM2I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:IZMXUF3C7RBZ6BAQAH3OHDKSRD2TJYE6537QHOY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:3GD2X6AU4FDZQ7JH5K2RKRWBI2P3625GL6LZRXQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:FME6NDZZLBIESNBKSBQ6WIVSR2JCT4ZTSDVWWCI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:5H76IEZ5TPQQHUYMOG7JBJW3CPUOLW3R6UMQRLI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:YG6TDRIQUWVXARHGPVJE7OFETSQ4GEPW735JP2Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:EEM5IKO3RQU74IKWOCOI2ZNMT33JR7WPYRT7M6Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:IZMXUF3C7RBZ6BAQAH3OHDKSRD2TJYE6537QHOY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:FLJS7DW7FT5BMTHUHPFIAQPZYWFNG53XGPZBXUY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:SYSEINJWLVTZB6TL4E5HZEJACZ3CPJYWERNYGCQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:OKIYSUSR257L6E2C4VY5JAX4SSFB4GNDXDUXWTQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:G6NO2RZV3BVOJPQHPWWG67OQY3XOCN635VPZVAY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:PO7QNHJQ4FRK42R6AQBLQ5HBV7RV7DV4A6SC67I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:DKE3FNJDFMFKDGG57FHL7JOVCLTFJKMDA2JC4LI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:EGWUDZ2YOUL6MZFVGYA7TGGEDSZSNJCEW4DKNBY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:NYEAKBQ3OEZDJ3J4ZC366QLY74P6OGWYBJDFXDY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:YH657MSUSZ7NP7H6MJMWBVLRBNTLOX3ZOCPLWXA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:SS3T6QPV5QTXYCM3BS5UMU4KZXX4PFIMMDSVPLA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:CIPPENLZEW5DTEDHZRECU4I62HMRFBDZG7KTMIY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:GSFLSA6YHIEZ6IVCRO2JYIDP7IXRA4HVBF25OVQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:EZ3XY7BF25FTJCGWETTNT26N2BMVIB3D7YSPM2I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:7DSZ6ARI3QAEI3WOX5IRHHCM4E6PDHIVS4QK2QY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:J6PXW3ACZZWSHOHVSI3PNQ4IHRUYXXY6X4YPJ4Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:3LOLLLQ263L4F44O3F4YPK3UBBHGAQ7DPZ6VIBA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:P4MJB32J5ARMGINRIG2IJJQ7ENBJK3TWKBRRHOI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:XIA5V3ES3HMFXMO26REHC6UZ2OE33UEOEW5INOA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:G6D2SY4VVX5QF2B5VZ7N3AU47G6W6I6WAYSNOFY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:OFKWIOOWUYLCYWTQ2Y74LIZIWKE54S32PF6MGPQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:7QWVFIZ32ZDQSAWLNYYZD6V6KYOI2TDYNHPQ4XA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:ZUKEQ2UQ4J4FV6RDPOE4XWYQSZ5TE22B234HFHI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:QVHR3EI35KDIGX45LVHKUDV6XRENJACTSY5QZRI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:VFNMRO2YTSEM2QT445MRBGXDRALMGAVHKCAOH5I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:O6GUOIBHWWS6OAEBZZQA7EWWLJ6QM5L4VMBB26Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:HNIU36SWLUXOTH42O5VCUKNP3VZ5YHXDWMRSY4Q",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:7YLJKBMHVRTY3W7FE5DIMBZRZ2RU77N44HD3YTI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:SNEMCJT5VIHNAMMXUHKACVYPYBFD6WPRVLWKWXQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:2AIFCBXE64G56N4JBTOCJXMPUZDUO52KHDGKH3I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:Z6CT3WI3DR65C5BVX5U6YTNSRGO7Q2ZRVCX2BWQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:C27IEE7L77WDH2LZMMPDSKCAFKP3V356WSI6YPY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:N2K3677NNAAOT4KFALTIID4HZBIIHDQR7ZXAZYA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:C5RS23S4O6EKK4BZ2AR6CTTHBPGV2ZLJ7BPLIOI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:IGE3CLR355QTJL2TFRSGY7ELXMWLNKWINMUXQ6I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:45G7YBQCGWBZKCJO65DAWXQIULF45VTXBK2JF7Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:KZ22TDER6CVRLHLSZG2PSP45KWFE27743WXJJOA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:LS72RAHVMQKMZICYHAHTCJM6PTFZ6OLVWQTVAYA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:GRYXE2JO4EZ4WXNRZSB4MSUYJ7QAHLRUWSVZBBA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:RKBZD2RIBRHDCWM6CLV54OXBMHPJVDSWIB3B27Y",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:CQJZBN5YZGOQ6QXN2S6R4MV3UXD3DUM2RPASCWQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:RW67FVKUYEOI7OOTJAH22FPXNH64XXQGHRBQYTY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:CCUMKWIMZWT4UYJWUQKVXOHY7BPKGGHSK2GYG5Q",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:BVP6N5IKBR6BJMASZPPLDR7JL2KZZSNHAOAAVTA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:JXLOZGCFYSKTEVBWBHKWWRCU2HMY4AD7K2XPWSA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:BE4VWC22APGK3V7H2BHDZ6ZX7H7PLHMKE7NVHCQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:4WHM62EJ26HJ57JCFWCD5NJMKXFO2YQ6SFVTQGA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:MSKI2YYNY4WDO5AIHX4CGSUWQOH22T5RKHFONIQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:UHRPRMLXNXLJBO6V6BBKIZFMRKOHT7FSDJKJPEA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:Q6OX6MHYHFPU36PYOFLMJYRM5TBYQMBUN6ZPWFY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:GHGZEIZFPLAD3T2MHHLYQR3AH57HHWOKFCQDELI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:SYNTXD5VNIU6AP5U7LNSYQUOS5RAH7EALGBGZFQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:SUO5FBO42UVJ57UWRLBQ6BHRP57OBQYQB5KJ37A",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:ILPD3GNX2JGBNHVRDUKYHBEMHA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:4KDH5P2RB2OLENTUNZNENIHDLWZMPTPMDAPTKJI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:C4YT3CPH7MYCUUPOABD5CLL7XRLZUTV6I6ALWHQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:NUVMAXYZICDZPYXEKFJW2EKFNAD7LHK5OH2M7BY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:XVGD7OLPHFDQXG4E62UMXGNTNY",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:SVGKUTYMKQ725RMOFVONBZTBAB3NCGDIJBXHFWA",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:GIUDUI4VI7BWVHQQBLGC3KFDUDFRUUVB5ASUHPQ",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:YT6C4EV7MNOMOPJ5YMPMX7JOTEIG55B4YKYWL7I",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:CYBNHSICPGWN3MRKXEUDM4IX2G2IUXU44ANODFI",
                        f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:X5LYKFUL5FL75UMVHS54QQORN7K4HGSZYPCECYI"
                        ]
                 )
                ]
                )
        )
                    
                             

        mpEdbIrisLogPipelinePolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisLogPipelinePolicy",
            description= "IRIS policy for logs and pipeline",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=["logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris*"
                    ]),
                    _iam.PolicyStatement(
                    actions=[ "codepipeline:PutJobSuccessResult",
                                "codepipeline:PutJobFailureResult",
                                "codepipeline:GetJobDetails"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "codepipeline:GetPipelineExecution",
                                "codepipeline:ListPipelineExecutions"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:*-iris-*"]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisLogPipelinePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisLogPipelinePolicy")

        mpEdbIrisGluePolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisGluePolicy",
            description= "IRIS policy for using Glue",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "logs:AssociateKmsKey",
							 	"logs:CreateLogGroup",
                                "logs:CreateLogStream",
                                "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:/aws-glue/*",
								 f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/*"
                    ]),
                    _iam.PolicyStatement(
                    actions=[ "s3:GetObject",
                              "s3:Get*",
                              "s3:Put*",
                              "s3:GetObjectTagging",
                              "s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-codeconfig-{params['pBucketPrefix']}/edb-core/core/abc/libs/glue/glueetl/*",
                        f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws_glue/scripts/edb-iris/*",
                        f"arn:aws:s3:::{params['ArtifactBucket']}/aws_glue/scripts/edb-iris/*"
                    ]
                    )
                    ,
		     _iam.PolicyStatement(
                    actions=[ "iam:PassRole"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:iam::{config.deploy_env.account}:role/OMT_GlueExecutionRole-qa"]
                     ),
                    _iam.PolicyStatement(
                    actions=[  "cloudwatch:PutMetricData",
                              "ec2:DescribeNetworkInterfaces",
                              "ec2:DescribeRouteTables",
                              "ec2:DescribeSecurityGroups",
                              "ec2:DescribeSubnets",
                              "ec2:DescribeVpcAttribute",
                              "ec2:DescribeVpcEndpoints",
                              "s3:GetBucketLocation",
                              "s3:ListAllMyBuckets",
                              "s3:ListBucket"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ "*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "glue:BatchGetJobs",
                              "glue:GetJobs",
                              "glue:GetJobRun",
                              "glue:GetJobRuns"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "glue:CreateCrawler",
                              "glue:GetCrawler",
                              "glue:GetCrawlerMetrics",
                              "glue:StartCrawler",
                              "glue:StartJobRun",
                              "glue:UpdateCrawler",
                              "glue:BatchStopJobRun",
                              "glue:UpdateJob",
                              "glue:GetJob",
                              "glue:PublishDataQuality",
                              "glue:StartDataQualityRulesetEvaluationRun"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris_*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/edb_iris*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/iris-dqa*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "glue:GetDatabase",
                              "glue:GetDatabases",
                              "glue:GetTable",
                              "glue:GetTables",
                              "glue:SearchTables"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/iris-dqa*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_iris*/*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/iris-dqa*/*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "glue:ListDatabases",
                              "glue:ListTables",
                              "glue:ListJobs",
                              "glue:ListJobRuns",
                              "glue:ListTriggers",
                              "glue:ListWorkflows",
                              "glue:ListConnections",
                              "glue:ListCrawlers"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=["s3:GetBucketAcl","s3:List*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-logarchival-us-east-2-{params['pEnvironment']}/aws/glue/aads_edb_iris_glue_cwlogs/*",
                        f"arn:aws:s3:::lly-edp-logarchival-us-east-2-{params['pEnvironment']}",
                        f"arn:aws:s3:::lly-edp-codeconfig-{params['pBucketPrefix']}"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['glue'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_iris*/*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/iris-dqa*/*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/iris-dqa*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_bas*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:userDefinedFunction/edb_iris*/*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/edb_iris*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/iris-dqa*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_abc*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  
                        "ec2:Describe*",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:CreateTags",
                        "ec2:DeleteTags"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ec2:*:*:instance/*",
                        "arn:aws:ec2:*:*:security-group/*",
                        "arn:aws:ec2:*:*:network-interface/*"
                    ],
                    conditions={
                        "ForAllValues:StringEquals": {
                            "aws:TagKeys": "aws-glue-service-resource"
                        }
                    }
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisGluePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisGluePolicy")

        mpEdbIrisAthenaPolicyAdmin = _iam.ManagedPolicy(
            self,
            "mpEdbIrisAthenaPolicyAdmin",
            description=  "IRIS policy for IRIS admins using Athena",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=["athena:Get*",
                                "athena:StartQueryExecution",
                                "athena:DeleteNamedQuery",
                                "athena:StopQueryExecution",
                                "athena:RunQuery",
                                "athena:CreateNamedQuery",
                                "athena:CancelQueryExecution",
                                "athena:UpdateWorkGroup",
                                "athena:DeleteWorkGroup",
                                "athena:CreateWorkGroup"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_admin"
                          ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisAthenaPolicyAdmin.node.default_child
        cfn_func.override_logical_id("mpEdbIrisAthenaPolicyAdmin")

        mpEdbIrisStateMachinePolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisStateMachinePolicy",
            description= "IRIS policy for State machine access",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris*",
                                f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris*:*",
                                f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:omnisource*",
                                f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:omnisource*",
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=  [ "events:PutTargets",
                                "events:PutRule",
                                "events:DescribeRule"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisStateMachinePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisStateMachinePolicy")

        mpEdbIrisBrmsDatabrewSecurityPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisBrmsDatabrewSecurityPolicy",
            description=  "Managed policy for setting databrew access for BRMS",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewlist'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:*"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['databrewdescribe'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                          f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-brms-ds*",
                          f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-brms-job*",
                          f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}::recipe/iris-brms-rcp*"
                                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "glue:Get*"],
                    effect= _iam.Effect.DENY,
                    resources= [
                          f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:*/AwsGlueDataBrew-{params['pDatabrewProjectTag']}*",
                          f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                                    ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisBrmsDatabrewSecurityPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisBrmsDatabrewSecurityPolicy")

        rBRMSServiceRole = _iam.Role(
                self,
                "rBRMSServiceRole",
                role_name= "edb_buids_iris_brms_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("databrew.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpBRMSLambdaPolicy,
                    mpBRMSDatabrewPolicy,
                    mpBRMSS3RWPolicy,
                    mpBRMSStateMachinePolicy,
                    mpBRMSGlueJobPolicy,
                    mpBRMSRedshiftDataPolicy,
                    mpEdbIrisKmsRWPolicy
                ]
            )
        rBRMSServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=["ses:SendEmail"],
            resources=[f"arn:aws:ses:us-east-1:539199905087:identity/lilly.com"],
            effect=_iam.Effect.ALLOW,
            sid="BrmsPolicyCodepipelineIamSesEc2Secrets"
        ))
        rBRMSServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=["codepipeline:PutJobSuccessResult","codepipeline:PutJobFailureResult"],
            resources=[
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-aads-edb-gha-migration",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-lusa-iris-lz-actions",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-lusa-iris-edb-master-v1",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:bia-adhoc-main"
			],
            effect=_iam.Effect.ALLOW
        ))
        rBRMSServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "iam:GetRole",
                    "iam:PassRole",
                    "iam:ListRoleTags",
                    "iam:GetRolePolicy"],
            resources=[ f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_brms_service_role"],
            effect=_iam.Effect.ALLOW
        ))
        rBRMSServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  
                "ec2:Describe*",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "ec2:CreateTags",
                "ec2:DeleteTags"
            ],
            effect= _iam.Effect.ALLOW,
            resources= [
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ec2:*:*:security-group/*",
                "arn:aws:ec2:*:*:network-interface/*"
            ],
            conditions={
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "aws-glue-service-resource"
                }
            }
        ))
        rBRMSServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "secretsmanager:GetSecretValue",
                    "secretsmanager:DescribeSecret",
                    "secretsmanager:PutSecretValue",
                    "secretsmanager:RotateSecret",
                    "secretsmanager:UpdateSecret",
                    "secretsmanager:UpdateSecretVersionStage"],
            resources=[f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-BRMSSystemUser-??????"
                        ],
            effect=_iam.Effect.ALLOW
        ))

        rBRMSServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "kms:Decrypt",
                        "kms:GenerateDataKey"],
            resources=[ f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}"],
            effect=_iam.Effect.ALLOW
        ))
        _tag.of(rBRMSServiceRole).add("databrewproject",params['pDatabrewProjectTag'])
        cfn_func = rBRMSServiceRole.node.default_child
        cfn_func.override_logical_id("rBRMSServiceRole")

        
        rBASServiceRole = _iam.Role(
                self,
                "rBASServiceRole",
                role_name= "edb_buids_bas_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("databrew.us-east-2.amazonaws.com"),
                _iam.ServicePrincipal("events.amazonaws.com"),
                _iam.ServicePrincipal("scheduler.redshift.amazonaws.com"),
                _iam.ServicePrincipal("dms.amazonaws.com"),
                _iam.ServicePrincipal("ssm.amazonaws.com"),
                _iam.ServicePrincipal("dms.us-east-2.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpBASLambdaPolicy,
                    mpBASS3RWPolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpBASGlueJobPolicy,
                    mpBASRedshiftDataPolicy
                ]
            )

        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=["ses:SendEmail"],
            resources=[f"arn:aws:ses:us-east-1:539199905087:identity/lilly.com"],
            effect=_iam.Effect.ALLOW,
            sid="BasPolicyCodepipelineIamSesEc2Secrets"
        ))
        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "codepipeline:PutJobSuccessResult",
            "codepipeline:PutJobFailureResult"],
            resources=[
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-aads-edb-gha-migration",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-lusa-iris-lz-actions",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-lusa-iris-edb-master-v1",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:bia-adhoc-main"
			],
            effect=_iam.Effect.ALLOW
        ))
        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "iam:GetRole",
            "iam:PassRole",
            "iam:ListRoleTags",
            "iam:GetRolePolicy"],
            resources=[f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_{params['pEnvironment']}_bas_operations",
                        f"arn:aws:iam::{config.deploy_env.account}:role/Iris-bas-GlueExecutionRole-{params['pEnvironment']}",
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_bas_LambdaExecRole-{params['pEnvironment']}",
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_bas_service_role"],
            effect=_iam.Effect.ALLOW
        ))
		
        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ 
				"ec2:Describe*",
				"ec2:DeleteNetworkInterface",
				"ec2:DeleteTags"
			],
            resources=[f"arn:aws:ec2:{config.deploy_env.region}:{config.deploy_env.account}:instance/i-0"],
            effect=_iam.Effect.ALLOW
        ))

        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ 
				"ec2:Describe*",
				"ec2:DeleteNetworkInterface",
				"ec2:CreateTags"
			],
            resources=[f"arn:aws:ec2:{config.deploy_env.region}:{config.deploy_env.account}:instance/i-0"],
            effect=_iam.Effect.ALLOW
        ))
		
        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
			actions=[
				"secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret",
				"secretsmanager:PutSecretValue",
				"secretsmanager:RotateSecret",
				"secretsmanager:UpdateSecret",
				"secretsmanager:UpdateSecretVersionStage"
			],
            resources=[f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-bas-SystemUser-??????"],
            effect=_iam.Effect.ALLOW
        ))
		
        rBASServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "kms:Decrypt",
                        "kms:GenerateDataKey",
                        "kms:List*",
                        "kms:DescribeKey"],
            resources=[RedshiftKMSKey.key_arn,
            f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}"
            ],
            effect=_iam.Effect.ALLOW
        ))
        cfn_func = rBASServiceRole.node.default_child
        cfn_func.override_logical_id("rBASServiceRole")

        rLMServiceRole = _iam.Role(
                self,
                "rLMServiceRole",
                role_name= "edb_buids_iris_lm_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("databrew.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpLMLambdaPolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpLMGlueJobPolicy,
                    mpLMRedshiftDataPolicy,
                    mpLMS3RWPolicy
                ]
            )


        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "ses:SendEmail"],
            effect=_iam.Effect.ALLOW,
            resources=[f"arn:aws:ses:us-east-1:539199905087:identity/lilly.com"]
        ))
        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "codepipeline:PutJobSuccessResult",
                        "codepipeline:PutJobFailureResult"],
            effect=_iam.Effect.ALLOW,
            resources=[
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-aads-edb-gha-migration",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-lusa-iris-lz-actions",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:pipeline-lusa-iris-edb-master-v1",
				f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:bia-adhoc-main"
			],
        ))
        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "iam:GetRole",
                        "iam:PassRole",
                        "iam:ListRoleTags",
                        "iam:GetRolePolicy"],
            effect=_iam.Effect.ALLOW,
            resources=[
                f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_lm_service_role"
                        ]
        ))
        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "ec2:Describe*",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:CreateTags",
                        "ec2:DeleteTags"],
            effect=_iam.Effect.ALLOW,
            resources=[f"arn:aws:ec2:{config.deploy_env.region}:{config.deploy_env.account}:instance/i-0"]
        ))
        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "ec2:Describe*",
                        "ec2:DeleteNetworkInterface",
                        "ec2:DeleteTags"],
            effect=_iam.Effect.ALLOW,
            resources=[f"arn:aws:ec2:{config.deploy_env.region}:{config.deploy_env.account}:instance/i-0"]
        ))
        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "secretsmanager:GetSecretValue",
                        "secretsmanager:DescribeSecret",
                        "secretsmanager:PutSecretValue",
                        "secretsmanager:RotateSecret",
                        "secretsmanager:UpdateSecret",
                        "secretsmanager:UpdateSecretVersionStage"],
            effect=_iam.Effect.ALLOW,
            resources=[f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-LMSystemUser-??????"
                        ]
        ))
		
        rLMServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "kms:Decrypt",
                        "kms:GenerateDataKey"],
            effect=_iam.Effect.ALLOW,
            resources=[
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}"
                        ]
        ))
        _tag.of(rLMServiceRole).add("databrewproject",params['pDatabrewProjectTag'])
        cfn_func = rLMServiceRole.node.default_child
        cfn_func.override_logical_id("rLMServiceRole")
        
        mpEdbIrisServicePolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisServicePolicy",
            description= "Single Managed Service Policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "kms:Decrypt",
                              "kms:Encrypt",
                              "kms:DescribeKey",
                              "kms:GenerateDataKey*",
                              "kms:ReEncrypt*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [ 
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}::key/{params['pEdbS3KmsKey']}"
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "kms:ListKeys",
                              "kms:ListAliases"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "sns:Publish"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:sns:{config.deploy_env.region}:{config.deploy_env.account}::edb_iris*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "kms:DisableKey",
                                "kms:ScheduleKeyDeletion"],
                    effect= _iam.Effect.DENY,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris*"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=["codepipeline:PutJobSuccessResult",
                                "codepipeline:PutJobFailureResult",
                                "codepipeline:GetJobDetails"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:*-iris-*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "codepipeline:GetPipelineExecution",
                                "codepipeline:ListPipelineExecutions"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:*-iris-*"]
                    ),
                     _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['lambda'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[ "lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:pipeline-iris-core-LambdaStack*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "dms:StartReplicationTask",
                                "dms:StopReplicationTask",
                                "dms:DescribeReplicationTasks"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:DY3DTOPBVE2MTKTT7YKEQ4YAPO5JBZWQA5HPC3Q"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ 
                                "redshift-data:ExecuteStatement",
                                "redshift-data:DescribeStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    ),
                    _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris*",
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:omnisource*",
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris*:*",
                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:omnisource*:*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[   "events:PutTargets",
                                "events:PutRule",
                                "events:DescribeRule"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[    "athena:Get*",
                                "athena:StartQueryExecution",
                                "athena:DeleteNamedQuery",
                                "athena:StopQueryExecution",
                                "athena:RunQuery",
                                "athena:CreateNamedQuery",
                                "athena:CancelQueryExecution",
                                "athena:UpdateWorkGroup",
                                "athena:DeleteWorkGroup",
                                "athena:CreateWorkGroup"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[   "s3:ListAllMyBuckets",
                                "s3:GetBucketLocation",
                                "s3:ListAccessPoints",
                                "redshift-data:CancelStatement",
                                "redshift-data:GetStatementResult"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       "*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[  "cloudwatch:PutDashboard",
                                "cloudwatch:DeleteDashboards"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:cloudwatch::{config.deploy_env.account}:dashboard/edb_iris*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[  "ssm:GetParameter"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[  "ecr:BatchDeleteImage",
                                "ecr:CompleteLayerUpload",
                                "ecr:UploadLayerPart",
                                "ecr:InitiateLayerUpload",
                                "ecr:BatchCheckLayerAvailability",
                                "ecr:PutImage"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb-iris*"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[  "dms:DeleteReplicationInstance"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "dms:rep-tag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ),
                     _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['dmsEndpoint'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "dms:endpoint-tag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ),
                     _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['dmsTask'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
								f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
							],
                    conditions={
                        "StringEquals": {
                            "dms:task-tag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ),
                     _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['dmsResource'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "aws:ResourceTag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ),
                     _iam.PolicyStatement(
                    actions= [ "iam:GetRole",
                                "iam:PassRole",
                                "iam:ListRoleTags",
                                "iam:GetRolePolicy"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_service_role",
                       f"arn:aws:iam::{config.deploy_env.account}:role/edb_iris_redshift_service_role",
                       rBRMSServiceRole.role_arn,
                       rBASServiceRole.role_arn,
                       rLMServiceRole.role_arn
                    ],
                    )   
                ]
            )
        )
        cfn_func = mpEdbIrisServicePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisServicePolicy")


        rMDMServicerole = _iam.Role(
                self,
                "rMDMServicerole",
                role_name= "edb_buids_iris_mdm_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("scheduler.redshift.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpEdbIrisRedshiftDataPolicy,
                    mpEdbIrisLambdaPolicy,
                    mpEdbIrisDmsLambdaPolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpEdbIrisRedshiftAdminPolicy,
                    mpEdbIrisServicePolicy,
                    mpEdbIrisSecretsPolicyTwo,
                    mpEdbIrisReadMinusS3Policy 
                ]
            )
        cfn_func = rMDMServicerole.node.default_child
        cfn_func.override_logical_id("rMDMServicerole")
        
        rCTGOVServicerole = _iam.Role(
                self,
                "rCTGOVServicerole",
                role_name= "edb_buids_ext_schema_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("scheduler.redshift.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpEdbIrisRedshiftDataPolicy,
                    mpEdbIrisLambdaPolicy,
                    mpEdbIrisDmsLambdaPolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpEdbIrisRedshiftAdminPolicy,
                    mpEdbIrisServicePolicy,
                    mpEdbIrisSecretsPolicyTwo,
                    mpEdbIrisReadMinusS3Policy 
                ]
            )
        cfn_func = rCTGOVServicerole.node.default_child
        cfn_func.override_logical_id("rCTGOVServicerole")

        FlexDataArchivePolicy = _iam.ManagedPolicy(
            self,
            "FlexDataArchivePolicy",
            description= "Temporary Policy for Archiving Flex Data to EDB",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= [
			                    "dms:DescribeReplicationInstances",
			                    "dms:StartReplicationTask",
			                    "dms:StopReplicationTask"
			                ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"],
                     conditions=  {
                              "StringEquals": {
                                  "dms:rep-tag/temp_usage": "archive_flex_data"
                              }
                          }
                ),
                _iam.PolicyStatement(
                    actions= [
			                    "dms:DescribeEndpoints",
			                    "dms:ModifyEndpoint"
			                ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:endpoint:*"],
                     conditions= {
                              "StringEquals": {
                                  "dms:endpoint-tag/temp_usage": "archive_flex_data"
                              }
                          }
                ),
                _iam.PolicyStatement(
                    actions= [
			                    "dms:DescribeReplicationTasks",
			                    "dms:StartReplicationTask",
			                    "dms:ModifyReplicationTask"
			                ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"],
                     conditions=  {
                              "StringEquals": {
                                  "dms:task-tag/temp_usage": "archive_flex_data"
                              }
                          }
                ),
                _iam.PolicyStatement(
                    actions= [
								"dms:Describe*"
							],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:*"],
                     conditions=  {
                              "StringEquals": {
                                  "aws:ResourceTag/temp_usage": "archive_flex_data"
                              }
                          }
                ),
                _iam.PolicyStatement(
                    actions= ["kms:Decrypt", "kms:GenerateDataKey"],
                    effect= _iam.Effect.ALLOW,
                    resources= [DMSIrisKMSKey.key_arn]
                )
                ]
            )
        )
        cfn_func = FlexDataArchivePolicy.node.default_child
        cfn_func.override_logical_id("FlexDataArchivePolicy")

        if config.env in ['dev']:
            Verso_GlueExecutionRole2_dev = _iam.Role.from_role_name(self,
                                                                    "Verso_GlueExecutionRole2_dev",
                                                                    role_name= "Iris-Verso-GlueExecutionRole2-dev"
            )
            Verso_LambdaExecRole_dev = _iam.Role.from_role_name(self,
                                                                    "Verso_LambdaExecRole_dev",
                                                                    role_name= "Iris-Verso-LambdaExecRole-dev"
            )
            Verso_exec_role = Verso_GlueExecutionRole2_dev.role_arn
            verso_lamda_role = Verso_LambdaExecRole_dev.role_arn
        else :
            Verso_exec_role = None
            verso_lamda_role =  None

        if config.env in ['dev']:
            Iam_resources =[f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_service_role",
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_iris_redshift_service_role",
                        rBRMSServiceRole.role_arn,
                        Verso_exec_role,
                        verso_lamda_role
                    ]
        else :
            Iam_resources = [f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_service_role",
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_iris_redshift_service_role",
                        rBRMSServiceRole.role_arn,
                        rBASServiceRole.role_arn
                    ]
        mpEdbIrisFederatedServicePolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisFederatedServicePolicy",
            description= "Managed Service Policy for Federated Roles",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "sns:Publish"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [ f"arn:aws:sns:{config.deploy_env.region}:{config.deploy_env.account}:edb_iris*"]),
                _iam.PolicyStatement(
                    actions=[   "kms:DisableKey",
                                "kms:ScheduleKeyDeletion",
                                "ssm:StartSession"
                            ],
                    effect= _iam.Effect.DENY,
                    resources= ["*"]
                    ),
                _iam.PolicyStatement(
                    actions=[  "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris*"]
                    ) ,
                _iam.PolicyStatement(
                    actions=[  "codepipeline:PutJobSuccessResult",
                                "codepipeline:PutJobFailureResult",
                                "codepipeline:GetJobDetails"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:*-iris-*"]
                    ) ,
                _iam.PolicyStatement(
                    actions=[   "codepipeline:GetPipelineExecution",
                                "codepipeline:ListPipelineExecutions"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:codepipeline:{config.deploy_env.region}:{config.deploy_env.account}:*-iris-*"]
                    ),
                _iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['lambda'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_global*"
                        ]
                    ) ,
                _iam.PolicyStatement(
                    actions= ["lambda:InvokeFunction"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*",
                                f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"],
                    conditions={
                        "StringEquals": {
                            "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_developers"
                        }
                    }
                ),
                _iam.PolicyStatement(
                    actions= [  "dms:StartReplicationTask",
                                "dms:StopReplicationTask",
                                "dms:DescribeReplicationTasks"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:DY3DTOPBVE2MTKTT7YKEQ4YAPO5JBZWQA5HPC3Q"
                                ]
                    ),
                 _iam.PolicyStatement(
                    actions= [ "redshift-data:ExecuteStatement",
                                "redshift-data:DescribeStatement"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:redshift:{config.deploy_env.region}:{config.deploy_env.account}:cluster:iris-edb-{params['pEnvironment']}"]
                    ),
                 _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris*",
                                f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:omnisource*",
                                f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris*:*",
                                f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:omnisource*:*"]
                    ),
                 _iam.PolicyStatement(
                    actions= [  "events:DisableRule",
                                "events:EnableRule"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/edb_iris_*",
                                f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/edb-iris-*"]
                    ) ,
                _iam.PolicyStatement(
                    actions= [  "events:PutTargets",
                                "events:PutRule",
                                "events:DescribeRule"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
                                ]
                    ),
                _iam.PolicyStatement(
                    actions= [  "athena:Get*",
                                "athena:StartQueryExecution",
                                "athena:DeleteNamedQuery",
                                "athena:StopQueryExecution",
                                "athena:RunQuery",
                                "athena:CreateNamedQuery",
                                "athena:CancelQueryExecution",
                                "athena:UpdateWorkGroup",
                                "athena:DeleteWorkGroup",
                                "athena:CreateWorkGroup"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:athena:{config.deploy_env.region}:{config.deploy_env.account}:workgroup/edb_iris*"
                                ]
                    ),
                _iam.PolicyStatement(
                    actions= [   "s3:ListAllMyBuckets",
                                "s3:GetBucketLocation",
                                "s3:ListAccessPoints",
                                "redshift-data:CancelStatement",
                                "redshift-data:GetStatementResult"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ) ,
                _iam.PolicyStatement(
                    actions= [  "cloudwatch:PutDashboard",
                                "cloudwatch:DeleteDashboards"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:cloudwatch::{config.deploy_env.account}:dashboard/edb_iris*"
                                ]
                    ),
                _iam.PolicyStatement(
                    actions= [  "ssm:GetParameter"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris*"
                                ]
                    ),
                _iam.PolicyStatement(
                    actions= [  "ecr:BatchDeleteImage",
                                "ecr:CompleteLayerUpload",
                                "ecr:UploadLayerPart",
                                "ecr:InitiateLayerUpload",
                                "ecr:BatchCheckLayerAvailability",
                                "ecr:PutImage"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb-iris*"
                                ]
                    ) ,
                _iam.PolicyStatement(
                    actions= [  "dms:DeleteReplicationInstance"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "dms:rep-tag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ) ,
                _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['dmsTask'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "dms:task-tag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ) ,
                _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['dmsEndpoint'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "dms:endpoint-tag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ),
                _iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['dmsResource'],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			                    f"arn:aws:dms:{config.deploy_env.region}:{config.deploy_env.account}:task:*"
			                ],
                    conditions={
                        "StringEquals": {
                            "aws:ResourceTag/AppName": "iris-core-edb-prd"
                        }
                    }
                    ),
                _iam.PolicyStatement(
                    actions= [ "iam:GetRole",
                                "iam:PassRole",
                                "iam:ListRoleTags",
                                "iam:GetRolePolicy"],
                    effect= _iam.Effect.ALLOW,
                    resources= Iam_resources
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisFederatedServicePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisFederatedServicePolicy")

        mpEdbIrisFederatedServicePolicy1 = _iam.ManagedPolicy(
            self,
            "mpEdbIrisFederatedServicePolicy1",
            description= "Managed Service Policy for Federated Roles",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['cloudformation'],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/Iris*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/iris*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/pipeline-lusa*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/Infra-ECS*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/pipeline-iris*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/buit-aws-core*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/IrisLusa*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/iris-verso*/*",
								f"arn:aws:cloudformation:{config.deploy_env.region}:{config.deploy_env.account}:stack/IrisCore*/*"
                    ]),
                    _iam.PolicyStatement(
                    actions=[  "kms:Decrypt",
                                "kms:Encrypt",
                                "kms:DescribeKey",
                                "kms:GenerateDataKey*",
                                "kms:ReEncrypt*"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}",
                                DMSIrisKMSKey.key_arn,
                                rLMServiceRole.role_arn
                    ]),
                    _iam.PolicyStatement(
                    actions=[    "kms:ListKeys",
                                "kms:ListAliases"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisFederatedServicePolicy1.node.default_child
        cfn_func.override_logical_id("mpEdbIrisFederatedServicePolicy1")

        mpEdbIrisS3AdminLandingPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3AdminLandingPolicy",
            managed_policy_name=  "edb-iris-s3-admin-landing",
            description=  "EDB IRIS admin policy S3 landing bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:GetObject",
                             "s3:PutObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                            f"arn:aws:s3:::{params['ArtifactBucket']}/lusa-iris-aws-core/*",
                            f"arn:aws:s3:::{params['ArtifactBucket']}/lusa-iris-aws-vending-machine/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws-glue/*/iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws_glue/iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws_glue/*/edb-iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/edb/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/redshift/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
						    f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*", # RITM3026470, RITM3057102
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*",  #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/lilly_mdm/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/targeting_lists_iris/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/zs_campaign_metadata/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*", 
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3346617
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/act_lusa_activity_restricted/*", # RITM3587665-QA RITM3587698- Prod
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3346617
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/flex_lusa_iris_restricted/*", #RITM3346617
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/hibbert_oneconnect_extracts/*",
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/eversana_edwin_extract/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/cvs_health/*", #RITM6437048
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/roman_health_ventures/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/manual_business_files_pr/*", #RITM3593791
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*",  #RITM3593791
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/esi_optum_prime_zinc_caremark_cmm_humana/*", #RITM3610484
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Caremark/*", #RITM4107676
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ESI_Enrollment/*", #RITM4107676
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Optum/*", #RITM4107676
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*", #RITM4107676
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Humana/*", #RITM4107676
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/met_extract/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/met_extract/*",
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/pcp_patient_demographics/*",  #RITM3987919
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iqvia_lusa_paid_claims_enriched_restricted/*", #RITM4245015
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eversana_copay/*" # RITM4593732-QA RITM4593737-Prod
                         ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisS3AdminLandingPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3AdminLandingPolicy")

        mpEdbIrisS3AdminRawPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3AdminRawPolicy",
            managed_policy_name= "edb-iris-s3-admin-raw",
            description= "EDB IRIS admin policy S3 raw bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "s3:GetObject",
                              "s3:PutObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", # RITM3140803
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*", # RITM3026470, RITM3057102
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lilly_mdm/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lusa_janrain/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lusa_lilly_play/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/cvs_health/*", #RITM6437048
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/roman_health_ventures/*", 
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/targeting_lists_iris/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*", # RITM3140803
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_campaign_metadata/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*", #RITM3150131
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/match_list_lusa_marketing_restricted/*", #RITM3150131
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris_lusa_data_quality_restricted/*", # RITM3127077
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*", 
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3346617
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/mtm_lusa_product_restricted/*", # RITM3296073-QA RITM3296079-Prod
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/salesforce_marketing_cloud/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/mmsi_ehr_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/publicis_ehr_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/act_lusa_activity_restricted/*", # RITM3587665-QA RITM3587698- Prod, RITM3623034
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_lusa_affinity_monitor_restricted/*", #RITM3570125
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_omnichannel_field_suggestions/*", 
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/manual_business_files_pr/*", #RITM3593791
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*",  #RITM3593791
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/met_extract/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/esi_optum_prime_zinc_caremark_cmm_humana/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ESI_Enrollment/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ESI_Portal/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Optum/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/optum_revitl/*", #RITM6465787
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Zinc/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Caremark/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Humana/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/carevalue_pap_business_files/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/deal_development_common_business_files/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/scout_global_restricted/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/emisar/*", #RITM4031525
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/salesforce_marketing_cloud/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ibu_omnichannel/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_zaidyn_omnichannel/*",
                        # f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_paid_claims_enriched_restricted/*", #RITM4245015
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/employer_govt_glghr_data_set/*", #RITM4302408
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_dataspine_pwd_restricted/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/veeva_vvpm/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/veeva_medcomms/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ap_reporting/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/deal_development_common_business_files_restricted/*", #RITM4775981
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*", #RITM5144304
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/hibbert_hcp_consent/*",
						f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iqvia_historical_data/*", #RITM5869273
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/healthdyne/*",  #RITM6330332
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/data_observability/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/centerwell/*", #RITM6330332				
                         ])
                ]
            )
        )
        cfn_func = mpEdbIrisS3AdminRawPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3AdminRawPolicy")

        mpEdbIrisS3AdminRawOmmPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3AdminRawOmmPolicy",
            managed_policy_name= "edb-iris-s3-admin-raw-omm",
            description= "EDB IRIS admin policy S3 raw bucket OMM folders",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:GetObject",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_9am/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_andel/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_calibrate/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_costplus/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_crux/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_emed/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_flyte/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_form/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_goodpath/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_goodrx/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_ilant/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_onsera/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_revive/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_salta/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_sesame/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_teladoc/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_transcarent/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_waltz/*", #RITM6401109
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*" #INC14839894
                         ])
                ]
            )
        )
        cfn_func = mpEdbIrisS3AdminRawOmmPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3AdminRawOmmPolicy")

        # Bucket policy for anaplan 
        mpAnaplanS3AdminDeparturePolicy = _iam.ManagedPolicy(
            self,
            "mpAnaplanS3AdminDeparturePolicy",
            managed_policy_name= "anaplan-s3-admin-departure",
            description= "Anaplan admin policy S3 departure bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:PutObject",
                              "s3:GetObject"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
						f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/gross_to_net_anaplan/*",
						f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/sap_snp_finance_1b/*"
						#f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/sap_snp_finance_1b/*",
                         ])
                ]
            )
        )
        cfn_func = mpAnaplanS3AdminDeparturePolicy.node.default_child
        cfn_func.override_logical_id("mpAnaplanS3AdminDeparturePolicy")

        mpEdbIrisEmployerS3AdminRawRefinedPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisEmployerS3AdminRawRefinedPolicy",
            managed_policy_name= "edb-iris-employer-s3-admin-raw-refined",
            description= "EDB IRIS Employer admin policy S3 raw bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/gifthealth_altaccess/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/healthdyne/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/centerwell/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_9am/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_andel/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_calibrate/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_crux/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_emed/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_flyte/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_form/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_goodpath/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_ilant/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_onsera/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_salta/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_waltz/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_revive/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_teladoc/*",
						f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_costplus/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_sesame/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_transcarent/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_goodrx/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/cvs_health/*", #RITM6437048
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/roman_health_ventures/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/gifthealth_altaccess/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/healthdyne/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/centerwell/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/judy_diamond_form55/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_9am/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_andel/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_calibrate/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_crux/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_emed/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_flyte/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_form/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_goodpath/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_ilant/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_onsera/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_salta/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_waltz/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_revive/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_teladoc/*",
						f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_costplus/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_sesame/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_transcarent/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_goodrx/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/cvs_health/*", #RITM6437048
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/roman_health_ventures/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/gifthealth_altaccess/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/healthdyne/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/centerwell/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/judy_diamond_form55/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_9am/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_andel/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_calibrate/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_crux/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_emed/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_flyte/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_form/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_goodpath/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_ilant/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_onsera/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_salta/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_waltz/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_revive/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_teladoc/*",
						f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_costplus/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_sesame/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_transcarent/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cvs_health/*", #RITM6437048
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/roman_health_ventures/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_goodrx/*",


                         ])
                ]
            )
        )
        
        mpEdbIrisS3AdminRefinedPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3AdminRefinedPolicy",
            description= "EDB IRIS admin policy S3 refined bucket",
            managed_policy_name= "edb-iris-s3-admin-refined",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:GetObject",
                              "s3:PutObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*", 
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3346617
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", # RITM3140803
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*", 
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*", 
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hibbert_oneconnect_extracts/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mlr_brand_specialties_us/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*", # RITM3026470, RITM3057102
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_data_quality_restricted/*", # RITM3127077
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lilly_mdm/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lusa_janrain/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lusa_lilly_play/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cvs_health/*", #RITM6437048
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/roman_health_ventures/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/match_list_lusa_marketing_restricted/*", #RITM3150131 
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mtm_lusa_product_restricted/*", # RITM3296073-QA RITM3296079-Prod
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/targeting_lists_iris/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*", # RITM3140803
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_campaign_metadata/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*", #RITM3150131
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/enterprisecustomer/eph/rdm/processed/*", #RITM3395172
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/salesforce_marketing_cloud/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mmsi_ehr_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/publicis_ehr_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/act_lusa_activity_restricted/*", # RITM3587665-QA RITM3587698- Prod, RITM3623034
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_lusa_affinity_monitor_restricted/*", #RITM3570125
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/manual_business_files_pr/*", #RITM3593791
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*",  #RITM3593791
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ESI_Portal/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ESI_Enrollment/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Optum/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/optum_revitl/*",  #RITM6465787
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Zinc/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Caremark/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Humana/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/carevalue_pap_business_files/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/deal_development_common_business_files/*",  #RITM3610484
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/emisar/*",  #RITM4031525
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lash_tokenized_patient_data/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lash_tokenized_patient_data/*",  
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/pcp_patient_demographics/*",  #RITM3987919
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_omnichannel_field_suggestions/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/veeva_vvpm/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/veeva_medcomms/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/salesforce_marketing_cloud/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/scout_global_restricted/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ibu_omnichannel/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_zaidyn_omnichannel/*",
                    # f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_paid_claims_enriched_restricted/*", #RITM4245015
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/employer_govt_glghr_data_set/*", #RITM4302408
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_dataspine_pwd_restricted/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hospital_anomaly_detection/*", #RITM4758697,RITM4769700
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ap_reporting/*",
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/deal_development_common_business_files_restricted/*", #RITM4775981
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*" #RITM5144304
                     ])
                ]
            )
        )
        cfn_func = mpEdbIrisS3AdminRefinedPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3AdminRefinedPolicy")

        mpEdbIrisS3AdminConformedPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3AdminConformedPolicy",
            managed_policy_name= "edb-iris-s3-admin-conform",
            description= "EDB IRIS admin policy S3 conform bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                     f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", # RITM3140803
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*", # RITM3026470, RITM3057102
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/lilly_mdm/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/lusa_janrain/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/lusa_lilly_play/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/targeting_lists_iris/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*", # RITM3140803
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris_lusa_data_quality_restricted/*", # RITM3127077
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*", 
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*", 
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/incentives_lusa_extracts_restricted/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/icyte_transactions_gross_to_net/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/sap_snp_finance_1b/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iqvia_transactions_gross_to_net/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/speciality_pharma/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/gross_sales_forecast/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/demand_forecast/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/managed_care_partd_invoice_details/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/wholesale_inventory/*",
                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/copay_claims_and_payment/*"
                     ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisS3AdminConformedPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3AdminConformedPolicy")


############################## Roles ##############################################

        
        rSecretsManagerRole = _iam.Role(
                self,
                "rSecretsManagerRole",
                role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_secrets_manager",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.FederatedPrincipal(
                    f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                    assume_role_action="sts:AssumeRoleWithSAML",
                    conditions={
                        "StringEquals": {
                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                        }
                    }
                )),
                managed_policies= [
                    mpEdbIrisReadMinusS3Policy,
                    mpEdbIrisConsolePolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpEdbIrisSecretsPolicy,
                    mpEdbIrisRedshiftAdminPolicy,
                    mpEdbIrisRDSAdminPolicy,
                    mpEdbIrisFederatedServicePolicy,
                    mpEdbIrisS3AdminRawPolicy,
                    mpEdbIrisS3AdminRawOmmPolicy,
                    mpEdbIrisS3AdminRefinedPolicy,
                    mpEdbIrisFederatedServicePolicy1,
                    mpEdbIrisSecretsPolicyTwo,
                ]
            )
        cfn_func = rSecretsManagerRole.node.default_child
        cfn_func.override_logical_id("rSecretsManagerRole")

        edb_ehr_pi_secret_kms = _kms.Alias.from_alias_name(self,
                                          "EdbEhrPiSecret12",
                                           "alias/aws-kms-edb-s3")

        mpDQAMiscPolicy = _iam.ManagedPolicy(
            self,
            "mpDQAMiscPolicy",
            managed_policy_name="dqa-managed-policy-misc",
            description=  "IRIS DQA policy for EC2, SES, Secrets Access",
            document= _iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[ "ec2:DescribeNetworkInterfaces",
                                "ec2:DescribeRouteTables",
                                "ec2:DescribeSecurityGroups",
                                "ec2:DescribeSubnets",
                                "ec2:DescribeVpcAttribute",
                                "ec2:DescribeVpcEndpoints",
                                "ec2:AssignPrivateIpAddresses",
                                "ec2:AttachNetworkInterface",
                                "ec2:UnassignPrivateIpAddresses",
                                "ec2:CreateNetworkInterface",
                                "ec2:DeleteNetworkInterface"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "ec2:DeleteTags",
                                "ec2:CreateTags"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:ec2:*:{config.deploy_env.account}:instance/i-*",
                                f"arn:aws:ec2:*:{config.deploy_env.account}:volume/*",
                                f"arn:aws:ec2:*:{config.deploy_env.account}:network-interface/*"],
                                conditions={
                        "ForAllValues:StringEquals": {
                            "aws:TagKeys/AppName": "lusa-iris-edb"
                        }
                    }
                    ),
                    _iam.PolicyStatement(
                    actions=[ "secretsmanager:GetSecretValue",
                                "secretsmanager:DescribeSecret",
                                "secretsmanager:PutSecretValue",
                                "secretsmanager:RotateSecret",
                                "secretsmanager:UpdateSecret",
                                "secretsmanager:UpdateSecretVersionStage"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                         f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-SQA-??????",
                         f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-dqa-snow-secret-??????",
                         f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-SoaroUser-??????",
                         f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_ehr_cortex-apim-{params['pEnvironment']}-credentials"
                    ]
                    ),
                     _iam.PolicyStatement(
                    actions=[   "kms:Decrypt",
                                "kms:GenerateDataKey"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbSnsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{edb_ehr_pi_secret_kms.key_id}"
                                ]
                    ),
                     _iam.PolicyStatement(
                    actions=[   "iam:GetRole",
                                "iam:PassRole",
                                "iam:ListRoleTags",
                                "iam:GetRolePolicy"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_dqa_service_role",
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_soa_databrew_service_role",
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_ehr_pi_autofill_service_role"
                        
                                ]
                    ),
                     _iam.PolicyStatement(
                    actions=[  "sns:Publish",
                                "sns:Subscribe"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:sns:{config.deploy_env.region}:{config.deploy_env.account}:iris-dqa-topic"
                                ]
                    ),
                     _iam.PolicyStatement(
                    actions=[   "ses:SendEmail",
                                "ses:SendRawEmail",
                                "ses:VerifyEmailIdentity"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["arn:aws:ses:us-east-1:539199905087:identity/lilly.com"]
                    ),
                     _iam.PolicyStatement(
                    actions=[    "ses:SendEmail",
                                "ses:SendRawEmail",
                                "ses:VerifyEmailIdentity"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["arn:aws:ses:us-east-1:539199905087:identity/lilly.com"]
                    )
                ]
            ),
            roles= [rSecretsManagerRole]
        )
        cfn_func = mpDQAMiscPolicy.node.default_child
        cfn_func.override_logical_id("mpDQAMiscPolicy")

        rEHRPiServiceRole = _iam.Role(
                self,
                "rEHRPiServiceRole",
                role_name= "edb_buids_ehr_pi_autofill_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
		_iam.ServicePrincipal("apigateway.amazonaws.com") 
                ),
                managed_policies= [
                    mpEHRPiLambdaPolicy,
                    mpEHRPiS3RWPolicy,
                    mpEHRMiscPolicy,
                    mpDQAMiscPolicy,
                    mpEdbIrisReadMinusS3Policy
                ]
            )
        cfn_func = rEHRPiServiceRole.node.default_child
        cfn_func.override_logical_id("rEHRPiServiceRole")

         # Add AssumeRole condition
        rEHRPiServiceRole.assume_role_policy.add_statements(
            _iam.PolicyStatement(
                effect=_iam.Effect.ALLOW,
                actions=["sts:AssumeRole"],
                principals=[
                    _iam.ArnPrincipal("arn:aws:iam::408787358807:role/lrl-light-apps/lrl-light-apps-llm-dev-lmm-data"),
                    _iam.ArnPrincipal("arn:aws:iam::474366589702:role/lrl-light-apps/lrl-light-apps-llm-qa-lmm-data"),
                    _iam.ArnPrincipal("arn:aws:iam::283234040926:role/lrl-light-apps/lrl-light-apps-llm-prd-lmm-data")
                    
                ],
                conditions={"StringEquals": {"sts:ExternalId": "ehrchatbot30"}}
            )
        )

        mpSplunkObservabilityMicsPolicy = _iam.ManagedPolicy(
            self,
            "mpSplunkObservabilityMicsPolicy",
            description= "Splunk Observability miscellaneous policy",
            document= _iam.PolicyDocument(
                statements=[
                    _iam.PolicyStatement(
                        actions=[
                            "secretsmanager:GetSecretValue",
                            "secretsmanager:DescribeSecret"
                        ],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:splunk-hec-secret-??????"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=["kms:Decrypt"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=["s3:GetObject", "s3:HeadObject"],
                        effect= _iam.Effect.ALLOW,
                        resources=[ 
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eversana_copay/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/centerwell/*",
							f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lva_splunk_test/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/healthdyne/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/judy_diamond_form55/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=["s3:GetObject", "s3:HeadObject"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eversana_copay/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*",
							f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lva_splunk_test/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/centerwell/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/healthdyne/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/judy_diamond_form55/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=["events:PutRule", "events:PutTargets"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/edb-iris-*"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpSplunkObservabilityMicsPolicy.node.default_child
        cfn_func.override_logical_id("mpSplunkObservabilityMicsPolicy")

        rLvaSplunkObservabilityRole = _iam.Role(
                self,
                "rLvaSplunkObservabilityRole",
                role_name= "edb_buids_lva_splunk_observability_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("apigateway.amazonaws.com")
                ),
                managed_policies= [
                    mpEHRPiLambdaPolicy,
                    mpEHRPiS3RWPolicy,
                    mpEHRMiscPolicy,
                    mpDQAMiscPolicy,
                    mpEdbIrisReadMinusS3Policy,
                    mpSplunkObservabilityMicsPolicy
                ]
            )
        cfn_func = rLvaSplunkObservabilityRole.node.default_child
        cfn_func.override_logical_id("rLvaSplunkObservabilityRole")

        mpSplunkObservabiltyOmmMiscPolicy = _iam.ManagedPolicy(
            self,
            "mpSplunkObservabiltyOmmMiscPolicy",  # CDK construct ID
            description= "Splunk Observability OMM miscellaneous policy",  # Human-readable description shown in IAM console
            document= _iam.PolicyDocument(
                statements=[
                    # Statement 1: Allow reading the Splunk HEC (HTTP Event Collector) secret
                    # from Secrets Manager. The HEC token is used to authenticate when sending
                    # events/metrics to the Splunk endpoint.
                    _iam.PolicyStatement(
                        actions=[
                            "secretsmanager:GetSecretValue",   # Retrieve the secret value (HEC token)
                            "secretsmanager:DescribeSecret"    # Describe secret metadata (rotation status, etc.)
                        ],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            # The Splunk HEC secret; '??????' is a wildcard for the random suffix AWS appends
                            f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:splunk-hec-secret-??????"
                        ]
                    ),
                    # Statement 3: Allow read-only S3 access (GetObject, HeadObject) to landing and raw
                    # bucket prefixes. These are the source data paths that Splunk observability monitors.
                    _iam.PolicyStatement(
                        actions=["s3:GetObject", "s3:HeadObject"],  # Read objects and check metadata
                        effect= _iam.Effect.ALLOW,
                        resources=[
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/data_observability/omm_splunk_observability/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_goodpath/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_goodrx/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_ilant/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_knownwell/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_sesame/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_teledoc/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_transcarent/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_waltz/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_9am/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_andel/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_calibrate/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_emed/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_flyte/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/omm_form/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_9am/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_andel/*",
							f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_calibrate/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_crux/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_emed/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_flyte/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_form/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_goodpath/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_goodrx/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_ilant/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_knownwell/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_sesame/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_teledoc/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_transcarent/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/omm_waltz/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_9am/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_andel/*",
							f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_calibrate/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_crux/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_emed/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_flyte/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_form/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_goodpath/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_goodrx/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_ilant/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_knownwell/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_sesame/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_teledoc/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_transcarent/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/omm_waltz/*"
                        ]
                    ),
                    # Statement 4: Allow creating and managing EventBridge rules and targets.
                    # Used to schedule or trigger Splunk observability workflows via EventBridge.
                    _iam.PolicyStatement(
                        actions=["events:PutRule", "events:PutTargets"],  # Create/update EventBridge rules and attach targets
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            # Allow managing any EventBridge rule in the account/region
                            f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/edb_iris*"
                        ]
                    )
                ]
            )
        )
        # Override the CloudFormation logical ID to keep it consistent across deployments
        cfn_func = mpSplunkObservabiltyOmmMiscPolicy.node.default_child
        cfn_func.override_logical_id("mpSplunkObservabiltyOmmMiscPolicy")

        rLvaSplunkObservabilityOmmRole = _iam.Role(
                self,
                "rLvaSplunkObservabilityOmmRole",  # CDK construct ID
                role_name= "edb_buids_lva_splunk_observability_omm_role",  # Physical IAM role name in AWS
                permissions_boundary= policy,  # Account-level permissions boundary to limit maximum privileges
                max_session_duration= Duration.seconds(36000),  # Max session duration of 10 hours for long-running jobs
                assumed_by=_iam.CompositePrincipal(  # Trust policy: which AWS services can assume this role
                _iam.ServicePrincipal("lambda.amazonaws.com"),       # AWS Lambda functions
                _iam.ServicePrincipal("glue.amazonaws.com"),         # AWS Glue ETL jobs
                _iam.ServicePrincipal("s3.amazonaws.com"),           # S3 event notifications
                _iam.ServicePrincipal("apigateway.amazonaws.com")    # API Gateway integrations
                ),
                managed_policies= [
                    mpEHRPiLambdaPolicy,                    
                    mpEHRPiS3RWPolicy,                      
                    mpEHRMiscPolicy,                        
                    mpDQAMiscPolicy,                        
                    mpEdbIrisReadMinusS3Policy,              
                    mpSplunkObservabiltyOmmMiscPolicy
                ]
            )
        # Override the CloudFormation logical ID to keep it consistent across deployments
        cfn_func = rLvaSplunkObservabilityOmmRole.node.default_child
        cfn_func.override_logical_id("rLvaSplunkObservabilityOmmRole")

        # ==========================================
        # Managed Policy: mpSplunkPACEObservabilityMicsPolicy
        # Purpose: PACE variant of the Splunk Observability miscellaneous policy.
        # Grants access to Secrets Manager (PACE HEC credentials), KMS, S3 (landing,
        # raw, and refined buckets for PACE-specific paths), and EventBridge.
        # ==========================================
        mpSplunkPACEObservabilityMicsPolicy = _iam.ManagedPolicy(
            self,
            "mpSplunkPACEObservabilityMicsPolicy",
            description="Splunk PACE Observability miscellaneous policy",
            document=_iam.PolicyDocument(
                statements=[
                    _iam.PolicyStatement(
                        actions=[
                            "secretsmanager:GetSecretValue",
                            "secretsmanager:DescribeSecret"
                        ],
                        effect=_iam.Effect.ALLOW,
                        resources=[
                            f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:pace_splunk_hec_credentials-??????"
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=["s3:GetObject", "s3:HeadObject"],
                        effect=_iam.Effect.ALLOW,
                        resources=[
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/roman_health_ventures/*",
                            f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/data_observability/pace_splunk_observability/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eversana_copay/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/roman_health_ventures/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/paysign_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                            f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/roman_health_ventures/*",
                        ]
                    ),
                    _iam.PolicyStatement(
                        actions=["events:PutRule", "events:PutTargets"],
                        effect=_iam.Effect.ALLOW,
                        resources=[
                            f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/edb_iris*"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpSplunkPACEObservabilityMicsPolicy.node.default_child
        cfn_func.override_logical_id("mpSplunkPACEObservabilityMicsPolicy")

        rLvaSplunkPACEObservabilityRole = _iam.Role(
                self,
                "rLvaSplunkPACEObservabilityRole",
                role_name="edb_buids_lva_splunk_pace_observability_role",
                permissions_boundary=policy,
                max_session_duration=Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                    _iam.ServicePrincipal("lambda.amazonaws.com"),
                    _iam.ServicePrincipal("glue.amazonaws.com"),
                    _iam.ServicePrincipal("s3.amazonaws.com"),
                    _iam.ServicePrincipal("apigateway.amazonaws.com")
                ),
                managed_policies=[
                    mpEHRPiLambdaPolicy,
                    mpEHRPiS3RWPolicy,
                    mpEHRMiscPolicy,
                    mpDQAMiscPolicy,
                    mpEdbIrisReadMinusS3Policy,
                    mpSplunkPACEObservabilityMicsPolicy
                ]
            )
        cfn_func = rLvaSplunkPACEObservabilityRole.node.default_child
        cfn_func.override_logical_id("rLvaSplunkPACEObservabilityRole")

        if config.env in ['qa','prod']:
            rIrisActRestrictedRole = _iam.Role(
                        self,
                        "rIrisActRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_act_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisActRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisActRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisAdsRestrictedRole = _iam.Role(
                        self,
                        "rIrisAdsRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_ads_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [

                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisAdsRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisAdsRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisMtmRestrictedRole = _iam.Role(
                        self,
                        "rIrisMtmRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_mtm_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [

                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy,
                        ]
                    )
            cfn_func = rIrisMtmRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisMtmRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisTcmRestrictedRole = _iam.Role(
                        self,
                        "rIrisTcmRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_tcm_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [

                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy,
                        ]
                    )
            cfn_func = rIrisTcmRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisTcmRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisCptRestrictedRole = _iam.Role(
                        self,
                        "rIrisCptRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_cpt_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy,
                        ]
                    )
            cfn_func = rIrisCptRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisCptRestrictedRole")
        
        rIrisBIACapgeminiBiaMarketplaceRole = _iam.Role(
                        self,
                        "rIrisBIACapgeminiBiaMarketplaceRole",
                        role_name= "aws_edp_capgemini_bia_mp_ro",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisKmsRWPolicy
                        ]
                    )
        cfn_func = rIrisBIACapgeminiBiaMarketplaceRole.node.default_child
        cfn_func.override_logical_id("rIrisBIACapgeminiBiaMarketplaceRole")
        
        if config.env in ['prod']:
            rIrisBIAARole = _iam.Role(
                        self,
                        "rIrisBIAARole",
                        role_name= "aws_edb_biaa_ro",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [ mpEdbIrisKmsRWPolicy
                        ]
                    )
            cfn_func = rIrisBIAARole.node.default_child
            cfn_func.override_logical_id("rIrisBIAARole")
        
        if config.env in ['qa','prod']:
            rIrisBIADDRole = _iam.Role(
                        self,
                        "rIrisBIADDRole",
                        role_name= "aws_edb_biadd_ro",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisKmsRWPolicy
                        ]
                    )
            cfn_func = rIrisBIADDRole.node.default_child
            cfn_func.override_logical_id("rIrisBIADDRole")
        
        if config.env in ['qa','prod']:
            rIrisBIADGRole = _iam.Role(
                        self,
                        "rIrisBIADGRole",
                        role_name= "aws_edb_biadg_ro",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisKmsRWPolicy
                        ]
                    )
            cfn_func = rIrisBIADGRole.node.default_child
            cfn_func.override_logical_id("rIrisBIADGRole")
        
        if config.env in ['qa','prod']:
            rIrisManualFilesRestrictedRole = _iam.Role(
                        self,
                        "rIrisManualFilesRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_manual_files_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisManualFilesRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisManualFilesRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisTurboUsersRestrictedRole = _iam.Role(
                        self,
                        "rIrisTurboUsersRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_turbo_users_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisTurboUsersRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisTurboUsersRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisBrgRestrictedRole = _iam.Role(
                        self,
                        "rIrisBrgRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_brg_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisBrgRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisBrgRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisEdiRestrictedRole = _iam.Role(
                        self,
                        "rIrisEdiRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_edi_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisEdiRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisEdiRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisRelayHealthRestrictedRole = _iam.Role(
                        self,
                        "rIrisRelayHealthRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_relayhealth_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisRelayHealthRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisRelayHealthRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisErxRestrictedRole = _iam.Role(
                        self,
                        "rIrisErxRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_erx_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisErxRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisErxRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisSapScaRestrictedRole = _iam.Role(
                        self,
                        "rIrisSapScaRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_sap_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisSapScaRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisSapScaRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisFive9RestrictedRole = _iam.Role(
                        self,
                        "rIrisFive9RestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_five9_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisFive9RestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisFive9RestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisSymphonyRestrictedRole = _iam.Role(
                        self,
                        "rIrisSymphonyRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_symphony_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisSymphonyRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisSymphonyRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisOpusRestrictedRole = _iam.Role(
                        self,
                        "rIrisOpusRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_opus_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                           mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisOpusRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisOpusRestrictedRole")
        
        rIrisZsFieldInsightsRestrictedRole = _iam.Role(
                self,
                "rIrisZsFieldInsightsRestrictedRole",
                role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_zs_dt_ex",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                managed_policies= [
                    mpEdbIrisReadMinusS3Policy,
                    mpEdbIrisConsolePolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpEdbIrisGluePolicy
                ]
            )
        cfn_func = rIrisZsFieldInsightsRestrictedRole.node.default_child
        cfn_func.override_logical_id("rIrisZsFieldInsightsRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisIncentivesRestrictedRole = _iam.Role(
                        self,
                        "rIrisIncentivesRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_incentives_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
            )
            cfn_func = rIrisIncentivesRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisIncentivesRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisJavelinRestrictedRole = _iam.Role(
                        self,
                        "rIrisJavelinRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_javelin_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisJavelinRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisJavelinRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisIqviaRestrictedRole = _iam.Role(
                        self,
                        "rIrisIqviaRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_iqvia_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisIqviaRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisIqviaRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisCapgeminiRestrictedRole = _iam.Role(
                        self,
                        "rIrisCapgeminiRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_capgemini_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisCapgeminiRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisCapgeminiRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisEversanaRestrictedRole = _iam.Role(
                        self,
                        "rIrisEversanaRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_eversana_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisEversanaRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisEversanaRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisCcpaRestrictedRole = _iam.Role(
                        self,
                        "rIrisCcpaRestrictedRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_ccpa_ex",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisCcpaRestrictedRole.node.default_child
            cfn_func.override_logical_id("rIrisCcpaRestrictedRole")
        
        if config.env in ['qa','prod']:
            rIrisPublicRole = _iam.Role(
                        self,
                        "rIrisPublicRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_public",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisConsolePolicy,
                            mpEdbIrisKmsRWPolicy,
                            mpEdbIrisGluePolicy
                        ]
                    )
            cfn_func = rIrisPublicRole.node.default_child
            cfn_func.override_logical_id("rIrisPublicRole")
        
        if config.env in ['qa','prod']:
            rOperationRole = _iam.Role(
                        self,
                        "rOperationRole",
                        role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_operations",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                        _iam.FederatedPrincipal(
                            f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                            assume_role_action="sts:AssumeRoleWithSAML",
                            conditions={
                                "StringEquals": {
                                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                                }
                            }
                        )),
                        managed_policies= [
                            mpEdbIrisReadMinusS3Policy,
                            mpEdbIrisFederatedServicePolicy,
                            mpEdbIrisGluePolicy,
                            mpEdbIrisAthenaPolicyAdmin,
                            mpEdbIrisFederatedServicePolicy1,
                            # mpEdbIrisS3AdminLandingPolicy,
                            mpEdbIrisS3AdminRawPolicy,
                            mpEdbIrisS3AdminRawOmmPolicy,
                            mpEdbIrisS3AdminRefinedPolicy,
                            FlexDataArchivePolicy,
                            mpEdbIrisS3ExplrtryPolicy,
                            mpEdbIrisRadAwbPolicy
                        ]
                    )
            cfn_func = rOperationRole.node.default_child
            cfn_func.override_logical_id("rOperationRole")
        
        ImpEipDatabrewCommonpolicy=_iam.ManagedPolicy.from_managed_policy_name(
                            self,
                            "ImpEipDatabrewCommonpolicy",
                            managed_policy_name="EipDatabrewCommon"
                            )
        rBRMSConsoleRole = _iam.Role(
                self,
                "rBRMSConsoleRole",
                role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_brms",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.FederatedPrincipal(
                    f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                    assume_role_action="sts:AssumeRoleWithSAML",
                    conditions={
                        "StringEquals": {
                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                        }
                    }
                )),
                managed_policies= [
                    mpEdbIrisBrmsDatabrewSecurityPolicy,
      #              ImpEipDatabrewCommonpolicy
                ]
            )
        _tag.of(rBRMSConsoleRole).add("databrewproject",params['pDatabrewProjectTag'])
        cfn_func = rBRMSConsoleRole.node.default_child
        cfn_func.override_logical_id("rBRMSConsoleRole")
        
        if config.env in ['dev']:
            rDeveloperRole = _iam.Role(
                    self,
                    "rDeveloperRole",
                    role_name= "aws_edb_buids_iris_developers",
                    permissions_boundary= policy,
                    max_session_duration= Duration.seconds(36000),
                    assumed_by=_iam.CompositePrincipal(
                    _iam.FederatedPrincipal(
                        f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                        assume_role_action="sts:AssumeRoleWithSAML",
                        conditions={
                            "StringEquals": {
                                "SAML:aud": "https://signin.aws.amazon.com/saml"
                            }
                        }
                    )),
                    managed_policies= [
                        mpEdbIrisReadMinusS3Policy,
                        mpEdbIrisGluePolicy,
                        mpEdbIrisAthenaPolicyAdmin,
                        mpEdbIrisFederatedServicePolicy,
                        mpEdbIrisFederatedServicePolicy1,
                        # mpEdbIrisS3AdminLandingPolicy,
                        # mpEdbIrisS3AdminRawPolicy,
                        mpEdbIrisS3AdminRawOmmPolicy,
                        # mpEdbIrisS3AdminRefinedPolicy
                    ]
                )
            cfn_func = rDeveloperRole.node.default_child
            cfn_func.override_logical_id("rDeveloperRole")
        
        rZSDataTransferServiceRole = _iam.Role(
                    self,
                    "rZSDataTransferServiceRole",
                    role_name= "edb_buids_iris_zs_service_role",
                    permissions_boundary= policy,
                    max_session_duration= Duration.seconds(36000),
                    assumed_by=_iam.CompositePrincipal(
                    _iam.ServicePrincipal("lambda.amazonaws.com")
                    ),
                    managed_policies= [
                        mpEdbIrisServicePolicy,
                        mpEdbIrisS3AdminRawPolicy,
                        mpEdbIrisS3AdminRawOmmPolicy,
                        mpEdbIrisS3AdminRefinedPolicy,
                        mpEdbIrisS3AdminConformedPolicy,
                        mpEdbIrisKmsRWPolicy,
                        mpEdbIrisS3AdminLandingPolicy
                    ]
                )
        rZSDataTransferServiceRole.add_to_policy(_iam.PolicyStatement(
                actions=[  "sts:AssumeRole"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"{params['pZSDataTransferRole']}"
                    ],
                sid = "zstransferassumerolepolicy"
                ))
        cfn_func = rZSDataTransferServiceRole.node.default_child
        cfn_func.override_logical_id("rZSDataTransferServiceRole")

        # rZSDataTransferServiceRole.add_to_policy(_iam.PolicyStatement(
        #     actions=["s3:PutObject"],
        #     effect=_iam.Effect.ALLOW,
        #     resources=[
        #         f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/*",
        #         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/*",
        #         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/*",
        #         f"arn:aws:s3:::{params['ArtifactBucket']}/*",
        #         f"arn:aws:s3:::{params['ArtifactEdbBucket']}/*"
        #     ],
        #     sid="zsServiceRoleS3PutObject"
        # ))
		
        rVanigentDataTransferServiceRole = _iam.Role(
                    self,
                    "rVanigentDataTransferServiceRole",
                    role_name= "edb_buids_iris_vanigent_service_role",
                    permissions_boundary= policy,
                    max_session_duration= Duration.seconds(36000),
                    assumed_by=_iam.CompositePrincipal(
                    _iam.ServicePrincipal("lambda.amazonaws.com")
                    ),
                    managed_policies= [
                        mpEdbIrisServicePolicy,
                        mpEdbIrisS3AdminRawPolicy,
                        mpEdbIrisS3AdminRawOmmPolicy,
                        mpEdbIrisS3AdminRefinedPolicy,
                        mpEdbIrisS3AdminConformedPolicy,
                        mpEdbIrisKmsRWPolicy,
                        mpEdbIrisS3AdminLandingPolicy
                    ]
                )
        rVanigentDataTransferServiceRole.add_to_policy(_iam.PolicyStatement(
                actions=[  "sts:AssumeRole"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    "arn:aws:iam::790779513551:role/S3UploadRole-Lly-PROD"
                    ],
                sid = "vanigenttransferassumerolepolicy"
                ))
        cfn_func = rVanigentDataTransferServiceRole.node.default_child
        cfn_func.override_logical_id("rVanigentDataTransferServiceRole")
        
        rCCPAServiceRole = _iam.Role(
                self,
                "rCCPAServiceRole",
                role_name= "edb_buids_iris_ccpa_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpCCPAStateMachinePolicy,
                    mpCCPALambdaPolicy,
                    mpCCPAGluePolicy,
                    mpEdbIrisRedshiftDataPolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpEdbIrisS3AdminLandingPolicy,
                    mpEdbIrisS3AdminRawPolicy,
                    mpEdbIrisS3AdminRawOmmPolicy,
                    mpEdbIrisS3AdminRefinedPolicy
                ]
            )


        rCCPAServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "kms:Decrypt",
            "kms:GenerateDataKey"],
            resources=[ f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}"],
            effect=_iam.Effect.ALLOW
        ))
        rCCPAServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[  "secretsmanager:GetSecretValue",
            "secretsmanager:DescribeSecret"],
            resources=[ f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-SystemUser-??????"],
            effect=_iam.Effect.ALLOW,
            sid = "ccpapolicysecrets"
        ))
        cfn_func = rCCPAServiceRole.node.default_child
        cfn_func.override_logical_id("rCCPAServiceRole")
        
        rEHRServiceRole = _iam.Role(
                self,
                "rEHRServiceRole",
                role_name= "iris_ehr_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("databrew.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpEHRLambdaPolicy,
                    mpEHRDatabrewPolicy,
                    mpEHRS3RWPolicy,
                    mpEHRStateMachinePolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpEHRRedshiftDataPolicy,
                    mpEHRMiscPolicy,
                    mpEHRGlueJobPolicy
                ]
            )
        cfn_func = rEHRServiceRole.node.default_child
        cfn_func.override_logical_id("rEHRServiceRole")
        
        
        

        
        role_ceh_bia_service_role = _iam.Role.from_role_arn(self,"role_ceh_bia",role_arn=params['pCEHBiaRoleArn'])
        rCEHBiaRole = _iam.Role(
                self,
                "rCEHBiaRole",
                role_name= "edb_buids_bia_ceh_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ArnPrincipal(role_ceh_bia_service_role.role_arn)
                ),
                managed_policies= [
                    mpEdbIrisKmsRWPolicy,
                    mpBIAS3RefinedROPolicy,
                    mpBIAS3RefinedROPolicy1
                    ]
            )
        cfn_func = rCEHBiaRole.node.default_child
        cfn_func.override_logical_id("rCEHBiaRole")

        rCEHBiaIbuRole = _iam.Role(
                self,
                "rCEHBiaIbuRole",
                role_name= "edb_buids_bia_ibu_ceh_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ArnPrincipal(role_ceh_bia_service_role.role_arn),
                _iam.ArnPrincipal("arn:aws:iam::130087722982:role/BIA-CEH-EC2-Instance-Role")
                ),
                managed_policies= [
                    mpEdbIrisKmsRWPolicy,
                    mpBIAS3ConfROPolicy
                    ]
        )

        mpIFPPolicy = _iam.ManagedPolicy(
            self,
            "mpIFPPolicy",
            description="IFP policy for Lambda Job",
            document=_iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[  "glue:BatchCreatePartition",
                               "glue:BatchGetPartition",
                               "glue:CreateDatabase",
			       "glue:DeleteDatabase",
                               "glue:CreateTable",
                               "glue:Get*",                               "glue:StartCrawler",
                               "glue:UpdateConnection",
                               "glue:UpdatePartition",
                                                             "glue:UpdateTable"],
                                        effect=_iam.Effect.ALLOW,
                                        resources=[ f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog",
                                                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris_pataf",
                                                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_iris_pataf/edb_iris_pataf_*"
                                                            ]
                                        ),
                                        _iam.PolicyStatement(
                                        actions=[  "athena:StartQueryExecution",
                               "athena:StopQueryExecution",
                               "athena:RunQuery",
                               "athena:CancelQueryExecution",
                               "athena:UpdateWorkGroup",
                               ],
                    effect=_iam.Effect.ALLOW,
                                        resources=[ f"arn:aws:athena:{config.deploy_env.region}:{config.deploy_env.account}:workgroup/edb_iris_admin"
                                                            ]
                                        ),
                                        _iam.PolicyStatement(
                                        actions=[ "athena:CreateNamedQuery",
                               "athena:DeleteNamedQuery",
                               "athena:GetNamedQuery",
                               ],
                    effect=_iam.Effect.ALLOW,
                                        resources=[ f"arn:aws:athena:{config.deploy_env.region}:{config.deploy_env.account}:workgroup/edb_iris_admin"
                                                            ]
                                        ),
                                        _iam.PolicyStatement(
                                        actions=[ "lambda:InvokeFunction" ],
                                        effect=_iam.Effect.ALLOW,
                                        resources=[ f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_ifp_*"
                                                            ]
                                        ),
                                        _iam.PolicyStatement(
                                        actions=[ "s3:GetObject" ],
                                        effect=_iam.Effect.ALLOW,
                                        resources=[ f"arn:aws:s3:::lly-edp-refined-us-east-2-qa/iris_lusa_data_quality_restricted/*"
                              ]
                    )
                ]
            )
        )
        cfn_func = mpIFPPolicy.node.default_child
        cfn_func.override_logical_id("mpIFPPolicy")

        self.iris_artifact_bucket = s3.Bucket.from_bucket_arn(
            self, "ArtifactBucket", bucket_arn=f"arn:aws:s3:::{config.artifact_bucket}"
        )

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

        mpEdbIrisS3IncentiveRefinedPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3IncentiveRefinedPolicy",
			description="Incentive refined policy for Lambda Job",
			document=_iam.PolicyDocument(
			statements=[_iam.PolicyStatement(
			    actions=[ "s3:PutObject",
			              "s3:GetObject",
				      "s3:DeleteObject",
				      "s3:DeleteObjectVersion",
				      "s3:ListBucketMultipartUploads",
				      "s3:RestoreObject",
				      "s3:PutObjectVersionTagging",
				      "s3:GetObjectAcl",
				      "s3:GetObjectVersionAcl",
				      "s3:GetObjectTagging",
				      "s3:PutObjectTagging",
				      "s3:GetObjectVersion",
				      "s3:ListBucket",
				       ],
			    effect=_iam.Effect.ALLOW,
			    resources=[ f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_inbound_dataspine/*" #RITM5365519			       
				    ]
			    ),
                _iam.PolicyStatement(
                    actions=[
                        "s3:GetObject",
                        "s3:GetObjectVersion",
                        "s3:PutObject",
                        "s3:AbortMultipartUpload",
                        "s3:ListMultipartUploadParts",
                        "s3:ListBucket"
                    ],
                    resources=object_arns
                ),
                _iam.PolicyStatement(
                    actions=[  
                        "ec2:Describe*",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:CreateTags",
                        "ec2:DeleteTags"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ec2:*:*:instance/*",
                        "arn:aws:ec2:*:*:security-group/*",
                        "arn:aws:ec2:*:*:network-interface/*"
                    ],
                    conditions={
                        "ForAllValues:StringEquals": {
                            "aws:TagKeys": "aws-glue-service-resource"
                        }
                    }
                ),
                _iam.PolicyStatement(
                    actions=[   
                        "ec2:AssignPrivateIpAddresses",
                        "ec2:AttachNetworkInterface",
                        "ec2:UnassignPrivateIpAddresses",
                        "ec2:CreateNetworkInterface",
                        "ec2:DeleteNetworkInterface",
                        "ec2:Describe*",
                        "ec2:ENI*",
                        "ec2:ModifyNetworkInterfaceAttribute",
                        "ec2:SearchTransitGatewayRoutes"
                    ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "*"
                    ]
                )
			]
			)
        )
        
        cfn_func = mpEdbIrisS3IncentiveRefinedPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3IncentiveRefinedPolicy")

        #Anaplan Policy 
        mpG2NAnaplanPolicy = _iam.ManagedPolicy(
            self,
            "mpG2NAnaplanPolicy1",
            managed_policy_name="g2n-anaplan-s3-policy1",
            description="G2N Anaplan S3 and KMS access for Fabric and Anaplan workloads",
            document=_iam.PolicyDocument(
                statements=[
                    _iam.PolicyStatement(
                        actions= [ "s3:List*"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}*",
                            f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        sid="AllowListAllBuckets",
                        effect=_iam.Effect.ALLOW,
                        actions=["s3:ListAllMyBuckets"],
                        resources=["*"]
                    ),
                    _iam.PolicyStatement(
                        sid="S3CreateBucket",
                        effect=_iam.Effect.ALLOW,
                        actions=["s3:CreateBucket"],
                        resources=[
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}*"
                            ]
                    ),
                    _iam.PolicyStatement(
                        sid="AllowConformBucketFullAccess",
                        effect=_iam.Effect.ALLOW,
                        actions=[
                            "s3:GetObjectVersion",
                            "s3:PutObject",
                            "s3:GetObject",
                            "s3:ListBucketMultipartUploads",
                            "s3:RestoreObject",
                            "s3:ListBucket"
                            ],
                        resources=[
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/icyte_transactions_gross_to_net/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iqvia_transactions_gross_to_net/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/speciality_pharma/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/gross_sales_forecast/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/demand_forecast/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/managed_care_partd_invoice_details/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/wholesale_inventory/*",
                            f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/copay_claims_and_payment/*"
                        ]
                    ),
                    _iam.PolicyStatement(
                        sid="AllowKmsForConformBucketObjects",
                        effect=_iam.Effect.ALLOW,
                        actions=[
                            "kms:Decrypt",
                            "kms:Encrypt",
                            "kms:DescribeKey",
                            "kms:GenerateDataKey",
                            "kms:ReEncrypt"
                        ],
                        resources=[
                            f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}"
                        ]
                    )
                ]   
            )
        )
        cfn_func = mpG2NAnaplanPolicy.node.default_child
        cfn_func.override_logical_id("mpG2NAnaplanPolicy")
        
        mpEdbIrisS3AdminDeparturePolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisS3AdminDeparturePolicy",
            description="Edwin policy for unload Job",
            document=_iam.PolicyDocument(
                statements=[_iam.PolicyStatement(
                    actions=[ "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
			    ],
                    effect=_iam.Effect.ALLOW,
                    resources=[ 
                                f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/eversana_edwin_extract/*", #RITM527010
								f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/hcp_meal_expenses_iris_data/*",
								f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iqvia_daily_extract/*",
                                f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*",
                                f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/gross_to_net_anaplan/*",
                                f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/sap_snp_finance_1b/*"
                              ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisS3AdminDeparturePolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisS3AdminDeparturePolicy")

        rGatewayRole = _iam.Role(
                self,
                "rGatewayRole",
                role_name= f"aws_{params['pClientId']}",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.FederatedPrincipal(
                    f"arn:aws:iam::{env.account}:saml-provider/LillyUserAPIGW",
                    assume_role_action="sts:AssumeRoleWithSAML",
                    conditions={
                        "StringEquals": {
                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                        }
                    }
                    ),
                _iam.FederatedPrincipal(
                    f"arn:aws:iam::{env.account}:oidc-provider/login.microsoftonline.com/18a59a81-eea8-4c30-948a-d8824cdc2580/v2.0",
                    assume_role_action="sts:AssumeRoleWithWebIdentity",
                    conditions={
                        "StringEquals": {
                            "login.microsoftonline.com/18a59a81-eea8-4c30-948a-d8824cdc2580/v2.0:aud": f"{params['pClientId']}"
                        }
                    }
                )),
                managed_policies= [
                    mpEdbIrisLambdaPolicy,
                    mpEdbIrisDmsLambdaPolicy,
                    mpEdbIrisRedshiftDataPolicy,
                    mpEdbIrisStateMachinePolicy,
                    mpEdbIrisKmsRWPolicy
                ]
            )
        cfn_func = rGatewayRole.node.default_child
        cfn_func.override_logical_id("rGatewayRole")

        #Anaplan service role
        rG2nAnaplanServiceRole = _iam.Role(
                self,
                "rG2nAnaplanServiceRole",
                role_name= "edb_g2n_anaplan_iris_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com")
                ),
                managed_policies= [
                    mpG2NAnaplanPolicy,
                    mpEdbIrisS3AdminConformedPolicy,
                    mpEdbIrisS3AdminRawPolicy,
                    mpEdbIrisS3AdminRawOmmPolicy,
                    mpAnaplanS3AdminDeparturePolicy,
					mpEdbIrisSecretsPolicyTwo
                ]
            )
        cfn_func = rG2nAnaplanServiceRole.node.default_child
        cfn_func.override_logical_id("rG2nAnaplanServiceRole")

        
        # Allow anaplan role to assume edb_g2n_anaplan_iris_service_role with ExternalId
        rG2nAnaplanServiceRole.assume_role_policy.add_statements(
            _iam.PolicyStatement(
                #sid = "STSAssumeRole",
                effect=_iam.Effect.ALLOW,
                actions=["sts:AssumeRole"],
                principals=[
                    #_iam.AccountRootPrincipal(),
                    _iam.ArnPrincipal(
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_g2n_anaplan_iris_service_role"
                    )
                ]
            )
        )

        rRedshiftServiceRole = _iam.Role(
                self,
                "rRedshiftServiceRole",
                role_name= "edb_iris_redshift_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("scheduler.redshift.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpEdbIrisRedshiftDataPolicy,
                    mpEdbIrisLambdaPolicy,
                    mpEdbIrisDmsLambdaPolicy,
                    mpEdbIrisLogPipelinePolicy,
                    mpEdbIrisRedshiftAdminPolicy
                ]
            )
        cfn_func = rRedshiftServiceRole.node.default_child
        cfn_func.override_logical_id("rRedshiftServiceRole")

        rCmaServiceRole = _iam.Role(
                self,
                "rCmaServiceRole",
                role_name= "edb_buids_iris_cma_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("redshift.amazonaws.com")
                )
            )


        rCmaServiceRole.add_to_policy(_iam.PolicyStatement(
                            actions=["sts:AssumeRole"],
                            effect=_iam.Effect.ALLOW,
                            resources=[
                                f"arn:aws:iam::{params['pCmaAccountId']}:role/lusa_cma_iris_assume_role"
                                ],
                            sid = "AssumeRoleCmaIcyteReporting"
                        ))
        cfn_func = rCmaServiceRole.node.default_child
        cfn_func.override_logical_id("rCmaServiceRole")

        rServiceRole = _iam.Role(
                self,
                "rServiceRole",
                role_name= "edb_buids_iris_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("scheduler.redshift.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("dms.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com"),
                _iam.ServicePrincipal("dms.us-east-2.amazonaws.com"),
                _iam.ServicePrincipal("databrew.us-east-2.amazonaws.com"),
                _iam.ServicePrincipal("events.amazonaws.com"),
                _iam.ServicePrincipal("ssm.amazonaws.com"),
                _iam.ServicePrincipal("athena.amazonaws.com"),
                _iam.ServicePrincipal("apigateway.amazonaws.com")    
                ),
                managed_policies= [
                    mpEdbIrisReadMinusS3Policy,
                    mpEdbIrisGluePolicy,
                    mpEdbIrisSecretsPolicy,
                    mpEdbIrisRedshiftAdminPolicy,
                    mpEdbIrisServicePolicy,
                    mpEdbIrisS3AdminRawPolicy,
                    mpEdbIrisS3AdminRawOmmPolicy,
                    mpEdbIrisS3AdminRefinedPolicy,
                    mpEdbIrisEmployerS3AdminRawRefinedPolicy,
                    mpEdbIrisS3AdminConformedPolicy,
                    mpEdbIrisS3AdminLandingPolicy,
                    mpEdbIrisS3AdminDeparturePolicy,
                    mpEdbIrisSecretsPolicyTwo,
                    mpEdbIrisS3ExplrtryPolicy,
                    mpEdbIrisLambdaPolicy,
                    mpEdbIrisDmsLambdaPolicy,
                    mpEdbIrisRadAwbPolicy,
                    mpIFPPolicy,
		            mpEdbIrisS3IncentiveRefinedPolicy
                ]
            )
        cfn_func = rServiceRole.node.default_child
        cfn_func.override_logical_id("rServiceRole")


        rPCPServiceRole = _iam.Role(
                        self,
                        "rPCPServiceRole",
                        role_name= "edb_buids_iris_pcp_service_role",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                                  _iam.ServicePrincipal("lambda.amazonaws.com"),
                                  _iam.ServicePrincipal("redshift.amazonaws.com"),
                                  _iam.ServicePrincipal("s3.amazonaws.com"),
                                  _iam.ServicePrincipal("states.amazonaws.com"),
                                  _iam.ServicePrincipal("ssm.amazonaws.com")
                        ),
                        managed_policies= [
                        mpEdbIrisKmsRWPolicy,
                        mpEdbIrisServicePolicy,
                        mpEdbIrisRedshiftAdminPolicy,
                        mpEdbIrisSecretsPolicy,
                        mpEdbIrisReadMinusS3Policy,
                        mpEdbIrisSecretsPolicyTwo
                        ]
         )
        cfn_func = rPCPServiceRole.node.default_child
        cfn_func.override_logical_id("rPCPServiceRole")


##########################SES POLICY ###########################################

        rIrisSesPolicy = _iam.Policy(
            self,
            "rIrisSesPolicy",
            policy_name="ris-ses-policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[   "ses:SendEmail",
                                "ses:VerifyEmailIdentity",
                                "ses:SendRawEmail"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ses:us-east-1:539199905087:identity/lilly.com",
                        f"arn:aws:ses:{config.deploy_env.region}:{config.deploy_env.account}:identity/lilly.com"
                                ],
                    conditions={
                        "StringEquals": {
                            "ses:FromAddress": "aws-notifications-${aws:PrincipalAccount}@lilly.com"
                        },
                        "ForAnyValue:StringLike": {
                            "ses:Recipients": ["*@lilly.com",
                                        "*@*.lilly.com"]
                        }
                    }
                    )
                ]
            ),
            roles= [rServiceRole]
        )
        cfn_func = rIrisSesPolicy.node.default_child
        cfn_func.override_logical_id("rIrisSesPolicy")


        rDQAServiceRole = _iam.Role(
                self,
                "rDQAServiceRole",
                role_name= "edb_buids_iris_dqa_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("databrew.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpDQALambdaPolicy,
                    mpDQADatabrewPolicy,
                    mpDQAS3RWPolicy,
                    mpDQAStateMachinePolicy,
                    mpEdbIrisKmsRWPolicy,
                    mpDQARedshiftDataPolicy,
                    mpDQAMiscPolicy,
                    mpDQAGlueJobPolicy
                ]
            )
        _tag.of(rDQAServiceRole).add("dataqualityautomationproject",params['pDataQualityAutomationProjectTag'])
        cfn_func = rDQAServiceRole.node.default_child
        cfn_func.override_logical_id("rDQAServiceRole")

        rEPHServiceRole = _iam.Role(
                self,
                "rEPHServiceRole",
                role_name= "edb_buids_iris_eph_export_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpEdbIrisReadMinusS3Policy,
                    mpEdbIrisKmsRWPolicy,
                    mpEdbIrisLambdaPolicy,
                    mpEdbIrisLogPipelinePolicy,
                    mpEdbEPHSecretsPolicy,
                    mpEdbIrisDmsLambdaPolicy,
                    mpEdbEPHS3Policy
                ]
            )
        cfn_func = rEPHServiceRole.node.default_child
        cfn_func.override_logical_id("rEPHServiceRole")

        pCloudFormationRole_arn =  _iam.Role.from_role_name(
            self,
            "pCloudFormationRole_arn",
            role_name= f"{params['pCloudFormationRole']}"
        )
        rCloudFormationRolePolicy = _iam.Policy(
            self,
            "rCloudFormationRolePolicy",
            policy_name="edb-iris-cloudformation-policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "databrew:CreateDataset",
                              "databrew:DeleteDataset",
                              "databrew:PublishDataset",
                              "databrew:UpdateDataset",
                              "databrew:TagResource",
                              "databrew:UntagResource"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/edb-iris-*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:dataset/iris-edb-*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "databrew:CreateProject",
                              "databrew:DeleteProject",
                              "databrew:UpdateProject",
                              "databrew:TagResource",
                              "databrew:UntagResource"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:project/edb-iris-*",
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:project/iris-edb-*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "databrew:CreateRecipe",
                              "databrew:DeleteRecipeVersion",
                              "databrew:PublishRecipe",
                              "databrew:UpdateRecipe",
                              "databrew:TagResource",
                              "databrew:UntagResource"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:recipe/iris-*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "databrew:CreateRecipeJob",
                              "databrew:DeleteJob",
                              "databrew:UpdateJob",
                              "databrew:TagResource",
                              "databrew:UntagResource"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:job/iris-*"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "databrew:DeleteSchedule",
                              "databrew:UpdateSchedule",
                              "databrew:TagResource",
                              "databrew:UntagResource"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:databrew:{config.deploy_env.region}:{config.deploy_env.account}:schedule/edbIris*"
                    ]
                    )
                ]
            ),
            roles= [pCloudFormationRole_arn ]
        )
        cfn_func = rCloudFormationRolePolicy.node.default_child
        cfn_func.override_logical_id("rCloudFormationRolePolicy")

        rServiceRole.assume_role_policy.add_statements(
            _iam.PolicyStatement(
                sid="AllowDbxCrossAccount",
                effect=_iam.Effect.ALLOW,
                actions=["sts:AssumeRole"],
                principals=[
                    _iam.ArnPrincipal(
                        "arn:aws:iam::414351767826:role/unity-catalog-prod-UCMasterRole-14S5ZJVKOTYTL"
                    ),
                    _iam.ArnPrincipal(
                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_service_role"
                    ),
                ],
                conditions={
                    "StringEquals": {
                        "sts:ExternalId": "7e4a6f59-de54-4b3c-8dc5-fcb503e332aa"
                    }
                },
            )
        )


        rBRGServiceRole = _iam.Role(
                self,
                "rBRGServiceRole",
                role_name= "edb_buids_iris_brg_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                _iam.ServicePrincipal("events.amazonaws.com"),
                _iam.ServicePrincipal("dms.amazonaws.com"),
                _iam.ServicePrincipal("dms.us-east-2.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com")
                ),
                managed_policies= [
                    mpEdbIrisKmsRWPolicy,
                    mpBRGLambdaPolicy,
                    mpEdbIrisLogPipelinePolicy,
                    mpEdbIrisGluePolicy
                ]
        )
        rBRGServiceRole.add_to_policy(_iam.PolicyStatement(
           actions=[  "ssm:GetParameter",
                    "ssm:GetParameters",
                    "ssm:GetParametersByPath",
                    "ssm:PutParameter"],
            effect=_iam.Effect.ALLOW,
            resources=[f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris_brg_867_extract_date"
                    ],
            sid="BrgPolicySsm"
        ))
        rBRGServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=["ses:SendEmail"],
            resources=["arn:aws:ses:us-east-1:539199905087:identity/lilly.com"],
            effect=_iam.Effect.ALLOW,
            sid="BrgPolicySes"
        ))
        rBRGServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "secretsmanager:GetSecretValue"],
            resources=[f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsredshift-brg-medicaid-iris-edb-{params['pEnvironment']}-??????"
            ],
            effect=_iam.Effect.ALLOW,
            sid="Brgpolicysecrets"
        ))
        rBRGServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "kms:Decrypt","kms:GenerateDataKey"],
            resources= [f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}"],
            effect=_iam.Effect.ALLOW,
            sid="brgpolicysecretskms"
        ))
        cfn_func = rBRGServiceRole.node.default_child
        cfn_func.override_logical_id("rBRGServiceRole")

        if config.env in ['qa','prod']:
            rIrisIdsLvaRole = _iam.Role(
                            self,
                            "rIrisIdsLvaRole",
                            role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_lva_ids",
                            permissions_boundary= policy,
                            max_session_duration= Duration.seconds(36000),
                            assumed_by=_iam.CompositePrincipal(
                                _iam.FederatedPrincipal(
                                    f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                                    assume_role_action="sts:AssumeRoleWithSAML",
                                    conditions={
                                        "StringEquals": {
                                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                                        }
                                    }
                            )),
                            managed_policies= [
                                mpEdbIrisReadMinusS3Policy,
                                mpEdbIrisConsolePolicy,
                                mpEdbIrisKmsRWPolicy,
                                mpEdbIrisGluePolicy
                            ]
            )


            rIrisIdsLvaRole.add_to_policy(_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                    effect=_iam.Effect.ALLOW,
                    resources=[
                      f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*", #RITM3795237
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_medicaid_lusa_iris_restricted/*", #RITM3881918
                        f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_medicaid_lusa_iris_restricted/*", #RITM3881918
                        # f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_paid_claims_enriched_restricted/*", #RITM4245015
                        # f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_paid_claims_enriched_restricted/*", #RITM4245015
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hospital_anomaly_detection/*" #RITM4758697, RITM4769700
                      ]
            ))
            rIrisIdsLvaRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_lusa_lva_ids_restricted/*"
                ]
            ))
            rIrisIdsLvaRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                effect=_iam.Effect.ALLOW,
                resources=[f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_lva_ids_ex"]
            ))
            rIrisIdsLvaRole.add_to_policy(_iam.PolicyStatement(
                actions=[ "lambda:InvokeFunction"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"
                    ],
                conditions={
                    "StringEquals": {
                        "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_lva_ids"
                    }
                }
            ))
            rIrisIdsLvaRole.add_to_policy(_iam.PolicyStatement(
                actions=[  "states:DescribeExecution",
                        "states:StartExecution",
                        "states:StopExecution"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_*"
                    ,f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_*"
                    ],
                    conditions={
                        "StringEquals": {
                            "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_lva_ids"
                        }
                    }
            ))
            cfn_func = rIrisIdsLvaRole.node.default_child
            cfn_func.override_logical_id("rIrisIdsLvaRole")

        if config.env in ['qa','prod']:
            rIrisIdsCspRole = _iam.Role(
                            self,
                            "rIrisIdsCspRole",
                            role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_csp_ids",
                            permissions_boundary= policy,
                            max_session_duration= Duration.seconds(36000),
                            assumed_by=_iam.CompositePrincipal(
                                _iam.FederatedPrincipal(
                                    f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                                    assume_role_action="sts:AssumeRoleWithSAML",
                                    conditions={
                                        "StringEquals": {
                                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                                        }
                                    }
                            )),
                            managed_policies= [
                                mpEdbIrisReadMinusS3Policy,
                                mpEdbIrisConsolePolicy,
                                mpEdbIrisKmsRWPolicy,
                                mpEdbIrisGluePolicy
                            ]
            )

            rIrisIdsCspRole.add_to_policy(_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                    effect=_iam.Effect.ALLOW,
                    resources=[
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*" #RITM3795237/*
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*" #RITM3795237
                        ]
            ))
            rIrisIdsCspRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_lusa_csp_ids_restricted/*"
                ]
            ))
            rIrisIdsCspRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                effect=_iam.Effect.ALLOW,
                resources=[f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_csp_ids_ex"]
            ))
            rIrisIdsCspRole.add_to_policy(_iam.PolicyStatement(
                actions=[ "lambda:InvokeFunction"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"
                    ],
                conditions={
                "StringEquals": {
                "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_csp_ids"
                    }
                }
            ))
            rIrisIdsCspRole.add_to_policy(_iam.PolicyStatement(
                actions=[  "states:DescribeExecution",
                        "states:StartExecution",
                        "states:StopExecution"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_*"
                    ,f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_*"
                    ],
                    conditions={
                    "StringEquals": {
                    "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_csp_ids"
                        }
                    }
            ))
            cfn_func = rIrisIdsCspRole.node.default_child
            cfn_func.override_logical_id("rIrisIdsCspRole")

        if config.env in ['qa','prod']:
            rIrisIdsSalesRole = _iam.Role(
                            self,
                            "rIrisIdsSalesRole",
                            role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_sales_ids",
                            permissions_boundary= policy,
                            max_session_duration= Duration.seconds(36000),
                            assumed_by=_iam.CompositePrincipal(
                                _iam.FederatedPrincipal(
                                    f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                                    assume_role_action="sts:AssumeRoleWithSAML",
                                    conditions={
                                        "StringEquals": {
                                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                                        }
                                    }
                            )),
                            managed_policies= [
                                mpEdbIrisReadMinusS3Policy,
                                mpEdbIrisConsolePolicy,
                                mpEdbIrisKmsRWPolicy,
                                mpEdbIrisGluePolicy,
								mpDQADatabrewPolicy,
                                mpEdbIrisFederatedServicePolicy,
                                mpEdbIrisAthenaPolicyAdmin,
                                mpEdbIrisFederatedServicePolicy1,
                                mpEdbIrisS3AdminLandingPolicy,
                                mpEdbIrisS3AdminRawPolicy,
                                mpEdbIrisS3AdminRefinedPolicy,
                                FlexDataArchivePolicy,
                                mpEdbIrisS3ExplrtryPolicy,
                                mpEdbIrisRadAwbPolicy,
                                mpEdbIrisS3AdminConformedPolicy,
                                mpEdbIrisLambdaPolicy,
                                mpEdbIrisLogPipelinePolicy,
                                mpCCPAStateMachinePolicy,
                                mpEdbIrisS3AdminLandingPolicy,
                            ]
            )
            rIrisIdsSalesRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/incentives_lusa_extracts_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/incentives_lusa_extracts_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/act_lusa_activity_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/act_lusa_activity_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*", #RITM3795237
                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*" #RITM3795237
                ]
            ))
            rIrisIdsSalesRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                effect=_iam.Effect.ALLOW,
                resources=[f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_lusa_sales_ids_restricted/*"]
            ))
            rIrisIdsSalesRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                effect=_iam.Effect.ALLOW,
                resources=[f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_sales_ids_ex"]
            ))
            rIrisIdsSalesRole.add_to_policy(_iam.PolicyStatement(
                actions=[ "lambda:InvokeFunction"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda",
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3",
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*",
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*",
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"
                ],
                conditions = {
                    "StringEquals": {
                        "aws:PrincipalArn": [
                            {
                                "Fn::Sub": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_sales_ids"
                            }
                        ]
                    }
                }
            ))
            rIrisIdsSalesRole.add_to_policy(_iam.PolicyStatement(
                actions=[ "states:DescribeExecution",
                        "states:StartExecution",
                        "states:StopExecution"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_*",
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_*"
                ],
                conditions = {
                            "StringEquals": {
                                "aws:PrincipalArn": [
                                    {
                                        "Fn::Sub": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_sales_ids"
                                    }
                                ]
                            }
                        }
            ))
            cfn_func = rIrisIdsSalesRole.node.default_child
            cfn_func.override_logical_id("rIrisIdsSalesRole")

        if config.env in ['qa','prod']:
            rIrisIdsMarketingRole = _iam.Role(
                            self,
                            "rIrisIdsMarketingRole",
                            role_name= f"aws_edb_buids_iris_{params['pEnvironment']}_marketing_ids",
                            permissions_boundary= policy,
                            max_session_duration= Duration.seconds(36000),
                            assumed_by=_iam.CompositePrincipal(
                                _iam.FederatedPrincipal(
                                    f"arn:aws:iam::{env.account}:saml-provider/{params['pSamlProviderAdmin']}",
                                    assume_role_action="sts:AssumeRoleWithSAML",
                                    conditions={
                                        "StringEquals": {
                                            "SAML:aud": "https://signin.aws.amazon.com/saml"
                                        }
                                    }
                            )),
                            managed_policies= [
                                mpEdbIrisReadMinusS3Policy,
                                mpEdbIrisConsolePolicy,
                                mpEdbIrisKmsRWPolicy,
                                mpEdbIrisGluePolicy
                            ]
            )
            rIrisIdsMarketingRole.add_to_policy(_iam.PolicyStatement(
                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                    effect=_iam.Effect.ALLOW,
                    resources=[
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/match_list_lusa_marketing_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/match_list_lusa_marketing_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_lusa_affinity_monitor_restricted/*" #RITM3795237
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_lusa_affinity_monitor_restricted/*" #RITM3795237
                        ]
            ))
            rIrisIdsMarketingRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_lusa_marketing_ids_restricted/*"
                ]
            ))
            rIrisIdsMarketingRole.add_to_policy(_iam.PolicyStatement(
                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                effect=_iam.Effect.ALLOW,
                resources=[f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_marketing_ids_ex"]
            ))
            rIrisIdsMarketingRole.add_to_policy(_iam.PolicyStatement(
                actions=[ "lambda:InvokeFunction"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_landing_to_raw_lambda"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_audit_log_s3"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                    ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"
                    ],
                conditions={
                    "StringEquals": {
                        "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_marketing_ids"
                    }
                }
            ))
            rIrisIdsMarketingRole.add_to_policy(_iam.PolicyStatement(
                actions=[  "states:DescribeExecution",
                        "states:StartExecution",
                        "states:StopExecution"],
                effect=_iam.Effect.ALLOW,
                resources=[
                    f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_*"
                    ,f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_*"
                    ],
                    conditions={
                    "StringEquals": {
                        "aws:PrincipalArn": f"arn:aws:iam::{config.deploy_env.account}:role/aws_edb_buids_iris_qa_marketing_ids"
                    }
                }
            ))
            cfn_func = rIrisIdsMarketingRole.node.default_child
            cfn_func.override_logical_id("rIrisIdsMarketingRole")
        
        rCCOrchServiceRole = _iam.Role(
                        self,
                        "rCCOrchServiceRole",
                        role_name= "edb_buids_iris_cc_orch_service_role",
                        permissions_boundary= policy,
                        max_session_duration= Duration.seconds(36000),
                        assumed_by=_iam.CompositePrincipal(
                                  _iam.ServicePrincipal("lambda.amazonaws.com")
                        )
         )

        rCCOrchServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "lambda:InvokeAsync",
                      "lambda:InvokeFunction"],
            resources=[ 
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_cc_crossacnt_glue_trigger",
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow"
                        ],
            effect=_iam.Effect.ALLOW,
            sid =  "mhsccpolicylambda"
        ))

        rCCOrchServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "logs:CreateLogStream",
                        "logs:CreateLogGroup",
                        "logs:AssociateKmsKey",
                        "logs:PutLogEvents",
                        "logs:Describe*",
                        "logs:FilterLogEvents",
                        "logs:Get*",
                        "logs:List*",
                        "logs:StartQuery",
                        "logs:TestMetricFilter"],
            resources=[ f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_cc_crossacnt_glue_trigger*"],
            effect=_iam.Effect.ALLOW
        ))

        rCCOrchServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "sts:AssumeRole"],
            resources=[ params['pIRISCCRole']],
            effect=_iam.Effect.ALLOW
        ))
        cfn_func = rCCOrchServiceRole.node.default_child
        cfn_func.override_logical_id("rCCOrchServiceRole")


############################ Final Policies #############################
        
        rBRMSGlueConnectionPolicy = _iam.Policy(
                self,
                "rBRMSGlueConnectionPolicy",
                policy_name="edb-lusa-brms-glue-connection-policy",
                document= _iam.PolicyDocument(
                    statements= [_iam.PolicyStatement(
                        actions=[ "glue:Get*",
                                "glue:UpdateConnection"
                                ],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_lusa_brms*",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                                    ]
                                    )
                    ]
                ),
                roles= [ rSecretsManagerRole,
                        rBRMSServiceRole
                ]
        )
        cfn_func = rBRMSGlueConnectionPolicy.node.default_child
        cfn_func.override_logical_id("rBRMSGlueConnectionPolicy")
        
        rDQAGlueConnectionPolicy = _iam.Policy(
                self,
                "rDQAGlueConnectionPolicy",
                policy_name="edb-lusa-dqa-glue-connection-policy",
                document= _iam.PolicyDocument(
                    statements= [_iam.PolicyStatement(
                        actions=[  "glue:Get*",
                            "glue:UpdateConnection",
                            "glue:CreateTable",
                            "glue:UpdateTable",
                            "glue:BatchGetPartition",
                            "glue:BatchCreatePartition",
                            "glue:CreateDatabase",
                            "glue:StartCrawler",
                            "glue:UpdatePartition"
                            ],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris_dqa*",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/iris-dqa-*",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/iris-dqa-*",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/iris-dqa-*",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris_soa_databrew_redshift_connection",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris*",
                            f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris*",
                            ]
                        )
                    ]
                ),
                roles= [
                    rDQAServiceRole,
                    rSecretsManagerRole
                    ]
            )
        cfn_func = rDQAGlueConnectionPolicy.node.default_child
        cfn_func.override_logical_id("rDQAGlueConnectionPolicy")

        rS3IrisBiaOmnichannelPolicy = _iam.Policy(
                    self,
                    "rS3IrisBiaOmnichannelPolicy",
                    policy_name="edb-glue-bia-iris-omnichannel-policy",
                    document= _iam.PolicyDocument(
                        statements= [_iam.PolicyStatement(
                            actions=[  "glue:Get*",
                                "glue:List*",
                                "glue:CreateDatabase"],
                            effect= _iam.Effect.ALLOW,
                            resources= [
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris_omnichannel_refined",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_omt_adhoc_list",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_omt_list_management",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/vvpm*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/vvmc*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/cmi_refined_media_cost_db*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                            ]
                            ),
                            _iam.PolicyStatement(
                            actions=[ "glue:BatchCreatePartition",
                              "glue:BatchDeletePartition",
                              "glue:BatchDeleteTable",
                              "glue:BatchGetPartition",
                              "glue:Get*"],
                            effect= _iam.Effect.ALLOW,
                            resources= [
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_iris*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/eph_*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/vvpm_*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/cmi_refined_media_cost_db*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/vvpm*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/cmi_refined_media_cost_db*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/vvmc_*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/vvmc*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_gccp*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_iris*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:userDefinedFunction/edb_iris*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:job/edb_iris*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:crawler/edb_iris*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_iris*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:database/edb_omt*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/list_management_*/*",
                                f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:table/edb_omt_*/*"
                                        ]
                            )
                        ]
                    ),
                    roles= [
                        rCEHBiaRole
                        ]
                )
        cfn_func = rS3IrisBiaOmnichannelPolicy.node.default_child
        cfn_func.override_logical_id("rS3IrisBiaOmnichannelPolicy")

        rLMGlueConnectionPolicy = _iam.Policy(
            self,
            "rLMGlueConnectionPolicy",
            policy_name="edb-lusa-lm-glue-connection-policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[    "glue:Get*",
                                "glue:UpdateConnection"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:connection/edb_lusa_lm*",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:catalog"
                                ]
                    )
                ]
            ),
            roles= [rSecretsManagerRole,rLMServiceRole]
        )
        cfn_func = rLMGlueConnectionPolicy.node.default_child
        cfn_func.override_logical_id("rLMGlueConnectionPolicy")

        if config.env in ['dev']:
            role_rIrisS3IqviaScrubPolicy = [rServiceRole,rDeveloperRole]
        elif config.env in ['qa']:
            role_rIrisS3IqviaScrubPolicy = [rServiceRole,rOperationRole,rIrisIdsLvaRole,rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole]
        else :
            role_rIrisS3IqviaScrubPolicy = [rServiceRole,rOperationRole]
        rIrisS3IqviaScrubPolicy = _iam.Policy(
                        self,
                        "rIrisS3IqviaScrubPolicy",
                        policy_name= "edb-iris-s3-iqvia-scrub-policy",
                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=[ "s3:List*",
                                            "s3:Get*",
                                            "s3:PutObject*",
                                            "s3:DeleteObject",
                                            "s3:DeleteObjectVersion"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/flex_lusa_paid_claims_restricted/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/flex_lusa_paid_claims_restricted/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_rebate_scrub_lusa_dataextracts_restricted/*"
                                ]
                                )
                            ]
                        ),
                        roles=role_rIrisS3IqviaScrubPolicy
                    )
        cfn_func = rIrisS3IqviaScrubPolicy.node.default_child
        cfn_func.override_logical_id("rIrisS3IqviaScrubPolicy")

        rS3LndGatewayPolicy = _iam.Policy(
            self,
            "rS3LndGatewayPolicy",
            policy_name="edb-s3-landing-iris-gw",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[     "kms:ListAliases",
                                "cloudwatch:GetMetricStatistics",
                                "cloudwatch:ListMetrics"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*" ]
                    ),
                    _iam.PolicyStatement(
                    actions=[      "kms:Encrypt"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:alias/aws-kms-edb-s3"]
                    ),
                    _iam.PolicyStatement(
                    actions=["s3:GetBucketLocation",
                                "s3:GetBucketVersioning",
                                "s3:ListBucketVersions",
                                "s3:ListBucket",
                                "s3:GetMetricsConfiguration"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}",
                        f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "s3:PutObject",
                                "s3:PutObjectTagging",
                                "s3:PutObjectVersionTagging"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*", # RITM3026470, RITM3057102
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*",  #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/lilly_mdm/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/targeting_lists_iris/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", #pre-approved(RITM3140803)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*", #RITM3140803 pre=approved
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3346617
                        f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*", #RITM3429800
                        f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/flex_lusa_iris_restricted/*", #RITM3429800
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/mtm_lusa_product_restricted/*", # RITM3296073-QA RITM3296079-Prod
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/act_lusa_activity_restricted/*", # RITM3587665-QA RITM3587698- Prod, RITM3623034
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/manual_business_files_pr/*", #RITM3702639
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*",  #RITM3702639
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ibu_omnichannel/*", #RITM3729338
                        f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/met_extract/*",
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/esi_optum_prime_zinc_caremark_cmm_humana/*", #RITM3610484, RITM3863681
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Caremark/*", #Pre-approved (RITM4109795)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ESI_Enrollment/*", #Pre-approved (RITM4109795)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Optum/*", #Pre-approved (RITM4109795)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*", #Pre-approved (RITM4109795)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Humana/*", #Pre-approved (RITM4109795)
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/carevalue_pap_business_files/*", #Pre-approved (RITM4118552)
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_medicaid_lusa_iris_restricted/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/outbox/VendorExtracts/*"
                       ]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "s3:GetObject",
                                "s3:GetObjectTagging",
                                "s3:GetObjectVersionTagging"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/verso/*"
                    ]
                    )
                ]
            ),
            roles= [rGatewayRole]
        )
        cfn_func = rS3LndGatewayPolicy.node.default_child
        cfn_func.override_logical_id("rS3LndGatewayPolicy")

        rRedshiftServicePolicy = _iam.Policy(
            self,
            "rRedshiftServicePolicy",
            policy_name="edb-iris-redshift-srvc-rw",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[  "secretsmanager:GetSecretValue",
                                "secretsmanager:DescribeSecret"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:iris_srvc_account_pat-??????",
                        f"arn:aws:glue:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-SystemUser-??????"
                                ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "secretsmanager:ListSecrets"],
                    effect= _iam.Effect.ALLOW,
                    resources= ["*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[   "kms:Decrypt",
                                "kms:GenerateDataKey"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisSmKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRDSSecretKmsKey']}"
                    ]
                    )
                ]
            ),
            roles= [rRedshiftServiceRole]
        )
        cfn_func = rRedshiftServicePolicy.node.default_child
        cfn_func.override_logical_id("rRedshiftServicePolicy")

        if config.env in ['qa','prod']:
            roles_rS3IrisListPolicy = [rOperationRole,
                                       rSecretsManagerRole,
                                       rServiceRole,
                                       rG2nAnaplanServiceRole,
                                       rEHRPiServiceRole,
                                       rLvaSplunkObservabilityRole,
                                       rLvaSplunkObservabilityOmmRole,
                                       rLvaSplunkPACEObservabilityRole,
                                       rCCPAServiceRole,
                                       rEPHServiceRole,
                                       rZSDataTransferServiceRole,
									   rVanigentDataTransferServiceRole,
                                       rIrisPublicRole,
                                       rIrisEversanaRestrictedRole,
                                    rIrisCapgeminiRestrictedRole,
                                    rIrisIqviaRestrictedRole,
                                    rIrisOpusRestrictedRole,
                                    rIrisSymphonyRestrictedRole,
                                    rIrisFive9RestrictedRole,
                                    rIrisSapScaRestrictedRole,
                                    rIrisErxRestrictedRole,
                                    rIrisRelayHealthRestrictedRole,
                                    rIrisEdiRestrictedRole,
                                    rIrisManualFilesRestrictedRole,
                                    rIrisCcpaRestrictedRole,  # RITM3026470, RITM3057102
                                    rIrisJavelinRestrictedRole,  #RITM3134999
                                    rIrisIncentivesRestrictedRole,
                                    rIrisBrgRestrictedRole, #RITM3346617
                                    rIrisIdsLvaRole,
                                    rIrisIdsSalesRole,
                                    rIrisIdsMarketingRole,
                                    rIrisIdsCspRole,
                                    rIrisZsFieldInsightsRestrictedRole
                                       ]
        else :
            roles_rS3IrisListPolicy = [rDeveloperRole,
                                       rSecretsManagerRole,
                                       rServiceRole,
                                       rG2nAnaplanServiceRole,
                                       rEHRPiServiceRole,
                                       rLvaSplunkObservabilityRole,
                                       rLvaSplunkObservabilityOmmRole,
                                       rLvaSplunkPACEObservabilityRole,
                                       rCCPAServiceRole,
                                       rEPHServiceRole,
                                       rZSDataTransferServiceRole,
									   rVanigentDataTransferServiceRole
                                       ]
        rS3IrisListPolicy = _iam.Policy(
            self,
            "rS3IrisListPolicy",
            policy_name="edb-s3-iris-l",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[    "s3:GetAccelerateConfiguration",
                                "s3:GetAnalyticsConfiguration",
                                "s3:GetBucket*",
                                "s3:GetEncryptionConfiguration",
                                "s3:GetIntelligentTieringConfiguration",
                                "s3:GetInventoryConfiguration",
                                "s3:GetLifecycleConfiguration",
                                "s3:GetMetricsConfiguration",
                                "s3:GetReplicationConfiguration",
                                "s3:ListBucket",
                                "s3:ListBucketVersions",
                                "s3:ListMultipartUploadParts",
                                "s3:PutBucketNotification"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}"
                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}"
                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                        ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}"
                        ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}"
                        ,f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}" #RITM3424004
                        ,f"arn:aws:s3:::{params['ArtifactBucket']}"
                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}"
                    ]
                    )
                ]
            ),
            roles= roles_rS3IrisListPolicy
        )
        cfn_func = rS3IrisListPolicy.node.default_child
        cfn_func.override_logical_id("rS3IrisListPolicy")

        if config.env in ['qa','prod']:
            role_rIrisEPHCODSPolicy = [rOperationRole, rServiceRole, rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole]
        else :
            role_rIrisEPHCODSPolicy = [rDeveloperRole, rServiceRole, rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole]
        rIrisEPHCODSPolicy = _iam.Policy(
            self,
            "rIrisEPHCODSPolicy",
            policy_name="edb-iris-eph-cods-policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[   "s3:GetObject",
                                "s3:GetObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:GetObjectVersion",
                                "s3:ListBucket"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/enterprisecustomer/eph/consumption/cods/data/full/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/enterprisecustomer/rdm/data/processed/rdmlov/*"
                                ]
                    )
                ]
            ),
            roles=role_rIrisEPHCODSPolicy
        )
        cfn_func = rIrisEPHCODSPolicy.node.default_child
        cfn_func.override_logical_id("rIrisEPHCODSPolicy")

        rIrisEPHLOVPolicy = _iam.Policy(
            self,
            "rIrisEPHLOVPolicy",
            policy_name="edb-iris-eph-lov-policy",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[    "s3:GetObject",
                                "s3:ListBucketMultipartUploads",
                                "s3:GetObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:GetObjectVersion",
                                "s3:ListBucket"],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/enterprisecustomer/rdm/data/processed/*"]
                    )
                ]
            ),
            roles= [rServiceRole ]
        )
        cfn_func = rIrisEPHLOVPolicy.node.default_child
        cfn_func.override_logical_id("rIrisEPHLOVPolicy")

        rIrisNBEEPHPolicy = _iam.Policy(
                        self,
                        "rIrisNBEEPHPolicy",
                        policy_name= "edb-iris-nbe-eph-policy",
                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=[ "s3:GetObject",
                                            "s3:ListBucketMultipartUploads",
                                            "s3:GetObjectAcl",
                                            "s3:GetObjectVersionAcl",
                                            "s3:GetObjectTagging",
                                            "s3:GetObjectVersion",
                                            "s3:ListBucket"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/enterprisecustomer/rdm/data/processed/*"
                                ]
                                )
                            ]
                        ),
                        roles= [rServiceRole]
                    )
        cfn_func = rIrisNBEEPHPolicy.node.default_child
        cfn_func.override_logical_id("rIrisNBEEPHPolicy")

        if config.env in ['dev'] :
            rS3EdbABCLibPolicy = _iam.Policy(
                    self,
                    "rS3EdbABCLibPolicy",
                    policy_name="edb-s3-get-abc-lib",
                    document= _iam.PolicyDocument(
                        statements= [_iam.PolicyStatement(
                            actions=[   "s3:GetBucketAcl",
                                        "s3:GetBucketLocation",
                                        "s3:ListAllMyBuckets",
                                        "s3:ListBucket"],
                            effect= _iam.Effect.ALLOW,
                            resources= [
                                f"arn:aws:s3:::lly-edp-codeconfig-us-east-2-{params['pBucketPrefix']}/edb-core/core/abc/libs/glue/glueetl/*"
                                ]
                            )
                        ]
                    ),
                    roles= [
                        rServiceRole,
                        rOperationRole
                        ]
                )
            cfn_func = rS3EdbABCLibPolicy.node.default_child
            cfn_func.override_logical_id("rS3EdbABCLibPolicy")

        if config.env in ['qa','prod']:
            role_rS3IrisReadWritePolicy = [rServiceRole ,rOperationRole,rZSDataTransferServiceRole,rVanigentDataTransferServiceRole,rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole,rG2nAnaplanServiceRole]
        else :
            role_rS3IrisReadWritePolicy = [rServiceRole ,rDeveloperRole,rZSDataTransferServiceRole,rVanigentDataTransferServiceRole,rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole,rG2nAnaplanServiceRole]
        rS3IrisReadWritePolicy = _iam.Policy(
                self,
                "rS3IrisReadWritePolicy",
                policy_name="edb-s3-iris-rw",
                document= _iam.PolicyDocument(
                    statements= [_iam.PolicyStatement(
                        actions=[ "s3:PutObject",
                                "s3:GetObject",
                                "s3:DeleteObject",
                                "s3:DeleteObjectVersion",
                                "s3:ListBucketMultipartUploads",
                                "s3:RestoreObject",
                                "s3:PutObjectVersionTagging",
                                "s3:GetObjectAcl",
                                "s3:GetObjectVersionAcl",
                                "s3:GetObjectTagging",
                                "s3:PutObjectTagging",
                                "s3:GetObjectVersion",
                                "s3:ListBucket"],
                        effect= _iam.Effect.ALLOW,
                        resources= [
                           f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris/*"
                            ,f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*"
                            ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/incentives_lusa_extracts_restricted/*"
                            ,f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/*" #RITM3424004
                            ,f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*" #
                            ]
                        )
                    ]
                ),
                roles=role_rS3IrisReadWritePolicy
            )
        cfn_func = rS3IrisReadWritePolicy.node.default_child
        cfn_func.override_logical_id("rS3IrisReadWritePolicy")

        if config.env in ['qa','prod'] :
            rS3IrisBiaDGRoPolicy = _iam.Policy(
                    self,
                    "rS3IrisBiaDGRoPolicy",
                    policy_name="edb-s3-biadg-iris-ro",
                    document= _iam.PolicyDocument(
                        statements= [_iam.PolicyStatement(
                            actions=[  "s3:ListAllMyBuckets",
                                    "s3:GetBucketLocation",
                                    "s3:ListAccessPoints"],
                            effect= _iam.Effect.ALLOW,
                            resources= ["*"]
                            ),
                            _iam.PolicyStatement(
                            actions=[   "s3:ListBucket",
                                    "s3:ListBucketMultipartUploads"],
                            effect= _iam.Effect.ALLOW,
                            resources= [
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                                        ]
                            ),
                            _iam.PolicyStatement(
                            actions=[   "s3:GetBucketTagging",
                                    "s3:GetObject",
                                    "s3:GetObjectTagging"],
                            effect= _iam.Effect.ALLOW,
                            resources= [
                              f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                                f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lilly_mdm/*",
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", # RITM3140803
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*", #Pre-approved (pre-RITM process)
                                f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*" #Pre-approved (pre-RITM process)1
                                        ]
                            )
                        ]
                    ),
                    roles= [
                        rIrisBIADGRole
                        ]
                )
            cfn_func = rS3IrisBiaDGRoPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisBiaDGRoPolicy")
        
        if config.env in ['qa','prod']:
            rS3IrisBiaDDRoPolicy = _iam.Policy(
                        self,
                        "rS3IrisBiaDDRoPolicy",
                        policy_name= "edb-s3-biadd-iris-ro",

                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=[   "s3:ListAllMyBuckets",
                                    "s3:GetBucketLocation",
                                    "s3:ListAccessPoints"],
                                effect= _iam.Effect.ALLOW,
                                resources= ["*"]
                                ),
                                _iam.PolicyStatement(
                                actions=[   "s3:ListBucket",
                                    "s3:ListBucketMultipartUploads"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                                            ]
                                ),
                                _iam.PolicyStatement(
                                actions=[  "s3:GetBucketTagging",
                                    "s3:GetObject",
                                    "s3:GetObjectTagging"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lilly_mdm/*",
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*", #RITM3306104
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", # RITM3140803
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*"
                                            ]
                                )
                            ]
                        ),
                        roles= [
                            rIrisBIADDRole
                            ]
                    )
            cfn_func = rS3IrisBiaDDRoPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisBiaDDRoPolicy")

        if config.env in ['prod'] :
            rS3IrisBiaaRoPolicy = _iam.Policy(
                        self,
                        "rS3IrisBiaaRoPolicy",
                        policy_name= "edb-s3-biaa-iris-ro",

                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=[   "s3:ListAllMyBuckets",
                                "s3:GetBucketLocation",
                                "s3:ListAccessPoints"],
                                effect= _iam.Effect.ALLOW,
                                resources= ["*"]
                                ),
                                _iam.PolicyStatement(
                                actions=[    "s3:ListBucket",
                                "s3:ListBucketMultipartUploads"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                                            ]
                                ),
                                _iam.PolicyStatement(
                                actions=[   "s3:GetBucketTagging",
                                "s3:GetObject",
                                "s3:GetObjectTagging"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lilly_mdm/*",
                                    f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*", #RITM3306104
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*", # RITM3140803
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*", #Pre-approved (pre-RITM process)
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations_restricted/*"
                               ]
                                )
                            ]
                        ),
                        roles= [
                            rIrisBIAARole
                            ]
                    )
            cfn_func = rS3IrisBiaaRoPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisBiaaRoPolicy")

        rS3IrisCapgeminiBiaMarketplaceRoPolicy = _iam.Policy(
                        self,
                        "rS3IrisCapgeminiBiaMarketplaceRoPolicy",
                        policy_name= "edb-s3-capgemini-bia-marketplace-iris-ro",

                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=[  "s3:ListAllMyBuckets",
                                "s3:GetBucketLocation",
                                "s3:ListAccessPoints"],
                                effect= _iam.Effect.ALLOW,
                                resources= ["*"]
                                ),
                                _iam.PolicyStatement(
                                actions=[  "s3:ListBucket",
                                "s3:ListBucketMultipartUploads"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                                            ]
                                ),
                                _iam.PolicyStatement(
                                actions=[ "s3:GetBucketTagging",
                                        "s3:GetObject",
                                        "s3:GetObjectTagging"],
                                effect= _iam.Effect.ALLOW,
                                resources= [
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*"
                                            ]
                                )
                            ]
                        ),
                        roles= [
                          rIrisBIACapgeminiBiaMarketplaceRole
                            ]
                    )
        cfn_func = rS3IrisCapgeminiBiaMarketplaceRoPolicy.node.default_child
        cfn_func.override_logical_id("rS3IrisCapgeminiBiaMarketplaceRoPolicy")

        if config.env in ['qa']:
            role_rVES3DepartureRWPolicy = [rOperationRole, rServiceRole,rIrisPublicRole]
        elif config.env in ['prod']:
            role_rVES3DepartureRWPolicy = [rOperationRole, rServiceRole]
        else :
            role_rVES3DepartureRWPolicy = [rDeveloperRole, rServiceRole]
        rVES3DepartureRWPolicy = _iam.Policy(
                        self,
                        "rVES3DepartureRWPolicy",
                        policy_name= "ve-s3-departure-write-policy",

                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=[ "s3:PutObject*",
                                "s3:GetObject",
                                "s3:List*"],
                                effect= _iam.Effect.ALLOW,
                                resources= [f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_precision_extracts/*" #RITM3893292
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_rxvantage_extracts/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_lilly_internal_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_physicians_world_hcp_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_boehringer_ingelheim_sales_rep_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_element_fleet_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_government_third_Party_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_hibbert_hcp_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_legal_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_report_management_facility_extract/*"
                                ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/iris_syneos_inventive_extract/*"
                                ]
                                )
                            ]
                        ),
                        roles= role_rVES3DepartureRWPolicy
                    )
        cfn_func = rVES3DepartureRWPolicy.node.default_child
        cfn_func.override_logical_id("rVES3DepartureRWPolicy")

        if config.env in ['qa','prod'] :
            rS3IrisRawPublicPolicy = _iam.Policy(
                            self,
                            "rS3IrisRawPublicPolicy",
                            policy_name= 'edb-s3-raw-public-iris',

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                      f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lilly_mdm/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lusa_janrain/*",              
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/lusa_lilly_play/*",              
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/targeting_lists_iris/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_campaign_metadata/*",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_verso_recommendations/*"
                                    ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisPublicRole,
                                rIrisEversanaRestrictedRole,
                                rIrisCapgeminiRestrictedRole,
                                rIrisIqviaRestrictedRole,
                                rIrisOpusRestrictedRole,
                                rIrisSymphonyRestrictedRole,
                                rIrisFive9RestrictedRole,
                                rIrisSapScaRestrictedRole,
                                rIrisErxRestrictedRole,
                                rIrisRelayHealthRestrictedRole,
                                rIrisEdiRestrictedRole,
                                rIrisManualFilesRestrictedRole,
                                rIrisCcpaRestrictedRole, # RITM3026470, RITM3057102,
                                rIrisTcmRestrictedRole,
                                rIrisCptRestrictedRole,
                                rIrisJavelinRestrictedRole,
                                rIrisIncentivesRestrictedRole,
                                rIrisBrgRestrictedRole, #RITM3346617,
                                rIrisIdsLvaRole,
                                rIrisIdsSalesRole,
                                rIrisIdsMarketingRole,
                                rIrisIdsCspRole,
                                rIrisZsFieldInsightsRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisRawPublicPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisRawPublicPolicy")

        if config.env in ['prod']:
            roles_rS3IrisRefPublicPolicy = [
                            rIrisPublicRole,
                            rIrisBIADGRole,
                            rIrisBIADDRole,
                            rIrisBIAARole,
                            rIrisEversanaRestrictedRole,
                            rIrisCapgeminiRestrictedRole,
                            rIrisIqviaRestrictedRole,
                            rIrisOpusRestrictedRole,
                            rIrisSymphonyRestrictedRole,
                            rIrisFive9RestrictedRole,
                            rIrisSapScaRestrictedRole,
                            rIrisErxRestrictedRole,
                            rIrisRelayHealthRestrictedRole,
                            rIrisEdiRestrictedRole,
                            rIrisManualFilesRestrictedRole,
                            rIrisCcpaRestrictedRole,
                            rIrisCptRestrictedRole,
                            rIrisTcmRestrictedRole,
                            rIrisJavelinRestrictedRole,
                            rIrisIncentivesRestrictedRole,
                            rIrisBrgRestrictedRole,
                            rIrisIdsLvaRole,
                            rIrisIdsSalesRole,
                            rIrisIdsMarketingRole,
                            rIrisIdsCspRole,
                            rIrisZsFieldInsightsRestrictedRole
            ]
        else :
            roles_rS3IrisRefPublicPolicy = [rIrisPublicRole,
                            rIrisBIADGRole,
                            rIrisBIADDRole,
                            rIrisEversanaRestrictedRole,
                            rIrisCapgeminiRestrictedRole,
                            rIrisIqviaRestrictedRole,
                            rIrisOpusRestrictedRole,
                            rIrisSymphonyRestrictedRole,
                            rIrisFive9RestrictedRole,
                            rIrisSapScaRestrictedRole,
                            rIrisErxRestrictedRole,
                            rIrisRelayHealthRestrictedRole,
                            rIrisEdiRestrictedRole,
                            rIrisManualFilesRestrictedRole,
                            rIrisCcpaRestrictedRole,
                            rIrisCptRestrictedRole,
                            rIrisTcmRestrictedRole,
                            rIrisJavelinRestrictedRole,
                            rIrisIncentivesRestrictedRole,
                            rIrisBrgRestrictedRole,
                            rIrisIdsLvaRole,
                            rIrisIdsSalesRole,
                            rIrisIdsMarketingRole,
                            rIrisIdsCspRole,
                            rIrisZsFieldInsightsRestrictedRole
                            ]

        if config.env in ['qa','prod'] :
            rS3IrisRefPublicPolicy = _iam.Policy(
                            self,
                            "rS3IrisRefPublicPolicy",
                            policy_name= "edb-s3-ref-public-iris",
                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lilly_mdm/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lusa_janrain/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/lusa_lilly_play/*",              
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/targeting_lists_iris/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/veeva_lusa_objects/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_campaign_metadata/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_verso_recommendations/*",
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/manual_business_files_pr/*", #RITM3702639
                                    f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/manual_business_files_pr_restricted/*"  #RITM3702639
                                    ]
                                    )
                                ]
                            ),
                            roles= roles_rS3IrisRefPublicPolicy
                        )
            cfn_func = rS3IrisRefPublicPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisRefPublicPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisPublicPolicy = _iam.Policy(
                        self,
                        "pAthenaIrisPublicPolicy",
                        policy_name= "edb-athena-public-iris",

                        document= _iam.PolicyDocument(
                            statements= [_iam.PolicyStatement(
                                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                effect= _iam.Effect.ALLOW,
                                resources= [f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_public/*"
                                ]
                                ),
                                _iam.PolicyStatement(
                                actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                effect= _iam.Effect.ALLOW,
                                resources= [f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_public"
                                ]
                                )
                            ]
                        ),
                        roles= [rIrisPublicRole]
                    )
            cfn_func = pAthenaIrisPublicPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisPublicPolicy")

        if config.env in ['qa','prod'] :
            rS3IrisConformPublicPolicy = _iam.Policy(
                            self,
                            "rS3IrisConformPublicPolicy",
                            policy_name= "edb-s3-conform-public-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                    f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/cmi_lusa_marketing_interactions/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/hibbert_lusa_marketing_interactions/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/sfmc_lusa_marketing_interactions/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/lilly_mdm/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/lusa_janrain/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/lusa_lilly_play/*'"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/canopy_lusa_campaign_metadata/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iqvia_lusa_sales/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/targeting_lists_iris/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/mmit_lusa_formulary_access/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/veeva_lusa_objects/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/inext_lusa_employee_expenses/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/webmd_lusa_marketing_interactions/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/zs_campaign_metadata/*"
                                    ,f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/zs_verso_recommendations/*"
                                    ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisPublicRole,
                            rIrisEversanaRestrictedRole,
                            rIrisCapgeminiRestrictedRole,
                            rIrisIqviaRestrictedRole,
                            rIrisOpusRestrictedRole,
                            rIrisSymphonyRestrictedRole,
                            rIrisFive9RestrictedRole,
                            rIrisSapScaRestrictedRole,
                            rIrisErxRestrictedRole,
                            rIrisRelayHealthRestrictedRole,
                            rIrisEdiRestrictedRole,
                            rIrisManualFilesRestrictedRole,
                            rIrisCcpaRestrictedRole,
                            rIrisCptRestrictedRole,
                            rIrisTcmRestrictedRole,
                            rIrisJavelinRestrictedRole,
                            rIrisIncentivesRestrictedRole,
                            rIrisBrgRestrictedRole,
                            rIrisZsFieldInsightsRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisConformPublicPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisConformPublicPolicy")

        # Converted rIrisDBMigrationsPolicy + rIrisPrefectPolicy from inline to
        # a MANAGED policy to avoid the 10,240 byte per-role inline policy limit.
        # Using a managed policy means:
        #   - CFN CREATEs the managed policy (no inline size impact)
        #   - CFN DELETEs old inline rIrisDBMigrationsPolicy & rIrisPrefectPolicy
        #   - No inline policy is ever UPDATED/grown, so no transition size issue
        # rIrisPrefectPolicy statements are absorbed into this managed policy.
        if config.env == 'qa':
            roles_mpIrisDBMigrationsPolicy = [
                rIrisIdsLvaRole,
                rIrisIdsSalesRole,
                rIrisIdsMarketingRole,
                rOperationRole
            ]
        elif config.env == 'prod':
            roles_mpIrisDBMigrationsPolicy = [rOperationRole]
        else:
            roles_mpIrisDBMigrationsPolicy = [rOperationRole, rDeveloperRole]
        mpIrisDBMigrationsPolicy = _iam.ManagedPolicy(
                            self,
                            "mpIrisDBMigrationsPolicy",
                            managed_policy_name= f"iris-dbmigrations-{config.env}-policy",
                            document= _iam.PolicyDocument(
                                statements= [
                                # DynamoDB list (shared by both original policies)
                                _iam.PolicyStatement(
                                    actions=[ "dynamodb:List*"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= ["*"]
                                    ),
                                # DynamoDB table-level access (merged tables from both policies)
                                _iam.PolicyStatement(
                                    actions=[   "dynamodb:BatchGetItem",
                                                "dynamodb:BatchWriteItem",
                                                "dynamodb:Get*",
                                                "dynamodb:Scan",
                                                "dynamodb:Query",
                                                "dynamodb:Describe*",
                                                "dynamodb:DeleteTable",
                                                "dynamodb:DeleteItem",
                                                "dynamodb:PartiQLSelect"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:dynamodb:{config.deploy_env.region}:{config.deploy_env.account}:table/iris-redshift-log",
                                         f"arn:aws:dynamodb:{config.deploy_env.region}:{config.deploy_env.account}:table/iris-redshift-log-*",
                                         f"arn:aws:dynamodb:{config.deploy_env.region}:{config.deploy_env.account}:table/prefect_flow_deploy_config"
                                    ]
                                    ),
                                # KMS for DynamoDB (from original rIrisDBMigrationsPolicy)
                                _iam.PolicyStatement(
                                    actions=[  
                                        "kms:Decrypt",
                                        "kms:GenerateDataKey"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisDynDBKmsKey']}"
                                    ]
                                    ),
                                # Step Functions (from original rIrisDBMigrationsPolicy)
                                _iam.PolicyStatement(
                                    actions=[   
                                        "states:List*",
                                        "states:Describe*",
                                        "states:StartExecution",
                                        "states:StopExecution",
                                        "states:UpdateStateMachine",
                                        "states:DeleteStateMachine"
                                        ],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_db_migrations_pr_*",
                                         f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_db_migrations_pr_*"
                                    ]
                                    ),
                                # Lambda invoke (from original rIrisPrefectPolicy)
                                _iam.PolicyStatement(
                                    actions=[   
                                        "lambda:InvokeFunction",
                                        "lambda:InvokeAsync"
                                        ],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:Prefect*"
                                    ]
                                    ),
                                # ACM (from original rIrisPrefectPolicy)
                                _iam.PolicyStatement(
                                    actions=[  
                                        "acm:DescribeCertificate",
                                        "acm:ListCertificates",
                                        "acm:GetCertificate",
                                        "acm:ListTagsForCertificate",
                                        "acm:GetAccountConfiguration",
                                        "acm:ImportCertificate",
                                        "acm:AddTagsToCertificate"
                                        ],
                                    effect= _iam.Effect.ALLOW,
                                    resources= ["arn:aws:acm:us-east-2:346644684160:certificate/96d9030f-a281-4092-b5cc-8492cb5849a3"]
                                    )
                                ]
                            ),
                            roles= roles_mpIrisDBMigrationsPolicy
                        )
        cfn_func = mpIrisDBMigrationsPolicy.node.default_child
        cfn_func.override_logical_id("mpIrisDBMigrationsPolicy")

        if config.env in ['qa','prod']:
            role_pFlexIrisManualExtractsPolicy = [rOperationRole, rServiceRole]
        else :
            role_pFlexIrisManualExtractsPolicy = [rDeveloperRole, rServiceRole]
        pFlexIrisManualExtractsPolicy = _iam.Policy(
                            self,
                            "pFlexIrisManualExtractsPolicy",
                            policy_name= "edb-iris-flex-manual-extracts-ex",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=[ 
                                        "s3:PutObject",
                                        "s3:GetObject",
                                        "s3:GetObjectVersion",
                                        "s3:DeleteObject",
                                        "s3:DeleteObjectVersion",
                                        "s3:ListBucket",
                                        "s3:ListBucketMultipartUploads",
                                        "s3:RestoreObject"
                                        ],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/flex_lusa_iris_data_extracts_restricted/*"]
                                    )
                                ]
                            ),
                            roles= role_pFlexIrisManualExtractsPolicy
                        )
        cfn_func = pFlexIrisManualExtractsPolicy.node.default_child
        cfn_func.override_logical_id("pFlexIrisManualExtractsPolicy")

        if config.env in ['qa','prod']:
            role_pBrgMedicaidPolicy = [rOperationRole, rServiceRole,rBRGServiceRole,rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole]
        else :
            role_pBrgMedicaidPolicy = [rDeveloperRole, rServiceRole,rBRGServiceRole,rEHRPiServiceRole,rLvaSplunkObservabilityRole,rLvaSplunkObservabilityOmmRole,rLvaSplunkPACEObservabilityRole]
        pBrgMedicaidPolicy = _iam.Policy(
                            self,
                            "pBrgMedicaidPolicy",
                            policy_name= "edb-iris-brg-medicaid-ex",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=[
                                        "s3:PutObject",
                                        "s3:GetObject",
                                        "s3:GetObjectVersion",
                                        "s3:DeleteObject",
                                        "s3:DeleteObjectVersion",
                                        "s3:ListBucket",
                                        "s3:ListBucketMultipartUploads",
                                        "s3:RestoreObject"
                                        ],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_medicaid_lusa_iris_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_medicaid_lusa_iris_restricted/*",
                                         ]
                                    )
                                ]
                            ),
                            roles= role_pBrgMedicaidPolicy
                        )
        cfn_func = pBrgMedicaidPolicy.node.default_child
        cfn_func.override_logical_id("pBrgMedicaidPolicy")

        if config.env in ['qa','prod']:
            rS3IrisCcpaPolicy = _iam.Policy(
                            self,
                            "rS3IrisCcpaPolicy",
                            policy_name="edb-s3-ccpa-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris_lusa_ccpa_restricted/*",
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisCcpaRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisCcpaPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisCcpaPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisCcpaPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisCcpaPolicy",
                            policy_name= "edb-athena-ccpa-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_lusa_ccpa_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_ccpa_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisCcpaRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisCcpaPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisCcpaPolicy")

        if config.env in ['qa','prod']:
            rS3IrisEversanaPolicy = _iam.Policy(
                            self,
                            "rS3IrisEversanaPolicy",
                            policy_name= "edb-s3-eversana-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/eversana_lusa_copay_restricted/*",
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisEversanaRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisEversanaPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisEversanaPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisEversanaPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisEversanaPolicy",
                            policy_name= "edb-athena-eversana-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/eversana_lusa_copay_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_eversana_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisEversanaRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisEversanaPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisEversanaPolicy")

        if config.env in ['qa','prod']:
            rS3IrisCapgeminiPolicy = _iam.Policy(
                            self,
                            "rS3IrisCapgeminiPolicy",
                            policy_name= "edb-s3-capgemini-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/capgemini_lusa_specialty_metrics_restricted/*",
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisCapgeminiRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisCapgeminiPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisCapgeminiPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisCapgeminiPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisCapgeminiPolicy",
                            policy_name= "edb-athena-capgemini-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/capgemini_lusa_specialty_metrics_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_capgemini_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisCapgeminiRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisCapgeminiPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisCapgeminiPolicy")

        if config.env in ['qa','prod']:
            rS3IrisIqviaPolicy = _iam.Policy(
                            self,
                            "rS3IrisIqviaPolicy",
                            policy_name= "edb-s3-iqvia-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iqvia_lusa_sales_restricted/*",
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisIqviaRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisIqviaPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisIqviaPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisIqviaPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisIqviaPolicy",
                            policy_name= "edb-athena-iqvia-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iqvia_lusa_sales_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_iqvia_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisIqviaRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisIqviaPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisIqviaPolicy")

        if config.env in ['qa','prod']:
            rS3IrisJavelinPolicy = _iam.Policy(
                            self,
                            "rS3IrisJavelinPolicy",
                            policy_name= "edb-s3-javelin-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/dataspine_lusa_javelin_restricted/*",
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisJavelinRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisJavelinPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisJavelinPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisJavelinPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisJavelinPolicy",
                            policy_name= "edb-athena-javelin-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/dataspine_lusa_javelin_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_javelin_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisJavelinRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisJavelinPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisJavelinPolicy")

        if config.env in ['qa','prod']:
            rS3IrisIncentivesPolicy = _iam.Policy(
                            self,
                            "rS3IrisIncentivesPolicy",
                            policy_name= "edb-s3-incentives-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/incentives_lusa_extracts_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisIncentivesRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisIncentivesPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisIncentivesPolicy")

        if config.env in ['qa', 'prod']:
            rS3IrisZsFieldInsightsPolicy = _iam.Policy(
                            self,
                            "rS3IrisZsFieldInsightsPolicy",
                            policy_name=  "edb-s3-zs-field-insights-ex-iris",
                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*",
                                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*",
                                        f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/zs_lusa_field_insights_restricted/*"
                                    ]
                                    )
                                ]
                            ),
                            roles=[rIrisZsFieldInsightsRestrictedRole]
                        )
            cfn_func = rS3IrisZsFieldInsightsPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisZsFieldInsightsPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisIncentivesPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisIncentivesPolicy",
                            policy_name= "edb-athena-incentives-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/incentives_lusa_extracts_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_incentives_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisIncentivesRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisIncentivesPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisIncentivesPolicy")

        if config.env in ['qa','prod']:
            rS3IrisOpusPolicy = _iam.Policy(
                            self,
                            "rS3IrisOpusPolicy",
                            policy_name= "edb-s3-opus-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/opus_lusa_copay_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisOpusRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisOpusPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisOpusPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisOpusPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisOpusPolicy",
                            policy_name= "edb-athena-opus-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/opus_lusa_copay_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_opus_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisOpusRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisOpusPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisOpusPolicy")

        if config.env in ['qa','prod']:
            rS3IrisSymphonyPolicy = _iam.Policy(
                            self,
                            "rS3IrisSymphonyPolicy",
                            policy_name= "edb-s3-symphony-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/symphony_lusa_sales_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisSymphonyRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisSymphonyPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisSymphonyPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisSymphonyPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisSymphonyPolicy",
                            policy_name= "edb-athena-symphony-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/symphony_lusa_sales_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_symphony_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisSymphonyRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisSymphonyPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisSymphonyPolicy")

        if config.env in ['qa','prod']:
            rS3IrisFive9Policy = _iam.Policy(
                            self,
                            "rS3IrisFive9Policy",
                            policy_name= "edb-s3-five9-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/five9_lusa_call_metrics_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisFive9RestrictedRole
                                ]
                        )
            cfn_func = rS3IrisFive9Policy.node.default_child
            cfn_func.override_logical_id("rS3IrisFive9Policy")

        if config.env in ['qa','prod']:
            pAthenaIrisFive9Policy = _iam.Policy(
                            self,
                            "pAthenaIrisFive9Policy",
                            policy_name= "edb-athena-five9-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/five9_lusa_call_metrics_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_five9_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisFive9RestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisFive9Policy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisFive9Policy")

        if config.env in ['qa','prod']:
            rS3IrisSapScaPolicy = _iam.Policy(
                            self,
                            "rS3IrisSapScaPolicy",
                            policy_name= "edb-s3-sapsca-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/sap_lusa_supply_chain_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisSapScaRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisSapScaPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisSapScaPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisSapPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisSapPolicy",
                            policy_name= "edb-athena-sap-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/sap_lusa_supply_chain_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_sap_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisSapScaRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisSapPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisSapPolicy")

        if config.env in ['qa','prod']:
            rS3IrisErxPolicy = _iam.Policy(
                            self,
                            "rS3IrisErxPolicy",
                            policy_name= "edb-s3-erx-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/erx_lusa_copay_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisErxRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisErxPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisErxPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisErxPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisErxPolicy",
                            policy_name= "edb-athena-erx-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/erx_lusa_copay_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_erx_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisErxRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisErxPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisErxPolicy")

        if config.env in ['qa','prod']:
            rS3IrisRelayHealthPolicy = _iam.Policy(
                            self,
                            "rS3IrisRelayHealthPolicy",
                            policy_name= "edb-s3-relayhealth-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/relayhealth_lusa_copay_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisRelayHealthRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisRelayHealthPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisRelayHealthPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisRelayHealthPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisRelayHealthPolicy",
                            policy_name= "edb-athena-relayhealth-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/relayhealth_lusa_copay_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_relayhealth_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                                rIrisRelayHealthRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisRelayHealthPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisRelayHealthPolicy")

        if config.env in ['qa','prod']:
            rS3IrisEdiPolicy = _iam.Policy(
                            self,
                            "rS3IrisEdiPolicy",
                            policy_name= "edb-s3-edi-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisEdiRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisEdiPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisEdiPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisEdiPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisEdiPolicy",
                            policy_name= "edb-athena-edi-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/edi_lusa_supply_chain_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_edi_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisEdiRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisEdiPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisEdiPolicy")

        if config.env in ['qa','prod']:
            rS3IrisBrgPolicy = _iam.Policy(
                            self,
                            "rS3IrisBrgPolicy",
                            policy_name= "edb-s3-brg-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*",
                                         f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*",
                                         f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/flex_lusa_iris_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisBrgRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisBrgPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisBrgPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisBrgPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisBrgPolicy",
                            policy_name= "edb-athena-brg-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/brg_lusa_iris_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_brg_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisBrgRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisBrgPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisBrgPolicy")

        rS3IrisTurboUsersReadPolicy = _iam.Policy(
                            self,
                            "rS3IrisTurboUsersReadPolicy",
                            policy_name= "edb-s3-turbo-users-ex-ro-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=["s3:List*"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=["s3:List*",
                                             "s3:Get*"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/turbo_lusa_dataextracts_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisTurboUsersRestrictedRole,
                            rServiceRole,
                            rOperationRole
                                ]
                        )
        cfn_func = rS3IrisTurboUsersReadPolicy.node.default_child
        cfn_func.override_logical_id("rS3IrisTurboUsersReadPolicy")

        rS3IrisTurboUsersWriteDeletePolicy = _iam.Policy(
                            self,
                            "rS3IrisTurboUsersWriteDeletePolicy",
                            policy_name= "edb-s3-turbo-users-ex-rw-iris",

                            document= _iam.PolicyDocument(
                                statements= [
                                    _iam.PolicyStatement(
                                    actions=["s3:PutObject*",
                                             "s3:DeleteObject",
                                             "s3:DeleteObjectVersion",
                                             ],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/turbo_lusa_dataextracts_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rServiceRole,
                            rOperationRole
                                ]
                        )
        cfn_func = rS3IrisTurboUsersWriteDeletePolicy.node.default_child
        cfn_func.override_logical_id("rS3IrisTurboUsersWriteDeletePolicy")

        if config.env in ['qa','prod']:
            rAthenaIrisTurboUsersPolicy = _iam.Policy(
                            self,
                            "rAthenaIrisTurboUsersPolicy",
                            policy_name= "edb-athena-turbo-users-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/turbo_lusa_dataextracts_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_turbo_users_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisTurboUsersRestrictedRole
                                ]
                        )
            cfn_func = rAthenaIrisTurboUsersPolicy.node.default_child
            cfn_func.override_logical_id("rAthenaIrisTurboUsersPolicy")


        if config.env in ['qa','prod']:
            rS3IrisManualFilesPolicy = _iam.Policy(
                            self,
                            "rS3IrisManualFilesPolicy",
                            policy_name="edb-s3-manual-files-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/iris_lusa_manual_files_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisManualFilesRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisManualFilesPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisManualFilesPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisManualFilesPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisManualFilesPolicy",
                            policy_name= "edb-athena-manual-files-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/iris_lusa_manual_files_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_manual_files_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisManualFilesRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisManualFilesPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisManualFilesPolicy")

        if config.env in ['qa','prod']:
            rS3IrisCptPolicy = _iam.Policy(
                            self,
                            "rS3IrisCptPolicy",
                            policy_name="edb-s3-cpt-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/capgemini_lusa_tokenized_patient_data_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisCptRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisCptPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisCptPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisCptPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisCptPolicy",
                            policy_name= "edb-athena-cpt-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/capgemini_lusa_tokenized_patient_data_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_cpt_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisCptRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisCptPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisCptPolicy")

        Iris_engin_iam_role_OIDC = _iam.Role.from_role_name(
            self,
             "Iris_engin_iam_role_OIDC",
             role_name=  "iris-engine-IAMRoleForGithubOIDC"
        )
        rIrisEngineGitHubOIDCRolePermissions = _iam.Policy(
            self,
            "rIrisEngineGitHubOIDCRolePermissions",
            policy_name="edb-iris-engine-oidc-role-permissions",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[   "lambda:PublishLayerVersion",
                                "lambda:UpdateFunctionConfiguration",
                                "lambda:GetLayerVersion",
                                "lambda:ListLayerVersions"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:layer:PrefectDependencies*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:PrefectLambda"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:Prefects3EventLambda"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:layer:DqaDependencies*"
                        ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:layer:edb_iris_*"
                    ]
                    )
                ]
            ),
            roles= [Iris_engin_iam_role_OIDC ]
        )
        cfn_func = rIrisEngineGitHubOIDCRolePermissions.node.default_child
        cfn_func.override_logical_id("rIrisEngineGitHubOIDCRolePermissions")
        
        if config.env in ['qa','prod']:
            rS3IrisTcmPolicy = _iam.Policy(
                            self,
                            "rS3IrisTcmPolicy",
                            policy_name="edb-s3-tcm-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*",
                                         f"arn:aws:s3:::lly-edp-conform-{params['pBucketPrefix']}/total_contract_manager_lusa_contracts_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisTcmRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisTcmPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisTcmPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisTcmPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisTcmPolicy",
                            policy_name= "edb-athena-tcm-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/total_contract_manager_lusa_contracts_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_tcm_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisTcmRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisTcmPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisTcmPolicy")

        if config.env in ['qa','prod']:
            rS3IrisMTMPolicy = _iam.Policy(
                            self,
                            "rS3IrisMTMPolicy",
                            policy_name="edb-s3-mtm-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/mtm_lusa_product_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/mtm_lusa_product_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisMtmRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisMTMPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisMTMPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisMtmPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisMtmPolicy",
                            policy_name= "edb-athena-mtm-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/mtm_lusa_product_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_mtm_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisMtmRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisMtmPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisMtmPolicy")

        iris_eng_IAM_ROLE_CICD = _iam.Role.from_role_name(
            self ,
            "iris_eng_IAM_ROLE_CICD",
            role_name= "iris-engine-IAMRoleForCodePipeline"
        )
        statemachinePolicyForCodePipelineRole = _iam.Policy(
                            self,
                            "statemachinePolicyForCodePipelineRole",
                            policy_name=  "codepipeline-inline-role-statemachine",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=[  "states:List*",
                                "states:Describe*",
                                "states:StartExecution"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris*",
                                         f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:omnisource*",
                                         f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris*",
                                         f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:omnisource*",
                                         ]
                                    )
                                ]
                            ),
                            roles= [iris_eng_IAM_ROLE_CICD ]
                        )
        cfn_func = statemachinePolicyForCodePipelineRole.node.default_child
        cfn_func.override_logical_id("statemachinePolicyForCodePipelineRole")

        if config.env in ['qa','prod']:
            rS3IrisAdsPolicy = _iam.Policy(
                            self,
                            "rS3IrisAdsPolicy",
                            policy_name="edb-s3-ads-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ads_lusa_alignment_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisAdsRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisAdsPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisAdsPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisAdsPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisAdsPolicy",
                            policy_name= "edb-athena-ads-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/ads_lusa_alignment_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_ads_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisAdsRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisAdsPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisAdsPolicy")

        if config.env in ['qa','prod']:
            rS3IrisActPolicy = _iam.Policy(
                            self,
                            "rS3IrisActPolicy",
                            policy_name="edb-s3-act-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/act_lusa_activity_restricted/*",
                                         f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/act_lusa_activity_restricted/*"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisActRestrictedRole
                                ]
                        )
            cfn_func = rS3IrisActPolicy.node.default_child
            cfn_func.override_logical_id("rS3IrisActPolicy")

        if config.env in ['qa','prod']:
            pAthenaIrisActPolicy = _iam.Policy(
                            self,
                            "pAthenaIrisActPolicy",
                            policy_name= "edb-athena-act-ex-iris",

                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['s3athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:s3:::lly-edp-athena-results-{params['pBucketPrefix']}/iris/act_lusa_activity_restricted/*"
                                         ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['athena'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:athena:us-east-2:{config.deploy_env.account}:workgroup/edb_iris_act_ex"
                                         ]
                                    )
                                ]
                            ),
                            roles= [
                            rIrisActRestrictedRole
                                ]
                        )
            cfn_func = pAthenaIrisActPolicy.node.default_child
            cfn_func.override_logical_id("pAthenaIrisActPolicy")

        rBrgHashingBinaryPolicy = _iam.Policy(
                            self,
                            "rBrgHashingBinaryPolicy",
                            policy_name= "iris-brg-hashing-binary-policy",
                            document= _iam.PolicyDocument(
                                statements= [_iam.PolicyStatement(
                                    actions=[  "ecr:BatchCheckLayerAvailability",
                                                "ecr:GetDownloadUrlForLayer",
                                                "ecr:BatchGetImage",
                                                "logs:PutLogEvents"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                         f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/ecs/edb-iris*:log-stream:edb-iris*",
                                         f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb_iris*",
                                         f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/edb-iris*",
                                         f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/iris-*",
                                         f"arn:aws:ecr:{config.deploy_env.region}:{config.deploy_env.account}:repository/pipeline-iris-core*"
                                    ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=[  "ecr:GetAuthorizationToken",
                                            "s3:ListAllMyBuckets",
                                            "ec2:CreateNetworkInterface",
                                            "ec2:DeleteNetworkInterface",
                                            "ec2:DescribeNetworkInterfaces",
                                            "kms:ListKeys",
                                            "kms:ListAliases"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= ["*"]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=[ "logs:CreateLogGroup",
                                                "logs:CreateLogStream"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/ecs/edb-iris*"]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=[ "s3:List*"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}",
                                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}",
                                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}",
                                        f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}",
                                        f"arn:aws:s3:::{params['ArtifactBucket']}",
                                        f"arn:aws:s3:::{params['ArtifactEdbBucket']}"
                                        ]
                                    ),
                                     _iam.PolicyStatement(
                                    actions=[ "s3:PutObject",
                                            "s3:GetObject",
                                            "s3:DeleteObject",
                                            "s3:DeleteObjectVersion",
                                            "s3:RestoreObject",
                                            "s3:PutObjectVersionTagging",
                                            "s3:GetObjectAcl",
                                            "s3:GetObjectVersionAcl",
                                            "s3:GetObjectTagging",
                                            "s3:PutObjectTagging",
                                            "s3:GetObjectVersion"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                       f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/brg_lusa_iris_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/flex_lusa_iris_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-departure-{params['pBucketPrefix']}/flex_lusa_iris_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/edi_lusa_supply_chain_restricted/*" # RITM3346617
                                        ,f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/*"
                                        ,f"arn:aws:s3:::{params['ArtifactBucket']}/aws_glue/*"
                                        ,f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws_glue/*"
                                        ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=[ "kms:Decrypt",
                                            "kms:Encrypt",
                                            "kms:DescribeKey",
                                            "kms:GenerateDataKey*",
                                            "kms:ReEncrypt*"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}"
                                        ]
                                    ),
                                     _iam.PolicyStatement(
                                    actions=[   "lambda:GetFunctionConfiguration"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_brg_invoke_hashing_binary"
                                        ]
                                    ),
                                     _iam.PolicyStatement(
                                    actions=[    "ecs:RunTask"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:ecs:{config.deploy_env.region}:{config.deploy_env.account}:task-definition/edb-iris-hashing-binary"
                                        ]
                                    ),
                                     _iam.PolicyStatement(
                                    actions=[      "iam:PassRole"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:iam::{config.deploy_env.account}:role/edb_buids_iris_brg_service_role"
                                        ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=[  "ecs:DescribeTasks"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:ecs:{config.deploy_env.region}:{config.deploy_env.account}:task/edb-iris*"
                                        ]
                                    ),
                                    _iam.PolicyStatement(
                                    actions=config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['states'],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:stateMachine:edb_iris_brg*",
                                        f"arn:aws:states:{config.deploy_env.region}:{config.deploy_env.account}:execution:edb_iris_brg*"
                                        ]
                                    ),
                                     _iam.PolicyStatement(
                                    actions=[   "events:PutTargets",
                                                "events:PutRule",
                                                "events:DescribeRule"],
                                    effect= _iam.Effect.ALLOW,
                                    resources= [
                                        f"arn:aws:events:{config.deploy_env.region}:{config.deploy_env.account}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
                                        ]
                                    )
                                ]
                            ),
                            roles=[rBRGServiceRole]
                        )
        cfn_func = rBrgHashingBinaryPolicy.node.default_child
        cfn_func.override_logical_id("rBrgHashingBinaryPolicy")


############################### Security Groups ###############################

        rIrisMDMSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisMDMSecurityGroup",
            description = "MDM Security Group",
            vpc= vpc
        )
        _tag.of(rIrisMDMSecurityGroup).add("Restricted","Restricted")

        cfn_func = rIrisMDMSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisMDMSecurityGroup")
        
        rIrisAuroraDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisAuroraDbSecurityGroup",
            description = "Aurora Consolidated Security Group",
            vpc= vpc
        )
        cfn_func = rIrisAuroraDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisAuroraDbSecurityGroup")

        rIrisMDMSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
                self, "rIrisMDMSecurityGroupIngress",
                ip_protocol="tcp",
                from_port = 5430,
                to_port = 5440,
                description= "MdmSecurityGroupIngress",
                source_prefix_list_id = params['pLillyOwnedIPplID'],
                group_id= rIrisAuroraDbSecurityGroup.security_group_id,
                source_security_group_id = rIrisMDMSecurityGroup.security_group_id
            )

        if config.env in ['qa','prod']:
            rIrisAuroraJumpSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
                self, "rIrisAuroraJumpSecurityGroupIngress",
                ip_protocol="tcp",
                from_port = 5430,
                to_port = 5440,
                description= "Iris Jump Server Access",
                group_id= rIrisAuroraDbSecurityGroup.security_group_id,
                source_security_group_id = params['pIrisJumpSGId']
            )


        rIrisLashDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisLashDbSecurityGroup",
            description = "Lash Security Group",
            vpc= vpc
        )
        cfn_func = rIrisLashDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisLashDbSecurityGroup")

        rIrisDTGlueSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisDTGlueSecurityGroup",
            description = "Allow EDB taffic from glue to oracle",
            security_group_name= "dt-iris-glue-sg-group",
            vpc= vpc
        )
        cfn_func = rIrisDTGlueSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisDTGlueSecurityGroup")

        rIrisDTGlueConnectionSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisDTGlueConnectionSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 0,
            to_port = 65535,
            description= "Self Referential security group for Glue",
            group_id= rIrisDTGlueSecurityGroup.security_group_id,
            source_security_group_id= rIrisDTGlueSecurityGroup.security_group_id
            )

        rIrisLashSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisLashSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 5430,
            to_port = 5440,
            description= "lash security group ingress",
            group_id= rIrisAuroraDbSecurityGroup.security_group_id,
            source_security_group_id= rIrisLashDbSecurityGroup.security_group_id
        )

        rIrisDHCDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisDHCDbSecurityGroup",
            description = "DHC Security Group",
            vpc= vpc
        )
        _tag.of(rIrisDHCDbSecurityGroup).add("Restricted","Restricted")
        cfn_func = rIrisDHCDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisDHCDbSecurityGroup")

        rIrisDHCSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisDHCSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 5430,
            to_port = 5440,
            description= "DHC security group ingress",
            group_id= rIrisAuroraDbSecurityGroup.security_group_id,
            source_security_group_id= rIrisDHCDbSecurityGroup.security_group_id
            )
            
        rIrisSonexusCRMDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisSonexusCRMDbSecurityGroup",
            description = "SonexusCRM Security Group",
            vpc= vpc
        )
        cfn_func = rIrisSonexusCRMDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisSonexusCRMDbSecurityGroup")
        
        rIrisSonexusCRMSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisSonexusCRMSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 5430,
            to_port = 5440,
            description= "SonexusCRM security group ingress",
            group_id= rIrisAuroraDbSecurityGroup.security_group_id,
            source_security_group_id= rIrisSonexusCRMDbSecurityGroup.security_group_id
        )

        rIrisIqviaclaimsDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisIqviaclaimsDbSecurityGroup",
            description = "Iqviaclaims Security Group",
            vpc= vpc
        )
        cfn_func = rIrisIqviaclaimsDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisIqviaclaimsDbSecurityGroup")

        rIrisIqviaclaimsSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisIqviaclaimsSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 5430,
            to_port = 5440,
            description= "Iqviaclaims security group ingress",
            group_id= rIrisAuroraDbSecurityGroup.security_group_id,
            source_security_group_id= rIrisIqviaclaimsDbSecurityGroup.security_group_id
        )
        
        rIrisEversanaCRMDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisEversanaCRMDbSecurityGroup",
            description = "EversanaCRM Security Group",
            vpc= vpc
        )
        cfn_func = rIrisEversanaCRMDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisEversanaCRMDbSecurityGroup")
        
        rIrisEversanaCRMSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisEversanaCRMSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 5430,
            to_port = 5440,
            description= "EversanaCRM security group ingress",
            group_id= rIrisAuroraDbSecurityGroup.security_group_id,
            source_security_group_id= rIrisEversanaCRMDbSecurityGroup.security_group_id
        )
        
        rIrisEversanaDbSecurityGroup = _ec2.SecurityGroup(
            self, "rIrisEversanaDbSecurityGroup",
            description = "Eversana Security Group",
            vpc= vpc
        )
        cfn_func = rIrisEversanaDbSecurityGroup.node.default_child
        cfn_func.override_logical_id("rIrisEversanaDbSecurityGroup")
        
        rIrisEversanaSecurityGroupIngress = _ec2.CfnSecurityGroupIngress(
            self, "rIrisEversanaSecurityGroupIngress",
            ip_protocol="tcp",
            from_port = 5430,
            to_port = 5440,
            description= "Eversana security group ingress",
            group_id= rIrisAuroraDbSecurityGroup.security_group_id,
            source_security_group_id= rIrisEversanaDbSecurityGroup.security_group_id
        )


############################# OUTPUTS       ##########################
        BASServiceRoleName = CfnOutput(
            self ,
            "BASServiceRoleName",
            description= "BAS Service Role Name",
            value = rBASServiceRole.role_name,
            export_name= "BAS-Service-Role-Name"
        )

        BRMSServiceRoleName = CfnOutput(
            self ,
            "BRMSServiceRoleName",
            description= "BRMS Service Role Name",
            value = rBRMSServiceRole.role_name,
            export_name= "BRMS-Service-Role-Name"
        )

        LMServiceRoleName = CfnOutput(
            self ,
            "LMServiceRoleName",
            description= "LM Service Role Name",
            value = rLMServiceRole.role_name,
            export_name= "LM-Service-Role-Name"
        )

        oDMSIrisKMSKeyAlias = CfnOutput(
            self ,
            "oDMSIrisKMSKeyAlias",
            description=  "IRIS Specific KMS Key for DMS",
            value = DMSIrisKMSKeyAlias.alias_name,
            export_name= "DMS-Iris-KMS-Key-Alias"
        )

        rIrisLashDbSecurityGroupId = CfnOutput(
            self ,
            "rIrisLashDbSecurityGroupId",
            description= "Lash security group",
            value = rIrisLashDbSecurityGroup.security_group_id,
            export_name= "Lash-Csp-Security-Group-Id"
        )

        rIrisDHCDbSecurityGroupId = CfnOutput(
            self ,
            "rIrisDHCDbSecurityGroupId",
            description= "DHC security group",
            value = rIrisDHCDbSecurityGroup.security_group_id,
            export_name= "DHC-Csp-Security-Group-Id"
        )
        
        rIrisSonexusCRMDbSecurityGroupId = CfnOutput(
            self ,
            "rIrisSonexusCRMDbSecurityGroupId",
            description= "SonexusCRM security group",
            value = rIrisSonexusCRMDbSecurityGroup.security_group_id,
            export_name= "SonexusCRM-Csp-Security-Group-Id"
        )

        rIrisIqviaclaimsDbSecurityGroupId = CfnOutput(
            self ,
            "rIrisIqviaclaimsDbSecurityGroupId",
            description= "Iqviaclaims security group",
            value = rIrisIqviaclaimsDbSecurityGroup.security_group_id,
            export_name= "Iqviaclaims-Csp-Security-Group-Id"
        )
        
        rIrisEversanaCRMDbSecurityGroupId = CfnOutput(
            self ,
            "rIrisEversanaCRMDbSecurityGroupId",
            description= "EversanaCRM security group",
            value = rIrisEversanaCRMDbSecurityGroup.security_group_id,
            export_name= "EversanaCRM-Csp-Security-Group-Id"
        )
        
        rIrisEversanaDbSecurityGroupId = CfnOutput(
            self ,
            "rIrisEversanaDbSecurityGroupId",
            description= "Eversana security group",
            value = rIrisEversanaDbSecurityGroup.security_group_id,
            export_name= "Eversana-Csp-Security-Group-Id"
        )

        OrIrisDTGlueSecurityGroup = CfnOutput(
            self ,
            "OrIrisDTGlueSecurityGroup",
            description= "Dynamic Targeting security group",
            value = rIrisDTGlueSecurityGroup.security_group_id,
            export_name= "DT-Security-Group-Id"
        )

        IrisMDMSecurityGroupId = CfnOutput(
            self ,
            "IrisMDMSecurityGroupId",
            description= "MDM security group",
            value = rIrisMDMSecurityGroup.security_group_id,
            export_name= "MDM-Security-Group-Id"
        )

        #ddw_service_role_lambda_policy

        mpDDWLambdaPolicy =  _iam.ManagedPolicy(
            self,
            "mpDDWLambdaPolicy",
            managed_policy_name= "ddw-managed-policy-lambda",
            description= "IRIS DDW policy for Lambda",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions= config.legacy_security_stack_mapping['mEnvSpecificAccess'][config.env]['lambda'],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris*"]
                    ),
		_iam.PolicyStatement(
                actions= ["lambda:InvokeAsync","lambda:InvokeFunction","lambda:Update*"],
                effect= _iam.Effect.ALLOW,
                resources= [f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_ddw_*"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_ddrft_*"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_inc_snow*"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_abc*"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_raw_s3_processRawFile"
                                ,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_monitoring_metric_publish"
				,f"arn:aws:lambda:{config.deploy_env.region}:{config.deploy_env.account}:function:edb_iris_*"
                                ]
                ),
                _iam.PolicyStatement(
                    actions= [  "logs:CreateLogStream",
                                "logs:CreateLogGroup",
                                "logs:AssociateKmsKey",
                                "logs:PutLogEvents",
                                "logs:Describe*",
                                "logs:FilterLogEvents",
                                "logs:Get*",
                                "logs:List*"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_ddw_*"
				,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_ddrft_*"
				,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_raw_s3_processRawFile"
				,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws/lambda/edb_iris_*"
                                ,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:edb_iris_ddw_*"
			        ,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:edb_iris_ddrft_*"
			        ,f"arn:aws:logs:{config.deploy_env.region}:{config.deploy_env.account}:log-group:/aws-glue/jobs/output:edb_iris_*"]
                )
                ]
            )
        )
        cfn_func = mpDDWLambdaPolicy.node.default_child
        cfn_func.override_logical_id("mpDDWLambdaPolicy")

        #ddw_service_role_s3_landing_policy

        mpEdbIrisDdwS3AdminLandingPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisDdwS3AdminLandingPolicy",
            managed_policy_name=  "edb-iris-ddw-s3-admin-landing",
            description=  "EDB IRIS DDW admin policy S3 landing bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                            f"arn:aws:s3:::{params['ArtifactBucket']}/lusa-iris-aws-core/*",
                            f"arn:aws:s3:::{params['ArtifactBucket']}/aws_glue/*/edb-iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/lambda/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws-glue/edb_iris*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws_glue/*/edb-iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/edb/iris/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/aws/*",
                            f"arn:aws:s3:::{params['ArtifactEdbBucket']}/redshift/iris-edb*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/iris/*",
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/esi_optum_prime_zinc_caremark_cmm_humana/*", #RITM3610484
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Regional_Payer/*", #RITM3594897
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Caremark/*", #RITM5505542
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/carevalue_pap_business_files/*", #RITM3594897
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ESI_Enrollment/*", #RITM5505542
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/ESI_Portal/*", #RITM5505542
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Optum/*", #RITM5505542
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/emisar/*", #RITM5505542
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*", #RITM3594897
                            f"arn:aws:s3:::lly-edp-landing-{params['pBucketPrefix']}/Humana/*" #RITM5505542
                            ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisDdwS3AdminLandingPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisDdwS3AdminLandingPolicy")

        #ddw_service_role_s3_raw_policy

        mpEdbIrisDdwS3AdminRawPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisDdwS3AdminRawPolicy",
            managed_policy_name= "edb-iris-ddw-s3-admin-raw",
            description= "EDB IRIS DDW admin policy S3 raw bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/iris/*",
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/esi_optum_prime_zinc_caremark_cmm_humana/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ESI_Enrollment/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/ESI_Portal/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Optum/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/emisar/*", #RITM4031525
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Zinc/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Caremark/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Humana/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Regional_Payer/*", #RITM3594897
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/carevalue_pap_business_files/*", #RITM3594897
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*", #RITM3594897
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/deal_development_common_business_files/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-raw-{params['pBucketPrefix']}/deal_development_common_business_files_restricted/*" #RITM4775981

                         ])
                ]
            )
        )
        cfn_func = mpEdbIrisDdwS3AdminRawPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisDdwS3AdminRawPolicy")

        #ddw_service_role_s3_refined_policy

        mpEdbIrisDdwS3AdminRefinedPolicy = _iam.ManagedPolicy(
            self,
            "mpEdbIrisDdwS3AdminRefinedPolicy",
            managed_policy_name= "edb-iris-ddw-s3-admin-refined",
            description= "EDB IRIS DDW admin policy S3 refined bucket",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "s3:PutObject",
                              "s3:GetObject",
                              "s3:DeleteObject",
                              "s3:DeleteObjectVersion",
                              "s3:ListBucketMultipartUploads",
                              "s3:RestoreObject",
                              "s3:PutObjectVersionTagging",
                              "s3:GetObjectAcl",
                              "s3:GetObjectVersionAcl",
                              "s3:GetObjectTagging",
                              "s3:PutObjectTagging",
                              "s3:GetObjectVersion",
                              "s3:ListBucket"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/iris/*",
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/esi_optum_prime_zinc_caremark_cmm_humana/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ESI_Enrollment/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/ESI_Portal/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Optum/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/emisar/*", #RITM4031525
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Zinc/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Caremark/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Humana/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Regional_Payer/*", #RITM3594897
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/carevalue_pap_business_files/*", #RITM3594897
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/Clinformatics_For_Managed_Markets/*", #RITM3594897
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/deal_development_common_business_files/*", #RITM3610484
                        f"arn:aws:s3:::lly-edp-refined-{params['pBucketPrefix']}/deal_development_common_business_files_restricted/*" #RITM4775981

                         ])
                ]
            )
        )
        cfn_func = mpEdbIrisDdwS3AdminRefinedPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisDdwS3AdminRefinedPolicy")

        #ddw_service_role_secret_policy

        mpEdbIrisDdwSecretsPolicy =  _iam.ManagedPolicy(
            self,
            "mpEdbIrisDdwSecretsPolicy",
            description=  "DDW policy for using secrets manager",
            document= _iam.PolicyDocument(
                statements= [_iam.PolicyStatement(
                    actions=[ "secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret",
                              "secretsmanager:PutSecretValue",
                              "secretsmanager:UpdateSecret",
                              "secretsmanager:RotateSecret",
							  "secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                       f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-SystemUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-bas-SystemUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-user-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsredshift-rsadmin-iris-edb-{params['pEnvironment']}-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-DdwReportingUser-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsRedshift-iris-edb-{params['pEnvironment']}-DdwReportingSecretRotation-??????",
                        f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_snow_api_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_laad_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_laad_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_fcdr_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_rft_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_crossvendor_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_cmm_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_optum_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_caremark_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_esi_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_ddw_humana_report_refresh_secret-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-ddw-snow-reference-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb-iris-ddw-esi-portal-reference-??????",
			f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:edb_iris_maat_rds_secret-??????"
                        ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "secretsmanager:GetSecretValue",
                              "secretsmanager:DescribeSecret"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:secretsmanager:{config.deploy_env.region}:{config.deploy_env.account}:secret:awsedb-auroradb-secrets-??????"]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "kms:Decrypt",
                              "kms:GenerateDataKey"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRdsKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRDSSecretKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMedbKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisSmKmsKey']}",
                        f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisDDWKMSKey']}"
                    ]
                    ),
                    _iam.PolicyStatement(
                    actions=[  "ssm:GetParameter",
                              "ssm:GetParameters",
                              "ssm:GetParametersByPath",
                              "ssm:PutParameter"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [f"arn:aws:ssm:{config.deploy_env.region}:{config.deploy_env.account}:parameter/edb_iris*"]
                    ),
                    _iam.PolicyStatement(
                    actions=[ "s3:DeleteBucketLifecycle",
                              "s3:Get*",
                              "s3:PutBucketLifecycleConfiguration",
                              "s3:PutLifecycleConfiguration",
                              "s3:PutBucketLifecycle"
                            ],
                    effect= _iam.Effect.ALLOW,
                    resources= [
			f"arn:aws:s3:::{params['ArtifactEdbBucket']}"
                        ]
                    )
                ]
            )
        )
        cfn_func = mpEdbIrisDdwSecretsPolicy.node.default_child
        cfn_func.override_logical_id("mpEdbIrisDdwSecretsPolicy")

        rDDWServiceRole = _iam.Role(
                self,
                "rDDWServiceRole",
                role_name= "edb_buids_iris_ddw_service_role",
                permissions_boundary= policy,
                max_session_duration= Duration.seconds(36000),
                assumed_by=_iam.CompositePrincipal(
                _iam.ServicePrincipal("lambda.amazonaws.com"),
                _iam.ServicePrincipal("glue.amazonaws.com"),
                _iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                _iam.ServicePrincipal("events.amazonaws.com"),
                _iam.ServicePrincipal("states.amazonaws.com"),
                _iam.ServicePrincipal("s3.amazonaws.com"),
                _iam.ServicePrincipal("ec2.amazonaws.com"),
                _iam.ServicePrincipal("scheduler.amazonaws.com"),
                _iam.ServicePrincipal("sns.amazonaws.com"),
                _iam.ServicePrincipal("redshift.amazonaws.com"),
                _iam.ServicePrincipal("redshift-data.amazonaws.com"),
                _iam.ServicePrincipal("redshift-serverless.amazonaws.com")
                ),
                managed_policies= [
                    mpEdbIrisGluePolicy,
		            mpDDWLambdaPolicy,
                    mpEdbIrisDdwS3AdminLandingPolicy,
                    mpEdbIrisDdwS3AdminRawPolicy,
                    mpEdbIrisDdwS3AdminRefinedPolicy,
		            mpEdbIrisDdwSecretsPolicy,
					mpEdbIrisRedshiftDataPolicy
                ]
        )
        rDDWServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=["ses:SendEmail","ses:SendRawEmail"],
            effect=_iam.Effect.ALLOW,
                    resources= [
                        "arn:aws:ses:us-east-1:539199905087:identity/lilly.com",
                        f"arn:aws:ses:{config.deploy_env.region}:{config.deploy_env.account}:identity/lilly.com"
                                ],
                    conditions={
                        "StringEquals": {
                            "ses:FromAddress": "aws-notifications-${aws:PrincipalAccount}@lilly.com"
                        },
                        "ForAnyValue:StringLike": {
                            "ses:Recipients": ["*@lilly.com",
                                        "*@*.lilly.com"]
                        }
                    },
            sid="DdwPolicySes"
        ))
        rDDWServiceRole.add_to_policy(_iam.PolicyStatement(
            actions=[ "kms:Decrypt","kms:GenerateDataKey","kms:Encrypt"],
            resources=[
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pKMSKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisKMSKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRdsKmsKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pRDSSecretKmsKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMedbKmsKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pSMIrisKMSKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisSmKmsKey']}",
                f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pIrisDDWKMSKey']}",
				 f"arn:aws:kms:{config.deploy_env.region}:{config.deploy_env.account}:key/{params['pEdbS3KmsKey']}"
				
            ],
            effect=_iam.Effect.ALLOW,
            sid="ddwpolicysecretskms"
        ))

        cfn_func = rDDWServiceRole.node.default_child
        cfn_func.override_logical_id("rDDWServiceRole")
