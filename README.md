# AWS Cognito

## Overview

Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple.

https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html

## Use Case
- sign up
- confirm sign up
- sign in (initiate auth)
- sign out
- get user

API: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html

## Requirements
- aws account (https://aws.amazon.com/)
- python (https://www.python.org/)

## Setup
1. Create stack through cloud formation file (cloudformatino/stack.yml)

2. Set the follow env variables (app/libs/.env) 
- AWS_ACCESS_KEY_ID=XXXX
- AWS_SECRET_ACCESS_KEY=XXXX
- AWS_REGION=XXXX
- USER_POOL_ID=XXXX
- APP_CLIENT_ID=XXXX
- APP_CLIENT_SECRET=XXXX

## Running

`$ python3 ./app/index.py`