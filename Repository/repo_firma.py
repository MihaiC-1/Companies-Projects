from Domain.firma import *


class RepoFirma:
    def __init__(self, file_name):
        self.file = file_name
        self.store = []
        self.store = self.readFile()

    def readFile(self):
        """
        Citeste obiecte de tip firma din fisier si le retine intr-o lista.
        :return: o lista de obiecte de tip Firma.
        """
        store_b = []
        f = open(self.file, "r")
        lines = f.readlines()
        for line in lines:
            s = line[:-1]
            rip = s.split("/")
            id_ = int(rip[0])
            nume = rip[1]
            oras_sediu = rip[2]
            c = Firma(id_, nume, oras_sediu)
            store_b.append(c)
        f.close()
        return store_b

    def writeFile(self):
        """
        Scrie in fisier obiectele de tip firma din memorie.
        :return:
        """
        f = open(self.file, "w")
        content = ""
        for p in self.store:
            line = '{}/{}/{}\n'.format(p.get_id(), p.get_nume(), p.get_oras_sediu())
            content += line
        f.write(content)
        f.close()

    def create(self, c):
        """
        Creeaza un obiect dou de tip firma.
        :param c:
        :return:
        """
        for p in self.store:
            if p.get_id() == c.get_id():
                raise ValueError('ID-ul exista deja')
        self.store.append(c)
        self.writeFile()

    def read(self, id_=None):
        """
        Citeste un obiect de tip firma dupa un id dat.
        :param id_: intreg
        :return: obiect de tip firma
        """
        if id_ is None:
            return self.store[:]
        for p in self.store:
            if p.get_id() == id_:
                return p
        return None

    def update(self, c):
        """
        Inlocuieste un obiect din memorie cu noul obiect dat.
        :param c:
        :return:
        """
        id_ = c.get_id()
        for index in range(len(self.store)):
            if self.store[index].get_id() == id_:
                self.store[index] = c
                break
        self.writeFile()

    def delete(self, id_):
        """
        Sterge un obiect de tip firma din lista de obiecte dupa un id dat.
        :param id_:
        :return:
        """
        for index in range(len(self.store)):
            if id_ == self.store[index].get_id():
                del self.store[index]
                break
        self.writeFile()
        KeyError('Nu exista acest id')

    def all(self):
        """
        :return: lista de obiecte de tip firma.
        """
        return self.store
