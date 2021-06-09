# test_addition.py

import pytest
from src.calculator import add, multiply, divide, subtract

def test_add():
    result = add(3, 4)
    assert result == 7

def test_multiply():
    result = multiply(3, 4)
    assert result == 12

def test_divide():
    result = divide(4, 2)
    assert result == 2

def test_subtract():
    result = subtract(4, 2)
    assert result == 2

def test_divide_2():
    result = divide(3, 2)
    assert result == 1.5

def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)