# AWS Cognito

[![Project Status](https://img.shields.io/static/v1?label=project%20status&message=complete&color=success&style=flat-square)](#)
[![GitHub License](https://img.shields.io/github/license/raphaelbh/aws-cognito?style=flat-square)](#)

Proof of concept to demonstrate how to use AWS Cognito.

> Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple.

Features:
- sign up
- confirm sign up
- sign in (initiate auth)
- sign out (global)
- get user
- delete user

## Requirements

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Installation

```bash
# aws-cli config
alias aws='docker run --rm -it -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli'
aws configure set aws_access_key_id ${your_aws_access_key_id}
aws configure set aws_secret_access_key ${your_aws_secret_access_key}
aws configure set region ${your_aws_default_region}

# create stack (user pool)
aws cloudformation create-stack --stack-name poc-cognito --template-body file://infrastructure/cloudformation/stack.yaml

# get user_pool_id and user_pool_client_id
aws cloudformation describe-stacks --stack-name poc-cognito
```
    
## Environment Variables

Set the follow env variables (./application/.env)

`AWS_ACCESS_KEY_ID`=${your_aws_access_key_id}

`AWS_SECRET_ACCESS_KEY`=${your_aws_secret_access_key}

`AWS_DEFAULT_REGION`=${your_aws_default_region}

`USER_POOL_ID`=${your_created_user_pool_id}

`USER_POOL_CLIENT_ID`=${your_created_user_pool_client_id}

## Usage / Tests

```bash
$ export PYTHONPATH=application 
$ pytest --cache-clear tests/
```

## Tech Stack

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![aws](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)

## Reference

- https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html

## Feedback

If you have any feedback, please contact me at raphaeldias.ti@gmail.com

[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/raphaelbh)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raphaelbh/)