# test_addition.py

import pytest
from src.calculator import add, multiply

def test_add():
    result = add(3, 4)
    assert result == 7

def test_multiply():
    result = multiply(3, 4)
    assert result == 12

def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)