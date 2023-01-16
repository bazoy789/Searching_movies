from dao.model.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, fid):
        return self.session.query(Favorite).get(fid)

    def create(self, favorite_d):
        favorite = Favorite(**favorite_d)
        self.session.add(favorite)
        self.session.commit()
        return favorite

    def delete(self, favorite_d):
        user_id = favorite_d['user_id'],
        movie_id = favorite_d['movie_id']
        print(user_id[0])
        print(movie_id)
        del_favorite = self.session.query(Favorite).filter_by(user_id=user_id[0], movie_id=movie_id).first()
        self.session.delete(del_favorite)
        self.session.commit()
