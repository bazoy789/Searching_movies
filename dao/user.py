from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        del_user = self.get_one(uid)
        self.session.delete(del_user)
        self.session.commit()

    def update(self, user_d):
        user_id = user_d.get('id')
        self.session.query(User).filter(User.id == user_id).update(user_d)
        self.session.commit()
