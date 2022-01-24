from libs.fake import fake
from libs.cognito import cognito

user = fake.create_user()

cognito.sign_up(user)
cognito.admin_confirm_sign_up(user)
jwt = cognito.initiate_auth(user)
cognito.get_user(jwt['access_token'])
cognito.global_sign_out(jwt['access_token'])
cognito.get_user(jwt['access_token'])