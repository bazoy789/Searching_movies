from flask import request
from flask_restx import Resource, Namespace

from implemented import genre_service
from decorators import auth_req, admin_req
from dao.model.genre import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):

    @auth_req
    def get(self):
        all_genre = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genre), 200

    @admin_req
    def post(self):
        rej = request.json
        rs = genre_service.create(rej)
        return '', 201, {'location': f'/genre/{rs.id}'}


@genres_ns.route('/<int:gid>')
class GenreView(Resource):

    @auth_req
    def get(self, gid):
        one_genre = genre_service.get_one(gid)
        return GenreSchema().dump(one_genre), 200

    @admin_req
    def put(self, gid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = gid
        genre_service.update(rej)
        return '', 204

    @admin_req
    def patch(self, gid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = gid
        genre_service.update(rej)
        return '', 204

    @admin_req
    def delete(self, gid):
        genre_service.delete(gid)
        return '', 204
