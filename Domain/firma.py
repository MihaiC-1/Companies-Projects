class Firma:
    def __init__(self, id_, nume, oras_sediu):
        self.id_ = id_
        self.nume = nume
        self.oras_sediu = oras_sediu

    def __str__(self):
        return 'ID : {}, Nume : {}, Orasul sediului central : {}'.format(self.id_, self.nume, self.oras_sediu)

    def get_id(self):
        return self.id_

    def get_nume(self):
        return self.nume

    def get_oras_sediu(self):
        return self.oras_sediu
