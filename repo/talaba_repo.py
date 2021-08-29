from config.data_source import db
from model.talaba import Talaba


class TalabaRepo():
    def findById(self, id):
        return db.session.query(Talaba).filter(Talaba.id == id).first()
    def findAll(self, page, size):

        return Talaba.query.paginate(page, per_page=size)
       # return db.session.query(Talaba).paginate(page, per_page=10)

    def create(self, talaba):
        db.session.add(talaba)
        db.session.commit()
        return True

    def deleteById(self, id):
        m = self.findById(id)
        db.session.delete(m)
        db.session.commit()
        return True

    def update(self, talaba):
        t = self.findById(talaba.id)
        t.ism = talaba.ism
        t.familiya = talaba.familiya
        t.sharif = talaba.sharif
        t.telefon = talaba.telefon
        t.yunalish_id = talaba.yunalish_id
        t.guruh_id = talaba.guruh_id
        db.session.commit()
        return True

    def count(self):
        return db.session.query(Talaba).count()