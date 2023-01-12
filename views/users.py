from flask_restx import Resource, Namespace
from flask import request

from decorators import auth_req_get, auth_req_put, auth_req_patch

users_ns = Namespace('users')


@users_ns.route('/')
class UsersView(Resource):
    @auth_req_get
    def get(self):
        return '', 200

    @auth_req_patch
    def patch(self):
        rej = request.json
        return rej, 204

    @auth_req_put
    def put(self):
        rej = request.json
        return rej, 204
