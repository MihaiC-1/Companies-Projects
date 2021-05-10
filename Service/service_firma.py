from Repository.repo_firma import *


class ServiceFirma:
    def __init__(self):
        self.repo = RepoFirma('firme.txt')

    def create(self, id_, nume, oras_sediu):
        clas = Firma(id_, nume, oras_sediu)
        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, nume, oras_sediu):
        clas = Firma(id_, nume, oras_sediu)
        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()
