from Domain.proiect import *


def test_getter_proiect():
    p = Proiect(1, 3, 'TEST', 23, 'TEST echipa')

    assert p.get_id() == 1
    assert p.get_id_firma() == 3
    assert p.get_nume() == 'TEST'
    assert p.get_durata_proiect() == 23
    assert p.get_echipa_asignata() == 'TEST echipa'
