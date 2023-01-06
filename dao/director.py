from dao.model.director import Director


class DirectorDAO:
    def __int__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
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
        up_director = self.get_one(director_d.get('id'))
        self.session.query(Director).filter(Director.id == up_director).update(director_d)
        self.session.commit()
