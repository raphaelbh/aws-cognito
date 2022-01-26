from os import access
from libs.fake import fake
from libs.cognito import cognito

# fake user
user = fake.create_user()

# sign up user
cognito.sign_up(user)
cognito.admin_confirm_sign_up(user)

# check sign in
jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token']
cognito.get_user(access_token)

# check signout
cognito.global_sign_out(access_token)
cognito.get_user(access_token)

# delete user
jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token']
cognito.delete_user(access_token)