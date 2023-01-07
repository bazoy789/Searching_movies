from flask import request
from flask_restx import Resource, Namespace

from decorators import auth_req, admin_req
from implemented import director_service
from dao.model.director import DirectorSchema

directors_ns = Namespace('directors')

@directors_ns.route('/')
class DirectorsView(Resource):

    @auth_req
    def get(self):
        all_directors = director_service.get_all()
        return DirectorSchema(many=True).dump(all_directors), 200

    @admin_req
    def post(self):
        rej = request.json
        rd = director_service.create(rej)
        return '', 201, {'location': f'/director/{rd.id}'}

@directors_ns.route('/<int:did>')
class DirectorView(Resource):

    @auth_req
    def get(self, did):
        one_director = director_service.get_one(did)
        return DirectorSchema().dump(one_director), 200

    @admin_req
    def put(self, did):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = did
        director_service.update(rej)
        return '', 204

    @admin_req
    def patch(self, did):
        rej = request.json
        if 'id' not in rej:
            rej['id'] = did
        director_service.update(rej)
        return '', 204

    @admin_req
    def delete(self, did):
        director_service.delete(did)
        return '', 204