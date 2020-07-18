import pytest
from model_bakery import baker

from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)
