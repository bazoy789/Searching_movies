from dao.model.director import Director

from typing import Optional
from config import Config


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self, page: Optional[int] = None):
        if page:
            return self.session.query(Director).paginate(page=page, per_page=Config.MAX_PAGE, error_out=False).items
        else:
            return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, did):
        del_director = self.get_one(did)
        self.session.delete(del_director)
        self.session.commit()

    def update(self, director_d):
        id_director = director_d.get('id')
        self.session.query(Director).filter(Director.id == id_director).update(director_d)
        self.session.commit()
