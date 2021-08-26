from config.data_source import db


class Guruh(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100))
    yunalish_id = db.Column(db.Integer, db.ForeignKey('yunalish.id'), nullable=False)
    yunalish = db.relationship('Yunalish', backref=db.backref('guruhlar', lazy=True))
    til = db.Column(db.String(20))
    yil = db.Column(db.Integer)


    def __init__(self, nom, yunalish_id,til, yil):
        self.nom = nom
        self.yunalish_id = yunalish_id
        self.til = til
        self.yil = yil


