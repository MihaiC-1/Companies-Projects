from Service.service_firma import *
from Service.service_proiect import *
import json


class Console:
    def __init__(self):
        self.firme = ServiceFirma()
        self.proiecte = ServiceProiect()

    def menu(self):
        """
        Afisarea meniului de optiuni.
        """
        print('1. Adaugare firma')
        print('2. Adaugare proiect')
        print('3. Afisare firme si numarul de proiecte descrescator')
        print('4. Afisare echipe cu numarul de proiecte descrescator')
        print('5. Export json file')
        print('6. Exit')

    def handle_add_firma(self):
        """
        Adaugare unui obiect de tip firma.
        """
        try:
            id_ = int(input('ID : '))
            nume = input('Nume : ')
            oras_sediu = input('Oras sediu central : ')

            if nume == '':
                raise ValueError('Numele trebuie sa fie neul.')

            if len(oras_sediu) < 3:
                raise ValueError('Oras sediu central trebuie sa fie de minim 3 caractere.')

            self.firme.create(id_, nume, oras_sediu)
        except Exception as ex:
            print(ex)

    def handle_add_proiect(self):
        """
        Adaugarea unui obiect de tip proiect.
        """
        try:
            id_ = int(input('ID : '))
            id_firma = int(input('ID firma : '))
            nume = input('Nume : ')
            durata = int(input('Durata proiect : '))
            echipa = input('Echipa asignata : ')

            firme = self.firme.show_all()
            ok = True
            for f in firme:
                if f.get_id() == id_firma:
                    ok = False
                    break
            if ok:
                raise ValueError('ID firma nu exista.')

            if nume == '':
                raise ValueError('Numele trebuie sa fie nenul.')

            if echipa == '':
                raise ValueError('Numele echipei asignate trebuie sa fie nenul.')

            self.proiecte.create(id_, id_firma, nume, durata, echipa)
        except Exception as ex:
            print(ex)

    def handle_show_firme_si_numar_proiecte_descresc(self):
        """
        Afiseaza pe ecran firmele si numarul de proiecte ale acestei firme in ordine descrescatoare
        dupa acest numar.
        """
        proiecte = self.proiecte.show_all()
        firme = self.firme.show_all()
        rez = []

        for f in firme:
            count = 0
            for p in proiecte:
                if p.get_id_firma() == f.get_id():
                    count += 1
            rez.append([f.get_id(), count])

        for i in range(len(rez) - 1):
            for j in range(i + 1, len(rez)):
                if rez[i][1] < rez[j][1]:
                    aux = rez[i]
                    rez[i] = rez[j]
                    rez[j] = aux

        for r in rez:
            print(self.firme.read(r[0]), ' ---> Numar proiecte : ', r[1], '\n')

    def handle_show_echipe_cu_numar_proiecte(self):
        """
        Afiseaza pe ecran numele echipelor, numele firmelor din care fac parte si numarul de proiecte ale acestei
        echipe in ordine descrescatoare dupa acest numar.
        """
        proiecte = self.proiecte.show_all()
        rez = []

        for p in proiecte:
            if p.get_echipa_asignata() not in rez:
                rez.append(p.get_echipa_asignata())

        for i in range(len(rez) - 1):
            for j in range(i + 1, len(rez)):
                count_i = 0
                count_j = 0
                for p in proiecte:
                    if p.get_echipa_asignata() == rez[i]:
                        count_i += 1
                    elif p.get_echipa_asignata() == rez[j]:
                        count_j += 1
                if count_i < count_j:
                    aux = rez[i]
                    rez[i] = rez[j]
                    rez[j] = aux

        for r in rez:
            count = 0
            for p in proiecte:
                if p.get_echipa_asignata() == r:
                    count += 1
                    id_firma = p.get_id_firma()
            firma = self.firme.read(id_firma)
            print('Echipa : ', r, ', din firma : ', firma.get_nume(), ', au numar de proiecte = ', count, '\n')

    def handle_export_json_file(self):
        """
        Scrie intr-un fisier cu extensia .json numele firmelor si echipele din aceasta firma ce au durata maxina
        la proiectul asignat.
        """
        firme = self.firme.show_all()
        proiecte = self.proiecte.show_all()
        data = {}

        for f in firme:
            if f.get_nume() not in data:
                data[f.get_nume()] = []

        for f in firme:
            durata_maxima = 0
            echipa_maxima = ''
            for p in proiecte:
                if p.get_id_firma() == f.get_id():
                    if durata_maxima < p.get_durata_proiect():
                        durata_maxima = p.get_durata_proiect()
                        echipa_maxima = p.get_echipa_asignata()
            data[f.get_nume()] = [echipa_maxima, durata_maxima]

        f = open('/Users/c.mihai/Desktop/exersare/r4921/out.json', "w")
        json.dump(data, f, indent=4)

    def run_console(self):
        """
        Prelucrarea optiunilor din meniul aplicatiei.
        """
        while True:
            self.menu()
            op = input('Alegeti o optiune : ')
            if op == '1':
                self.handle_add_firma()
            elif op == '2':
                self.handle_add_proiect()
            elif op == '3':
                self.handle_show_firme_si_numar_proiecte_descresc()
            elif op == '4':
                self.handle_show_echipe_cu_numar_proiecte()
            elif op == '5':
                self.handle_export_json_file()
            elif op == '6':
                print('Exit program !!')
                break
            else:
                print('Nu exista optiunea !')
