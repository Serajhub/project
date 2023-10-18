import jwt
import datetime

SECRET_KEY = 'your-secret-key'

def generate_token(data):
    data['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')

def verify_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data
    except jwt.ExpiredSignatureError:
        return "Token expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
