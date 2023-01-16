from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self, val):
        if val.get('page') is not None:
            genre = self.dao.get_all(page=val.get('page'))
        else:
            genre = self.dao.get_all()
        return genre

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def delete(self, gid):
        self.dao.delete(gid)

    def update(self, genre_d):
        self.dao.update(genre_d)
        return self.dao