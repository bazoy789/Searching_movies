import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SOLT, PWD_HASH_ITERATIONS, PWD_ALGO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def create(self, movie_d):
        movie_d['password'] = self.make_password(movie_d.get('password'))
        return self.dao.create(movie_d)

    def delete(self, mid):
        self.dao.delete(mid)

    def update(self, movie_d):
        if 'password' in movie_d:
            movie_d['password'] = self.make_password(movie_d.get('password'))
        return self.dao.update(movie_d)

    def make_password(self, password):
        hash_password = hashlib.pbkdf2_hmac(PWD_ALGO,
                                            password.encode('utf-8'),
                                            PWD_HASH_SOLT,
                                            PWD_HASH_ITERATIONS
                                            )
        return base64.b64encode(hash_password)

    def compare_password(self, hash_password, password) -> bool:
        return hmac.compare_digest(base64.b64decode(hash_password),
                                   hashlib.pbkdf2_hmac(PWD_ALGO,
                                                       password.encode('utf-8'),
                                                       PWD_HASH_SOLT,
                                                       PWD_HASH_ITERATIONS
                                                       )
                                   )
