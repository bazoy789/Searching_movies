from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from dao.favorite import FavoriteDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from service.user import UserService
from service.auth import AuthService
from service.favorite import FavoriteService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
favorite_dao = FavoriteDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service=user_service)
favorite_service = FavoriteService(dao=favorite_dao)