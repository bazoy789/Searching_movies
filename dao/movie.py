from typing import Optional

from dao.model.movie import Movie
from setup_db import db
from config import Config

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all_get(self, val):
        movie_by_arg = self.session.query(Movie)
        print(movie_by_arg)
        if 'director_id' in val:
            movie_by_arg = movie_by_arg.filter(Movie.director_id == val.get('director_id'))
        elif 'genre_id' in val:
            movie_by_arg = movie_by_arg.filter(Movie.genre_id == val.get('genre_id'))
        elif 'year' in val:
            movie_by_arg = movie_by_arg.filter(Movie.year == val.get('year'))
        return movie_by_arg.all()

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None):
        if page and status == 'new':
            movie_by_arg = self.session.query(Movie).order_by(db.desc(Movie.year))
            movie_by_arg = movie_by_arg.paginate(page=page, per_page=Config.MAX_PAGE, error_out=False).items

            return movie_by_arg
        elif page:
            return self.session.query(Movie).paginate(page=page, per_page=Config.MAX_PAGE, error_out=False).items

        elif status == 'new':
            return self.session.query(Movie).order_by(db.desc(Movie.year))

    def create(self, movie_d):
        exp = Movie(**movie_d)
        self.session.add(exp)
        self.session.commit()
        return exp

    def delete(self, mid):
        del_movie = self.get_one(mid)
        self.session.delete(del_movie)
        self.session.commit()

    def update(self, movie_d):
        id_movie = movie_d.get('id')
        self.session.query(Movie).filter(Movie.id == id_movie).update(movie_d)
        self.session.commit()


