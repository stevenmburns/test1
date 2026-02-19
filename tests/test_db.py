import pytest
from db import KeyValueStore


@pytest.fixture
def store():
    kv = KeyValueStore()
    yield kv
    kv.close()


def test_set_and_get(store):
    store.set("foo", "bar")
    assert store.get("foo") == "bar"


def test_get_missing_key(store):
    assert store.get("nonexistent") is None


def test_overwrite(store):
    store.set("key", "first")
    store.set("key", "second")
    assert store.get("key") == "second"


def test_delete(store):
    store.set("key", "value")
    store.delete("key")
    assert store.get("key") is None


def test_delete_nonexistent(store):
    store.delete("nonexistent")  # should not raise
