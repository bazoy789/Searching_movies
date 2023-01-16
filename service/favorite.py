from dao.favorite import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def create(self, favorite_d):
        return self.dao.create(favorite_d)

    def delete(self, favorite_d):
        self.dao.delete(favorite_d)
