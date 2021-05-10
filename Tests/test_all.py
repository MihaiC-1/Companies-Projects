from Tests.test_firma import *
from Tests.test_proiect import *
from Tests.test_repo_firma import *
from Tests.test_repo_proiect import *


def test_all():
    test_getter_firma()
    test_getter_proiect()
    test_repo_firma()
    test_repo_proiect()
