from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, val):
        if val.get('director_id') is not None:
            movies = self.dao.get_all_get(val)
        elif val.get('genre_id') is not None:
            movies = self.dao.get_all_get(val)
        elif val.get('year') is not None:
            movies = self.dao.get_all_get(val)
        elif val.get('page') or val.get('status') is not None:
            movies = self.dao.get_all(page=val.get('page'), status=val.get('status'))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def delete(self, mid):
        self.dao.delete(mid)

    def update(self, movie_d):
        return self.dao.update(movie_d)
