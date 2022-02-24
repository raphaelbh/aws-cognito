import uuid

def user():
    user = uuid.uuid4().hex[0:7] 
    email = user + '@fake.com'
    return {
        'username':  email,
        'password': 'user@password',
        'attributes': [{
            'Name': 'name',
            'Value': user
        }, {
            'Name': 'email',
            'Value': email
        }]
    }