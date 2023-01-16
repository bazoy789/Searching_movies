from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self, val):
        if val.get('page') is not None:
            director = self.dao.get_all(page=val.get('page'))
        else:
            director = self.dao.get_all()
        return director


    def create(self, director_d):
        return self.dao.create(director_d)

    def delete(self, did):
        self.dao.delete(did)

    def update(self, director_d):
        self.dao.update(director_d)
        return self.dao
