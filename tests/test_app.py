"""Tests for app.py - now with multiplication!"""

from app import add, is_even, reverse_string, multiply


class TestMath:
    """Tests for math functions."""

    def test_add_positive(self):
        assert add(2, 3) == 5

    def test_add_negative(self):
        assert add(-1, -1) == -2

    def test_multiply_positive(self):
        # Multiplying two positive numbers
        assert multiply(5, 5) == 25

    def test_multiply_by_zero(self):
        # Multiplying by zero
        assert multiply(10, 0) == 0
        assert multiply(0, 0) == 0

    def test_multiply_negative(self):
        # Multiplying negative numbers
        assert multiply(-3, 4) == -12
        assert multiply(-2, -5) == 10

    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(3) is False


class TestStrings:
    """Tests for string functions."""

    def test_reverse(self):
        assert reverse_string("hello") == "olleh"