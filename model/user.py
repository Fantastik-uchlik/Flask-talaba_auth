from flask_login import UserMixin

from config.data_source import db


class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ism = db.Column(db.String(100))
    familiya = db.Column(db.String(30))
    login = db.Column(db.String(30))
    parol = db.Column(db.String(30))


    def __init__(self, ism, familiya, login, parol):
        self.ism = ism
        self.familiya = familiya
        self.login = login
        self.parol = parol


