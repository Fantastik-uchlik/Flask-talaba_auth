from config.data_source import db


class Talaba(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ism = db.Column(db.String(50))
    familiya = db.Column(db.String(50))
    sharif = db.Column(db.String(50))
    telefon = db.Column(db.String(15))
    yunalish_id = db.Column(db.Integer, db.ForeignKey('yunalish.id'), nullable=False)
    yunalish = db.relationship('Yunalish', backref=db.backref('yunalishlar', lazy=True))
    guruh_id = db.Column(db.Integer, db.ForeignKey('guruh.id'), nullable=False)
    guruh = db.relationship('Guruh', backref=db.backref('guruhlar', lazy=True))

    def __init__(self, ism, familiya,sharif, telefon, yunalish_id, guruh_id):
        self.ism = ism
        self.familiya = familiya
        self.sharif = sharif
        self.telefon = telefon
        self.yunalish_id = yunalish_id
        self.guruh_id = guruh_id

