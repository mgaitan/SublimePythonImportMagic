import os

import pytest

from importmagic.index import SymbolIndex


@pytest.fixture(scope='session')
def index(request):
    directory = os.path.dirname(__file__)
    with open(os.path.join(directory, '..', 'testing', 'test_index.json')) as fd:
        return SymbolIndex.deserialize(fd)
