import calendar
import datetime
import jwt

from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def gen_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_password(user.password, password):
                raise Exception()

        data = {
            'email': email,
            'password': password
        }

        min60 = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        data['exp'] = calendar.timegm(min60.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        day100 = datetime.datetime.utcnow() + datetime.timedelta(days=100)
        data['exp'] = calendar.timegm(day100.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def new_refresh(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])

        email = data.get('email')
        password = data.get('password')
        user = self.user_service.get_by_email(email)
        if user is None:
            raise Exception()

        return self.gen_token(email, password, is_refresh=True)
