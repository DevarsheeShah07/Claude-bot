#!/bin/bash
# set -xe

# This runs the pre_build phase of the build.
#
# To run outside CodeBuild, set the following variables before running:
# CODEBUILD_SRC_DIR
#   Set this to your project's root directory.
# CODEBUILD_SRC_DIR_LintRules
#   Set this to the cfn-lint-rules subdirectory in a local git clone of
#   https://github.com/EliLillyCo/CIRR_CloudFormationLintRules
# TEMPLATE_PATH
#   Set this to the path to the template.yml file at the root of your project.
#
# Be sure you are logged in to AWS, as this script runs an AWS CLI command.

check_node_code() {
  echo "Checking Node.js code"
  for function_directory in ${CODEBUILD_SRC_DIR}/lambda/* ; do
    cd ${function_directory}
    if [ -f "package.json" ]; then
      echo "  Linting ${function_directory}"
      npm run lint
      echo "  Testing ${function_directory}"
      npm test
    fi
  done
}

check_python_code() {
  echo "Checking Python code"
  for function_directory in ${CODEBUILD_SRC_DIR}/lambda/* ; do
    cd ${function_directory}
    if [ -f "requirements.txt" ]; then
      echo "  Linting ${function_directory}"
      pylint ${function_directory}
      echo "  Testing ${function_directory}"
      python -m pytest .
    fi
  done
}

check_cf_template() {
  echo "Linting CloudFormation template"
  cd ${CODEBUILD_SRC_DIR}
  cfn-lint --version
  # https://github.com/aws-cloudformation/cfn-python-lint/issues/1265#issuecomment-568525313
  cfn-lint --ignore-checks W3011 --append-rules ${CODEBUILD_SRC_DIR_LintRules} --template ${TEMPLATE_PATH}
}

download_authenticators_template() {
  echo "Copying Cirrus Authenticators template from S3"
  aws s3 cp s3://lly-templates/cirrus/cloudformation/cirr-aws-authenticators/latest.yaml ${CODEBUILD_SRC_DIR}/codebuild-api-authenticators/authenticators.yaml
}

download_db_migrations_template() {
  echo "Copying DB Migrations template from S3"
  aws s3 cp s3://${S3_DEPLOY_BUCKET}/iris_rvm/redshift_db_migrations.yml ${CODEBUILD_SRC_DIR}/app-templates/redshift_db_migrations.yml
}


echo "Starting pre_build - $(date)"
check_node_code
check_python_code
cd ${CODEBUILD_SRC_DIR}
python build-scripts/pre_build_lambda_libraries.py
check_cf_template
download_db_migrations_template
# download_authenticators_template
echo "Completed pre_build - $(date)"
