from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self, val=None):
        all_user = self.session.query(User)
        if 'username' in val:
            all_user = all_user.filter(User.name == val.get('username')).first()
        return all_user


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
        user_id = self.get_one(user_d.get('id'))
        self.session.query(User).filter(User.id == user_id).update(user_d)
        self.session.commit()
