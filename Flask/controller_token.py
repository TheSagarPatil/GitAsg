from functools import wraps
import jwt
import datetime

key = "\xc1\xc8\xef\xb6\xd4,\xbc\x82I\x8azD\x08\xb6\xf4\xe4\n]\x0e\xb8\xd7\x8c1\xaf"

def encode_auth_token(payloadData):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta( days = 0, seconds = 9000),
            'iat': datetime.datetime.utcnow(),
            'sub': payloadData
        }
        return jwt.encode(
            payload,
            #app.config.get('SECRET_KEY'),
            key
        )
    except Exception as e:
        return e

def decodeToken(token):
    data = jwt.decode(token, key, options={"verify_signature": False})
    print('decodedData', data)
    return data

def isTokenExpired(tokenData : dict):
    print(tokenData['exp'], datetime.datetime.now().timestamp())
    return tokenData['exp'] < datetime.datetime.now().timestamp()

def isAuthenticated(request):
    auth = request.authorization
    frm = request.form

    if frm['user_id'] == '1' and frm['password'] == 'password':
        return True

    return False