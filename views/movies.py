from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service
from decorators import auth_req, admin_req
from dao.model.movie import MovieSchema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MovieView(Resource):

    # @auth_req
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        status = request.args.get('status', type=str)
        page = request.args.get('page', type=int)
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
            'status': status,
            'page': page
        }
        all_movies = movie_service.get_all(filters)
        return MovieSchema(many=True).dump(all_movies), 200

    # @admin_req
    def post(self):
        rej = request.json
        rs = movie_service.create(rej)
        return '', 201, {'location': f'/movies/{rs.id}'}


@movies_ns.route('/<int:mid>')
class MovieView(Resource):

    # @auth_req
    def get(self, mid):
        one_movie = movie_service.get_one(mid)
        return MovieSchema().dump(one_movie), 200

    # @admin_req
    def put(self, mid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = mid
        movie_service.update(rej)
        return '', 204

    # @admin_req
    def patch(self, mid):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = mid
        movie_service.update(rej)
        return '', 204

    # @admin_req
    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
