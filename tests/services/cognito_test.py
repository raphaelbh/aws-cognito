import unittest

import application.utils.fake as fake
import application.services.cognito as cognito

class CognitoTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(CognitoTest, cls).setUpClass()
        cls.user = fake.user()

    def test_1_sign_up_user(self):
        # sign up
        response_sign_up = cognito.sign_up(self.user)
        response_admin_confirm_sign_up = cognito.admin_confirm_sign_up(self.user)
        # validate
        assert 200 == response_sign_up['statusCode']
        assert 200 == response_admin_confirm_sign_up['statusCode']

    def test_2_sign_in_user(self):
        # sign in
        response = cognito.initiate_auth(self.user)
        # validate
        assert 200 == response['statusCode']
        assert len(response['body']['access_token']) > 0
    
    def test_3_get_user(self):
        # get access token
        response_initiate_auth = cognito.initiate_auth(self.user)
        access_token = response_initiate_auth['body']['access_token']
        # get user
        response_get_user = cognito.get_user(access_token)
        # validate
        assert 200 == response_get_user['statusCode']
    
    def test_4_sign_out(self):
        # get access token
        response_initiate_auth = cognito.initiate_auth(self.user)
        access_token = response_initiate_auth['body']['access_token']
        # sign out
        cognito.global_sign_out(access_token)
        # check access token after sign out
        response = cognito.get_user(access_token)
        # validate
        assert 500 == response['statusCode']

    def test_5_delete_user(self):
        # get access token
        response_initiate_auth = cognito.initiate_auth(self.user)
        access_token = response_initiate_auth['body']['access_token']
        # delete user
        response_delete_user = cognito.delete_user(access_token)
        # validate
        assert 200 == response_initiate_auth['statusCode']
        assert 200 == response_delete_user['statusCode']

if __name__ == '__main__':
    unittest.main()