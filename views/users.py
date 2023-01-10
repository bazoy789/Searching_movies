from flask import request
from flask_restx import Resource, Namespace

from implemented import user_service
from decorators import auth_req, admin_req
from dao.model.user import UserSchema

users_ns = Namespace('users')

@users_ns.route('/')
class UsersView(Resource):

    # @auth_req
    def get(self):
        all_users = user_service.get_all()
        return UserSchema(many=True).dump(all_users), 200

    # @admin_req
    def post(self):
        rej = request.json
        rs = user_service.create(rej)
        return '', 201, {'location': f'/users/{rs.id}'}

@users_ns.route('/<int:uid>')
class UserView(Resource):

    # @auth_req
    def get(self, uid):
        one_user = user_service.get_one(uid)
        return UserSchema().dump(one_user), 200

    # @auth_req
    def put(self, uid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = uid
        user_service.update(rej)
        return '', 204

    # @auth_req
    def patch(self, uid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = uid
        user_service.update(rej)
        return '', 204

    # @admin_req
    def delete(self, uid):
        user_service.delete(uid)
        return '', 204

