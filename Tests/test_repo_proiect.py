from Repository.repo_proiect import *


def test_repo_proiect():
    p = Proiect(1000, 1002, 'TEST', 3000, 'TEST echipa')
    repo = RepoProiect('proiecte.txt')

    rez = repo.read(1000)
    assert rez is None

    repo.create(p)
    rez = repo.read(1000)
    assert rez == p

    p2 = Proiect(1000, 1005, 'TEST 2', 3033, 'TEST echipa 2')
    repo.update(p2)
    rez = repo.read(1000)
    assert rez == p2

    repo.delete(1000)
    rez = repo.read(1000)
    assert rez is None
