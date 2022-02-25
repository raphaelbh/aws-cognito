import uuid

def user():
    user = uuid.uuid4().hex[0:7] 
    email = user + '@fake.com'
    return {
        'username':  email,
        'password': 'User001@Password',
        'attributes': [{
            'Name': 'name',
            'Value': user
        }, {
            'Name': 'email',
            'Value': email
        }]
    }