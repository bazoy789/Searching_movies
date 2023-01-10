from flask import request, abort
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthRegView(Resource):

    def post(self):

        rej = request.json
        email = rej.get('email')
        password = rej.get('password')
        if None in [email, password]:
            abort(401)
        data = {
            'email': email,
            'password': password
        }
        if user_service.get_by_email(email) is not None:
            return 'email not unique', 201
        user_service.create(data)
        return '', 201


@auth_ns.route('/login')
class AuthView(Resource):

    def post(self):
        rej = request.json
        email = rej.get('email')
        password = rej.get('password')
        if None in [email, password]:
            abort(401)

        tokens = auth_service.gen_token(email, password)
        return tokens, 201

    def put(self):
        rej = request.json
        refresh_token = rej.get('refresh_token')
        tokens = auth_service.new_refresh(refresh_token)
        return tokens, 201
