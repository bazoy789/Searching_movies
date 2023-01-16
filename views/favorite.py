from flask_restx import Namespace, Resource
from decorators import favorite_reg_post, favorite_reg_delete

favorite_ns = Namespace('favorite/movies')


@favorite_ns.route('/<int:fid>')
class FavoriteView(Resource):

    @favorite_reg_post
    def post(self, fid):
        return fid, 200

    @favorite_reg_delete
    def delete(self, fid):
        return fid, 204
