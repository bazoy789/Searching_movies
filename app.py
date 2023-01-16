from flask import Flask
from flask_restx import Api

from views.directors import directors_ns
from views.favorite import favorite_ns
from views.movies import movies_ns
from views.genres import genres_ns
from views.users import users_ns
from views.auths import auth_ns
from setup_db import db
from config import Config

from dao.model.user import User


def config_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    create_db(app)
    return app


def create_db(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorite_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        user = User()
        with db.session.begin(user):
            db.session.commit()


app = config_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
