import re
from repo.user_repo import UserRepo


class UserService():
    tr = UserRepo()
    def getAll(self):
        return self.tr.findAll()

    def create(self, User):
        return self.tr.create(User)

    def deleteById(self, id):
        return self.tr.deleteById(id)
    def getById(self,tahrirlashId):
        return self.tr.findById(tahrirlashId)
    def update(self, User):
        return self.tr.update(User)

    def getByLogin(self, login):
        return self.tr.findByLogin(login)
