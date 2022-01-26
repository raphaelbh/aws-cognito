from libs.fake import fake
from libs.cognito import cognito

# fake user
user = fake.create_user()

# sign up user
cognito.sign_up(user)
cognito.admin_confirm_sign_up(user)
print('User created')

# check sign in
jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token']
cognito.get_user(access_token)
print('User auth')

# check signout
cognito.global_sign_out(access_token)
cognito.get_user(access_token)
print('User sign out')

# delete user
jwt = cognito.initiate_auth(user)
access_token = jwt['body']['access_token']
cognito.delete_user(access_token)
print('User deleted')