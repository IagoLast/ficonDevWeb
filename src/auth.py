from functools import wraps
from flask import request, Response
from werkzeug.security import check_password_hash

from src.database import find_user

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    user = find_user(username)
    if (user == None):
        return False
    hashed_password = user['hashed_password']
    print hashed_password
    return check_password_hash(hashed_password, password)

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated