import pytest
from greet import greet


def test_greet_basic():
    assert greet("World") == "Hello, World!"


def test_greet_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_raises():
    with pytest.raises(ValueError):
        greet("")
