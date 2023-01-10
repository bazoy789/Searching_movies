from flask_restx import abort
from flask import request
import jwt

from constants import JWT_SECRET, JWT_ALGORITHM


def auth_req(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)

        return func(*args, **kwargs)
    return wrapper


def admin_req(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)

            role = decode_token.get('role')

            if role != 'admin':
                abort(401)
        except Exception:
            abort(401)

        return func(*args, **kwargs)
    return wrapper

