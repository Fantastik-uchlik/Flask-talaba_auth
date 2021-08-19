from repo.guruh_repo import GuruhRepo


class GuruhService():
    gr = GuruhRepo()
    def getAll(self):
        return self.gr.findAll()

    def create(self, guruh):
        return self.gr.create(guruh)

    def deleteById(self, id):
        return self.gr.deleteById(id)

    def getById(self, tahrirlashId):
        return self.gr.findById(tahrirlashId)

    def update(self, guruh):
        return self.gr.update(guruh)
