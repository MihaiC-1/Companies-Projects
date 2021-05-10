from Repository.repo_proiect import *


class ServiceProiect:
    def __init__(self):
        self.repo = RepoProiect('proiecte.txt')

    def create(self, id_, id_firma, nume, durata, echipa):
        clas = Proiect(id_, id_firma, nume, durata, echipa)
        self.repo.create(clas)

    def read(self, id_):
        return self.repo.read(id_)

    def update(self, id_, id_firma, nume, durata, echipa):
        clas = Proiect(id_, id_firma, nume, durata, echipa)
        self.repo.update(clas)

    def delete(self, id_):
        self.repo.delete(id_)

    def show_all(self):
        return self.repo.all()
