from Domain.firma import *


def test_getter_firma():
    f = Firma(1, 'TEST', 'TEST Oras')

    assert f.get_id() == 1
    assert f.get_nume() == 'TEST'
    assert f.get_oras_sediu() == 'TEST Oras'
