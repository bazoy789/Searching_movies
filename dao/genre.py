from typing import Optional

from config import Config
from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self, page: Optional[int] = None):
        if page:
            return self.session.query(Genre).paginate(page=page, per_page=Config.MAX_PAGE, error_out=False).items
        else:
            return self.session.query(Genre).all()

    def create(self, genre_d):
        exp = Genre(**genre_d)
        self.session.add(exp)
        self.session.commit()
        return exp

    def delete(self, gid):
        del_genre = self.get_one(gid)
        self.session.delete(del_genre)
        self.session.commit()

    def update(self, genre_d):
        id_genre = genre_d.get('id')
        self.session.query(Genre).filter(Genre.id == id_genre).update(genre_d)
        self.session.commit()
