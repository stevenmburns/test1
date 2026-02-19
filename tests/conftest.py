import pytest
from db import KeyValueStore


@pytest.fixture
def store():
    kv = KeyValueStore()
    yield kv
    kv.close()
