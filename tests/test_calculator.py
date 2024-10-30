"""Unit tests for the calculator module."""

import pytest
from example_python_package.calculator import add, divide, multiply, subtract


def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    """Test the subtract function."""
    assert subtract(3, 2) == 1
    assert subtract(3.5, 2.5) == 1.0


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(2.5, 3.5) == 8.75


def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(7.5, 2.5) == 3.0
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
