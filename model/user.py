from flask_login import UserMixin

from config.data_source import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ism = db.Column(db.String(100), nullable=False)
    familiya = db.Column(db.String(30))
    login = db.Column(db.String(30), unique=True, nullable=False)
    parol = db.Column(db.String(30), nullable=False)

    def __init__(self, ism, familiya, login, parol):
        self.ism = ism
        self.familiya = familiya
        self.login = login
        self.parol = parol

    def get_id(self):
        return self.login
