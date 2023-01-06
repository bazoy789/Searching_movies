from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, val=None):
        movie_by_arg = self.session.query(Movie)
        if 'director_id' in val:
            movie_by_arg = movie_by_arg.filter(Movie.director_id == val.get('director_id'))
        if 'genre_id' in val:
            movie_by_arg = movie_by_arg.filter(Movie.genre_id == val.get('genre_id'))
        if 'year' in val:
            movie_by_arg = movie_by_arg.filter(Movie.year == val.get('year'))

        return movie_by_arg

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
        up_movie = self.get_one(movie_d.get('id'))
        self.session.query(Movie).filter(Movie.id == up_movie).update(movie_d)
        self.session.commit()
