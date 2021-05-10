from Repository.repo_firma import *


def test_repo_firma():
    f = Firma(1000, 'TEST', 'TEST oras')
    repo = RepoFirma('firme.txt')

    rez = repo.read(1000)
    assert rez is None

    repo.create(f)
    rez = repo.read(1000)
    assert rez == f

    f2 = Firma(1000, 'TEST 2', 'TEST oras 2')
    repo.update(f2)
    rez = repo.read(1000)
    assert rez == f2

    repo.delete(1000)
    rez = repo.read(1000)
    assert rez is None
