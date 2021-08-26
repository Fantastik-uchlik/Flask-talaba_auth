from config.data_source import db
from model.user import User


class UserRepo():
    def findById(self, id):
        return db.session.query(User).filter(User.id == id).first()
    def findAll(self):
        return db.session.query(User).all()

    def create(self, user):
        db.session.add(user)
        db.session.commit()
        return True

    def deleteById(self, id):
        m = self.findById(id)
        db.session.delete(m)
        db.session.commit()
        return True

    def update(self, user):
        t = self.findById(user.id)
        t.ism = user.ism
        t.familiya = user.familiya
        t.login = user.login
        t.parol = user.parol
        db.session.commit()
        return True

    def findByLogin(self, login):
        return db.session.query(User).filter(User.login == login).first()