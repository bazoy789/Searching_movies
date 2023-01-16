from flask_restx import abort
from flask import request
import jwt

from constants import JWT_SECRET, JWT_ALGORITHM
from dao.model.user import UserSchema
from implemented import user_service, favorite_service


def auth_req_get(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            dec_toc = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user = user_service.get_by_email(dec_toc['email'])
            return UserSchema().dump(user)
        except Exception:
            abort(401)
    return wrapper


def auth_req_patch(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        rej = func(*args, **kwargs)
        if 'password' in rej[0]:
            del rej[0]['password']
        try:
            dec_toc = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user = user_service.get_by_email(dec_toc['email'])
            if 'id' not in rej[0]:
                rej[0]['id'] = user.id
            user_service.update(rej[0])
            return 'update'
        except Exception:
            abort(401, '++++++')
    return wrapper


def auth_req_put(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        rej = func(*args, **kwargs)
        dec_toc = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = user_service.get_by_email(dec_toc['email'])
        _check = user_service.compare_password(user.password, rej[0]['password_old'])

        if 'id' not in rej[0]:
            rej[0]['id'] = user.id

        data = {
            'id': rej[0]['id'],
            'password': rej[0]['password']
        }
        try:
            if not _check:
                raise Exception()
            user_service.update(data)
            return 'update'
        except Exception:
            abort(401, '====')
    return wrapper


def favorite_reg_post(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        rej = func(*args, **kwargs)

        dec_toc = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        user = user_service.get_by_email(dec_toc['email'])
        new_favorite = {
            'user_id': user.id,
            'movie_id': rej[0]
        }
        print(new_favorite)
        try:
            favorite_service.create(new_favorite)
        except Exception:
            abort(401, '====')
        return True
    return wrapper


def favorite_reg_delete(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        rej = func(*args, **kwargs)

        dec_toc = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        user = user_service.get_by_email(dec_toc['email'])
        new_favorite = {
            'user_id': user.id,
            'movie_id': rej[0]
        }
        favorite_service.delete(new_favorite)
        # try:
        #
        # except Exception:
        #     abort(401, '====')
        return True
    return wrapper
