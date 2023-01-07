from flask import request, abort
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


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
        return tokens, 204
