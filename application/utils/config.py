import os
from dotenv import load_dotenv

load_dotenv()

AWS_CONFIG = {
    "credentials": {
        "access_key": os.environ.get("AWS_ACCESS_KEY_ID"),
        "secret_key": os.environ.get("AWS_SECRET_ACCESS_KEY")
    },
    "region": os.environ.get("AWS_DEFAULT_REGION"),
    "cognito": {
        "user_pool_id": os.environ.get("USER_POOL_ID"),
        "user_pool_client_id": os.environ.get("USER_POOL_CLIENT_ID")
    }
}