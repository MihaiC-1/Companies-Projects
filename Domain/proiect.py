class Proiect:
    def __init__(self, id_, id_firma, nume, durata, echipa):
        self.id_ = id_
        self.id_firma = id_firma
        self.nume = nume
        self.durata = durata
        self.echipa = echipa

    def __str__(self):
        return 'ID : {}, ID firma : {}, Nume : {}, Durata : {}, Echipa asignata : {}'.format(self.id_, self.id_firma,
                                                                                             self.nume, self.durata,
                                                                                             self.echipa)

    def get_id(self):
        return self.id_

    def get_id_firma(self):
        return self.id_firma

    def get_nume(self):
        return self.nume

    def get_durata_proiect(self):
        return self.durata

    def get_echipa_asignata(self):
        return self.echipa
