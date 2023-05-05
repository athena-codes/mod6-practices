import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", 'not found')
    print(SECRET_KEY)
