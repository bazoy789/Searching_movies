from marshmallow import Schema, fields

from setup_db import db


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id_rel = db.relationship('User')
    movie_id_rel = db.relationship('Movie')


class FavoriteSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    movie_id = fields.Int()
