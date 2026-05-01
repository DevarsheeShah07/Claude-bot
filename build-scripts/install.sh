#!/bin/bash
# set -xe

# This runs the install phase of the build.
#
# To run outside CodeBuild, set the following variables before running:
# CODEBUILD_SRC_DIR
#   Set this to your project's root directory.

install_tools() {
  echo "Installing AWS SAM CLI"
  pip install aws-sam-cli==1.58.0

  echo "Installing CloudFormation template linting tool cfn-lint"
  pip install cfn-lint

  echo "Installing Python code linting tool pylint"
  pip install pylint

  echo "Installing Python testing tool pytest"
  pip install pytest
  pip install --force-reinstall aws-sam-translator==1.57.0

  echo "Installing Python aws sdk boto3"
  pip install --force-reinstall boto3==1.26.101
}

install_dependencies() {
  echo "Installing Node.js code dependencies"
  for function_directory in ${CODEBUILD_SRC_DIR}/lambda/* ; do
    cd ${function_directory}
    if [ -f "package.json" ]; then
      echo "  Installing dependencies for ${function_directory}"
      npm install
    fi
  done

  echo "Installing Python code dependencies"
  for function_directory in ${CODEBUILD_SRC_DIR}/lambda/* ; do
    cd ${function_directory}
    if [ -f "requirements.txt" ]; then
      echo "  Installing dependencies for ${function_directory}"
      pip install -r requirements.txt
    fi
  done
}

install_layers() {
  echo "Installing Lambda layers"
  export PYTHON_VERSION=3.7
  for function_directory in ${CODEBUILD_SRC_DIR}/lambda/*; do
    cd ${function_directory}
    if [ -f "install_layer.sh" ]; then
      echo "  Installing layer in ${function_directory}"
      LAYER_DIR=${function_directory}
      /bin/bash ./install_layer.sh $PYTHON_VERSION
    fi
  done
}

echo "Starting install - $(date)"
install_tools
install_dependencies
install_layers
echo "Completed install - $(date)"
