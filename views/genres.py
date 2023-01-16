from flask import request
from flask_restx import Resource, Namespace

from implemented import genre_service
from dao.model.genre import GenreSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):


    def get(self):
        page = request.args.get('page', type=int)
        filters = {
            'page': page
        }
        all_genre = genre_service.get_all(filters)
        return GenreSchema(many=True).dump(all_genre), 200


    def post(self):
        rej = request.json
        rs = genre_service.create(rej)
        return '', 201, {'location': f'/genre/{rs.id}'}


@genres_ns.route('/<int:gid>')
class GenreView(Resource):


    def get(self, gid):
        one_genre = genre_service.get_one(gid)
        return GenreSchema().dump(one_genre), 200

    def put(self, gid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = gid
        genre_service.update(rej)
        return '', 204


    def patch(self, gid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = gid
        genre_service.update(rej)
        return '', 204


    def delete(self, gid):
        genre_service.delete(gid)
        return '', 204
