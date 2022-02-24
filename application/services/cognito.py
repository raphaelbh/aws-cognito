import boto3
import sys
from utils.config import AWS_CONFIG

cognito_idp = boto3.client('cognito-idp', region_name=AWS_CONFIG['region'])

def sign_up(user):
    try:
        response = cognito_idp.sign_up(
            ClientId = AWS_CONFIG['cognito']['user_pool_client_id'],
            Username = user['username'],
            Password = user['password'],
            UserAttributes = user['attributes']
        )
        return __response(200, {
            'userSub': response['UserSub'],
            'codeDeliveryDetails': response['CodeDeliveryDetails'],
            'userConfirmed': response['UserConfirmed']
        })
    except:
        e = sys.exc_info()[1]
        return __response(500, e.args[0])

def admin_confirm_sign_up(user):
    try:
        cognito_idp.admin_confirm_sign_up(
            UserPoolId = AWS_CONFIG['cognito']['user_pool_id'],
            Username = user['username']
        )
        return __response(200, {
            'userConfirmed': True
        })
    except:
        e = sys.exc_info()[1]
        return __response(500, e.args[0])

def initiate_auth(user):
    try:
        response = cognito_idp.initiate_auth(
            AuthFlow = 'USER_PASSWORD_AUTH',
            AuthParameters = {
                'USERNAME': user['username'],
                'PASSWORD': user['password']
            },
            ClientId = AWS_CONFIG['cognito']['user_pool_client_id']
        )
        return __response(200, {
            'access_token': response['AuthenticationResult']['AccessToken'],
            'id_token': response['AuthenticationResult']['IdToken'],
            'refresh_token': response['AuthenticationResult']['RefreshToken']
        })
    except:
        e = sys.exc_info()[1]
        return __response(500, e.args[0])

def get_user(access_token):
    try:
        response = cognito_idp.get_user(
            AccessToken = access_token
        )
        return __response(200, response['UserAttributes'])
    except:
        e = sys.exc_info()[1]
        return __response(500, e.args[0])

def delete_user(access_token):
    try:
        cognito_idp.delete_user(
            AccessToken = access_token
        )
        return __response(200, {
            'userDeleted': True
        })
    except:
        e = sys.exc_info()[1]
        return __response(500, e.args[0])

def global_sign_out(access_token):
    try:
        response = cognito_idp.global_sign_out(
            AccessToken = access_token
        )
        return __response(200, response)
    except:
        e = sys.exc_info()[1]
        return __response(500, e.args[0])

def __response(statusCode, body):
    response = {
        'statusCode': statusCode,
        'body': body
    }
    return response